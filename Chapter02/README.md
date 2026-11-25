# Chapter 2 Deep CNN Architectures

Run the third-edition notebooks in chapter order, starting with a fresh CPU kernel for each one.

1. [LeNet on CIFAR-10](02_lenet_cifar10.ipynb) · [Open in Colab](https://colab.research.google.com/github/arj7192/MasteringPyTorchV3/blob/main/Chapter02/02_lenet_cifar10.ipynb). Train a small classifier, choose a checkpoint on the validation set, and inspect predictions on the test set.
2. [Inception, ResNet, and DenseNet blocks](03_cnn_blocks.ipynb) · [Open in Colab](https://colab.research.google.com/github/arj7192/MasteringPyTorchV3/blob/main/Chapter02/03_cnn_blocks.ipynb). Compare branches, shortcuts, and concatenation on the same input tensor.
3. [ConvNeXt](01_convnext.ipynb) · [Open in Colab](https://colab.research.google.com/github/arj7192/MasteringPyTorchV3/blob/main/Chapter02/01_convnext.ipynb). Follow a photo through a pretrained model, compare feature maps from two photos, and check a ConvNeXt V2 block.

## Setup

Use a standard CPU runtime in Colab. For local Jupyter, install [PyTorch and TorchVision](https://pytorch.org/get-started/locally/) and Matplotlib. The ConvNeXt setup cell installs its additional packages. On the first run, LeNet downloads the CIFAR-10 archive (about 163 MiB) and ConvNeXt downloads a public checkpoint (about 15 MB). The downloads use public links.

All three notebooks passed on local CPU. LeNet and the CNN blocks also passed on Colab CPU. The six-cell ConvNeXt walkthrough passed on Colab CPU before the locally tested two-photo comparison was added.

The other notebooks in this folder are examples from the second edition.
