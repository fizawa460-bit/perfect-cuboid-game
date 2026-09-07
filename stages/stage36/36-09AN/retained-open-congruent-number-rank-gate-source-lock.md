# Stage36 36-09AN source lock: retained-open full-2 covering map and congruent-number torsion/rank gate

Accessed: 2026-09-07

This leaf strengthens 36-09AM. It uses the already source-locked full-2 homogeneous-space equations from 36-09AJ and the standard rational torsion structure of the congruent-number curve.

## A. Explicit map from the Stage36 full-2 covering to its Jacobian

36-09AJ source-locks the standard full-2 homogeneous-space model for

```text
E_T : y^2 = x*(x-T)*(x+T)
```

and rewrites the Stage36 common-u:v curve as

```text
D1*u^2-D2*r^2 = T*v^2,
D1*u^2-D3*s^2 = -T*v^2,
D1*D2*D3 = L^4.
```

On the affine chart `v != 0`, set

```text
x = D1*(u/v)^2,
y = L^2*u*r*s/v^3.
```

Then exactly

```text
x-T = D2*(r/v)^2,
x+T = D3*(s/v)^2,
```

and therefore

```text
y^2 = x*(x-T)*(x+T).
```

Thus this is an explicit Q-rational covering map on the retained chart, not merely a Jacobian isomorphism statement.

## B. Retained-open nonvanishing

Hostile-audited 36-09AD gives

```text
U=A*u^2,
V=B*v^2,
U-V=eta*2^e*C*r^2,
U+V=2^f*D*s^2
```

with the receiver retained open requiring the two original factor-square conditions to be nonzero. Hence on a retained receiver point

```text
u != 0,
v != 0,
r != 0,
s != 0.
```

The explicit map above therefore satisfies

```text
x != 0,
x-T != 0,
x+T != 0,
y != 0.
```

So the image is not `O`, `(0,0)`, `(T,0)`, or `(-T,0)`.

## C. Rational torsion on congruent-number curves

For nonzero positive integer `n`, the standard congruent-number curve

```text
E_n : Y^2 = X^3 - n^2*X
```

has rational torsion subgroup exactly

```text
E_n(Q)_tors = { O, (0,0), (n,0), (-n,0) }
             ~= Z/2Z x Z/2Z.
```

Accessible reference checked:
- Roberto Villaflor Loyola, *Notes on elliptic curves and the congruent number problem*, Section 5: https://www.mat.uc.cl/~roberto.villaflor/pdf2/teach/AulasIMPA/Notes_IMFEC.pdf

This is also the standard congruent-number torsion computation obtainable from Nagell-Lutz.

The rational square scaling from audited 36-09AI/AJ carries the four raw branch points `O,(0,0),(T,0),(-T,0)` to the four normalized 2-torsion points on `E_n` and preserves the distinction between branch/nonbranch points.

Therefore every retained-open Stage36 rational covering point maps to a rational point of infinite order on `E_n`.

## D. Congruent-number and Tunnell implication

The congruent-number equivalence source-locked in 36-09AL gives

```text
rank E_n(Q) > 0  <=>  n is a congruent number.
```

36-09AM source-locks Tunnell's unconditional necessary equality for both odd and even positive squarefree `n`.

Hence the exact retained-open implication is

```text
Stage36 retained receiver point
  -> non-2-torsion Q-point on E_n
  -> positive Mordell-Weil rank
  -> n congruent
  -> parity-appropriate Tunnell necessary equality holds.
```

Contrapositively, failure of the parity-appropriate Tunnell equality excludes the retained-open Stage36 covering **without any Selmer/local-solubility hypothesis**.

## Scope firewall

- Tunnell equality is only necessary; no BSD converse is used.
- The result does not decide any branch on which Tunnell's equality holds.
- It does not enumerate all variable `n` produced by Stage36.
- It does not by itself shrink the global parameter population until the equality is evaluated or structurally constrained across that population.
- It does not close the receiver/R29/Q11/endpoint or prove any perfect-cuboid claim.
