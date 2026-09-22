#!/usr/bin/env python3
"""Reproduce immutable S1 checkpoints using only the Python standard library.

Run from any directory: python /path/to/repository/verify.py
Historical scripts use assertions; optimized Python is deliberately rejected.
Finite checks are not continuous-time proofs, empirical validation, or novelty audits.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CHECKPOINTS = (
    ("passive-2026-09-22", "MANIFEST.sha256", "validation.json",
     ("--output", "validation.json")),
    ("active-2026-09-22", "SHA256SUMS.txt", "RESULTS.json", ()),
)


def check_manifest(folder: Path, manifest: str) -> int:
    """Check every declared member and reject unexpected/missing checkpoint files."""
    seen: set[str] = set()
    for line in (folder / manifest).read_text(encoding="utf-8").splitlines():
        digest, name = line.split(maxsplit=1)
        if name in seen or Path(name).name != name or len(digest) != 64:
            raise ValueError(f"Invalid manifest entry in {folder}: {line!r}")
        seen.add(name)
        actual = hashlib.sha256((folder / name).read_bytes()).hexdigest()
        if actual != digest:
            raise RuntimeError(f"Checkpoint integrity mismatch: {folder / name}")
    actual_names = {p.name for p in folder.iterdir()}
    if actual_names != seen | {manifest}:
        raise RuntimeError(f"Unexpected/missing checkpoint members in {folder}")
    return len(seen)


def snapshot(folder: Path) -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.iterdir()) if p.is_file()}


def reproduce(name: str, manifest: str, report_name: str,
              arguments: tuple[str, ...]) -> dict:
    source = ROOT / "checkpoints" / name
    members = check_manifest(source, manifest)
    before = snapshot(source)
    expected = (source / report_name).read_bytes()
    with tempfile.TemporaryDirectory(prefix=f"s1-{name}-") as tmp:
        work = Path(tmp) / name
        shutil.copytree(source, work)
        env = dict(os.environ)
        env.pop("PYTHONOPTIMIZE", None)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        completed = subprocess.run(
            [sys.executable, "-B", "verify.py", *arguments], cwd=work,
            env=env, text=True, capture_output=True, timeout=120, check=False,
        )
        if completed.returncode:
            raise RuntimeError(f"{name} verifier failed:\n{completed.stdout}\n"
                               f"{completed.stderr}")
        actual = (work / report_name).read_bytes()
        report = json.loads(actual)
        if report != json.loads(expected):
            raise RuntimeError(f"{name}: regenerated report differs semantically")
        if actual != expected:
            raise RuntimeError(f"{name}: report matches values but not archived bytes")
        if report.get("status") != "PASS":
            raise RuntimeError(f"{name}: report did not record PASS")
        check_manifest(work, manifest)
    if snapshot(source) != before:
        raise RuntimeError(f"{name}: historical files were changed")
    return {
        "status": "PASS", "manifest_verified_files": members,
        "historical_files_unchanged": True, "report_byte_identical": True,
        "report_sha256": hashlib.sha256(actual).hexdigest(),
        "original_report": report,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "build" / "verification.json")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or newer is required")
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE; assertions must run")
    target = args.output.resolve()
    checkpoint_root = (ROOT / "checkpoints").resolve()
    if target == checkpoint_root or checkpoint_root in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    try:
        reports = {name: reproduce(name, manifest, report, arguments)
                   for name, manifest, report, arguments in CHECKPOINTS}
        result = {
            "schema_version": 1, "status": "PASS",
            "scope": "Checkpoint integrity and exact finite-report reproduction only; "
                     "not a theorem proof, empirical validation, or novelty audit.",
            "checkpoints": reports,
        }
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"Verification failed: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: both checkpoints reproduced without modifying originals.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
