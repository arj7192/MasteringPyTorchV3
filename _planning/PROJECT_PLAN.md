# Mastering PyTorch 3E — Project plan (re-baselined May 2026)

**Author:** Ashish Ranjan Jha
**Re-baseline date:** 17 May 2026
**Original schedule:** Packt `SCHEDULE_Ashish.xlsx` (issued Oct 2025)
**Day-count proposal:** my email to Sanjana, 2 Nov 2025

---

## Honest summary of where we are

- E3 outline (with color coding) was delivered to Packt 21 Oct 2025.
- Editorial board feedback received 23 Oct 2025; addressed in the new `OUTLINE_E3.md` (PyTorch 2.x subtitle, new Ch 1 section, Responsible AI coverage).
- Packt schedule received 27 Oct 2025; my day-count revision proposed 2 Nov 2025 to reflect the higher load on net-new and heavily-refactored chapters.
- Between Nov 2025 and now, day-job load at Nativ (a16z Speedrun-backed startup, fundraising and shipping) plus a stretch of being unwell in April pushed first-draft work behind. **No first drafts have been delivered yet.**
- The artifacts shipped alongside this plan are intended as honest, visible progress to restart momentum, not as a substitute for chapter drafts.

The rest of this document is a re-baselined plan I am committing to.

---

## Working assumptions

- **Authoring capacity:** Sustainable ~10–12 focused hours/week of writing, plus another ~4–6 hours/week of code-running, screenshots, and review. Higher in bursts; not sustainably more.
- **Vacation / conferences / Nativ travel windows:** 1 week buffer per month assumed.
- **Editorial review turnaround:** 2 weeks per chapter on the Packt side (per the original schedule).
- **Print target:** Late Q1 / early Q2 2027 — a realistic re-baseline rather than the original 2026 print target.

---

## Re-baselined milestones (first-draft delivery)

I have grouped chapters into waves so editorial review can start before all drafts are in. Each wave assumes first-draft delivery; final drafts follow ~3 weeks later after review.

### Wave 0 — Setup and outline lock-in (this week, by **Fri 22 May 2026**)
- Final outline `OUTLINE_E3.md` shared with Sanjana (draft alongside this email)
- Change log `CHANGE_LOG_2E_to_3E.md` shared
- New Chapter 1 section draft (`Chapter01_PyTorch2x_section.md`) shared as a writing-progress sample
- `requirements_E3.txt` and infra notes circulated
- Confirm with editorial board: new Ch 21 (Responsible & Efficient AI), Ch 8 / NST drop, headline LLM choice

### Wave 1 — Refresh chapters (front-loaded, low risk) — first drafts by **Fri 27 Jun 2026**
- Ch 1: Overview of DL with PyTorch — refresh + the new PyTorch 2.x section
- Ch 2: Deep CNN Architectures — code refresh on PyTorch 2.x + ConvNeXt v2
- Ch 3: Deep Recurrent Models — code refresh, torchtext migration
- Ch 15: Rapid Prototyping — refresh, drop `poutyne`
- Ch 17: Explainable AI — Captum refresh

### Wave 2 — Heavy-refactor chapters — first drafts by **Fri 22 Aug 2026**
- Ch 4: Transformers (+ Vision Transformers heavy new section)
- Ch 6: GNNs (+ Graph Transformers heavy new section)
- Ch 9: DCGANs (refresh + pix2pix update)
- Ch 12: Model Training Optimizations (FSDP, `torch.compile`, distributed checkpoint)
- Ch 13: Operationalizing into Production (vLLM, AOTInductor, DeepSpeed)

### Wave 3 — Net-new and big-bet chapters — first drafts by **Fri 14 Nov 2026**
- Ch 5: Advanced Multimodal Models (mostly new)
- Ch 7: Music and Text Generation (modern LLMs, MusicGen, speculative decoding)
- **Ch 8: Fine-tuning LLMs (entirely new)**
- Ch 10: Image Generation Using Diffusion (SDXL, ControlNet)
- Ch 11: Deep RL (+ RLHF, DPO)

### Wave 4 — Tail and the new closing chapter — first drafts by **Fri 16 Jan 2027**
- Ch 14: Mobile & Edge (ExecuTorch)
- Ch 16: AutoML (+ AutoGluon, AutoKeras)
- Ch 18: Recommendation Systems (TorchRec)
- Ch 19: PyTorch × Hugging Face (refresh + modern models)
- **Ch 20: Responsible and Efficient AI (entirely new)**

### Final drafts and production
- All final drafts delivered: **Fri 27 Feb 2027**
- Copy-edit and typesetting: Mar–Apr 2027
- Realistic print target: **early Q2 2027**

---

## Day-count map vs my Nov 2025 proposal

The Nov 2025 numbers I proposed remain my best estimate per chapter:

| Ch (E3) | Title | Days proposed (Nov 2025) | Wave |
|---|---|---|---|
| 1  | Overview of DL with PyTorch | 18 | 1 |
| 2  | Deep CNN Architectures | 28 | 1 |
| 3  | Deep Recurrent Models | 16 | 1 |
| 4  | Transformers | 22 | 2 |
| 5  | Advanced Multimodal Models | 30 | 3 |
| 6  | Graph Neural Networks | 22 | 2 |
| 7  | Music and Text Generation | 22 | 3 |
| 8  | Fine-tuning LLMs | 30 | 3 |
| 9  | Deep Convolutional GANs | 22 | 2 |
| 10 | Image Generation w/ Diffusion | 18 | 3 |
| 11 | Deep RL (+ RLHF) | 27 | 3 |
| 12 | Model Training Optimizations | 18 | 2 |
| 13 | Operationalizing PyTorch | 25 | 2 |
| 14 | Mobile & Edge | 16 | 4 |
| 15 | Rapid Prototyping | 8 | 1 |
| 16 | PyTorch and AutoML | 15 | 4 |
| 17 | Explainable AI | 9 | 1 |
| 18 | Recommendation Systems (TorchRec) | 15 | 4 |
| 19 | PyTorch × Hugging Face | 16 | 4 |
| 20 | **Responsible & Efficient AI (new)** | 18 | 4 |

Total: **~375 person-days** of focused writing time. With my realistic capacity, parallel wave structure, and editorial cycles, this maps to the **~9-month authoring window** above.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Day-job (Nativ) commitments spike, especially around fundraising / product launches | Wave structure keeps editorial unblocked even if one chapter slips by 2-3 weeks; I commit to weekly status updates so we can re-plan together, not surprise each other |
| Open-weight LLM landscape moves (Llama 3 → 4, etc.) | Lock model choice 4 weeks before each affected chapter goes to copy-edit; reference latest stable on GitHub but keep print examples conservative |
| New Ch 21 (Responsible & Efficient AI) is scoped wider than expected | Sequenced last on purpose; if scope balloons we cut to bias + privacy + watermarking and keep efficiency as cross-cutting callouts |
| Code rot in the 2E repo (libraries that have moved on) | Wave 1 deliberately front-loads refresh chapters so we catch and document API breakages early |
| Reviewer availability | Suggest having a tech reviewer lined up by end of Wave 1 (June); happy to suggest names |

---

## What I would like from Packt

1. Confirmation on Ch 21 (Responsible & Efficient AI as a new chapter vs distributed sections).
2. Confirmation on dropping standalone Neural Style Transfer chapter.
3. Updated contract / schedule if the re-baseline above is workable.
4. Whether a reader survey for E2 → E3 exists; if so, please share so I can fold findings in.
5. A standing 30-minute monthly check-in for the duration of the project (lighter touch than per-chapter sync, sharper than ad-hoc emails).

---

## Weekly cadence I will hold myself to

- **Monday:** ship a one-paragraph status note (what's in progress, what's due, blockers).
- **Friday:** push WIP commits to `MasteringPyTorchV3` GitHub repo so progress is visible, not just declared.
- **Per-chapter:** open a tracking issue with checklist (text, code, screenshots, references) so the editorial side can see exactly where each chapter sits.
