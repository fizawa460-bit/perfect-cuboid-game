#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE / "BOUNDED-RESULT.json"
RESULT_BLOB = "837ae21d2ef80a58d5d61bbfbedf5e4277ff5d0e"
RESULT_CANON = "b3387e3f07a02a30bfc5558ad72859c72c25a5289320abd22ac1947bf53b3d77"
PILOT = HERE / "bounded_exact_deletion_correlation.py"
PILOT_BLOB = "98d84c925af74c35b99001b08d8428f997ab63ea"
H08_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
H08_VERIFY_BLOB = "91020f335c416bf1265fd04b4571631cb6a0836c"
H08_PREFLIGHT_BLOB = "8ecc5ecd97838d4225de1d1163fd8843451b68e5"
H10_COUNTER_BLOB = "eebeb47f91df22461c33e9974d63aceca4da3b52"
H21_BOUNDED_BLOB = "266c7eb92fc971df24733f651c245cd14a32e494"
MANIFEST_BLOB = "0a46b34e278688240656b4977e9cb7f589e90e06"
H08_REJECTED = 25770706503487
H21 = 323299108813
H22 = 287982138108
GAIN = 35316970705


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(RESULT.is_file() and git_blob(RESULT) == RESULT_BLOB, "bounded result blob drift")
    req(PILOT.is_file() and git_blob(PILOT) == PILOT_BLOB, "bounded pilot blob drift")
    d = json.loads(RESULT.read_text())
    req(d.get("canonical_sha256_without_this_field") == RESULT_CANON, "stored result canonical drift")
    req(canonical(d) == RESULT_CANON, "result canonical drift")
    req(d["schema"] == "STAGE32EX5_HPADJ22_BOUNDED_EXACT_DELETION_CORRELATION_V1", "schema")
    req(d["status"] == "STRICT_BOUNDED_REFINEMENT_FOUND__FULL178_NOT_RUN", "status")

    src = d["source_locks"]
    req(src["hpadj21_bounded_pilot_blob_sha1"] == H21_BOUNDED_BLOB, "HPADJ21 source lock")
    req(src["hpadj08_audited_exact_head"] == H08_HEAD, "HPADJ08 head")
    req(src["hpadj08_bounded_verifier_blob_sha1"] == H08_VERIFY_BLOB, "HPADJ08 verifier lock")
    req(src["hpadj08_preflight_blob_sha1"] == H08_PREFLIGHT_BLOB, "HPADJ08 preflight lock")
    req(src["hpadj10_counter_blob_sha1"] == H10_COUNTER_BLOB, "HPADJ10 counter lock")
    req(src["full178_manifest_blob_sha1"] == MANIFEST_BLOB, "FULL178 manifest lock")

    scope = d["bounded_scope"]
    req(scope == {"H": 16, "max_d": 32, "row_count": 26, "tested_exact_cells": 208}, "bounded scope")

    cross = d["joint_histogram_crosscheck"]
    req(cross["joint_bruteforce_H"] == 4 and cross["joint_bruteforce_pass"] is True, "joint brute force")
    req(cross["qbc_marginal_cells_checked"] == 2312, "qBC marginal coverage")
    req(cross["parity_marginal_cells_checked"] == 2312, "parity marginal coverage")

    ident = d["exact_identity_checks"]
    req(ident["hpadj08_exact_square_rejected_terminals"] == H08_REJECTED, "HPADJ08 rejected total")
    req(ident["expected_hpadj08_exact_square_rejected_terminals"] == H08_REJECTED, "HPADJ08 expected total")
    req(ident["every_cell_pre_mass_matches_hpadj21"] is True, "pre-mass identity")
    req(ident["every_cell_hpadj08_rejected_mass_matches_retained_post_mass_certificate"] is True,
        "rejected-mass identity")
    req(ident["every_cell_post_mass_conservation_exact"] is True, "post-mass conservation")

    cand = d["candidate"]
    req(cand["hpadj21_bounded_cellwise_floor_sum"] == H21, "HPADJ21 bounded sum")
    req(cand["hpadj22_bounded_exact_survivor_sum"] == H22, "HPADJ22 bounded sum")
    req(cand["strict_improvement"] == GAIN and H21 - H22 == GAIN, "bounded gain")
    req(cand["strict_row_count"] == 26 and cand["all_rows_strict"] is True, "strict rows")
    req(cand["strict_cell_count"] == 36, "strict cells")
    req(cand["all_cells_no_weaker"] is True, "cellwise no-weaker")

    rows = d["rows"]
    req(len(rows) == 26 and len({r["row_id"] for r in rows}) == 26, "row coverage")
    req(all(r["strict"] is True for r in rows), "row strictness")
    req(all(int(r["hpadj22_exact_survivor_sum"]) <= int(r["hpadj21_floor_sum"]) for r in rows),
        "row no-weaker")
    req(sum(int(r["hpadj21_floor_sum"]) for r in rows) == H21, "row HPADJ21 sum")
    req(sum(int(r["hpadj22_exact_survivor_sum"]) for r in rows) == H22, "row HPADJ22 sum")
    req(sum(int(r["improvement"]) for r in rows) == GAIN, "row gain sum")
    req(sum(int(r["hpadj08_exact_square_rejected_terminals"]) for r in rows) == H08_REJECTED,
        "row HPADJ08 sum")

    sem = d["semantics"]
    req(sem["same_pre_domain_population_as_hpadj21"] is True, "population semantics")
    req(sem["same_picard_qA_survivor_rule_as_hpadj21"] is True, "Picard/qA semantics")
    req(sem["hpadj08_deletion_location_recomputed_exactly"] is True, "deletion correlation")
    req(sem["whole_x4_block_deletion"] is True, "whole-block semantics")
    req(sem["direct_refinement_not_additive_subtraction"] is True, "composition")
    req(sem["bounded_pilot_is_not_full178_numeric_replay"] is True, "bounded/full firewall")
    req(sem["main_consumption_performed"] is False, "MAIN consumption firewall")

    req(all(v is False for v in d["firewalls"].values()), "credit firewall")
    print("PASS: HPADJ22 bounded retained result is source-locked and canonical")
    print("PASS: 26/26 rows strict; 208 cells no-weaker; 36 strict cells")
    print("PASS: HPADJ08 exact-square rejected total 25770706503487 reproduced with exact cell conservation")
    print("PASS: HPADJ21 323299108813 -> HPADJ22 287982138108; bounded gain 35316970705")
    print("PASS: bounded evidence grants zero FULL178 / MAIN / theorem / endpoint credit")


if __name__ == "__main__":
    main()
