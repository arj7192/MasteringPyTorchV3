# Mastering PyTorch, Third Edition

Companion code repository for *Mastering PyTorch, Third Edition* (Packt, forthcoming).

> **Status: work in progress.** This repository is being prepared in parallel with chapter authoring. Contents will land chapter-by-chapter as drafts move into review. See [`_planning/PROJECT_PLAN.md`](./_planning/PROJECT_PLAN.md) for the schedule.

## About this edition

This third edition is a substantial update to *Mastering PyTorch, 2E* (2024). It re-anchors the entire book on **PyTorch 2.x** semantics (`torch.compile`, FSDP, AOTInductor, ExecuTorch), modernizes the generative-AI coverage (open-weight LLMs, SDXL, ControlNet, MusicGen), and adds two new chapters:

- **Chapter 9 — Fine-tuning LLMs** (PEFT/LoRA/DPO, RAG)
- **Chapter 21 — Responsible and Efficient AI with PyTorch**

For the full delta from 2E, see [`_planning/CHANGE_LOG_2E_to_3E.md`](./_planning/CHANGE_LOG_2E_to_3E.md). For the editor-facing outline that incorporates the editorial board's feedback, see [`_planning/OUTLINE_E3.md`](./_planning/OUTLINE_E3.md).

## Repository layout

```
.
├── Chapter01/ … Chapter21/   # one folder per chapter, notebooks + scripts
├── _planning/                # outline, change log, project plan (editorial-facing)
├── _drafts/                  # in-progress prose drafts before they land in the book
├── requirements.txt          # base Python deps (PyTorch 2.x anchored)
└── README.md                 # this file
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Many chapters need a GPU. Where they do, the chapter README will say so and point at the cheapest path (Colab, Kaggle, or a small cloud instance).

## Author

[Ashish Ranjan Jha](https://www.linkedin.com/in/ashishrj/) — Co-Founder and CEO at [Nativ](https://www.nativ.ai), an a16z Speedrun-backed AI localization startup. Previously Head of ML & AI at XYZ Reality; prior to that at Tractable, Revolut, Sony and Oracle. IIT Roorkee, EPFL, Quantic. Previously authored *Mastering PyTorch, 2E* and *Fight Fraud with Machine Learning*.

## License

Apache 2.0 (to match V2 repo; will confirm with Packt before public release).
