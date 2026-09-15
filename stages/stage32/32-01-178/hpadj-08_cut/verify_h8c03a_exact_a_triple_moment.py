#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CXX = HERE / "h8c03a_exact_a_triple_moment.cpp"
RESULT = HERE / "H8C-03A-RESULT.json"
H8C02_RESULT = HERE / "H8C-02-RESULT.json"
N358_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")

N358_AUDITED_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
N358_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
CXX_BLOB = "65d554c53ffb6a3a3be4fa51a52e6dd16821b2dc"
RESULT_BLOB = "248aaad49186b5efdf187114e9efd98db1f320ad"
H8C02_RESULT_BLOB = "81cfcbe8f9cb9c1c9750be3187e15f61ade3ea9d"
EXPECTED_BC_CELLS = 97 * 97 * 8


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def exact_head(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve audited N358 checkout head: " + exc.output.strip()) from exc


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def check_projection(path: Path, bc, hmax: int) -> tuple[int, str]:
    expected_cells = (hmax + 1) * (hmax + 1) * 8
    req(expected_cells == EXPECTED_BC_CELLS, "audited N358 HMAX/domain drift")
    seen = 0
    stream = hashlib.sha256()
    with path.open("rb") as fh:
        for b in range(hmax + 1):
            for c in range(hmax + 1):
                for support in range(8):
                    raw = fh.readline()
                    req(bool(raw), f"truncated C++ BC projection at cell {seen}")
                    stream.update(raw)
                    try:
                        fields = raw.decode("utf-8").rstrip("\n").split("\t")
                        got_b, got_c, got_s, got_value = map(int, fields)
                    except Exception as exc:
                        raise SystemExit(f"FAIL: malformed C++ BC projection at cell {seen}: {raw!r}") from exc
                    req((got_b, got_c, got_s) == (b, c, support), f"C++ BC coordinate/order drift at cell {seen}")
                    req(got_value == bc[b][c][support], f"C++ BC value != audited N358 build_bc_exact at {(b, c, support)}")
                    seen += 1
        req(fh.readline() == b"", "C++ BC projection has trailing cells/data")
    req(seen == expected_cells, "C++ BC projection cell-count drift")
    return seen, stream.hexdigest()


def check_rows(path: Path, result: dict, cpp: dict) -> tuple[int, str]:
    raw = path.read_bytes()
    stream_sha = hashlib.sha256(raw).hexdigest()
    expected_sha = result["verification"]["row_stream_sha256"]
    req(stream_sha == expected_sha, "H8C-03A 178-row stream SHA256 drift")

    lines = raw.splitlines()
    expected_order = [(0, d) for d in range(8, 177, 2)] + [(1, d) for d in range(8, 193, 2)]
    req(len(lines) == result["verification"]["row_count"] == len(expected_order) == 178, "H8C-03A row-count drift")

    keys = {
        "g", "d", "h8c02_prefixes", "h8c03a_prefixes",
        "h8c02_terms", "h8c03a_terms", "incremental_vs_h8c02",
    }
    rows = []
    for idx, (line, expected_gd) in enumerate(zip(lines, expected_order)):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"FAIL: malformed H8C-03A row {idx}") from exc
        req(set(row) == keys, f"H8C-03A row schema drift at {idx}")
        req((row["g"], row["d"]) == expected_gd, f"H8C-03A row order/domain drift at {idx}")
        req(row["h8c03a_terms"] >= row["h8c02_terms"], f"H8C-03A dominance regression at row {idx}")
        req(row["incremental_vs_h8c02"] == row["h8c03a_terms"] - row["h8c02_terms"], f"H8C-03A row subtraction drift at {idx}")
        rows.append(row)

    sums = {
        "h8c02_rejected_terminals": sum(r["h8c02_terms"] for r in rows),
        "h8c03a_rejected_terminals": sum(r["h8c03a_terms"] for r in rows),
        "incremental_vs_h8c02": sum(r["incremental_vs_h8c02"] for r in rows),
        "h8c02_prefixes": sum(r["h8c02_prefixes"] for r in rows),
        "h8c03a_prefixes": sum(r["h8c03a_prefixes"] for r in rows),
        "h8c03a_genus0_terms": sum(r["h8c03a_terms"] for r in rows if r["g"] == 0),
        "h8c03a_genus1_terms": sum(r["h8c03a_terms"] for r in rows if r["g"] == 1),
    }
    for key, value in sums.items():
        req(cpp[key] == value, f"C++ aggregate != 178-row sum for {key}")

    req(sum(1 for r in rows if r["h8c02_terms"] > 0) == cpp["h8c02_rows"] == 178, "H8C-02 nonzero-row count drift")
    req(sum(1 for r in rows if r["h8c03a_terms"] > 0) == cpp["h8c03a_rows"] == 178, "H8C-03A nonzero-row count drift")
    req(sum(1 for r in rows if r["incremental_vs_h8c02"] > 0) == cpp["incremental_rows"] == result["verification"]["affected_incremental_rows"], "H8C-03A incremental-row count drift")
    return len(rows), stream_sha


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n358-root", required=True, type=Path)
    args = ap.parse_args()

    req(CXX.is_file() and git_blob(CXX) == CXX_BLOB, "H8C-03A C++ source-lock drift")
    req(RESULT.is_file() and git_blob(RESULT) == RESULT_BLOB, "H8C-03A RESULT source-lock drift")
    req(H8C02_RESULT.is_file() and git_blob(H8C02_RESULT) == H8C02_RESULT_BLOB, "H8C-02 RESULT source-lock drift")
    result = json.loads(RESULT.read_text())
    h8c02 = json.loads(H8C02_RESULT.read_text())

    audited = args.audited_n358_root.resolve()
    req(audited.is_dir(), "missing audited N358 checkout")
    req(exact_head(audited) == N358_AUDITED_HEAD, "audited N358 exact-head drift")
    n358_path = audited / N358_REL
    req(n358_path.is_file() and git_blob(n358_path) == N358_BLOB, "audited N358 verifier blob drift")
    n358 = load_module(n358_path, "stage32_h8c03a_audited_n358")
    req(n358.HMAX == 96, "audited N358 HMAX drift")
    audited_bc = n358.build_bc_exact(n358.HMAX)
    req(n358.n357_count_witness(audited_bc) == result["verification"]["n357_witness"], "audited N358 witness drift")

    with tempfile.TemporaryDirectory(prefix="stage32-h8c03a-") as td:
        tmp = Path(td)
        binary = tmp / "h8c03a"
        rows_path = tmp / "rows.jsonl"
        projection_path = tmp / "bc-projection.tsv"
        compile_run = subprocess.run(
            ["g++", "-std=c++17", "-O3", "-DNDEBUG", str(CXX), "-o", str(binary)],
            text=True,
            capture_output=True,
            timeout=120,
        )
        req(compile_run.returncode == 0, "H8C-03A C++ compilation failed: " + compile_run.stderr[-2000:])
        run = subprocess.run(
            [str(binary), str(rows_path), str(projection_path)],
            text=True,
            capture_output=True,
            timeout=300,
        )
        req(run.returncode == 0, "H8C-03A C++ execution failed: " + run.stderr[-2000:])

        # The C++ aggregate is not trusted until its entire reconstructed BC table
        # has been checked cell-for-cell against audited N358 build_bc_exact().
        cells, projection_sha = check_projection(projection_path, audited_bc, n358.HMAX)

        stdout_lines = [line for line in run.stdout.splitlines() if line.strip()]
        req(len(stdout_lines) == 1, "H8C-03A C++ stdout schema drift")
        try:
            cpp = json.loads(stdout_lines[0])
        except json.JSONDecodeError as exc:
            raise SystemExit("FAIL: malformed H8C-03A C++ aggregate JSON") from exc

        required_cpp = {
            "n357_witness", "h8c02_rejected_terminals", "h8c03a_rejected_terminals",
            "incremental_vs_h8c02", "h8c02_prefixes", "h8c03a_prefixes",
            "h8c03a_genus0_terms", "h8c03a_genus1_terms",
            "h8c02_rows", "h8c03a_rows", "incremental_rows",
        }
        req(set(cpp) == required_cpp, "H8C-03A C++ aggregate schema drift")
        req(cpp["n357_witness"] == result["verification"]["n357_witness"], "H8C-03A C++ N357 witness drift")

        rows, row_sha = check_rows(rows_path, result, cpp)

    aggregate = result["aggregate"]
    for key in (
        "h8c02_rejected_terminals", "h8c03a_rejected_terminals", "incremental_vs_h8c02",
        "h8c02_prefixes", "h8c03a_prefixes", "h8c03a_genus0_terms", "h8c03a_genus1_terms",
    ):
        req(cpp[key] == aggregate[key], f"H8C-03A frozen aggregate drift for {key}")

    req(cpp["h8c03a_prefixes"] - cpp["h8c02_prefixes"] == aggregate["incremental_prefixes_vs_h8c02"], "H8C-03A prefix increment drift")
    hpadj07 = h8c02["population_replay"]["hpadj07_rejected_terminals"]
    req(cpp["h8c02_rejected_terminals"] == h8c02["population_replay"]["h8c02_rejected_terminals"], "H8C-02 predecessor identity drift")
    req(cpp["h8c03a_rejected_terminals"] - hpadj07 == aggregate["incremental_vs_hpadj07"], "H8C-03A HPADJ-07 increment drift")

    firewalls = result["firewalls"]
    req(firewalls["main_pruning_credit"] is False, "MAIN credit firewall drift")
    req(firewalls["current_authority_overlap_accounted"] is False, "overlap firewall drift")
    req(firewalls["double_charge_accounted"] is False, "double-charge firewall drift")
    req(firewalls["merge_authorized"] is False, "merge firewall drift")

    print(json.dumps({
        "status": "PASS_H8C03A_EXACT_N358_BC_CPP_AGGREGATE_REPLAY_CANDIDATE",
        "audited_n358_head": N358_AUDITED_HEAD,
        "audited_n358_bc_cells_exact_match": cells,
        "bc_projection_sha256": projection_sha,
        "row_count": rows,
        "row_stream_sha256": row_sha,
        "h8c03a_rejected_terminals": cpp["h8c03a_rejected_terminals"],
        "incremental_vs_h8c02": cpp["incremental_vs_h8c02"],
        "main_pruning_credit": False,
        "hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
