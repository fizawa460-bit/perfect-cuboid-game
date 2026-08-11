from pathlib import Path

root = Path(__file__).resolve().parents[3]
checks = {
    "4do": root / "14-4do" / "result.md",
    "s7-58": root / "14-s7-58" / "result.md",
    "t98": root / "14-t98" / "result.md",
    "bgX19": root / "14-Work-bgX19" / "result.md",
}
for name, path in checks.items():
    assert path.exists(), (name, path)

x = checks["bgX19"].read_text()
for token in [
    "COMMON_PHYSICAL_BOUNDARY_LANGUAGE_PROVED=true",
    "DISJOINT_PRIME_MULTI_BOUNDARY_ACCUMULATION_PROVED=false",
    "COMMON_ARITHMETIC_ADAPTER_PROVED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "Disjoint-Prime Physical Boundary Accumulation Lemma",
]:
    assert token in x, token

s = checks["s7-58"].read_text()
assert "FULL_ZERO_MODE_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_PROVED=false" in s

t = checks["t98"].read_text()
assert "SIGN_BOUNDARY_REDUCED_TO_O1_LINEAR_HALFSPACE_XOR=true" in t
assert "FOUR_CELL_BOUNDARY_REDUCED_TO_BO1_FIXED_DIVISOR_CONGRUENCE_XORS=true" in t
assert "ENDPOINT_BOUNDARY_REDUCED_TO_BO1_SMALL_MODULUS_RESIDUE_XORS=true" in t

m = checks["4do"].read_text()
assert "ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true" in m

print("Stage14-Work-bgX19 audit: PASS")
