from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

work = read("stages/stage14/14-Work-caX39/result.md")
matrix = read("docs/stage14-toolbox/work-caX39-receiver-matrix.md")
main = read("stages/stage14/14-4gh/result.md")
s = read("stages/stage14/14-s7-116/result.md")
t = read("stages/stage14/14-t152/result.md")
prior = read("stages/stage14/14-Work-bzX38/result.md")

assert "N_rec" in main and "FIRST_MOMENT" in main
assert "S_NONALIGNED_CRT_ADAPTER_PROVED=false" in s
assert "GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR_PROVED=true" in t
assert "Q_COMPONENT=COMPLETE" in prior
for token in [
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "Q_COMPONENT=NOT_TRIGGERED",
    "RESTRICTED_MAIN_S_FIXED_E_TWO_SIDED_ADAPTER_PROVED=true",
    "COMMON_ADAPTER_PROVED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert token in work
assert "fixed-E two-sided" in matrix
assert "forbidden" in matrix
print("STAGE14_WORK_CA_X39_AUDIT=OK")
