# Mastering PyTorch, Third Edition

Companion code for *Mastering PyTorch, Third Edition* (Packt, forthcoming).

> Work in progress. Planning is locked; Wave 1 code prep is underway. Live board: [`_planning/STATUS.md`](./_planning/STATUS.md). Schedule: [`_planning/PROJECT_PLAN.md`](./_planning/PROJECT_PLAN.md).

## About this edition

This is a substantial update to *Mastering PyTorch, 2E* (2024). The book is re-anchored on **PyTorch 2.x** (`torch.compile`, FSDP, AOTInductor, ExecuTorch), with modern GenAI coverage (open-weight LLMs, SDXL, ControlNet, MusicGen). Two chapters are essentially new:

- **Chapter 5: Advanced Multimodal Models** (CLIP, BLIP-2, LLaVA)
- **Chapter 8: Fine-tuning LLMs** (PEFT/LoRA/DPO, RAG)

Responsible and Efficient AI is woven into the relevant chapters (not a standalone chapter), per Packt's May 2026 guidance.

Full 2E to 3E delta: [`_planning/CHANGE_LOG_2E_to_3E.md`](./_planning/CHANGE_LOG_2E_to_3E.md). Editor-facing outline: [`_planning/OUTLINE_E3.md`](./_planning/OUTLINE_E3.md).

## Layout

```
.
├── Chapter01/ … Chapter19/   # notebooks and scripts per chapter
├── _planning/                # outline, change log, project plan, status
├── _drafts/                  # prose drafts before they land in the book
├── requirements.txt          # PyTorch 2.13+ and ecosystem floors
├── requirements-core.txt     # lighter set for Wave 1 validation
├── scripts/                  # notebook scan / execute helpers
└── README.md
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

On macOS, if dataset downloads fail with SSL errors, make sure certifi is installed and `SSL_CERT_FILE` points at it (the validation scripts do this for you).

Many chapters want a GPU. Where they do, the chapter notes will say so and point at Colab, Kaggle, or a small cloud box.

## Author

[Ashish Ranjan Jha](https://www.linkedin.com/in/ashishrj/), Co-Founder and CEO at [Nativ](https://www.usenativ.com) (a16z Speedrun). Previously Head of ML and AI at XYZ Reality; before that Tractable, Revolut, Sony, Oracle. IIT Roorkee, EPFL, Quantic. Also authored *Mastering PyTorch, 2E* and *Fight Fraud with Machine Learning*.

## License

Apache 2.0 (same as V2; will confirm with Packt before public release).
