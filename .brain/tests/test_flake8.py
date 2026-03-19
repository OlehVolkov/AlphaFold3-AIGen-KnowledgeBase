from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_flake8_passes_for_brain_codebase() -> None:
    project_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "flake8", "brain", "tests"],
        cwd=project_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout + result.stderr)
