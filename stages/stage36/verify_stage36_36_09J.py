#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json'
STATE = ROOT / 'stages/stage36/MAIN-STATE.json'
BASE = 'd761baa2d2d5e69479ef191041c5e2f017a50283'
CERT_BLOB = '72e9ca86f726f2ff286c983138d9381acdd97e62'
LOCKS = {
    ROOT / 'stages/stage36/36-09I/post-w01-breadth-refresh.json': 'f9bf252f3be47f606a3b270961df3b5943fa1909',
    ROOT / 'docs/arsenal/cards/formal/S31-W01.md': '122a6c1c5c871c1c7b797017e854de8ec55e7c50',
    ROOT / 'docs/research-os/policies/cycle-exploration-safety-protocol.md': '4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',
    ROOT / 'docs/research-os/policies/research-credit-and-promotion-firewalls.md': '7a3de0b2692afe4fb25b6825b31bd0384a118a41',
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


# Z-polynomials are coefficient lists in ascending degree.
def norm(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return norm(out)


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return norm(out)


def scale(a, k):
    return norm([k * x for x in a])


def powp(a, n):
    out = (1,)
    for _ in range(n):
        out = mul(out, a)
    return out


def evalp(a, z):
    s = 0
    for c in reversed(a):
        s = s * z + c
    return s


def mul_xpoly(a, b):
    # coefficients are Z-polynomials, ascending x-degree
    out = [(0,)] * (len(a) + len(b) - 1)
    out = [tuple(v) for v in out]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = add(out[i + j], mul(ai, bj))
    return out


def main() -> None:
    req(blob(CERT) == CERT_BLOB, '36-09J certificate blob drift')
    for p, sha in LOCKS.items():
        req(blob(p) == sha, f'locked 36-09J source drift: {p}')

    c = json.loads(CERT.read_text())
    req(c['schema'] == 'STAGE36_36_09J_RECIPROCAL_INVOLUTION_TWO_LINEAR_COVER_PREFLIGHT_V1', '36-09J schema moved')
    req(c['base_main_sha'] == BASE, '36-09J base moved')
    req(c['entry_authority']['36_09I_promotion_merged_main_sha'] == 'fc5886d62b78d8dcb21824ff02419a3e3b7634c8', '36-09I promotion merge moved')
    req(c['entry_authority']['36_09I_hostile_reaudit_review'] == 5121286430, '36-09I hostile re-audit provenance moved')

    ONE = (1,)
    Z = (0, 1)
    Zm2 = (-2, 1)
    Zp2 = (2, 1)
    Zm6 = (-6, 1)
    Zp6 = (6, 1)

    # Base conic discriminant in X.
    # (X+Z)*((Z-2)X+2(Z+6))
    a0 = Zm2
    b0 = add(powp(Z, 2), (12,))  # Z^2+12
    c0 = add(scale(powp(Z, 2), 2), scale(Z, 12))
    disc0 = sub(powp(b0, 2), scale(mul(a0, c0), 4))
    target_disc0 = mul(powp(Zm6, 2), powp(Zp2, 2))
    req(disc0 == target_disc0, f'base conic discriminant mismatch: {disc0}')

    # Middle quartic factors A and B in x.
    A = [ONE, Z, ONE]
    B = [Zm2, add(scale(Z, 2), (12,)), Zm2]

    discA = sub(powp(Z, 2), (4,))
    req(discA == mul(Zm2, Zp2), 'disc(A) mismatch')

    bB = add(scale(Z, 2), (12,))
    discB = sub(powp(bB, 2), scale(powp(Zm2, 2), 4))
    req(discB == scale(Zp2, 64), 'disc(B) mismatch')

    # resultant formula for quadratics:
    # Res(ax^2+bx+c, dx^2+ex+f)
    # = (af-cd)^2 - (ae-bd)(bf-ce)
    a, b, cc = ONE, Z, ONE
    d, e, f = Zm2, bB, Zm2
    af_cd = sub(mul(a, f), mul(cc, d))
    ae_bd = sub(mul(a, e), mul(b, d))
    bf_ce = sub(mul(b, f), mul(cc, e))
    res = sub(powp(af_cd, 2), mul(ae_bd, bf_ce))
    target_res = mul(powp(Zm6, 2), powp(Zp2, 2))
    req(res == target_res, f'Res(A,B) mismatch: {res}')

    quartic_disc = mul(mul(discA, discB), powp(res, 2))
    target_quartic_disc = scale(mul(mul(powp(Zm6, 4), Zm2), powp(Zp2, 6)), 64)
    req(quartic_disc == target_quartic_disc, 'quartic discriminant mismatch')

    F = mul_xpoly(A, B)
    req(len(F) == 5, 'middle model is not quartic')
    req(F[0] == Zm2 and F[4] == Zm2, 'quartic constant/leading coefficient moved')
    req(F[0] == F[4] and F[1] == F[3], 'quartic lost reciprocal palindromicity')

    # x=1 rational boundary point: F(1)=4(Z+2)^2.
    F1 = (0,)
    for coeff in F:
        F1 = add(F1, coeff)
    req(F1 == scale(powp(Zp2, 2), 4), 'x=1 boundary basepoint identity failed')

    # Physical Z excludes every degeneration.
    req(not (math.isqrt(8) ** 2 == 8), '8 unexpectedly square')
    bad = c['degeneracy_audit']['algebraic_bad_Z']
    req(bad == ['-2', '2', '6'], 'bad-Z list moved')
    req(c['degeneracy_audit']['all_algebraic_degeneracies_removed_on_physical_Z'] is True, 'physical degeneration firewall lost')

    # Smooth even-degree hyperelliptic genus formula g=(d-2)/2.
    genus0 = (2 - 2) // 2
    genus1 = (4 - 2) // 2
    genus3 = (8 - 2) // 2
    req((genus3, genus1, genus0) == (3, 1, 0), 'genus formula moved')
    tower = c['exact_cover_tower']
    req(tower['fiber_genus_sequence'] == [3, 1, 0], 'fiber genus sequence moved')
    req(tower['base_conic_C0']['genus_on_physical_Z'] == 0, 'base conic genus moved')
    req(tower['middle_quartic_C1']['genus_on_physical_Z'] == 1, 'middle quartic genus moved')
    req(tower['top_q_cover_C3']['genus_on_physical_Z'] == 3, 'top cover genus moved')
    req(tower['middle_quartic_C1']['map_to_C0']['degree'] == 2, 'middle-to-base degree moved')
    req(tower['top_q_cover_C3']['map_to_C1']['degree'] == 2, 'top-to-middle degree moved')
    req(tower['middle_quartic_C1']['rational_boundary_basepoint']['physical_receiver_point_credit'] is False, 'boundary basepoint leaked receiver credit')

    ars = c['arsenal_routing']
    req(ars['S31_W01_type_match'] is True, 'S31-W01 type match lost')
    req(ars['S31_W01_triggered'] is False, 'S31-W01 prematurely triggered')
    req(ars['S34_W01_retried'] is False and ars['S34_W03_triggered'] is False, 'unrelated Arsenal route prematurely changed')
    req(ars['next_exact_leaf_after_hostile_audit'] == '36-09K_GENUS_ONE_QUARTIC_ELLIPTIC_ADAPTER_PREFLIGHT', '36-09K routing moved')

    led = c['cycle_ledger_update']
    req(led['B3_FINITE_CURVE_OR_COVER_DECOMPOSITION'] == 'LIVE_EXACT_PHYSICAL_FIBER_TOWER_GENUS_3_1_0_WITH_GENUS_ONE_MIDDLE_ADAPTER_TARGET', 'B3 result moved')
    req(led['B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER'] == 'UNTESTED_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER', 'B7 overwritten')
    req(led['C2_GAUSSIAN_NORM_COMPRESSION'] == 'UNTESTED_DISTINCT_FROM_B7_NO_EXACT_EQUIVALENCE', 'C2 Gaussian candidate lost')
    req(led['B11_DIRECT_MULTIPLACE_ADELIC_RECIPROCITY'] == 'UNTESTED_VARIABLE_PRIME_RECIPROCITY', 'B11 candidate lost')
    req(led['counts'] == {'live': 1, 'untested': 3, 'blocked': 6, 'dominated': 2}, 'cycle counts moved')
    req(led['new_route_broadening_required'] is False, 'unexpected breadth reset')

    fire = c['scope_firewalls']
    req(fire['generic_cover_genera_classified'] is True and fire['fiberwise_physical_genus_tower_classified'] is True, '36-09J exact genus credit lost')
    for k in [
        'S31_W01_birational_adapter_triggered',
        'explicit_elliptic_model_derived',
        'quartic_rational_points_exhausted',
        'top_genus3_rational_points_exhausted',
        'receiver_emptiness_proved',
        'quotient_Q_point_emptiness_proved',
        'receiver_matched_replacement_theorem_proved',
        'R29_CAMP2_closed',
        'Q11_CAMPEDELLI_closed',
        'endpoint_closed',
        'perfect_cuboid_existence_claim',
        'perfect_cuboid_nonexistence_claim',
    ]:
        req(fire[k] is False, f'higher credit leaked: {k}')

    s = json.loads(STATE.read_text())
    req(s['schema'] == 'STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V32_36_09J_PENDING_HOSTILE_AUDIT', 'V32 schema moved')
    req(s['status'] == 'ACTIVE_PENDING_HOSTILE_AUDIT' and s['base_main_sha'] == BASE, 'V32 status/base moved')
    a = s['authority_frontier']['36-09J']
    req(a['certificate_blob_sha'] == CERT_BLOB, 'V32 certificate blob moved')
    req(a['PHYSICAL_FIBER_GENUS_SEQUENCE'] == [3, 1, 0], 'V32 genus sequence moved')
    req(a['S31_W01_TYPE_MATCH'] is True and a['S31_W01_TRIGGERED'] is False, 'V32 S31-W01 boundary moved')
    req(s['current']['36_09K_entry_allowed'] is False, '36-09K prematurely unlocked')
    req(s['promotion_gates']['generic_cover_genera_classified'] is True, 'V32 genus gate not set')
    req(s['promotion_gates']['genus_one_quartic_adapter_triggered'] is False, 'V32 adapter gate prematurely set')
    req(s['promotion_gates']['receiver_emptiness_proved'] is False and s['promotion_gates']['R29_CAMP2_closed'] is False, 'V32 closure credit leaked')
    req(all(v is False for v in s['claims'].values()), 'V32 high credit leaked')

    print('PASS STAGE36_36_09J_RECIPROCAL_COVER_PREFLIGHT')
    print('physical fiber tower: genus 3 -> genus 1 quartic -> genus 0 conic')
    print('S31-W01 type match confirmed but not triggered; explicit elliptic adapter remains next')
    print('36-09K locked pending hostile audit')


if __name__ == '__main__':
    main()
