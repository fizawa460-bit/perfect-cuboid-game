"""Mutation regressions: changed dependencies must never execute."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from mb104_fib_source_locks import LOCKS, ROOT

HERE = Path(__file__).resolve().parent


def main():
    targets = [*(ROOT / p for p in LOCKS), HERE / 'mb104_fib_source_locks.py']
    with tempfile.TemporaryDirectory() as td:
        marker = Path(td) / 'executed'
        for path in targets:
            original = path.read_bytes()
            try:
                path.write_bytes(original + (
                    '\nfrom pathlib import Path as _AuditPath\n'
                    f'_AuditPath({str(marker)!r}).write_text("executed")\n'
                    'raise RuntimeError("changed dependency executed")\n'
                ).encode())
                result = subprocess.run(
                    [sys.executable, str(HERE / 'derive_mb104_000707_gen30_adaptive_affine_cold.py'), '--output', str(Path(td) / 'out.json')],
                    cwd=ROOT, capture_output=True, text=True,
                    env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
                )
                if result.returncode == 0 or marker.exists() or 'source-lock mismatch before exec:' not in result.stderr:
                    raise AssertionError(f'changed dependency was not rejected before execution: {path}')
            finally:
                path.write_bytes(original)
            print(f'PASS pre-import rejection: {path.relative_to(ROOT)}')
    print('PASS: six dependency mutation regressions; original bytes restored')


if __name__ == '__main__':
    main()
