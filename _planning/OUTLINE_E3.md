# Mastering PyTorch, Third Edition — Outline (working draft)

**Document owner:** Ashish Ranjan Jha
**Status:** Working draft, addresses editorial board feedback from Sanjana (23 Oct 2025)
**Last updated:** 17 May 2026

---

## Book metadata

- **Title:** Mastering PyTorch
- **Subtitle (proposed update):** *Build, train, and deploy modern deep learning and generative AI systems with PyTorch 2.x*
  - Replaces the 2E subtitle that still referenced PyTorch 1.x (per editorial board feedback).
- **Edition:** 3rd
- **Anchor PyTorch version at publication:** PyTorch 2.x (latest stable at the time of go-to-press)
- **Format:** Print + ebook + GitHub companion repo (`MasteringPyTorchV3`)

## About the author (refresh)

Ashish Ranjan Jha studied electrical engineering at IIT Roorkee, computer science at École Polytechnique Fédérale de Lausanne (EPFL), and completed his MBA at Quantic School of Business, graduating with distinction from all three. He has worked at Oracle and Sony, and at recent tech unicorns Revolut and Tractable, mostly in applied machine learning. He was Head of ML and AI at XYZ Reality (London) where construction tech, AR/VR, and AI converge. He is currently Co-Founder and CEO at **Nativ**, an AI localization startup backed by a16z Speedrun. He is also an advisor to SUIND, an agritech drone startup. Ashish previously authored *Fight Fraud with Machine Learning* and *Mastering PyTorch, 2E*.

---

## Editorial board feedback — how this outline addresses it

| # | Editorial point (Sanjana, 23 Oct 2025) | How E3 addresses it |
|---|---|---|
| 1 | Reflect all latest PyTorch 2.x features, especially GenAI and LLM ecosystem | Every chapter has explicit "PyTorch 2.x uplift" items in the change log; Parts 3 and 4 are heavily reweighted toward LLMs and generative models |
| 2 | Subtitle still mentions PyTorch 1.x | Subtitle updated above |
| 3 | Add a short section in Ch 1: *"What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI"* | Added as new heading in Chapter 1 (draft section written, see `_drafts/Chapter01_PyTorch2x_section.md`) |
| 4 | Add coverage on *Responsible and Efficient AI* | Two-pronged: (a) new dedicated **Chapter 20: Responsible and Efficient AI with PyTorch** anchoring the topic; (b) recurring "Responsible AI Notes" callouts in Chapters 6, 7, 8, 10, 11, 13 (LLM/diffusion/RL/production), and an "Efficient AI" thread in Ch 12 and Ch 14 |

---

## Color-coding convention (carried over from E2 prep)

- 🟧 **UPDATE** — chapter/section/recipe refreshed to current tools and PyTorch 2.x
- 🟩 **NEW** — content that did not exist in E2
- 🟥 **REMOVE** — material being dropped as outdated

Each chapter below lists its sections with explicit tags so the editorial board can quickly see the percentage of new/updated content.

---

## Part 1 — PyTorch Overview

Concise refresher that brings any reader fluent in Python and basic DL onto a level footing for the rest of the book — now anchored on PyTorch 2.x semantics.

### Chapter 1: Overview of Deep Learning Using PyTorch  (~34 pp)
*Level: Basic*

- 🟧 A refresher on deep learning (activation functions, optimization schedule)
- 🟧 PyTorch vs TensorFlow in 2026 (tensor modules, `torch.nn`, `torch.optim`, `torch.utils.data`)
- 🟧 Training a neural network using PyTorch (MNIST feedforward)
- 🟩 **NEW — What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI** *(direct response to editorial board feedback)*
  - `torch.compile` and the TorchInductor stack
  - Dynamic shapes and graph capture
  - PyTorch 2.x performance wins on real models
  - The GenAI lens: why 2.x matters for transformers and diffusion
  - First-class integrations: HF Accelerate, vLLM, ExecuTorch
- 🟩 **NEW — Responsible AI primer** (one-page section that motivates Ch 20 and the recurring callouts)

Datasets / examples: MNIST.

### Chapter 2: Deep CNN Architectures  (~50 pp)
*Level: Advanced*

- 🟧 Why CNNs are still powerful in 2026 (and what GenAI changed)
- 🟧 Evolution of CNN architectures (LeNet → AlexNet → VGG → Inception → ResNet → DenseNet → EfficientNet → ConvNeXt)
- 🟧 Code refresh on PyTorch 2.x for all worked examples
- 🟩 Short section: **ConvNeXt v2 and the "CNNs strike back" era**

Datasets / examples: CIFAR-10 (LeNet), Hymenoptera (AlexNet, VGG).

---

## Part 2 — Modern Neural Network Architectures with PyTorch

### Chapter 3: Deep Recurrent Model Architectures  (~32 pp)
*Level: Advanced*

- 🟧 Evolution of recurrent networks (RNN, BiRNN, LSTM, GRU, attention)
- 🟧 RNN sentiment analysis (PyTorch 2.x rewrite, modern tokenizers)
- 🟧 Bidirectional LSTM
- 🟧 GRUs and attention-based models — with explicit "and this is what transformers replaced" framing
- 🟥 *(E2 standalone "Combining CNNs and LSTMs" chapter is dropped from E3; the CNN+LSTM idea is referenced briefly here as historical context and superseded by the multimodal chapter)*

Datasets / examples: IMDB.

### Chapter 4: Transformers  (formerly "Advanced Hybrid Models")  (~30 pp)
*Level: Advanced*

- 🟧 Transformer model for language modeling (PyTorch 2.x, native `nn.Transformer` vs. modern HF parity)
- 🟩 **NEW — Vision Transformers (ViT, Swin, DINO v2)** — heavy section, addresses the big gap in E2
- 🟥 **REMOVE — RandWireNN** (dated; replaced by the ViT section)

Datasets / examples: WikiText-2 (language), CIFAR-100 / ImageNet-1k subset (vision).

### Chapter 5: Advanced Multimodal Models  (~24 pp, mostly NEW)
*Level: Intermediate–Advanced*

- 🟩 Multimodal landscape in 2026 (CLIP, FLAVA, BLIP-2, LLaVA)
- 🟩 Loading and fine-tuning a CLIP model in PyTorch
- 🟩 Vision-language captioning with a modern multimodal model (replaces the 2E CNN+LSTM image captioning example as the "state-of-the-art" path)

Datasets / examples: MS-COCO, Flickr30k.

### Chapter 6: Graph Neural Networks  (~30 pp)
*Level: Advanced*

- 🟧 Intro to GNNs and graph learning tasks
- 🟧 GCN, GAT, GraphSAGE refresh on PyTorch Geometric latest
- 🟩 **NEW — Graph Transformers (Graphormer, GraphGPS)** — heavy section
- 🟩 *Responsible AI note:* fairness in graph models (e.g. social-network recommendation harms)

Datasets / examples: Karate Club, Planetoid (Cora/Citeseer/Pubmed), OGB.

---

## Part 3 — Generative AI and Reinforcement Learning with PyTorch

### Chapter 7: Music and Text Generation with PyTorch  (~32 pp)
*Level: Intermediate*

- 🟧 Transformer-based text generator (PyTorch 2.x rewrite)
- 🟧 Pre-trained LLM as text generator (swap GPT-2/3 for **Llama 3 / Qwen 2.5 / Mistral**)
- 🟧 Decoding strategies (greedy, beam, top-k, top-p, temperature, **speculative decoding** as new addition)
- 🟧 Music generation: **MusicGen** (replaces the LSTM MIDI example as the headline; LSTM kept as a teaching baseline)
- 🟩 *Responsible AI note:* watermarking generated content, attribution, dataset licensing

Datasets / examples: WikiText-2, Classical Piano MIDI, MusicGen prompts.

### Chapter 8: Fine-tuning LLMs  (~28 pp, mostly NEW)  *replaces E2 Ch 8 "Neural Style Transfer"*
*Level: Advanced*

- 🟩 Loading open-weight LLMs in PyTorch with HF Transformers
- 🟩 Parameter-Efficient Fine-Tuning (PEFT) overview: LoRA, QLoRA, IA³, adapters
- 🟩 Hands-on **LoRA fine-tuning** on an open-weight model with `peft`, on a single GPU
- 🟩 **Direct Preference Optimization (DPO)** as a lightweight alternative to RLHF — quick worked example
- 🟩 Inference and deployment teaser (full deployment lives in Ch 13)
- 🟩 Retrieval-Augmented Generation (RAG) with PyTorch + a vector store
- 🟩 *Responsible AI note:* training data provenance, model card, eval hygiene
- 🟥 **REMOVE — Neural Style Transfer chapter** (folded into Ch 9 as a short historical section if at all)

Datasets / examples: WikiText, a small instruction-tuning set (e.g. Alpaca-style subset).

### Chapter 9: Deep Convolutional GANs  (~25 pp)
*Level: Intermediate*

- 🟧 Generator/discriminator definitions, DCGAN training in PyTorch 2.x
- 🟧 GANs for style transfer (pix2pix) — modernized
- 🟩 Brief section: **where GANs still win vs diffusion** (small-data, real-time, edge)
- 🟩 (Optional one-pager) Neural style transfer as the historical bridge to GANs (preserves the educational thread without a full chapter)

Datasets / examples: MNIST, paired image dataset for pix2pix.

### Chapter 10: Image Generation Using Diffusion  (~18-20 pp)
*Level: Advanced*

- 🟧 Understanding diffusion, forward/reverse processes
- 🟧 Training a diffusion model from scratch with `diffusers`
- 🟩 **Stable Diffusion XL** (replaces SD v1.5 as the worked text-to-image example)
- 🟩 **ControlNet** for conditional generation
- 🟩 Short note on **video diffusion** (e.g. Stable Video Diffusion) — landscape only
- 🟩 *Responsible AI note:* deepfakes, watermarking, opt-outs

Datasets / examples: a small image set for from-scratch diffusion, SDXL prompts.

### Chapter 11: Deep Reinforcement Learning  (~32-35 pp)
*Level: Advanced*

- 🟧 RL concepts, Q-learning, deep Q-learning
- 🟧 Building a DQN in PyTorch 2.x (Pong on Gymnasium, replacing legacy OpenAI Gym imports)
- 🟩 **RLHF in LLMs** — PPO recap, then a focused walkthrough wiring `trl` + PyTorch
- 🟩 **DPO as the modern RLHF alternative** (cross-referenced with Ch 8)
- 🟩 *Responsible AI note:* reward hacking, value alignment

Datasets / examples: Atari Pong (Gymnasium), small preference dataset for RLHF/DPO.

---

## Part 4 — PyTorch in Production at Scale

### Chapter 12: Model Training Optimizations  (~18-22 pp)
*Level: Advanced*

- 🟧 Distributed training with PyTorch (`torch.distributed`)
- 🟧 GPU + CUDA + Automatic Mixed Precision
- 🟩 **Fully Sharded Data Parallel (FSDP / FSDP 2)** — large model training on commodity GPUs
- 🟩 **`torch.distributed.checkpoint`** for resumable large-scale training
- 🟩 **`torch.compile`** integration patterns and gotchas
- 🟩 *Efficient AI note:* energy use, throughput per watt

Datasets / examples: MNIST (baseline), a tiny LLM (e.g. nanoGPT-scale) for FSDP demo.

### Chapter 13: Operationalizing PyTorch Models into Production  (~38-43 pp)
*Level: Intermediate–Advanced*

- 🟧 Model serving in PyTorch (inference pipeline, Flask, microservice, TorchServe)
- 🟧 TorchScript and ONNX export
- 🟧 PyTorch in C++
- 🟧 Cloud deployments (AWS, GCP, Azure) — refreshed
- 🟩 **vLLM** for high-throughput LLM serving
- 🟩 **AOTInductor** for ahead-of-time compiled inference
- 🟩 **DeepSpeed-Inference** for multi-GPU LLM serving
- 🟩 *Responsible AI note:* observability and guardrails in production

Datasets / examples: MNIST classifier (baseline serving), a small open-weight LLM (vLLM/AOTInductor/DeepSpeed paths).

### Chapter 14: PyTorch on Mobile and Edge Devices  (~20-22 pp)
*Level: Advanced*

- 🟧 Deploying a PyTorch model on Android (refreshed)
- 🟧 Building PyTorch apps on iOS (refreshed)
- 🟩 **ExecuTorch** as the modern on-device runtime (replaces legacy `torch.mobile`)
- 🟩 **PyTorch Edge** stack overview; Jetson workflow refresh

Datasets / examples: Image segmentation (Android), speech recognition (iOS), object detection (Jetson).

---

## Part 5 — The PyTorch Ecosystem

### Chapter 15: Rapid Prototyping with PyTorch  (~15 pp)
*Level: Intermediate*

- 🟧 fast.ai
- 🟧 PyTorch Lightning
- 🟧 PyTorch Profiler

### Chapter 16: PyTorch and AutoML  (~20 pp)
*Level: Intermediate*

- 🟧 AutoML overview, neural architecture search
- 🟧 Optuna for hyperparameter search
- 🟩 Auto-PyTorch alternatives: **AutoGluon**, **AutoKeras** comparison (per the Nov 2025 plan update)

### Chapter 17: PyTorch and Explainable AI  (~15 pp)
*Level: Intermediate*

- 🟧 Model interpretability in PyTorch
- 🟧 Captum, refreshed (incl. `SimilarityInfluence`)
- 🟩 Short section: **interpretability for LLMs** (attention attribution, simple probing) — bridges to Ch 20

### Chapter 18: Recommendation Systems with PyTorch  (~12-15 pp)
*Level: Advanced*

- 🟧 EmbeddingNet baseline on MovieLens
- 🟩 **TorchRec** for production-scale recommendation
- 🟩 Shared embeddings and large embedding tables

### Chapter 19: PyTorch and Hugging Face  (~15-18 pp)
*Level: Advanced*

- 🟧 Hugging Face within the PyTorch context
- 🟧 Hub, Datasets, Accelerate, Optimum — refreshed to latest APIs
- 🟩 Modern model coverage (Llama 3, Qwen, Mistral, SDXL, Whisper v3)

### Chapter 20: Responsible and Efficient AI with PyTorch  (~18 pp, ALL NEW)
*Level: Intermediate–Advanced* — **net-new chapter, directly addresses editorial feedback**

- 🟩 What "Responsible AI" means in 2026 (NIST AI RMF, EU AI Act practitioner view)
- 🟩 Bias detection and mitigation in PyTorch (with Fairlearn / AIF360 / Captum)
- 🟩 Privacy: differential privacy with **Opacus**
- 🟩 Robustness: adversarial training basics
- 🟩 Watermarking generated content (text + images)
- 🟩 **Efficient AI:** energy-aware training, throughput/Watt, quantization-aware training, sparsity
- 🟩 A practitioner's checklist for shipping responsible PyTorch systems

Datasets / examples: a small tabular fairness dataset, an image classifier for adversarial demos, an LLM for watermarking, MNIST for DP-SGD.

---

## Net change summary (rough)

| Bucket | Chapters touched |
|---|---|
| 🟩 Net-new chapters | Ch 5 (Advanced Multimodal Models), Ch 8 (Fine-tuning LLMs), Ch 20 (Responsible & Efficient AI) |
| 🟩 Heavy new sections inside existing chapters | Ch 1 (PyTorch 2.x), Ch 4 (ViT), Ch 6 (Graph Transformers), Ch 7 (modern LLMs + MusicGen), Ch 9 (pix2pix refresh + GANs-vs-diffusion), Ch 10 (SDXL + ControlNet), Ch 11 (RLHF/DPO), Ch 12 (FSDP, `torch.compile`), Ch 13 (vLLM, AOTInductor, DeepSpeed), Ch 14 (ExecuTorch), Ch 16 (AutoGluon/AutoKeras), Ch 18 (TorchRec) |
| 🟥 Removed | E2 Ch 3 *Combining CNNs and LSTMs* (standalone chapter), E2 Ch 8 *Neural Style Transfer* (standalone chapter), RandWireNN, GPT-3 OpenAI-API notebook |
| 🟧 Pure refresh | Ch 2, Ch 3, Ch 15, Ch 17 |

Rough overall churn: **~55-60% of the book** is updated or replaced, **~25%** is completely new, **~15-20%** is a light PyTorch 2.x code refresh.

---

## Open questions for the editorial board

1. Comfortable with the new Chapter 21 ("Responsible and Efficient AI"), or prefer it distributed as sections across existing chapters? My recommendation is dedicated chapter + recurring callouts (as drafted above).
2. Comfortable dropping the standalone Neural Style Transfer chapter, given it is well-covered online and crowds out higher-impact GenAI content?
3. Any opinion on swapping the headline LLM example (Llama 3 vs Qwen 2.5 vs Mistral) for license/availability stability over the print lifetime?
4. Was a reader survey collected for E2→E3 (similar to the E1→E2 one)? If yes, please share — I will fold findings into the next outline revision.
