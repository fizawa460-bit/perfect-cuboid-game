# Stage13-13fp — R07 repair plan

> STATUS: `R07_REQUIRED_BY_R06_DEEPSEEK_REVIEW`
>
> SOURCE_REVIEW_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R06`
>
> R06_IMMUTABLE: `true`

R06 remains byte-for-byte immutable. This plan records the accepted repair obligations after adjudicating the DeepSeek zero-base review.

## Gate R07-A — fixed finite Hecke/ray-class twist contract

For the exact finite residue-character family used in the fixed-`S` expansion:

1. list the finite-order characters `omega` actually needed;
2. identify `Xi_{2 ell} * omega` as a Hecke/ray-class character over `Q(i)`;
3. prove its finite conductor is independent of `B` and belongs to a finite set;
4. prove its infinity type remains nonzero for every retained `ell>=1`;
5. attach the exact continuation/functional-equation theorem to this family;
6. derive holomorphy at `s=1` and fixed-strip polynomial growth;
7. choose common exponents over the finite twist family.

```text
R07_FIXED_TWIST_FAMILY_EXPLICIT=true
R07_FIXED_TWIST_PRIMARY_CONTRACT_VERIFIED=true
R07_TWIST_CONDUCTOR_INDEPENDENT_OF_B=true
R07_TWIST_INFINITY_TYPE_NONZERO_FOR_ELL_GE_1=true
R07_COMMON_STRIP_GROWTH_EXPONENTS_EXIST=true
```

## Gate R07-B — concrete fixed-S residue and pole-signature model

Replace schema-only `G_{p,nu}` / `Omega_{p,nu}` notation by an explicit finite model for every inert valuation stratum `U`, `R_b`, `S_c`.

The proof must:

1. write the actual residue coordinates and congruence constraints inherited from `P=hrs`, `z=h(s^2-r^2)/2`, `d=h(r^2+s^2)/2` and the two Pythagorean equations;
2. define the ambient finite abelian group and constrained subset explicitly;
3. compute the accepted-state indicator and its finite character expansion;
4. prove the effective-character quotient is compatible with the weighted coefficient system;
5. define the five induced pole-slot characters from that coefficient system and prove the reduced signature is representative-independent;
6. evaluate the principal-residue functional in the same coordinates and recover exactly `lambda_p=(p+5)/(2(p+1))`;
7. prove CRT factorization gives `product_{p in S} lambda_p`;
8. prove every class outside the kernel loses at least one pole slot.

Once every nonprincipal summand has lower pole order, explicitly note that a finite sum cannot create a higher-order pole absent from every summand.

```text
R07_ACTUAL_RESIDUE_COORDINATES_EXPLICIT=true
R07_EFFECTIVE_QUOTIENT_WELL_DEFINED=true
R07_REDUCED_POLE_SIGNATURE_WELL_DEFINED=true
R07_PRINCIPAL_RESIDUE_RATIO_COMPUTED_IN_SAME_MODEL=true
R07_NONPRINCIPAL_TERM_WISE_POLE_LOSS=true
```

## Gate R07-C — curved-region self-contained closure

Promote the complete curved-region proof into the R07 review target. Either inline it in the canonical proof or embed the full audited lemma as a mandatory bundle source.

Expose:

- the multiplicative box decomposition and `O(log(2B)/eta)=O((log B)^9)` intervals per coordinate;
- why the rectangle/Perron remainder is uniform on every core box;
- the sum to `O(B(log B)^-35)` over the crude `O((log B)^27)` box family;
- power tails and their stretched-exponential saving;
- shell/boundary counting and `O(B(log B)^-5)`;
- interior mesh variation and why no extra box factor is inserted;
- the exact route from the one-dimensional Vaaler interval approximants to the angular/curved physical region;
- equality-wall endpoint handling separately from the physical cutoff.

```text
R07_CURVED_REGION_FULL_LEMMA_IN_REVIEW_TARGET=true
R07_PER_BOX_UNIFORMITY_EXPLICIT=true
R07_BOUNDARY_MESH_DERIVATION_EXPLICIT=true
```

## Gate R07-D — exact arithmetic and quantifier hardening

Add the exact inequalities

```text
3465625 < 529*6561 = 3470769
10799919009 < 432*25000000 = 10800000000
```

and explicitly derive retained-`ell` uniform logarithmic moments from the phase-uniform weighted Wiener majorant.

For the overlap squeeze, write the epsilon form:

```text
for epsilon>0 choose k with 2D_q(3/4)^k<epsilon/2;
for this fixed k choose B0(k) so the fixed-S remainder is <epsilon/2;
then B>=B0(k) gives O_qr(B)/(B(log B)^3)<epsilon.
```

Keep the Stage12 projection fiber wording explicitly at the level of oriented distinguished-face records.

## False-positive locks from the R06 review

R07 must not reopen correct arguments merely because they were challenged:

```text
SUM_IQ_ANALYTIC_IDENTITY_REOPEN_REQUIRED=false
FINITE_SUM_CAN_RESTORE_ABSENT_HIGHER_POLE=false
TAGGED_SHARED_EDGE_INJECTION_REOPEN_REQUIRED=false
STAGE12_TWO_ORIENTED_PREIMAGES_REOPEN_REQUIRED=false
```

## R07 synthesis and bundle rule

After R07-A through R07-D close:

1. synthesize a new canonical R07 proof;
2. build a new immutable R07 bundle from a merged fixed snapshot;
3. reset external reviews to zero again;
4. require at least two independent `CLOSED` verdicts and zero unresolved theorem-level objections;
5. only then permit `13-13g` final freeze.

```text
R06_IMMUTABLE=true
R06_PROMOTION_ALLOWED=false
R07_REQUIRED=true
R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fq
```
