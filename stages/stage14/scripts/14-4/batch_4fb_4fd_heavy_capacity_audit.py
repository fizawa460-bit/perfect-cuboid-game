#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    '4fa': ROOT/'stages/stage14/14-4fa/result.md',
    '4fb': ROOT/'stages/stage14/14-4fb/result.md',
    '4fc': ROOT/'stages/stage14/14-4fc/result.md',
    '4fd': ROOT/'stages/stage14/14-4fd/result.md',
    'work': ROOT/'stages/stage14/14-Work-bpX28/result.md',
    'report': ROOT/'stages/stage14/14-4-batch/4fb-4fd-report.md',
}
for k,p in paths.items():
    assert p.exists(), (k,p)
t={k:p.read_text() for k,p in paths.items()}
assert 'UNIFORM_FIXED_AGREEMENT_RADIAL_SCALE_COUNT_MAX=B^(1/24+o(1))' in t['4fa']
assert 'OUTER_SUPPORT_CAPACITY_LEMMA_PROVED=true' in t['work']
for needle in [
    'HEAVY_RAY_ATOMIC_CAPACITY_EXPONENT=rho(phi)=1/4-phi',
    'UNIFORM_HEAVY_RAY_ATOMIC_MULTIPLICITY_BOUND=B^(1/24+o(1))',
]: assert needle in t['4fb'], needle
for needle in [
    'HEAVY_RAY_SURVIVAL_REQUIRES_MU_LE_1_4_MINUS_PHI=true',
    'UNIFORM_HEAVY_RAY_SURVIVAL_REQUIRES_MU_LE_1_24=true',
    'MU_GT_RADIAL_CAPACITY_FORCES_GENUINE_MOVER=true',
]: assert needle in t['4fc'], needle
for needle in [
    'SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))',
    'SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_UPPER_BOUND=B^(1/4-phi+o(1))',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'NEXT=Stage14-4fe',
]: assert needle in t['4fd'], needle
for needle in [
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'NEXT=Stage14-4fe',
]: assert needle in t['report'], needle
# Exponent arithmetic guard across phi in [5/24,1/4].
for i in range(0,101):
    phi = 5/24 + (1/4-5/24)*i/100
    rho = 1/4-phi
    assert rho <= 1/24 + 1e-12
    assert rho >= -1e-12
print('Stage14-main-batch 4fb-4fd audit: OK')
