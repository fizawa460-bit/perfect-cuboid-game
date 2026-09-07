#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648h-full-g-deck-vs-box-stoll-type-separation.json"
EXPECTED = "704fc900f65c3f4c28140ff7d4907b94b2d0903c47af665ac2ac11df6105a655"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_locked(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file()
    assert blob_sha1(path) == lock["blob_sha1"]
    doc = json.loads(path.read_text())
    assert canonical(doc) == lock["canonical_sha256"]
    return doc


cert = json.loads(CERT.read_text())
assert canonical(cert) == EXPECTED
locks = cert["source_locks"]
common = load_locked(locks["common_double_cover"])
fullg = load_locked(locks["full_g_normalizer"])
relh = load_locked(locks["retained_relative_h_action"])

sq = common["group_quotient_square"]
assert sq["P"] == "Z x Z with diagonal G action"
assert sq["X"].startswith("P/H_diag")
assert sq["B"].startswith("P/G_diag")
assert sq["G"] == "Gamma[4]/Gamma[8], order 8"
assert "order 4" in sq["H"] and "normal index 2" in sq["H"]

chain = fullg["quotient_chain"]
assert chain["H_normal_index_in_G"] == 2
assert chain["C0_to_X4_degree"] == 2
assert chain["deck_involution_is_hyperelliptic"] is True
assert fullg["full_G_normalizer"]["choose_g_in_G_minus_H_lifting_tau"] is True
assert fullg["full_G_normalizer"]["X_to_B_equivariant"] is True

adapter = relh["equivariant_adapter"]
assert adapter["quotient_square"] == "pi o t_h = bar_t_h o pi for t_h represented by (h,1)"
assert adapter["modular_to_stoll"] == {"u":"g7*g9","uv":"g8*g9","v":"g7*g8"}

q = cert["quotient_type_check"]
assert q["X"] == "P/H_diag"
assert q["B"] == "P/G_diag"
assert q["G_over_H_order"] == 2
assert q["extra_involution_action_on_B"] == "identity, because B is the G_diag quotient"
assert q["retained_relative_H_words"] == {"u":"g7*g9","v":"g7*g8","uv":"g8*g9"}

d = cert["decision"]
assert d["result"] == "FULL_G_EXTRA_INVOLUTION_IS_NOT_A_NONTRIVIAL_BOX_STOLL_MEMBER"
assert d["post1629_nontrivial_stoll_T4_search_is_type_incompatible"] is True
assert d["post1648f_order8_boundary_kernel_promoted_to_modular_G"] is False
assert d["post1648g_four_outside_H_words_promoted_to_T4"] is False
assert d["survivors_current_credit"] == [73,97,235]
assert d["Q602_excluded"] is False and d["O210_excluded"] is False
assert not any(cert["firewalls"].values())

print("POST1648H_FULL_G_DECK_VS_BOX_STOLL_TYPE_SEPARATION_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("T4/nontrivial G/H deck acts upstairs on X and is identity on B=P/G_diag")
print("retained u,v,uv are relative (h,1) actions, not diagonal G/H deck")
print("nontrivial Stoll(B) search for T4=CLOSED_TYPE_MISMATCH")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
