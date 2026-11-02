# %% [markdown]
# # A short tour of PyTorch
#
# Run these seven code cells before the movie-review exercise if you want a
# refresher on tensors, views, devices, gradients, modules, and batches.
# This notebook needs only PyTorch. It downloads no dataset or model and runs
# entirely on CPU. The examples are deliberately small enough to inspect.

# %%
import importlib.util
import subprocess
import sys

if importlib.util.find_spec("torch") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch==2.15.0"])

import json
import platform
from pathlib import Path
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(17)
print(f"PyTorch {torch.__version__} | device: cpu")

# %% [markdown]
# ## A tensor has a shape and a data type
#
# Think of this tensor as three reviews, each represented by two numbers.
# Matrix multiplication can turn two input features into one output score.

# %%
features = torch.tensor([[1., 4.], [2., 1.], [3., 5.]])
weights = torch.tensor([[0.5], [-0.25]])
scores = features @ weights
print("shape:", tuple(features.shape), "dtype:", features.dtype)
print("first review:", features[0].tolist())
print("scores:", scores.flatten().tolist())
assert scores.shape == (3, 1)
torch.testing.assert_close(scores, torch.tensor([[-0.5], [0.75], [0.25]]))

# %% [markdown]
# ## A view can share data with its source
#
# A slice usually does not copy the selected values. Change the slice and its
# source changes too. A clone gives us independent values. A transpose changes
# how we walk through memory, so a tensor need not be contiguous.

# %%
values = torch.tensor([[1., 4.], [2., 1.], [3., 5.]])
row = values[1]
separate = row.clone()
row[0] = 9.
transposed = values.T
print("source row:", values[1].tolist(), "clone:", separate.tolist())
print("source stride:", values.stride(), "row offset:", row.storage_offset())
print("transpose:", tuple(transposed.shape), "contiguous:", transposed.is_contiguous())
assert values[1, 0].item() == 9. and separate[0].item() == 2.
assert transposed.stride() == (1, 2)

# %% [markdown]
# ## Put compatible tensors on the same device
#
# This CPU example changes precision. Moving to another device uses the same
# `.to(...)` method, but requires that device and a compatible installation.
# Integer class labels are different from floating-point model inputs.

# %%
precise = features.to(device="cpu", dtype=torch.float64)
labels = torch.tensor([0, 1, 0], dtype=torch.long)
print("inputs:", precise.device, precise.dtype)
print("labels:", labels.dtype)
assert features.dtype == torch.float32 and precise.dtype == torch.float64

# %% [markdown]
# ## Ask autograd which direction lowers the loss
#
# For one adjustable number `w`, let the loss be `w ** 2`. At `w = 2`, the
# derivative is 4. One SGD step with a learning rate of 0.1 takes us to 1.6.
# Predict the new loss before running the cell.

# %%
w = nn.Parameter(torch.tensor(2.))
optimizer = torch.optim.SGD([w], lr=0.1)
optimizer.zero_grad(set_to_none=True)
loss = w.square()
loss.backward()
print(f"before: w={w.item():.1f}, loss={loss.item():.2f}, gradient={w.grad.item():.1f}")
optimizer.step()
print(f"after:  w={w.item():.1f}, loss={w.square().item():.2f}")
torch.testing.assert_close(w.detach(), torch.tensor(1.6))

# %% [markdown]
# ## A module groups parameters and a forward calculation
#
# A linear layer with two inputs and two outputs has four weights and two
# biases. It returns two logits for each review. Cross-entropy takes logits
# and integer class labels, so do not add softmax before this loss.

# %%
torch.manual_seed(17)
head = nn.Linear(2, 2)
logits = head(features)
loss_fn = nn.CrossEntropyLoss()
classification_loss = loss_fn(logits, labels)
print("logits shape:", tuple(logits.shape))
print("trainable parameters:", sum(p.numel() for p in head.parameters()))
print("loss is a scalar:", classification_loss.ndim == 0)
assert logits.shape == (3, 2) and classification_loss.ndim == 0
assert sum(p.numel() for p in head.parameters()) == 6

# %% [markdown]
# ## Load a batch and take one real training step
#
# A DataLoader gives us corresponding inputs and labels. We clear gradients,
# predict, calculate the loss, backpropagate, and update the head. This is one
# step for learning the API, not an accuracy benchmark on a useful dataset.

# %%
loader = DataLoader(TensorDataset(features, labels), batch_size=2, shuffle=False)
batch_x, batch_y = next(iter(loader))
head.train()
before = head.weight.detach().clone()
optimizer = torch.optim.AdamW(head.parameters(), lr=0.01)
optimizer.zero_grad(set_to_none=True)
batch_loss = loss_fn(head(batch_x), batch_y)
batch_loss.backward()
optimizer.step()
head.eval()
with torch.no_grad():
    predictions = head(batch_x).argmax(dim=1)
changed = not torch.equal(before, head.weight.detach())
print("batch shapes:", tuple(batch_x.shape), tuple(batch_y.shape))
print("head weights changed:", changed)
print("predictions shape:", tuple(predictions.shape))
assert changed and predictions.shape == batch_y.shape

output = Path("outputs/fundamentals")
output.mkdir(parents=True, exist_ok=True)
results = {"python": platform.python_version(), "torch": torch.__version__,
           "device": "cpu", "tensor_scores": scores.flatten().tolist(),
           "view_and_clone_checked": True, "transpose_stride": list(transposed.stride()),
           "autograd_update_checked": True, "head_parameters": 6,
           "head_update_checked": changed, "batch_shapes": [list(batch_x.shape), list(batch_y.shape)]}
(output / "results.json").write_text(json.dumps(results, indent=2) + "\n")

# %% [markdown]
# Try changing one input dimension. Which weight shape must change with it?
# Explain why `head.eval()` does not replace `torch.no_grad()`, and why neither
# method is a substitute for choosing the parameters in an optimizer.
#
# References: [tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html),
# [autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html),
# [optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).
