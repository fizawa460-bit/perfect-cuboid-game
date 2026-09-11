#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_family import exceptional_terminal_count
from compressed_terminal_indexer import CompressedTerminalIndexer

PREFLIGHT = HERE / "e8-terminal-population-preflight.json"
ADAPTER = HERE / "e8_terminal_population_adapter.py"
N220 = ROOT / "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json"
N355_RESULT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-RESULT.json"
N355_AUDIT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-HOSTILE-AUDIT-PASS.json"
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
GROUPS = [[101,102,103],[97,98,99],[93,94,95,96]]
LOCKS = {
    ADAPTER: "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    PREFLIGHT: "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    N220: "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    N355_RESULT: "0f30517cc5007ea435f4183201fc6cad699dd635",
    N355_AUDIT: "033294f56fb86d81b7aa43758a51a39747ccc082",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_18_n354_survivor_exceptional_mod8_decomposition.py": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
    ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-17-n354-authority-picard64-retarget-v2-evidence.json": "28c4b762c7f96a4898c62751062648cad066578c",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
}


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def checked(path: Path, canonical: str) -> dict:
    obj = json.loads(path.read_text())
    q = dict(obj); claimed = q.pop("canonical_sha256_without_this_field", None)
    req(claimed == canonical and csha(q) == canonical, f"canonical drift: {path.relative_to(ROOT)}")
    return obj


def signature(idx: CompressedTerminalIndexer, block_index: int) -> dict:
    lo = block_index * 113; hi = lo + 112
    base = tuple(int(v) for v in idx.unrank(lo)); top = tuple(int(v) for v in idx.unrank(hi))
    req(base[4] == 0 and top[4] == 112, "x4 block endpoint regression")
    req(base[:4] + base[5:] == top[:4] + top[5:], "exceptional signature block regression")
    req(idx.rank(base) == lo and idx.rank(top) == hi, "rank/unrank block endpoint regression")
    fixed = {label: int(v) for label, v in zip(ASSIGNMENT_ORDER, base) if label != 49}
    mass = sum(fixed.values()); support = sum(v > 0 for v in fixed.values())
    n220 = support + min(38, 8 - mass) >= 2
    sums = [sum(fixed[label] for label in group) for group in GROUPS]
    n355 = max(sums) <= 4
    return {"base": list(base), "mass": mass, "support": support, "sums": sums, "pass": bool(n220 and n355), "raw": math.comb((8-mass)+19,19)}


def main() -> None:
    for path, expected in LOCKS.items():
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")
    p = json.loads(PREFLIGHT.read_text())
    req(p["schema"] == "STAGE32EX5_E8_CURRENT_MAIN_TERMINAL_POPULATION_PREFLIGHT_V2", "preflight schema drift")
    n220 = json.loads(N220.read_text())
    req(n220["status"] == "DONE_AUDITED_EXACT_NECESSARY_PREFIX_PRUNING" and n220["hostile_audit"]["result"] == "PASS", "N220 audit authority drift")
    req(n220["audited_predicate"]["necessary_form"] == "S10 + min(38, e-M10) >= ceil((d-16g+16)/4)", "N220 predicate drift")
    n355 = checked(N355_RESULT, "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775")
    req(n355["full_prefix_cut"]["known_groups"] == GROUPS, "N355 group partition drift")
    req(n355["full_prefix_cut"]["equivalent_cut"] == "max(group1_sum,group2_sum,group3_sum)<=floor(d/2)", "N355 cut drift")
    audit = checked(N355_AUDIT, "d6bda89f94eb57bf021f0acbbc5000e198f1805c09da3e5f9a531d20b70ce004")
    req(audit["status"] == "PASS" and audit["audited_exact_head"] == "3f3aadd2e5ada2a0a02a69490d6d659c02762682" and audit["review_id"] == 5165895301, "N355 audit receipt drift")

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget == 112 and idx.exceptional_count == 11318 and idx.terminal_count == 1278934, "e8 unfiltered population drift")
    survivor = []; raw_survivor = 0; h = hashlib.sha256(); n220_fail_inside_n355 = 0
    for block_index in range(11318):
        s = signature(idx, block_index)
        n355_pass = max(s["sums"]) <= 4
        if n355_pass and not s["pass"]:
            n220_fail_inside_n355 += 1
        if s["pass"]:
            survivor.append(block_index); raw_survivor += s["raw"]; h.update(f"{block_index}\n".encode())
    req(len(survivor) == 7596 and 113*len(survivor) == 858348, "current-MAIN e8 handoff population drift")
    req(n220_fail_inside_n355 == 0, "N220 unexpectedly removes N355 survivor blocks")
    req(h.hexdigest() == "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3", "survivor block stream drift")
    req(raw_survivor == 12357387, "current-MAIN raw parent population drift")
    req(11318-len(survivor) == 3722 and 113*(11318-len(survivor)) == 420586, "N355 rejected population drift")
    b0 = signature(idx,0); b1 = signature(idx,1)
    req(b0["pass"] and b0["mass"] == 2 and b0["raw"] == 177100, "first block regression")
    req(b1["pass"] and b1["base"] == [0,1,0,0,0,0,0,1,0,0,1] and b1["sums"] == [1,1,1] and b1["raw"] == 42504, "first disjoint current-MAIN block regression")
    wave = survivor[1:256]
    wh = hashlib.sha256(); wave_raw = 0
    for block_index in wave:
        wh.update(f"{block_index}\n".encode()); wave_raw += signature(idx, block_index)["raw"]
    req(len(wave)==255 and wave[0]==1 and wave[-1]==343 and wave_raw==407672, "preferred wave population drift")
    req(wh.hexdigest()=="68ca7b27ffeceb52c35942449ca47105fd4a74757575544033454c3c9be514ea", "preferred wave block stream drift")
    req(p["current_main_handoff_population"]["block_count"] == 7596 and p["current_main_handoff_population"]["terminal_count"] == 858348, "preflight handoff population drift")
    req(p["credit"]["stage32_main_pruning_credit"] is False and p["credit"]["merge_authorized"] is False, "credit leak")
    compile(ADAPTER.read_text(), str(ADAPTER), "exec")
    print("PASS: Stage32EX5 common e8 adapter is scoped to audited current-MAIN prefix survivors")
    print("adapter_universe=11318_blocks/1278934_terminals")
    print("cut_handoff=7596_blocks/858348_terminals;rejected_by_audited_prefix=3722_blocks/420586_terminals")
    print("N220_additional_inside_N355=0;N356_candidate_consumed=NO")
    print("preferred_wave=255_survivor_blocks/28815_terminals/source_blocks_1..343/raw_candidates_407672")
    print("stage32_main_pruning_credit=NO;merge_authorized=NO")


if __name__ == "__main__":
    main()
