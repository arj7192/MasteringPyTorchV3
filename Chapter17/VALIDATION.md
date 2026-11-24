# Validation

Latest local check, 24 November 2026: All 11 language cells and all 10 vision cells completed in separate fresh Python CPU processes with cached model weights. Both optional flags were enabled. The previously reported scores for the core experiments matched the earlier runs.

- Joel has yellow, block 1: blue note -6.948, after swap +6.024, red note +6.023
- Joel has yellow, block 24: blue note -6.948, after swap -6.948, red note +6.023
- Black reference: +0.0039; IG sum: +0.0562; residual: +0.000159

These exact versions have not been rerun in Colab. The earlier hosted runs below refer to earlier notebook versions.

Earlier run on 24 November 2026: All 10 code cells of the revised language notebook completed in order in one fresh local Python CPU process using cached weights. Joel first: red, red-minus-blue score +4.447. Original scores, language IG and activation-patching results matched the previous run exactly. This revision has not been rerun in Colab. The vision notebook is unchanged; the optional black-baseline variation was checked locally with 256 IG steps, keeping the original photograph intact. Its start score was +0.003868 and its numerical residual was +0.000159.

Earlier notebook executions, 10 November 2026: Both reader notebooks match the exact cell sources executed in separate fresh local CPU kernels. All 19 code cells completed with no error outputs. Source fingerprints cover the cell types and source text, independently of saved outputs and notebook metadata.

## Local CPU execution

- Language: 10 cells, 142.7 seconds including cached model loading, plotting, and kernel execution; peak process resident memory 4.77 GiB. Python 3.12, macOS, PyTorch 2.15.0. Model: Qwen/Qwen3.5-0.8B, revision `2fc06364715b967f1860aea9cf38778875588b17`.
- Vision: 9 cells, 58.1 seconds including cached model loading, plotting, and kernel execution; peak process resident memory 1.40 GiB. Python 3.12, macOS, PyTorch 2.15.0. Model: google/siglip2-base-patch16-224, revision `75de2d55ec2d0b4efc50b3e9ad70dba96a7b2fa2`.

These are whole-process memory measurements, not GPU tensor allocation. First-time downloads add time and disk usage.

## Checks covered

- Language: candidate tokenization, prompt alignment, generated answers, input/embedding score agreement, IG convergence, unchanged score after capture, earlier-position negative control, same-input replacement, held-out names and unrelated-colour edits, and hook cleanup.
- Vision: exact model-input display alignment, finite gradients and IG, endpoint convergence for grey and blur, equal-area masks, all 20 seeded random scores, alternative descriptions and photographs, and neighbour ranks and values checked against direct cosine similarity.
- Reader access: both model repositories were confirmed public and ungated through requests without an authentication header. Neither notebook requires sign-in or a token. A Google account is needed when using Colab; local Jupyter does not require it.

## Hosted CPU checks

The language notebook completed all 10 sequential cells on a Google Colab CPU runtime with matching numerical results. The downloaded notebook retains the outputs and final execution count 10; reconnecting the frontend cleared some earlier counters.

The vision notebook completed all 9 cells in a separate fresh Colab CPU runtime, with execution counts 1–9 and no errors. Its attribution cell took approximately 11 minutes according to Colab's rounded timer. The grey-reference residual was +0.000074, the blur residual was -0.000009, and the similarities, mask scores, and neighbour ranking agreed closely with the local run. Peak process memory was approximately 1.75 GiB.

The final vision revision only changes the mask figure's layout and legend. That exact revision was rerun locally on 10 November; its final hosted rerun remains pending because browser control was disabled. Numerical calculations and checks are unchanged from the hosted execution. The hosted language execution predates the Joel-first addition.

Runtime and memory vary with hardware and library builds. CUDA, MPS, and native Windows execution have not been validated. No claim is made that every free hosted session supplies the same resources.
