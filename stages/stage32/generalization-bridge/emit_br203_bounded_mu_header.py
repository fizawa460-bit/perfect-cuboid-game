#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_SCHEMA = "STAGE32_BR203_PICARD_MU_16_STATE_V2"
EXPECTED_MU_SHA256 = "f8570c9b045c204d55231cd855832648dbac1f26244c9581855f21cf4f8b6dbb"
EXPECTED_TERMINAL_SHA256 = "2456dba5d197737eaa6be0e0a83bbe8087dcea638d4a50c2f2ef737bfdbd6a31"

LABEL_FOR_X = {
    0: 95,
    1: 99,
    2: 103,
    3: 102,
    5: 97,
    6: 94,
    7: 101,
    8: 93,
    9: 98,
    10: 96,
}


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def syndrome_mask(values: list[int]) -> int:
    req(len(values) == 46, "syndrome row count is not 46")
    mask = 0
    for i, value in enumerate(values):
        req(value in (0, 4), f"syndrome entry {i} is not 0/4: {value}")
        if value == 4:
            mask |= 1 << i
    return mask


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("result", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()

    data = json.loads(args.result.read_text())
    req(data.get("schema") == EXPECTED_SCHEMA, "BR203 result schema drift")
    req(data.get("status") == "PASS_SOURCE_LOCKED_HISTORICAL_BC2_COORDINATES_16_STATE_MU_ZERO_CREDIT", "BR203 result not PASS")
    req(data.get("selected64_replay", {}).get("historical_bc2_18_exact_match") is True, "historical BC2 coordinate replay not exact")

    mu = data.get("mu", {})
    req(mu.get("state_count") == 16, "mu state count drift")
    req(mu.get("max_mu") == 2, "mu max drift")
    req(mu.get("table_sha256") == EXPECTED_MU_SHA256, "mu table hash drift")

    terminal = data.get("terminal_syndrome_columns", {})
    req(terminal.get("sha256") == EXPECTED_TERMINAL_SHA256, "terminal syndrome hash drift")
    a_cols = terminal.get("A", {})
    bc_cols = terminal.get("BC", {})
    all_cols = {**a_cols, **bc_cols}

    masks: dict[int, int] = {}
    for x, label in LABEL_FOR_X.items():
        key = str(label)
        req(key in all_cols, f"missing terminal syndrome label {label}")
        masks[x] = syndrome_mask(all_cols[key])

    table: list[tuple[int, int]] = []
    for row in mu.get("table", []):
        table.append((syndrome_mask(row["syndrome"]), int(row["mu"])))
    req(len(table) == 16, "mu table length drift")
    req(len({mask for mask, _ in table}) == 16, "mu syndrome masks are not unique")
    req(sorted(v for _, v in table) == [0] + [1] * 7 + [2] * 8, "mu histogram drift")

    lines = [
        "#pragma once",
        "#include <array>",
        "#include <cstdint>",
        "using Br203Syn = std::uint64_t;",
        f'inline constexpr const char* BR203_MU_TABLE_SHA256 = "{EXPECTED_MU_SHA256}";',
        f'inline constexpr const char* BR203_TERMINAL_SHA256 = "{EXPECTED_TERMINAL_SHA256}";',
    ]
    for x in sorted(masks):
        lines.append(f"inline constexpr Br203Syn BR203_S_X{x} = 0x{masks[x]:x}ULL;")

    lines.extend([
        "struct Br203MuEntry { Br203Syn syndrome; int mu; };",
        "inline constexpr std::array<Br203MuEntry,16> BR203_MU_TABLE{{",
    ])
    for mask, value in table:
        lines.append(f"    {{0x{mask:x}ULL, {value}}},")
    lines.extend([
        "}};",
        "inline constexpr std::array<Br203Syn,8> BR203_A_SYNDROMES{{",
        "    0ULL,",
        "    BR203_S_X2,",
        "    BR203_S_X3,",
        "    BR203_S_X2 ^ BR203_S_X3,",
        "    BR203_S_X7,",
        "    BR203_S_X2 ^ BR203_S_X7,",
        "    BR203_S_X3 ^ BR203_S_X7,",
        "    BR203_S_X2 ^ BR203_S_X3 ^ BR203_S_X7,",
        "}};",
    ])
    args.output.write_text("\n".join(lines) + "\n")
    print(json.dumps({
        "status": "PASS_BR203_MU_HEADER_EMITTED",
        "mu_table_sha256": EXPECTED_MU_SHA256,
        "terminal_syndrome_sha256": EXPECTED_TERMINAL_SHA256,
        "state_count": 16,
        "max_mu": 2,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
