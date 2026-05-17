# Mastering PyTorch 2E → 3E — Per-chapter change log

This document accompanies `OUTLINE_E3.md`. It is the editor-facing rationale doc: what changes in each chapter, why, and what stays.

Tags: 🟧 update · 🟩 new · 🟥 remove.

Chapter numbers below are **E3 numbers**. Where the chapter moved from an E2 slot, the old number is shown in parentheses.

---

### Ch 1 — Overview of Deep Learning Using PyTorch  *(was Ch 1)*
- 🟧 Refresh all PyTorch 2.x API usage; remove TF parity table or trim to a paragraph (TF is no longer the relevant comparison in 2026)
- 🟩 New section: *What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI* (per editorial board)
- 🟩 New one-page "Responsible AI primer" pointer to Ch 21

### Ch 2 — Deep CNN Architectures  *(was Ch 2)*
- 🟧 All code re-run on PyTorch 2.x; replace deprecated `torchvision.models` weights API with the modern enum API
- 🟩 Short coverage of **ConvNeXt v2**
- 🟩 One paragraph framing CNNs in the GenAI era (UNet backbones, ConvNeXt in vision transformers, etc.)

### Ch 3 — Combining CNNs and LSTMs  *(was Ch 3)*
- 🟧 Code refresh, modern tokenizers (e.g. HF tokenizers) for MS-COCO captions
- 🟩 Pointer/teaser to Ch 6 multimodal models as the modern successor

### Ch 4 — Deep Recurrent Model Architectures  *(was Ch 4)*
- 🟧 Code refresh on PyTorch 2.x
- 🟧 IMDB pipeline updated to use `torchtext` 0.18+ replacement or HF Datasets equivalent (legacy `torchtext` APIs were deprecated)
- 🟧 Trim attention coverage — it now lives in Ch 5

### Ch 5 — Transformers  *(was Ch 5: Advanced Hybrid Models)*
- 🟧 Transformer language modeling example refreshed; better correspondence with HF `transformers` internals
- 🟩 Heavy new section: **Vision Transformers** (ViT, Swin, DINO v2) — addresses the most-requested addition for E3
- 🟥 Remove **RandWireNN** (dated, low ROI; readers wanting NAS go to Ch 17)

### Ch 6 — Advanced Multimodal Models  *(NEW chapter slot in 3E)*
- 🟩 Entire chapter is new content area for the book
- 🟩 CLIP, FLAVA, BLIP-2, LLaVA overview
- 🟩 Worked example: fine-tune or zero-shot use of a CLIP-family model on a downstream task
- 🟩 Image captioning re-done with a modern vision-language model

### Ch 7 — Graph Neural Networks  *(was Ch 6)*
- 🟧 GCN/GAT/GraphSAGE code refresh on PyG latest
- 🟩 Heavy new section: **Graph Transformers** (Graphormer, GraphGPS)
- 🟩 Responsible AI callout on graph fairness

### Ch 8 — Music and Text Generation with PyTorch  *(was Ch 7)*
- 🟧 Code refresh
- 🟧 Swap **GPT-2/3 examples** for **Llama 3 / Qwen / Mistral** (open weights, stable over print lifetime)
- 🟩 **Speculative decoding** as a decoding strategy
- 🟩 **MusicGen** as the headline music generation example; the LSTM MIDI generator stays as a smaller educational baseline
- 🟥 Remove the OpenAI-API GPT-3 notebook (closed model + flaky over time)
- 🟩 Responsible AI callout: watermarking and licensing

### Ch 9 — Fine-tuning LLMs  *(NEW; replaces 2E Ch 8 Neural Style Transfer)*
- 🟥 Remove the standalone Neural Style Transfer chapter — folded into Ch 10 if at all (a one-pager)
- 🟩 Entirely new chapter:
  - Loading open-weight LLMs
  - Parameter-Efficient Fine-Tuning (LoRA, QLoRA, IA³, adapters)
  - Hands-on LoRA on a single GPU
  - DPO as lightweight alternative to RLHF
  - RAG with PyTorch and a vector store
- 🟩 Responsible AI callout: data provenance and model cards

### Ch 10 — Deep Convolutional GANs  *(was Ch 9)*
- 🟧 Generator/discriminator and DCGAN training refreshed
- 🟧 pix2pix updated
- 🟩 New section: **where GANs still win vs diffusion** (small data, real-time inference, edge)
- 🟩 Optional one-pager folding Neural Style Transfer in as a historical bridge to GANs

### Ch 11 — Image Generation Using Diffusion  *(was Ch 10)*
- 🟧 From-scratch diffusion code refreshed on PyTorch 2.x + `diffusers` latest
- 🟩 **Stable Diffusion XL** replaces SD v1.5 as the headline text-to-image example
- 🟩 **ControlNet** for conditional generation
- 🟩 Short note on **video diffusion** (Stable Video Diffusion / similar) — landscape coverage only
- 🟩 Responsible AI callout: deepfakes and watermarking

### Ch 12 — Deep Reinforcement Learning  *(was Ch 11)*
- 🟧 DQN/Pong example refreshed; migrate from legacy `gym` to `gymnasium`
- 🟩 **RLHF in LLMs** using `trl` + PyTorch (focused walkthrough, not a deep PPO derivation)
- 🟩 **DPO** as the modern RLHF alternative (cross-link with Ch 9)
- 🟩 Responsible AI callout: reward hacking and alignment

### Ch 13 — Model Training Optimizations  *(was Ch 12)*
- 🟧 Distributed training and AMP sections refreshed
- 🟩 **FSDP / FSDP 2** for large-model training on commodity GPUs
- 🟩 **`torch.distributed.checkpoint`** for resumable training
- 🟩 **`torch.compile`** integration patterns and gotchas
- 🟩 Efficient AI callout: throughput per watt

### Ch 14 — Operationalizing PyTorch Models into Production  *(was Ch 13)*
- 🟧 Refresh model serving sections (Flask, microservice, TorchServe)
- 🟧 Refresh TorchScript and ONNX content
- 🟧 Refresh cloud sections (AWS / GCP / Azure)
- 🟩 **vLLM** for high-throughput LLM serving
- 🟩 **AOTInductor** for ahead-of-time compiled inference
- 🟩 **DeepSpeed-Inference** for multi-GPU LLM serving
- 🟩 Responsible AI callout: observability and guardrails

### Ch 15 — PyTorch on Mobile and Edge Devices  *(was Ch 14)*
- 🟧 Android and iOS sections refreshed
- 🟩 **ExecuTorch** as the modern on-device runtime (replaces legacy `torch.mobile`)
- 🟩 **PyTorch Edge** overview; refreshed Jetson workflow

### Ch 16 — Rapid Prototyping with PyTorch  *(was Ch 15)*
- 🟧 fast.ai, PyTorch Lightning, PyTorch Profiler sections refreshed
- 🟥 Drop the `poutyne` notebook (low industry traction, redundant with Lightning)

### Ch 17 — PyTorch and AutoML  *(was Ch 16)*
- 🟧 AutoML / NAS overview refreshed
- 🟧 Optuna content refreshed
- 🟩 Add **AutoGluon** and **AutoKeras** comparison (per Nov 2025 plan update)

### Ch 18 — PyTorch and Explainable AI  *(was Ch 17)*
- 🟧 Captum content refreshed (incl. `SimilarityInfluence`)
- 🟩 New short section: **interpretability for LLMs** (attention attribution, simple probing classifiers)

### Ch 19 — Recommendation Systems with PyTorch  *(was Ch 18)*
- 🟧 EmbeddingNet/MovieLens baseline refreshed
- 🟩 **TorchRec** for production-scale recsys
- 🟩 Shared embeddings and large embedding tables

### Ch 20 — PyTorch and Hugging Face  *(was Ch 19)*
- 🟧 Refresh all sections to latest HF APIs
- 🟩 Modern model coverage (Llama 3, Qwen, Mistral, SDXL, Whisper v3)

### Ch 21 — Responsible and Efficient AI with PyTorch  *(NEW)*
- 🟩 Entire chapter is new — anchors the recurring "Responsible AI Notes" callouts across the book
- 🟩 Bias detection, privacy (Opacus DP-SGD), robustness, watermarking, energy/efficiency, QAT, sparsity, a shippable checklist

---

## Chapters dropped from E2

- **Old Ch 8 — Neural Style Transfer**: dropped as standalone; optionally folded as a one-pager in Ch 10
- **2E Ch 5 sub-section — RandWireNN**: dropped; covered indirectly in Ch 17 (AutoML/NAS)
- **2E Ch 7 — GPT-3 (OpenAI API) text generation notebook**: dropped; replaced by open-weight LLM examples
- **2E Ch 15 — `poutyne` notebook**: dropped

## Notebooks that need to be written from scratch (estimated)

| Chapter | Notebook(s) |
|---|---|
| Ch 1  | `pytorch2x_compile_demo.ipynb` |
| Ch 2  | `convnext_v2.ipynb` |
| Ch 5  | `vision_transformer.ipynb` (heavy) |
| Ch 6  | `clip_finetune.ipynb`, `multimodal_captioning.ipynb` |
| Ch 7  | `graph_transformer.ipynb` |
| Ch 8  | `llama3_text_generation.ipynb`, `musicgen.ipynb`, `speculative_decoding.ipynb` |
| Ch 9  | `peft_overview.ipynb`, `lora_finetuning.ipynb`, `dpo_quickstart.ipynb`, `rag_with_pytorch.ipynb` |
| Ch 11 | `sdxl_text_to_image.ipynb`, `controlnet.ipynb` |
| Ch 12 | `rlhf_trl.ipynb`, `dpo_for_llms.ipynb` |
| Ch 13 | `fsdp_training.py`, `torch_compile_patterns.ipynb`, `distributed_checkpoint.py` |
| Ch 14 | `vllm_serving.ipynb`, `aotinductor_export.ipynb`, `deepspeed_inference.ipynb` |
| Ch 15 | `executorch_export.ipynb`, `pytorch_edge_jetson.md` |
| Ch 17 | `autogluon_pytorch.ipynb`, `autokeras_compare.ipynb` |
| Ch 18 | `llm_interpretability.ipynb` |
| Ch 19 | `torchrec_basic.ipynb`, `shared_embeddings.ipynb` |
| Ch 20 | refreshed HF notebooks |
| Ch 21 | `opacus_dp_sgd.ipynb`, `watermarking_text.ipynb`, `watermarking_image.ipynb`, `quantization_aware_training.ipynb` |
