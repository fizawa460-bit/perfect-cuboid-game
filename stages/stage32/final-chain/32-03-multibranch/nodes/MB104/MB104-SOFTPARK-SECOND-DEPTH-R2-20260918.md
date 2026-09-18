# Stage32 MB104 — SOFT-PARK second-depth screening Round 2 — 2026-09-18

Status: **ROUND 2 COMPLETE / W20 ADVANCES / W5 HIGH RESERVE / W6,W11,W30 PARK / NO MATHEMATICAL CREDIT**

## Scope

Continue the user-directed second-depth review without manufacturing new W labels.

Round 2 screens

```
W5   adaptive higher symmetric differentials
W6   genuinely coupled two-factor modular relation
W11  special seven-section elliptic linear series
W20  cuboid-specific residue / Abel moment identities
W30  four-quadric-specific Gaussian identities
```

The target remains the active balanced ray

```
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
D_l^2=336l^2,
K.D_l=112l,
normalization genus=1.
```

A route advances only if it now has a source-complete forward object and a credible all-`l` or large-`l` exclusion shape.

## W5 — adaptive higher symmetric differentials

### Published upgrade checked

Bruin--Ilten--Xu (EpiGA 2025, DOI 10.46298/epiga.2025.12665) gives an explicit quasi-polynomial formula for the local Euler characteristic of `Sym^m Omega` at `A_n` singularities and an explicit lattice-point method for the extension conditions.  This is genuinely newer than the retained BTVA pure-power wall.

For an `A_1` point, however, the same paper recalls the BTVA asymptotic

```
chi^1(A1, Sym^m Omega) = (4/27)m^3 + O(m).
```

On the smooth cuboid resolution,

```
K^2=16,
c2=80,
```

so Hirzebruch--Riemann--Roch has leading term

```
chi(Sym^m Omega_S)
 ~ ((K^2-c2)/6)m^3
 = -(32/3)m^3.
```

All 48 `A_1` corrections in the standard lower bound contribute only

```
48*(4/27)m^3=(64/9)m^3.
```

Thus the untwisted standard lower-bound coefficient remains

```
-32/3 + 64/9 = -32/9 < 0.
```

So the 2025 exact local-Euler formula does **not** by itself turn the cuboid resolution into a big-cotangent closure.

The retained BTVA pure-power architecture also has exact zero slack:

```
available hyperplane vanishing / order = 1/2,
A1 regularization cost / order        = 1/2.
```

Therefore the new source materially improves exact finite-order bookkeeping but does not yet supply the missing asymptotic advantage.

A W5 revival still needs one of:

- an explicit higher-order section with better-than-`1/2` movable exceptional valuation;
- a section intrinsically regular at many of the fourteen active nodes;
- a packet-specific cancellation reducing the extension cost.

**Disposition: HIGH_RESERVE.**

It is worth revisiting after the five-round selection because the 2025 paper gives a concrete finite-order/lattice-point engine, but there is not yet a direct MB104 cutoff.

## W6 — coupled two-factor modular relation

Freitag--Salvati Manni identifies the box variety as a modular surface and the retained MB104 archive has already made the two quotient factor maps explicit.

For the active `e=2` normalization image

```
Psi:E -> C subset R x R = P1 x P1,
[C]=(28l,28l).
```

Any ordinary coupled modular divisor that descends to a divisor of bidegree `(a,b)` on `R x R` has intersection capacity

```
C.(a,b)=28l(a+b).
```

The archive has already classified every nontrivial raw special-grid capacity case:

```
(1,0), (0,1), (1,1), (1,2), (2,1).
```

Equivalently, all total bidegrees `a+b<4` are exhausted.  For `a+b>=4`,

```
28l(a+b) >= 112l,
```

which is at least the entire special-grid branch mass, so a raw zero-count/Bezout argument cannot improve the packet.

Hence a genuinely useful "coupled modular" continuation must use more than the divisor of a bivariate modular form: character, cover, monodromy, tangent, or Abel--Jacobi data.  Those structures have already been source-locked more concretely in the W20/conductor package.

**Disposition: PARK_DOMINATED_BY_W20.**

## W11 — seven-section elliptic linear series

On the elliptic normalization put

```
L=nu^*O_S(H),
deg L=112l,
V=im(H0(S,H)->H0(E,L)),
dim V<=7.
```

The support hyperplane gives one section whose zero divisor is saturated by the `112l` supported normalization points.

The canonical model of the cuboid surface is cut out by four quadrics, so the seven ambient sections satisfy at least four quadratic relations:

```
ker(Sym^2 V -> H0(E,L^2)) has dimension >=4.
```

But

```
dim Sym^2(V) <=28,
h0(E,L^2)=224l.
```

Thus there is no dimension overload.  A seven-dimensional subsystem of a line bundle of degree `112l` also has enormous ambient room; bare elliptic Riemann--Roch and the existence of four quadric relations do not produce an `l` cutoff.

To become useful, W11 would need special value/principal-part identities at the saturated support divisor.  That is exactly the packet-sensitive residue/Abel input now isolated in W20.

**Disposition: PARK_DOMINATED_BY_W20.**

## W20 — residue / Abel / factor-line torsion

This round finds W20 substantially more concrete than its original wide-scan label suggested.

For the `e=2` common-`H` cover, the retained archive proves that the two degree-`28l` factor fiber line bundles satisfy

```
M_1 tensor M_2^(-1) in Pic^0(E)[2].
```

Moreover two **explicit sheet-selected full fibers** are constructed entirely from the unresolved supported-node binary allocation:

```
D_z^+ = psi_1^*(+u),
D_w^+ = psi_2^*(+a),
deg D_z^+ = deg D_w^+ = 28l,
```

and hence

```
delta_fac
 = O_E(D_z^+-D_w^+)
 in Pic^0(E)[2].
```

Thus the continuous Picard-`0` ambiguity is already reduced to four classes.

This is not yet an `e=2` contradiction: the archive correctly does **not** identify `delta_fac` with the residual half-branch class

```
eta in Pic^0(E)[2],
e=2 <=> eta=0.
```

The third-depth target is therefore a single explicit bridge rather than another counting inequality:

```
ambient/product-cover restrictions
 -> compute delta_fac
 -> relate delta_fac to eta or to the generalized-Jacobian conductor character
 -> finite E[2] compatibility test.
```

Any source-locked bridge `delta_fac=eta` would be especially strong: in the `e=2` branch it would force `delta_fac=0`, so an independent ambient computation of a nonzero class would close the whole `e=2` branch uniformly in `l`.

More generally, because only four torsion classes remain, an exact conductor-descent test can check all possibilities uniformly rather than search a growing branch-allocation space.

This route applies directly only to the `e=2` branch; `e=4` would still need its own closure.  Nevertheless it is a genuine finite global obstruction on the actual packet and is the strongest Round-2 candidate.

**Disposition: ADVANCE_FOR_THIRD_DEPTH.**

## W30 — four-quadric Gaussian identity

The bare Gaussian dimension architecture was already dead:

```
dim wedge^2 V <=21,
h0(E,L^2)=224l.
```

At second depth one may try to use the four fixed quadrics defining `S`.  Differentiating those relations does give four canonical first-order relations among the seven ambient sections.

However, before packet data are inserted, these are the tautological conormal relations of the complete intersection

```
S=(2,2,2,2) subset P6.
```

Their number is fixed while `deg L=112l` grows.  They do not create an asymptotic overload or a finite cutoff by themselves.

The only plausible upgrade is to evaluate these differential relations at the saturated support divisor and extract residues/principal parts.  That is again W20's packet-sensitive target.

**Disposition: PARK_DOMINATED_BY_W20.**

## Round-2 selection

```
ADVANCE_FOR_THIRD_DEPTH:
  W20  finite Pic^0(E)[2] Abel/conductor bridge

HIGH_RESERVE:
  W5   2025 exact A_n local-Euler machinery, but no favorable cuboid asymptotic yet

PARK:
  W6   ordinary coupled modular divisors exhausted; stronger data absorbed by W20
  W11  seven-section/quadric dimension has large slack; packet refinement absorbed by W20
  W30  fixed Gaussian/conormal relations do not scale; packet refinement absorbed by W20
```

No closure or downstream credit is claimed.

## Next second-depth round

Continue with the normalization/projective-geometry family

```
W17  support-stabilizer carrier dichotomy
W18  cuboid-specific secant defect
W19  adaptive Wronskian / forced contact
W23  joint-factor special singularity/grid geometry
W29  cotangent stability on the special elliptic normalization
```

Use the same promotion rule: no third-depth advance without a source-complete forward adapter and an explicit path to all-`l` or finite-cutoff exclusion.
