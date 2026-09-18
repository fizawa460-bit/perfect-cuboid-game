# Stage32 MB104 — W31 Lazarsfeld--Mukai elementary-transform preflight — 2026-09-18

Status: **PROMOTE TO SECOND SHALLOW SCAN / FIRST POSITIVE WIDE-SCAN PRESSURE / NO CREDIT**

## 1. Input from a hypothetical carrier

Assume the active dangerous carrier exists:

```
C in |D_l|,
D_l=7lH-4l sum_(p in Sigma)E_p,
D_l^2=336l^2,
H.D_l=112l.
```

The canonical/hyperplane line bundle `O_S(H)` is globally generated and has seven canonical coordinate sections.

Put

```
A=O_C(H),
V=H0(S,O_S(H)), dim V=7.
```

Since `O_S(H)` is globally generated, the restriction evaluation is surjective:

```
V tensor O_S -> i_*A -> 0.
```

Define

```
0 -> F -> V tensor O_S -> i_*A -> 0.       (LM)
```

Here `C` is Cartier on the smooth resolution and `A` is invertible on `C`.  Locally, after trivializing `A`, the quotient is `R/(f)`; a surjection `R^7 -> R/(f)` has free kernel of rank seven.  Hence `F` is a vector bundle.  Put

```
E=F^vee.
```

This construction uses only the actual carrier and ambient canonical sections.  It does not use residual-sheet or branch-lift data.

## 2. Chern classes

For the elementary transform along a Cartier curve,

```
rank(E)=7,
c1(E)=D_l,
c2(E)=deg A=H.D_l=112l.
```

Thus the Bogomolov discriminant is

```
Delta_BG(E)
 =2*7*c2(E)-6*c1(E)^2
 =14*(112l)-6*(336l^2)
 =-224l(9l-7).
```

Therefore

```
Delta_BG(E)<0
```

for every `l>=1`.

By Bogomolov--Gieseker, a slope-semistable torsion-free sheaf on a smooth projective surface in characteristic zero has nonnegative discriminant.  Hence every hypothetical carrier canonically creates a **slope-unstable rank-seven bundle**.

This is qualitatively different from the previous cheap failures: a genuine new global object is forced, and its Harder--Narasimhan filtration supplies new determinant classes.

## 3. Why this is PROMOTE rather than closure

Negative discriminant alone does not contradict existence.  It proves only that `E` or equivalently the elementary transform `F` has a destabilizing subsheaf.

For

```
mu_H(E)=H.D_l/7=16l,
mu_H(F)=-16l,
```

a maximal destabilizing factor must cross one of these slopes.

The useful additional structure is

```
F subset O_S^7.
```

A saturated subsheaf of a trivial bundle has determinant constrained by an effective divisor after taking exterior powers.  Combined with the exact Picard lattice, this can potentially reduce the HN determinant to a finite numerical cone problem.

That reduction has **not** yet been proved.

## 4. Second shallow scan target

Do not launch a large HN enumeration yet.

The next test is only:

1. take a maximal destabilizing saturated subsheaf `G subset F` of rank `r=1,...,6`;
2. write `det G=O_S(-B)` using the injection into a trivial bundle;
3. derive the slope window from
   ```
   -16l < mu_H(G) <= 0;
   ```
4. combine with the known zero-quartic and rank-3 fibration pairings;
5. ask whether **any** effective determinant class `B` can satisfy the resulting inequalities.

If the cone is empty, W31 closes the carrier. If it is large, W31 returns to SOFT-PARK. If it collapses to a small explicit family, only then deepen.

## Decision

```
tested_architecture_status = PROMOTE
broader_direction_status   = PROMOTE
second_scan_required       = true
DEEP                        = false
```

No MB104 or downstream credit is claimed.
