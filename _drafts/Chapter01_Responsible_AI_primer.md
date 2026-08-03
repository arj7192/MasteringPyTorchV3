# Chapter 1: Responsible AI primer (about one page)

> Draft v0.2 (3E). Short framing section near the end of Chapter 1. Packt's May 2026 guidance was to spread Responsible and Efficient AI through the book, not add a standalone chapter. This primer is the map for that.

Training a model is only half the job. Once a PyTorch model is in front of users (an LLM answering questions, a diffusion model making images, a recommender ranking feeds, a phone app running on-device), fairness, privacy, provenance, safety, and efficiency sit next to accuracy and latency.

We do not park those topics in an appendix. They show up where the implementation actually happens:

| Chapter | What you will do |
|---|---|
| Ch 6 Graph Neural Networks | Measure and mitigate fairness issues in node / link prediction |
| Ch 7 Music and Text Generation | Text watermarking; licensing notes for open-weight models |
| Ch 8 Fine-tuning LLMs | Write a model card; run a small bias check on fine-tuned Llama 3 |
| Ch 10 Diffusion | Image watermarking, C2PA provenance, deepfake risks |
| Ch 11 Deep RL | Reward hacking, alignment, a short red-team pass after RLHF |
| Ch 12 Training Optimizations | Efficient AI: energy per Watt, QAT, sparsity |
| Ch 13 Production | Opacus DP-SGD; LLM guardrails (toxicity, PII, prompt injection) |
| Ch 14 Mobile and Edge | On-device efficiency, and the privacy upside of keeping data local |

A few habits to start with, even before those chapters:

1. **Know where your data came from.** Are you allowed to use it for this purpose?
2. **Measure more than average accuracy.** Look at subgroups, latency, and (when it matters) energy.
3. **Leave a paper trail.** Model cards, eval notes, and basic monitoring are how good intentions survive production.
4. **Prefer the smaller option when it is good enough.** Efficient AI is not only about the planet. It is also how models stay deployable on real hardware.

You will see these again as concrete recipes later. For now, treat them as part of the same craft as writing a clean training loop.
