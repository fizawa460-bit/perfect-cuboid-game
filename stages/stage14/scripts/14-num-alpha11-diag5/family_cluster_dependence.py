#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
DIRECTIONS = ("a", "b", "c")
LATE_LO = (300_000_000, 400_000_000)
LATE_HI = (400_000_000, 500_000_000)


def load_rows():
    encoded = "".join(SOURCE.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"B500 source regression failed: rows={len(rows)} unique={len(set(rows))}")
    return sorted(rows)


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def face_mask(a: int, b: int, c: int):
    mask = 0
    diags = []
    for i, n in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        r = isqrt(n)
        if r*r == n:
            mask |= 1 << i
            diags.append(r)
        else:
            diags.append(0)
    return mask, tuple(diags)


def object_view(row):
    a, b, c, d, mask = row
    if mask == 0b011:
        return "a", a, (b, c)
    if mask == 0b101:
        return "b", b, (a, c)
    if mask == 0b110:
        return "c", c, (a, b)
    raise ArithmeticError(f"unexpected mask {mask}")


def primitive_face(shared: int, other: int, hyp: int):
    g = gcd(shared, other)
    if hyp % g:
        raise ArithmeticError("face primitive reduction failed")
    return shared // g, other // g, hyp // g


def object_edge(row):
    a, b, c, _, mask = row
    m2, (dab, dac, dbc) = face_mask(a, b, c)
    if m2 != mask:
        raise ArithmeticError(f"mask recomputation mismatch {row}: {m2}")
    if mask == 0b011:
        u = primitive_face(a, b, dab)
        v = primitive_face(a, c, dac)
    elif mask == 0b101:
        u = primitive_face(b, a, dab)
        v = primitive_face(b, c, dbc)
    elif mask == 0b110:
        u = primitive_face(c, a, dac)
        v = primitive_face(c, b, dbc)
    else:
        raise ArithmeticError(f"unexpected mask {mask}")
    return tuple(sorted((u, v)))


def shared_edge(row):
    return object_view(row)[1]


def direction(row):
    return object_view(row)[0]


def ratios(rows):
    c = Counter(direction(r) for r in rows)
    n = len(rows)
    return {q: c[q] / n for q in DIRECTIONS}


def vec(d):
    return [d[q] for q in DIRECTIONS]


def sub(x, y):
    return [x[i] - y[i] for i in range(len(x))]


def norm(x):
    return math.sqrt(sum(v*v for v in x))


def chi2_sf_df2(x: float) -> float:
    return math.exp(-x / 2.0)


def contingency_2x3(rows, exposure):
    tab = [[0, 0, 0], [0, 0, 0]]
    for r in rows:
        i = 1 if exposure(r) else 0
        j = DIRECTIONS.index(direction(r))
        tab[i][j] += 1
    rt = [sum(x) for x in tab]
    ct = [tab[0][j] + tab[1][j] for j in range(3)]
    n = sum(rt)
    if min(rt) == 0 or min(ct) == 0:
        return {"table_no_yes_by_abc": tab, "testable": False}
    chi2 = 0.0
    emin = float("inf")
    for i in range(2):
        for j in range(3):
            e = rt[i] * ct[j] / n
            emin = min(emin, e)
            chi2 += (tab[i][j] - e) ** 2 / e
    return {
        "table_no_yes_by_abc": tab,
        "testable": emin >= 5.0,
        "pearson_chi2": chi2,
        "df": 2,
        "pearson_p": chi2_sf_df2(chi2),
        "cramers_v": math.sqrt(chi2 / n),
        "minimum_expected_cell": emin,
    }


class DSU:
    def __init__(self):
        self.p = {}
        self.rank = {}

    def add(self, x):
        if x not in self.p:
            self.p[x] = x
            self.rank[x] = 0

    def find(self, x):
        p = self.p[x]
        if p != x:
            self.p[x] = self.find(p)
        return self.p[x]

    def union(self, a, b):
        self.add(a); self.add(b)
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def same_d_groups(rows):
    g = defaultdict(list)
    for i, r in enumerate(rows):
        g[r[3]].append(i)
    return {str(k): v for k, v in sorted(g.items())}


def face_component_groups(rows):
    dsu = DSU()
    edges = []
    degree = Counter()
    for i, r in enumerate(rows):
        e = object_edge(r)
        if e[0] == e[1]:
            raise ArithmeticError("loop in face graph")
        edges.append(e)
        dsu.union(*e)
        degree[e[0]] += 1
        degree[e[1]] += 1
    if len(set(edges)) != 3495:
        raise ArithmeticError(f"edge uniqueness regression failed {len(set(edges))}")
    if len(degree) != 5082 or max(degree.values()) != 13:
        raise ArithmeticError(f"face graph regression failed vertices={len(degree)} maxdeg={max(degree.values())}")
    by_root = defaultdict(list)
    vertices = defaultdict(set)
    for i, e in enumerate(edges):
        root = dsu.find(e[0])
        by_root[root].append(i)
        vertices[root].update(e)
    ordered = sorted(by_root, key=lambda root: (min(vertices[root]), len(by_root[root])))
    groups = {f"C{j+1:05d}": by_root[root] for j, root in enumerate(ordered)}
    meta = {
        f"C{j+1:05d}": {
            "vertices": len(vertices[root]),
            "id_min_vertex": list(min(vertices[root])),
        }
        for j, root in enumerate(ordered)
    }
    return groups, meta


def group_size_bin(m: int) -> str:
    if m == 1:
        return "1"
    if m == 2:
        return "2"
    if m == 3:
        return "3"
    if m <= 7:
        return "4-7"
    return "8+"


def histogram(groups):
    h = Counter(len(v) for v in groups.values())
    return {str(k): h[k] for k in sorted(h)}


def top_groups(rows, groups, meta=None, limit=12):
    out = []
    for gid, idxs in groups.items():
        rs = [rows[i] for i in idxs]
        c = Counter(direction(r) for r in rs)
        item = {
            "group_id": gid,
            "objects": len(rs),
            "direction_counts": {q: c[q] for q in DIRECTIONS},
            "distinct_d": len({r[3] for r in rs}),
            "d_min": min(r[3] for r in rs),
            "d_max": max(r[3] for r in rs),
        }
        if meta and gid in meta:
            item.update(meta[gid])
        out.append(item)
    return sorted(out, key=lambda x: (-x["objects"], x["group_id"]))[:limit]


def equal_group_ratios(rows, groups, predicate=lambda r: True):
    sums = Counter({q: 0.0 for q in DIRECTIONS})
    represented = 0
    for idxs in groups.values():
        rs = [rows[i] for i in idxs if predicate(rows[i])]
        if not rs:
            continue
        represented += 1
        c = Counter(direction(r) for r in rs)
        for q in DIRECTIONS:
            sums[q] += c[q] / len(rs)
    return {
        "represented_groups": represented,
        "ratios": {q: sums[q] / represented for q in DIRECTIONS},
    }


def shell_concentration(rows, groups, shell):
    counts = []
    for idxs in groups.values():
        n = sum(shell[0] < rows[i][3] <= shell[1] for i in idxs)
        if n:
            counts.append(n)
    total = sum(counts)
    shares = sorted((n / total for n in counts), reverse=True)
    hhi = sum(x*x for x in shares)
    return {
        "objects": total,
        "represented_groups": len(counts),
        "max_group_objects": max(counts),
        "max_group_share": shares[0],
        "top5_group_share": sum(shares[:5]),
        "hhi": hhi,
        "effective_group_count_inverse_hhi": 1.0 / hhi,
    }


def late_equalization(rows, groups):
    obj = {"lo": ratios([r for r in rows if LATE_LO[0] < r[3] <= LATE_LO[1]]),
           "hi": ratios([r for r in rows if LATE_HI[0] < r[3] <= LATE_HI[1]])}
    eq_lo = equal_group_ratios(rows, groups, lambda r: LATE_LO[0] < r[3] <= LATE_LO[1])
    eq_hi = equal_group_ratios(rows, groups, lambda r: LATE_HI[0] < r[3] <= LATE_HI[1])
    obj_shift = sub(vec(obj["hi"]), vec(obj["lo"]))
    eq_shift = sub(vec(eq_hi["ratios"]), vec(eq_lo["ratios"]))
    obj_n = norm(obj_shift)
    eq_n = norm(eq_shift)
    return {
        "object_weighted": obj,
        "equal_group_weighted": {"lo": eq_lo, "hi": eq_hi},
        "object_shift_hi_minus_lo": {q: obj_shift[i] for i, q in enumerate(DIRECTIONS)},
        "equal_group_shift_hi_minus_lo": {q: eq_shift[i] for i, q in enumerate(DIRECTIONS)},
        "object_shift_l2": obj_n,
        "equal_group_shift_l2": eq_n,
        "equal_group_to_object_shift_l2_ratio": eq_n / obj_n,
        "lo_concentration": shell_concentration(rows, groups, LATE_LO),
        "hi_concentration": shell_concentration(rows, groups, LATE_HI),
    }


def size_mixture_decomposition(rows, groups):
    row_bin = {}
    for gid, idxs in groups.items():
        b = group_size_bin(len(idxs))
        for i in idxs:
            row_bin[i] = b
    all_bins = ("1", "2", "3", "4-7", "8+")
    combined_idxs = [i for i, r in enumerate(rows) if LATE_LO[0] < r[3] <= LATE_HI[1]]
    class_dir = defaultdict(Counter)
    class_total = Counter()
    for i in combined_idxs:
        b = row_bin[i]
        q = direction(rows[i])
        class_dir[b][q] += 1
        class_total[b] += 1
    bins = [b for b in all_bins if class_total[b]]
    cond = {b: {q: class_dir[b][q] / class_total[b] for q in DIRECTIONS} for b in bins}
    weights = {}
    observed = {}
    predicted = {}
    for tag, shell in (("lo", LATE_LO), ("hi", LATE_HI)):
        idxs = [i for i, r in enumerate(rows) if shell[0] < r[3] <= shell[1]]
        mix = Counter(row_bin[i] for i in idxs)
        weights[tag] = {b: mix[b] / len(idxs) for b in bins}
        observed[tag] = ratios([rows[i] for i in idxs])
        predicted[tag] = {q: sum(weights[tag][b] * cond[b][q] for b in bins) for q in DIRECTIONS}
    obs_shift = sub(vec(observed["hi"]), vec(observed["lo"]))
    pred_shift = sub(vec(predicted["hi"]), vec(predicted["lo"]))
    residual = sub(obs_shift, pred_shift)
    obs_n = norm(obs_shift)
    return {
        "bins": bins,
        "shell_object_mix": weights,
        "pooled_direction_given_size_bin": cond,
        "observed_direction_ratios": observed,
        "mixture_only_predicted_direction_ratios": predicted,
        "observed_shift_l2": obs_n,
        "mixture_predicted_shift_l2": norm(pred_shift),
        "residual_shift_l2": norm(residual),
        "mixture_explained_fraction_l2": 1.0 - norm(residual) / obs_n if obs_n else 0.0,
        "same_data_descriptive_only": True,
    }


def comb2(n):
    return n * (n - 1) // 2


def comb3(n):
    return n * (n - 1) * (n - 2) // 6


def falling(n, k):
    out = 1
    for j in range(k):
        out *= n - j
    return out


def pair_clustering_moment_calibration(rows, groups):
    N = len(rows)
    C = Counter(direction(r) for r in rows)
    sizes = [len(v) for v in groups.values()]
    M = sum(comb2(m) for m in sizes)
    same = 0
    for idxs in groups.values():
        c = Counter(direction(rows[i]) for i in idxs)
        same += sum(comb2(c[q]) for q in DIRECTIONS)
    if M == 0:
        return {"within_group_pairs": 0, "calibration_available": False}
    p2 = sum(falling(C[q], 2) for q in DIRECTIONS) / falling(N, 2)
    p3 = sum(falling(C[q], 3) for q in DIRECTIONS) / falling(N, 3)
    p22_num = sum(falling(C[q], 4) for q in DIRECTIONS)
    for q in DIRECTIONS:
        for r in DIRECTIONS:
            if q != r:
                p22_num += falling(C[q], 2) * falling(C[r], 2)
    p22 = p22_num / falling(N, 4)
    H = sum(3 * comb3(m) for m in sizes)
    all_pairpairs = comb2(M)
    D = all_pairpairs - H
    var = M * p2 * (1 - p2) + 2 * H * (p3 - p2*p2) + 2 * D * (p22 - p2*p2)
    expected = M * p2
    z = (same - expected) / math.sqrt(var) if var > 0 else 0.0
    normal_two_sided_p = math.erfc(abs(z) / math.sqrt(2.0))
    return {
        "calibration_available": True,
        "within_group_pairs": M,
        "same_direction_pairs": same,
        "observed_same_direction_fraction": same / M,
        "fixed_global_label_shuffle_expected_fraction": p2,
        "expected_same_direction_pairs": expected,
        "exact_first_two_moment_variance_under_fixed_label_shuffle": var,
        "z_normal_moment_calibration": z,
        "normal_two_sided_p_calibration_only": normal_two_sided_p,
        "iid_claim": False,
        "normal_tail_is_calibration_only": True,
    }


def direction_support(rows, groups):
    support = Counter()
    repeated = 0
    repeated_multi = 0
    compositions = Counter()
    for idxs in groups.values():
        if len(idxs) < 2:
            continue
        repeated += 1
        c = Counter(direction(rows[i]) for i in idxs)
        k = sum(c[q] > 0 for q in DIRECTIONS)
        support[k] += 1
        if k >= 2:
            repeated_multi += 1
        compositions[f"a{c['a']}_b{c['b']}_c{c['c']}"] += 1
    return {
        "repeated_groups": repeated,
        "repeated_groups_with_multiple_directions": repeated_multi,
        "multiple_direction_fraction_among_repeated": repeated_multi / repeated if repeated else 0.0,
        "direction_support_size_histogram": {str(k): support[k] for k in sorted(support)},
        "top_repeated_direction_compositions": [
            {"composition": k, "groups": v} for k, v in compositions.most_common(12)
        ],
    }


def p7_rates(rows, groups=None):
    if groups is None:
        out = {}
        for q in DIRECTIONS:
            rs = [r for r in rows if direction(r) == q]
            yes = sum(shared_edge(r) % 7 == 0 for r in rs)
            out[q] = {"yes": yes, "total": len(rs), "rate": yes / len(rs)}
        return out
    out = {}
    for q in DIRECTIONS:
        vals = []
        for idxs in groups.values():
            rs = [rows[i] for i in idxs if direction(rows[i]) == q]
            if rs:
                vals.append(sum(shared_edge(r) % 7 == 0 for r in rs) / len(rs))
        out[q] = {"represented_groups": len(vals), "equal_group_mean_rate": sum(vals) / len(vals)}
    return out


def p7_cluster_controls(rows, same_d, components):
    m_d = {gid: len(idxs) for gid, idxs in same_d.items()}
    row_d_mult = {}
    for gid, idxs in same_d.items():
        for i in idxs:
            row_d_mult[i] = m_d[gid]
    m_c = {gid: len(idxs) for gid, idxs in components.items()}
    row_c_mult = {}
    for gid, idxs in components.items():
        for i in idxs:
            row_c_mult[i] = m_c[gid]
    repeated_d_rows = [r for i, r in enumerate(rows) if row_d_mult[i] >= 2]
    singleton_d_rows = [r for i, r in enumerate(rows) if row_d_mult[i] == 1]
    nontrivial_c_rows = [r for i, r in enumerate(rows) if row_c_mult[i] >= 2]
    isolated_c_rows = [r for i, r in enumerate(rows) if row_c_mult[i] == 1]
    exposure = lambda r: shared_edge(r) % 7 == 0
    return {
        "raw_object_weighted_rates": p7_rates(rows),
        "equal_same_d_weighted_rates": p7_rates(rows, same_d),
        "equal_face_component_weighted_rates": p7_rates(rows, components),
        "same_d_repeated_subset": {"rows": len(repeated_d_rows), **contingency_2x3(repeated_d_rows, exposure)},
        "same_d_singleton_subset": {"rows": len(singleton_d_rows), **contingency_2x3(singleton_d_rows, exposure)},
        "face_component_nontrivial_subset": {"rows": len(nontrivial_c_rows), **contingency_2x3(nontrivial_c_rows, exposure)},
        "face_component_isolated_subset": {"rows": len(isolated_c_rows), **contingency_2x3(isolated_c_rows, exposure)},
        "interpretation": "tests whether the strong diag4 p=7 shared-edge signature is merely produced by a few repeated diagonals or connected face families; subset p-values are calibration only",
    }


def summarize_scheme(rows, groups, meta=None):
    sizes = [len(v) for v in groups.values()]
    n = len(rows)
    singleton_objects = sum(len(v) for v in groups.values() if len(v) == 1)
    repeated_objects = n - singleton_objects
    return {
        "groups": len(groups),
        "objects": n,
        "mean_objects_per_group": n / len(groups),
        "max_objects_per_group": max(sizes),
        "group_size_histogram": histogram(groups),
        "singleton_objects": singleton_objects,
        "singleton_object_fraction": singleton_objects / n,
        "repeated_objects": repeated_objects,
        "repeated_object_fraction": repeated_objects / n,
        "object_weighted_mean_group_size": sum(m*m for m in sizes) / n,
        "global_object_weighted_direction_ratios": ratios(rows),
        "global_equal_group_weighted_direction_ratios": equal_group_ratios(rows, groups),
        "direction_support": direction_support(rows, groups),
        "pair_direction_clustering": pair_clustering_moment_calibration(rows, groups),
        "late_shell_equalization": late_equalization(rows, groups),
        "late_shell_group_size_mixture": size_mixture_decomposition(rows, groups),
        "top_groups": top_groups(rows, groups, meta),
    }


def main():
    rows = load_rows()
    total = Counter(direction(r) for r in rows)
    if tuple(total[q] for q in DIRECTIONS) != (1374, 1371, 750):
        raise ArithmeticError(f"direction regression failed {total}")
    lo = [r for r in rows if LATE_LO[0] < r[3] <= LATE_LO[1]]
    hi = [r for r in rows if LATE_HI[0] < r[3] <= LATE_HI[1]]
    if len(lo) != 328 or len(hi) != 301:
        raise ArithmeticError(f"late shell regression failed {len(lo)}, {len(hi)}")

    same_d = same_d_groups(rows)
    components, comp_meta = face_component_groups(rows)
    d_summary = summarize_scheme(rows, same_d)
    c_summary = summarize_scheme(rows, components, comp_meta)
    p7 = p7_cluster_controls(rows, same_d, components)

    d_att = d_summary["late_shell_equalization"]["equal_group_to_object_shift_l2_ratio"]
    c_att = c_summary["late_shell_equalization"]["equal_group_to_object_shift_l2_ratio"]
    d_z = d_summary["pair_direction_clustering"]["z_normal_moment_calibration"]
    c_z = c_summary["pair_direction_clustering"]["z_normal_moment_calibration"]

    report = {
        "stage": "14-num-alpha11-diag5",
        "classification": "SAME_DIAGONAL_AND_FACE_GRAPH_FAMILY_CLUSTER_DEPENDENCE_DIAGNOSTIC",
        "source": "merged Stage14-num-alpha11 frozen exact B500m 3495-row exactly-two census",
        "source_rows": len(rows),
        "global_direction_counts": {q: total[q] for q in DIRECTIONS},
        "cluster_schemes_predeclared": [
            "same space diagonal d",
            "connected component in the primitive oriented-face graph already frozen by Stage14-num",
        ],
        "same_diagonal": d_summary,
        "face_graph_component": c_summary,
        "diag4_p7_shared_divisibility_cluster_controls": p7,
        "interpretation_boundary": {
            "finite_exact_cluster_structure": True,
            "pair_label_shuffle_moment_model_is_calibration_only": True,
            "iid_arithmetic_objects_claim": False,
            "late_shell_equal_group_reweighting_is_descriptive_not_causal": True,
            "same_data_p7_subsets_are_not_independent_replication": True,
            "asymptotic_claim": False,
        },
        "decision": {
            "FAMILY_CLUSTER_DIAGNOSTIC_COMPLETE": True,
            "SAME_DIAGONAL_DIRECTIONAL_CLUSTERING_NORMAL_CALIBRATION_ABS_Z_GE_2": abs(d_z) >= 2.0,
            "FACE_GRAPH_COMPONENT_DIRECTIONAL_CLUSTERING_NORMAL_CALIBRATION_ABS_Z_GE_2": abs(c_z) >= 2.0,
            "LATE_SHIFT_MATERIALLY_ATTENUATED_BY_EQUAL_DIAGONAL_WEIGHTING_RATIO_LE_0P75": d_att <= 0.75,
            "LATE_SHIFT_MATERIALLY_ATTENUATED_BY_EQUAL_FACE_COMPONENT_WEIGHTING_RATIO_LE_0P75": c_att <= 0.75,
            "FINER_25M_SHELLS_RECOMMENDED_NEXT": False,
            "IID_ARITHMETIC_OBJECTS_CLAIM": False,
            "ASYMPTOTIC_CLAIM": False,
            "NEXT": "Stage14-num-alpha11-diag6 choose the stable observable after conditioning/reweighting, and directly compare the Stage13 exactly-one directional law with Stage14 exactly-two under matched cutoff/shell conventions",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
