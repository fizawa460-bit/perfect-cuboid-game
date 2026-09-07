#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648t-krr-official-ancillary-marked-g-bounded-negative.json"
EXPECTED = "32526ad10b38309fc7e4f27ed0228c6272775898add4ef8dc2136262cbdf4f23"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

for lock_name in ("post1648S", "source_note"):
    lock = cert["source_locks"][lock_name]
    path = ROOT / lock["path"]
    assert path.is_file()
    assert blob_sha1(path) == lock["git_blob_sha1"]

parent = json.loads((ROOT / cert["source_locks"]["post1648S"]["path"]).read_text())
assert canonical(parent) == cert["source_locks"]["post1648S"]["canonical_sha256"]
assert parent["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert parent["decision"]["survivors_current_credit"] == [73, 97, 235]
assert "an actual source-bound conjugating element" in parent["anti_loop_theorem"]["not_closed"]

ext = cert["external_source_lock"]
assert ext["paper"]["arxiv"] == "1904.00793v4"
assert ext["official_arxiv_ancillary"]["inventory"] == ["Magma_KRR.pdf"]
assert ext["official_arxiv_ancillary"]["page_count"] == 2
assert ext["official_arxiv_ancillary"]["complete_section_headers"] == ["Section 5.3", "Section 6.1"]

bounded = cert["bounded_ancillary_inspection"]
assert bounded["scope"] == "ONLY_THE_OFFICIAL_ARXIV_V4_ANCILLARY_INVENTORY_AND_THE_CITED_SECTION4_LOCATOR"
assert bounded["global_absence_claim"] is False
for key in (
    "section4_code_present",
    "explicit_conjugating_g_on_A_present",
    "explicit_g_homology_matrix_present",
    "explicit_g_on_A2_present",
    "kkk_canonical_basis_change_present",
    "branch_point_to_half_characteristic_table_present",
    "marked_theta_divisor_normalization_present",
):
    assert bounded[key] is False

dec = cert["decision"]
assert dec["krr_official_ancillary_actual_g_route_closed_bounded"] is True
assert dec["absolute_delta0inf_retained_W_line_identified"] is False
assert dec["survivors_current_credit"] == [73, 97, 235]
assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
assert not any(cert["firewalls"].values())

note = (ROOT / cert["source_locks"]["source_note"]["path"]).read_text()
for needle in ("Magma_KRR.pdf", "Section 5.3", "Section 6.1", "Corollary 6", "bounded"):
    assert needle in note

print("POST1648T_KRR_OFFICIAL_ANCILLARY_MARKED_G_BOUNDED_NEGATIVE_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("official_ancillary_inventory=Magma_KRR.pdf pages=2 sections=5.3,6.1")
print("actual_g_materialized=false marked_half_period_materialized=false")
print("bounded_negative_only=true global_absence_claim=false")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
