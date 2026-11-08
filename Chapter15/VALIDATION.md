# Chapter 15 execution record

The pet prototype was executed end to end on 8 November 2026.

## Local CPU

All 16 code cells in the published notebook passed, producing three plot outputs. The final run used Python 3.12.14, PyTorch 2.15.0, and torchvision 0.29.2 on macOS arm64. A separate run in a fresh working directory also passed and built the image-feature cache from scratch. Model and dataset downloads were already cached locally.

The runs confirmed 216 distinct selected image hashes across the three splits, unchanged frozen encoder parameters with no gradients, validation-based experiment and checkpoint selection, matching logits after head reload, and descending numerical losses consistent with the probability assigned to each actual breed. Both Trainer and Lightning completed their training and checkpoint-recovery paths.

The selected main head correctly classified 72 of 72 test photographs. This is a small teaching selection, with unknown overlap with encoder pretraining, and is not a general performance claim.

## Fresh Google Colab CPU

The uploaded notebook completed all 16 cells in order, without cell errors, and produced three image outputs. The downloaded executed notebook was compared with the local sources. The run built its feature cache in approximately 197 seconds and completed the Trainer, Profiler, save/reload, and Lightning stages. Core execution required no GPU or model-access token.

After this hosted pass, one plot-title separator was changed from a vertical bar to a newline so the loss and probability labels do not overlap. The final notebook, including that display adjustment, passed another complete local run. No training, data, profiling, or numerical-loss code changed after the hosted pass.

CUDA, MPS, Windows, and other local Linux configurations have not been validated. Exact times vary with hardware, downloads, resource contention, and cache state. Profiler timings include recording overhead; the notebook measures elapsed time separately.

## Cell source fingerprints

These SHA-256 values cover ordered pairs of cell type and cell source, serialized as JSON, excluding outputs and execution metadata.

- Final published notebook, also executed locally: `9e3dc45f41c034a9eeffe5bde88df59906b6df7ef349e2304d86a4d29d375b59`.
- Colab-executed notebook before the plot-label line break: `e6b30f696ae91eabd81a6b3befe99e05a48d12bfc253b76c52a1d4efb98cf77d`.

Model and dataset revisions and the additional package versions are pinned in the notebook. Repository notebooks have their outputs and execution counts cleared. Executed copies, traces, and detailed run evidence are retained with the author’s review materials.
