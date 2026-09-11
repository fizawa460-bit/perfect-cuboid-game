# Stage32 MB104 — A1 contraction conductor / delta source note

Status: **RETAINED MEMBER-LEVEL LOCAL COUPLING / NO FINITE-DEGREE CREDIT**.

This note separates two different delta ledgers that must not be conflated:

1. the delta of the strict transform `D` on the smooth minimal resolution `S` (the MB102 ledger), and
2. the extra normalization defect created when the exceptional `(-2)` curve over an `A1` box node is contracted and `D` is viewed as an integral curve `C` on the singular box surface `X`.

The second quantity is controlled exactly by the exceptional intersection multiplicity.

## External source lock

Primary theorem source:

José Ignacio Cogolludo-Agustín, Tamás László, Jorge Martín-Morales, András Némethi,
*Delta invariant of curves on rational surfaces I. An analytic approach*,
Communications in Contemporary Mathematics 24 (2022), no. 7, 2150052,
DOI `10.1142/S0219199721500528`, arXiv `1911.07539`.

Exact source ingredients used:

- Theorem 1.1 / Theorem 4.2: for a reduced curve germ `C` on a rational normal surface singularity,
  `delta(C)=chi(-ell'_C)-chi(s_{-[ell'_C]})` (equivalently the displayed rational-singularity formula in Theorem 4.2).
- the Riemann--Roch expression `chi(ell')=-(ell',ell'+K_pi)/2`;
- Blache correction (Theorem 1.4) and Corollary 1.5: the local correction term is the `chi` of the minimal Lipman representative of the local Weil class.

Independent cuboid differential cross-check:

Natalia Garcia-Fritz, Giancarlo Urzúa,
*Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Math. Z. 296 (2020), 573--593,
DOI `10.1007/s00209-019-02439-x`, arXiv `1804.07671`.

Theorem 3.1 gives for an irreducible cuboid-surface curve with strict transform `D`

`-deg(C) + E.D + 4*g(C) - 4 < 0`

as a sufficient condition for the curve to fall into the differential-integral locus. Thus an unknown carrier must satisfy

`d <= M + 4*g - 4`,

which is exactly the coefficient-one population-wide wall already independently retained in MB104. Corollary 3.3 obtains `d<=4g+44` only under smoothness at the surface singularities, where exceptional contact is uniformly bounded; it is not a multibranch theorem.

## A1 specialization

At each box node the surface germ is

`xz=y^2`,

with minimal resolution exceptional curve `E` satisfying

`E^2=-2`, `K_S.E=0`.

Let `D` be the strict transform of an integral curve `C` and put

`M=D.E >= 0`.

The numerical pullback of the Weil curve class is

`pi^* C = D + (M/2) E`,

because `(D+(M/2)E).E=M-M=0`.

The local discriminant group of the `A1` lattice is `Z/2`. Hence the local Weil class is trivial exactly when `M` is even. The minimal Lipman representative is

- `s=0` if `M` is even;
- `s=E/2` if `M` is odd.

Since `K_pi=0`,

`chi(E/2) = -((E/2)^2)/2 = 1/4`.

Therefore the Blache local correction is

`A_X(C)=0` for even `M`, and `A_X(C)=1/4` for odd `M`.

## Exact arithmetic-genus jump under contraction

The singular-surface self-intersection is computed by numerical pullback:

`C^2=(D+(M/2)E)^2=D^2+M^2/2`.

The `A1` resolution is crepant, so `K_X.C=K_S.D`. Smooth adjunction on `S` and Blache adjunction on `X` give

`D^2+K_S.D = 2*p_a(D)-2`,

`C^2+K_X.C = 2*p_a(C)-2 + 2*A_X(C)`.

Subtracting yields

`p_a(C)-p_a(D) = M^2/4 - A_X(C) = floor(M^2/4)`.

Thus for the 48 box nodes, with `M_i=D.E_i`,

`p_a(C)-p_a(D) = sum_i floor(M_i^2/4)`.

Since normalization is unchanged by the surface resolution, the same identity is the exact difference of total normalization-defect ledgers:

`Delta_image = Delta_strict + Q_A1`,

where

`Q_A1 := sum_i floor(M_i^2/4)`.

This is compatible with MB102: MB102 deliberately computes `Delta_strict` on the smooth resolved surface. It never asserted that contracting the `A1` exceptional curves creates zero curve singularity defect.

## Population-wide lower bounds

The function `f(m)=floor(m^2/4)` is discretely convex. If

`M=sum_i M_i = 48*q+r`, `0<=r<48`,

then among all 48-entry nonnegative integer profiles with mass `M`, the minimum contraction defect is the balanced value

`Q_min(M)=(48-r)*floor(q^2/4)+r*floor((q+1)^2/4)`.

A convenient weaker closed form is

`Q_A1 >= M^2/192 - 12`.

Combining with the retained MB104 factor-slack bound gives

- genus `0`: `M>=d+4`, hence `Q_A1 >= (d+4)^2/192 - 12`;
- genus `1`: `M>=d`, hence `Q_A1 >= d^2/192 - 12`.

These are member-level quadratic conductor/delta debts on the singular box-surface image. They do **not** bound `d` by themselves because the arithmetic genus / discriminant degree of the image can also grow quadratically.

The retained scaling ray `D_k=6kH-k*sum E_i` has `M_i=2k`, so

`Q_A1=48*k^2`.

Thus the new quadratic term is real and nonzero on the explicit effective divisor-class ray, but it does not by itself eliminate that scaling direction.

## S32-PW09 interface

The provisional Arsenal weapon `S32-PW09` records the exact member-level identity

`Disc(pi)=Br(f)+2*A`

for a singular finite curve projection and its normalization, with `deg A=delta`.

The A1 computation above supplies a source-independent lower contribution to that normalization-index divisor: the contraction of box nodes contributes total index degree at least `Q_A1`, supported over the special factor values containing the 48 box nodes. Therefore any successful discriminant route must upper-bound the available discriminant/index multiplicity at those special values; degree accounting alone is tautological and does not close MB104.

## Firewalls

- `Delta_strict` and `Delta_image` remain distinct typed quantities.
- `Q_A1` is an exact contraction correction, not an effectivity or existence theorem.
- The quadratic lower bound is not an absolute degree bound.
- No unibranch `176/192` cap is imported.
- No finite Picard enumeration is released.
- No `R29-LG2-MB`, receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit.
- Merge is not authorized.
