# Chapter 17: PyTorch and Explainable AI

Two complete, independent exercises investigate fixed pretrained models. No Hugging Face account, access token, gated-model agreement, private data, or paid API is required. The chapter introduces sparse feature dictionaries and circuit tracing conceptually; it does not require a third model or feature-library installation.

1. **01_language_interventions.ipynb**: Qwen3.5-0.8B, supplied facts, explicit red-versus-blue next-token scores, word edits, embedding Integrated Gradients, actual block-output capture, activation replacement and controls.
2. **02_vision_attribution.ipynb**: SigLIP 2, image-text cosine contrasts, input gradients, Integrated Gradients with two references, equal-area masking with 20 random controls, alternative descriptions and representation neighbours.

## Running in Google Colab

Upload one notebook at https://colab.research.google.com/ and select a CPU runtime. Run all cells in order. Use a **fresh runtime for each notebook** so both models do not occupy memory together. Run the notebook installation cell rather than installing the local requirements file: setup keeps Colab's existing PyTorch and preloaded matplotlib, while installing the needed interpretation and model libraries. Model downloads can take longer than the computation. Public Hugging Face access works without a token; occasional download limits depend on the host.

## Running locally

Use a fresh Python environment (validation used Python 3.12 on macOS; the hosted language check used Python 3.13). Install requirements with `python -m pip install -r requirements.txt`, open JupyterLab and select that environment's kernel. Run each notebook in a fresh kernel. For accelerator-specific PyTorch builds, use the official installation selector at https://pytorch.org/get-started/locally/. These notebooks intentionally default to CPU and float32; GPU and MPS execution are not claimed as validated paths.

Allow several GB of free RAM and disk space. The language component has 752 million parameters and the full vision-language model 375 million. On the tested Colab CPU, the vision attribution cell took about 11 minutes; other machines and sessions can differ. First-time downloads are approximately 1.75 GB and 1.5 GB respectively; library caches can require additional disk space. Local measured process high-water memory and execution times are recorded in VALIDATION.md. Free hosted resources can vary.

## Reading and changing the experiments

The chapter contains selected excerpts; these notebooks include the imports, helpers, numerical checks and real plotting code. Keep the candidate answers, score, reference, model revision and intervention explicit when changing an example. The two candidate language words are checked to be single tokens. Prompt lengths and changed positions are checked before patching. Hooks are always removed. The first-name token before the edit and a same-input patch provide controls.

IG convergence residuals check numerical integration, not explanation correctness. A word with zero difference from the reference can have zero IG even if the model uses it. SigLIP cosine differences are not probabilities. A positive cat-minus-dog score on coffee is retained as a counterexample. SimilarityInfluence searches only the supplied pool and is not evidence of training-data causation.

Figures are generated from actual runs. Raw numerical evidence and figures are saved beneath `outputs/language/` and `outputs/vision/`; those folders and model caches should not be committed. The language checkpoint uses native PyTorch fallbacks for optional optimized sequence kernels on CPU. The warning indicates a slower implementation, not a need to install CUDA extensions.

See IMAGE_CREDITS.md for the three reusable example photographs and VALIDATION.md for the measured verification scope.

The neighbour exercise supplies a cosine helper that accepts a queried layer returned inside a one-item list, as well as a tensor. Its ranking and numerical values are checked against a direct PyTorch calculation. Some Transformers versions warn about unused SigLIP generation-token configuration fields; these exercises encode images and text and never ask SigLIP to generate text.

## Optional variations

After the main exercise, set `TRY_YELLOW_BADGE = True` in the language notebook or `TRY_BLACK_BASELINE = True` in the vision notebook and rerun just that optional cell. Each variation uses its own scores and leaves the main results intact.
