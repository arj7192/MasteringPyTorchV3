# PyTorch / notebook validation summary : 3 Aug 2026

## Are we stuck?

**No, but the venv had drifted.** Requirements say torch 2.13; the active `.venv` was still on **torch 2.2.0** / torchvision 0.17, and a NumPy 2.4 install broke `tensor.numpy()` / DataLoader workers. That explains most of the scary Wave 1 reds, not "PyTorch is broken."

## Versions

| Package | requirements floor | What was in `.venv` during your re-run | Target after upgrade |
|---|---|---|---|
| torch | >=2.13.0 | **2.2.0** (stale) | 2.13.0 |
| torchvision | >=0.28.0 | 0.17.0 | 0.28.0 |
| numpy | >=1.26,<2.3 (pinned after re-run) | 2.4.6 during fail / 1.26.4 later | <2.3 |

## Your Wave 1 re-run (partial paste)

| Notebook | Result | Likely cause |
|---|---|---|
| Ch01 `mnist_pytorch` | fail @ train loop (~43s) | env / numpy↔torch ABI (upgrade torch) |
| Ch01 `pytorch2x_compile_demo` | fail @ MNIST load (~3s) | download/SSL or empty `Chapter01/data`; also env |
| Ch02 `lenet` | **timeout 600s** | CIFAR tar incomplete (~45 MB; full is ~170 MB). Delete and re-download |
| Ch02 `transfer_learning_alexnet` | fail @ `imageshow` (~5s) | `img.numpy()` under broken numpy/torch combo |
| Ch02 `vgg13_...` | fail @ visualize | same numpy ABI + DataLoader `num_workers=2` spawn; transformers also saw torch 2.2 |
| Ch02 ResNet / DenseNet / GoogLeNet | **pass** | pure tensor ops, no dataset/numpy bridge |
| Ch03 `rnn` | fail | missing `Chapter03/aclImdb/` |
| Ch03 `lstm` | fail | **`torchtext.legacy` removed** (real code debt) |
| Ch15 `fastai` | **pass** (~336s) | - |
| Ch15 `pytorch_lightning` | (still running in paste) | should be OK after earlier hook fix |

## Hard breaks (need author / data work)

1. **`torchtext.legacy`** - Ch03 `lstm.ipynb` (also Ch04 transformer, Ch07 text_generation)
2. **Missing IMDB** - Ch03 `rnn.ipynb` needs `aclImdb/`
3. **Incomplete CIFAR** - Ch02 `lenet.ipynb`

## Fix env, then re-run

```bash
cd /Users/ashish/code/MasteringPyTorchV3
source .venv/bin/activate
pip install -U 'torch>=2.13.0' 'torchvision>=0.28.0' 'numpy>=1.26,<2.3'
python -c "import torch,numpy,torchvision; print(torch.__version__, torchvision.__version__, numpy.__version__)"
# expect: 2.13.x  0.28.x  1.26.x or 2.2.x (not 2.4)

# CIFAR (lenet) - wipe partial and fetch full ~170MB
rm -f data/cifar-10-python.tar.gz
curl -L --retry 3 -o data/cifar-10-python.tar.gz \
  https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# optional extract; torchvision will also extract on download=True if root=../data or ./data matches

# IMDB (rnn) - only if you want that notebook green now
# curl -L -o /tmp/aclImdb_v1.tar.gz https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
# tar -xzf /tmp/aclImdb_v1.tar.gz -C Chapter03

python scripts/validate_notebooks.py --wave1 --timeout 600
```

**Expect after env + CIFAR:** architecture notebooks + Ch1 + alexnet/vgg + fastai/lightning/profiler/captum mostly green. Still red until rewritten: **Ch03 lstm**. Still red without IMDB: **Ch03 rnn**.
