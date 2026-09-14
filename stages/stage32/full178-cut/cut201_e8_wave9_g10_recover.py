#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
from pathlib import Path


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def alias_parent_shards(root: Path) -> None:
    files = sorted(root.glob("cut201-g9-parent-shard-*.json"))
    by_id = {}
    for path in files:
        m = re.fullmatch(r"cut201-g9-parent-shard-(\d+)\.json", path.name)
        if not m:
            raise SystemExit(f"unexpected G9 shard filename: {path.name}")
        sid = int(m.group(1))
        if sid in by_id:
            raise SystemExit(f"duplicate G9 shard id: {sid}")
        by_id[sid] = path
    if sorted(by_id) != list(range(32)) or len(files) != 32:
        raise SystemExit(f"G9 shard-id coverage drift: {sorted(by_id)}")
    extras = sorted(p.name for p in root.glob("*.json") if p not in set(files))
    if extras:
        raise SystemExit(f"unexpected JSON files before aliasing: {extras}")
    for sid, path in sorted(by_id.items()):
        alias = root / f"cut201-g8-parent-shard-{sid}.json"
        if alias.exists():
            raise SystemExit(f"alias destination already exists: {alias.name}")
        shutil.copyfile(path, alias)
        if path.read_bytes() != alias.read_bytes():
            raise SystemExit(f"alias byte drift: shard {sid}")
    print(json.dumps({"retained_g9_shards": 32, "alias_ids": list(range(32))}, sort_keys=True))


def combine_shard5(root: Path, output: Path) -> None:
    files = sorted(list(root.glob("cut201-shard-5-singleton-*.json")) + list(root.glob("cut201-shard-5-part-*.json")))
    expected = [(2201,2201),(2202,2202),(2203,2203),(2204,2204),(2205,2208),(2209,2212),(2213,2216),(2217,2220),(2221,2224),(2225,2228),(2229,2232)]
    if len(files) != 11:
        raise SystemExit(f"expected 11 recovery pieces, got {len(files)}")
    shards = [json.loads(path.read_text()) for path in files]
    got = sorted(tuple(s["target"]["survivor_offset_range"]) for s in shards)
    if got != expected:
        raise SystemExit(f"recovery ranges drift: {got}")
    for shard in shards:
        q = dict(shard)
        claimed = q.pop("canonical_sha256_without_this_field", None)
        if shard.get("schema") != "STAGE32_CUT201_E8_COMMON_ADAPTER_WAVE9_SHARD_V1" or claimed != csha(q):
            raise SystemExit("piece canonical/schema drift")
        if shard["credit"]["stage32_main_pruning_credit"] is not False or shard["credit"]["cut201_pruning_credit"] is not False:
            raise SystemExit("piece credit leak")
        if shard["firewalls"]["main_authority_mutated"] is not False:
            raise SystemExit("piece MAIN mutation leak")
    ordered = sorted(shards, key=lambda s: s["target"]["survivor_offset_range"][0])
    first = ordered[0]
    for shard in ordered[1:]:
        if shard["source"] != first["source"] or shard["method"] != first["method"] or shard["credit"] != first["credit"] or shard["firewalls"] != first["firewalls"]:
            raise SystemExit("piece invariant drift")
        for key in ("row_id","g","d","e","cut191_block0_disjoint","cut193_wave1_disjoint","cut194_wave2_disjoint","cut195_wave3_disjoint","cut196_wave4_disjoint","cut197_wave5_disjoint","cut198_wave6_disjoint","cut199_wave7_disjoint","cut200_wave8_disjoint","n356_preserved_all_wave_blocks"):
            if shard["target"][key] != first["target"][key]:
                raise SystemExit(f"piece target invariant drift: {key}")
    covered=[]; block_indices=[]; closed=[]; records=[]; methods={}
    for shard in ordered:
        a,b = shard["target"]["survivor_offset_range"]
        covered += list(range(a,b+1))
        block_indices += list(shard["target"]["block_indices"])
        closed += list(shard["result"]["candidate_closed_block_indices"])
        records += list(shard["result"]["blocks"])
        for key,value in shard["result"]["method_counts"].items():
            methods[key] = methods.get(key,0) + int(value)
    if covered != list(range(2201,2233)):
        raise SystemExit("combined shard5 survivor-offset coverage drift")
    if len(block_indices) != 32 or len(set(block_indices)) != 32 or len(records) != 32:
        raise SystemExit("combined shard5 block coverage drift")
    if sorted(r["block_index"] for r in records) != sorted(block_indices):
        raise SystemExit("combined shard5 record coverage drift")
    closed = sorted(int(v) for v in closed)
    if len(closed) != len(set(closed)):
        raise SystemExit("combined shard5 duplicate closure")
    bh=hashlib.sha256(); ch=hashlib.sha256()
    for value in block_indices: bh.update(f"{value}\n".encode())
    for value in closed: ch.update(f"{value}\n".encode())
    out=copy.deepcopy(first)
    out.pop("canonical_sha256_without_this_field",None)
    out["target"]["survivor_offset_range"]=[2201,2232]
    out["target"]["block_indices"]=block_indices
    out["target"]["block_index_stream_sha256"]=bh.hexdigest()
    out["target"]["block_count"]=32
    out["target"]["terminal_count"]=3616
    out["result"]["candidate_closed_block_indices"]=closed
    out["result"]["candidate_closed_block_count"]=len(closed)
    out["result"]["candidate_closed_block_stream_sha256"]=ch.hexdigest()
    out["result"]["candidate_pruned_terminals"]=113*len(closed)
    out["result"]["method_counts"]=methods
    out["result"]["blocks"]=records
    out["canonical_sha256_without_this_field"]=csha(out)
    output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"combined_range":[2201,2232],"blocks":32,"closed":len(closed),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))


def main() -> None:
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("alias-parent-shards"); p.add_argument("--root",type=Path,required=True)
    p=sub.add_parser("combine-shard5"); p.add_argument("--root",type=Path,required=True); p.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.cmd=="alias-parent-shards": alias_parent_shards(args.root)
    else: combine_shard5(args.root,args.output)

if __name__ == "__main__":
    main()
