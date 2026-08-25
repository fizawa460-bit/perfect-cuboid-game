#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib

EXPECTED_FAST_BLOB = "f9479ee73c9a5960cb8a3a8bc11a0c1c0fe8f4ba"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()
    text = args.source.read_text()

    loop = "        for (long long zi=lo;zi<=hi;zi++) {\n"
    snapshots = (
        "        std::array<long double,140> parent_assigned{};\n"
        "        for (int r=0;r<m_;r++) parent_assigned[r]=assigned_[r];\n"
        "        std::array<long double,64> parent_sassigned{};\n"
        "        for (int r=0;r<s_.k;r++) parent_sassigned[r]=sassigned_[r];\n"
        + loop
    )
    text = replace_once(text, loop, snapshots, "DFS loop insertion")

    old_update = (
        "            z_[i]=zi;\n"
        "            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;\n"
        "            for (int r=0;r<s_.k;r++) sassigned_[r]+=sa_[r][i]*ti;\n"
    )
    new_update = (
        "            z_[i]=zi;\n"
        "            for (int r=0;r<m_;r++) assigned_[r]=parent_assigned[r]+a_[r][i]*ti;\n"
        "            for (int r=0;r<s_.k;r++) sassigned_[r]=parent_sassigned[r]+sa_[r][i]*ti;\n"
    )
    text = replace_once(text, old_update, new_update, "child-state update")

    old_restore = (
        "            for (int r=0;r<s_.k;r++) sassigned_[r]-=sa_[r][i]*ti;\n"
        "            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;\n"
    )
    text = replace_once(text, old_restore, "", "child-state restore")

    marker = "struct TierResult {\n"
    text = replace_once(text, marker, "// STAGE32_18D_SNAPSHOT_PARENT_RESTORE=both\n" + marker, "marker")
    args.output.write_text(text)
    print({"expected_source_blob": EXPECTED_FAST_BLOB, "snapshot_parent_restore": "both", "numerical_credit": False})


if __name__ == "__main__":
    main()
