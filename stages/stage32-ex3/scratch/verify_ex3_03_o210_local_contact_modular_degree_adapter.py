#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-03-o210-local-contact-modular-degree-adapter.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"

art = json.loads(ART.read_text(encoding="utf-8"))
v6 = json.loads(V6.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
all140 = v6["witness"]["all140_pairings"]
assert len(all140) == 140
exc = all140[-48:]
assert exc == art["v6_exceptional_vector"]
assert sum(exc) == 266
assert sum(x & 1 for x in exc) == 26
assert sum(x // 2 for x in exc) == 120

# Exact O210 coarse split witness: m_j = x_j + 2 y_j.
y = art["coarse_node_split"]["example_y_j"]
x = art["coarse_node_split"]["example_x_j"]
assert len(x) == len(y) == len(exc) == 48
assert all(xx >= 0 and yy >= 0 and xx + 2 * yy == mm for xx, yy, mm in zip(x, y, exc))
assert sum(x) == 210
assert sum(y) == 28

# Boundary labels are 1-based positions in the first 92 retained normal curves.
def pairing(label: int) -> int:
    return all140[label - 1]

first_labels = [34, 35, 38, 39, 42, 43]
second_labels = [33, 36, 37, 40, 41, 44]
first_CL = [pairing(i) for i in first_labels]
second_CL = [pairing(i) for i in second_labels]
assert first_CL == [26, 31, 26, 25, 40, 34]
assert second_CL == [11, 22, 16, 11, 28, 22]
assert sum(first_CL) == 182
assert sum(second_CL) == 110
first_M = [105 - 2 * c for c in first_CL]
second_M = [81 - 2 * c for c in second_CL]
assert first_M == [53, 43, 53, 55, 25, 37]
assert second_M == [59, 37, 49, 59, 25, 37]
assert sum(first_M) == sum(second_M) == 266
assert all(m > 0 and m % 2 == 1 for m in first_M + second_M)

fc = art["factor_cusp_mass_ledgers"]["first_factor"]
sc = art["factor_cusp_mass_ledgers"]["second_factor"]
assert fc["C_dot_L"] == first_CL and fc["incident_exceptional_mass_M"] == first_M
assert sc["C_dot_L"] == second_CL and sc["incident_exceptional_mass_M"] == second_M

# Local source calculation.  Put e_z=a1/4 and e_w=a2/4.
# The translation-lattice relation a1+a2 == 0 mod 8 says e_z+e_w is even.
# The retained resolution adapter gives m=min(e_z,e_w).
for ez in range(1, 25):
    for ew in range(1, 25):
        if (ez + ew) % 2:
            continue
        m = min(ez, ew)
        assert (ez % 2) == (ew % 2) == (m % 2)

# First normalized quadratic base change is etale: e/gcd(e,2)=1, hence e=1 or 2.
def base_change_ram_index(e: int) -> int:
    return e if e % 2 else e // 2

assert [e for e in range(1, 20) if base_change_ram_index(e) == 1] == [1, 2]
# At exceptional O210 contacts parity then forces e_z=m for m=1,2.
for m in [1, 2]:
    candidates = [ez for ez in [1, 2] if ez >= m and ez % 2 == m % 2]
    assert candidates == [m]

# First cusp profile is rigid globally:
# 210 m1 exceptional -> e_z=1; 28 m2 exceptional -> e_z=2.
# No nonexceptional odd cusp point is possible because Y->N has exactly 210 branch points.
# Remaining cusp degree = 6*105 - (210+2*28) = 364, all in e_z=2 points.
remaining_first_degree = 6 * 105 - (210 + 2 * 28)
assert remaining_first_degree == 364
assert remaining_first_degree // 2 == 182 == sum(first_CL)
assert 28 + 182 == 210  # all first-factor 2-cycles

# Per-cusp first profile for any number y_L of m2 exceptional contacts.
for M, c in zip(first_M, first_CL):
    for yL in range(M // 2 + 1):
        a = M - 2 * yL
        b = c + yL
        assert a >= 1 and a % 2 == 1
        assert a + 2 * b == 105

# Second factor: write exceptional e_w=m+2r and nonexceptional cusp e_w=2s.
# If n is the total number of nonexceptional cusp points, exact boundary excess
# gives cusp ramification 2*(110-n); the remaining N->X4 ramification is n-86.
for n in range(86, 111):
    cusp_y_ram = 2 * (110 - n)
    outside_n_ram = n - 86
    outside_y_ram = 2 * outside_n_ram
    assert cusp_y_ram >= 0 and outside_n_ram >= 0
    assert cusp_y_ram + outside_y_ram == 48

# The symmetric 35-odd-cycle witnesses from EX3-01/02 cannot attach to this
# carrier cusp mass ledger: one exact cusp has total exceptional mass only 25.
assert min(first_M) == 25 < 35
assert min(second_M) == 25 < 35
assert art["effect_on_previous_scratch_witnesses"]["EX3_01_symmetric_105_witness_carrier_attachable"] is False
assert art["effect_on_previous_scratch_witnesses"]["EX3_02_symmetric_81_witness_carrier_attachable"] is False

verdict = art["diagnostic_verdict"]
assert verdict["local_contact_to_modular_degree_adapter_obtained"] is True
assert verdict["EX3_03_exclusion_obtained"] is False
assert all(value is False for value in art["firewalls"].values())

print("PASS EX3-03 scratch O210 local contact/modular-degree adapter")
print("first cusp masses:", first_M, "boundary excess:", first_CL)
print("second cusp masses:", second_M, "boundary excess:", second_CL)
print("first projection: exceptional e_z=m; 210 one-cycles + 210 two-cycles globally")
print("second projection: 86<=nonexceptional cusp points<=110; outside ramification 0..24")
print("symmetric EX3-01/02 witnesses are not carrier-attachable; full populations remain open")
