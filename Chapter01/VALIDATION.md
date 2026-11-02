# Chapter 1 execution record

The two current Chapter 1 notebooks were executed end to end on 31 October 2026. The cell sources published here match those runs. Saved outputs and execution metadata are cleared from the repository notebooks for easier review.

| Check | Local Apple Silicon CPU | Fresh Google Colab CPU |
|---|---|---|
| Python | 3.12.14 | 3.13.18 |
| PyTorch | 2.15.0 | 2.11.0+cpu |
| Foundations | All 7 code cells passed | All 7 code cells passed |
| Review classifier | All 9 code cells passed | All 9 code cells passed |
| Test predictions | 110/128 correct (85.9%) | 110/128 correct (85.9%) |
| Checkpoint selected by validation loss | Epoch 19 | Epoch 19 |
| Transformer frozen and unchanged | Passed | Passed |
| Saved head reloads with matching logits | Passed | Passed |

The classifier used Transformers 5.22.1, Datasets 5.1.0, and Matplotlib 3.11.2 in both environments. The model and dataset revisions are pinned in the notebook.

The local classifier notebook ran in about 39 seconds with downloads already cached. The Colab run took about nine minutes after setup, including the first model download. These timings describe the tested runs, not a promise for other machines.

Some rich outputs did not display in the Colab browser after a JavaScript login/cookie warning. All code cells completed, and the downloaded executed notebook and saved results confirmed successful computation. Reader-facing rich-output display still needs a separate check. CUDA, MPS, Windows, and other local Linux configurations have not been validated.

## Cell source fingerprints

These SHA-256 values cover the ordered pairs of cell type and cell source, serialized as JSON. They exclude outputs and execution metadata.

| Notebook | SHA-256 |
|---|---|
| `00_pytorch_fundamentals.ipynb` | `1246e1c0fb4a6b63dec64db4437f701107c93917d3ef64eee5745bd85540b28a` |
| `01_transformer_review_classifier.ipynb` | `e6f95c69461c77a44baf3846b9fbcf36daa1748988880406a785034ab6c9d323` |
