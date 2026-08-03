#!/usr/bin/env python3
"""Static scan of notebooks for known-deprecated PyTorch / ecosystem APIs."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERNS = [
    (r"pretrained\s*=\s*True", "torchvision: use weights=Model_Weights.DEFAULT"),
    (r"from\s+torchtext", "torchtext: migrate to Hugging Face datasets / torchdata"),
    (r"import\s+torchtext", "torchtext: migrate to Hugging Face datasets / torchdata"),
    (r"import\s+gym\b", "gym: migrate to gymnasium"),
    (r"from\s+gym\b", "gym: migrate to gymnasium"),
    (r"torch\.jit\.script", "prefer torch.compile for new 3E examples (TorchScript still OK for export chapters)"),
    (r"torch\.cuda\.amp\.autocast", "prefer torch.amp.autocast('cuda', ...)"),
    (r"GradScaler\(\)", "prefer torch.amp.GradScaler('cuda', ...)"),
    (r"Variable\(", "torch.autograd.Variable is obsolete"),
    (r"\.data\b", "tensor .data is discouraged (review manually)"),
    (r"poutyne", "poutyne dropped in 3E"),
    (r"openai\.Completion|openai\.ChatCompletion", "legacy OpenAI API — remove / replace"),
]


def cell_source(cell) -> str:
    src = cell.get("source", "")
    return src if isinstance(src, str) else "".join(src)


def main() -> int:
    notebooks = sorted(ROOT.rglob("*.ipynb"))
    notebooks = [p for p in notebooks if ".ipynb_checkpoints" not in str(p)]
    hits = []
    for path in notebooks:
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            hits.append((path, f"PARSE_ERROR: {e}", ""))
            continue
        for i, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            text = cell_source(cell)
            for pat, note in PATTERNS:
                for m in re.finditer(pat, text):
                    line = text[: m.start()].count("\n") + 1
                    hits.append((path, f"cell {i} line ~{line}: {pat}", note))

    print(f"Scanned {len(notebooks)} notebooks\n")
    if not hits:
        print("No deprecated-pattern hits.")
        return 0

    by_file: dict[Path, list] = {}
    for path, where, note in hits:
        by_file.setdefault(path, []).append((where, note))

    for path, items in sorted(by_file.items(), key=lambda x: str(x[0])):
        rel = path.relative_to(ROOT)
        print(f"## {rel}")
        for where, note in items:
            print(f"  - {where}")
            print(f"    → {note}")
        print()

    print(f"TOTAL hits: {len(hits)} across {len(by_file)} notebooks")
    return 1


if __name__ == "__main__":
    sys.exit(main())
