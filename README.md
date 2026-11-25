# Mastering PyTorch, Third Edition

Companion code for *Mastering PyTorch, Third Edition* by Ashish Ranjan Jha (Packt, forthcoming).

This edition is in progress. Start with the [Chapter 1 notebooks and setup instructions](Chapter01/README.md). Tested third-edition examples are also available for [Chapter 2](Chapter02/README.md), [Chapter 15](Chapter15/README.md), and [Chapter 17](Chapter17/README.md).

## Chapter 1

The chapter introduces a PyTorch training workflow through movie-review classification. A frozen pretrained transformer supplies features, and a small classification head learns to distinguish positive and negative reviews.

1. [A short tour of PyTorch](Chapter01/00_pytorch_fundamentals.ipynb): tensors, storage, devices, gradients, modules, and batches.
2. [Teach a small classifier to read movie reviews](Chapter01/01_transformer_review_classifier.ipynb): prepare data, extract features, train and evaluate the head, try new reviews, and save and reload the model.

Both notebooks have been run on local CPU and in fresh Google Colab CPU sessions. See the [tested configurations and results](Chapter01/VALIDATION.md).

## Chapter 2

Train LeNet, compare Inception, ResNet, and DenseNet blocks, and follow two photographs through ConvNeXt. The [Chapter 2 guide](Chapter02/README.md) links to the notebooks in chapter order and covers CPU setup.

## Chapter 15

[Rapid prototyping with a pet-photo classifier](Chapter15/01_pet_prototype_trainer.ipynb) uses a frozen SigLIP 2 image encoder, a small trainable head, Transformers Trainer, PyTorch Profiler, and a short Lightning alternative. The [chapter guide](Chapter15/README.md) explains setup, downloads, saved outputs, and the [validation scope](Chapter15/VALIDATION.md).

## Running the examples

Each chapter provides its own setup instructions. You can upload a notebook to Google Colab or run it locally in Jupyter. The chapter guides explain dependencies, downloads, and tested runtimes.

The matching Python files provide the same cells in a format that is easy to review in Git. Generated model weights, downloaded datasets, and local run outputs are not included.

## Author

[Ashish Ranjan Jha](https://github.com/arj7192)

## License

Apache 2.0 (same as V2; will confirm with Packt before public release).
