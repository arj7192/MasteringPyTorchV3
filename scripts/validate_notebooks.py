#!/usr/bin/env python3
"""Execute notebooks with nbclient and write a JSON/Markdown report.

Usage:
  python scripts/validate_notebooks.py                  # all notebooks
  python scripts/validate_notebooks.py --wave1          # Wave 1 only
  python scripts/validate_notebooks.py Chapter01/       # path filter
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WAVE1 = [
    "Chapter01/mnist_pytorch.ipynb",
    "Chapter01/pytorch2x_compile_demo.ipynb",
    # mnist_tensorflow.ipynb intentionally skipped from default wave1 gate
    "Chapter02/lenet.ipynb",
    "Chapter02/transfer_learning_alexnet.ipynb",
    "Chapter02/vgg13_pretrained_run_inference.ipynb",
    "Chapter02/ResNetBlock.ipynb",
    "Chapter02/DenseNetBlock.ipynb",
    "Chapter02/GoogLeNet.ipynb",
    "Chapter03/rnn.ipynb",
    "Chapter03/lstm.ipynb",
    "Chapter15/fastai.ipynb",
    "Chapter15/pytorch_lightning.ipynb",
    "Chapter15/pytorch_profiler.ipynb",
    "Chapter17/captum_interpretability.ipynb",
    "Chapter17/pytorch_interpretability.ipynb",
]


def discover(paths: list[str] | None, wave1: bool) -> list[Path]:
    if wave1:
        return [ROOT / p for p in WAVE1 if (ROOT / p).exists()]
    if paths:
        out: list[Path] = []
        for p in paths:
            path = Path(p)
            if not path.is_absolute():
                path = ROOT / path
            if path.is_dir():
                out.extend(sorted(path.rglob("*.ipynb")))
            else:
                out.append(path)
        return [p for p in out if ".ipynb_checkpoints" not in str(p)]
    return sorted(
        p for p in ROOT.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(p)
    )


def run_one(path: Path, timeout: int) -> dict:
    from nbclient import NotebookClient
    from nbformat import read as nb_read

    started = time.time()
    result = {
        "path": str(path.relative_to(ROOT)),
        "status": "unknown",
        "seconds": 0.0,
        "error": None,
    }
    try:
        with path.open(encoding="utf-8") as f:
            nb = nb_read(f, as_version=4)
        client = NotebookClient(
            nb,
            timeout=timeout,
            kernel_name="python3",
            resources={"metadata": {"path": str(path.parent)}},
        )
        # Execute in the notebook's directory so relative data paths work
        cwd = os.getcwd()
        os.chdir(path.parent)
        try:
            client.execute()
        finally:
            os.chdir(cwd)
        result["status"] = "pass"
    except Exception as e:
        result["status"] = "fail"
        result["error"] = f"{type(e).__name__}: {e}"
        result["traceback"] = traceback.format_exc(limit=8)
    result["seconds"] = round(time.time() - started, 2)
    return result


def _ensure_ssl_certs() -> None:
    """macOS Python.org builds often lack system CA certs; point OpenSSL at certifi."""
    try:
        import certifi

        ca = certifi.where()
        os.environ.setdefault("SSL_CERT_FILE", ca)
        os.environ.setdefault("REQUESTS_CA_BUNDLE", ca)
        os.environ.setdefault("CURL_CA_BUNDLE", ca)
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Notebook or chapter paths")
    parser.add_argument("--wave1", action="store_true")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument(
        "--out",
        default=str(ROOT / "_planning" / "NOTEBOOK_VALIDATION.md"),
    )
    args = parser.parse_args()

    _ensure_ssl_certs()
    notebooks = discover(args.paths or None, args.wave1)
    if not notebooks:
        print("No notebooks found.")
        return 2

    print(f"Validating {len(notebooks)} notebooks (timeout={args.timeout}s each)")
    results = []
    for i, path in enumerate(notebooks, 1):
        print(f"[{i}/{len(notebooks)}] {path.relative_to(ROOT)} ...", flush=True)
        r = run_one(path, args.timeout)
        results.append(r)
        print(f"  → {r['status']} ({r['seconds']}s)")
        if r["error"]:
            print(f"     {r['error'][:300]}")

    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Notebook validation report",
        "",
        f"**When:** {now}",
        f"**Scope:** {'Wave 1' if args.wave1 else 'custom/all'}",
        f"**Result:** {passed} passed, {failed} failed, {len(results)} total",
        "",
        "| Notebook | Status | Seconds | Error |",
        "|---|---|---:|---|",
    ]
    for r in results:
        err = (r.get("error") or "").replace("|", "\\|").replace("\n", " ")[:180]
        lines.append(
            f"| `{r['path']}` | {r['status']} | {r['seconds']} | {err} |"
        )
    lines.append("")
    if failed:
        lines.append("## Failures (detail)")
        lines.append("")
        for r in results:
            if r["status"] != "fail":
                continue
            lines.append(f"### `{r['path']}`")
            lines.append("```")
            lines.append(r.get("traceback") or r.get("error") or "")
            lines.append("```")
            lines.append("")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out.with_suffix(".json")).write_text(
        json.dumps({"when": now, "results": results}, indent=2), encoding="utf-8"
    )
    print(f"\nWrote {out}")
    print(f"Summary: {passed} pass / {failed} fail / {len(results)} total")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
