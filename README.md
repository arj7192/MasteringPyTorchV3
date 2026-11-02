# Mastering PyTorch, Third Edition

Companion code for *Mastering PyTorch, Third Edition* by Ashish Ranjan Jha (Packt, forthcoming).

This edition is in progress. Start with the [Chapter 1 notebooks and setup instructions](Chapter01/README.md). Other chapter folders contain earlier examples that are being revised; they should not yet be treated as validated third-edition code.

## Chapter 1

The chapter introduces a PyTorch training workflow through movie-review classification. A frozen pretrained transformer supplies features, and a small classification head learns to distinguish positive and negative reviews.

1. [A short tour of PyTorch](Chapter01/00_pytorch_fundamentals.ipynb): tensors, storage, devices, gradients, modules, and batches.
2. [Teach a small classifier to read movie reviews](Chapter01/01_transformer_review_classifier.ipynb): prepare data, extract features, train and evaluate the head, try new reviews, and save and reload the model.

Both notebooks have been run on local CPU and in fresh Google Colab CPU sessions. See the [tested configurations and results](Chapter01/VALIDATION.md).

## Running the examples

Each chapter provides its own setup instructions. For Chapter 1, the notebooks include dependency installation cells and can run on CPU. You can upload a notebook to Google Colab or run it locally in Jupyter. The [Chapter 1 guide](Chapter01/README.md) explains the download size, expected outputs, and local setup.

The matching Python files provide the same cells in a format that is easy to review in Git. Generated model weights, downloaded datasets, and local run outputs are not included.

## Author

[Ashish Ranjan Jha](https://github.com/arj7192)

## License

Apache 2.0 (same as V2; will confirm with Packt before public release).
