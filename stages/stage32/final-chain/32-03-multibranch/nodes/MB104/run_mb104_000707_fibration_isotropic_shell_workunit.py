#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

import run_mb104_000707_fibration_isotropic_shells as engine


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shell-index", type=int, required=True, choices=range(len(engine.SHELLS)))
    ap.add_argument("--output", required=True)
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args()

    all_shells = [dict(x) for x in engine.SHELLS]
    engine.SHELLS = [all_shells[args.shell_index]]
    sys.argv = [
        sys.argv[0],
        "--output",
        args.output,
        "--timeout",
        str(args.timeout),
    ]
    engine.main()


if __name__ == "__main__":
    main()
