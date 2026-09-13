#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FROZEN_N385_VERIFIER_HEAD = "865b5732143c8328f507f880def24907afdfef0a"
FROZEN_N385_VERIFIER_BLOB = "885324d78b4dd84978c60346db1f0a32307ba42c"
FROZEN_N385_VERIFIER_REL = "stages/stage32/32-01-178/nodes/N385/verify_n385_certlift03_v23_hostile_audited_main_sync.py"
N386_VERIFIER = HERE.parent / "N386" / "verify_n386_hpadj01_n372_nontransfer.py"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def arg_value(flag: str) -> str:
    req(flag in sys.argv, f"missing required argument {flag}")
    i = sys.argv.index(flag)
    req(i + 1 < len(sys.argv), f"missing value for {flag}")
    return sys.argv[i + 1]


def main() -> None:
    frozen = subprocess.check_output(
        ["git", "show", f"{FROZEN_N385_VERIFIER_HEAD}:{FROZEN_N385_VERIFIER_REL}"]
    )
    req(
        git_blob_bytes(frozen) == FROZEN_N385_VERIFIER_BLOB,
        "frozen N385 verifier blob drift",
    )

    frozen_file = str(HERE / ".verify_n385_frozen_865b.py")
    scope = {
        "__name__": "__main__",
        "__file__": frozen_file,
        "__package__": None,
    }
    exec(compile(frozen, frozen_file, "exec"), scope)

    req(N386_VERIFIER.is_file(), "missing N386 verifier")
    main_v23_root = arg_value("--main-v23-root")
    subprocess.run(
        [
            sys.executable,
            str(N386_VERIFIER),
            "--main-v23-root",
            main_v23_root,
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
