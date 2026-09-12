# MB104 — Hodge / exceptional-mass asymptotic wall

Status: **RETAINED NECESSARY BOUND / INSUFFICIENT FOR FINITE WINDOW / NO CREDIT**

This note asks how strongly the Picard intersection form alone can bound the minimal-cusp branch count `R8`.

Let `H=K_S`, `H^2=16`, and let the 48 exceptional curves satisfy

```text
H.E_i=0,
E_i.E_j=0  (i!=j),
E_i^2=-2.
```

For a strict transform `D`, write

```text
d=H.D,
M_i=D.E_i.
```

Over `NS(S)_R`, decompose orthogonally as

```text
D = (d/16) H - sum_i (M_i/2) E_i + z,
```

with `z.H=z.E_i=0`. The Hodge index theorem makes the complement of `H` negative definite, hence `z^2<=0`. Therefore

```text
D^2 <= d^2/16 - (1/2) sum_i M_i^2.        (H1)
```

MB102 gives

```text
D^2 = 2g-2+2Delta_total-d >= 2g-2-d.       (H2)
```

Combining `(H1)` and `(H2)` yields

```text
sum_i M_i^2 <= d^2/8 + 2d - 4g + 4.       (H3)
```

Since every minimal cusp branch has multiplicity one,

```text
R8 <= R <= M=sum_i M_i.
```

By Cauchy--Schwarz over at most 48 exceptional curves,

```text
R8^2 <= M^2 <= 48 sum_i M_i^2
      <= 6d^2 + 96d - 192g + 192.
```

Thus the strongest immediate bound from this orthogonal Hodge projection is

```text
R8 <= sqrt(6d^2 + 96d - 192g + 192)
   = (sqrt(6)+o(1)) d.
```

The branchwise FSM finite-window interface needs an asymptotic coefficient strictly below `1/4`. Since `sqrt(6)>1/4`, this numerical-lattice route is asymptotically far too weak.

This is not a claim that no stronger Picard-lattice theorem exists. It records that the direct Hodge projection onto `H` plus the 48 orthogonal exceptional classes, even combined with MB102 adjunction, cannot close MB104.

No finite window, enumeration, receiver, theorem, endpoint, Perfect Cuboid, or merge credit is granted.
