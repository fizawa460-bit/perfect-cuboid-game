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

from compressed_terminal_indexer import CompressedTerminalIndexer

REPORT = HERE / "NON-E8-CUT-INTERFACE-SCOUT-E10.json"
MANIFEST = RESIDUAL / "full178-manifest.json"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
N220 = ROOT / "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json"
N353 = ROOT / "stages/stage32/32-01-178/nodes/N353/RESULT.json"
N354 = ROOT / "stages/stage32/32-01-178/nodes/N354/RESULT.json"
N355_RESULT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-RESULT.json"
N355_AUDIT = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-HOSTILE-AUDIT-PASS.json"
N356 = ROOT / "stages/stage32/32-01-178/nodes/N356/RESULT.json"
E8_PREFLIGHT = ROOT / "stages/stage32-ex5/cut-handoff/e8-terminal-population-preflight.json"
E8_ADAPTER = ROOT / "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py"

LOCKS = {
    FAMILY: "90ff82ed312dcc0cb32cf207935945f550e29170",
    INDEXER: "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    MANIFEST: "0a46b34e278688240656b4977e9cb7f589e90e06",
    N220: "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    N353: "6306f741b28f693e72ab8ce12c0c4e97e2f2cb0d",
    N354: "6f6ed5646689940cc304a655711dba83333d3576",
    N355_RESULT: "0f30517cc5007ea435f4183201fc6cad699dd635",
    N355_AUDIT: "033294f56fb86d81b7aa43758a51a39747ccc082",
    N356: "677b1ae2bab910db0805d20ee489d922522919ed",
    E8_PREFLIGHT: "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    E8_ADAPTER: "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
}
EXPECTED_REPORT_CANONICAL = "655c513f36ba239fdd46386adde3e1b16a01c46d3e2ebc0e46aca7d9a1f0e356"
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_row(row_id: str) -> tuple[int, int]:
    gpart, dpart = row_id.split("-")
    return int(gpart[1:]), int(dpart[1:])


def full178_rows(manifest: dict) -> list[str]:
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    req(len(rows) == 178 and len(set(rows)) == 178, "FULL178 row population drift")
    return rows


def n354_survivor_rows_for_e(rows: list[str], e: int) -> list[dict]:
    out = []
    for row_id in rows:
        g, d = parse_row(row_id)
        legacy_emin = 8 if g == 0 else 4
        n220_required = ceil_div(d - 16 * g + 16, 4)
        if not (max(legacy_emin, n220_required) <= e <= (19 * d) // 5):
            continue
        if d > e + 4 * g - 4:
            continue
        if e % 2 or d < 2 * ceil_div(e, 6):
            continue
        out.append({"row_id": row_id, "g": g, "d": d, "e": e})
    return out


def block_filter(base: tuple[int, ...], *, e: int, d: int, g: int) -> dict:
    by_label = {label: int(v) for label, v in zip(ASSIGNMENT_ORDER, base)}
    fixed = {label: value for label, value in by_label.items() if label != X4_LABEL}
    mass = sum(fixed.values())
    support = sum(v > 0 for v in fixed.values())
    required = ceil_div(d - 16 * g + 16, 4)
    n220 = support + min(38, e - mass) >= required
    sums = [sum(fixed[label] for label in grp) for grp in GROUPS]
    n355 = max(sums) <= d // 2
    b, c = sums[1], sums[2]
    n356 = b - c <= 3 * d - e
    return {
        "fixed": fixed,
        "mass": mass,
        "support": support,
        "required": required,
        "group_sums": sums,
        "n220": n220,
        "n355": n355,
        "n356": n356,
        "survives": bool(n220 and n355 and n356),
    }


def population(*, e: int, d: int, g: int) -> dict:
    idx = CompressedTerminalIndexer(e, d)
    width = idx.normal_budget + 1
    survivors = []
    raw = 0
    stream = hashlib.sha256()
    records = []
    for block_index in range(idx.exceptional_count):
        lo = block_index * width
        hi = lo + width - 1
        base = tuple(int(v) for v in idx.unrank(lo))
        top = tuple(int(v) for v in idx.unrank(hi))
        req(base[4] == 0 and top[4] == idx.normal_budget, f"x4 block regression {block_index}")
        req(base[:4] + base[5:] == top[:4] + top[5:], f"exceptional signature drift {block_index}")
        f = block_filter(base, e=e, d=d, g=g)
        if not f["survives"]:
            continue
        survivors.append(block_index)
        stream.update(f"{block_index}\n".encode())
        residual = e - int(f["mass"])
        parents = math.comb(residual + 19, 19)
        raw += parents
        records.append((block_index, parents))
    return {
        "idx": idx,
        "width": width,
        "survivors": survivors,
        "stream": stream.hexdigest(),
        "raw": raw,
        "records": records,
    }


def main() -> None:
    for path, expected in LOCKS.items():
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    report = json.loads(REPORT.read_text())
    body = dict(report)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == EXPECTED_REPORT_CANONICAL and csha(body) == EXPECTED_REPORT_CANONICAL,
        "scout report canonical drift")

    manifest = json.loads(MANIFEST.read_text())
    n353 = json.loads(N353.read_text())
    n354 = json.loads(N354.read_text())
    n356 = json.loads(N356.read_text())
    e8pf = json.loads(E8_PREFLIGHT.read_text())

    req(n353["candidate_scalar_rule"]["necessary_condition"] == "d <= e+4g-4",
        "N353 necessary condition drift")
    req(n354["necessary_condition"]["parity"] == "e % 2 == 0", "N354 parity drift")
    req(n354["necessary_condition"]["lower"] == "d >= 2*ceil(e/6)", "N354 lower bound drift")
    req(n356["transport_contract"]["even_degree_specialization"] == "b-c<=3*d-e",
        "N356 specialization drift")

    rows = full178_rows(manifest)
    req(n354_survivor_rows_for_e(rows, 4) == [], "unexpected e4 N354 survivor")
    req(n354_survivor_rows_for_e(rows, 6) == [], "unexpected e6 N354 survivor")
    e10_rows = n354_survivor_rows_for_e(rows, 10)
    req(e10_rows == [
        {"row_id": "g1-d008", "g": 1, "d": 8, "e": 10},
        {"row_id": "g1-d010", "g": 1, "d": 10, "e": 10},
    ], f"e10 N354 survivor frontier drift: {e10_rows}")

    p8 = population(e=10, d=8, g=1)
    req(p8["idx"].exceptional_count == 47256, "e10/d8 unfiltered block count drift")
    req(p8["idx"].terminal_count == 4867368 and p8["width"] == 103, "e10/d8 terminal geometry drift")
    req(len(p8["survivors"]) == 17375, "e10/d8 survivor block count drift")
    req(p8["stream"] == "b0a35a5cbad0bb3e907f0433b82e92db640207cafd8ae61820423df5f4c677b5",
        "e10/d8 survivor stream drift")
    req(p8["raw"] == 185744104, "e10/d8 raw parent accounting drift")
    req(len(p8["survivors"]) * 103 == 1789625, "e10/d8 terminal handoff count drift")

    wave = p8["records"][:255]
    wh = hashlib.sha256()
    for block_index, _ in wave:
        wh.update(f"{block_index}\n".encode())
    req([wave[0][0], wave[-1][0]] == [0, 560], "e10 initial wave source range drift")
    req(sum(v for _, v in wave) == 9366381, "e10 initial wave raw parent accounting drift")
    req(wh.hexdigest() == "948f4de1870fbec2b9d168ff6b99844afefcd9fdbac25c3c0918d95cc019d79a",
        "e10 initial wave stream drift")

    p10 = population(e=10, d=10, g=1)
    req(len(p10["survivors"]) == 31410 and p10["width"] == 141, "e10/d10 population drift")
    req(len(p10["survivors"]) * 141 == 4428810, "e10/d10 terminal handoff count drift")
    req(p10["raw"] == 189328410, "e10/d10 raw parent accounting drift")

    idx8 = CompressedTerminalIndexer(8, 8)
    idx10 = CompressedTerminalIndexer(10, 8)
    base8 = tuple(int(v) for v in idx8.unrank(0))
    base10 = tuple(int(v) for v in idx10.unrank(0))
    req(base8 == base10 == (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        "e8/e10 block0 signature monotonicity drift")
    f8 = block_filter(base8, e=8, d=8, g=1)
    f10 = block_filter(base10, e=10, d=8, g=1)
    req(f8["survives"] and f10["survives"], "block0 lost current-MAIN necessary filters")
    req(8 - f8["mass"] == 6 and 10 - f10["mass"] == 8, "residual cap monotonicity drift")
    req(e8pf["adapter_semantics"]["selected64_inverse_denominator"] == 8, "selected64 denominator drift")
    req(e8pf["adapter_semantics"]["free_selected_exceptional_count_per_block"] == 19,
        "selected64 free exceptional count drift")
    req(e8pf["adapter_semantics"]["first_block_regression_parent_count"] == 7336,
        "e8 first-block HNF parent regression")
    req(102 + 5 * 10 == 19 * 8 == 112 + 5 * 8, "weighted degree identity drift")

    print(json.dumps({
        "verdict": "PASS_FIRST_NON_E8_CUT_INTERFACE_POPULATION_E10_D8",
        "first_non_e8": 10,
        "e10_n354_rows": [r["row_id"] for r in e10_rows],
        "preferred_target": "g1-d008/e10",
        "current_main_blocks": len(p8["survivors"]),
        "current_main_terminals": len(p8["survivors"]) * p8["width"],
        "initial_wave_blocks": 255,
        "initial_wave_terminals": 255 * p8["width"],
        "e8_hnf_parent_subset_lower_bound": 7336,
        "production_pruning_credit": False,
        "stage32_main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
