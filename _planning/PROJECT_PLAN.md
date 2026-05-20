# Mastering PyTorch 3E — Project plan (re-baselined May 2026)

**Author:** Ashish Ranjan Jha
**Re-baseline date:** 17 May 2026 (updated 20 May 2026 with Packt's editorial decisions)
**Original schedule:** Packt `SCHEDULE_Ashish.xlsx` (issued Oct 2025)
**Day-count proposal:** my email to Sanjana, 2 Nov 2025
**Editorial decisions:** Shashank, 20 May 2026 (Responsible AI distributed; NST dropped; Llama 3 headline)

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
- ✅ Final outline `OUTLINE_E3.md` shared
- ✅ Change log `CHANGE_LOG_2E_to_3E.md` shared
- ✅ New Chapter 1 section draft (`Chapter01_PyTorch2x_section.md`) shared as a writing-progress sample
- ✅ `requirements.txt` and infra notes circulated
- ✅ Editorial decisions locked with Packt (20 May): Responsible AI distributed across chapters (not standalone), NST dropped, Llama 3 = primary LLM
- Awaiting: reader-survey data from Sanjana on return from leave
- Awaiting: confirmation of contract amendment to the Feb 2027 print target

### Wave 1 — Refresh chapters (front-loaded, low risk) — first drafts by **Fri 12 Jun 2026** (4 weeks)
- Ch 1: Overview of DL with PyTorch — refresh + the new PyTorch 2.x section + Responsible AI primer
- Ch 2: Deep CNN Architectures — code refresh on PyTorch 2.x + ConvNeXt v2
- Ch 3: Deep Recurrent Models — code refresh, torchtext migration
- Ch 15: Rapid Prototyping — refresh, drop `poutyne`
- Ch 17: Explainable AI — Captum refresh

### Wave 2 — Heavy-refactor chapters — first drafts by **Fri 24 Jul 2026** (10 weeks)
- Ch 4: Transformers (+ Vision Transformers heavy new section)
- Ch 6: GNNs (+ Graph Transformers + graph-fairness section)
- Ch 9: DCGANs (refresh + pix2pix update + NST one-pager)
- Ch 12: Model Training Optimizations (FSDP, `torch.compile`, distributed checkpoint **+ QAT + sparsity + energy/Watt**)
- Ch 13: Operationalizing into Production (vLLM, AOTInductor, DeepSpeed **+ Opacus DP-SGD + LLM guardrails**)

### Wave 3 — Net-new and big-bet chapters — first drafts by **Fri 4 Sep 2026** (16 weeks)
- Ch 5: Advanced Multimodal Models (mostly new)
- Ch 7: Music and Text Generation (Llama 3, MusicGen, speculative decoding **+ text watermarking**)
- **Ch 8: Fine-tuning LLMs (entirely new)** (LoRA on Llama 3, DPO, RAG **+ model card + bias eval**)
- Ch 10: Image Generation Using Diffusion (SDXL, ControlNet **+ image watermarking**)
- Ch 11: Deep RL (DQN, RLHF on Llama 3, DPO **+ reward-hacking diagnosis + red-teaming**)

### Wave 4 — Tail chapters — first drafts by **Fri 16 Oct 2026** (22 weeks)
- Ch 14: Mobile & Edge (ExecuTorch **+ on-device efficiency**)
- Ch 16: AutoML (+ AutoGluon, AutoKeras)
- Ch 18: Recommendation Systems (TorchRec)
- Ch 19: PyTorch × Hugging Face (refresh + Llama 3-anchored model coverage)

### Final drafts and production
- All final drafts delivered: **Fri 4 Dec 2026**
- Copy-edit, typesetting, proof, index: Dec 2026 – Jan 2027
- **Print target: Feb 2027**

---

## Day-count map vs my Nov 2025 proposal

The Nov 2025 numbers I proposed are mostly unchanged. A few chapters have grown slightly to absorb the Responsible/Efficient AI material that was originally scoped into the (now-dropped) Ch 20:

| Ch (E3) | Title | Days proposed (Nov 2025) | Adj. for distributed RAI | Wave |
|---|---|---|---|---|
| 1  | Overview of DL with PyTorch | 18 | 18 | 1 |
| 2  | Deep CNN Architectures | 28 | 28 | 1 |
| 3  | Deep Recurrent Models | 16 | 16 | 1 |
| 4  | Transformers | 22 | 22 | 2 |
| 5  | Advanced Multimodal Models | 30 | 30 | 3 |
| 6  | Graph Neural Networks | 22 | **24** (+2, graph fairness) | 2 |
| 7  | Music and Text Generation | 22 | **25** (+3, text watermarking) | 3 |
| 8  | Fine-tuning LLMs | 30 | **32** (+2, model card + bias eval) | 3 |
| 9  | Deep Convolutional GANs | 22 | 22 | 2 |
| 10 | Image Generation w/ Diffusion | 18 | **21** (+3, image watermarking) | 3 |
| 11 | Deep RL (+ RLHF) | 27 | **29** (+2, reward hacking + red-team) | 3 |
| 12 | Model Training Optimizations | 18 | **23** (+5, QAT + sparsity + energy) | 2 |
| 13 | Operationalizing PyTorch | 25 | **29** (+4, Opacus DP-SGD + guardrails) | 2 |
| 14 | Mobile & Edge | 16 | **18** (+2, on-device efficiency) | 4 |
| 15 | Rapid Prototyping | 8 | 8 | 1 |
| 16 | PyTorch and AutoML | 15 | 15 | 4 |
| 17 | Explainable AI | 9 | 9 | 1 |
| 18 | Recommendation Systems (TorchRec) | 15 | 15 | 4 |
| 19 | PyTorch × Hugging Face | 16 | 16 | 4 |

Total: **~378 person-days** of focused writing time (was ~375 with the standalone Ch 20). Net effect of distributing Responsible/Efficient AI: roughly the same total effort, but spread across the book rather than concentrated in one tail chapter. Compressed against the **~5-month authoring window**, this still lands at ~17 person-days/week — only feasible by raising my weekly capacity to 18–22 focused writing hours and overlapping waves with editorial review. See "What this requires" below.

## What this requires

To honestly hit Feb 2027 print, a few things have to change vs the original Nov 2025 plan:

1. **My capacity goes up to 18–22 writing hours/week** (vs 10–12 baseline). I plan to block Tuesdays and Thursdays as protected writing days at Nativ for the duration; weekend mornings + evenings absorb the rest.
2. **Overlap, not stop-start.** I start the next wave the same week I deliver the previous wave's first drafts, instead of waiting for editorial review to come back. Author edits on prior wave happen in parallel with new-chapter drafting.
3. **Scope guardrails on the heavy new chapters.** Ch 5 (Multimodal) and Ch 8 (Fine-tuning LLMs) each get a "minimum viable chapter" cut and a "stretch" cut. If a Wave 3 chapter is at risk of slipping, we ship the MVC and move on. The distributed Responsible/Efficient AI sections inside Ch 6–14 are scoped as 2–5 day additions each — if any one is at risk, that section moves to a lighter "callout" instead of a hands-on subsection.
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
| Distributed Responsible/Efficient AI sections balloon and slow down host chapters | Each section is hard-capped (2–5 days); if a section is at risk, it degrades to a lighter callout instead of being skipped |
| Code rot in the 2E repo (libraries that have moved on) | Wave 1 deliberately front-loads refresh chapters so we catch and document API breakages early |
| Reviewer availability | Tech reviewer must be locked by **mid-June 2026** — happy to suggest names |
| Editorial review turnaround slips past 2 weeks | First thing to slip is the print date, not the chapter quality; would re-baseline transparently rather than rush |

---

## What I would like from Packt

1. ~~Confirmation on Ch 20 (Responsible & Efficient AI as a new chapter vs distributed sections).~~ **Closed 20 May:** distributed.
2. ~~Confirmation on dropping standalone Neural Style Transfer chapter.~~ **Closed 20 May:** dropped, folded into Ch 9.
3. Updated contract / schedule aligned to the **Feb 2027 print target** above.
4. A commitment to **2-week editorial review per chapter** through the compressed window — single biggest external dependency.
5. Reader-survey data for E2 → E3 (awaiting Sanjana's return from leave).
6. An (optional) standing 30-minute monthly check-in for the duration of the project (lighter touch than per-chapter sync, sharper than ad-hoc emails).

---

## Weekly cadence I will hold myself to

- **Monday:** ship a one-paragraph status note (what's in progress, what's due, blockers).
- **Friday:** push WIP commits to `MasteringPyTorchV3` GitHub repo so progress is visible, not just declared.
- **Per-chapter:** open a tracking issue with checklist (text, code, screenshots, references) so the editorial side can see exactly where each chapter sits.
