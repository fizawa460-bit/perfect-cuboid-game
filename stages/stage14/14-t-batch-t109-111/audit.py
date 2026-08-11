from pathlib import Path
from math import gcd

repo = Path(__file__).resolve().parents[3]
paths = {
    "t109": repo / "stages/stage14/14-t109/result.md",
    "t110": repo / "stages/stage14/14-t110/result.md",
    "t111": repo / "stages/stage14/14-t111/result.md",
    "th26": repo / "stages/stage14/14-tH26/result.md",
    "th28": repo / "stages/stage14/14-tH28/result.md",
}
for key, path in paths.items():
    assert path.exists(), (key, path)

texts = {key: path.read_text() for key, path in paths.items()}

for token in [
    "RAY_PHYSICAL_PREDICATE_FACTORS_EXACTLY=true",
    "RAY_FIXED_GAMMA_PRIME_DEPENDENCE_ONLY_PROJECTIVE_SELECTOR=true",
    "T109_MAY_CONSUME_TH28_FIXED_POWER_SAVING=false",
    "NEXT=Stage14-t110",
]:
    assert token in texts["t109"], token

for token in [
    "PROJECTIVE_CLASS_LIFT_TO_GAUSSIAN_RESIDUES_EXACT=true",
    "PROJECTIVE_CLASS_RESIDUE_UNION_SIZE=Bo1",
    "RAY_OCCUPANCY_REDUCED_TO_GAUSSIAN_PRIME_PROGRESSIONS=true",
    "NEXT=Stage14-t111",
]:
    assert token in texts["t110"], token

for token in [
    "PROJECTIVE_CLASSES_PARTITION_CANONICAL_PRIME_LABELS=true",
    "PROJECTIVE_CLASS_COUNT=Bo1",
    "UNIFORM_ALL_CLASS_FIXED_POWER_DEFICIT_IMPOSSIBLE=true",
    "ENDPOINT_PROJECTIVE_SELECTOR_STANDALONE_FIXED_POWER_SOURCE=false",
    "JOINT_COFACTOR_SELECTED_CLASS_PRIME_CORRELATION_REMAINS=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "T_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-t112",
]:
    assert token in texts["t111"], token

assert "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false" in texts["th26"]
assert "UNIFORM_FIXED_POWER_SAVING_PROVED=false" in texts["th28"]

for stage in ("t109", "t110", "t111"):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in texts[stage]
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in texts[stage]

# Finite quotient sanity: projective classes are orbits of invertible Gaussian
# residues under multiplication by rational units modulo d.
def units(d):
    return [s for s in range(d) if gcd(s, d) == 1]

def invertible_gaussian(a, b, d):
    return gcd((a * a + b * b) % d, d) == 1

def orbit(z, d):
    a, b = z
    return {(s * a % d, s * b % d) for s in units(d)}

def cls(z, d):
    return min(orbit(z, d))

checked = 0
for d in (3, 5, 7, 9, 13):
    elems = [(a, b) for a in range(d) for b in range(d)
             if invertible_gaussian(a, b, d)]
    buckets = {}
    for z in elems:
        buckets.setdefault(cls(z, d), set()).add(z)
    assert sum(len(v) for v in buckets.values()) == len(elems)
    assert len(buckets) <= d * d
    for rep, members in buckets.items():
        assert members == orbit(rep, d)
        assert len(members) <= len(units(d))
        checked += 1

print(f"Stage14-t-batch t109-t111 audit: OK; quotient classes checked={checked}")
