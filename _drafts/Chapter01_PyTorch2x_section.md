# Chapter 1 — *What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI*

> **Draft v0.1 (3E).** This is the new section requested by the editorial board. Intended position: late in Chapter 1, after *Exploring the PyTorch library in contrast to TensorFlow* and before *Training a neural network using PyTorch*. Target length: ~3 book pages. Notebook companion: `Chapter01/pytorch2x_compile_demo.ipynb`.

PyTorch 2 was first released in March 2023 and has, by the time of this third edition, become the default mental model for almost every active PyTorch user. If you are coming from PyTorch 1.x, the headline news is simple: the API you know is still there, and most of your existing code runs unmodified. What is new is *how* that code can run — substantially faster, with the same eager-mode authoring experience that made PyTorch popular in the first place.

This section walks through the four shifts that matter most for the rest of this book: `torch.compile`, the TorchInductor compiler stack underneath it, dynamic shapes, and the way PyTorch 2.x has become the substrate for the modern generative-AI ecosystem.

## `torch.compile`: one line, real speedups

The single most important addition in PyTorch 2 is `torch.compile`. You wrap a model — or any callable — with `torch.compile(...)`, and PyTorch traces it, lowers it through a compiler pipeline, and gives you back a drop-in replacement that runs faster on the same hardware:

```python
import torch

model = MyModel().cuda()
compiled_model = torch.compile(model)

for batch in loader:
    out = compiled_model(batch)  # behaves like model(batch), but compiled
```

There is no separate "graph mode" to maintain alongside eager mode, no IR you have to author by hand, and no special way of writing your model. You keep writing PyTorch the way you have always written PyTorch, and you opt in to compilation at the boundary.

Under the hood, `torch.compile` is doing three things in sequence:

1. **TorchDynamo** captures the Python bytecode of your forward pass into an FX graph, falling back to eager execution for anything it cannot capture (this is what makes "drop-in" feasible in practice).
2. **AOTAutograd** captures the corresponding backward graph, so training is compiled, not just inference.
3. **TorchInductor** (the default backend) lowers the captured graph to fused GPU kernels — generated via Triton on NVIDIA, and via C++/OpenMP on CPU.

For the kinds of models we build in this book — CNNs in Chapter 2, transformers in Chapter 5, diffusion models in Chapter 11 — the result is typically a 1.3× to 2× wall-clock speedup at training time, and often more at inference, with no other changes to the code. We will use `torch.compile` throughout the rest of the book and surface it explicitly wherever the wins are material; we will also call out the cases where it is *not* yet a free lunch (very small models, very dynamic control flow, certain custom CUDA kernels) so you know when to leave it off.

## Dynamic shapes and graph breaks

In PyTorch 1.x, the standard way to make a model fast was to export it to TorchScript and then ship that. TorchScript demanded a static, fully traceable subset of Python, and any branch on a tensor's shape or value tended to break the trace. PyTorch 2 takes a different stance: TorchDynamo is allowed to insert *graph breaks* whenever it encounters something it cannot capture, fall back to eager Python for that fragment, and then continue capturing on the other side.

The practical implication is that you can use Python control flow, NumPy, Hugging Face tokenizers, and other "messy" code inside a compiled model, and `torch.compile` will still recover real speedups on the parts of the graph it can see. Combined with first-class support for **dynamic shapes** — sequence-length-dependent transformer blocks, variable-batch inference — this is what makes PyTorch 2 usable on real generative-AI workloads, not just on the kinds of fixed-shape ConvNets that earlier graph compilers handled.

We will demonstrate a dynamic-shape compile in the worked example at the end of this chapter, and revisit graph breaks (and how to find them with `torch._dynamo.explain`) in Chapter 13 when we look at large-model training.

## Performance: not a benchmark, a vibe shift

Compile times aside, PyTorch 2 has also brought a steady stream of kernel-level improvements: **FlashAttention-2** as the default scaled-dot-product attention backend on supported hardware, **memory-efficient attention** as a fallback, fused optimizer kernels for AdamW, and tighter integration with **CUDA Graphs** for inference. None of these are individually as visible as `torch.compile`, but together they are the reason a small open-weight LLM that was barely tractable on a single consumer GPU in 2023 is comfortably fine-tunable today.

When we get to Chapters 8, 9 and 12, we will lean on these defaults rather than wiring them up by hand, and you will see how much the stack has moved underneath you. The pragmatic takeaway for Chapter 1: prefer `torch.nn.functional.scaled_dot_product_attention` over a hand-rolled `softmax(QK^T / sqrt(d)) V`, prefer `torch.compile` over `torch.jit.script`, and trust the defaults more than you would have in PyTorch 1.x.

## A substrate for generative AI

If PyTorch 1.x was a research framework that happened to be deployable, PyTorch 2.x is, in practical terms, *the* substrate for modern generative AI. The libraries we are going to use heavily in the later parts of this book — Hugging Face `transformers`, `diffusers`, `accelerate`, `peft`, `trl`, `vllm`, **ExecuTorch**, **TorchRec** — are all PyTorch-native and all built against the PyTorch 2 contract.

This has three consequences worth flagging up front:

1. **Open-weight LLMs are PyTorch-native by default.** Llama 3, Qwen 2.5, Mistral, Phi-3 — the open-weight model you reach for is, almost without exception, distributed as a PyTorch checkpoint. We use them in Chapters 8 and 9.
2. **Compiled inference is now an option for big models too.** `torch.compile` plus **AOTInductor** (Chapter 14) lets you ahead-of-time compile a model into a shippable artifact, while **vLLM** uses PyTorch internals to serve LLMs at high throughput. Both replace older, more fragile recipes from 2E.
3. **Edge deployment has consolidated on ExecuTorch.** `torch.mobile` from earlier editions has effectively been superseded; Chapter 15 walks through the new path.

## What this means for the rest of the book

You will see PyTorch 2.x conventions woven through every chapter from here on:

- All training loops are written to be `torch.compile`-friendly.
- Attention is computed via `scaled_dot_product_attention` wherever it appears.
- Distributed training in Chapter 13 uses **FSDP / FSDP 2** and `torch.distributed.checkpoint`.
- Production serving in Chapter 14 prefers **AOTInductor**, **vLLM** and **DeepSpeed-Inference** over the recipes you may remember from the second edition.
- Edge deployment in Chapter 15 uses **ExecuTorch**.

If you are skimming this section because you already know most of this — fair enough. The one piece of advice it is worth pausing on is this: turn `torch.compile` on early. Every recipe in this book runs faster with it on, and turning it on in a hello-world MNIST notebook is the cheapest way to internalize the new defaults before you need them on a 7B-parameter model.

---

### Reference list (to be added in copy-edit)

- PyTorch 2.0 launch post, March 2023
- *PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation*, Ansel et al., ASPLOS 2024 (the canonical reference for TorchDynamo and TorchInductor)
- PyTorch official docs: `torch.compile`, `torch._dynamo`, `torch._inductor`
- Flash Attention 2 paper (Dao, 2023)
- ExecuTorch docs, AOTInductor docs, vLLM docs
