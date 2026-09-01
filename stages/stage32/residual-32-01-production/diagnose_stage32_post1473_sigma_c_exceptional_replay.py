#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import re
from pathlib import Path

import sympy as sp
from sympy import Matrix

from pairing_prefix_engine import close_permutation_group

TANGENT_EXPECTED = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
WITNESS_EXPECTED = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
WITNESS_PICARD_EXPECTED = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
WITNESS_ALL140_EXPECTED = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
SIGMA_C_PICARD_ROWS_EXPECTED = "65f90a3356941bd4bdaeb77cfc3a8c5370d5726e2f66e2eb348bf5f9633af43a"
PICARD_GRAM_ROWS_EXPECTED = "22b1f891116ea16fcb615c95e9a83be9fef76c275d792e638d9ab0dab65a6e3b"
KC_WALL_GIT_BLOB_SHA1 = "03f07ef74986ac7aede6fc5ab462b41b71435561"
I = sp.I


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x) -> bool:
    return clean(x) == 0


def decode_element(v: list[int]):
    if len(v) != 4:
        raise ValueError("Q(i) encoded element shape regression")
    an, ad, bn, bd = (int(x) for x in v)
    if ad == 0 or bd == 0:
        raise ValueError("Q(i) encoded denominator is zero")
    return clean(sp.Rational(an, ad) + I * sp.Rational(bn, bd))


def decode_point(point: list[list[int]]):
    if len(point) != 7:
        raise ValueError("ambient P6 point length regression")
    return tuple(decode_element(v) for v in point)


def projective_normalize(v):
    values = [clean(x) for x in v]
    pivot = next((x for x in values if not is_zero(x)), None)
    if pivot is None:
        raise ValueError("zero projective vector")
    return tuple(clean(x / pivot) for x in values)


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = v
    return (
        clean(a1 * a1 + a2 * a2 - b3 * b3),
        clean(a2 * a2 + a3 * a3 - b1 * b1),
        clean(a1 * a1 + a3 * a3 - b2 * b2),
        clean(a1 * a1 + a2 * a2 + a3 * a3 - c * c),
    )


def neg_c(v):
    out = list(v)
    out[6] = clean(-out[6])
    return tuple(out)


def matrix_vector(v: Matrix) -> list[int]:
    return [int(v[i, 0]) for i in range(v.rows)]


def parse_literal(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise ValueError(f"missing Magma output {name}")
    return ast.literal_eval(m.group(1))


def materialize_pinned_kc_picard(repo: Path, retained_gram: list[list[int]]) -> dict:
    source_path = repo / "stages/stage33/33-07/stoll_cuboid_source.py"
    source = load_module(source_path, "stage32_post1473_pinned_stoll_source")
    _text, core, blob, fetch_attempt = source.load_pinned_source()
    extra = r'''
actperm32 := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
act32 := func<sch, subs | Curve(Pr6, [Evaluate(e, subs) : e in DefiningEquations(sch)])>;
function actpt32(pt, subs)
  i0 := 1; while pt[i0] eq 0 do i0 +:= 1; end while;
  pteqns := [Pr6.j*pt[i0] - Pr6.i0*pt[j] : j in [1..7] | j ne i0];
  return Rep(Points(Scheme(Pr6, [Evaluate(e, subs) : e in pteqns])));
end function;
su32 := [a1,a2,a3,b1,b2,b3,-c];
perm32 := [Position(C1s,act32(C,su32)):C in C1s]
 cat [#C1s+Position(C2s,act32(C,su32)):C in C2s]
 cat [#C1s+#C2s+Position(C3s,act32(C,su32)):C in C3s]
 cat [#Cs+Position(pts,actpt32(pt,su32)):pt in pts];
assert #Cs eq 92 and #pts eq 48 and #perm32 eq 140;
sigmaPic32 := Matrix(Integers(),[Eltseq(actperm32(Pic.j,perm32)):j in [1..64]]);
assert sigmaPic32*pmPic*Transpose(sigmaPic32) eq pmPic;
assert sigmaPic32^2 eq IdentityMatrix(Integers(),64);
printf "STAGE32_KC_PICARD_BEGIN\n";
printf "SIGMA_EXC_PERM=%o\n", [perm32[#Cs+j]-#Cs:j in [1..#pts]];
for r in [1..64] do printf "SIGMA_ROW_%o=%o\n",r,Eltseq(sigmaPic32[r]); end for;
for r in [1..64] do printf "GRAM_ROW_%o=%o\n",r,Eltseq(pmPic[r]); end for;
for j in [1..#pts] do printf "EXC_ROW_%o=%o\n",j,Eltseq(qPic(Big.(#Cs+j))); end for;
printf "STAGE32_KC_PICARD_END\n";
'''
    code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
    stdout, magma_attempt = source.run_magma(code, 240, "Stage32 Kc sigma-c Picard64 materialization")
    if "STAGE32_KC_PICARD_END" not in stdout or any(
        x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
    ):
        print(stdout)
        raise ValueError("pinned Kc Picard materialization failed")
    sigma_rows = [[int(x) for x in parse_literal(stdout, f"SIGMA_ROW_{r}")] for r in range(1, 65)]
    gram_rows = [[int(x) for x in parse_literal(stdout, f"GRAM_ROW_{r}")] for r in range(1, 65)]
    exceptional_rows = [[int(x) for x in parse_literal(stdout, f"EXC_ROW_{j}")] for j in range(1, 49)]
    sigma_exc_1based = [int(x) for x in parse_literal(stdout, "SIGMA_EXC_PERM")]
    if any(len(row) != 64 for row in sigma_rows + gram_rows + exceptional_rows):
        raise ValueError("pinned Kc Picard row width regression")
    if csha(sigma_rows) != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError(f"full sigma_c Picard64 hash mismatch: {csha(sigma_rows)}")
    if csha(gram_rows) != PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError(f"pinned Picard Gram hash mismatch: {csha(gram_rows)}")
    if gram_rows != retained_gram:
        raise ValueError("pinned Magma Picard Gram differs from retained Stage33 Gram")
    return {
        "testa_stoll_git_blob_sha1": blob,
        "source_fetch_attempt": fetch_attempt,
        "magma_request_attempt": magma_attempt,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "sigma_rows": sigma_rows,
        "sigma_rows_sha256": csha(sigma_rows),
        "sigma_exc_1based": sigma_exc_1based,
        "exceptional_rows": exceptional_rows,
        "exceptional_rows_sha256": csha(exceptional_rows),
        "gram_rows_sha256": csha(gram_rows),
    }


def replay_kc_pushforward(sigma_cert: dict) -> dict:
    here = Path(__file__).resolve().parent
    repo = Path(__file__).resolve().parents[3]
    witness_path = repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
    retained_path = repo / "stages/stage33/33-07/picard_base_rows_retained.py"
    endpoint_path = repo / "stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json"
    wall_path = here / "post1473-specific-class-kc-adapter-wall.md"

    witness = json.loads(witness_path.read_text())
    claimed = witness.get("canonical_sha256_without_this_field")
    body = dict(witness)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != WITNESS_EXPECTED or actual != WITNESS_EXPECTED:
        raise ValueError(f"V6 recovered witness source lock moved: claimed={claimed} actual={actual}")
    w = witness.get("witness", {})
    x_list = [int(v) for v in w.get("picard_coordinates", [])]
    p_list = [int(v) for v in w.get("all140_pairings", [])]
    if len(x_list) != 64 or len(p_list) != 140:
        raise ValueError("V6 witness vector shape regression")
    if csha(x_list) != WITNESS_PICARD_EXPECTED or w.get("picard_coordinates_sha256") != WITNESS_PICARD_EXPECTED:
        raise ValueError("V6 Picard coordinate hash regression")
    if csha(p_list) != WITNESS_ALL140_EXPECTED or w.get("all140_pairings_sha256") != WITNESS_ALL140_EXPECTED:
        raise ValueError("V6 all140 pairing hash regression")

    if git_blob_sha1(wall_path) != KC_WALL_GIT_BLOB_SHA1:
        raise ValueError("K_c source-lock wall blob moved")
    wall = wall_path.read_text()
    required_wall_strings = (
        "pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E",
        "(pi_*C)^2 = P^2 / 2",
        "(pi_*C)^2 >= 0",
        "degree `186/2=93`",
        "Lemma 12's even-degree condition",
    )
    missing = [s for s in required_wall_strings if s not in wall]
    if missing:
        raise ValueError(f"K_c source-lock semantics moved: {missing}")

    bundle = load_module(retained_path, "stage32_post1473_sigma_c_picard_bundle").load()
    gram_rows = [[int(x) for x in row] for row in bundle["picard_gram_64x64"]]
    gram = Matrix(gram_rows)
    if gram.shape != (64, 64) or gram != gram.T:
        raise ValueError("retained Picard Gram regression")

    endpoint = json.loads(endpoint_path.read_text())
    endpoint_sign_hashes = endpoint.get("picard_sign_rows_sha256", {})
    if endpoint.get("coordinate_order") != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
        raise ValueError("retained endpoint coordinate order moved")
    if endpoint_sign_hashes.get("c") != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError("retained endpoint c-sign Picard64 hash moved")
    if endpoint.get("picard_gram_rows_sha256") != PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("retained endpoint Picard Gram hash moved")

    mat = materialize_pinned_kc_picard(repo, gram_rows)
    sigma = Matrix(mat["sigma_rows"])
    exceptional = [Matrix(row) for row in mat["exceptional_rows"]]
    expected_exc = [int(x) + 1 for x in sigma_cert["sigma_c_exceptional_permutation_0based"]]
    if mat["sigma_exc_1based"] != expected_exc:
        raise ValueError("pinned Magma c-sign exceptional permutation disagrees with retained-node replay")
    for j, E in enumerate(exceptional):
        if int((E.T * gram * E)[0, 0]) != -2:
            raise ValueError(f"exceptional class {j} ceased to be a (-2)-class")
        target = exceptional[expected_exc[j] - 1]
        if sigma.T * E != target:
            raise ValueError(f"sigma_c Picard64 convention mismatch on exceptional class {j}")

    C = Matrix(x_list)
    C2 = sp.cancel((C.T * gram * C)[0, 0])
    if C2 != 758 or int(w.get("self_intersection")) != 758:
        raise ValueError(f"V6/V7 self-intersection regression: {C2}")
    for j, E in enumerate(exceptional):
        direct = int((C.T * gram * E)[0, 0])
        if direct != p_list[92 + j]:
            raise ValueError(f"V6 exceptional pairing convention mismatch at {j}: {direct} vs {p_list[92+j]}")

    sigma_C = sigma.T * C
    if sigma.T * sigma_C != C:
        raise ValueError("sigma_c Picard64 action failed involution on V6 class")
    sigma_C2 = int((sigma_C.T * gram * sigma_C)[0, 0])
    if sigma_C2 != 758:
        raise ValueError("sigma_c failed exact Picard isometry on V6 class")

    epi = [int(v) for v in sigma_cert["c_zero_exceptional_indices_0based"]]
    if len(epi) != 24 or len(set(epi)) != 24 or any(v < 0 or v >= 48 for v in epi):
        raise ValueError(f"E_pi retained exceptional shape regression: {epi}")
    if any(expected_exc[i] != i + 1 for i in epi):
        raise ValueError("E_pi node is not fixed by sigma_c")

    correction = Matrix.zeros(64, 1)
    correction_rows = []
    for j in epi:
        E = exceptional[j]
        coefficient = int((C.T * gram * E)[0, 0])
        correction += coefficient * E
        correction_rows.append({
            "exceptional_index_0based": j,
            "exceptional_id": f"EXC_{j + 1:03d}",
            "all140_curve_index_1based": 93 + j,
            "C_dot_E": coefficient,
            "picard_coordinates_sha256": csha(matrix_vector(E)),
        })

    P = C + sigma_C + correction
    P2 = int((P.T * gram * P)[0, 0])
    if P2 % 2:
        raise ValueError(f"P^2 is not divisible by quotient degree 2: {P2}")
    push2 = P2 // 2
    if push2 % 2:
        raise ValueError(f"K3 pushforward square is not even: {push2}")

    class_sigma_invariant = sigma_C == C
    noninvariant_excluded = push2 < 0
    invariant_case_obstruction = True
    result = {
        "mode": "EXACT_PINNED_TESTA_STOLL_SIGMA_C_AND_LEMMA11_SINGLE_V6_CLASS_REPLAY",
        "source_locks": {
            "v6_recovered_witness_canonical_sha256": claimed,
            "v6_picard_coordinates_sha256": WITNESS_PICARD_EXPECTED,
            "v6_all140_pairings_sha256": WITNESS_ALL140_EXPECTED,
            "kc_wall_git_blob_sha1": KC_WALL_GIT_BLOB_SHA1,
            "retained_picard_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_endpoint_c_sign_picard64_rows_sha256": SIGMA_C_PICARD_ROWS_EXPECTED,
            "retained_endpoint_picard_gram_rows_sha256": PICARD_GRAM_ROWS_EXPECTED,
            "testa_stoll_git_blob_sha1": mat["testa_stoll_git_blob_sha1"],
            "submitted_magma_code_sha256": mat["submitted_code_sha256"],
            "sigma_c_aut140_permutation_sha256": sigma_cert["sigma_c_aut140"]["permutation_sha256"],
        },
        "materialization": {
            "source_fetch_attempt": mat["source_fetch_attempt"],
            "magma_request_attempt": mat["magma_request_attempt"],
            "sigma_c_picard64_rows_sha256": mat["sigma_rows_sha256"],
            "exceptional_picard64_rows_sha256": mat["exceptional_rows_sha256"],
            "picard_gram_rows_sha256": mat["gram_rows_sha256"],
            "sigma_c_exceptional_permutation_matches_retained_nodes": True,
            "all_48_exceptional_classes_are_minus2": True,
            "sigma_c_picard_action_matches_all_48_exceptional_classes": True,
            "V6_all_48_exceptional_pairings_match_recovered_all140": True,
        },
        "formula": "P=C+sigma_c(C)+sum_{E in E_pi}(C.E)E=pi^*pi_*C; (pi_*C)^2=P^2/2",
        "C_square": int(C2),
        "sigma_C_square": sigma_C2,
        "C_dot_sigma_C": int((C.T * gram * sigma_C)[0, 0]),
        "C_picard_coordinates_sha256": csha(matrix_vector(C)),
        "sigma_C_picard_coordinates": matrix_vector(sigma_C),
        "sigma_C_picard_coordinates_sha256": csha(matrix_vector(sigma_C)),
        "class_sigma_c_invariant": bool(class_sigma_invariant),
        "E_pi_count": len(epi),
        "E_pi_exceptional_indices_0based": epi,
        "E_pi_exceptional_ids": [f"EXC_{i + 1:03d}" for i in epi],
        "E_pi_correction_terms": correction_rows,
        "E_pi_correction_picard_coordinates": matrix_vector(correction),
        "E_pi_correction_picard_coordinates_sha256": csha(matrix_vector(correction)),
        "E_pi_correction_square": int((correction.T * gram * correction)[0, 0]),
        "C_plus_sigma_C_dot_E_pi_correction": int(((C + sigma_C).T * gram * correction)[0, 0]),
        "P_picard_coordinates": matrix_vector(P),
        "P_picard_coordinates_sha256": csha(matrix_vector(P)),
        "P_square": P2,
        "pi_pushforward_C_square": push2,
        "noninvariant_integral_genus1_carrier_necessary_condition": "(pi_*C)^2>=0",
        "noninvariant_integral_genus1_carrier_excluded_by_negative_square": noninvariant_excluded,
        "invariant_curve_case_source_locked_even_degree_obstruction": invariant_case_obstruction,
        "invariant_curve_image_degree": 93,
        "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies": bool(noninvariant_excluded and invariant_case_obstruction),
        "scope": "SINGLE_V6_SUPPORT47_CLASS_ONLY",
        "firewalls": {
            "full178_closed": False,
            "general_low_genus_classification_closed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tangent", type=Path, required=True)
    p.add_argument("--marking", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    tangent = json.loads(args.tangent.read_text())
    tangent_claimed = tangent.get("canonical_sha256")
    tangent_body = dict(tangent)
    tangent_body.pop("canonical_sha256", None)
    tangent_actual = csha(tangent_body)
    if tangent_claimed != TANGENT_EXPECTED or tangent_actual != TANGENT_EXPECTED:
        raise ValueError(f"retained tangent source lock moved: claimed={tangent_claimed} actual={tangent_actual}")
    marking = load_module(args.marking, "stage32_post1473_sigma_c_marking").load()

    models = tangent["exceptional_models"]
    ids = [m["exceptional_id"] for m in models]
    if len(models) != 48 or tangent.get("exceptional_count") != 48 or ids != [f"EXC_{i:03d}" for i in range(1, 49)]:
        raise ValueError("48-exceptional tangent ordering regression")
    points = [decode_point(m["node_point_ambient_P6_L_basis"]) for m in models]
    normalized_points = [projective_normalize(q) for q in points]
    if len(set(normalized_points)) != 48:
        raise ValueError("retained exceptional nodes are not 48 distinct projective points")
    if any(any(not is_zero(x) for x in quadrics(q)) for q in points):
        raise ValueError("decoded node escaped ambient cuboid surface")
    zero_c = [i for i, q in enumerate(points) if is_zero(q[6])]
    if len(zero_c) != 24:
        raise ValueError(f"decoded ambient c=0 exceptional count regression: {len(zero_c)}")

    point_by_normalized = {q: i for i, q in enumerate(normalized_points)}
    sigma_exc = []
    for q in points:
        target = projective_normalize(neg_c(q))
        if target not in point_by_normalized:
            raise ValueError("ambient c-sign failed to permute retained 48 nodes")
        sigma_exc.append(point_by_normalized[target])
    if sorted(sigma_exc) != list(range(48)) or any(sigma_exc[sigma_exc[i]] != i for i in range(48)):
        raise ValueError("ambient c-sign node action is not an involutive permutation")
    if any(sigma_exc[i] != i for i in zero_c):
        raise ValueError("ambient c=0 exceptional node is not fixed by c-sign")

    aut = marking.get("aut_action", {})
    generators = aut.get("permutations_1based", [])
    full_group = close_permutation_group(generators)
    if len(full_group) != 1536:
        raise ValueError(f"retained Aut group order regression: {len(full_group)}")
    candidates = []
    for gi, g in enumerate(full_group):
        if all(g[92 + i] == 92 + sigma_exc[i] for i in range(48)):
            one_based = [int(x) + 1 for x in g]
            candidates.append({
                "closed_group_index": gi,
                "permutation_1based": one_based,
                "permutation_sha256": csha(one_based),
            })
    if len(candidates) != 1:
        raise ValueError(f"retained Aut140 c-sign match is not unique: {len(candidates)}")

    cert = {
        "schema": "STAGE32_POST1473_SIGMA_C_EXCEPTIONAL_KC_PUSHFORWARD_REPLAY_V5",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EPI_KC_PUSHFORWARD_REPLAY",
        "mode": "EXACT_RETAINED_NODE_C_SIGN_PLUS_PINNED_TESTA_STOLL_PICARD64_LEMMA11_REPLAY",
        "source_locks": {
            "tangent_canonical_sha256": tangent_claimed,
            "tangent_canonical_recomputed": tangent_actual,
            "tangent_producer": "stages/stage33/33-07/certify_exceptional_p1_tangent_coordinates.py",
            "tangent_producer_origin_commit": "8d8a455a02df891d45e9ad36c1e0a93cab3d3812",
            "coefficient_encoding": "[Re.numerator,Re.denominator,Im.numerator,Im.denominator] over Q(i)",
            "marking_canonical_sha256": marking.get("canonical_sha256"),
            "marking_aut_sha256": marking.get("stage32_aut_action_sha256"),
        },
        "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "decoded_nodes_satisfy_all_four_ambient_quadrics": True,
        "exceptional_model_order_exact": True,
        "c_zero_exceptional_indices_0based": zero_c,
        "c_zero_exceptional_ids": [ids[i] for i in zero_c],
        "c_zero_exceptional_count": len(zero_c),
        "direct_projective_node_match_complete": True,
        "sigma_c_exceptional_permutation_0based": sigma_exc,
        "sigma_c_exceptional_permutation_1based": [x + 1 for x in sigma_exc],
        "sigma_c_exceptional_permutation_sha256": csha([x + 1 for x in sigma_exc]),
        "retained_aut_group_order": len(full_group),
        "aut140_candidates_matching_exceptional_c_sign_count": len(candidates),
        "sigma_c_aut140": candidates[0],
    }
    cert["kc_pushforward_replay"] = replay_kc_pushforward(cert)
    cert["firewalls"] = {
        "full178_closed": False,
        "general_low_genus_classification_closed": False,
        "endpoint_credit": False,
        "route_credit": False,
        "theorem_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    kc = cert["kc_pushforward_replay"]
    print(json.dumps({
        "success": True,
        "c_zero_count": len(zero_c),
        "aut_candidate_count": len(candidates),
        "sigma_c_aut140_sha256": candidates[0]["permutation_sha256"],
        "sigma_c_picard64_sha256": kc["materialization"]["sigma_c_picard64_rows_sha256"],
        "class_sigma_c_invariant": kc["class_sigma_c_invariant"],
        "P_square": kc["P_square"],
        "pi_pushforward_C_square": kc["pi_pushforward_C_square"],
        "specific_class_genus1_excluded": kc["specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
