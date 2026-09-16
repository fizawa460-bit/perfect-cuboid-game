#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HPADJ10_SCRIPT = ROOT / "stages/stage32-ex5/hpadj-10_ex5/count_hpadj_kernel_population.py"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
FAMILY = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"

LOCKS = {
    "hpadj10_counter_blob": "eebeb47f91df22461c33e9974d63aceca4da3b52",
    "manifest_blob": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
}

TD01 = {
    "producer_pr": 1815,
    "audited_exact_head": "54945927416a94a67533c7b06c59c5a24e50c4f1",
    "hostile_audit_review_id": 5214778974,
    "post_audit_sync_head": "ce808eb50d9b75e9c5994b083939e7e2f65e276c",
    "exact_bound_packet_blob_sha1": "51271c11078459ad9171138c4fb6121d7a665c39",
    "exact_bound_packet_canonical_sha256": "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d",
    "main_handoff_canonical_sha256": "09b1bb55b8bdfbe844258d8ad7d112d78c25c4397f08675c9c4c3b1f4a000469",
    "replay_domain_exact_terminals": 47589703313957134107892,
    "hpadj08_survivor_envelope_terminals": 6703403803993209250491,
    "td01_17_over_33_upper_bound": 3453268626299532038131,
}

V30 = {
    "main_pr": 1808,
    "authority_head": "cfc23c7c633fa4192c281c8ba6a356ec071fc305",
    "hostile_audit_review_id": 5209163478,
    "remaining_terminal_upper_bound": 6703403803993210101494,
    "semantics": "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
}


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_hpadj10_module():
    # Fail closed before executing the retained HPADJ10 combinatorial code.
    req(HPADJ10_SCRIPT.is_file(), "missing retained HPADJ10 counter")
    req(git_blob(HPADJ10_SCRIPT) == LOCKS["hpadj10_counter_blob"], "HPADJ10 counter blob drift")
    req(MANIFEST.is_file() and git_blob(MANIFEST) == LOCKS["manifest_blob"], "FULL178 manifest blob drift")
    req(FAMILY.is_file() and git_blob(FAMILY) == LOCKS["family_blob"], "compressed terminal family blob drift")
    spec = importlib.util.spec_from_file_location("hpadj10_counter_locked", HPADJ10_SCRIPT)
    req(spec is not None and spec.loader is not None, "cannot load retained HPADJ10 counter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def census_pre_hpadj08_blocks(mod) -> dict:
    manifest = mod.load_locked_json(
        MANIFEST,
        LOCKS["manifest_blob"],
        LOCKS["manifest_canonical"],
        "FULL178 manifest",
    )
    rows = mod.manifest_rows(manifest)
    H = max(d // 2 for _, _, d in rows)
    BC = mod.build_bc_exact_parity(H)

    total_blocks = 0
    total_terms = 0
    per_row = []

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = mod.ceil_div(d - 16 * g + 16, 4)
        row_blocks = 0
        row_terms = 0
        A = [[mod.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]

        for b in range(h + 1):
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = mod.component3(d, b, c)
                if c3 < 0:
                    continue
                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = mod.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    scount = [0 for _ in range(11)]
                    for sbc, pair in enumerate(bcv):
                        left = int(pair[0]) + int(pair[1])
                        if not left:
                            continue
                        for sa, right in enumerate(avec):
                            if right:
                                scount[sbc + sa] += left * right

                    for support, count in enumerate(scount):
                        if not count:
                            continue
                        qneed = K - support
                        if qneed > 0 and srem < qneed:
                            continue
                        lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                        upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                        if lower > upper:
                            continue
                        excluded: set[int] = set()
                        e_n358 = 3 * d - (b - c)
                        if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                            excluded.add(e_n358)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        ne, normal_sum = mod.even_interval_normal_sum(d, lower, upper, excluded)
                        if ne <= 0:
                            continue
                        row_blocks += count * ne
                        row_terms += count * normal_sum

        req(row_terms > 0, f"pre-HPADJ08 row unexpectedly empty {row_id}")
        total_blocks += row_blocks
        total_terms += row_terms
        per_row.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "pre_hpadj08_x4_complete_blocks": row_blocks,
            "pre_hpadj08_replay_domain_terminals": row_terms,
        })

    req(len(per_row) == 178, "FULL178 row count drift")
    req(
        total_terms == TD01["replay_domain_exact_terminals"],
        "TD01 pre-HPADJ08 replay-domain terminal total mismatch",
    )

    stream = hashlib.sha256()
    for rec in sorted(per_row, key=lambda r: (r["g"], r["d"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    return {
        "rows": per_row,
        "pre_hpadj08_x4_complete_blocks": total_blocks,
        "pre_hpadj08_replay_domain_terminals": total_terms,
        "row_stream_sha256": stream.hexdigest(),
    }


def main() -> None:
    mod = load_hpadj10_module()
    result = census_pre_hpadj08_blocks(mod)

    survivor_terms = TD01["hpadj08_survivor_envelope_terminals"]
    pre_blocks = result["pre_hpadj08_x4_complete_blocks"]

    # Every retained x4 block has odd size B=N+1 with N even. For one parity
    # character at most ceil(B/2)=(B+1)/2 terminals survive. The exact HPADJ08
    # survivor block count is <= the pre-HPADJ08 block count, hence this is a
    # conservative current-envelope upper bound that needs no identity-set
    # interpretation of V30 MAIN.
    block_count_refined_upper_bound = (survivor_terms + pre_blocks) // 2
    block_count_refined_rejection_lower_bound = survivor_terms - block_count_refined_upper_bound
    td01_bound = TD01["td01_17_over_33_upper_bound"]
    improvement_vs_td01 = td01_bound - block_count_refined_upper_bound

    req(block_count_refined_upper_bound <= survivor_terms, "refined bound exceeds source envelope")
    req(block_count_refined_rejection_lower_bound >= 0, "negative rejection lower bound")

    out = {
        "schema": "STAGE32EX5_HPADJ11_TD01_ENVELOPE_BLOCKCOUNT_REFINEMENT_V1",
        "status": "EXACT_PRE_HPADJ08_BLOCK_CENSUS_WITH_CONSERVATIVE_SAME_CHARACTER_ENVELOPE_BOUND_AUDIT_REQUIRED",
        "route_id": "HPADJ-11_ex5",
        "sources": {
            "hpadj10_counter_blob_sha1": LOCKS["hpadj10_counter_blob"],
            "full178_manifest_blob_sha1": LOCKS["manifest_blob"],
            "full178_manifest_canonical_sha256": LOCKS["manifest_canonical"],
            "compressed_terminal_family_blob_sha1": LOCKS["family_blob"],
            "td01": TD01,
            "v30_main": V30,
        },
        "exact_replay": {
            "affected_rows": 178,
            "pre_hpadj08_x4_complete_blocks": pre_blocks,
            "pre_hpadj08_replay_domain_terminals": result["pre_hpadj08_replay_domain_terminals"],
            "expected_td01_replay_domain_terminals": TD01["replay_domain_exact_terminals"],
            "replay_domain_terminal_total_exact_match": True,
            "row_stream_sha256": result["row_stream_sha256"],
        },
        "same_character_bound": {
            "hpadj08_survivor_envelope_terminals": survivor_terms,
            "survivor_block_count_known_exactly": False,
            "survivor_block_count_upper_bounded_by_pre_hpadj08_blocks": pre_blocks,
            "per_survivor_block_rule": "For odd block size B=N+1, one parity character retains at most ceil(B/2)=(B+1)/2 terminals.",
            "block_count_refined_survivor_upper_bound": block_count_refined_upper_bound,
            "block_count_refined_rejection_lower_bound": block_count_refined_rejection_lower_bound,
            "td01_17_over_33_upper_bound": td01_bound,
            "improvement_vs_td01_upper_bound": improvement_vs_td01,
            "strict_improvement_over_td01": improvement_vs_td01 > 0,
        },
        "semantics": {
            "v30_main_is_exact_identity_set": False,
            "v30_main_upper_bound_used_as_population_identity": False,
            "hpadj10_additive_stacking_performed": False,
            "same_picard64_character_as_td01": True,
            "uses_only_x4_complete_block_structure": True,
            "uses_exact_hpadj08_survivor_terminal_total": True,
            "uses_pre_hpadj08_block_count_only_as_survivor_block_count_upper_bound": True,
            "main_consumption_performed": False,
            "hostile_audit_required_before_any_consumption": True,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "rows": result["rows"],
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
