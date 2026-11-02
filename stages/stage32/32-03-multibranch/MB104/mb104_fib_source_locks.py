"""Check the retained numeric dependency boundary before importing any of it."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[6]
LOCKS = {
    'stages/stage33/33-07/stoll_cuboid_source.py': '010db3767b8f932c71ac5722b50ccb64a8c79f9d',
    'stages/stage33/33-07/stage32_picard_marking_retained.py': '5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7',
    'stages/stage33/33-07/picard_base_rows_retained.py': '82e4d450a1d852e34f6615440fb88a029c6e54eb',
    'stages/stage32/residual-32-01-production/hperp_integral_adapter.py': 'fb1eb380ca786e42a6b00c5ef454b0e79fdba771',
    'stages/stage32/residual-32-01-production/pairing_prefix_engine.py': 'c8e87c6598fa1cd7ba1675fc35fa83bea983c94b',
}


def verify_before_import():
    for relative, expected in LOCKS.items():
        actual = subprocess.check_output(['git', 'hash-object', str(ROOT / relative)], cwd=ROOT, text=True).strip()
        if actual != expected:
            raise SystemExit(f'source-lock mismatch before exec: {relative}: {actual} != {expected}')
    return dict(LOCKS)
