#!/usr/bin/env python3
"""Prepare the exact four-orbit pure-geometric k=3 full-Q[4] universe."""
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_SCRIPT = HERE / 'certify_nonelementary_k3_geometric_q2_2q_support_orbits.py'
OUT = HERE / 'nonelementary-k3-geometric-q4-manifest.json'
NVAR = 24
X_MASK = (1 << 10) - 1

# Rebuild the complete pure-geometric predecessor.  It uses finite q support
# plus source coordinate symmetry only; arithmetic cc/ct is explicitly absent.
ns = runpy.run_path(str(SOURCE_SCRIPT))
source = json.loads((HERE / 'nonelementary-k3-geometric-q2-2q-support-orbits.json').read_text())
if source.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_Q2_2Q_SUPPORT_ORBITS_V1':
    raise SystemExit('geometric-support predecessor schema regression')
if source.get('arithmetic_generators_used') != []:
    raise SystemExit('geometric-support predecessor crossed arithmetic firewall')
if source.get('exact_support_survivor_orbit_count') != 4:
    raise SystemExit('geometric-support orbit count moved')

canon = ns['canon']
rank = ns['rank']

def complement(base, whole):
    current = list(canon(base))
    result = []
    for vector in canon(whole):
        if rank(current + [vector]) > len(current):
            current.append(vector)
            result.append(vector)
    return tuple(result)

def dot(a, b):
    return (int(a) & int(b)).bit_count() & 1

def section_equations(p_basis, quotient_basis):
    k = len(p_basis)
    q = len(quotient_basis)
    rows = []
    for i in range(k):
        for j in range(i):
            mask = 0
            for a, vector in enumerate(quotient_basis):
                if dot(vector & X_MASK, p_basis[j] & X_MASK):
                    mask ^= 1 << (q * i + a)
                if dot(vector & X_MASK, p_basis[i] & X_MASK):
                    mask ^= 1 << (q * j + a)
            constant = (
                (p_basis[i] & p_basis[j] & X_MASK).bit_count()
                + 2 * (p_basis[i] & p_basis[j] & ~X_MASK).bit_count()
            )
            if constant & 1:
                raise SystemExit('half-pairing parity regression')
            rows.append((mask, (constant // 2) & 1))
    return rows

def affine_rref(rows):
    mask_all = (1 << NVAR) - 1
    pivots = {}
    for mask, rhs in rows:
        value = int(mask) | ((int(rhs) & 1) << NVAR)
        coefficient = value & mask_all
        while coefficient:
            pivot = coefficient.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
                coefficient = value & mask_all
            else:
                for old in list(pivots):
                    if (pivots[old] >> pivot) & 1:
                        pivots[old] ^= value
                pivots[pivot] = value
                break
        if not coefficient and ((value >> NVAR) & 1):
            return None
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))

records = []
representative_total = 0
weighted_total = 0
for orbit_index, representative in enumerate(source['orbit_representatives']):
    p = tuple(map(int, representative['P_basis_bits']))
    w = tuple(map(int, representative['W_basis_bits']))
    orbit_size = int(representative['orbit_size'])
    t = int(representative['t'])
    expected_eqrank = int(representative['section_equation_rank'])
    if len(p) != 3 or len(w) != 6 or orbit_size != 9 or t not in (1, 2):
        raise SystemExit('geometric-support representative shape regression')
    quotient_basis = complement(w, canon(1 << j for j in range(14)))
    if len(quotient_basis) != 8:
        raise SystemExit('k3 quotient-basis dimension regression')
    reduced = affine_rref(section_equations(p, quotient_basis))
    if reduced is None:
        raise SystemExit('base lift-section fibre inconsistent')
    equation_rank = len(reduced)
    if equation_rank != expected_eqrank:
        raise SystemExit('section-equation rank moved from support certificate')
    dimension = NVAR - equation_rank
    expected_dimension = 22 if t == 1 else 21
    if dimension != expected_dimension:
        raise SystemExit('k3 pure-geometric affine dimension regression')
    section_count = 1 << dimension
    representative_total += section_count
    weighted_total += orbit_size * section_count
    records.append({
        'orbit_index': orbit_index,
        'orbit_size': orbit_size,
        't': t,
        'target_theta_image_rank': 4 - t,
        'P_basis_bits': list(p),
        'W_basis_bits': list(w),
        'quotient_basis_bits': list(quotient_basis),
        'section_equation_rank': equation_rank,
        'affine_dimension': dimension,
        'representative_section_count': section_count,
        'weighted_structural_H_count': orbit_size * section_count,
        'base_affine_rref_augmented': list(map(int, reduced)),
    })

if representative_total != 12582912:
    raise SystemExit(f'representative section total regression: {representative_total}')
if weighted_total != 113246208:
    raise SystemExit(f'weighted structural-H total regression: {weighted_total}')
if sorted((r['t'], r['affine_dimension']) for r in records) != [(1, 22), (1, 22), (2, 21), (2, 21)]:
    raise SystemExit('four-orbit fibre profile regression')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_Q4_MANIFEST_V1',
    'source_geometric_support_sha256': source['canonical_sha256'],
    'arithmetic_generators_used': [],
    'firewall': 'NO_ARITHMETIC_CC_CT_USED_IN_MANIFEST_OR_PREDECESSOR',
    'orbit_count': 4,
    'representative_section_count': representative_total,
    'weighted_structural_H_count': weighted_total,
    'coverage_partition': 'one canonical source-coordinate-symmetry representative per orbit; all affine lift sections retained',
    'records': records,
    'full_Q4_condition_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
}
raw = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
certificate['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'orbit_count': len(records),
    'representative_sections': representative_total,
    'weighted_H': weighted_total,
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
