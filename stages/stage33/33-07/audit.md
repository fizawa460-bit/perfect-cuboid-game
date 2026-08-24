# Stage33-07 hostile audit

## Verdict

```text
PASS_AFTER_J2_PROPER_TRANSCENDENTAL_ENDPOINT_SURVIVAL_AND_EXACT_BR0B_BR0G_GLOBAL_INTEGRATION
```

PR: `#1370`

Audited functional head:

```text
5f469907c125cdabd96c9084fd107fc79d57b6ad
```

Authoritative current-head production evidence:

```text
workflow_run=32730159528
workflow_run_number=22
workflow_conclusion=success
artifact_id=9521076746
artifact_zip_sha256=c9de08cff9ce04b0bfe1fd216e176996437d44fa7c841673f037400ad8e47dca
```

The hostile audit independently downloaded the current-head artifact ZIP and reproduced its GitHub SHA256. Every JSON certificate in that artifact was independently canonical-rehashed and matched its stored certificate hash.

## 1. J2 survives the endpoint and is not constant

Stage33-05 had already audited the exact Q-relevant K3 survivor space as one-dimensional with basis `J2`. Stage33-07 now crosses the previously open endpoint-survival boundary.

For the audited ruled chart

```text
w^2 = t^2(1-s^2)^2 + s^2(1-t^2)^2,
e=(1-t^2)(1-s^2),
x=2t(1-s^2),
y=2s(1-t^2),
c^2=e^2+x^2+y^2=e^2+4w^2,
```

the point `(t,s)=(2,3)` has

```text
w^2=337,
c^2=1924=4*481.
```

Both are squares in `Q_2`: the relevant odd units are `1 mod 8`. The specialized Stage33-05 arithmetic representative is exactly

```text
L=Q(alpha), alpha^4+alpha^2/4+1=0,
ell_J2=-(16*alpha^2+8)/3,
second slot=3-alpha.
```

The Stage33-05 formula was independently respecialized at `t=2`; both the quartic and `ell_J2` agree exactly with the Stage33-07 probe.

Magma factors `2` into two primes of `L` and returns local Hilbert symbols

```text
[-1,1]
```

so the corestriction invariant is `1/2`. A zero endpoint pullback would evaluate trivially at every local endpoint point; this witness therefore certifies that the endpoint pullback of `J2` is nonzero.

The independent seven-point `Q_2` scan at `t=2`, `s=3,5,7,8,9,11,13` first verifies the K3 and endpoint square conditions exactly, then evaluates the same class. It realizes both

```text
inv_2(J2)=1/2  (for example s=3)
inv_2(J2)=0    (s=8)
```

and therefore certifies nonconstant evaluation on the tested genuine endpoint `Q_2` locus. In particular, the endpoint class is nonzero modulo `Br(Q)`.

This is local evidence only. It does not certify a Brauer--Manin obstruction or endpoint emptiness.

## 2. Proper extension and transcendental separation of J2

The coordinate-sign quotient gives a Q-defined rational map from the smooth proper cuboid surface `S` to the proper K3 resolution `K_c`.

At each prime divisor of regular `S`, the local ring is a DVR. Properness of `K_c` extends the rational map over that DVR, so the pullback of the unramified class `J2 in Br(K_c)` has zero residue at every codimension-one valuation of `S`. Purity therefore places the pullback in `Br(S)`.

The primary Testa--Stoll source was independently checked. Theorem 10 states that the algebraic part of `Br(S)` is exactly the image of `Br(Q)`; its proof identifies the quotient with `H^1(Q,Pic(Sbar))` and computes that group to be zero. Since the Stage33-07 `Q_2` scan proves that endpoint `J2` is not constant, its proper pullback is transcendental.

Consequences accepted exactly:

```text
J2 endpoint pullback nonzero = true
J2 proper/unramified = true
J2 nonconstant modulo Br(Q) = true
J2 proper-transcendental = true
J2 exact order = 2
```

Hence `J2` is independent from the algebraic constant-character block and from every nonzero boundary-residue class. Stage33-06 independently gives zero seven-line endpoint survival, so there is no line9 duplicate.

## 3. Full BR0B injection and duplicate accounting

For `U=S-D`, the compactification triangle yields the exact segment

```text
H^1(Q,Pic(Sbar))
  -> H^2(Q,UPic(Ubar))
  -> H^2(Q,Div_D(Sbar)).
```

Using the independently verified Testa--Stoll vanishing `H^1(Q,Pic(Sbar))=0`, the full BR0B boundary map is injective. This closes the possible hidden kernel not covered merely by the explicit left-filtration coordinate calculation.

The Stage33-04 boundary permutation lattice has exactly 48 Q-orbits and 12 Q(i)-orbits. Shapiro therefore gives the all-primary constant-character block

```text
Hom_cont(G_Q,Q/Z)^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)^12.
```

BR0B is counted exactly once as its distinguished injective image in this block. Its Stage33-03 internal nonsplit filtration is preserved; no splitting is promoted by Stage33-07.

Accepted:

```text
full BR0B boundary map injective = true
BR0B/BR0G constant-block overlap exact = true
trivial algebraic duplicate quotient exact = true
```

## 4. BR0G finite ramified presentation

The audit independently checked the reconstructed finite residue presentation:

```text
unit-symbol rank F2 = 44
graph residual rank F2 = 17
combined exponent-two rank F2 = 61
order-four generators = 12
rank of order-four doubles = 12
projection of doubles to R17 rank = 3
intersection of doubles with U44 rank = 9
```

The exact 73-generator relation matrix has Smith nonzero invariant factors

```text
1^12, 2^49, 4^12,
```

hence the finite ramified boundary residue group is exactly

```text
(Z/2)^49 direct_sum (Z/4)^12.
```

The diagnostic quotient by `U44`, `(Z/2)^23 direct_sum (Z/4)^3`, is not promoted to the final class group.

## 5. Global finite-coefficient lift and no hidden order-8 extension

The theorem-level lift step was checked against its cited sources.

Panin--Zainoulline/Bloch--Ogus gives exact Gersten-type complexes for finite etale coefficients of order prime to the characteristic on the smooth characteristic-zero surface. Gille--Szamuely Theorem 6.9.1 gives the finite-coefficient Faddeev sequence on each rational boundary normalization. Kummer identifies the relevant finite-coefficient cohomology with torsion Brauer lifts modulo Picard terms.

For an invariant residue generator of exact order `n=2` or `4`, finite-coefficient exactness supplies a lift killed by `n`; because its residue already has exact order `n`, the lift itself has exact order `n`. Choosing such lifts for an invariant-factor basis gives a noncanonical section of the finite ramified quotient. Thus no hidden order-8 extension is created by this integration.

Adding the independent proper `J2 ~= Z/2` gives the exact finite nonconstant two-primary block

```text
(Z/2)^50 direct_sum (Z/4)^12.
```

The audit independently recomputed the Smith form of the augmented 74x74 relation matrix and obtained exactly 50 factors of order 2 and 12 of order 4 (plus 12 unit Smith factors). The 74x120 mixed-modulus relation/symbol compatibility was also independently checked.

## 6. Complete Stage33 frozen-scope inventory

After exact duplicate removal, the Stage33 frozen relevant Q-defined inventory is accepted as

```text
odd-primary constant-character block:
  Hom_cont(G_Q,Q/Z)_odd^48
    direct_sum
  Hom_cont(G_Q(i),Q/Z)_odd^12

two-primary constant-character block:
  Hom_cont(G_Q,Q_2/Z_2)^48
    direct_sum
  Hom_cont(G_Q(i),Q_2/Z_2)^12

finite nonconstant two-primary block:
  (Z/2)^50 direct_sum (Z/4)^12

seven-line endpoint block:
  0
```

The finite block consists of `(Z/2)^49 direct_sum (Z/4)^12` from BR0G ramified classes plus the independent proper K3 `J2 ~= Z/2`.

NF-PHYS2 and CAMP4 remain hypothesis-gated and are not invoked for credit.

## 7. Closure and firewall

All fourteen Stage33-07 closure conditions are accepted after hostile audit.

```text
BR2A=DISCHARGED
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
CLOSURE_CRITERIA=14/14
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
STAGE33_PROGRESS=7/11
STAGE33_08_RELEASED=true
```

This result is materially stronger than merely finding a surviving Brauer class: `J2` already has certified nonconstant evaluation at `Q_2`. It is nevertheless only the A->B portion of the obstruction chain.

```text
A. nontrivial Q-defined endpoint class          DONE for J2
B. nonconstant local evaluation                 DONE at Q_2 for J2
C. global reciprocity excludes all physical
   adelic candidates                            NOT DONE
```

Therefore:

```text
BRAUER_MANIN_SET_EMPTY_NOT_PROVED=true
ENDPOINT_EMPTY_NOT_PROVED=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage33-08 may be released. It must materialize evaluable representatives for the complete inventory without treating the present `Q_2` preview as the Stage33-10 full local-evaluation computation.
