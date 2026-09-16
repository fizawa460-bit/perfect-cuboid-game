#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PACKET = HERE / "EXACT-X4-ENVELOPE-BOUND.json"
N358 = ROOT / "stages/stage32/management/N358-AUDITED-RESULT.json"
EQUIV = HERE / "HPADJ09-EQUIVALENCE-NOTE.json"
EQUIV_VERIFIER = HERE / "verify_hpadj09_grf02_character_equivalence.py"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"

PACKET_BLOB = "51271c11078459ad9171138c4fb6121d7a665c39"
PACKET_CANON = "f55bf17b7206fb81caccba46c4df7de441f5ef75fab9f422cc33148432a3242d"
N358_BLOB = "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"
N358_CANON = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
EQUIV_BLOB = "9825be2067c1dbd2ea4583e715cfedd991456c82"
EQUIV_CANON = "0cabdf02524c1d5e976df863454c790fb7b89c7d585a9e9ba9f36757d13eafd7"
EQUIV_VERIFIER_BLOB = "0d9c2c506edb33d656f449593597c8befadd2e0d"
MAIN_BLOB = "76bf5e3d9d97297ff5fbee2bf4826a78d125e171"
MAIN_CANON = "bfa2441840bcf60ca70ef6cb288f8721310cdcc78e9f0724a197d35e60e79b21"

HISTORICAL = [
    ("0d787839b7e0dad4a42108c61d16e7849c50862f", "stages/stage32/32-01-178/nodes/N357/RESULT.json", "50014d453266ad79101910a943d14388bd3ef6ec", "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"),
    ("0d787839b7e0dad4a42108c61d16e7849c50862f", "stages/stage32/32-01-178/nodes/N357/verify_n357_all178_support_capacity_census.py", "beb6fb487a41f16d783f8762220a175d46ff2620", None),
    ("462174f74d6470ec7c64f5b6d078757c7b3372fc", "stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py", "c07a7e358a6253919194189377d6ed56f95e047a", None),
    ("289437a4a97a814c2388133cbde0c794d9502e4b", "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json", "291bb8b125566bb72c1caae0537dff2625219ffb", "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858"),
    ("421543ef7864b4f99d57284958db2fb8839c9a3b", "stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json", "442f84b392254383736f1b695da7a9b2954c053d", "ceec3c102ad194c05e1429e7af293716a21993fb2dcfd531525c30c371bc2821"),
    ("36eab50192cf80ec5ed48aba40f4a56076759fea", "stages/stage32-ex5/hpadj-08_ex5/FULL178-RESULT.json", "f9a01c3e673dc630a3446ac4560c72c4f76db812", "625e289a1a9f086b5e02f247665a7f9ac4b7fe72eaacd3011fe73a0e96041953"),
    ("36eab50192cf80ec5ed48aba40f4a56076759fea", "stages/stage32-ex5/hpadj-08_ex5/hpadj08_ex5_full178_b_shard.py", "c5fc340ea734dfc54436f124bb302c1ec6c5677c", None),
]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def git_blob(path: Path) -> str:
    return git_blob_bytes(path.read_bytes())


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def locked_json(path: Path, blob: str, canonical: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == blob, f"{label} blob drift")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical drift")
    req(canon(obj) == canonical, f"{label} canonical drift")
    return obj


def historical_bytes(ref: str, path: str) -> bytes:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{ref}:{path}"])
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"FAIL: historical object unavailable {ref}:{path}; fetch the exact audited commit before --historical-replay") from exc


def verify_historical() -> None:
    payloads: dict[str, dict] = {}
    for ref, path, blob, canonical in HISTORICAL:
        raw = historical_bytes(ref, path)
        req(git_blob_bytes(raw) == blob, f"historical blob drift {ref}:{path}")
        if canonical is not None:
            obj = json.loads(raw)
            req(obj.get("canonical_sha256_without_this_field") == canonical, f"historical stored canonical drift {path}")
            req(canon(obj) == canonical, f"historical canonical drift {path}")
            payloads[path] = obj

    n357 = payloads["stages/stage32/32-01-178/nodes/N357/RESULT.json"]
    req(n357["aggregate"]["candidate_remaining_terminals"] == 47598978285064933810198, "N357 remaining drift")
    req(n357["necessary_condition"] == "s + min(e-M,Srem) >= K", "N357 semantic condition drift")
    req(n357["verification"]["n356_authority_replayed_exactly"] is True, "N357 exact authority replay drift")
    req(n357["verification"]["partition_identity"] is True, "N357 partition identity drift")

    cert = payloads["stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json"]
    req(cert["population"]["current_prefix_blocks"] == 7596, "CERTLIFT03 e8 block population drift")
    req(cert["population"]["block_width_terminals"] == 113, "CERTLIFT03 e8 block width drift")
    req(cert["prior_authority_overlap"]["n358_blocks"] == 0, "CERTLIFT03/N358 e8 overlap drift")

    cert_pass = payloads["stages/stage32/cert-lift/CERTLIFT-03-V22-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json"]
    req(cert_pass["status"] == "HOSTILE_AUDIT_PASS" and cert_pass["review_id"] == 5188860951, "CERTLIFT03 hostile audit drift")

    hpadj = payloads["stages/stage32-ex5/hpadj-08_ex5/FULL178-RESULT.json"]
    req(hpadj["coverage"]["rows"] == 178 and hpadj["coverage"]["all_shards_success"] is True, "HPADJ08 FULL178 coverage drift")
    req(hpadj["stored_exact_square_candidate_rejected_terminals"] == 40886299509963924857401, "HPADJ08 exact-square count drift")


def replay_completion_character(*, historical: bool) -> None:
    req(EQUIV_VERIFIER.is_file(), "missing GRF02/HPADJ09 equivalence verifier")
    req(git_blob(EQUIV_VERIFIER) == EQUIV_VERIFIER_BLOB, "GRF02/HPADJ09 equivalence verifier blob drift")
    cmd = [sys.executable, str(EQUIV_VERIFIER)]
    if historical:
        cmd.append("--historical-replay")
    subprocess.check_call(cmd, cwd=ROOT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--historical-replay", action="store_true", help="also fail-closed replay exact historical Git objects; fetch the listed commits first")
    ns = ap.parse_args()

    packet = locked_json(PACKET, PACKET_BLOB, PACKET_CANON, "TD01 exact-envelope packet")
    n358 = locked_json(N358, N358_BLOB, N358_CANON, "retained N358 result")
    equiv = locked_json(EQUIV, EQUIV_BLOB, EQUIV_CANON, "GRF02/HPADJ09 equivalence note")
    main_state = locked_json(MAIN, MAIN_BLOB, MAIN_CANON, "MAIN V30 state")

    req(packet["status"] == "RETAINED_NONHEAVY_EXACT_X4_ENVELOPE_UPPER_BOUND_CANDIDATE_AUDIT_REQUIRED", "packet status drift")
    req(n358["aggregate"]["candidate_remaining_terminals"] == 47589703313957134966240, "N358 residual drift")
    req(n358["aggregate"]["source_terminals"] == 47598978285064933810198, "N358 source/N357 residual drift")
    req(n358["aggregate"]["incremental_rejected_terminals"] == 9274971107798843958, "N358 rejected count drift")
    req(n358["verification"]["partition_identity"] is True, "N358 partition identity drift")

    req(equiv["status"] == "EXACT_SAME_CHARACTER_PROVED_SOURCE_LOCKED_NO_MAIN_CREDIT", "completion-character status drift")
    req(equiv["character_identity"]["hash_match"] is True, "completion-character hash identity drift")
    req(equiv["character_identity"]["hpadj09_reconstructed_mod8_row"] == [4,0,0,0,4,0,0,0,4,0,4], "HPADJ09 character drift")
    req(packet["source_locks"]["completion_character"]["grf02_mod2_row"] == [1,0,0,0,1,0,0,0,1,0,1], "GRF02 character drift")

    # Load-bearing character replay is part of this verifier, not a documentary
    # side note.  Historical mode additionally source-locks PANEL-RESULT itself.
    replay_completion_character(historical=ns.historical_replay)

    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == 6703403803993210101494, "MAIN V30 numeric authority drift")
    req(frontier["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "MAIN V30 semantics drift")

    n357 = 47598978285064933810198
    n358_reject = 9274971107798843958
    n358_remaining = n357 - n358_reject
    req(n358_remaining == 47589703313957134966240, "N357-N358 arithmetic drift")

    e8 = 7596 * 113
    req(e8 == 858348, "g1-d008/e8 exact population arithmetic drift")
    envelope = n358_remaining - e8
    req(envelope == 47589703313957134107892, "HPADJ08 exact replay-domain envelope drift")

    hpadj_reject = 40886299509963924857401
    survivors = envelope - hpadj_reject
    req(survivors == 6703403803993209250491, "HPADJ08 exact survivor-envelope drift")

    # For an even N>=32, the worse of the two required-parity classes retains
    # N/2+1 of N+1 values.  33*(N+2) <= 34*(N+1) iff N>=32, hence
    # (N/2+1)/(N+1) <= 17/33.  This avoids any distribution assumption.
    req(33 * (32 + 2) == 34 * (32 + 1), "17/33 endpoint identity drift")
    for N in range(32, 4001, 2):
        req(33 * (N + 2) <= 34 * (N + 1), f"17/33 parity ratio regression N={N}")

    combined = (17 * survivors) // 33
    rejected_lower = survivors - combined
    req(combined == 3453268626299532038131, "combined upper bound drift")
    req(rejected_lower == 3250135177693677212360, "additional rejection lower bound drift")
    req(frontier["authoritative_remaining_terminals"] - combined == 3250135177693678063363, "MAIN min-composition tightening arithmetic drift")

    req(packet["main_composition_candidate"]["main_authority_mutated"] is False, "packet mutated MAIN")
    req(packet["main_composition_candidate"]["main_credit"] is False, "packet self-granted MAIN credit")
    req(packet["main_composition_candidate"]["audit_required"] is True, "packet bypassed audit")
    req(packet["heavy_avoidance"]["heavy_run_executed"] is False, "packet claims heavy execution")
    req(packet["firewalls"]["merge_authorized"] is False, "packet authorizes merge")

    if ns.historical_replay:
        verify_historical()

    print(json.dumps({
        "status": "PASS_TD01_EXACT_X4_ENVELOPE_BOUND_PACKET",
        "historical_replay": ns.historical_replay,
        "completion_character_replayed": True,
        "hpadj09_panel_source_locked": ns.historical_replay,
        "exact_hpadj08_survivor_envelope": survivors,
        "candidate_td01_upper_bound": combined,
        "candidate_tightening_vs_current_main": frontier["authoritative_remaining_terminals"] - combined,
        "heavy_required": False,
        "audit_required": True,
        "main_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
