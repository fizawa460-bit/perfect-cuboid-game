# Stage33-05 source lock — Creutz--Viray presentation and arithmetic descent

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

For the rational ruled base `W=P1`, the source gives `L_{c,E}=L_E`.  At a singular branch point its `e(b/w)` is the sum of ramification indices over normalization points; this is load-bearing for the corrected count of four nodal even-e fibers.

## Hyperelliptic cocycle / Hochschild--Serre compatibility source

- Brendan Creutz, Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, arXiv:1403.2924, Manuscripta Math. 147 (2015), 139--167.
- Remark 3.1: the exact Brauer-to-`H^1(Pic)` construction is the one coming from the étale Hochschild--Serre spectral sequence, up to sign.
- Proposition 3.2: gives the explicit Picard-valued Galois cocycle associated to the corestriction construction and identifies its class with the spectral-sequence map.
- Lemma 3.4: lifts the Picard cocycle to divisors and computes its coboundary explicitly as the divisor of the norm of `(x-alpha)` with the corresponding cochain exponent.
- Lemma 3.5: identifies the resulting function-field 2-cocycle with the corestriction quaternion algebra by cup product and Shapiro.

These locators are used only for compatibility of the explicit Creutz--Viray presentation with the standard étale/Kummer cochain construction.  The final `C2` Bockstein itself is recomputed exactly in `q1_hs_d2_bockstein.py`.

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

The Stage33 checker performs this normalized cochain chase explicitly on `C2=<ct>`.

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

The true exact presentation is now materialized in basis `[J1,J2,q1,q2,q3]` with

```text
im(x-alpha)=span_F2{
  J1,
  b*J2+q1+q2,
  d*J2+q1+q2+q3
}, b,d in F2,
```

and geometric quotient basis `[J2,q1]`.  The full-pair action is identity on the quotient, so the geometric invariant dimension is two.

## J2 arithmetic source application

The Q-defined branch algebra representative is

```text
ell_J2=
4*(alpha^2*t^2+t^4-4*t^2+2)
 / ((t^2-1)*(t^2-2*t-1)),
```

with exact square norm

```text
Norm(ell_J2)=1024/(t^2-2*t-1)^4.
```

All geometric branch valuations are even; Creutz--Viray Proposition 3.1 / Corollary 3.2 and Proposition 3.4 then certify the corresponding Q-defined corestriction class as unramified on the K3 resolution.

## q1 Hochschild--Serre source application

The presentation defect is `ct(q1)-q1=J1`.  Stage33 materializes

```text
D=Cb+E_P0,
Cb : i*A1+B1=i*A2+B2=i*A3+B3=0,
P0=[0:1:0:-1:0:1],
```

as an integral `ct`-invariant NS lift of `J1`.  The invariant test conic

```text
T : A1=0, A2+B3=0, A3-B2=0
```

has `D.T=1`, proving `D` is not a cyclic norm.  The Kummer defect is `D mod 2`; on `C2=<ct>` the normalized integral lift has

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

## Source-lock disposition

```text
SOURCE_THEOREM_APPLICABILITY=FROZEN_AUDITED
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
FINITE_EXPLICIT_PRESENTATION_MATERIALIZED=true
FULL_PAIR_GALOIS_ACTION_MATERIALIZED=true
J2_Q_ARITHMETIC_REPRESENTATIVE_MATERIALIZED=true
Q1_HS_D2_MATERIALIZED=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_CERTIFIED=true
Q_RELEVANT_SURVIVING_DIM=1
MAIN_PRODUCTION_COMPLETE=true
HOSTILE_AUDIT=PENDING
```
