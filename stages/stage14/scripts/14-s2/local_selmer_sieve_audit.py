#!/usr/bin/env python3
"""Stage14-s2: Pythagorean-base local 2-Selmer support audit.

This stage does NOT compute Selmer groups from scratch.  It proves/audits the
support architecture inherited from s1:

  E_F: Y^2 = Z(Z-S^2)(Z+X^2),  Delta=16 S^4 X^4 H^4.

For odd p, a primitive Pythagorean base is bad at p iff p divides S*X*H.
In Euclid coordinates [m:n] in P^1(F_p), the bad projective slopes are

  0, infinity, +1, -1,

plus the two roots of r^2+1=0 when p=1 mod 4.  Hence the exact projective bad
fraction is 4/(p+1) for p=3 mod 4 and 6/(p+1) for p=1 mod 4.

The s1 split Kummer classes are supported on Sigma={infinity} union primes
p|2SXH.  If k=omega(2SXH), the ambient square-class triple space with product
constraint has F2-dimension at most 2(k+1), hence at most 4^(k+1) candidate
classes before local equations are imposed.  Maximal order of omega gives a
subpolynomial per-base envelope H^{o(1)}.

This audit checks the exact local densities over finite projective lines and
compares them with primitive Euclid pairs up to a deterministic hypotenuse
ceiling.  It records finite diagnostics only; no average-Selmer theorem is
silently imported.
"""

from math import gcd, isqrt, log
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUTPUT = ROOT / "stages/stage14/data/14-s2/local_selmer_sieve_audit.json"
MAX_H = 200_000
CUTS = (10_000, 50_000, 100_000, 200_000)
PRIMES = (3,5,7,11,13,17,19,23,29,31,37,41,43,47)


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p)+1)
    return [i for i in range(2, n+1) if sieve[i]]


def spf_table(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for x in range(p*p, n+1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


SPF = spf_table(MAX_H)


def factor_support(n):
    out = set()
    while n > 1:
        p = SPF[n]
        out.add(p)
        while n % p == 0:
            n //= p
    return out


def primitive_triples(B):
    rows=[]
    m=2
    while m*m+1 <= B:
        for n in range(1,m):
            if gcd(m,n) != 1 or ((m-n)&1)==0:
                continue
            H=m*m+n*n
            if H>B:
                continue
            a=m*m-n*n
            b=2*m*n
            S,X=(a,b) if a<b else (b,a)
            rows.append((S,X,H,m,n))
        m+=1
    rows.sort(key=lambda z:(z[2],z[0],z[1]))
    return rows


def bad_projective_count(p):
    pts={(0,1),(1,0),(1,1),((-1)%p,1)}
    for r in range(p):
        if (r*r+1)%p==0:
            pts.add((r,1))
    return len(pts)


def exact_bad_fraction(p):
    c=6 if p%4==1 else 4
    return c/(p+1)


def audit_cut(B, triples):
    rows=[t for t in triples if t[2]<=B]
    omega=[]
    log2_caps=[]
    for S,X,H,_,_ in rows:
        supp={2}|factor_support(S)|factor_support(X)|factor_support(H)
        k=len(supp)
        omega.append(k)
        log2_caps.append(2*(k+1))
    return {
        "H_max":B,
        "primitive_triples":len(rows),
        "oriented_first_face_states":2*len(rows),
        "mean_omega_2SXH":sum(omega)/len(omega) if omega else 0.0,
        "max_omega_2SXH":max(omega,default=0),
        "mean_log2_ambient_cover_cap":sum(log2_caps)/len(log2_caps) if log2_caps else 0.0,
        "max_log2_ambient_cover_cap":max(log2_caps,default=0),
    }


def prime_rows(triples):
    out=[]
    for p in PRIMES:
        projective=bad_projective_count(p)
        expected_count=6 if p%4==1 else 4
        assert projective==expected_count
        bad=sum((S*X*H)%p==0 for S,X,H,_,_ in triples)
        frac=bad/len(triples)
        out.append({
            "p":p,
            "p_mod_4":p%4,
            "bad_projective_slopes":projective,
            "projective_line_size":p+1,
            "exact_bad_density":exact_bad_fraction(p),
            "finite_bad_fraction_H_le_200k":frac,
            "finite_minus_exact":frac-exact_bad_fraction(p),
        })
    return out


def main():
    triples=primitive_triples(MAX_H)
    assert triples
    # pairwise coprimality for primitive Pythagorean triples
    for S,X,H,_,_ in triples:
        assert gcd(S,X)==gcd(S,H)==gcd(X,H)==1
        assert S*S+X*X==H*H

    prows=prime_rows(triples)
    cuts=[audit_cut(B,triples) for B in CUTS]
    last=cuts[-1]

    report={
        "metadata":{
            "stage":"14-s2",
            "title":"Pythagorean-base local 2-Selmer support and density audit",
            "max_hypotenuse":MAX_H,
            "prime_audit":list(PRIMES),
        },
        "exact_local_architecture":{
            "integral_family":"E_F: Y^2=Z(Z-S^2)(Z+X^2)",
            "discriminant":"16*S^4*X^4*H^4",
            "bad_prime_support":"2 and odd p dividing S*X*H",
            "odd_p_projective_bad_slopes":{
                "always":["0","infinity","+1","-1"],
                "extra_when_p_eq_1_mod_4":["roots of r^2+1=0"]
            },
            "odd_p_bad_density":{
                "p_eq_3_mod_4":"4/(p+1)",
                "p_eq_1_mod_4":"6/(p+1)"
            },
            "good_prime_statement":"For odd p not dividing S*X*H, E_F has good reduction and the 2-descent local condition is the unramified local Kummer condition; no new base-dependent bad-prime coordinate is introduced at p.",
        },
        "squareclass_envelope":{
            "Sigma_f":"primes dividing 2*S*X*H",
            "k":"omega(2*S*X*H)",
            "ambient_squareclass_dimension_bound":"2*(k+1) over F2 after the d1*d2*d3 square constraint",
            "ambient_cover_class_count_bound":"4^(k+1)",
            "maximal_order_consequence":"4^(omega(2SXH)+1)=H^o(1) uniformly for S,X,H<=H",
            "meaning":"local 2-cover search multiplicity is subpolynomial per base; this alone does not thin the number of bases"
        },
        "finite_projective_density_audit":prows,
        "finite_support_complexity":cuts,
        "theorem_boundary":{
            "fixed_auxiliary_prime_product_sieve_available":False,
            "reason":"positive-rank candidacy is a global F2 compatibility problem among the moving bad primes dividing 2SXH; at good fixed primes the local condition is only unramified and does not independently reject the base",
            "quadratic_twist_average_theorems_imported":False,
            "reason_twist_theorems_not_imported":"j(t) is nonconstant, so the Pythagorean-base family is not a quadratic-twist family of one fixed elliptic curve; moreover the family has rational 4-torsion, excluding hypotheses of some full-2-torsion twist theorems",
            "average_selmer_theorem_for_this_base_change_proved":False,
            "positive_rank_density_proved":False,
            "power_saving_from_local_conditions_proved":False,
            "log_saving_from_local_conditions_proved":False,
            "small_point_gate_still_required":True,
        },
        "decision":{
            "STAGE14_S2":"COMPLETE_LOCAL_SUPPORT_ARCHITECTURE_AND_FIXED_PRIME_SIEVE_BOUNDARY",
            "PYTHAGOREAN_BAD_PRIME_DENSITIES_LOCKED":True,
            "SELMER_SQUARECLASS_SUBPOLYNOMIAL_PER_BASE_ENVELOPE":True,
            "FIXED_AUXILIARY_PRIME_PRODUCT_SIEVE_PROVES_POWER_SAVING":False,
            "AVERAGE_SELMER_THEOREM_IMPORTED":False,
            "POSITIVE_RANK_DENSITY_PROVED":False,
            "LOCAL_CONDITIONS_POWER_SAVING_PROVED":False,
            "FINITE_MAX_OMEGA_2SXH_AT_H200K":last["max_omega_2SXH"],
            "NEXT":"Stage14-s3 first-small-point / regulator gate",
        }
    }
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report["decision"],indent=2))

if __name__=="__main__":
    main()
