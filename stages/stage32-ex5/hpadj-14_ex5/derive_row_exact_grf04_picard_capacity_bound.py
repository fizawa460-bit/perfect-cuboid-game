#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import math
import zlib
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

HPADJ10_COUNTER = ROOT / "stages/stage32-ex5/hpadj-10_ex5/count_hpadj_kernel_population.py"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
FAMILY = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
KERNEL = ROOT / "stages/stage32-ex5/hpadj-10_ex5/KERNEL-RESULT.json"
HPADJ11_CHECKPOINT = ROOT / "stages/stage32-ex5/hpadj-11_ex5/REMOVED-BLOCK-CHECKPOINT.json"
HPADJ11_REFINER = ROOT / "stages/stage32-ex5/hpadj-11_ex5/refine_with_hpadj08_removed_blocks.py"
ROW_CERT = ROOT / "stages/stage32-ex5/hpadj-12_ex5/HPADJ08-ROW-REJECT-CERTIFICATE.json"
V35_REL = Path("stages/stage32/management/grf04-uniform-bound/GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json")

LOCKS = {
    "hpadj10_counter_blob": "eebeb47f91df22461c33e9974d63aceca4da3b52",
    "manifest_blob": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "kernel_blob": "0a073dc9e01e037fa02fdbca5a482ee1ce6ab002",
    "kernel_canonical": "c678a84a8bb8aa44db0063ca797dec0e174ff021893ae5e9631ac607f43f1598",
    "hpadj11_checkpoint_blob": "81abb4aa2c626ec2a77b5b1e751e99f4299c55ba",
    "hpadj11_checkpoint_canonical": "0eff74f8adb64b3ecd8d2a3959d55686a64b57b52bcf6baabe62ac184cc1760d",
    "hpadj11_refiner_blob": "bda314b4ebbca59a209e2f4fd4d17dfc826cd17a",
    "row_cert_blob": "29ef2acf15e6649f5db90935f53b65a9388f7db4",
    "row_cert_canonical": "9dc6d1976b171dc1b71df1e767200a62cba9683ebc2d722819b92f8cd1e617c3",
    "row_cert_stream": "eb5716aad8931012fabc2183e3ef5957b0951606970eb89067a6bdbfb66f3f2f",
    "v35_blob": "a203df7b15a9cc655b78aa70b849933b98404a2d",
    "v35_canonical": "221f7bc44989130de39b639d4a0a0af85a056ea0ab9461e61a1cb24be907d5b5",
}

EXPECTED_PRE_TERMS = 47589703313957134107892
EXPECTED_PRE_BLOCKS = 33358843813855035700
EXPECTED_HPADJ08_REJECTED = 40886299509963924857401
EXPECTED_SURVIVOR_ENVELOPE = 6703403803993209250491
EXPECTED_HPADJ11_ROW_STREAM = "4fe260f31c999226042e4bfe39f3024eb92660f21e580dd5b4e1c34d9ae6a8ba"
V35_BENCHMARK = 511195899564352597589
V34_AUDITED_MAIN = 3360778813767800658369


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


def locked_json(path: Path, blob: str, canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")
    data = json.loads(path.read_text())
    req(data.get("canonical_sha256_without_this_field") == canon, f"{label} stored canonical drift")
    req(canonical(data) == canon, f"{label} canonical drift")
    return data


def load_counter():
    # Lock every repository byte needed by the retained combinatorial engine
    # before executing that engine.
    req(HPADJ10_COUNTER.is_file() and git_blob(HPADJ10_COUNTER) == LOCKS["hpadj10_counter_blob"],
        "HPADJ10 counter blob drift")
    req(MANIFEST.is_file() and git_blob(MANIFEST) == LOCKS["manifest_blob"], "manifest blob drift")
    req(FAMILY.is_file() and git_blob(FAMILY) == LOCKS["family_blob"], "compressed family blob drift")
    spec = importlib.util.spec_from_file_location("hpadj10_locked_for_hpadj14", HPADJ10_COUNTER)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ10 counter")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row_stream_sha256(rows: list[dict]) -> str:
    raw = "\n".join(
        json.dumps(
            {
                "d": int(r["d"]),
                "g": int(r["g"]),
                "stored_exact_square_candidate_rejected_terminals":
                    int(r["stored_exact_square_candidate_rejected_terminals"]),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        for r in rows
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def load_rejected_rows() -> dict[tuple[int, int], int]:
    cert = locked_json(ROW_CERT, LOCKS["row_cert_blob"], LOCKS["row_cert_canonical"], "HPADJ08 row reject certificate")
    rows_raw = zlib.decompress(base64.b64decode(cert["rows_zlib_base64"]))
    req(hashlib.sha256(rows_raw).hexdigest() == cert["aggregate"]["rows_json_sha256"], "row certificate payload sha")
    rows = json.loads(rows_raw)
    req(len(rows) == 178, "row certificate count")
    req(row_stream_sha256(rows) == LOCKS["row_cert_stream"], "row certificate stream")
    out = {}
    for r in rows:
        key = (int(r["g"]), int(r["d"]))
        req(key not in out, f"duplicate row certificate {key}")
        out[key] = int(r["stored_exact_square_candidate_rejected_terminals"])
    req(sum(out.values()) == EXPECTED_HPADJ08_REJECTED, "HPADJ08 rejected aggregate")
    return out


def even_values(lower: int, upper: int, excluded: set[int]) -> list[int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return []
    return [e for e in range(lo, hi + 1, 2) if e not in excluded]


def block_survivor_count(g: int, d: int) -> int:
    R = 3*d*d + 48*d + 96 - 96*g
    req(R >= 0 and R % 4 == 0, f"GRF04 R divisibility {(g,d)}")
    r = math.isqrt(R // 4)
    U = (d // 2 + r) // 2
    return U // 2 + 1


def exact_pre_gde_caps(mod) -> tuple[list[dict], str]:
    manifest = mod.load_locked_json(
        MANIFEST, LOCKS["manifest_blob"], LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = mod.manifest_rows(manifest)
    H = max(d // 2 for _, _, d in rows)
    BC = mod.build_bc_exact_parity(H)

    row_records = []
    row_hash_records = []
    total_terms = 0
    total_blocks = 0

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = mod.ceil_div(d - 16*g + 16, 4)
        A = [[mod.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        caps: dict[int, int] = defaultdict(int)

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
                        lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                        upper = min((19*d)//5, 3*d, 3*d - (b-c))
                        if lower > upper:
                            continue
                        excluded: set[int] = set()
                        e_n358 = 3*d - (b-c)
                        if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                            excluded.add(e_n358)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        for e in even_values(lower, upper, excluded):
                            B = 19*d - 5*e + 1
                            req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                            caps[e] += count

        row_blocks = sum(caps.values())
        row_terms = sum(n * (19*d - 5*e + 1) for e, n in caps.items())
        req(row_blocks > 0 and row_terms > 0, f"empty pre row {row_id}")
        total_blocks += row_blocks
        total_terms += row_terms
        row_records.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "pre_blocks": row_blocks,
            "pre_terms": row_terms,
            "caps": dict(sorted(caps.items())),
        })
        row_hash_records.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "pre_hpadj08_x4_complete_blocks": row_blocks,
            "pre_hpadj08_replay_domain_terminals": row_terms,
        })

    req(len(row_records) == 178, "pre row count")
    req(total_terms == EXPECTED_PRE_TERMS, "pre terminal aggregate")
    req(total_blocks == EXPECTED_PRE_BLOCKS, "pre block aggregate")

    stream = hashlib.sha256()
    for rec in sorted(row_hash_records, key=lambda r: (r["g"], r["d"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(stream.hexdigest() == EXPECTED_HPADJ11_ROW_STREAM, "HPADJ11 row-stream reproduction")

    return row_records, stream.hexdigest()


def greedy_max_blocks_for_mass(caps: dict[int, int], d: int, mass: int) -> tuple[int, int]:
    # Relax exact weighted equality to <= mass. To maximize block count, take
    # available blocks in increasing B order. This is the exact integer optimum
    # of that relaxation and therefore an upper bound for the actual equality.
    rem = mass
    blocks = 0
    used_mass = 0
    items = sorted(
        ((19*d - 5*e + 1, e, int(cap)) for e, cap in caps.items()),
        key=lambda x: (x[0], -x[1]),
    )
    for B, _e, cap in items:
        if rem < B:
            break
        take = min(cap, rem // B)
        blocks += take
        dm = take * B
        used_mass += dm
        rem -= dm
    return blocks, used_mass


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v35-root", required=True)
    ns = ap.parse_args()

    kernel = locked_json(KERNEL, LOCKS["kernel_blob"], LOCKS["kernel_canonical"], "HPADJ10 kernel")
    req(kernel["kernel"]["accepted_terminal_condition"] == "x4 ≡ x0 + x8 + x10 (mod 2)", "Picard parity drift")

    checkpoint = locked_json(
        HPADJ11_CHECKPOINT,
        LOCKS["hpadj11_checkpoint_blob"],
        LOCKS["hpadj11_checkpoint_canonical"],
        "hostile-audited HPADJ11 bridge checkpoint",
    )
    req(git_blob(HPADJ11_REFINER) == LOCKS["hpadj11_refiner_blob"], "HPADJ11 refiner blob drift")
    req(checkpoint["semantics"]["same_picard64_character_as_td01_and_hpadj10"] is True,
        "HPADJ11 same-character bridge drift")

    v35 = locked_json(
        Path(ns.v35_root) / V35_REL,
        LOCKS["v35_blob"], LOCKS["v35_canonical"], "latest MAIN V35 candidate"
    )
    req(v35["exact_input_envelope"]["x4_complete_after_hpadj08"] is True, "V35 x4-complete drift")
    req(v35["exact_input_envelope"]["hpadj08_survivor_x4_complete_envelope_terminals"] == EXPECTED_SURVIVOR_ENVELOPE,
        "V35 envelope drift")
    req(v35["exact_input_envelope"]["hostile_audited_completion_character"] == "x4 == x0+x8+x10 (mod 2)",
        "V35 completion character drift")
    req(v35["candidate_bound"]["candidate_upper_bound"] == V35_BENCHMARK, "V35 benchmark drift")
    req(v35["grf04_block_bound"]["fixed_parity_survivor_count"] == "c_g(d)=floor(U_g(d)/2)+1",
        "V35 GRF04 block-count formula drift")

    rejected = load_rejected_rows()
    mod = load_counter()
    pre_rows, pre_row_stream = exact_pre_gde_caps(mod)

    aggregate_survivor_mass = 0
    aggregate_block_upper_greedy = 0
    aggregate_block_upper_removed = 0
    aggregate_block_upper = 0
    aggregate_candidate = 0
    diagnostic_stream = hashlib.sha256()
    strict_greedy_vs_removed_rows = 0
    strict_removed_vs_greedy_rows = 0

    for rec in sorted(pre_rows, key=lambda r: (r["g"], r["d"])):
        g = int(rec["g"])
        d = int(rec["d"])
        key = (g, d)
        req(key in rejected, f"missing rejected row {key}")
        R = rejected[key]
        pre_terms = int(rec["pre_terms"])
        pre_blocks = int(rec["pre_blocks"])
        M = pre_terms - R
        req(M >= 0, f"negative survivor row mass {key}")
        aggregate_survivor_mass += M

        greedy_blocks, greedy_used_mass = greedy_max_blocks_for_mass(rec["caps"], d, M)
        req(greedy_used_mass <= M, f"greedy mass overflow {key}")

        bmax = max(19*d - 5*int(e) + 1 for e, cap in rec["caps"].items() if int(cap) > 0)
        removed_block_lb = (R + bmax - 1) // bmax
        removed_blocks_upper = pre_blocks - removed_block_lb
        req(removed_blocks_upper >= 0, f"negative removed-block survivor cap {key}")

        row_block_upper = min(greedy_blocks, removed_blocks_upper)
        if greedy_blocks < removed_blocks_upper:
            strict_greedy_vs_removed_rows += 1
        elif removed_blocks_upper < greedy_blocks:
            strict_removed_vs_greedy_rows += 1

        c = block_survivor_count(g, d)
        row_candidate = c * row_block_upper
        aggregate_candidate += row_candidate
        aggregate_block_upper_greedy += greedy_blocks
        aggregate_block_upper_removed += removed_blocks_upper
        aggregate_block_upper += row_block_upper

        compact = {
            "g": g,
            "d": d,
            "pre_terms": pre_terms,
            "pre_blocks": pre_blocks,
            "hpadj08_rejected_terms": R,
            "post_hpadj08_survivor_mass": M,
            "greedy_mass_block_upper": greedy_blocks,
            "removed_terminal_block_upper": removed_blocks_upper,
            "combined_block_upper": row_block_upper,
            "grf04_picard_survivors_per_block_upper": c,
            "row_candidate_upper": row_candidate,
        }
        diagnostic_stream.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(set(rejected) == {(int(r["g"]), int(r["d"])) for r in pre_rows}, "row key set mismatch")
    req(aggregate_survivor_mass == EXPECTED_SURVIVOR_ENVELOPE, "exact row survivor mass aggregate")
    req(aggregate_candidate < V35_BENCHMARK, "HPADJ14 does not improve current V35 benchmark")

    out = {
        "schema": "STAGE32EX5_HPADJ14_ROW_EXACT_GRF04_PICARD_CAPACITY_BOUND_V1",
        "status": "STRICTER_ROW_EXACT_GRF04_PICARD_CAPACITY_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id": "HPADJ-14_ex5",
        "source_locks": {
            "hpadj10_counter_blob_sha1": LOCKS["hpadj10_counter_blob"],
            "full178_manifest_blob_sha1": LOCKS["manifest_blob"],
            "full178_manifest_canonical_sha256": LOCKS["manifest_canonical"],
            "compressed_terminal_family_blob_sha1": LOCKS["family_blob"],
            "hpadj10_kernel_blob_sha1": LOCKS["kernel_blob"],
            "hpadj10_kernel_canonical_sha256": LOCKS["kernel_canonical"],
            "hpadj11_hostile_audit_review_id": 5216065509,
            "hpadj11_checkpoint_blob_sha1": LOCKS["hpadj11_checkpoint_blob"],
            "hpadj11_checkpoint_canonical_sha256": LOCKS["hpadj11_checkpoint_canonical"],
            "hpadj11_refiner_blob_sha1": LOCKS["hpadj11_refiner_blob"],
            "hpadj08_row_reject_certificate_blob_sha1": LOCKS["row_cert_blob"],
            "hpadj08_row_reject_certificate_canonical_sha256": LOCKS["row_cert_canonical"],
            "hpadj08_row_reject_stream_sha256": LOCKS["row_cert_stream"],
            "main_v35_exact_source_head": "a01dfd4173ae46c7d51e4f6f9ecdad8b4755f90c",
            "main_v35_candidate_blob_sha1": LOCKS["v35_blob"],
            "main_v35_candidate_canonical_sha256": LOCKS["v35_canonical"],
            "main_v35_candidate_hostile_audited": False,
        },
        "exact_population_adapter": {
            "full178_rows": 178,
            "pre_hpadj08_replay_domain_terminals": EXPECTED_PRE_TERMS,
            "pre_hpadj08_x4_complete_blocks": EXPECTED_PRE_BLOCKS,
            "pre_hpadj08_row_stream_sha256": pre_row_stream,
            "hpadj08_exact_square_rejected_terminals": EXPECTED_HPADJ08_REJECTED,
            "post_hpadj08_x4_complete_survivor_mass": aggregate_survivor_mass,
            "post_hpadj08_row_masses_known_exactly": True,
            "pre_hpadj08_gde_block_capacities_recomputed_exactly": True,
        },
        "optimization": {
            "problem":
                "For each exact (g,d) row, maximize surviving complete x4-block count subject to exact post-HPADJ08 row terminal mass and exact pre-HPADJ08 per-e block capacities.",
            "greedy_relaxation":
                "Relax weighted equality to <= row mass, sort blocks by increasing B=19d-5e+1, and fill exact per-e capacities greedily; the resulting integer optimum upper-bounds every actual survivor block set.",
            "independent_removed_terminal_cap":
                "Also use pre_blocks-ceil(rejected_terms/Bmax_row); take the smaller rowwise block-count upper bound.",
            "aggregate_greedy_mass_block_upper": aggregate_block_upper_greedy,
            "aggregate_removed_terminal_block_upper": aggregate_block_upper_removed,
            "aggregate_combined_block_upper": aggregate_block_upper,
            "rows_where_greedy_mass_is_stricter": strict_greedy_vs_removed_rows,
            "rows_where_removed_terminal_cap_is_stricter": strict_removed_vs_greedy_rows,
            "row_diagnostic_stream_sha256": diagnostic_stream.hexdigest(),
        },
        "candidate_bound": {
            "current_audited_main_upper_bound": V34_AUDITED_MAIN,
            "latest_main_v35_candidate_upper_bound": V35_BENCHMARK,
            "hpadj14_candidate_upper_bound": aggregate_candidate,
            "improvement_vs_current_audited_main": V34_AUDITED_MAIN - aggregate_candidate,
            "improvement_vs_main_v35_candidate": V35_BENCHMARK - aggregate_candidate,
            "strict_improvement_vs_main_v35_candidate": True,
            "composition_if_consumed": "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_SUBTRACTION",
        },
        "semantics": {
            "same_x4_direct_grf04_picard_intersection": True,
            "statistical_independence_assumed": False,
            "current_main_upper_bound_used_as_exact_identity_set": False,
            "exact_incremental_rejected_identity_set_claimed": False,
            "hpadj08_rejection_used_as_whole_x4_blocks": True,
            "row_survivor_terminal_masses_are_exact_on_audited_td01_replay_domain": True,
            "main_v35_is_used_as_source_locked_formula_and_benchmark_only": True,
            "main_v35_candidate_credit_inherited": False,
            "main_consumption_performed": False,
            "hostile_audit_required_before_main_handoff_or_consumption": True,
            "heavy_run_required": False,
            "new_heavy_run_used": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
