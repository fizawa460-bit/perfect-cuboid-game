#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib

EXPECTED_FAST_BLOB = "f9479ee73c9a5960cb8a3a8bc11a0c1c0fe8f4ba"
MODES = {"cap", "sym", "both"}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--mode", choices=sorted(MODES), required=True)
    args = ap.parse_args()

    text = args.source.read_text()
    mode = args.mode

    loop = "        for (long long zi=lo;zi<=hi;zi++) {\n"
    snapshots = ""
    if mode in {"cap", "both"}:
        snapshots += (
            "        std::array<long double,140> scout2_parent_assigned{};\n"
            "        for (int r=0;r<m_;r++) scout2_parent_assigned[r]=assigned_[r];\n"
        )
    if mode in {"sym", "both"}:
        snapshots += (
            "        std::array<long double,64> scout2_parent_sassigned{};\n"
            "        for (int r=0;r<s_.k;r++) scout2_parent_sassigned[r]=sassigned_[r];\n"
        )
    snapshots += loop
    text = replace_once(text, loop, snapshots, "DFS loop insertion")

    old_update = (
        "            z_[i]=zi;\n"
        "            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;\n"
        "            for (int r=0;r<s_.k;r++) sassigned_[r]+=sa_[r][i]*ti;\n"
    )
    cap_update = (
        "            for (int r=0;r<m_;r++) assigned_[r]=scout2_parent_assigned[r]+a_[r][i]*ti;\n"
        if mode in {"cap", "both"}
        else "            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;\n"
    )
    sym_update = (
        "            for (int r=0;r<s_.k;r++) sassigned_[r]=scout2_parent_sassigned[r]+sa_[r][i]*ti;\n"
        if mode in {"sym", "both"}
        else "            for (int r=0;r<s_.k;r++) sassigned_[r]+=sa_[r][i]*ti;\n"
    )
    text = replace_once(
        text,
        old_update,
        "            z_[i]=zi;\n" + cap_update + sym_update,
        "child-state update",
    )

    old_restore = (
        "            for (int r=0;r<s_.k;r++) sassigned_[r]-=sa_[r][i]*ti;\n"
        "            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;\n"
    )
    new_restore = ""
    if mode not in {"sym", "both"}:
        new_restore += "            for (int r=0;r<s_.k;r++) sassigned_[r]-=sa_[r][i]*ti;\n"
    if mode not in {"cap", "both"}:
        new_restore += "            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;\n"
    text = replace_once(text, old_restore, new_restore, "child-state restore")

    marker = "struct TierResult {\n"
    text = replace_once(
        text,
        marker,
        f"// STAGE32_SCOUT2_SNAPSHOT_RESTORE_MODE={mode}\n" + marker,
        "mode marker",
    )

    args.output.write_text(text)
    print({
        "mode": mode,
        "expected_source_blob": EXPECTED_FAST_BLOB,
        "cap_snapshot_restore": mode in {"cap", "both"},
        "symmetry_snapshot_restore": mode in {"sym", "both"},
        "scout_only": True,
    })


if __name__ == "__main__":
    main()
