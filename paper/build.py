#!/usr/bin/env python3
"""Build the editable working paper; auxiliary files stay in ignored build/."""
from pathlib import Path
import os
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "build" / "paper"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    # Fixed draft date; main.tex also omits pdfTeX's path-dependent trailer ID.
    env["SOURCE_DATE_EPOCH"] = "1790035200"
    env["FORCE_SOURCE_DATE"] = "1"
    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
         "-outdir=" + str(OUT), "main.tex"],
        cwd=HERE, env=env, check=True,
    )
    log = (OUT / "main.log").read_text(errors="replace")
    failures = ("There were undefined references", "There were undefined citations",
                "Overfull \\hbox", "Overfull \\vbox")
    present = [item for item in failures if item in log]
    if present:
        raise RuntimeError("Resolve manuscript build findings: " + ", ".join(present))
    destination = HERE / "manuscript.pdf"
    shutil.copyfile(OUT / "main.pdf", destination)
    print(f"Built {destination}")


if __name__ == "__main__":
    main()
