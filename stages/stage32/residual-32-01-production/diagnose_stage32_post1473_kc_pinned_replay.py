#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path

from sympy import Matrix

import diagnose_stage32_post1473_sigma_c_exceptional_replay as base

ENDPOINT_EXPECTED = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
SIGMA_C_PICARD_ROWS_EXPECTED = "65f90a3356941bd4bdaeb77cfc3a8c5370d5726e2f66e2eb348bf5f9633af43a"
PICARD_GRAM_ROWS_EXPECTED = "22b1f891116ea16fcb615c95e9a83be9fef76c275d792e638d9ab0dab65a6e3b"


def lit(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise ValueError(f"missing Magma output {name}")
    return ast.literal_eval(m.group(1))


def pinned_picard_materialization(repo: Path, retained_gram: list[list[int]]) -> dict:
    source = base.load_module(repo / "stages/stage33/33-07/stoll_cuboid_source.py", "stage32_kc_pinned_stoll")
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
printf "STAGE32_KC_PINNED_BEGIN\n";
printf "SIGMA_EXC_PERM=%o\n",[perm32[#Cs+j]-#Cs:j in [1..#pts]];
for r in [1..64] do printf "SIGMA_ROW_%o=%o\n",r,[sigmaPic32[r,k]:k in [1..64]]; end for;
for r in [1..64] do printf "GRAM_ROW_%o=%o\n",r,[pmPic[r,k]:k in [1..64]]; end for;
for j in [1..#pts] do printf "EXC_ROW_%o=%o\n",j,Eltseq(qPic(Big.(#Cs+j))); end for;
printf "STAGE32_KC_PINNED_END\n";
'''
    code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
    stdout, magma_attempt = source.run_magma(code, 240, "Stage32 pinned Kc Picard64 replay")
    if "STAGE32_KC_PINNED_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")):
        print(stdout)
        raise ValueError("pinned Kc Picard materialization failed")
    sigma_rows = [[int(x) for x in lit(stdout, f"SIGMA_ROW_{r}")] for r in range(1, 65)]
    gram_rows = [[int(x) for x in lit(stdout, f"GRAM_ROW_{r}")] for r in range(1, 65)]
    exc_rows = [[int(x) for x in lit(stdout, f"EXC_ROW_{j}")] for j in range(1, 49)]
    sigma_exc = [int(x) for x in lit(stdout, "SIGMA_EXC_PERM")]
    if any(len(row) != 64 for row in sigma_rows + gram_rows + exc_rows):
        raise ValueError("pinned Picard64 row shape regression")
    if base.csha(sigma_rows) != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError(f"sigma_c Picard64 retained hash mismatch: {base.csha(sigma_rows)}")
    if base.csha(gram_rows) != PICARD_GRAM_ROWS_EXPECTED or gram_rows != retained_gram:
        raise ValueError("pinned Picard Gram differs from retained Stage33 Gram")
    return {
        "testa_stoll_git_blob_sha1": blob,
        "source_fetch_attempt": fetch_attempt,
        "magma_request_attempt": magma_attempt,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "sigma_rows": sigma_rows,
        "sigma_rows_sha256": base.csha(sigma_rows),
        "gram_rows_sha256": base.csha(gram_rows),
        "exceptional_rows": exc_rows,
        "exceptional_rows_sha256": base.csha(exc_rows),
        "sigma_exceptional_permutation_1based": sigma_exc,
    }


def geometry(tangent: dict, marking: dict) -> dict:
    body = dict(tangent)
    claimed = body.pop("canonical_sha256", None)
    actual = base.csha(body)
    if claimed != base.TANGENT_EXPECTED or actual != base.TANGENT_EXPECTED:
        raise ValueError("retained tangent lock moved")
    models = tangent["exceptional_models"]
    ids = [m["exceptional_id"] for m in models]
    if len(models) != 48 or ids != [f"EXC_{i:03d}" for i in range(1, 49)]:
        raise ValueError("retained exceptional ordering moved")
    pts = [base.decode_point(m["node_point_ambient_P6_L_basis"]) for m in models]
    norm = [base.projective_normalize(q) for q in pts]
    if len(set(norm)) != 48 or any(any(not base.is_zero(x) for x in base.quadrics(q)) for q in pts):
        raise ValueError("retained exceptional node geometry regression")
    epi = [i for i, q in enumerate(pts) if base.is_zero(q[6])]
    if len(epi) != 24:
        raise ValueError(f"E_pi count regression: {len(epi)}")
    bypt = {q: i for i, q in enumerate(norm)}
    sigma_exc = []
    for q in pts:
        target = base.projective_normalize(base.neg_c(q))
        if target not in bypt:
            raise ValueError("c-sign escaped retained node set")
        sigma_exc.append(bypt[target])
    if sorted(sigma_exc) != list(range(48)) or any(sigma_exc[sigma_exc[i]] != i for i in range(48)):
        raise ValueError("c-sign node action is not an involutive permutation")
    if any(sigma_exc[i] != i for i in epi):
        raise ValueError("E_pi node not fixed by c-sign")
    group = base.close_permutation_group(marking["aut_action"]["permutations_1based"])
    if len(group) != 1536:
        raise ValueError("retained Aut140 group-order regression")
    matches = [g for g in group if all(g[92 + i] == 92 + sigma_exc[i] for i in range(48))]
    if len(matches) != 1:
        raise ValueError(f"Aut140 c-sign match count regression: {len(matches)}")
    aut1 = [int(x) + 1 for x in matches[0]]
    return {
        "tangent_canonical_sha256": claimed,
        "E_pi_indices_0based": epi,
        "E_pi_ids": [ids[i] for i in epi],
        "sigma_exceptional_0based": sigma_exc,
        "sigma_exceptional_1based": [x + 1 for x in sigma_exc],
        "sigma_exceptional_sha256": base.csha([x + 1 for x in sigma_exc]),
        "sigma_aut140_1based": aut1,
        "sigma_aut140_sha256": base.csha(aut1),
        "aut140_match_count": 1,
    }


def pushforward(repo: Path, geo: dict) -> dict:
    witness = json.loads((repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json").read_text())
    wb = dict(witness)
    wc = wb.pop("canonical_sha256_without_this_field", None)
    if wc != base.WITNESS_EXPECTED or base.csha(wb) != base.WITNESS_EXPECTED:
        raise ValueError("V6 recovered witness lock moved")
    w = witness["witness"]
    x = [int(v) for v in w["picard_coordinates"]]
    p = [int(v) for v in w["all140_pairings"]]
    if base.csha(x) != base.WITNESS_PICARD_EXPECTED or base.csha(p) != base.WITNESS_ALL140_EXPECTED:
        raise ValueError("V6 witness coordinate hash moved")

    wall = repo / "stages/stage32/residual-32-01-production/post1473-specific-class-kc-adapter-wall.md"
    if base.git_blob_sha1(wall) != base.KC_WALL_GIT_BLOB_SHA1:
        raise ValueError("K_c theorem wall moved")
    wall_text = wall.read_text()
    for phrase in ("pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E", "(pi_*C)^2 = P^2 / 2", "(pi_*C)^2 >= 0", "degree `186/2=93`", "Lemma 12's even-degree condition"):
        if phrase not in wall_text:
            raise ValueError(f"K_c theorem-wall semantic lock moved: {phrase}")

    bundle = base.load_module(repo / "stages/stage33/33-07/picard_base_rows_retained.py", "stage32_kc_retained_picard").load()
    gram_rows = [[int(v) for v in row] for row in bundle["picard_gram_64x64"]]
    gram = Matrix(gram_rows)
    endpoint = json.loads((repo / "stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json").read_text())
    locks = endpoint.get("source_locks", {})
    if endpoint.get("canonical_sha256") != ENDPOINT_EXPECTED:
        raise ValueError("retained geometric-sign endpoint canonical lock moved")
    if endpoint.get("coordinate_order") != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
        raise ValueError("retained geometric-sign coordinate order moved")
    if locks.get("picard_sign_rows_sha256", {}).get("c") != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError("retained c-sign Picard64 hash moved")
    if locks.get("picard_gram_rows_sha256") != PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("retained Picard Gram hash moved")

    mat = pinned_picard_materialization(repo, gram_rows)
    if mat["sigma_exceptional_permutation_1based"] != geo["sigma_exceptional_1based"]:
        raise ValueError("pinned Magma c-sign permutation disagrees with direct node replay")
    sigma = Matrix(mat["sigma_rows"])
    exc = [Matrix(row) for row in mat["exceptional_rows"]]
    C = Matrix(x)
    if int((C.T * gram * C)[0, 0]) != 758:
        raise ValueError("V6 C^2 regression")
    for j, E in enumerate(exc):
        if int((E.T * gram * E)[0, 0]) != -2:
            raise ValueError(f"exceptional {j} ceased to be -2")
        if sigma.T * E != exc[geo["sigma_exceptional_0based"][j]]:
            raise ValueError(f"Picard64 c-sign convention mismatch on exceptional {j}")
        if int((C.T * gram * E)[0, 0]) != p[92 + j]:
            raise ValueError(f"V6 all140 exceptional pairing mismatch at {j}")

    sigmaC = sigma.T * C
    if sigma.T * sigmaC != C or int((sigmaC.T * gram * sigmaC)[0, 0]) != 758:
        raise ValueError("full integral sigma_c Picard64 isometry replay failed")
    correction = Matrix.zeros(64, 1)
    terms = []
    for j in geo["E_pi_indices_0based"]:
        E = exc[j]
        ce = int((C.T * gram * E)[0, 0])
        correction += ce * E
        terms.append({"exceptional_id": f"EXC_{j+1:03d}", "C_dot_E": ce, "picard_coordinates_sha256": base.csha(base.matrix_vector(E))})
    P = C + sigmaC + correction
    P2 = int((P.T * gram * P)[0, 0])
    if P2 % 2:
        raise ValueError(f"Lemma11 P^2 not divisible by 2: {P2}")
    push2 = P2 // 2
    if push2 % 2:
        raise ValueError(f"K3 square is not even: {push2}")
    negative = push2 < 0
    result = {
        "formula": "P=C+sigma_c(C)+sum_{E in E_pi}(C.E)E=pi^*pi_*C; (pi_*C)^2=P^2/2",
        "source_locks": {
            "v6_witness_canonical_sha256": wc,
            "v6_picard_coordinates_sha256": base.WITNESS_PICARD_EXPECTED,
            "v6_all140_pairings_sha256": base.WITNESS_ALL140_EXPECTED,
            "kc_wall_git_blob_sha1": base.KC_WALL_GIT_BLOB_SHA1,
            "retained_picard_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_geometric_sign_endpoint_canonical_sha256": ENDPOINT_EXPECTED,
            "testa_stoll_git_blob_sha1": mat["testa_stoll_git_blob_sha1"],
            "sigma_c_picard64_rows_sha256": mat["sigma_rows_sha256"],
            "picard_gram_rows_sha256": mat["gram_rows_sha256"],
            "exceptional_picard64_rows_sha256": mat["exceptional_rows_sha256"],
            "submitted_magma_code_sha256": mat["submitted_code_sha256"],
        },
        "materialization": {"source_fetch_attempt": mat["source_fetch_attempt"], "magma_request_attempt": mat["magma_request_attempt"]},
        "C_square": 758,
        "sigma_C_square": int((sigmaC.T * gram * sigmaC)[0, 0]),
        "C_dot_sigma_C": int((C.T * gram * sigmaC)[0, 0]),
        "class_sigma_c_invariant": bool(sigmaC == C),
        "sigma_C_picard_coordinates": base.matrix_vector(sigmaC),
        "sigma_C_picard_coordinates_sha256": base.csha(base.matrix_vector(sigmaC)),
        "E_pi_count": len(geo["E_pi_indices_0based"]),
        "E_pi_correction_terms": terms,
        "E_pi_correction_picard_coordinates": base.matrix_vector(correction),
        "E_pi_correction_square": int((correction.T * gram * correction)[0, 0]),
        "P_picard_coordinates": base.matrix_vector(P),
        "P_picard_coordinates_sha256": base.csha(base.matrix_vector(P)),
        "P_square": P2,
        "pi_pushforward_C_square": push2,
        "noninvariant_integral_genus1_carrier_excluded_by_negative_square": negative,
        "invariant_curve_case_source_locked_even_degree_obstruction": True,
        "invariant_curve_image_degree": 93,
        "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies": negative,
        "scope": "SINGLE_V6_SUPPORT47_CLASS_ONLY",
    }
    result["canonical_sha256_without_this_field"] = base.csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tangent", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    tangent = json.loads(args.tangent.read_text())
    marking = base.load_module(args.marking, "stage32_kc_marking").load()
    geo = geometry(tangent, marking)
    repo = Path(__file__).resolve().parents[3]
    kc = pushforward(repo, geo)
    cert = {
        "schema": "STAGE32_POST1473_KC_PINNED_REPLAY_V6",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EPI_KC_PUSHFORWARD_REPLAY",
        "geometry": geo,
        "kc_pushforward_replay": kc,
        "three_required_locks": {
            "full_integral_picard64_sigma_c_locked": True,
            "E_pi_exactly_extracted_from_c_zero_nodes": True,
            "lemma11_P_square_over_2_exactly_replayed": True,
        },
        "firewalls": {
            "full178_closed": False,
            "general_low_genus_classification_closed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = base.csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "E_pi_count": kc["E_pi_count"],
        "sigma_c_picard64_sha256": kc["source_locks"]["sigma_c_picard64_rows_sha256"],
        "class_sigma_c_invariant": kc["class_sigma_c_invariant"],
        "P_square": kc["P_square"],
        "pi_pushforward_C_square": kc["pi_pushforward_C_square"],
        "specific_class_genus1_excluded": kc["specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
