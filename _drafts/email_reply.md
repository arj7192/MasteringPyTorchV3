# Email reply — Title Update, Mastering PyTorch 3E

**To:** Shashank Desai <shashankd@packt.com>
**Cc:** Sanjana Gupta <sanjanag@packt.com>; Tiksha Abhimanyu Lad <tikshas@packt.com>
**Subject:** Re: Title Update - Mastering Pytorch, 3E

---

Hi Shashank, Sanjana, Tiksha,

Thank you for your patience, and I'm sorry for the long silence on this. The honest version is that between fundraising and shipping at Nativ, and being unwell in April, this book has not had the attention it deserves from me — and I know that has been frustrating for the team. I'm writing today to fix that, not just to acknowledge it.

Rather than send another "I'll get back to you with a plan" note, I wanted this email to carry actual progress. I've spent today putting together four artifacts and re-baselining the schedule end-to-end:

1. **Updated outline (`OUTLINE_E3.md`)** — A clean third-edition outline that addresses the four points from the editorial board's October 2025 feedback:
   - **Subtitle updated** from PyTorch 1.x to PyTorch 2.x: *"Build, train, and deploy modern deep learning and generative AI systems with PyTorch 2.x"* (open to alternatives).
   - **New section in Chapter 1** — *"What's New in PyTorch 2.x: Compiling, Performance, and Integration for GenAI"* — exactly as suggested.
   - **Responsible and Efficient AI** added as a new dedicated **Chapter 21**, plus recurring "Responsible AI notes" in the LLM, diffusion, RL, and production chapters. Happy to redistribute as sections instead if you prefer.
   - Every chapter explicitly tagged with the 🟧 update / 🟩 new / 🟥 remove convention from the original color-coding pass, so the scope of change is unambiguous.

2. **Per-chapter change log (`CHANGE_LOG_2E_to_3E.md`)** — A clean editor-facing delta showing exactly what changes in each chapter, what stays, and what's dropped. Rough headline: ~25% net-new content, ~55–60% refactored, ~15–20% pure PyTorch 2.x refresh.

3. **Sample draft (`Chapter01_PyTorch2x_section.md`)** — The new Chapter 1 section, drafted in full at roughly book length (~3 pages). I wanted to send a concrete writing sample rather than just an outline bullet, so the editorial board can see the voice and depth I'm aiming for from page one.

4. **Re-baselined project plan (`PROJECT_PLAN.md`)** — A realistic four-wave delivery schedule. Honest about the slippage to date and explicit about what I can sustain alongside Nativ. The waves are sequenced so editorial review can start on refresh chapters in June while the heavy new content (Ch 6, 9, 21) is still being written. Headline dates:
   - Wave 1 (5 refresh chapters) — first drafts by **27 June 2026**
   - Wave 2 (5 heavy-refactor chapters) — first drafts by **22 August 2026**
   - Wave 3 (5 net-new/big-bet chapters, incl. Fine-tuning LLMs) — first drafts by **14 November 2026**
   - Wave 4 (6 tail chapters, incl. the new Responsible & Efficient AI chapter) — first drafts by **16 January 2027**
   - All final drafts by **27 February 2027**, with a realistic print target of **early Q2 2027**.

Companion artifacts I've also started today, so the technical side is moving in parallel: a new `MasteringPyTorchV3` GitHub repo skeleton (will publish once you confirm naming), a base `requirements.txt` pinned to PyTorch 2.x and the modern ecosystem (HF, vLLM, ExecuTorch, TorchRec, Opacus, etc.), and a per-chapter notebook inventory of what gets refreshed vs. rewritten from scratch.

To keep us in sync from here on out, I'd like to commit to:
- A short Monday status note from me every week (one paragraph: what's in flight, what's due, what's blocking).
- WIP pushes to the GitHub repo every Friday so progress is visible, not just declared.
- A 30-minute standing monthly check-in with the three of you for the duration of the project.

A few things I'd love your input on, so I can lock the outline this week:

1. Are you comfortable with **Chapter 21: Responsible and Efficient AI** as a new dedicated chapter, or would you prefer the coverage distributed as sections across existing chapters? My recommendation is the dedicated chapter plus the recurring callouts.
2. Are you comfortable dropping the standalone **Neural Style Transfer** chapter? It crowds out higher-impact GenAI content; I'd fold it in as a one-page historical bridge inside the GANs chapter.
3. Any preference between **Llama 3 / Qwen 2.5 / Mistral** as the headline open-weight LLM example? My instinct is to pick whichever has the most stable license over a 12-month print lifetime.
4. Was a reader survey collected for E2 → E3 (similar to what we did for E1 → E2)? If yes, please share — I'd like to fold findings into the next outline revision.

I can share the four documents above today in whatever form works best for the team (Google Drive, email attachments, or as a PR on a fresh `MasteringPyTorchV3` repo) — just let me know your preference and I'll send them across in the next email.

Thanks again for the patience and the nudges — they worked. Looking forward to getting this rolling properly.

Best,
Ashish

--
Ashish Ranjan Jha
Co-Founder & CEO, Nativ
