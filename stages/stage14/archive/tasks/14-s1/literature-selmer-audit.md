# Stage14-s1 literature audit — 2-descent, Selmer bounds, parity boundary

## Scope

This audit supports the Stage14-s1 arithmetic interface for

\[
E_t:y^2=x(x-1)(x+t^2),\qquad t=X/S,
\]

or, after integral scaling on a primitive Pythagorean face `F=(S,X,H)`,

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2).
\]

The purpose is not to import a generic rank-distribution heuristic. It is to identify primary sources for the exact descent objects and to freeze the boundary between unconditional Selmer/rank information and parity/BSD conjectures.

## Primary descent references

### Schaefer — 2-descent Kummer map

Edward F. Schaefer, *2-Descent on the Jacobians of Hyperelliptic Curves*, Journal of Number Theory 51 (1995), 219–232, DOI `10.1006/jnth.1995.1044`.

For an odd-degree hyperelliptic model, Schaefer constructs the cohomological descent embedding into a square-class algebra. In the split cubic/full-rational-2-torsion elliptic case this specializes to the familiar Kummer square-class map using the three linear factors of the cubic. Stage14-s1 uses this only to justify the exact structural interface; the finite Selmer computation is delegated to PARI rather than reimplementing local solubility.

### Cremona — algorithmic 2-descent

J. E. Cremona, *Classical Invariants and 2-descent on Elliptic Curves*, Journal of Symbolic Computation 31 (2001), 71–87, DOI `10.1006/jsco.1998.1004`.

This is a primary algorithmic reference for 2-descent via binary quartics and Mordell–Weil rank bounds. It supports the decision to use a mature descent implementation rather than treating modular residue survival as equivalent to Selmer membership.

### Skorobogatov–Swinnerton-Dyer — rational 2-division descent / Kummer context

A. Skorobogatov and P. Swinnerton-Dyer, *2-Descent on elliptic curves and rational points on certain Kummer surfaces*, Advances in Mathematics 198 (2005), 448–483, DOI `10.1016/j.aim.2005.06.005`.

This is directly adjacent to the Stage14 geometry: it refines 2-descent for elliptic curves with rational 2-division and studies the associated Kummer surfaces. No result from this paper is promoted into a Stage14 density theorem in s1.

### Fisher — higher descent with rational 2-torsion

Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point*, arXiv:1509.03234.

This records the role of higher descent when ordinary 2-descent leaves a gap because of Tate–Shafarevich phenomena. It reinforces the s1 rule that a Selmer upper bound is not automatically the Mordell–Weil rank.

## Computational theorem boundary: PARI/GP

PARI/GP stable elliptic-curve documentation, function `ellrank`, documents an unconditional output

```text
[r1,r2,s,L]
```

with

```text
r1 <= rank E(Q) <= r2.
```

The same documentation states that its 2-descent/Cassels-pairing computation determines the 2-Selmer rank `C`, rational 2-torsion rank `T`, and an even quantity `s=rank(Sha[2]/2 Sha[4])`, with

```text
r2 = C - T - s.
```

For the Stage14 fibers all three 2-torsion points are rational, so `T=2` and therefore

```text
C = r2 + 2 + s.
```

Stage14-s1 uses `ellrank(E,0)` only. The effort parameter is kept at zero to avoid randomized point search. `ellrootno(E)` is recorded separately and is not used to alter the unconditional rank interval.

Primary software documentation:

`https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Elliptic_curves.html`

## Exact/adjacent family literature

### Love — root numbers in a closely adjacent Z/2 x Z/4 family

Jonathan Love, *Root numbers of a family of elliptic curves and two applications*, arXiv:2201.04708, studies

\[
y^2=x(x+1)(x+t^2)
\]

and derives an explicit root-number formula, with rank conclusions in parts of the paper explicitly depending on standard rank conjectures. The sign pattern differs from the Stage14 model, so no root-number formula is imported by analogy. This paper is retained as a direct warning that root-number information and unconditional positive-rank assertions must be separated.

### Wang–Zhang — full-2-torsion shape

Zhangjie Wang and Shenxing Zhang, *On the quadratic twist of elliptic curves with full 2-torsion*, arXiv:2303.05058, treats curves of the form

\[
y^2=x(x-a^2)(x+b^2).
\]

The Stage14 integral model has exactly this polynomial shape with `(a,b)=(S,X)`, but the paper imposes additional hypotheses and studies quadratic twists; those hypotheses are not silently transferred to the Pythagorean-base Stage14 family.

### Perfect-cuboid descent literature

John Ramsden and Ruslan Sharipov, *Two and three descent for elliptic curves associated with perfect cuboids*, arXiv:1303.0765, is directly adjacent perfect-cuboid literature. Its parametric elliptic families are not identified with the Stage14 raw-pair family without an explicit birational comparison, so no rank statement is imported.

## Average-Selmer / density boundary

Known average-Selmer theorems for quadratic-twist families or for broad families with rational 2-torsion do not automatically apply to the thin Pythagorean base

\[
t=\frac{2r}{1-r^2},\qquad r\in\mathbf Q,
\]

with the Stage14 physical height. In particular, Klagsbrun–Lemke Oliver and related twist-family distribution results are retained as methods/context only. Stage14-s2 must verify the actual family, ordering, local independence and uniformity hypotheses before importing any average.

## Locked proof discipline

```text
FULL_2_TORSION_KUMMER_DESCENT_INTERFACE=PRIMARY_STANDARD_METHOD
PARI_ELLRANK_BOUNDS=UNCONDITIONAL_COMPUTATIONAL_INPUT
SELMER_RANK_EQUALS_MW_RANK=false
ROOT_NUMBER_EQUALS_RANK_PARITY_USED=false
BSD_USED=false
PARITY_CONJECTURE_USED=false
GENERIC_AVERAGE_SELMER_THEOREM_IMPORTED=false
PYTHAGOREAN_BASE_DENSITY_THEOREM_IMPORTED=false
```

Stage14-s1 therefore establishes an exact descent interface and a finite unconditional rank/Selmer-bound audit only. Any density theorem belongs to s2 or later.
