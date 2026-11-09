"""Replay retained C35-08/11/12 arithmetic in a temporary copy.

Uses the original source bytes. This is an arithmetic replay, not a new
independent mathematical audit or certification of the upstream source map.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import pickle
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


class FractionReader(pickle.Unpickler):
    def find_class(self, module, name):
        require((module, name) == ('fractions', 'Fraction'),
                'Unexpected pickle global: ' + module + '.' + name)
        return Fraction


def validate_mumford_inputs(folder):
    for name in ('E_26.pkl', 'F_8.pkl'):
        with (folder / 'coleman' / name).open('rb') as stream:
            value = FractionReader(stream).load()
            require(stream.read() == b'', 'Trailing pickle data')
        require(isinstance(value, (list, tuple)) and len(value) == 2,
                'Unexpected Mumford input structure')
        require(all(isinstance(poly, (list, tuple)) and 1 <= len(poly) <= 4
                    and all(isinstance(c, (int, Fraction)) for c in poly)
                    for poly in value), 'Unexpected Mumford coefficients')


def main(output):
    require(not sys.flags.optimize and os.environ.get('PYTHONOPTIMIZE') in (None, '', '0'),
            'Run without -O/PYTHONOPTIMIZE: retained author scripts use assert')
    require(output != ROOT and ROOT not in output.parents,
            'Write the receipt outside the frozen material directory')
    checked = subprocess.run([sys.executable, str(ROOT / 'verify_migration.py')],
                             capture_output=True, text=True)
    require(checked.returncode == 0, checked.stdout + checked.stderr)
    require(importlib.metadata.version('sympy') == '1.14.0', 'Use sympy==1.14.0')
    results = []
    with tempfile.TemporaryDirectory(prefix='stage35ex-parents-') as temp:
        target = Path(temp) / 'certificates'
        shutil.copytree(ROOT / 'parents' / 'C35-11-12', target,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        validate_mumford_inputs(target)
        jobs = [
            ('C35-11-reduced-support', [sys.executable, 'selmer/c35_11_reduced_support.py'],
             'selmer/c35_11_reduced_support.py', 'reduced_support.log'),
            ('C35-12-Cantor', [sys.executable, 'cantor_independent.py'],
             'cantor_independent.py', 'cantor.log'),
            ('C35-08-Coleman', [sys.executable, 'coleman/c35_08_independent_disk.py'],
             'coleman/c35_08_independent_disk.py', 'coleman_replay.log'),
            ('C35-10-bridge', [sys.executable, 'bridge/C35_10_exact_bridge.py'],
             'bridge/C35_10_exact_bridge.py', 'bridge_replay.log'),
            ('C35-12-direct-signed6', [sys.executable, 'direct_signed6.py'],
             'direct_signed6.py', 'direct_signed6.log'),
        ]
        for label, command, source, expected_log in jobs:
            print('RUN ' + label, flush=True)
            start = time.monotonic()
            child = subprocess.run(command, cwd=target, capture_output=True)
            result = {'label': label, 'source': source,
                      'command': [part if part != sys.executable else 'python' for part in command],
                      'exit_code': child.returncode,
                      'stdout_sha256': hashlib.sha256(child.stdout).hexdigest(),
                      'stderr_sha256': hashlib.sha256(child.stderr).hexdigest(),
                      'stdout': child.stdout.decode('utf-8', errors='replace'),
                      'stderr': child.stderr.decode('utf-8', errors='replace'),
                      'seconds': round(time.monotonic() - start, 3)}
            require(child.returncode == 0, json.dumps(result, ensure_ascii=False))
            expected = (target / expected_log).read_bytes()
            require(child.stdout == expected, label + ': stdout differs from retained log')
            result['retained_stdout_byte_identity'] = True
            results.append(result)
            print('PASS ' + label, flush=True)

        # The GP command-line executable is optional. The cypari2 adapter evaluates
        # exactly the retained GP program with only its terminal quit; removed.
        # It runs in a child process and reports its engine and actual PARI version.
        gp = shutil.which('gp')
        adapter = None
        if gp:
            command = [gp, '-q', 'global_cert.gp']
            engine = 'gp-command-line'
        else:
            require(importlib.metadata.version('cypari2') == '2.2.4', 'Use cypari2==2.2.4 or install gp')
            adapter = target / '_publication_pari_adapter.py'
            adapter.write_text(
                "from pathlib import Path\nfrom cypari2 import Pari\nimport re\n"
                "source=Path('global_cert.gp').read_text()\n"
                "source,n=re.subn(r'quit\\s*;\\s*\\Z','',source)\n"
                "if n != 1: raise RuntimeError('Expected one final quit;')\n"
                "Pari()(source)\n", encoding='utf-8')
            command = [sys.executable, adapter.name]
            engine = 'cypari2-2.2.4-terminal-quit-removed'
        print('RUN C35-11-PARI-global', flush=True)
        start = time.monotonic()
        child = subprocess.run(command, cwd=target, capture_output=True)
        stdout = child.stdout.decode('utf-8', errors='replace')
        require(child.returncode == 0, stdout + child.stderr.decode('utf-8', errors='replace'))
        for marker in ('BNFCERTIFY=1', 'DISC=55376', 'CLASS=1', 'INDEX=64',
                       'DISC_F=226820096', 'PRINCIPAL_PI=', 'PRINCIPAL_GA=', 'PRINCIPAL_GB='):
            require(marker in stdout, 'Missing PARI result: ' + marker)
        for key in ('SUPPLIED_BASIS_DET', 'UNIT_TRANSITION_DET'):
            match = re.search(key + r'=(-?\d+)', stdout)
            require(match is not None and abs(int(match[1])) == 1, key + ' is not a unit')
        version = re.search(r'PARI_VERSION=(.+)', stdout)
        require(version is not None, 'Missing PARI version')
        results.append({'label': 'C35-11-PARI-global', 'source': 'global_cert.gp',
                        'engine': engine, 'pari_version': version[1],
                        'exit_code': child.returncode,
                        'stdout_sha256': hashlib.sha256(child.stdout).hexdigest(),
                        'stderr_sha256': hashlib.sha256(child.stderr).hexdigest(),
                        'stdout': stdout, 'stderr': child.stderr.decode('utf-8', errors='replace'),
                        'seconds': round(time.monotonic() - start, 3),
                        'retained_log_byte_identity_required': False,
                        'reason': 'PARI version and chosen fundamental units may differ; certificate invariants are checked.'})
        print('PASS C35-11-PARI-global', flush=True)

    after = subprocess.run([sys.executable, str(ROOT / 'verify_migration.py')],
                           capture_output=True, text=True)
    require(after.returncode == 0, after.stdout + after.stderr)
    receipt = {'schema': 1, 'purpose': 'REPLAY_EXISTING_PARENT_CERTIFICATES',
               'independent_mathematical_audit': False, 'retained_files_unchanged': True,
               'temporary_copy_execution': True,
               'environment': {'python': sys.version, 'platform': platform.platform(),
                               'sympy': importlib.metadata.version('sympy')},
               'results': results, 'integrity_before': checked.stdout.strip(),
               'integrity_after': after.stdout.strip(),
               'scope': 'Six parent arithmetic checks; theorem applicability, analytic tail arguments and upstream adapters are retained mathematical dependencies.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS all six parent arithmetic replays; retained source bytes unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    main(args.output.resolve())
