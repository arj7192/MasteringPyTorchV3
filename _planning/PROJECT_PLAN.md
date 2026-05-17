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

- **Print target:** **Feb 2027** (compressed re-baseline).
- **Backward solve:** if print is Feb 2027 and production needs ~8 weeks (copy-edit, typeset, proof, index), all final drafts must be delivered by **early Dec 2026**. That requires all first drafts by **mid-Oct 2026** to allow for editorial review + author final pass. Net authoring window: **5 months** from today.
- **Authoring capacity required to hit that:** ~**18–22 focused hours/week** of writing + another ~6–8 hours/week of code-running, screenshots, and review. This is roughly double the 10–12h/week baseline and is the binding constraint — see "What this requires" below.
- **Editorial review turnaround:** 2 weeks per chapter on the Packt side (per original schedule). I'll work the schedule so review queues never sit idle.
- **Vacation / conferences / Nativ travel windows:** 3 short windows of 1 week each assumed across the 5 months; anything beyond that pushes the print date.

---

## Compressed milestones (Feb 2027 print target)

Four waves of 5 chapters each, overlapped so editorial review and authoring run in parallel. Each wave is ~6 weeks; first-draft delivery cadence is roughly **one chapter per week** averaged across the run.

### Wave 0 — Setup and outline lock-in (this week, by **Fri 22 May 2026**)
- Final outline `OUTLINE_E3.md` shared with Sanjana (alongside this email)
- Change log `CHANGE_LOG_2E_to_3E.md` shared
- New Chapter 1 section draft (`Chapter01_PyTorch2x_section.md`) shared as a writing-progress sample
- `requirements.txt` and infra notes circulated
- Confirm with editorial board: new Ch 20 (Responsible & Efficient AI), Ch 8 / NST drop, headline LLM choice
- Confirm contract amendment to the Feb 2027 print target

### Wave 1 — Refresh chapters (front-loaded, low risk) — first drafts by **Fri 12 Jun 2026** (4 weeks)
- Ch 1: Overview of DL with PyTorch — refresh + the new PyTorch 2.x section
- Ch 2: Deep CNN Architectures — code refresh on PyTorch 2.x + ConvNeXt v2
- Ch 3: Deep Recurrent Models — code refresh, torchtext migration
- Ch 15: Rapid Prototyping — refresh, drop `poutyne`
- Ch 17: Explainable AI — Captum refresh

### Wave 2 — Heavy-refactor chapters — first drafts by **Fri 24 Jul 2026** (10 weeks)
- Ch 4: Transformers (+ Vision Transformers heavy new section)
- Ch 6: GNNs (+ Graph Transformers heavy new section)
- Ch 9: DCGANs (refresh + pix2pix update)
- Ch 12: Model Training Optimizations (FSDP, `torch.compile`, distributed checkpoint)
- Ch 13: Operationalizing into Production (vLLM, AOTInductor, DeepSpeed)

### Wave 3 — Net-new and big-bet chapters — first drafts by **Fri 4 Sep 2026** (16 weeks)
- Ch 5: Advanced Multimodal Models (mostly new)
- Ch 7: Music and Text Generation (modern LLMs, MusicGen, speculative decoding)
- **Ch 8: Fine-tuning LLMs (entirely new)**
- Ch 10: Image Generation Using Diffusion (SDXL, ControlNet)
- Ch 11: Deep RL (+ RLHF, DPO)

### Wave 4 — Tail and the new closing chapter — first drafts by **Fri 16 Oct 2026** (22 weeks)
- Ch 14: Mobile & Edge (ExecuTorch)
- Ch 16: AutoML (+ AutoGluon, AutoKeras)
- Ch 18: Recommendation Systems (TorchRec)
- Ch 19: PyTorch × Hugging Face (refresh + modern models)
- **Ch 20: Responsible and Efficient AI (entirely new)**

### Final drafts and production
- All final drafts delivered: **Fri 4 Dec 2026**
- Copy-edit, typesetting, proof, index: Dec 2026 – Jan 2027
- **Print target: Feb 2027**

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

Total: **~375 person-days** of focused writing time. Compressed against the **~5-month authoring window**, this lands at ~17 person-days/week — only feasible by raising my weekly capacity to 18–22 focused writing hours and overlapping waves with editorial review. See "What this requires" below.

## What this requires

To honestly hit Feb 2027 print, a few things have to change vs the original Nov 2025 plan:

1. **My capacity goes up to 18–22 writing hours/week** (vs 10–12 baseline). I plan to block Tuesdays and Thursdays as protected writing days at Nativ for the duration; weekend mornings + evenings absorb the rest.
2. **Overlap, not stop-start.** I start the next wave the same week I deliver the previous wave's first drafts, instead of waiting for editorial review to come back. Author edits on prior wave happen in parallel with new-chapter drafting.
3. **Scope guardrails on the heavy new chapters.** Ch 5 (Multimodal), Ch 8 (Fine-tuning LLMs) and Ch 20 (Responsible & Efficient AI) each get a "minimum viable chapter" cut and a "stretch" cut. If a Wave 3/4 chapter is at risk of slipping, we ship the MVC and move on.
4. **Faster editorial turnaround.** I'll need Packt's editorial review to hold to 2 weeks/chapter consistently. If it slips to 3+ weeks on the heavy chapters, the Feb 2027 print date is the first thing to slip.
5. **A technical reviewer locked in by mid-June.** Tech review can run concurrently with editorial; it cannot start late.
6. **Vacation/travel kept short.** Three 1-week windows in the 5-month run, no more.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| The 5-month compression doesn't hold (capacity, illness, Nativ spike) | Wave-overlap structure means a 1-week slip on one chapter doesn't blow the print date; weekly status notes so we re-plan together, not surprise each other |
| Day-job (Nativ) commitments spike, especially around fundraising / product launches | Tuesday/Thursday protected as writing days; if a Nativ event eats a writing day, weekend block compensates same week |
| Open-weight LLM landscape moves (Llama 3 → 4, etc.) | Lock model choice 4 weeks before each affected chapter goes to copy-edit; reference latest stable on GitHub but keep print examples conservative |
| New Ch 20 (Responsible & Efficient AI) is scoped wider than expected | Sequenced last on purpose; "minimum viable chapter" cut focuses on bias + privacy + watermarking; efficiency stays cross-cutting |
| Code rot in the 2E repo (libraries that have moved on) | Wave 1 deliberately front-loads refresh chapters so we catch and document API breakages early |
| Reviewer availability | Tech reviewer must be locked by **mid-June 2026** — happy to suggest names |
| Editorial review turnaround slips past 2 weeks | First thing to slip is the print date, not the chapter quality; would re-baseline transparently rather than rush |

---

## What I would like from Packt

1. Confirmation on Ch 20 (Responsible & Efficient AI as a new chapter vs distributed sections).
2. Confirmation on dropping standalone Neural Style Transfer chapter.
3. Updated contract / schedule aligned to the **Feb 2027 print target** above.
4. A commitment to **2-week editorial review per chapter** through the compressed window — this is the single biggest external dependency.
5. Whether a reader survey for E2 → E3 exists; if so, please share so I can fold findings in.
6. A standing 30-minute monthly check-in for the duration of the project (lighter touch than per-chapter sync, sharper than ad-hoc emails).

---

## Weekly cadence I will hold myself to

- **Monday:** ship a one-paragraph status note (what's in progress, what's due, blockers).
- **Friday:** push WIP commits to `MasteringPyTorchV3` GitHub repo so progress is visible, not just declared.
- **Per-chapter:** open a tracking issue with checklist (text, code, screenshots, references) so the editorial side can see exactly where each chapter sits.
