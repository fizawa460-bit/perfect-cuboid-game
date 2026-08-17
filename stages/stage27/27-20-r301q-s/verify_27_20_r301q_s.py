from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
STAGE = ROOT / "stages" / "stage27"

q = (STAGE / "27-20-r301q" / "result.md").read_text()
r = (STAGE / "27-20-r301r" / "result.md").read_text()
s = (STAGE / "27-20-r301s" / "result.md").read_text()
src = (STAGE / "27-20-r301r" / "source-justification.md").read_text()
reg = json.loads((STAGE / "27-20-r301q-s" / "batch-registry.json").read_text())
ctl = json.loads((STAGE / "27-controller.json").read_text())

# r301q exact receiver and height transfer
assert "X=\\delta z^2" in q
assert "Y=\\delta zV" in q
assert "Y^2=X(X-A)(X-B_0)" in q
assert "W^2=U(U-\\alpha)(U-\\beta)" in q
assert "ELLIPTIC_RECEIVER_MAP_DEGREE_AT_MOST_2=true" in q
assert "PHYSICAL_IMAGE_WEIL_HEIGHT_POLYNOMIAL_UNIFORM=true" in q
assert "UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=true" in q

# r301r source theorem and uniform point count
assert "SOURCE_ARXIV=2105.04032" in src
assert "SOURCE_THEOREM=Theorem_1.1" in src
assert "NACCARATO_THEOREM_1_1_ABSOLUTE_CONSTANTS=true" in src
assert "N_{\\mathcal E_{a,b}}(T_B)" in r
assert "=B^{o(1)}" in r
assert "UNIFORM_MOVING_Q1_DELTA_FIBER_SUBPOWER_PROVED=true" in r
assert "UNIFORM_FIXED_X_AGGREGATE_SUBPOWER_PROVED=true" in r
assert "FIXED_X_AGGREGATE_FIBER_EXPONENT=0" in r

# r301s support/population equivalence and scope firewall
assert "|Q(B)|\\le N_2(B)\\le |Q(B)|B^{o(1)}" in s
assert "N2_Q1_SUPPORT_EXPONENT_EQUIVALENCE_PROVED=true" in s
assert "N2_J_SUPPORT_EXPONENT_EQUIVALENCE_PROVED=true" in s
assert "INDEPENDENT_Q1_SUPPORT_DEFICIT_PROVED=false" in s
assert "STRICT_SUB_SQRT_UPPER_PROVED=false" in s
assert "NEXT_DERIVED_ROUTE=27-20-r301t" in s

# batch lifecycle
assert reg["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert reg["audit_status"] == "PENDING"
assert reg["merge_allowed"] is False
assert reg["advance_allowed"] is False
assert reg["fresh_reaudit_required"] is True
assert reg["numbering_contract"]["after_r301z"] == "Stage27-20-r302-main-batch"
assert reg["numbering_contract"]["r301aa_forbidden"] is True

# controller must retain checkpoint 40 and register all new routes.
assert ctl["checkpoint_status"]["50"] == "BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE"
for route in ("Stage27-20-r301q", "Stage27-20-r301r", "Stage27-20-r301s"):
    assert route in ctl["derived_routes"], route
    ent = ctl["derived_routes"][route]
    assert ent["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
    assert ent["audit_status"] == "PENDING"
    assert ent["merge_allowed"] is False
    assert ent["advance_allowed"] is False

assert ctl["derived_routes"]["Stage27-20-r301s"]["next_derived_route"] == "27-20-r301t"

print("Stage27-20-r301q-s verifier: PASS")
