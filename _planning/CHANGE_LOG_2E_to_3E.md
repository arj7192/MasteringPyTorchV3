# Mastering PyTorch 2E → 3E : Per-chapter change log

This document accompanies `OUTLINE_E3.md`. It is the editor-facing rationale doc: what changes in each chapter, why, and what stays.

Tags: 🟧 update · 🟩 new · 🟥 remove.

**Chapter numbering matches the Packt schedule of 27 Oct 2025 (accepted via my reply on 2 Nov 2025).** Where the chapter moved from a different E2 slot, the E2 number is shown in parentheses.

E3 has **19 chapters**, matching the agreed Packt schedule. Per Packt's 20 May 2026 guidance, the Responsible & Efficient AI coverage requested by the editorial board is now embedded contextually across the relevant chapters rather than as a standalone chapter.

---

### Ch 1 : Overview of Deep Learning Using PyTorch *(was E2 Ch 1)*
- 🟧 Refresh all PyTorch 2.x API usage; remove TF parity table or trim to a paragraph (TF is no longer the relevant comparison in 2026)
- 🟩 New section: *What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI* (per editorial board)
- 🟩 New one-page "Responsible AI primer" framing the distributed Responsible/Efficient AI thread readers will see across Ch 6, 7, 8, 10, 11, 12, 13, 14

### Ch 2 : Deep CNN Architectures *(was E2 Ch 2)*
- 🟧 All code re-run on PyTorch 2.x; replace deprecated `torchvision.models` weights API with the modern enum API
- 🟩 Short coverage of **ConvNeXt v2**
- 🟩 One paragraph framing CNNs in the GenAI era (UNet backbones, ConvNeXt in vision transformers, etc.)

### Ch 3 : Deep Recurrent Model Architectures *(was E2 Ch 4)*
- 🟧 Code refresh on PyTorch 2.x
- 🟧 IMDB pipeline updated to use `torchtext` 0.18+ replacement or HF Datasets equivalent (legacy `torchtext` APIs were deprecated)
- 🟧 Trim attention coverage - it now lives in Ch 4
- 🟥 *(E2 Ch 3 - "Combining CNNs and LSTMs" - is dropped from E3 as a standalone chapter; image captioning moves to the new multimodal chapter (Ch 5))*

### Ch 4 : Transformers *(was E2 Ch 5: Advanced Hybrid Models)*
- 🟧 Transformer language modeling example refreshed; better correspondence with HF `transformers` internals
- 🟩 Heavy new section: **Vision Transformers** (ViT, Swin, DINO v2) - addresses the most-requested addition for E3
- 🟥 Remove **RandWireNN** (dated, low ROI; readers wanting NAS go to Ch 16)

### Ch 5 : Advanced Multimodal Models *(NEW chapter slot in 3E)*
- 🟩 Entire chapter is new content area for the book
- 🟩 CLIP, FLAVA, BLIP-2, LLaVA overview
- 🟩 Worked example: fine-tune or zero-shot use of a CLIP-family model on a downstream task
- 🟩 Image captioning re-done with a modern vision-language model (supersedes the E2 CNN+LSTM captioning example)

### Ch 6 : Graph Neural Networks *(was E2 Ch 6)*
- 🟧 GCN/GAT/GraphSAGE code refresh on PyG latest
- 🟩 Heavy new section: **Graph Transformers** (Graphormer, GraphGPS)
- 🟩 **Responsible AI section: fairness in graph models** - measuring and mitigating disparate impact on node-classification / link-prediction, brief fairness-aware GNN training (per Packt 20 May guidance: distributed Responsible AI coverage)

### Ch 7 : Music and Text Generation with PyTorch *(was E2 Ch 7)*
- 🟧 Code refresh
- 🟧 Swap **GPT-2/3 examples** for **Llama 3 as the headline open-weight LLM**, with lighter comparative references to **Qwen 2.5** and **Mistral** (per Packt 20 May guidance)
- 🟩 **Speculative decoding** as a decoding strategy
- 🟩 **MusicGen** as the headline music generation example; the LSTM MIDI generator stays as a smaller educational baseline
- 🟥 Remove the OpenAI-API GPT-3 notebook (closed model + flaky over time)
- 🟩 **Responsible AI section: text watermarking + licensing** - hands-on text watermarking (e.g. Kirchenbauer-style scheme), attribution, dataset licensing for the open-weight examples

### Ch 8 : Fine-tuning LLMs *(NEW; replaces E2 Ch 8 Neural Style Transfer per Packt 20 May guidance)*
- 🟥 Remove the standalone Neural Style Transfer chapter - folded into Ch 9 as a short historical section
- 🟩 Entirely new chapter, anchored on **Llama 3** with comparative notes on Qwen 2.5 and Mistral:
 - Loading open-weight LLMs
 - Parameter-Efficient Fine-Tuning (LoRA, QLoRA, IA³, adapters)
 - Hands-on LoRA on Llama 3 on a single GPU
 - DPO as lightweight alternative to RLHF
 - RAG with PyTorch and a vector store
- 🟩 **Responsible AI section: provenance, model cards, bias evaluation** - training-data provenance, writing a model card for the fine-tuned Llama 3, hands-on bias-eval pass (e.g. BOLD or a small fairness suite)

### Ch 9 : Deep Convolutional GANs *(was E2 Ch 9)*
- 🟧 Generator/discriminator and DCGAN training refreshed
- 🟧 pix2pix updated
- 🟩 New section: **where GANs still win vs diffusion** (small data, real-time inference, edge)
- 🟩 Optional one-pager folding Neural Style Transfer in as a historical bridge to GANs

### Ch 10 : Image Generation Using Diffusion *(was E2 Ch 10)*
- 🟧 From-scratch diffusion code refreshed on PyTorch 2.x + `diffusers` latest
- 🟩 **Stable Diffusion XL** replaces SD v1.5 as the headline text-to-image example
- 🟩 **ControlNet** for conditional generation
- 🟩 Short note on **video diffusion** (Stable Video Diffusion / similar) - landscape coverage only
- 🟩 **Responsible AI section: deepfakes + image watermarking** - invisible image watermarking (e.g. Stable Signature / Tree-Ring style), C2PA provenance metadata, opt-out signals, and robustness against adversarial removal

### Ch 11 : Deep Reinforcement Learning *(was E2 Ch 11)*
- 🟧 DQN/Pong example refreshed; migrate from legacy `gym` to `gymnasium`
- 🟩 **RLHF in LLMs** using `trl` + PyTorch on Llama 3 (focused walkthrough, not a deep PPO derivation)
- 🟩 **DPO** as the modern RLHF alternative (cross-link with Ch 8)
- 🟩 **Responsible AI section: reward hacking and alignment** - diagnosing reward hacking in a worked example, mitigation patterns (KL penalties, reward-model ensembling), short red-teaming pass on the RLHF'd model

### Ch 12 : Model Training Optimizations *(was E2 Ch 12)*
- 🟧 Distributed training and AMP sections refreshed
- 🟩 **FSDP / FSDP 2** for large-model training on commodity GPUs
- 🟩 **`torch.distributed.checkpoint`** for resumable training
- 🟩 **`torch.compile`** integration patterns and gotchas
- 🟩 **Efficient AI section: energy, QAT, sparsity** - throughput/Watt measurement, **quantization-aware training** (`torch.ao.quantization`), **unstructured/structured sparsity** (`torch.ao.pruning`), and a practitioner checklist for shipping a more efficient model (absorbs the Efficient AI material that was originally scoped into the dropped Ch 20)

### Ch 13 : Operationalizing PyTorch Models into Production *(was E2 Ch 13)*
- 🟧 Refresh model serving sections (Flask, microservice, TorchServe)
- 🟧 Refresh TorchScript and ONNX content
- 🟧 Refresh cloud sections (AWS / GCP / Azure)
- 🟩 **vLLM** for high-throughput Llama 3 serving
- 🟩 **AOTInductor** for ahead-of-time compiled inference
- 🟩 **DeepSpeed-Inference** for multi-GPU LLM serving
- 🟩 **Responsible AI section: privacy, observability, guardrails** - **differential privacy via Opacus** (DP-SGD recipe), LLM-service guardrails (toxicity / PII redaction / prompt-injection defence), model-card-driven monitoring (absorbs the privacy + production-responsibility material from the dropped Ch 20)

### Ch 14 : PyTorch on Mobile and Edge Devices *(was E2 Ch 14)*
- 🟧 Android and iOS sections refreshed
- 🟩 **ExecuTorch** as the modern on-device runtime (replaces legacy `torch.mobile`)
- 🟩 **PyTorch Edge** overview; refreshed Jetson workflow
- 🟩 **Efficient AI section: on-device efficiency** - mobile quantization choices, latency/energy budgeting, privacy upside of on-device inference

### Ch 15 : Rapid Prototyping with PyTorch *(was E2 Ch 15)*
- 🟧 fast.ai, PyTorch Lightning, PyTorch Profiler sections refreshed
- 🟥 Drop the `poutyne` notebook (low industry traction, redundant with Lightning)

### Ch 16 : PyTorch and AutoML *(was E2 Ch 16)*
- 🟧 AutoML / NAS overview refreshed
- 🟧 Optuna content refreshed
- 🟩 Add **AutoGluon** and **AutoKeras** comparison (per my Nov 2025 plan update)

### Ch 17 : PyTorch and Explainable AI *(was E2 Ch 17)*
- 🟧 Captum content refreshed (incl. `SimilarityInfluence`)
- 🟩 New short section: **interpretability for LLMs** (attention attribution, simple probing classifiers)

### Ch 18 : Recommendation Systems with PyTorch *(was E2 Ch 18)*
- 🟧 EmbeddingNet/MovieLens baseline refreshed
- 🟩 **TorchRec** for production-scale recsys
- 🟩 Shared embeddings and large embedding tables

### Ch 19 : PyTorch and Hugging Face *(was E2 Ch 19)*
- 🟧 Refresh all sections to latest HF APIs
- 🟩 Modern model coverage anchored on **Llama 3**, with comparative examples around Qwen 2.5, Mistral, SDXL, Whisper v3

---

## Chapters dropped from E2

- **E2 Ch 3 - Combining CNNs and LSTMs**: dropped as standalone; the image-captioning example moves into the new multimodal chapter (Ch 5)
- **E2 Ch 8 - Neural Style Transfer**: dropped as standalone; optionally folded as a one-pager in Ch 9
- **E2 Ch 5 sub-section - RandWireNN**: dropped; covered indirectly in Ch 16 (AutoML/NAS)
- **E2 Ch 7 - GPT-3 (OpenAI API) text generation notebook**: dropped; replaced by open-weight LLM examples
- **E2 Ch 15 - `poutyne` notebook**: dropped

## Notebooks that need to be written from scratch (estimated)

| Chapter | Notebook(s) |
|---|---|
| Ch 1 | `pytorch2x_compile_demo.ipynb` |
| Ch 2 | `convnext_v2.ipynb` |
| Ch 4 | `vision_transformer.ipynb` (heavy) |
| Ch 5 | `clip_finetune.ipynb`, `multimodal_captioning.ipynb` |
| Ch 6 | `graph_transformer.ipynb`, `graph_fairness.ipynb` |
| Ch 7 | `llama3_text_generation.ipynb`, `musicgen.ipynb`, `speculative_decoding.ipynb`, `text_watermarking.ipynb` |
| Ch 8 | `peft_overview.ipynb`, `lora_finetuning_llama3.ipynb`, `dpo_quickstart.ipynb`, `rag_with_pytorch.ipynb`, `model_card_and_bias_eval.ipynb` |
| Ch 10 | `sdxl_text_to_image.ipynb`, `controlnet.ipynb`, `image_watermarking.ipynb` |
| Ch 11 | `rlhf_trl_llama3.ipynb`, `dpo_for_llms.ipynb`, `reward_hacking_diagnosis.ipynb` |
| Ch 12 | `fsdp_training.py`, `torch_compile_patterns.ipynb`, `distributed_checkpoint.py`, `quantization_aware_training.ipynb`, `pruning_sparsity.ipynb` |
| Ch 13 | `vllm_serving_llama3.ipynb`, `aotinductor_export.ipynb`, `deepspeed_inference.ipynb`, `opacus_dp_sgd.ipynb`, `llm_guardrails.ipynb` |
| Ch 14 | `executorch_export.ipynb`, `pytorch_edge_jetson.md`, `mobile_quantization.ipynb` |
| Ch 16 | `autogluon_pytorch.ipynb`, `autokeras_compare.ipynb` |
| Ch 17 | `llm_interpretability.ipynb` |
| Ch 18 | `torchrec_basic.ipynb`, `shared_embeddings.ipynb` |
| Ch 19 | refreshed HF notebooks (Llama 3 anchored) |

*Responsible AI / Efficient AI notebooks (formerly scoped for a standalone Ch 20) are now distributed: text watermarking → Ch 7, model card + bias eval → Ch 8, image watermarking → Ch 10, reward-hacking → Ch 11, QAT + pruning → Ch 12, Opacus DP-SGD + guardrails → Ch 13, mobile quantization → Ch 14.*
