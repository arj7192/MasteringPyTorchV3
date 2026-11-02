# Chapter 1: Overview of AI Using PyTorch

Start with the two notebooks below, in order. Run all cells from a fresh kernel. The notebook setup cells install the required dependencies while keeping an existing PyTorch installation.

| Notebook | What we do |
|---|---|
| [00_pytorch_fundamentals.ipynb](00_pytorch_fundamentals.ipynb) | Explore tensors, views, data types, devices, automatic differentiation, modules, and a training batch in seven short CPU cells. No model or dataset download is required. |
| [01_transformer_review_classifier.ipynb](01_transformer_review_classifier.ipynb) | Use a frozen Qwen3 embedding model to represent movie reviews, then train, evaluate, save, and reload a small PyTorch classification head. |

The `.py` files contain the same cells as the notebooks for readable code review. Repository notebooks have their outputs cleared; the chapter shows the recorded outputs, and the notebooks reproduce them when run.

## Run in Google Colab

Upload either `.ipynb` file to [Google Colab](https://colab.research.google.com/) and run its cells in order. The standard CPU runtime is sufficient for the tested quick profile. Download the notebook and any results you want to keep before ending a temporary session.

The review-classifier notebook downloads about 1.2 GB of model weights on its first run. It needs no API key, model access request, or paid inference service. The quick profile uses 256 training reviews, 64 validation reviews, and 128 test reviews. Its complete run took about nine minutes after setup on the tested Colab CPU, including the model download; timings vary with hardware and downloads.

## Run locally

The local CPU run used Python 3.12. Install the appropriate PyTorch build for your operating system and hardware, then install the remaining packages:

```bash
python -m pip install -r requirements-ch01.txt
```

Open the notebooks in Jupyter or your notebook editor. The first setup cell keeps an existing PyTorch installation. If it installs or replaces a package and asks for a kernel restart, restart the kernel before continuing.

The matching Python files can also run from this directory:

```bash
python 00_pytorch_fundamentals.py
python 01_transformer_review_classifier.py
```

The classifier selects an available CUDA, MPS, or CPU device for feature extraction. Only CPU execution has been validated so far. To use the validated path when running the script, set `CH01_DEVICE=cpu` in your environment. The small classification head always trains on CPU.

## Results and further experiments

The quick profile achieved 110 correct predictions out of 128 held-out reviews, or 85.9%, in both tested environments. It selected epoch 19 using validation loss, kept the transformer frozen, and passed the checkpoint reload check. These small-sample results illustrate the workflow and are not a general performance benchmark. See [VALIDATION.md](VALIDATION.md) for the tested configurations and source fingerprints.

The classifier saves its head, learning curve, and run settings under `outputs/review_classifier/`. These files are created when you run the notebook and are excluded from Git. Try the suggested changes near the end, including different reviews, learning rates, and the larger data profile. Use validation results to make choices and retain the test set for the final comparison.
