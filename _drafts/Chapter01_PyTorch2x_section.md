# Chapter 1: What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI

> Draft v0.2 (3E). New section requested by the editorial board. Sits late in Chapter 1, after the PyTorch vs TensorFlow overview and before the MNIST training walkthrough. Target: about 3 book pages. Notebook: `Chapter01/pytorch2x_compile_demo.ipynb`.

PyTorch 2 shipped in March 2023. By the time this edition lands, it is basically the default for anyone actively writing PyTorch. If you used 1.x a lot, the good news is boring in a helpful way: your old code still mostly runs. What changed is how fast that same code can run, without forcing you into a separate "graph mode" lifestyle.

This section covers the four things that matter for the rest of the book: `torch.compile`, the TorchInductor stack under it, dynamic shapes, and why PyTorch 2.x is now the usual substrate for generative AI work.

## `torch.compile`: one line, real speedups

The headline addition is `torch.compile`. You wrap a model (or any callable), PyTorch traces it, runs it through a compiler pipeline, and hands you back something that behaves like the original but usually runs faster:

```python
import torch

model = MyModel().cuda()
compiled_model = torch.compile(model)

for batch in loader:
    out = compiled_model(batch)  # same call site, compiled under the hood
```

You do not maintain a second IR by hand. You write normal PyTorch, then opt in at the boundary.

Under the hood, three pieces are involved:

1. **TorchDynamo** captures the Python bytecode of your forward pass into an FX graph. When it cannot capture something, it falls back to eager mode for that fragment (this is why "drop-in" is realistic).
2. **AOTAutograd** captures the backward graph too, so training can be compiled, not only inference.
3. **TorchInductor** (default backend) lowers the graph to fused kernels. On NVIDIA that usually means Triton. On CPU it uses C++/OpenMP.

For the models in this book (CNNs in Chapter 2, transformers in Chapter 4, diffusion in Chapter 10), you often see about 1.3x to 2x wall-clock improvement at training time, and sometimes more at inference. We will keep turning `torch.compile` on where it helps, and we will also say when it is not free: tiny models, very dynamic control flow, some custom CUDA kernels.

## Dynamic shapes and graph breaks

In PyTorch 1.x, the usual "make it fast" path was TorchScript. That path wanted a fairly static, fully traceable subset of Python. Branching on shapes or values tended to break the trace.

PyTorch 2 is more forgiving. TorchDynamo can insert graph breaks, run a bit of eager Python, then keep capturing. That means Hugging Face tokenizers, NumPy, and ordinary Python control flow can sit inside a compiled model, and you still get speedups on the parts that compile cleanly.

Dynamic shapes matter here too: variable sequence lengths, variable batch sizes, and other GenAI-shaped workloads. We will show a small dynamic-shape example at the end of this chapter, and come back to graph breaks (including `torch._dynamo.explain`) in Chapter 12.

## Performance: not one benchmark, a stack of defaults

Compile is the flashy bit, but PyTorch 2 also quietly improved a lot of kernels: FlashAttention-2 as the default scaled-dot-product attention on supported hardware, memory-efficient attention as a fallback, fused AdamW pieces, tighter CUDA Graphs integration for inference. None of those alone is as visible as `torch.compile`, but together they are why a small open-weight LLM that felt painful on one consumer GPU in 2023 is much more workable now.

When we get to Chapters 7, 8, and 11, we will lean on those defaults instead of hand-wiring everything. Practical takeaway for Chapter 1: prefer `torch.nn.functional.scaled_dot_product_attention` over a hand-rolled attention formula, prefer `torch.compile` over jumping straight to `torch.jit.script`, and trust the defaults more than you would have in 1.x.

## A substrate for generative AI

If 1.x was a research framework that also happened to deploy, 2.x is the usual home for modern GenAI tooling. The libraries we use later in the book (`transformers`, `diffusers`, `accelerate`, `peft`, `trl`, `vllm`, ExecuTorch, TorchRec) are PyTorch-native and built against the 2.x contract.

Three consequences for this book:

1. **Open-weight LLMs are PyTorch-native by default.** We use **Llama 3** as the main worked example, with lighter comparisons to Qwen 2.5 and Mistral. Chapters 7, 8, 11, and 13 cover generation, fine-tuning, RLHF, and serving with that anchor.
2. **Compiled inference is an option for bigger models too.** `torch.compile` plus AOTInductor (Chapter 13) can produce shippable artifacts. vLLM uses PyTorch internals for high-throughput LLM serving. Both replace older, more fragile 2E recipes.
3. **Edge has consolidated on ExecuTorch.** Older `torch.mobile` paths are effectively superseded. Chapter 14 covers the new path.

## What this means for the rest of the book

From here on:

- Training loops are written to be `torch.compile`-friendly.
- Attention uses `scaled_dot_product_attention` where it appears.
- Distributed training in Chapter 12 uses FSDP / FSDP 2 and `torch.distributed.checkpoint`.
- Production serving in Chapter 13 prefers AOTInductor, vLLM, and DeepSpeed-Inference over the older 2E recipes.
- Edge deployment in Chapter 14 uses ExecuTorch.

If you already know most of this, skip ahead. One habit still worth forming early: turn `torch.compile` on in a small notebook first. It is much cheaper to learn the defaults on MNIST than on a 7B model.

### Reference list (to fill in at copy-edit)

- PyTorch 2.0 launch post, March 2023
- Ansel et al., *PyTorch 2...*, ASPLOS 2024 (TorchDynamo / TorchInductor)
- PyTorch docs: `torch.compile`, `torch._dynamo`, `torch._inductor`
- Flash Attention 2 (Dao, 2023)
- ExecuTorch, AOTInductor, vLLM docs
