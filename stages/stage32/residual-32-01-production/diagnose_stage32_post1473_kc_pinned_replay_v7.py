#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path

from sympy import Matrix

import diagnose_stage32_post1473_kc_pinned_replay as v6

ENDPOINT_EXPECTED = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
SIGMA_C_PICARD_ROWS_EXPECTED = "65f90a3356941bd4bdaeb77cfc3a8c5370d5726e2f66e2eb348bf5f9633af43a"
PICARD_GRAM_ROWS_EXPECTED = "22b1f891116ea16fcb615c95e9a83be9fef76c275d792e638d9ab0dab65a6e3b"
PICARD_BASE_SPARSE_EXPECTED = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"


def lit(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise ValueError(f"missing Magma output {name}")
    return ast.literal_eval(m.group(1))


def compact_materialize(repo: Path, epi0: list[int]) -> dict:
    source = v6.base.load_module(
        repo / "stages/stage33/33-07/stoll_cuboid_source.py",
        "stage32_kc_pinned_stoll_v7",
    )
    _text, core, blob, fetch_attempt = source.load_pinned_source()
    epi1 = [j + 1 for j in epi0]
    epi_literal = "[" + ",".join(str(j) for j in epi1) + "]"
    extra = f'''
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
epi32 := {epi_literal};
assert #epi32 eq 24;
assert &and[perm32[#Cs+j] eq #Cs+j : j in epi32];
printf "STAGE32_KC_COMPACT_BEGIN\\n";
printf "SIGMA_EXC_PERM=%o\\n",[perm32[#Cs+j]-#Cs:j in [1..#pts]];
for r in [1..64] do printf "SIGMA_ROW_%o=%o\\n",r,[sigmaPic32[r,k]:k in [1..64]]; end for;
for j in epi32 do printf "EPI_ROW_%o=%o\\n",j,Eltseq(qPic(Big.(#Cs+j))); end for;
printf "STAGE32_KC_COMPACT_END\\n";
'''
    code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
    stdout, magma_attempt = source.run_magma(code, 240, "Stage32 compact pinned Kc Picard64 replay")
    if "STAGE32_KC_COMPACT_END" not in stdout or any(
        x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
    ):
        print(stdout)
        raise ValueError("compact pinned Kc Picard materialization failed")
    sigma_rows = [[int(x) for x in lit(stdout, f"SIGMA_ROW_{r}")] for r in range(1, 65)]
    if any(len(row) != 64 for row in sigma_rows):
        raise ValueError("sigma_c Picard64 row-width regression")
    sigma_sha = v6.base.csha(sigma_rows)
    if sigma_sha != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError(f"sigma_c Picard64 retained hash mismatch: {sigma_sha}")
    sigma_exc = [int(x) for x in lit(stdout, "SIGMA_EXC_PERM")]
    epi_rows = {
        j - 1: [int(x) for x in lit(stdout, f"EPI_ROW_{j}")]
        for j in epi1
    }
    if any(len(row) != 64 for row in epi_rows.values()):
        raise ValueError("E_pi Picard64 row-width regression")
    return {
        "testa_stoll_git_blob_sha1": blob,
        "source_fetch_attempt": fetch_attempt,
        "magma_request_attempt": magma_attempt,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "sigma_rows": sigma_rows,
        "sigma_rows_sha256": sigma_sha,
        "sigma_exceptional_permutation_1based": sigma_exc,
        "E_pi_rows": epi_rows,
        "E_pi_rows_sha256": v6.base.csha([epi_rows[j] for j in epi0]),
    }


def exact_pushforward(repo: Path, geo: dict) -> dict:
    witness = json.loads(
        (repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json").read_text()
    )
    wb = dict(witness)
    wc = wb.pop("canonical_sha256_without_this_field", None)
    if wc != v6.base.WITNESS_EXPECTED or v6.base.csha(wb) != v6.base.WITNESS_EXPECTED:
        raise ValueError("V6 recovered witness lock moved")
    w = witness["witness"]
    x = [int(a) for a in w["picard_coordinates"]]
    all140 = [int(a) for a in w["all140_pairings"]]
    if v6.base.csha(x) != v6.base.WITNESS_PICARD_EXPECTED:
        raise ValueError("V6 Picard-coordinate hash moved")
    if v6.base.csha(all140) != v6.base.WITNESS_ALL140_EXPECTED:
        raise ValueError("V6 all140-pairing hash moved")

    wall = repo / "stages/stage32/residual-32-01-production/post1473-specific-class-kc-adapter-wall.md"
    if v6.base.git_blob_sha1(wall) != v6.base.KC_WALL_GIT_BLOB_SHA1:
        raise ValueError("K_c theorem wall moved")
    wt = wall.read_text()
    for phrase in (
        "pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E",
        "(pi_*C)^2 = P^2 / 2",
        "(pi_*C)^2 >= 0",
        "degree `186/2=93`",
        "Lemma 12's even-degree condition",
    ):
        if phrase not in wt:
            raise ValueError(f"K_c theorem-wall semantic lock moved: {phrase}")

    bundle = v6.base.load_module(
        repo / "stages/stage33/33-07/picard_base_rows_retained.py",
        "stage32_kc_retained_picard_v7",
    ).load()
    gram_rows = [[int(a) for a in row] for row in bundle["picard_gram_64x64"]]
    if bundle.get("upstream_git_blob_sha1") != "0422b69847f2afb97cb7b3ed02ebef91279f61b1":
        raise ValueError("retained Picard upstream blob lock moved")

    sparse_path = repo / "stages/stage33/33-07/retained-picard-base-sparse.json"
    sparse_bundle = json.loads(sparse_path.read_text())
    sparse_body = dict(sparse_bundle)
    sparse_canonical = sparse_body.pop("canonical_sha256", None)
    if sparse_canonical != PICARD_BASE_SPARSE_EXPECTED or v6.base.csha(sparse_body) != PICARD_BASE_SPARSE_EXPECTED:
        raise ValueError("retained Picard sparse-base canonical lock moved")
    if sparse_bundle.get("schema") != "STAGE33_07_RETAINED_PICARD_BASE_SPARSE_V1":
        raise ValueError("retained Picard sparse-base schema moved")
    gram_object = sparse_bundle.get("objects", {}).get("gram", {})
    if gram_object.get("source_certificate_sha256") != PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("historical Picard Gram source-certificate lock moved")
    sparse_rows = gram_object.get("matrix_64x64_sparse_rows_1based", [])
    if len(sparse_rows) != 64:
        raise ValueError("retained sparse Picard Gram row-count regression")
    sparse_dense = []
    for row in sparse_rows:
        dense_row = [0] * 64
        seen = set()
        for pair in row:
            if not isinstance(pair, list) or len(pair) != 2:
                raise ValueError("retained sparse Picard Gram pair encoding moved")
            j1, value = int(pair[0]), int(pair[1])
            if not 1 <= j1 <= 64 or j1 in seen or value == 0:
                raise ValueError("retained sparse Picard Gram coordinate encoding moved")
            seen.add(j1)
            dense_row[j1 - 1] = value
        sparse_dense.append(dense_row)
    if sparse_dense != gram_rows:
        raise ValueError("retained sparse Picard Gram no longer matches dense retained Gram")
    gram = Matrix(gram_rows)

    endpoint = json.loads(
        (repo / "stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json").read_text()
    )
    locks = endpoint.get("source_locks", {})
    if endpoint.get("canonical_sha256") != ENDPOINT_EXPECTED:
        raise ValueError("retained geometric-sign endpoint canonical lock moved")
    if endpoint.get("coordinate_order") != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
        raise ValueError("retained geometric-sign coordinate order moved")
    if locks.get("picard_sign_rows_sha256", {}).get("c") != SIGMA_C_PICARD_ROWS_EXPECTED:
        raise ValueError("retained c-sign Picard64 hash moved")
    if locks.get("picard_gram_rows_sha256") != PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("retained endpoint Picard Gram hash moved")

    epi = [int(j) for j in geo["E_pi_indices_0based"]]
    mat = compact_materialize(repo, epi)
    if mat["testa_stoll_git_blob_sha1"] != locks.get("testa_stoll_git_blob_sha1"):
        raise ValueError("fresh pinned Testa-Stoll blob differs from retained endpoint")
    if mat["sigma_exceptional_permutation_1based"] != geo["sigma_exceptional_1based"]:
        raise ValueError("pinned Magma c-sign permutation disagrees with direct node replay")

    sigma = Matrix(mat["sigma_rows"])
    C = Matrix(x)
    C2 = int((C.T * gram * C)[0, 0])
    if C2 != 758 or int(w["self_intersection"]) != 758:
        raise ValueError(f"V6 C^2 regression: {C2}")
    sigmaC = sigma.T * C
    if sigma.T * sigmaC != C:
        raise ValueError("sigma_c Picard64 failed involution on V6 class")
    sigmaC2 = int((sigmaC.T * gram * sigmaC)[0, 0])
    if sigmaC2 != C2:
        raise ValueError("sigma_c Picard64 failed isometry on V6 class")

    correction = Matrix.zeros(64, 1)
    terms = []
    for j in epi:
        E = Matrix(mat["E_pi_rows"][j])
        if int((E.T * gram * E)[0, 0]) != -2:
            raise ValueError(f"E_pi exceptional {j} ceased to be a (-2)-class")
        if sigma.T * E != E:
            raise ValueError(f"E_pi exceptional {j} not fixed by full Picard64 sigma_c")
        ce = int((C.T * gram * E)[0, 0])
        if ce != all140[92 + j]:
            raise ValueError(
                f"V6/Testa-Stoll exceptional pairing convention mismatch at {j}: {ce} vs {all140[92+j]}"
            )
        correction += ce * E
        terms.append(
            {
                "exceptional_index_0based": j,
                "exceptional_id": f"EXC_{j+1:03d}",
                "C_dot_E": ce,
                "picard_coordinates_sha256": v6.base.csha(v6.base.matrix_vector(E)),
            }
        )

    P = C + sigmaC + correction
    P2 = int((P.T * gram * P)[0, 0])
    if P2 % 2:
        raise ValueError(f"Lemma11 P^2 not divisible by quotient degree 2: {P2}")
    push2 = P2 // 2
    if push2 % 2:
        raise ValueError(f"K3 pushforward square is not even: {push2}")
    negative = push2 < 0

    result = {
        "mode": "EXACT_COMPACT_PINNED_TESTA_STOLL_SIGMA_C_LEMMA11_SINGLE_V6_CLASS_REPLAY",
        "formula": "P=C+sigma_c(C)+sum_{E in E_pi}(C.E)E=pi^*pi_*C; (pi_*C)^2=P^2/2",
        "source_locks": {
            "v6_witness_canonical_sha256": wc,
            "v6_picard_coordinates_sha256": v6.base.WITNESS_PICARD_EXPECTED,
            "v6_all140_pairings_sha256": v6.base.WITNESS_ALL140_EXPECTED,
            "kc_wall_git_blob_sha1": v6.base.KC_WALL_GIT_BLOB_SHA1,
            "retained_picard_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_picard_base_sparse_canonical_sha256": sparse_canonical,
            "retained_geometric_sign_endpoint_canonical_sha256": ENDPOINT_EXPECTED,
            "testa_stoll_git_blob_sha1": mat["testa_stoll_git_blob_sha1"],
            "sigma_c_picard64_rows_sha256": mat["sigma_rows_sha256"],
            "picard_gram_rows_sha256": PICARD_GRAM_ROWS_EXPECTED,
            "E_pi_picard64_rows_sha256": mat["E_pi_rows_sha256"],
            "submitted_magma_code_sha256": mat["submitted_code_sha256"],
        },
        "materialization": {
            "source_fetch_attempt": mat["source_fetch_attempt"],
            "magma_request_attempt": mat["magma_request_attempt"],
            "picard_gram_historical_certificate_matches_sparse_retained_source": True,
            "picard_gram_sparse_retained_matches_dense_retained": True,
            "sigma_c_picard64_matches_retained_sha256": True,
            "sigma_c_exceptional_permutation_matches_direct_node_replay": True,
            "all_24_E_pi_classes_are_minus2_and_sigma_c_fixed": True,
            "all_24_E_pi_pairings_match_recovered_V6_all140": True,
        },
        "C_square": C2,
        "sigma_C_square": sigmaC2,
        "C_dot_sigma_C": int((C.T * gram * sigmaC)[0, 0]),
        "class_sigma_c_invariant": bool(sigmaC == C),
        "sigma_C_picard_coordinates": v6.base.matrix_vector(sigmaC),
        "sigma_C_picard_coordinates_sha256": v6.base.csha(v6.base.matrix_vector(sigmaC)),
        "E_pi_count": len(epi),
        "E_pi_exceptional_indices_0based": epi,
        "E_pi_exceptional_ids": geo["E_pi_ids"],
        "E_pi_correction_terms": terms,
        "E_pi_correction_picard_coordinates": v6.base.matrix_vector(correction),
        "E_pi_correction_picard_coordinates_sha256": v6.base.csha(v6.base.matrix_vector(correction)),
        "E_pi_correction_square": int((correction.T * gram * correction)[0, 0]),
        "C_plus_sigma_C_dot_E_pi_correction": int(((C + sigmaC).T * gram * correction)[0, 0]),
        "P_picard_coordinates": v6.base.matrix_vector(P),
        "P_picard_coordinates_sha256": v6.base.csha(v6.base.matrix_vector(P)),
        "P_square": P2,
        "pi_pushforward_C_square": push2,
        "noninvariant_integral_genus1_carrier_necessary_condition": "(pi_*C)^2>=0",
        "noninvariant_integral_genus1_carrier_excluded_by_negative_square": negative,
        "invariant_curve_case_source_locked_even_degree_obstruction": True,
        "invariant_curve_image_degree": 93,
        "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies": negative,
        "scope": "SINGLE_V6_SUPPORT47_CLASS_ONLY",
    }
    result["canonical_sha256_without_this_field"] = v6.base.csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tangent", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    tangent = json.loads(args.tangent.read_text())
    marking = v6.base.load_module(args.marking, "stage32_kc_marking_v7").load()
    geo = v6.geometry(tangent, marking)
    repo = Path(__file__).resolve().parents[3]
    kc = exact_pushforward(repo, geo)
    cert = {
        "schema": "STAGE32_POST1473_KC_PINNED_REPLAY_V7",
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
    cert["canonical_sha256_without_this_field"] = v6.base.csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "success": True,
                "E_pi_count": kc["E_pi_count"],
                "sigma_c_picard64_sha256": kc["source_locks"]["sigma_c_picard64_rows_sha256"],
                "class_sigma_c_invariant": kc["class_sigma_c_invariant"],
                "P_square": kc["P_square"],
                "pi_pushforward_C_square": kc["pi_pushforward_C_square"],
                "specific_class_genus1_excluded": kc[
                    "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies"
                ],
                "canonical_sha256": cert["canonical_sha256_without_this_field"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
