# Chapter 3 Deep Recurrent Model Architectures

Run these notebooks in chapter order, with a fresh CPU runtime for each one.

1. [Following a recurrent state through a sequence](01_recurrent_state.ipynb) · [Open in Colab](https://colab.research.google.com/github/arj7192/MasteringPyTorchV3/blob/main/Chapter03/01_recurrent_state.ipynb). Trace a one-number state, change the order of the words, and compare carrying the state with resetting it.
2. [Training recurrent classifiers on IMDb](02_imdb_recurrent_models.ipynb) · [Open in Colab](https://colab.research.google.com/github/arj7192/MasteringPyTorchV3/blob/main/Chapter03/02_imdb_recurrent_models.ipynb). Train an RNN, a bidirectional LSTM, and a GRU on the same review splits. Compare their test results and see how changing the order affects the scores.

## Setup

Select a CPU runtime in Colab and run all cells in order. For local Jupyter, install [PyTorch](https://pytorch.org/get-started/locally/) in the environment used by the notebook kernel. The first notebook only needs PyTorch. The IMDb notebook's setup cell installs its additional packages. Its first run downloads about 42 MB of public data without a Hugging Face account or token. It saves the two plots in `outputs/`.

Both notebooks completed successfully on local and Colab CPUs.

The other notebooks in this folder are examples from the second edition.
