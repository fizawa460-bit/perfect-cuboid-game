#!/usr/bin/env python3
# Explicit checks remain active under python -O.
"""Ten bounded semantic/failure cases in both normal and -O modes."""
import argparse, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def dump(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write-certificate', action='store_true')
    a = ap.parse_args()
    cert = json.loads((ROOT / 'F63-certificate.json').read_text())
    names = list(cert['files_sha256']) + ['F63-certificate.json']
    before = {x: sha(ROOT / x) for x in names}
    tests = ['altered_witness', 'altered_exact_relation', 'repeated_minor_row', 'altered_norm_coefficient', 'altered_bezout_coefficient', 'false_genus_one_claim', 'false_actual_adapter_claim', 'missing_odd_relation', 'false_credit_claim', 'empty_hash_table']
    rows = []
    for case in tests:
        with tempfile.TemporaryDirectory(prefix='f63-negative-') as tmp:
            r = Path(tmp)
            for name in names:
                dest = r / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, dest)
            c = json.loads((r / 'F63-certificate.json').read_text())
            changed = []
            if case == 'altered_witness':
                name = 'F63-witnesses97.json'
                d = json.loads((r / name).read_text())
                d['witnesses'][0][0] = (d['witnesses'][0][0] + 1) % 97
                d['even_witnesses'][0][0] = d['witnesses'][0][0]
                dump(r / name, d)
                changed = [name]
            elif case == 'altered_exact_relation':
                name = 'even/F63-EVEN-exact-relations.json'
                d = json.loads((r / name).read_text())
                d['relations'][0][0][1] = str(int(d['relations'][0][0][1]) + 1)
                dump(r / name, d)
                changed = [name]
            elif case == 'repeated_minor_row':
                name = 'odd/rank97.txt'
                lines = (r / name).read_text().splitlines()
                v = lines[1].split()
                v[1] = v[0]
                lines[1] = ' '.join(v)
                (r / name).write_text('\n'.join(lines) + '\n')
                changed = [name]
            elif case in ('altered_norm_coefficient', 'altered_bezout_coefficient'):
                name = 'F63-norm-slices97.json'
                d = json.loads((r / name).read_text())
                key = 'norms' if case == 'altered_norm_coefficient' else 'bezout'
                d['slices'][0][key][0][0] = (d['slices'][0][key][0][0] + 1) % 97
                dump(r / name, d)
                changed = [name]
            elif case == 'false_genus_one_claim':
                c['claims']['genus_one_proved'] = True
            elif case == 'false_actual_adapter_claim':
                c['claims']['actual_source_adapter_proved'] = True
            elif case == 'false_credit_claim':
                c['claims']['theorem_credit'] = 999
            elif case == 'empty_hash_table':
                c['files_sha256'] = {}
            else:
                (r / 'odd/F63-ODD-exact-relations.json').unlink()
            for name in changed:
                c['files_sha256'][name] = sha(r / name)
            dump(r / 'F63-certificate.json', c)
            for mode in ('normal', 'optimized'):
                command = [sys.executable] + (['-O'] if mode == 'optimized' else []) + [str(r / 'verify_f63.py')]
                z = subprocess.run(command, capture_output=True, text=True)
                if not z.returncode != 0:
                    raise ValueError('negative unexpectedly accepted: ' + case + ' ' + mode)
                rows.append({'case': case, 'mode': mode, 'rejected': True, 'payload_checksums_updated': bool(changed)})
    if not before == {x: sha(ROOT / x) for x in names}:
        raise ValueError('input payload changed')
    out = {'schema': 'MB104-F63-NEGATIVE-TESTS-v1', 'tests': rows, 'all_20_rejected': True, 'inputs_preserved': True}
    path = ROOT / 'F63-negative-tests.json'
    if a.write_certificate:
        dump(path, out)
    elif not json.loads(path.read_text()) == out:
        raise ValueError('verification condition failed')
    print(json.dumps({'status': 'PASS', 'negative_tests_rejected': 20, 'inputs_preserved': True}))
if __name__ == '__main__':
    main()
