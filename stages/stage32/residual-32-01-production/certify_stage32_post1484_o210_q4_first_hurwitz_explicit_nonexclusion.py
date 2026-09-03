#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path

REDUCTION_BLOB = "1f1b24eb09f48231a3897423c36f4e03095a6d75"
REDUCTION_CANONICAL = "329cf00d5380f515386622f5b18bcf90e36a99c16715e462ef9219abe0d609e1"
V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
INCIDENCE_BLOB = "b3f673aa73324ee731356eec2c0448592fd1e59b"
INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
SOURCE_NOTE_BLOB = "a72ff5572950a479e27a427c561c0c712f4ee998"
EXPECTED_CANONICAL = "ab0cfdda60096684f04ab90dfa6b4f98141194a19b7a39b881da0227ed56e4b1"
FIRST = [34, 35, 38, 39, 42, 43]
EXPECTED_C_DOT_L = [26, 31, 26, 25, 40, 34]
EXPECTED_K = [9, 4, 4, 5, 0, 6]
EXPECTED_R = [35, 35, 30, 30, 40, 40]
EXPECTED_FIXED = [35, 35, 45, 45, 25, 25]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical_without_field(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return csha(body)


def locked_json(path: Path, blob: str) -> dict:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return json.loads(raw)


def locked_text(path: Path, blob: str) -> str:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return raw.decode()


def involution(n: int, pairs: list[list[int]]) -> list[int]:
    p = list(range(n + 1))
    used: set[int] = set()
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError("bad transposition row")
        a, b = map(int, pair)
        if not (1 <= a <= n and 1 <= b <= n) or a == b or a in used or b in used:
            raise ValueError("not a matching")
        used.add(a)
        used.add(b)
        p[a], p[b] = b, a
    if any(p[p[i]] != i for i in range(1, n + 1)):
        raise ValueError("generator is not an involution")
    return p


def compose(p: list[int], q: list[int]) -> list[int]:
    # p after q
    return [0] + [p[q[i]] for i in range(1, len(p))]


def transitive(perms: list[list[int]]) -> bool:
    n = len(perms[0]) - 1
    seen = {1}
    q = deque([1])
    while q:
        x = q.popleft()
        for p in perms:
            y = p[x]
            if y not in seen:
                seen.add(y)
                q.append(y)
    return len(seen) == n


def validate(repo: Path, cert: dict) -> None:
    here = repo / "stages/stage32/residual-32-01-production"

    reduction = locked_json(here / "post1484-o210-q4-six-cusp-hurwitz-reduction.json", REDUCTION_BLOB)
    if canonical_without_field(reduction) != REDUCTION_CANONICAL:
        raise ValueError("six-cusp reduction canonical moved")
    if reduction["verdict"]["next_exact_leaf"] != "O210_Q4_SIX_CUSP_HURWITZ_MONODROMY_AND_SECOND_PROJECTION_COMPATIBILITY":
        raise ValueError("six-cusp reduction leaf moved")

    note = locked_text(here / "post1484-o210-q4-first-hurwitz-explicit-nonexclusion-source-note.md", SOURCE_NOTE_BLOB)
    for needle in ("Miranda", "SGA 1", "transitive product-one monodromy tuple", "O210_Q4_SECOND_PROJECTION_AND_COMMON_COVER_COMPATIBILITY"):
        if needle not in note:
            raise ValueError(f"source-note semantics moved: {needle}")

    v6 = locked_json(repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json", V6_BLOB)
    if v6.get("canonical_sha256_without_this_field") != V6_CANONICAL:
        raise ValueError("V6 canonical moved")
    all140 = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != ALL140_SHA:
        raise ValueError("V6 all140 moved")
    capacities = all140[92:]
    if len(capacities) != 48 or sum(capacities) != 266:
        raise ValueError("V6 exceptional capacity vector moved")

    incidence = locked_json(here / "post1473-x8-marked-exceptional-incidence.json", INCIDENCE_BLOB)
    if canonical_without_field(incidence) != INCIDENCE_CANONICAL:
        raise ValueError("exceptional incidence canonical moved")
    first_by_exc = {int(row["exceptional_label"]): int(row["first_factor_boundary_label"]) for row in incidence["rows"]}
    if sorted(first_by_exc) != list(range(93, 141)):
        raise ValueError("exceptional incidence labels moved")

    witness = cert["reachable_nodewise_contact_witness"]
    rows = witness["nodes"]
    if [int(row["exceptional_label"]) for row in rows] != list(range(93, 141)):
        raise ValueError("node witness does not cover 93..140 exactly")
    group_k = {label: 0 for label in FIRST}
    m1_total = 0
    m2_total = 0
    for row, cap in zip(rows, capacities):
        exc = int(row["exceptional_label"])
        if int(row["capacity"]) != cap:
            raise ValueError(f"capacity mismatch at exceptional {exc}")
        m1 = int(row["m1_contacts"])
        m2 = int(row["m2_contacts"])
        if m1 < 0 or m2 < 0 or m1 + 2 * m2 != cap:
            raise ValueError(f"invalid m1/m2 split at exceptional {exc}")
        m1_total += m1
        m2_total += m2
        group_k[first_by_exc[exc]] += m2
    if (m1_total, m2_total, m1_total + 2 * m2_total) != (210, 28, 266):
        raise ValueError("node witness totals moved")
    if [group_k[label] for label in FIRST] != EXPECTED_K:
        raise ValueError(f"first-cusp m2 aggregation moved: {group_k}")

    aggregation = cert["first_cusp_aggregation"]
    if aggregation["boundary_order"] != FIRST or aggregation["C_dot_L"] != EXPECTED_C_DOT_L or aggregation["m2_contacts"] != EXPECTED_K:
        raise ValueError("first-cusp aggregation inputs moved")
    r = [a + b for a, b in zip(EXPECTED_C_DOT_L, EXPECTED_K)]
    fixed = [105 - 2 * x for x in r]
    if r != EXPECTED_R or fixed != EXPECTED_FIXED:
        raise ValueError("cycle-type arithmetic moved")
    if aggregation["transposition_counts"] != r or aggregation["fixed_point_counts"] != fixed:
        raise ValueError("claimed cycle types moved")
    if sum(r) != 210:
        raise ValueError("RH total moved")

    tuple_data = cert["explicit_branch_cycle_tuple"]
    if tuple_data["degree"] != 105 or tuple_data["branch_labels"] != FIRST or tuple_data["generator_names"] != ["A", "A", "B", "B", "C", "C"]:
        raise ValueError("branch tuple labels/names moved")
    pairs = tuple_data["involution_transpositions"]
    if [len(pairs[k]) for k in ("A", "B", "C")] != [35, 30, 40]:
        raise ValueError("generator transposition counts moved")
    perms = {k: involution(105, pairs[k]) for k in ("A", "B", "C")}
    ordered = [perms[k] for k in tuple_data["generator_names"]]
    product = list(range(106))
    for p in ordered:
        product = compose(product, p)
    if product != list(range(106)):
        raise ValueError("branch-cycle product is not identity")
    if not transitive([perms["A"], perms["B"], perms["C"]]):
        raise ValueError("generated action is not transitive")

    # Stronger graph replay: the three matching edge sets must be exactly one
    # connected 105-cycle. This makes transitivity transparent and guards
    # against a tuple that passes only through an implementation accident.
    adj = {i: set() for i in range(1, 106)}
    unique_edges: set[tuple[int, int]] = set()
    for name in ("A", "B", "C"):
        for a, b in pairs[name]:
            edge = tuple(sorted((int(a), int(b))))
            unique_edges.add(edge)
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
    if len(unique_edges) != 105 or any(len(adj[i]) != 2 for i in range(1, 106)):
        raise ValueError("colored union is not a 2-regular 105-edge graph")
    seen = {1}
    q = deque([1])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append(y)
    if len(seen) != 105:
        raise ValueError("colored union is disconnected")

    # Degree 105, six involution branch cycles with 210 total transpositions:
    # 2g-2 = -2*105 + 210 = 0, so g=1.
    genus_numerator = -2 * 105 + sum(r)
    if genus_numerator != 0:
        raise ValueError("Riemann-Hurwitz genus numerator moved")

    verdict = cert["verdict"]
    if verdict != {
        "O210_excluded": False,
        "first_projection_cycle_type_condition_excluded": False,
        "first_projection_hurwitz_level_nonexcluded": True,
        "first_projection_transitive_product_one_monodromy_excluded": False,
        "next_exact_leaf": "O210_Q4_SECOND_PROJECTION_AND_COMMON_COVER_COMPATIBILITY",
    }:
        raise ValueError("verdict moved")
    if cert["firewalls"].get("simultaneous_second_projection_not_constructed") is not True or cert["firewalls"].get("this_is_not_fixed_V6_carrier_existence") is not True:
        raise ValueError("required firewalls missing")
    if canonical_without_field(cert) != EXPECTED_CANONICAL or cert.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        raise ValueError(f"canonical moved: {canonical_without_field(cert)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", required=True, type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    cert = json.loads(args.check.read_text())
    validate(repo, cert)
    print("PASS", EXPECTED_CANONICAL)


if __name__ == "__main__":
    main()
