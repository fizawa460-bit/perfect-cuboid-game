#!/usr/bin/env python3
"""Normalize the generated t25 JSON to the committed theorem/finite summary."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'stages/stage14/data/14-t25/local_minimality_large_prime.json'

d = json.loads(P.read_text())
d.pop('rows', None)
P.write_text(json.dumps(d, indent=2) + '\n')
