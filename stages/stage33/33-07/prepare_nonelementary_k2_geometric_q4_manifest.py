#!/usr/bin/env python3
"""Prepare the exact pure-geometric k=2 full-Q[4] section universe."""
import hashlib
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_SCRIPT = HERE / 'certify_nonelementary_k2_geometric_support_orbits.py'
OUT = HERE / 'nonelementary-k2-geometric-q4-manifest.json'
NVAR = 14
X_MASK = (1 << 10) - 1

# Rebuild the complete pure-geometric predecessor. It uses endpoint Q[2]/2Q
# support plus source integral coordinate symmetry only; arithmetic cc/ct is absent.
ns = runpy.run_path(str(SOURCE_SCRIPT))
source = json.loads((HERE / 'nonelementary-k2-geometric-support-orbits.json').read_text())
if source.get('schema') != 'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SUPPORT_ORBITS_V1':
    raise SystemExit('geometric-support predecessor schema regression')
if source.get('arithmetic_generators_used') != []:
    raise SystemExit('geometric-support predecessor crossed arithmetic firewall')
if source.get('exact_support_skeleton_orbit_count') != 1496:
    raise SystemExit('geometric-support orbit count moved')
if source.get('representative_lift_sections_for_next_exact_leaf') != 15548416:
    raise SystemExit('geometric-support representative section total moved')
if source.get('weighted_structural_H_count') != 988553216:
    raise SystemExit('geometric-support weighted H total moved')

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
profile = Counter()
for orbit_index, representative in enumerate(source['orbit_representatives']):
    p = tuple(map(int, representative['P_basis_bits']))
    w = tuple(map(int, representative['W_basis_bits']))
    orbit_size = int(representative['orbit_size'])
    t = int(representative['t'])
    expected_eqrank = int(representative['section_equation_rank'])
    if len(p) != 2 or len(w) != 7 or t not in (0, 1, 2):
        raise SystemExit('geometric-support representative shape regression')
    quotient_basis = complement(w, canon(1 << j for j in range(14)))
    if len(quotient_basis) != 7:
        raise SystemExit('k2 quotient-basis dimension regression')
    reduced = affine_rref(section_equations(p, quotient_basis))
    if reduced is None:
        raise SystemExit('base lift-section fibre inconsistent')
    equation_rank = len(reduced)
    if equation_rank != expected_eqrank or equation_rank not in (0, 1):
        raise SystemExit('section-equation rank moved from support certificate')
    dimension = NVAR - equation_rank
    if dimension not in (13, 14):
        raise SystemExit('k2 pure-geometric affine dimension regression')
    section_count = 1 << dimension
    if section_count != int(representative['lift_section_fibre_size']):
        raise SystemExit('source lift-section fibre size moved')
    representative_total += section_count
    weighted_total += orbit_size * section_count
    profile[(t, equation_rank, dimension)] += 1
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

if len(records) != 1496:
    raise SystemExit(f'orbit record count regression: {len(records)}')
if representative_total != 15548416:
    raise SystemExit(f'representative section total regression: {representative_total}')
if weighted_total != 988553216:
    raise SystemExit(f'weighted structural-H total regression: {weighted_total}')
expected_profile = Counter({(0, 0, 14): 402, (1, 1, 13): 964, (2, 1, 13): 130})
if profile != expected_profile:
    raise SystemExit(f'k2 orbit fibre profile regression: {profile}')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_Q4_MANIFEST_V1',
    'source_geometric_support_sha256': source['canonical_sha256'],
    'arithmetic_generators_used': [],
    'firewall': 'NO_ARITHMETIC_CC_CT_USED_IN_MANIFEST_OR_PREDECESSOR',
    'orbit_count': len(records),
    'orbit_profile_by_t_eqrank_dimension': {
        f't={t},eqrank={r},dim={d}': n for (t, r, d), n in sorted(profile.items())
    },
    'representative_section_count': representative_total,
    'weighted_structural_H_count': weighted_total,
    'coverage_partition': 'one canonical source-coordinate-symmetry representative per support-skeleton orbit; all affine lift sections retained',
    'records': records,
    'full_Q4_condition_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'unit_status': 'RUNNING_REPAIR',
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'theorem_credit': False,
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
    'profile': {f'{k}': v for k, v in sorted(profile.items())},
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
