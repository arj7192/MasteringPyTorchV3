# Mastering PyTorch 3E : Status board

**Last updated:** 3 Aug 2026

## Where we actually are

| Area | Status |
|---|---|
| Outline + change log + editorial decisions | ✅ Locked (May 2026) |
| Companion repo scaffolded | ✅ |
| Wave 1 first-draft chapters delivered to Packt | ❌ Not yet |
| Wave 2 | ❌ Not started (was due 24 Jul) |
| Contract / print-date confirmation from Packt | ⏳ Open |

**Honest bottom line:** planning and repo scaffolding are done; **no first-draft chapter manuscripts have been delivered**. Mechanical Wave 1 prep is now in the repo so Packt can see movement.

---

## Wave 1 progress (refresh chapters)

| Ch | Title | Manuscript | Code | What's left (Ashish) |
|---|---|---|---|---|
| 1 | Overview + PyTorch 2.x + RAI primer | 🟨 Prose drafts in `_drafts/` (2.x section + RAI primer) | 🟩 `mnist_*` + new `pytorch2x_compile_demo.ipynb` | Stitch drafts into Packt first-draft Word/Docs; run compile demo on GPU for screenshots |
| 2 | Deep CNN Architectures | ⬜ Not started | 🟨 V2 notebooks copied; `pretrained=True` → weights enum fixed | ConvNeXt v2 short section + GenAI-era CNN framing (author) |
| 3 | Deep Recurrent Models | ⬜ Not started | 🟨 V2 Ch4 notebooks copied (torchtext still legacy) | Migrate IMDB pipeline off torchtext → HF Datasets (author + code) |
| 15 | Rapid Prototyping | ⬜ Not started | 🟩 V2 notebooks copied; **poutyne removed** | Light prose refresh |
| 17 | Explainable AI | ⬜ Not started | 🟩 Captum notebooks copied | Light Captum refresh + optional LLM interpretability teaser |

Legend: 🟩 ready / 🟨 in progress / ⬜ not started / ❌ blocked

---

## Planned removals already applied in the repo

- ❌ E2 Ch 3 *Combining CNNs and LSTMs* - not copied (content moves into new Ch 5)
- ❌ E2 Ch 8 *Neural Style Transfer* - not copied as standalone (fold into Ch 9)
- ❌ `Chapter15/poutyne.ipynb` - deleted
- ❌ `Chapter07/..._gpt3.ipynb` - deleted
- ❌ `Chapter04/rand_wire_nn*` - deleted (ViT replaces RandWireNN)

---

## What only Ashish can do (high-value authorship)

These are the chapters/sections that need your judgment and voice - leave the mechanical work to scaffolding:

1. **Ch 5 - Advanced Multimodal Models** (entirely new)
2. **Ch 8 - Fine-tuning LLMs** (entirely new; Llama 3 + LoRA + DPO + RAG)
3. **Ch 4 - Vision Transformers** heavy new section
4. **Ch 6 - Graph Transformers** + fairness section
5. **Ch 7 - Llama 3 / MusicGen / text watermarking** (replace GPT-2/3 path)
6. **Ch 10 - SDXL + ControlNet + image watermarking**
7. **Ch 11 - RLHF / DPO / reward hacking**
8. **Ch 12–14** production/efficient-AI additions (FSDP, vLLM, ExecuTorch, Opacus, etc.)

---

## Re-baselined delivery ask (proposed to Packt)

| Milestone | Old date | Proposed new date |
|---|---|---|
| Wave 1 first drafts | 12 Jun 2026 | **Fri 29 Aug 2026** |
| Wave 2 first drafts | 24 Jul 2026 | **Fri 10 Oct 2026** |
| Wave 3 first drafts | 4 Sep 2026 | **Fri 12 Dec 2026** |
| Wave 4 first drafts | 16 Oct 2026 | **Fri 13 Feb 2027** |
| All final drafts | 4 Dec 2026 | **Fri 27 Mar 2027** |
| Print target | Feb 2027 | **May–Jun 2027** |

This is the honest schedule given current capacity. Feb 2027 print is no longer realistic without cutting scope hard.
