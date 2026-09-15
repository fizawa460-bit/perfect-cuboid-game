#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = HERE / "HPADJ09-EQUIVALENCE-NOTE.json"
GRF02 = ROOT / "stages/stage32/management/global-residual-feasibility/GRF-02-PROJECTED-KERNEL.json"

NOTE_BLOB = "9825be2067c1dbd2ea4583e715cfedd991456c82"
NOTE_CANON = "0cabdf02524c1d5e976df863454c790fb7b89c7d585a9e9ba9f36757d13eafd7"
GRF02_BLOB = "7c1cda07749fbfb90245995d1def2ae96fb5604b"
GRF02_CANON = "2e08a25e2de891bfabd0bf96ba06d928d733711b2c27449c9818b856665d4d6f"
HPADJ09_UNIQUE_ROWS_SHA256 = "fa255af25e535fa5e60670d2ad6eb5e40a5e4f28476d8ec2afcab4fbb6b787e3"
HPADJ09_PANEL_CANON = "7635e28de31e53161ee36b6b0d020a5127de2ddff73ca13ca591740758426115"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(git_blob(NOTE) == NOTE_BLOB, "equivalence note blob drift")
    note = json.loads(NOTE.read_text())
    req(note.get("canonical_sha256_without_this_field") == NOTE_CANON, "note stored canonical drift")
    req(canon(note) == NOTE_CANON, "note canonical drift")

    req(git_blob(GRF02) == GRF02_BLOB, "GRF02 blob drift")
    grf = json.loads(GRF02.read_text())
    req(grf.get("canonical_sha256_without_this_field") == GRF02_CANON, "GRF02 stored canonical drift")
    req(canon(grf) == GRF02_CANON, "GRF02 canonical drift")

    rows = grf["exact_completion_kernel"]["primitive_equation_rows"]
    req(len(rows) == 1 and int(rows[0]["modulus"]) == 2, "GRF02 primitive row contract drift")
    v = [int(x) for x in rows[0]["coefficients"]]
    req(v == note["character_identity"]["grf02_mod2_row"], "GRF02 row/note mismatch")

    w = [4 * x for x in v]
    req(w == note["character_identity"]["hpadj09_reconstructed_mod8_row"], "reconstructed mod8 row mismatch")
    rows_sha = hashlib.sha256(
        json.dumps([w], sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    req(rows_sha == HPADJ09_UNIQUE_ROWS_SHA256, "HPADJ09 unique-row hash mismatch")
    req(rows_sha == note["character_identity"]["hpadj09_retained_unique_congruence_rows_sha256"], "retained unique-row hash note mismatch")

    # For every integer S, 4*S == 0 mod 8 iff S == 0 mod 2.
    # Exhausting S mod 8 is a complete proof of the scalar congruence identity.
    for s in range(8):
        req((4 * s) % 8 == 0 if s % 2 == 0 else (4 * s) % 8 != 0,
            f"scalar congruence equivalence failed at residue {s}")

    total = 8 ** 11
    accepted = total // 2
    req(total == note["character_identity"]["total_mod8_classes"], "mod8 domain cardinality drift")
    req(accepted == note["character_identity"]["accepted_mod8_classes"], "accepted cardinality drift")
    req(note["sources"]["hpadj09"]["panel_result_canonical_sha256"] == HPADJ09_PANEL_CANON,
        "HPADJ09 panel source lock drift")
    req(note["ex5_bounded_confirmation"]["kernel_accepted_terminals"] == 17120, "EX5 bounded accepted drift")
    req(note["ex5_bounded_confirmation"]["kernel_rejected_terminals"] == 17120, "EX5 bounded rejected drift")

    req(grf["fixed_selected64"]["fixed_coefficient_matrix_sha256"] == note["fixed_problem"]["fixed_matrix_sha256"],
        "fixed matrix identity drift")
    req(grf["fixed_selected64"]["free_coefficient_matrix_sha256"] == note["fixed_problem"]["free_matrix_sha256"],
        "free matrix identity drift")
    req(grf["fixed_selected64"]["inverse_integer_matrix_sha256"] == note["fixed_problem"]["inverse_integer_matrix_sha256"],
        "inverse matrix identity drift")

    print(json.dumps({
        "status": "PASS_EXACT_HPADJ09_GRF02_CHARACTER_EQUIVALENCE",
        "grf02_mod2_row": v,
        "reconstructed_hpadj09_mod8_row": w,
        "unique_rows_sha256": rows_sha,
        "accepted_mod8_classes": accepted,
        "total_mod8_classes": total,
        "double_stack_forbidden": True,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
