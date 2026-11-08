# %% [markdown]
# # Rapid prototyping with a modern vision model
# We will teach a small classifier to distinguish six pet breeds, compare two
# experiments, inspect its predictions, and find where execution time goes.
# We will use PyTorch Image Models (timm), a library of pretrained vision models,
# to load SigLIP 2. SigLIP 2 learns visual representations from images and text;
# we will use only its image branch to turn each photograph into numerical features.
# Only our new classification head learns the six breed labels.
# The Trainer class in Hugging Face’s Transformers library will manage training,
# validation and checkpoints. Later, PyTorch Profiler will record where time goes,
# and PyTorch Lightning will give us an alternative way to organise the same loop.
# Run all cells in order in a fresh notebook. A CPU runtime is sufficient.

# %%
import importlib.metadata as metadata
import importlib.util
import subprocess
import sys

packages = {
    "timm": "1.0.30", "transformers": "5.22.1", "datasets": "5.1.0",
    "accelerate": "1.15.0", "matplotlib": "3.11.2", "safetensors": "0.8.0",
    "psutil": "7.2.2", "lightning": "2.6.6",
}
if importlib.util.find_spec("torch") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch==2.15.0"])
missing = []
for package, version in packages.items():
    try:
        installed = metadata.version(package)
    except metadata.PackageNotFoundError:
        installed = None
    if installed != version:
        missing.append(f"{package}=={version}")
if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
print("Dependencies ready. Keep the matching PyTorch/torchvision pair supplied by your runtime.")

# %% [markdown]
# ## Choosing a small, repeatable experiment
# We will use 16 training, 8 validation, and 12 test photographs for each breed.
# Validation guides our choices; test photographs stay aside until selection is
# complete. Increase these counts for a larger experiment after the short run.

# %%
import copy
import hashlib
import json
import os
import platform
import random
import statistics
import time
from pathlib import Path

if "ipykernel" not in sys.modules:
    import matplotlib
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12})
import numpy as np
import psutil
import timm
import torch
import torch.nn.functional as F
from datasets import load_dataset
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file, save_file
from transformers import Trainer, TrainingArguments, set_seed

SEED = 42
MODEL_ID = "timm/vit_base_patch16_siglip_224.v2_webli"
MODEL_REVISION = "4c3661e5ac879a276ddc5ddc6d3f0ecc78fd5d82"
DATA_ID = "timm/oxford-iiit-pet"
DATA_REVISION = "089695c834a7deb60505b7cc506672db1c31a6aa"
BREEDS = ["beagle", "bengal", "chihuahua", "persian", "pug", "siamese"]
COUNTS = {"train": 16, "validation": 8, "test": 12}
DEVICE = torch.device(os.environ.get("CH15_DEVICE", "cpu"))
OUT = Path("outputs/pet_prototype")
OUT.mkdir(parents=True, exist_ok=True)
set_seed(SEED)
torch.set_num_threads(min(4, os.cpu_count() or 1))
run_started = time.perf_counter()
print(f"Six breeds; device for image features: {DEVICE}")

def show_figure():
    if "ipykernel" in sys.modules:
        plt.show()
    else:
        plt.close()

# %%
data_started = time.perf_counter()
data = load_dataset(DATA_ID, revision=DATA_REVISION, token=False)
names = data["train"].features["label"].names
old_labels = {breed: names.index(breed) for breed in BREEDS}
rng = random.Random(SEED)
examples = {split: [] for split in COUNTS}
seen_pixels = set()

def add_examples(source, indices, split, breed, count):
    added = 0
    for index in indices:
        row = data[source][index]
        image = row["image"].convert("RGB")
        content = str(image.size).encode() + image.tobytes()
        pixel_hash = hashlib.sha256(content).hexdigest()
        if pixel_hash in seen_pixels:
            continue
        seen_pixels.add(pixel_hash)
        examples[split].append({
            "image": image, "label": BREEDS.index(breed), "breed": breed,
            "image_id": row["image_id"], "source_split": source,
            "source_index": int(index), "pixel_sha256": pixel_hash,
        })
        added += 1
        if added == count:
            return
    raise ValueError(f"Not enough unique images for {breed}/{split}.")

for breed in BREEDS:
    label = old_labels[breed]
    train_ids = [i for i, value in enumerate(data["train"]["label"]) if value == label]
    test_ids = [i for i, value in enumerate(data["test"]["label"]) if value == label]
    rng.shuffle(train_ids)
    rng.shuffle(test_ids)
    # seen_pixels also prevents a photograph from crossing the split boundaries.
    add_examples("train", train_ids, "train", breed, COUNTS["train"])
    add_examples("train", train_ids, "validation", breed, COUNTS["validation"])
    add_examples("test", test_ids, "test", breed, COUNTS["test"])

for split in examples:
    rng.shuffle(examples[split])
    print(f"{split}: {len(examples[split])} images, {COUNTS[split]} per breed")
manifest = {
    split: [{k: v for k, v in row.items() if k != "image"} for row in rows]
    for split, rows in examples.items()
}
(OUT / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
data_seconds = time.perf_counter() - data_started
assert len(seen_pixels) == sum(len(rows) for rows in examples.values())

# %% [markdown]
# These are small, balanced subsets of the Oxford-IIIT Pet dataset. Matching
# image hashes remove exact repeated RGB images across the selected splits.
# This does not detect every near-duplicate or establish what appeared in the
# encoder's pretraining data. Our exercise illustrates a workflow, not a new
# benchmark result for the encoder.

# %%
fig, axes = plt.subplots(2, 3, figsize=(7.2, 4.5))
for ax, breed in zip(axes.flat, BREEDS):
    row = next(row for row in examples["train"] if row["breed"] == breed)
    ax.imshow(row["image"])
    ax.set_title(breed.title(), fontsize=12, fontweight="bold")
    ax.axis("off")
fig.suptitle("Six breeds for our first prototype", fontsize=14, fontweight="bold", x=0.5)
fig.tight_layout()
fig.savefig(OUT / "pet_samples.png", dpi=220, bbox_inches="tight")
show_figure()

# %% [markdown]
# ## Loading the frozen image encoder
# SigLIP 2 has an image branch and a text branch, often called towers. During
# pretraining, these branches learn to represent related images and descriptions.
# Our checkpoint contains only the image branch, also called the image encoder.
# We do not download the text branch. The checkpoint supplies both learned weights and preprocessing
# settings. Freezing prevents parameter updates; eval() also fixes training-time
# behaviours such as dropout. Neither step trains a breed classifier for us.

# %%
model_started = time.perf_counter()
config_path = hf_hub_download(MODEL_ID, "config.json", revision=MODEL_REVISION, token=False)
weights_path = hf_hub_download(MODEL_ID, "model.safetensors", revision=MODEL_REVISION, token=False)
config = json.loads(Path(config_path).read_text())
encoder = timm.create_model(config["architecture"], pretrained=False,
                           num_classes=0, global_pool=config["global_pool"])
encoder.load_state_dict(load_file(weights_path), strict=True)
encoder.requires_grad_(False).eval().to(DEVICE)
preprocessing = config["pretrained_cfg"]
transform = timm.data.create_transform(
    input_size=tuple(preprocessing["input_size"]), is_training=False,
    interpolation=preprocessing["interpolation"], mean=tuple(preprocessing["mean"]),
    std=tuple(preprocessing["std"]), crop_pct=preprocessing["crop_pct"])

def parameters_digest(model):
    digest = hashlib.sha256()
    for name, value in model.state_dict().items():
        digest.update(name.encode())
        digest.update(value.detach().cpu().contiguous().numpy().tobytes())
    return digest.hexdigest()

encoder_digest_before = parameters_digest(encoder)
model_seconds = time.perf_counter() - model_started
print(f"Frozen encoder: {sum(p.numel() for p in encoder.parameters()):,} parameters")

# %% [markdown]
# ## Preparing features once
# Now that the encoder is loaded, we will run our selected photographs through it.
# Each image becomes a vector of 768 numbers. We will save these vectors in a
# cache, so trying another learning rate does not repeat the image processing.

# %%
identity = {"model": MODEL_ID, "revision": MODEL_REVISION,
            "dataset": DATA_ID, "dataset_revision": DATA_REVISION,
            "preprocessing": preprocessing, "breeds": BREEDS, "manifest": manifest,
            "feature_normalization": "L2", "dtype": "float32"}
cache_key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
cache_file = OUT / f"features_{cache_key}.pt"
feature_started = time.perf_counter()
cache_reused = cache_file.exists()

def encode_images(images):
    pixels = torch.stack([transform(image) for image in images]).to(DEVICE)
    with torch.inference_mode():
        values = F.normalize(encoder(pixels).float(), dim=-1)
    return values.cpu().clone()

if cache_reused:
    feature_data = torch.load(cache_file, map_location="cpu", weights_only=True)
else:
    feature_data = {}
    for split, rows in examples.items():
        batches = [encode_images([r["image"] for r in rows[i:i+4]])
                   for i in range(0, len(rows), 4)]
        feature_data[split] = {
            "features": torch.cat(batches),
            "labels": torch.tensor([row["label"] for row in rows]),
        }
    torch.save(feature_data, cache_file)
feature_seconds = time.perf_counter() - feature_started
for split, values in feature_data.items():
    assert values["features"].shape == (len(examples[split]), 768)
    assert torch.equal(values["labels"], torch.tensor([r["label"] for r in examples[split]]))
print(f"Features ready: {feature_data['train']['features'].shape[1]} values per image")
print(f"Cache reused: {cache_reused}; feature stage: {feature_seconds:.2f} seconds")

# %% [markdown]
# A cache is useful only while the encoder and image transformations stay fixed.
# Our key includes their settings and the selected photographs. Random crops,
# unfreezing the encoder, or changing the preprocessing require a new policy.
# We keep the feature extraction cost separate from the later training times.
# We are now ready to define a small PyTorch head. It maps each vector to six
# scores and returns a loss when labels are supplied. Trainer will use that loss.

# %%
class FeatureDataset(torch.utils.data.Dataset):
    def __init__(self, split):
        self.features = feature_data[split]["features"]
        self.labels = feature_data[split]["labels"]
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, index):
        return {"features": self.features[index], "labels": self.labels[index]}

class PetHead(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, len(BREEDS))
    def forward(self, features, labels=None):
        logits = self.linear(features)
        result = {"logits": logits}
        if labels is not None:
            result["loss"] = F.cross_entropy(logits, labels)
        return result

def accuracy_metric(prediction):
    predicted = prediction.predictions.argmax(axis=-1)
    return {"accuracy": float((predicted == prediction.label_ids).mean())}

print(f"Trainable head: {sum(p.numel() for p in PetHead().parameters()):,} parameters")

# %% [markdown]
# ## Comparing two training experiments
# The Trainer class from the Transformers library will handle batching,
# backpropagation, evaluation, and checkpointing.
# We still choose the model, data, loss, and experiment settings. Each run starts
# from the same initial head weights. We choose between learning rates using
# validation loss, then consult the held-out test set once.

# %%
set_seed(SEED)
initial_head = copy.deepcopy(PetHead().state_dict())
experiments = []
for learning_rate in [0.003, 0.03]:
    head = PetHead()
    head.load_state_dict(initial_head)
    arguments = TrainingArguments(
        output_dir=str(OUT / f"lr_{learning_rate}"), use_cpu=True,
        num_train_epochs=12, learning_rate=learning_rate,
        lr_scheduler_type="constant", weight_decay=0.01,
        per_device_train_batch_size=16, per_device_eval_batch_size=48,
        eval_strategy="epoch", save_strategy="epoch", logging_strategy="epoch",
        load_best_model_at_end=True, metric_for_best_model="eval_loss",
        greater_is_better=False, save_total_limit=1, report_to="none",
        seed=SEED, data_seed=SEED, disable_tqdm=True,
    )
    trainer = Trainer(model=head, args=arguments,
                      train_dataset=FeatureDataset("train"),
                      eval_dataset=FeatureDataset("validation"),
                      compute_metrics=accuracy_metric)
    fit_started = time.perf_counter()
    trainer.train()
    fit_seconds = time.perf_counter() - fit_started
    metrics = trainer.evaluate()
    experiments.append({"learning_rate": learning_rate,
                        "validation_loss": metrics["eval_loss"],
                        "validation_accuracy": metrics["eval_accuracy"],
                        "fit_seconds": fit_seconds,
                        "head_state": copy.deepcopy(head.state_dict()),
                        "history": copy.deepcopy(trainer.state.log_history),
                        "checkpoint": trainer.state.best_model_checkpoint})
    print(f"lr={learning_rate}: validation loss={metrics['eval_loss']:.4f}, "
          f"accuracy={metrics['eval_accuracy']:.1%}")
selected = min(experiments, key=lambda item: item["validation_loss"])
head = PetHead()
head.load_state_dict(selected["head_state"])
head.eval()
print(f"Selected learning rate: {selected['learning_rate']} (validation loss)")

# %% [markdown]
# Let us plot validation loss for both experiments. Lower loss means the head
# assigns more probability to the correct labels on these validation examples.
# We use these results, rather than test accuracy, to select our experiment.

# %%
fig, ax = plt.subplots(figsize=(7.2, 3.8))
for experiment in experiments:
    history = [row for row in experiment["history"] if "eval_loss" in row]
    # The final evaluate call may repeat the last epoch; plot epoch entries once.
    points = {row["epoch"]: row["eval_loss"] for row in history}
    ax.plot(list(points), list(points.values()), marker="o", markersize=3,
            label=f"Learning rate {experiment['learning_rate']}")
ax.set(title="Choose the experiment using validation loss", xlabel="Epoch", ylabel="Validation loss")
ax.title.set_fontweight("bold")
ax.legend()
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "validation_curves.png", dpi=220, bbox_inches="tight")
show_figure()

# %% [markdown]
# ## Evaluating the selected head
# We have selected the learning rate and checkpoint using validation data.
# Now we will consult the held-out test photographs and compare accuracy with
# a simple baseline that always predicts one breed.

# %%
with torch.inference_mode():
    test_logits = head(feature_data["test"]["features"])["logits"]
    test_probabilities = test_logits.softmax(dim=-1)
test_labels = feature_data["test"]["labels"]
predictions = test_logits.argmax(dim=-1)
test_correct = int((predictions == test_labels).sum())
test_accuracy = test_correct / len(test_labels)
losses = F.cross_entropy(test_logits, test_labels, reduction="none")
print(f"Test accuracy: {test_correct}/{len(test_labels)} ({test_accuracy:.1%})")
print(f"Constant-class baseline: {1 / len(BREEDS):.1%} on these balanced splits")

# %% [markdown]
# ## Looking at the predictions
# A high score does not show us every failure. We will inspect the highest-loss
# test examples after the final evaluation. Use validation images instead if you
# plan to change the model in response to what you see.

# %%
highest_loss = losses.argsort(descending=True)[:6].tolist()
highest_loss_records = []
fig, axes = plt.subplots(2, 3, figsize=(7.2, 6.1))
for ax, index in zip(axes.flat, highest_loss):
    row = examples["test"][index]
    predicted = int(predictions[index])
    loss_value = float(losses[index])
    p_actual = float(test_probabilities[index, row["label"]])
    highest_loss_records.append({
        "image_id": row["image_id"], "actual": row["breed"],
        "predicted": BREEDS[predicted], "loss": loss_value,
        "probability_of_actual_breed": p_actual,
    })
    print(f"{row['image_id']}: actual={row['breed']}, predicted={BREEDS[predicted]}, "
          f"loss={loss_value:.4f}, P(actual)={p_actual:.1%}")
    ax.imshow(row["image"])
    ax.set_title(f"Actual: {row['breed']}\nPredicted: {BREEDS[predicted]}\n"
                 f"Loss: {loss_value:.4f}\nP(actual): {p_actual:.1%}", fontsize=11,
                 color="#17665c" if predicted == row["label"] else "#a63b24")
    ax.axis("off")
fig.suptitle("Inspect the highest-loss test photographs", fontsize=14, fontweight="bold", x=0.5)
fig.tight_layout()
fig.savefig(OUT / "highest_loss_examples.png", dpi=220, bbox_inches="tight")
(OUT / "highest_loss_examples.json").write_text(json.dumps(highest_loss_records, indent=2) + "\n")
# Check both the ordering and the relationship between cross-entropy and P(actual).
assert all(a["loss"] >= b["loss"] for a, b in zip(highest_loss_records, highest_loss_records[1:]))
for row in highest_loss_records:
    assert abs(row["loss"] + np.log(row["probability_of_actual_breed"])) < 1e-5
show_figure()

# %% [markdown]
# ## Keeping the trained result
# We have inspected the predictions. Next we will save the head and its input
# settings, reload it into a fresh model, and check that its scores agree.
# The encoder must still be available to process a new photograph.

# %%
save_file({key: value.contiguous() for key, value in head.state_dict().items()},
          str(OUT / "pet_head.safetensors"))
head_config = {"model": MODEL_ID, "revision": MODEL_REVISION,
               "breeds": BREEDS, "preprocessing": preprocessing,
               "normalize_features": True, "feature_dimension": 768,
               "selected_learning_rate": selected["learning_rate"], "cache_key": cache_key}
(OUT / "pet_head.json").write_text(json.dumps(head_config, indent=2) + "\n")
reloaded = PetHead()
reloaded.load_state_dict(load_file(str(OUT / "pet_head.safetensors")))
reloaded.eval()
with torch.inference_mode():
    torch.testing.assert_close(reloaded(feature_data["test"]["features"])["logits"], test_logits)
assert parameters_digest(encoder) == encoder_digest_before
assert all(parameter.grad is None for parameter in encoder.parameters())
print("Reloaded head matches; the frozen encoder is unchanged and received no gradients.")

# %% [markdown]
# ## Finding the expensive work
# Predict which stage costs most: image preparation, the encoder, or our head.
# PyTorch Profiler, the operation recorder built into PyTorch, records CPU
# operations here. Separate repeated timings below
# measure elapsed time; profiler instrumentation is not a speed benchmark.

# %%
from torch.profiler import profile, ProfilerActivity, record_function
sample_images = [row["image"] for row in examples["validation"][:4]]
for _ in range(2):
    with torch.inference_mode():
        head(encode_images(sample_images))
activities = [ProfilerActivity.CPU]
if DEVICE.type == "cuda":
    activities.append(ProfilerActivity.CUDA)
with profile(activities=activities, record_shapes=True, profile_memory=True) as prof:
    with torch.inference_mode():
        with record_function("prepare_images"):
            batch_pixels = torch.stack([transform(image) for image in sample_images]).to(DEVICE)
        with record_function("image_encoder"):
            batch_features = F.normalize(encoder(batch_pixels).float(), dim=-1).cpu()
        with record_function("classification_head"):
            head(batch_features)
    if DEVICE.type == "cuda":
        torch.cuda.synchronize()
prof.export_chrome_trace(str(OUT / "pet_trace.json"))
print(prof.key_averages().table(sort_by="self_cpu_time_total", row_limit=8))
stage_times = {event.key: event.cpu_time_total / 1000 for event in prof.key_averages()
               if event.key in {"prepare_images", "image_encoder", "classification_head"}}
print("Labelled CPU regions (ms):", {k: round(v, 3) for k, v in stage_times.items()})

# %% [markdown]
# The operator table and the exported pet_trace.json show the recorded work.
# Open the trace in https://ui.perfetto.dev/ using Open trace file to explore it.
# Next we will time repeated calls without the profiler. This separates the cost
# of preparing and encoding new images from running the head on cached features.

# %%
def synchronize():
    if DEVICE.type == "cuda":
        torch.cuda.synchronize()
    elif DEVICE.type == "mps":
        torch.mps.synchronize()

def median_seconds(function, repeats=7):
    measurements = []
    for _ in range(repeats):
        synchronize()
        start = time.perf_counter()
        function()
        synchronize()
        measurements.append(time.perf_counter() - start)
    return statistics.median(measurements)

with torch.inference_mode():
    cached_sample = encode_images(sample_images)
    pipeline_seconds = median_seconds(lambda: head(encode_images(sample_images)))
    cached_head_seconds = median_seconds(lambda: head(cached_sample))
print(f"Four already-decoded images to logits: {pipeline_seconds * 1000:.3f} ms")
print(f"Head only on cached features: {cached_head_seconds * 1000:.3f} ms")
print("The second timing excludes image preparation and encoder work; it is not a faster image-to-logit service.")

# %% [markdown]
# ## A short Lightning alternative
# PyTorch Lightning is a training framework built around explicit PyTorch step
# methods. It leaves the training step in our own code and organises the surrounding
# loop. We will reuse the same cached features, initial head, and selected learning
# rate. This comparison uses validation data only; it does not reopen test selection.

# %%
import lightning as L
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.loggers import CSVLogger
from torch.utils.data import DataLoader

class LightningHead(L.LightningModule):
    def __init__(self, learning_rate=0.003):
        super().__init__()
        self.save_hyperparameters()
        self.head = PetHead()
    def training_step(self, batch, batch_index):
        result = self.head(**batch)
        self.log("train_loss", result["loss"], on_step=False, on_epoch=True,
                 batch_size=len(batch["labels"]))
        return result["loss"]
    def validation_step(self, batch, batch_index):
        result = self.head(**batch)
        correct = (result["logits"].argmax(-1) == batch["labels"]).float().mean()
        self.log("val_loss", result["loss"], batch_size=len(batch["labels"]))
        self.log("val_accuracy", correct, batch_size=len(batch["labels"]))
    def configure_optimizers(self):
        return torch.optim.AdamW(self.parameters(), lr=self.hparams.learning_rate,
                                 weight_decay=0.01)

L.seed_everything(SEED, workers=True)
lightning_model = LightningHead(selected["learning_rate"])
lightning_model.head.load_state_dict(initial_head)
checkpoint = ModelCheckpoint(monitor="val_loss", mode="min", save_top_k=1,
                             dirpath=str(OUT / "lightning/checkpoints"))
loop = L.Trainer(accelerator="cpu", devices=1, max_epochs=12,
                 logger=CSVLogger(str(OUT / "lightning"), name="pet_head"),
                 callbacks=[checkpoint], enable_progress_bar=False,
                 enable_model_summary=False, deterministic=True)
train_loader = DataLoader(FeatureDataset("train"), batch_size=16, shuffle=True,
                          generator=torch.Generator().manual_seed(SEED))
validation_loader = DataLoader(FeatureDataset("validation"), batch_size=48)
loop.fit(lightning_model, train_loader, validation_loader)
best_lightning = LightningHead.load_from_checkpoint(checkpoint.best_model_path,
                                                   map_location="cpu", weights_only=True)
lightning_metrics = loop.validate(best_lightning, validation_loader, verbose=False)[0]
print(f"Lightning validation accuracy: {lightning_metrics['val_accuracy']:.1%}")
print("Trainer and Lightning organise the loop differently; their defaults need not produce identical runs.")

# %% [markdown]
# ## Recording what we ran
# We now have a trained head, prediction plots, and a profiling trace. Save the
# settings and results alongside them so we can compare a later experiment.
# The memory value below is a sample at the end of the run, not peak memory.

# %%
versions = {name: metadata.version(name) for name in ["torch", "torchvision", *packages]}
result = {
    "model": MODEL_ID, "model_revision": MODEL_REVISION,
    "dataset": DATA_ID, "dataset_revision": DATA_REVISION,
    "seed": SEED, "device": str(DEVICE), "versions": versions,
    "python": platform.python_version(), "platform": platform.platform(),
    "encoder_parameters": sum(p.numel() for p in encoder.parameters()),
    "head_parameters": sum(p.numel() for p in head.parameters()),
    "split_counts": {split: len(rows) for split, rows in examples.items()},
    "unique_image_hashes": len(seen_pixels), "cache_key": cache_key,
    "cache_reused": cache_reused, "data_seconds": data_seconds,
    "model_seconds": model_seconds, "feature_seconds": feature_seconds,
    "experiments": [{k: v for k, v in item.items() if k not in {"head_state", "history"}}
                    for item in experiments],
    "selected_learning_rate": selected["learning_rate"],
    "test_correct": test_correct, "test_total": len(test_labels), "test_accuracy": test_accuracy,
    "encoder_unchanged": parameters_digest(encoder) == encoder_digest_before,
    "encoder_has_no_gradients": all(p.grad is None for p in encoder.parameters()),
    "head_reload_matches": True, "highest_loss_examples": highest_loss_records,
    "profile_cpu_region_ms": stage_times,
    "lightning_validation": lightning_metrics,
    "pipeline_four_images_seconds": pipeline_seconds,
    "cached_four_features_head_seconds": cached_head_seconds,
    "process_rss_at_end_bytes": psutil.Process().memory_info().rss,
    "elapsed_seconds": time.perf_counter() - run_started,
    "scope_note": "Small teaching subsets. Pretraining overlap unknown. RSS is an end-of-run process sample, not peak model memory.",
}
(OUT / "results.json").write_text(json.dumps(result, indent=2) + "\n")
print("Saved the head, split manifest, figures, profiling trace, and run record in", OUT)

# %% [markdown]
# ## Try another experiment
# 1. Inspect the highest-loss validation examples and propose one change.
#    Predict its effect before running it, even if all the labels are correct.
# 2. Increase the training photographs per breed and rebuild the cache.
# 3. Change the feature-extraction batch size and time the complete stage again.
# 4. Try a different pretrained encoder with its own preprocessing contract.
# Keep a fresh final test set if repeated experiments turn the current test
# photographs into part of your model-development process.
