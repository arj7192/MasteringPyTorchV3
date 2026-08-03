# PyTorch / notebook validation summary : 3 Aug 2026

## Are we stuck?

**No.** Environment is healthy. We were blocked briefly by (1) macOS SSL certs for dataset downloads and (2) a very slow CIFAR-10 fetch - not by PyTorch itself.

## Versions installed (`.venv`)

| Package | Installed |
|---|---|
| **torch** | **2.13.0** (latest) |
| **torchvision** | **0.28.0** (latest) |
| transformers | 5.14.1 |
| datasets | 5.0.1 |
| captum | 0.9.0 |
| pytorch-lightning | 2.6.5 |
| fastai | 2.8.8 |

`requirements.txt` and `requirements-core.txt` floored to these.

Smoke test (just now): MNIST loads, `torch.compile` works.

## Wave 1 execution results (first pass)

| Notebook | Result | Root cause |
|---|---|---|
| Ch02 ResNetBlock / DenseNetBlock / GoogLeNet | ✅ pass | - |
| Ch01 mnist_pytorch / compile_demo | ❌ then env-fixed | SSL cert on MNIST download (fixed via certifi) |
| Ch02 alexnet / vgg13 | ❌ then data-fixed | missing `hymenoptera_data` (now downloaded) |
| Ch02 lenet | ❌ | CIFAR-10 download incomplete (partial tar in `data/`) |
| Ch03 rnn | ❌ | missing local `aclImdb/` |
| Ch03 lstm | ❌ | **`torchtext.legacy` gone** - needs HF Datasets rewrite (Ashish) |
| Ch15 lightning | ❌ then code-fixed | `validation_epoch_end` removed in PL 2.0 (notebook updated) |
| Ch15 fastai / profiler, Ch17 captum | ❌ | same SSL/MNIST path issue (should pass on re-run) |

**Score first automated run:** 3/15 pass. After SSL + hymenoptera + Lightning fix, most of the rest should pass on re-run except Ch03 lstm (API rewrite) and anything needing full CIFAR/IMDB.

## Hard breaks that need author work (not env)

1. **`torchtext.legacy`** - Ch03 `lstm.ipynb`, also Ch04 `transformer.ipynb`, Ch07 `text_generation.ipynb`
2. **`import gym`** - Ch11 `pong.ipynb` → `gymnasium`
3. **Lightning hooks** - fixed in Ch15; scan other PL notebooks if any
4. **Missing datasets** - CIFAR (lenet), IMDB (rnn), chapter-specific assets

## How to re-run Wave 1 cleanly

```bash
cd /Users/ashish/code/MasteringPyTorchV3
source .venv/bin/activate
# finish CIFAR once (optional, for lenet):
# curl -L -o data/cifar-10-python.tar.gz https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# tar -xzf data/cifar-10-python.tar.gz -C data
python scripts/validate_notebooks.py --wave1 --timeout 600
```

## All 41 notebooks

Not fully executed yet. Static scan (`scripts/scan_deprecated.py`) shows the real API debt is concentrated in torchtext/gym notebooks; many `.data` hits are noisy false positives.

**Next cheapest validation win:** re-run Wave 1 with SSL helper (already in script) - expect ~10–12/15 green, with Ch03 lstm + maybe lenet/rnn still red until data/API migration.
