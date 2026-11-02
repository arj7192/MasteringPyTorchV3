# %% [markdown]
# # Teach a small classifier to read movie reviews
#
# Does a reviewer sound pleased or disappointed? We will use a pretrained
# transformer to turn each review into a vector, then train a small PyTorch
# classifier on those vectors. The transformer stays frozen. We train 2,050
# parameters in the new head, not the transformer's roughly 600 million weights.
#
# This is feature extraction followed by supervised learning. It is not training
# an LLM from scratch or fine-tuning its backbone. You will see the complete
# PyTorch training loop: prediction, loss, gradients, and a parameter update.
#
# **Start here:** run the cells in order. `quick` uses 256 training, 64 validation,
# and 128 test reviews. The first run downloads about 1.2 GB of model weights.
# A CPU is supported; an available CUDA GPU or Apple MPS device is selected
# automatically. The measured results in the accompanying validation record
# describe the machines actually tested, not every hosted service.
#
# No API key, model access request, or paid inference service is needed.

# %%
# Install the small set of notebook dependencies in the current kernel.
# Keep an existing PyTorch installation, especially a hosted GPU build.
import importlib.util
import subprocess
import sys

if importlib.util.find_spec("torch") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch==2.15.0"])

required = {"transformers": "5.22.1", "datasets": "5.1.0", "matplotlib": "3.11.2"}
from importlib.metadata import version, PackageNotFoundError

to_install = []
for package, tested_version in required.items():
    try:
        installed = version(package)
    except PackageNotFoundError:
        installed = None
    if installed != tested_version:
        to_install.append(f"{package}=={tested_version}")
if to_install:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *to_install])

# %% [markdown]
# ## Choose a short run
#
# The language model has already learned useful representations. Our small
# dataset teaches the new head to turn those representations into two labels:
# `0` for negative and `1` for positive. Change `PROFILE` to `larger` later to
# train on more reviews. Keep the test set out of your model-selection decisions.

# %%
import copy
import hashlib
import json
import os
import platform
import random
import time
from pathlib import Path

import matplotlib
from IPython import get_ipython

if get_ipython() is None:
    matplotlib.use("Agg")  # Save plots without opening a window when run as a script.
else:
    get_ipython().run_line_magic("matplotlib", "inline")
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset
from datasets import Dataset, load_dataset
from transformers import AutoModel, AutoTokenizer

SEED = 17
PROFILE = os.environ.get("CH01_PROFILE", "quick")
SIZES = {"quick": (256, 64, 128), "larger": (1024, 256, 256)}[PROFILE]
MODEL_ID = "Qwen/Qwen3-Embedding-0.6B"
MODEL_REVISION = "97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3"
DATASET_ID = "cornell-movie-review-data/rotten_tomatoes"
DATASET_REVISION = "aa13bc287fa6fcab6daf52f0dfb9994269ffea28"
MAX_LENGTH = 96
INSTRUCTION = "Identify the sentiment of this movie review."
ENCODE_BATCH_SIZE = 8
EPOCHS = 30
OUTPUT = Path("outputs/review_classifier")
OUTPUT.mkdir(parents=True, exist_ok=True)

random.seed(SEED)
torch.manual_seed(SEED)
torch.set_num_threads(min(4, os.cpu_count() or 1))
requested_device = os.environ.get("CH01_DEVICE", "auto")
if requested_device == "auto":
    requested_device = "cuda" if torch.cuda.is_available() else (
        "mps" if torch.backends.mps.is_available() else "cpu"
    )
device = torch.device(requested_device)
print(f"PyTorch {torch.__version__} | device: {device} | profile: {PROFILE}")
print(f"Train / validation / test sizes: {SIZES}")
started = time.perf_counter()

# %% [markdown]
# ## Give each split a different job
#
# Training reviews supply the parameter updates. Validation reviews help us
# select a checkpoint. Test reviews are evaluated once after that selection.
# We sample the same number of positive and negative reviews in each split.
# We also remove repeated text across the selected splits.
#
# The dataset contains published movie-review snippets. We download it from its
# source at runtime. The notebook displays a training example and a few error
# snippets for inspection, rather than bundling the corpus. Its dataset card
# does not specify a license. This is a small teaching experiment on a familiar
# benchmark, not evidence that the model will work equally well on new products,
# languages, or customers. Pretraining overlap with this benchmark is unknown.

# %%
raw = load_dataset(DATASET_ID, revision=DATASET_REVISION, token=False)

def balanced_sample(split, size, seen):
    selected = {0: [], 1: []}
    for row in split.shuffle(seed=SEED):
        key = " ".join(row["text"].casefold().split())
        label = int(row["label"])
        if key in seen or len(selected[label]) == size // 2:
            continue
        selected[label].append({"text": row["text"], "label": label})
        seen.add(key)
        if sum(map(len, selected.values())) == size:
            break
    if sum(map(len, selected.values())) != size:
        raise ValueError("Not enough distinct reviews for the requested profile.")
    rows = selected[0] + selected[1]
    random.Random(SEED).shuffle(rows)
    return Dataset.from_list(rows)

seen = set()
train_rows, val_rows, test_rows = [
    balanced_sample(raw[name], size, seen)
    for name, size in zip(("train", "validation", "test"), SIZES)
]
for name, rows in zip(("train", "validation", "test"), (train_rows, val_rows, test_rows)):
    print(name, len(rows), {label: list(rows["label"]).count(label) for label in (0, 1)})
print("One training review:", train_rows[0])

# %% [markdown]
# ## Turn words into vectors
#
# A tokenizer converts text into token IDs. The transformer turns those IDs
# into context-dependent vectors. We use left padding, so the last position is
# a real token in every review, and take its vector as the review representation.
# The attention mask tells the model which positions are padding.
#
# `requires_grad_(False)` freezes the backbone. `eval()` disables training-only
# behavior such as dropout. Neither command replaces the other. The same frozen
# features can be reused for every epoch of head training.

# %%
load_started = time.perf_counter()
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID, revision=MODEL_REVISION, padding_side="left", token=False
)
encoder = AutoModel.from_pretrained(
    MODEL_ID, revision=MODEL_REVISION, dtype=torch.float32,
    attn_implementation="sdpa", token=False
).to(device)
encoder.requires_grad_(False)
encoder.eval()
backbone_versions = tuple(p._version for p in encoder.parameters())
model_load_seconds = time.perf_counter() - load_started
print(f"Frozen backbone parameters: {sum(p.numel() for p in encoder.parameters()):,}")
print(f"Model load and any required downloads: {model_load_seconds:.1f} seconds")

@torch.no_grad()
def encode_reviews(texts):
    vectors = []
    for start in range(0, len(texts), ENCODE_BATCH_SIZE):
        reviews = texts[start:start + ENCODE_BATCH_SIZE]
        prompts = [f"Instruct: {INSTRUCTION}\nQuery: {text}" for text in reviews]
        batch = tokenizer(prompts, padding=True, truncation=True,
                          max_length=MAX_LENGTH, return_tensors="pt").to(device)
        hidden = encoder(**batch, use_cache=False).last_hidden_state
        vectors.append(F.normalize(hidden[:, -1, :], dim=-1).cpu())
    return torch.cat(vectors)

feature_started = time.perf_counter()
train_x = encode_reviews(list(train_rows["text"]))
print("Encoded training reviews.")
val_x = encode_reviews(list(val_rows["text"]))
print("Encoded validation reviews.")
# Encoding text does not use its label. Test labels remain out of model selection.
test_x = encode_reviews(list(test_rows["text"]))
feature_seconds = time.perf_counter() - feature_started
train_y = torch.tensor(train_rows["label"], dtype=torch.long)
val_y = torch.tensor(val_rows["label"], dtype=torch.long)
test_y = torch.tensor(test_rows["label"], dtype=torch.long)
assert not train_x.requires_grad
assert torch.isfinite(train_x).all()
print("Feature tensor:", tuple(train_x.shape), train_x.dtype)
print(f"Feature extraction: {feature_seconds:.1f} seconds")

# %% [markdown]
# ## Inspect one prediction before teaching the head
#
# The head returns two **logits**, unnormalized scores. Cross-entropy takes
# logits directly, so we do not add a softmax before computing the loss.
# Softmax is useful later when displaying the head's probabilities.
#
# The head is deliberately trained on CPU. Once the features are extracted,
# this part is tiny and does not need an accelerator.

# %%
torch.manual_seed(SEED)
head = nn.Linear(train_x.shape[1], 2)
initial_weights = head.weight.detach().clone()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(head.parameters(), lr=0.02, weight_decay=0.01)
loader = DataLoader(TensorDataset(train_x, train_y), batch_size=32, shuffle=True,
                    generator=torch.Generator().manual_seed(SEED))

@torch.no_grad()
def evaluate(x, y):
    head.eval()
    logits = head(x)
    return loss_fn(logits, y).item(), (logits.argmax(1) == y).float().mean().item()

initial_train_loss, _ = evaluate(train_x, train_y)
initial_val_loss, initial_val_accuracy = evaluate(val_x, val_y)
print(f"Trainable head parameters: {sum(p.numel() for p in head.parameters()):,}")
print(f"Untrained validation accuracy: {initial_val_accuracy:.1%}")

# %% [markdown]
# ## The four operations that teach the head
#
# For each batch, we calculate predictions and a loss. `backward()` calculates
# gradients. `step()` uses those gradients to update the head. `zero_grad()`
# clears gradients from the previous batch so they do not accumulate by accident.
#
# Before running this cell, predict what should happen to the training loss.
# Does validation accuracy have to improve every epoch?

# %%
best_state = copy.deepcopy(head.state_dict())
best_val_loss = initial_val_loss
best_epoch = 0
history = []
training_started = time.perf_counter()
for epoch in range(1, EPOCHS + 1):
    head.train()
    total_loss = 0.0
    for features, labels in loader:
        optimizer.zero_grad(set_to_none=True)
        logits = head(features)
        loss = loss_fn(logits, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * len(labels)
    val_loss, val_accuracy = evaluate(val_x, val_y)
    history.append({"epoch": epoch, "train_loss": total_loss / len(train_y),
                    "val_loss": val_loss, "val_accuracy": val_accuracy})
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        best_state = copy.deepcopy(head.state_dict())
        best_epoch = epoch
    if epoch == 1 or epoch % 5 == 0:
        print(f"Epoch {epoch:2}: train loss {history[-1]['train_loss']:.3f}, "
              f"validation loss {val_loss:.3f}, accuracy {val_accuracy:.1%}")
training_seconds = time.perf_counter() - training_started
head.load_state_dict(best_state)
assert not torch.equal(initial_weights, head.weight.detach()), "The head did not update."
assert all(p.grad is None for p in encoder.parameters()), "The frozen backbone received gradients."
assert backbone_versions == tuple(p._version for p in encoder.parameters()), "Backbone weights changed."
print(f"Selected epoch {best_epoch} using validation loss only.")

# %% [markdown]
# ## Read the learning curve and evaluate the held-out reviews
#
# We now use the test labels once. Our sample is deliberately small, so a few
# changed predictions can noticeably change the percentage. Accuracy here is a
# useful lesson, not a new benchmark claim. The majority-label baseline is 50%
# because the selected test set contains equal numbers of both labels.

# %%
test_loss, test_accuracy = evaluate(test_x, test_y)
epochs = [row["epoch"] for row in history]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(epochs, [row["train_loss"] for row in history], label="Training loss")
ax.plot(epochs, [row["val_loss"] for row in history], label="Validation loss")
ax.axvline(best_epoch, color="gray", linestyle=":", label=f"Selected epoch {best_epoch}")
ax.set(xlabel="Epoch", ylabel="Cross-entropy loss", title="Only the classification head learns")
ax.legend()
fig.tight_layout()
fig.savefig(OUTPUT / "learning_curve.png", dpi=180)
plt.show()
print(f"Test accuracy: {test_accuracy:.1%} on {len(test_y)} held-out reviews")
print(f"Majority-label baseline: {max(torch.bincount(test_y)).item() / len(test_y):.1%}")
with torch.no_grad():
    predictions = head(test_x).argmax(1)
mistakes = (predictions != test_y).nonzero().flatten().tolist()
for index in mistakes[:3]:
    print({"text": test_rows[index]["text"], "predicted": int(predictions[index]),
           "actual": int(test_y[index])})

# %% [markdown]
# ## Try your own review
#
# These examples were written for this notebook. Change a phrase and predict
# whether its classification will change. Try negation, mixed opinions, and a
# review of something other than a movie. The probability is a model output;
# it is not a guarantee that the answer is correct or calibrated.

# %%
your_reviews = [
    "The performances were warm and the ending stayed with me all evening.",
    "The plot went nowhere and I wanted to leave halfway through.",
    "I expected to hate this film, but it won me over.",
    "Beautiful images, although the story was painfully dull.",
]
your_features = encode_reviews(your_reviews)
with torch.no_grad():
    probabilities = head(your_features).softmax(dim=1)
for text, probability in zip(your_reviews, probabilities):
    label = ("negative", "positive")[int(probability.argmax())]
    print(f"{label:8} | P(positive)={probability[1].item():.3f} | {text}")

# %% [markdown]
# ## Save the small head and the run record
#
# The checkpoint stores the head, the label meaning, and the exact backbone
# revision. Reloading it still requires the same backbone and preprocessing.
# We do not save or upload the dataset or a second copy of the pretrained model.

# %%
checkpoint = {"head_state_dict": head.state_dict(), "model_id": MODEL_ID,
              "model_revision": MODEL_REVISION, "max_length": MAX_LENGTH,
              "instruction": INSTRUCTION, "padding_side": "left",
              "pooling": "last_token", "normalize_features": True,
              "labels": ["negative", "positive"]}
torch.save(checkpoint, OUTPUT / "review_head.pt")
reloaded = nn.Linear(train_x.shape[1], 2)
reloaded.load_state_dict(torch.load(OUTPUT / "review_head.pt", weights_only=True)["head_state_dict"])
with torch.no_grad():
    torch.testing.assert_close(head(val_x), reloaded(val_x))

results = {
    "profile": PROFILE, "seed": SEED, "device": str(device),
    "python": platform.python_version(), "platform": platform.platform(),
    "versions": {name: version(name) for name in ("torch", "transformers", "datasets", "matplotlib")},
    "model_id": MODEL_ID, "model_revision": MODEL_REVISION,
    "dataset_id": DATASET_ID, "dataset_revision": DATASET_REVISION,
    "split_sizes": dict(zip(("train", "validation", "test"), SIZES)),
    "selected_texts_sha256": hashlib.sha256(json.dumps(
        [list(rows["text"]) for rows in (train_rows, val_rows, test_rows)],
        ensure_ascii=False).encode()).hexdigest(),
    "max_length": MAX_LENGTH, "backbone_dtype": "float32", "head_device": "cpu",
    "instruction": INSTRUCTION, "padding_side": "left", "pooling": "last_token",
    "backbone_parameters": sum(p.numel() for p in encoder.parameters()),
    "trainable_parameters": sum(p.numel() for p in head.parameters()),
    "initial_train_loss": initial_train_loss,
    "initial_validation_accuracy": initial_val_accuracy,
    "selected_epoch": best_epoch, "test_loss": test_loss, "test_accuracy": test_accuracy,
    "model_load_seconds_including_any_downloads": model_load_seconds,
    "feature_extraction_seconds": feature_seconds, "head_training_seconds": training_seconds,
    "total_seconds_excluding_setup": time.perf_counter() - started,
    "backbone_received_gradients": any(p.grad is not None for p in encoder.parameters()),
    "backbone_weights_unchanged": backbone_versions == tuple(p._version for p in encoder.parameters()),
    "checkpoint_roundtrip_passed": True, "history": history,
}
(OUTPUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
print("Saved the head, learning curve, and results in", OUTPUT)

# %% [markdown]
# ## Experiments to try
#
# 1. Change `PROFILE` to `larger`. Compare learning curves and extraction time.
# 2. Change the learning rate. Use validation loss to select a run; save the
#    test set for your final comparison rather than tuning against it.
# 3. Inspect the mistakes. Which reviews contain mixed opinions or sarcasm?
# 4. Remove feature normalization and rerun. Explain why the optimization changes.
#
# Sources: [model and usage](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B),
# [dataset](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes),
# [PyTorch training basics](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html).
# Model architecture and pooling follow the model's documented interface;
# the teaching workflow and explanations here are written for this chapter.
