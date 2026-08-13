from pathlib import Path
stage14 = Path(__file__).resolve().parents[1]
paths = {n: stage14 / d / "result.md" for n,d in [("4do","14-4do"),("s7-58","14-s7-58"),("t98","14-t98"),("bgX19","14-Work-bgX19")]}
for p in paths.values(): assert p.exists(), p
x=paths["bgX19"].read_text()
for token in ["COMMON_PHYSICAL_BOUNDARY_LANGUAGE_PROVED=true","DISJOINT_PRIME_MULTI_BOUNDARY_ACCUMULATION_PROVED=false","COMMON_ARITHMETIC_ADAPTER_PROVED=false","CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2"]: assert token in x
assert "FULL_ZERO_MODE_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_PROVED=false" in paths["s7-58"].read_text()
t=paths["t98"].read_text()
for token in ["SIGN_BOUNDARY_REDUCED_TO_O1_LINEAR_HALFSPACE_XOR=true","FOUR_CELL_BOUNDARY_REDUCED_TO_BO1_FIXED_DIVISOR_CONGRUENCE_XORS=true","ENDPOINT_BOUNDARY_REDUCED_TO_BO1_SMALL_MODULUS_RESIDUE_XORS=true"]: assert token in t
assert "ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true" in paths["4do"].read_text()
print("Stage14-Work-bgX19 corrected audit: PASS")
