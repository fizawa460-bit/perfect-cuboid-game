# Stage33-05 source lock — Creutz--Viray presentation and arithmetic descent

## Post-R5 authoritative correction

The historical Q-defined `ell_J2` / corestriction-CSA witness from `j2_arithmetic_descent.py` is **revoked as a witness for the named nonzero J2**.  The exact regression

```text
stages/stage33/33-12/j2-cv-lclass-zero-regression.json
```

proves that its geometric Creutz--Viray class is zero.  It must not be reused to certify corrected J2.

The corrected nonzero geometric class is the full branch-algebra pair

```text
J2 = (f2,1),
f2=(t+1+sqrt(2))/(t-1+sqrt(2)),
```

certified in `j2-corrected-full-l-representative.json`, with exact E[2] cocycle `xi(rho)=Tr` in `j2-corrected-cv-e2-cocycle.json` and marked Brauer coordinate `[1,0]` after the R4 hostile integral-kernel verification.

The post-R5 arithmetic repair no longer relies on a replacement closed-form Q quaternion.  Instead

```text
stages/stage33/33-05/j2-post-r5-hs-descent-datum.json
stages/stage33/33-05/certify_j2_post_r5_q_descent_cocycle.py
```

materialize an equivalent Hochschild--Serre/Kummer descent datum.  In the exact full-pair basis `[J1,J2,q1,q2,q3]`, the source-locked actions have `tau(J2)=cc(J2)=ct(J2)=J2`.  Hence the presentation defect of the corrected J2 lift is zero on every Galois generator, the associated Pic/2 Kummer defect is the explicit zero 1-cocycle, and its Bockstein/HS `d2` is the explicit zero Pic-valued 2-cocycle.

For `k=Q`, `H^3(k,kbar^*)=0`.  Standard Hochschild--Serre exactness therefore identifies the kernel of

```text
Br(Kc_bar)^G_Q -> H^2(Q,Pic(Kc_bar))
```

with the image of `Br(Kc_Q)`.  Thus the corrected nonzero J2 has an arithmetic preimage `beta_J2_Q` whose geometric restriction is exactly corrected `(f2,1)`.  Since this class lies in the Brauer group of the smooth projective Q-K3 itself rather than merely its function field, unramifiedness is built into the conclusion.  No generic-function residue claim for the revoked `ell_Q` is inherited.

This is **pre-audit exact evidence only**.  By the repository-wide promotion firewall and the user's workflow rule, authoritative Q-descent credit and Stage33-05 reclosure remain forbidden until a separate super-hostile audit passes.

## Primary ruled-surface source

- Brendan Creutz, Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, arXiv:1306.3251, Math. Ann. 362 (2015), 1169--1200.
- Load-bearing locators: Theorem 2.5 (`Pic C/2 -> L_c -> Br C[2] -> 0`, Galois-equivariant); §3, Proposition 3.1 / Corollary 3.2 (vertical residue tests); Proposition 3.4 (exceptional curves over simple branch singularities); Theorem I and Theorem 5.2 / Corollary 5.4 (surface presentation and NS relations).

Stage33 uses this source in the exact direction

```text
reduced flat branch with simple singularities on a ruled surface
 -> finite presentation of geometric Br[2]
 -> explicit corestriction quaternion generators
 -> relations from NS(X)
 -> residue criterion for extending generic-fiber classes to the surface
```

For the rational ruled base `W=P1`, the source gives `L_{c,E}=L_E`. At a singular branch point its `e(b/w)` is the sum of ramification indices over normalization points; this is load-bearing for the corrected count of four nodal even-e fibers.

## Hyperelliptic cocycle / Hochschild--Serre compatibility source

- Brendan Creutz, Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, arXiv:1403.2924, Manuscripta Math. 147 (2015), 139--167.
- Remark 3.1: the exact Brauer-to-`H^1(Pic)` construction is the one coming from the étale Hochschild--Serre spectral sequence, up to sign.
- Proposition 3.2: gives the explicit Picard-valued Galois cocycle associated to the corestriction construction and identifies its class with the spectral-sequence map.
- Lemma 3.4: lifts the Picard cocycle to divisors and computes its coboundary explicitly as the divisor of the norm of `(x-alpha)` with the corresponding cochain exponent.
- Lemma 3.5: identifies the resulting function-field 2-cocycle with the corestriction quaternion algebra by cup product and Shapiro.

These locators are used for compatibility of the explicit Creutz--Viray presentation with the standard étale/Kummer cochain construction.  The q1 Bockstein and corrected-J2 zero-defect Bockstein are recomputed exactly in repository scripts.

## Hochschild--Serre arithmetic descent source

- Alexei N. Skorobogatov, Yuri G. Zarhin, *The Brauer group and the Brauer--Manin set of products of varieties*, JEMS 16 (2014), proof of Theorem B around equation (21): when `H^3(k,kbar^*)=0`, standard Hochschild--Serre theory gives

```text
ker(Br(Xbar)^G -> H^2(k,Pic(Xbar))) = image(Br(X) -> Br(Xbar)^G).
```

- Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, Proposition 8.3.11: for a number field `k`, `H^3(k,kbar^*)=0`.
- Harari--Skorobogatov, *The Brauer group of torsors and its arithmetic applications*, also recalls this number-field vanishing and the smooth/proper unramified Brauer interpretation.

## General cohomological source locks

- Stacks Project tag `03PK`, §59.28 Kummer theory, Lemma 59.28.1: for 2 invertible,
  `0 -> mu_2 -> G_m --square--> G_m -> 0` on the étale site, with the associated long exact cohomology sequence.
- Stacks Project tag `03QA` / Proposition 59.54.2: Leray spectral sequence
  `E2^{p,q}=H^p(Y,R^q f_*F) => H^{p+q}(X,F)`.
- Applied to `Xbar` and Kummer, and using torsion-freeness of the K3 Picard lattice, this gives

```text
0 -> Pic(Xbar)/2 -> H^2_et(Xbar,mu_2) -> Br(Xbar)[2] -> 0.
```

For an invariant geometric 2-torsion class, the Galois defect of a `mu_2` lift is a `Pic/2` 1-cocycle.  The `d2^{0,2}` in the `G_m` Hochschild--Serre/Leray spectral sequence is the Bockstein of this defect for

```text
0 -> Pic(Xbar) --2--> Pic(Xbar) -> Pic(Xbar)/2 -> 0.
```

## Frozen geometric application to K_c

The exact dimension checker certifies

```text
B=B+ union B-, genera 1 and 1
h0(B)=2
b1(Gamma)=7
Jac(B)[2] dimension=4
smooth common ramification fibers=4
nodal even-e fibers t=0,1,-1,infinity=4
special even-e fiber count=8
K*/K*2 -> L*/L*2 kernel dimension=1
raw generator subspace mod L*2 dimension=12
kernel to K*L*2 dimension=7
L_E=L_{c,E} dimension=5
x-alpha image dimension=3
Br(K_cbar)[2] dimension=2
```

The old Stage33 pilot `L_{c,E}=9` omitted the nodal fibers and is superseded.

The true exact presentation is materialized in basis `[J1,J2,q1,q2,q3]` with

```text
im(x-alpha)=span_F2{
  J1,
  b*J2+q1+q2,
  d*J2+q1+q2+q3
}, b,d in F2,
```

and geometric quotient basis `[J2,q1]`. The full-pair action is identity on the quotient, so the geometric invariant dimension is two.

## Corrected J2 arithmetic source application

The corrected J2 presentation lift is fixed by every exact action generator:

```text
tau(J2)-J2 = 0
cc(J2)-J2  = 0
ct(J2)-J2  = 0
```

The corresponding normalized cochains are therefore

```text
Pic/2 defect j_sigma = 0,
integral Pic lift J_sigma = 0,
Bockstein/HS d2(sigma,tau) = 0.
```

This gives

```text
HS_D2_CORRECTED_J2=0
CORRECTED_J2_IN_IMAGE_OF_Br_Kc_Q=true
GEOMETRIC_RESTRICTION=corrected nonzero (f2,1)
ARITHMETIC_UNRAMIFIED=true
OLD_ELL_Q_USED=false
```

The concrete Q-class is recorded cohomologically as `beta_J2_Q`, specified by its corrected geometric restriction and the explicit zero HS descent datum.  A new closed-form Q CSA formula is **not** claimed.

## q1 Hochschild--Serre source application

The presentation defect is `ct(q1)-q1=J1`. Stage33 materializes

```text
D=Cb+E_P0,
Cb : i*A1+B1=i*A2+B2=i*A3+B3=0,
P0=[0:1:0:-1:0:1],
```

as an integral `ct`-invariant NS lift of `J1`. The invariant test conic

```text
T : A1=0, A2+B3=0, A3-B2=0
```

has `D.T=1`, proving `D` is not a cyclic norm. The Kummer defect is `D mod 2`; on `C2=<ct>` the normalized integral lift has

```text
(dJ)(ct,ct)=2D,
Bockstein(ct,ct)=D.
```

Therefore the restricted Hochschild--Serre differential is nonzero, and `q1` does not descend.

## Immutable Picard geometry source

- `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`.
- Load-bearing facts: rank-20 Picard lattice generated by known curves, 2-saturation, explicit conic/branch-conic geometry and intersection pairing.
- Primitive generating indices frozen in Stage33:

```text
[2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72].
```

## Internal source locks

- `stages/stage29/29-15/k3-ruled2-audit-execution.md`
- `stages/stage29/29-02e/result.md`
- `stages/stage33/33-00/unit-closure-contract.md`
- `stages/stage33/33-05/j2-post-r5-hs-descent-datum.json`
- `stages/stage33/33-05/certify_j2_post_r5_q_descent_cocycle.py`

## Source-lock disposition

```text
SOURCE_THEOREM_APPLICABILITY=FROZEN_POST_R5_PRE_SUPER_HOSTILE_AUDIT
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
FINITE_EXPLICIT_PRESENTATION_MATERIALIZED=true
FULL_PAIR_GALOIS_ACTION_MATERIALIZED=true
CORRECTED_J2_GEOMETRIC_REPRESENTATIVE=(f2,1)
CORRECTED_J2_HS_ZERO_DESCENT_DATUM_MATERIALIZED=true
CORRECTED_J2_Q_DESCENT_EXACT_EVIDENCE_REESTABLISHED=true
OLD_ELL_Q_J2_WITNESS_REVOKED=true
Q1_HS_D2_MATERIALIZED=true
DESCENT_OBSTRUCTION_ACCOUNTED_PREAUDIT=true
Q_RELEVANT_SURVIVING_DIM_EVIDENCE=1
R5_FULL_REPAIR_EXIT_REACHED=true
STAGE33_05_UNIT_STATUS=AUDIT_REQUIRED
AUTHORITATIVE_Q_DESCENT_CREDIT_RESTORED=false
HOSTILE_AUDIT=SUPER_HOSTILE_REQUIRED
```
