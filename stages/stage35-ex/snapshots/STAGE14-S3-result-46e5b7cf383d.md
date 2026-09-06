# Stage14-s3 — first-small-point / canonical-height gate

## Purpose

Stage14-s1 showed that positive Mordell--Weil rank is common even among fibers with no physical Stage14 partner through `B=2,000,000`. Stage14-s2 showed that the local 2-Selmer architecture gives only a subpolynomial per-base cover-class envelope, not a base-count power saving. Stage14-s3 therefore isolates the remaining gate: the first **physical** non-torsion point must be small enough in the physical height.

## Exact physical point map

Fix a primitive oriented first face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

and a physical partner

\[
F_2=(S_2,X_2,H_2)
\]

appearing in a raw pair with space diagonal `d`. Put

\[
q=\frac{X_2}{H_2+S_2},\qquad
\rho=\frac XH,\qquad s=\frac SH,\qquad
z=\frac{\gcd(S,S_2)d}{HH_2}.
\]

Then the Stage14-4ad Jacobi quartic coordinate is

\[
Y_q=z(1+q^2),\qquad A=1-2\rho^2,
\]

and the exact birational map is

\[
X_0=\frac{Y_q+1}{q^2},\qquad U=A+X_0,
\]

\[
x=\frac{U}{2s^2},\qquad
V=\frac q2(X_0^2-1),\qquad
y=\frac{V}{2s^3}.
\]

Direct substitution gives

\[
y^2=x(x-1)(x+(X/S)^2).
\]

On the integral s1 model,

\[
\boxed{Z=S^2x,\qquad W=S^3y},
\]

so

\[
\boxed{W^2=Z(Z-S^2)(Z+X^2)}.
\]

Because merged Stage14 proves every physical fiber point is non-torsion, a physical hit is automatically a non-torsion point in this height window.

## Canonical-height window

The displayed birational formulas have fixed degree. Under `d<=B`, every quantity entering `q,z,x` has rational numerator and denominator polynomially bounded in the physical cutoff and first-face height. Hence the logarithmic naive x-height satisfies

\[
h_x(P)=O(\log B+\log H).
\]

Silverman's explicit Weil-height / canonical-height comparison for elliptic curves bounds their difference in terms of the curve invariants. In this family those invariants have polynomial height in `S,X,H`, so

\[
\boxed{\hat h(P)=O(\log B+\log H)}
\]

for every physical hit with `d<=B`.

This is the exact logical small-point gate:

```text
physical hit below B
    => positive Mordell--Weil rank
    + a non-torsion point in a logarithmic canonical-height window.
```

The converse is not asserted: an arbitrary small elliptic point may map to a nonphysical chart/sign/order, and Stage14 still lacks a uniform theorem controlling the least physical non-torsion point across the moving Pythagorean-base family.

## Finite audit

The deterministic audit regenerates all `490` active vertices through `B=2,000,000`, samples `96` height-stratified active vertices and `96` matched inactive controls, and uses the **actual first physical partner** of each active vertex to construct its elliptic point exactly. PARI/GP `ellheight` then measures the Néron--Tate height of those first-hit points.

For inactive controls, the audit runs deterministic `ellrank(E,0)` and records the canonical height of an independent non-torsion witness when PARI returns one. These points are explicitly **not** treated as a Mordell--Weil basis, as shortest generators, or as the least physical points.

The frozen JSON contains the resulting summary. Its role is diagnostic: s1 already proved that many inactive controls have certified positive rank; s3 asks whether the true distinction is the existence of a sufficiently small *physical* representative.

## Theorem boundary

Stage14-s3 proves the logarithmic canonical-height necessity of a physical hit, but it does not prove a uniform distribution theorem for least non-torsion heights or regulators. In particular:

```text
POSITIVE_RANK_IMPLIES_PHYSICAL_HIT_BELOW_B=false
PARI_WITNESS_IS_MW_GENERATOR_ASSUMED=false
UNIFORM_FIRST_GENERATOR_DISTRIBUTION_PROVED=false
UNIFORM_REGULATOR_DISTRIBUTION_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

Thus the finite `sqrt(B)` signal is not promoted.

## Decision

```text
STAGE14_S3=COMPLETE_CANONICAL_HEIGHT_WINDOW_AND_SMALL_POINT_BOUNDARY
PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW=true
FINITE_POSITIVE_RANK_WITHOUT_PHYSICAL_HIT_CONFIRMED=true
SMALL_POINT_GATE_IS_GENUINE=true
UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s4 compare arithmetic small-point classes with M-degree-4 bisections
```

## Artifacts

```text
stages/stage14/14-s3/result.md
stages/stage14/14-s3/literature-height-audit.md
stages/stage14/scripts/14-s3/small_point_gate_audit.py
stages/stage14/data/14-s3/small_point_gate_audit.json
.github/workflows/stage14-s3-small-point.yml
```
