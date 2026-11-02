#!/usr/bin/env python3
# Explicit checks remain active under python -O.
"""Read-only bounded certificates. Geometric deductions are in the F63 note."""
import argparse, hashlib, importlib.util, json, subprocess, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode = True
import norm_slices as n
import half_fiber
ROOT = Path(__file__).resolve().parent
P = 97
EXPECTED_FILES = {'F63-witnesses97.json', 'F63-norm-slices97.json', 'verify_f63.py', 'norm_slices.py', 'half_fiber.py', 'negative_tests.py'} | {parity + '/' + name for parity in ('even', 'odd') for name in ('build.py', 'check_exact.py', 'A97.bin', 'leading97.bin', 'evaluations97.bin', 'matrix97.json', 'rank97.txt', 'F63-' + parity.upper() + '-exact-relations.json')}

def dot(a, b):
    return sum((x * y for x, y in zip(a, b))) % P

def determinant(a):
    a = [list(r) for r in a]
    det = 1
    size = len(a)
    for c in range(size):
        p = next((j for j in range(c, size) if a[j][c]), None)
        if p is None:
            return 0
        if p != c:
            a[p], a[c] = (a[c], a[p])
            det = -det
        v = a[c][c]
        det = det * v % P
        iv = pow(v, -1, P)
        a[c] = [x * iv % P for x in a[c]]
        for j in range(c + 1, size):
            if a[j][c]:
                f = a[j][c]
                a[j] = [(x - f * y) % P for x, y in zip(a[j], a[c])]
    return det % P

def matrix_checks(parity):
    path = ROOT / parity
    meta = json.loads((path / 'matrix97.json').read_text())
    c = 344 if parity == 'even' else 340
    rank = 220 if parity == 'even' else 222
    if not (len(meta['columns']) == c and meta['rows'] == 224 and (meta['cover_order'] == 8)):
        raise ValueError('verification condition failed')
    raw = (path / 'A97.bin').read_bytes()
    lead = (path / 'leading97.bin').read_bytes()
    ev = (path / 'evaluations97.bin').read_bytes()
    if not (len(raw) == 224 * c and len(lead) == 14 * 9 * c and (len(ev) == 2 * c)):
        raise ValueError('verification condition failed')
    spec = importlib.util.spec_from_file_location('f63_' + parity, path / 'build.py')
    b = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b)
    with tempfile.TemporaryDirectory(prefix='f63-matrix-') as d:
        b.ROOT = Path(d)
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            b.main()
        for name in ('matrix97.json', 'A97.bin', 'leading97.bin', 'evaluations97.bin'):
            if not (Path(d) / name).read_bytes() == (path / name).read_bytes():
                raise ValueError('matrix rebuild mismatch: ' + parity + '/' + name)
    result = subprocess.run([sys.executable, str(path / 'check_exact.py')], capture_output=True, text=True)
    if not result.returncode == 0:
        raise ValueError(result.stderr or result.stdout)
    lines = (path / 'rank97.txt').read_text().splitlines()
    rows = list(map(int, lines[1].split()))
    cols = list(map(int, lines[2].split()))
    if not (len(rows) == rank and len(set(rows)) == rank and (len(set(cols)) == len(cols))):
        raise ValueError('verification condition failed')
    minor = [[raw[r * c + col] for col in cols[:rank]] for r in rows]
    det = determinant(minor)
    if not det:
        raise ValueError('verification condition failed')
    out = {'shape': [224, c], 'rank': rank, 'kernel_dimension': c - rank, 'minor_determinant': det}
    if parity == 'even':
        if not len(cols) == rank + 1:
            raise ValueError('verification condition failed')
        aug = [[raw[r * c + col] for col in cols] for r in rows] + [[ev[col] for col in cols]]
        out['evaluation_augmented_minor'] = determinant(aug)
        if not out['evaluation_augmented_minor']:
            raise ValueError('verification condition failed')
    return (meta, raw, lead, ev, out)

def excluded(columns, vectors):
    b, ii = (14, 22)
    e = ii * b % P
    c = (1 + ii) % P
    half = pow(2, -1, P)
    points = []
    for rz in (b, -b % P, e, -e % P):
        for uz in (b, -b % P):
            points.append(('hv_other', ('finite', rz, uz, 0), ('finite', e, b, 0)))
    for rw in (c, -c % P, ii * c % P, -ii * c % P):
        for vw in (e, -e % P):
            points.append(('hu_other', ('finite', ii * c % P, 0, e), ('finite', rw, 0, vw)))
    for ztype, zpoint in [('finite', ('finite', 0, 1, ii)), ('infinity', ('infinity', 0, half, half))]:
        for wtype in ('finite', 'infinity'):
            for su in (1, -1):
                for sv in (1, -1):
                    wp = ('finite', 0, su % P, sv * ii % P) if wtype == 'finite' else ('infinity', 0, su * half % P, sv * half % P)
                    points.append(('T_' + ztype + '_' + wtype, zpoint, wp))
    points.extend([('P27', ('finite', e, b, 0), ('finite', b, b, 0)), ('P35', ('finite', c, 0, e), ('finite', c, 0, -e % P))])

    def mon(leg, point):
        j, a, bb = leg
        kind, r, u, v = point
        if kind == 'infinity':
            return 0 if j + 2 * a + 2 * bb != 14 else pow(u, a, P) * pow(v, bb, P) % P
        return pow(r, j, P) * pow(u, a, P) * pow(v, bb, P) % P
    out = []
    for label, z, w in points:
        row = [mon(a, z) * mon(b, w) % P for a, b in columns]
        vals = []
        for s in vectors:
            a = dot(row, s)
            t = sum((v * x * (-1 if (zleg[0] + wleg[0]) % 2 else 1) for v, x, (zleg, wleg) in zip(row, s, columns))) % P
            if not (a and t):
                raise ValueError('half-section hits an excluded node: ' + label)
            vals.append([a, t, a * t % P])
        out.append({'type': label, 'values_s_tau_norm': vals})
    if not len(out) == 34:
        raise ValueError('verification condition failed')
    return out

def biquad_mul(a, b, u2, v2):
    out = [[], [], [], []]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            val = n.mul(x, y)
            if i & j & 1:
                val = n.mul(val, u2)
            if i & j & 2:
                val = n.mul(val, v2)
            out[i ^ j] = n.add(out[i ^ j], val)
    return out

def four_conjugates(parts, t):
    iv = pow(16, -1, P)
    q = t ** 4 % P
    u2 = [4 * (q + 4) * iv % P, 0, 0, 0, (q + 4) * iv % P]
    v2 = [-4 * (q - 4) * iv % P, 0, 0, 0, (q - 4) * iv % P]
    out = [[1], [], [], []]
    for su, sv in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        out = biquad_mul(out, [n.scale(x, s) for x, s in zip(parts, [1, su, sv, su * sv])], u2, v2)
    if not out[1:] == [[], [], []]:
        raise ValueError('verification condition failed')
    return out[0]

def claims():
    return {'scope': 'SOURCE_CONDITIONAL_COMPLEX_MODEL_RESEARCH_UNAUDITED_ZERO_CREDIT', 'half_degree_m1_dimension': 242, 'even_dimension': 124, 'odd_dimension': 118, 'half_exceptional_degree': 8, 'half_exceptional_h0': 9, 'image_dimension': 2, 'all_m_integral_split_norm_local_model_existence': True, 'supported_X_A1': 14, 'supported_Y_A1': 28, 'avoided_X_A1': 34, 'X_branches_per_support': '16*m', 'Y_branches_per_support': '8*m', 'balanced_Q': 0, 'half_strict_self_intersection': '672*m^2', 'half_strict_canonical_intersection': '224*m', 'half_strict_arithmetic_genus': '336*m^2+112*m+1', 'half_strict_genus_one_required_delta': '336*m^2+112*m', 'X_strict_genus_one_required_delta': '672*m^2+112*m', 'strict_mixed_delta': '336*m^2', 'genus_one_proved': False, 'actual_source_adapter_proved': False, 'actual_marked_conductor_evaluated': False, 'coreless_no_clump_proved': False, 'candidate_exclusion': 0, 'uniform_degree_bound': False, 'MB104': 'OPEN', 'independent_audit': False, 'theorem_credit': 0, 'receiver_credit': 0, 'endpoint_credit': 0}

def compute():
    data = json.loads((ROOT / 'F63-witnesses97.json').read_text())
    even = matrix_checks('even')
    odd = matrix_checks('odd')
    if not data['columns'] == even[0]['columns'] + odd[0]['columns']:
        raise ValueError('verification condition failed')
    if not len(data['witnesses']) == 2:
        raise ValueError('verification condition failed')
    forms = []
    for k, s in enumerate(data['witnesses']):
        if not (len(s) == 684 and s == data['even_witnesses'][k] + data['odd_witnesses'][k]):
            raise ValueError('verification condition failed')
        fs = []
        for mat, vec in ((even, s[:344]), (odd, s[344:])):
            c = len(vec)
            if not all((dot(mat[1][j * c:(j + 1) * c], vec) == 0 for j in range(224))):
                raise ValueError('verification condition failed')
        for j in range(14):
            ev = [dot(even[2][(j * 9 + i) * 344:(j * 9 + i + 1) * 344], s[:344]) for i in range(9)]
            od = [dot(odd[2][(j * 9 + i) * 340:(j * 9 + i + 1) * 340], s[344:]) for i in range(9)]
            f = n.add(ev, od)
            t = n.add(ev, n.scale(od, -1))
            b = n.mul(f, t)
            if not (len(b) == 17 and b[0] and b[-1]):
                raise ValueError('verification condition failed')
            if not n.gcd(b, [i * b[i] % P for i in range(1, len(b))]) == [1]:
                raise ValueError('verification condition failed')
            fs.append([f, t, b])
        forms.append(fs)
    if not data['forms'] == forms:
        raise ValueError('verification condition failed')
    if not all((n.gcd(f[2], g[2]) == [1] for f, g in zip(*forms))):
        raise ValueError('verification condition failed')
    ns = n.calculate()
    if not ns == json.loads((ROOT / 'F63-norm-slices97.json').read_text()):
        raise ValueError('verification condition failed')
    for row in ns['slices']:
        if not (row['degree'] == [56, 56] and all(row['leading_coefficients'])):
            raise ValueError('verification condition failed')
        for vec, expected in zip(data['witnesses'], row['norms']):
            if not four_conjugates(n.section_slice(data['columns'], vec, row['fixed_leg'], row['value']), row['value']) == expected:
                raise ValueError('verification condition failed')
        if not n.add(n.mul(row['bezout'][0], row['norms'][0]), n.mul(row['bezout'][1], row['norms'][1])) == [1]:
            raise ValueError('verification condition failed')
    if not 344 - 220 + 340 - 222 == 242 > 9:
        raise ValueError('verification condition failed')
    if not (7 ** 2 * 32 - 4 ** 2 * 28 * 2 == 672 and 7 * 32 == 224):
        raise ValueError('verification condition failed')
    if not 14 ** 2 * 16 - 8 ** 2 * 14 * 2 == 1344:
        raise ValueError('verification condition failed')
    return {'ranks': [even[4], odd[4]], 'half_fiber': half_fiber.calculate(), 'excluded_nodes': excluded(data['columns'], data['witnesses']), 'norm_slices': [{k: v for k, v in r.items() if k not in ('norms', 'bezout')} for r in ns['slices']]}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate', type=Path, default=ROOT / 'F63-certificate.json')
    args = p.parse_args()
    c = json.loads(args.certificate.read_text())
    if not (c['schema'] == 'MB104-F63-RESEARCH-CERT-v1' and c['claims'] == claims()):
        raise ValueError('claim scope mismatch')
    if not set(c['files_sha256']) == EXPECTED_FILES:
        raise ValueError('incomplete or unexpected dependency hash table')
    if not c['computed'] == compute():
        raise ValueError('computed certificate mismatch')
    for name, h in c['files_sha256'].items():
        if not hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == h:
            raise ValueError('checksum mismatch: ' + name)
    if not set(c) == {'schema', 'claims', 'computed', 'files_sha256'}:
        raise ValueError('verification condition failed')
    print(json.dumps({'status': 'PASS', 'half_degree_dimension': 242, 'rank_even': 220, 'rank_odd': 222, 'tangent_forms_checked': 28, 'avoided_X_nodes': 34, 'norm_coprime_slices': 2, 'all_m_split_integral_existence': 'conditional geometric deduction; see note', 'genus_one_proved': False, 'candidate_exclusion': 0, 'MB104': 'OPEN'}))
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('FAIL: ' + str(e), file=sys.stderr)
        sys.exit(1)
