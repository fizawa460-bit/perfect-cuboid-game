from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def text(rel: str) -> str:
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding="utf-8")


t135 = text("stages/stage14/archive/tasks/14-t135/result.md")
t157 = text("stages/stage14/archive/tasks/14-t157/result.md")
ab = text("stages/stage27/27-40ab/result.md")
result = text("stages/stage27/27-40ad/result.md")
audit = text("stages/stage27/27-40aa-ac/audit.md")

assert "h_d=B^o(1)" in t135
assert "d=B^o(1)" in t157
assert "PHYSICAL_PUSHFORWARD_WEIGHT_DEFINED=true" in ab
assert "FIXED_U_CLASS_UNIVERSE_SUBPOLYNOMIAL=true" in result
assert "FIXED_POWER_EXCEPTION_FRACTION_IMPLIES_EVENTUAL_ZERO_EXCEPTIONS=true" in result
assert "T_FIXED_U_CLASS_AVERAGING_ATTACK_EXECUTED=true" in result
assert "STRICT_SUB_SQRT_UPPER_PROVED=false" in result
assert "ADVANCE_TO_CHECKPOINT50=false" in audit
assert "AUDIT_VERDICT=PASS" in audit

print("Stage27-40ad verification: PASS")
