# Stage14-t30 — physical height compression and auxiliary good-prime character separation

## Purpose

Stage14-t29 showed that the canonical largest odd direction prime

\[
\ell=P^+(\Delta)_{\rm odd},\qquad
\Delta=2ab(b^2-a^2)(a^2+b^2),
\]

is useful as a large **incidence modulus**, but not as an independent square-sieve character prime. Stage14-t30 explains this boundary exactly and adds a sharp physical-height constraint on the primitive cover ratio.

The two new structural facts are:

1. every physical primitive cover ratio `(p,q)` satisfies
   \[
   \boxed{p^2+q^2\le 2B},
   \]
   when the actual space diagonal is at most `B`;
2. for the binary quartic governing the four-linear cover,
   \[
   f_{a,b}(T)=(b^2T^2-a^2)(b^2-a^2T^2),
   \]
   one has the exact discriminant identity
   \[
   \boxed{\operatorname{disc}_T f_{a,b}=\Delta(a,b)^4}.
   \]

Thus direction-support primes are exactly the bad primes of the quartic character problem. The canonical largest prime must be used for incidence routing, while auxiliary primes `lambda` not dividing `Delta` are the correct primes for character averaging.

No global power saving is claimed in t30. The remaining issue is now an incomplete **moving-family correlation average**, not local algebra.

## 1. Sharp denominator gate for the physical ratio

On the t22/t24 quotient, write the physical Kummer ratio in lowest terms as

\[
z=-\left(\frac pq\right)^2,
\qquad (p,q)=1,
\]

with

\[
\frac pq=\frac{D+X}{Q}.
\]

Since

\[
Q^2=D^2-X^2,
\]

the usual rational parametrisation gives

\[
\boxed{
X=D\frac{p^2-q^2}{p^2+q^2},
\qquad
Q=\frac{2Dpq}{p^2+q^2}.
}
\tag{30.1}
\]

Put

\[
S=p^2+q^2.
\]

Primitivity gives

\[
\gcd(S,pq)=1.
\]

Let `g` be the actual scale of the reduced direction, so the actual space diagonal is

\[
d=gD\le B.
\]

Because `gQ` is an integer physical face diagonal, the reduced denominator of `Q` in (30.1) must divide `g`. Since `gcd(S,pq)=1`, this denominator is exactly

\[
\boxed{
\frac{S}{\gcd(S,2D)}.
}
\]

Therefore

\[
\frac{S}{\gcd(S,2D)}\mid g,
\]

and hence

\[
S\le g\gcd(S,2D)\le 2gD=2d\le2B.
\]

Thus

\[
\boxed{p^2+q^2\le2B}.
\tag{30.2}
\]

In particular

\[
p,q\le\sqrt{2B}.
\]

This is substantially sharper than the earlier generic polynomial-height transfer.

## 2. Consequences for the visible canonical prime

The t29 perfect matchings are exactly the rational branches of the t26 routing theorem.

### 2.1 `C` column: `ell|a` or `ell|b`

Kernel visibility forces

\[
\ell\mid p\quad\text{or}\quad\ell\mid q.
\]

Therefore

\[
\boxed{\ell^2\le p^2+q^2\le2B},
\]

so

\[
\boxed{\ell\le\sqrt{2B}}.
\tag{30.3}
\]

### 2.2 Difference / `ru` column: `ell|(b^2-a^2)`

Visibility forces

\[
p\equiv q\pmod\ell
\quad\text{or}\quad
p\equiv-q\pmod\ell.
\]

On the non-torsion branch `p!=q`. Hence the relevant nonzero integer `p-q` or `p+q` is divisible by `ell`. Since

\[
(p+q)^2\le2(p^2+q^2)\le4B,
\]

we obtain

\[
\boxed{\ell\le2\sqrt B}.
\tag{30.4}
\]

### 2.3 Sum / `D` column: `ell|(a^2+b^2)`

Visibility is equivalent to

\[
q\equiv\pm\rho p\pmod\ell,
\qquad \rho^2=-1,
\]

or, rationally,

\[
\ell\mid p^2+q^2=S.
\]

The height gate only gives

\[
\boxed{\ell\le S\le2B}.
\tag{30.5}
\]

Consequently:

\[
\boxed{
\ell>2\sqrt B\ \text{and kernel-visible non-torsion}
\Longrightarrow \ell\mid(a^2+b^2),
}
\tag{30.6}
\]

so every super-square-root visible prime lies in the `D` / sum column.

This is a genuine branch elimination. It does not apply to kernel-invisible Gaussian/dual states.

## 3. The quartic character polynomial

The four-linear product can be grouped as

\[
g_1g_2=b^2p^2-a^2q^2,
\qquad
g_3g_4=b^2q^2-a^2p^2.
\]

For `q!=0`, put `T=p/q`. Up to the fourth-power factor `q^4`, the square condition is governed by

\[
\boxed{
f_{a,b}(T)
=(b^2T^2-a^2)(b^2-a^2T^2).
}
\tag{30.7}
\]

Expanding,

\[
f_{a,b}(T)
=-a^2b^2T^4+(a^4+b^4)T^2-a^2b^2.
\]

Its four geometric roots are

\[
\pm a/b,\qquad \pm b/a.
\]

A direct discriminant computation gives

\[
\operatorname{disc}_T f_{a,b}
=16a^4b^4(b-a)^4(b+a)^4(a^2+b^2)^4.
\]

Since

\[
\Delta=2ab(b^2-a^2)(a^2+b^2),
\]

this becomes the exact identity

\[
\boxed{
\operatorname{disc}_T f_{a,b}=\Delta^4.
}
\tag{30.8}
\]

Hence every odd direction-support prime is a bad-reduction prime for the quartic, and every odd auxiliary prime

\[
\lambda\nmid\Delta
\]

is a squarefree good-reduction prime.

This gives the conceptual explanation for the t29 boundary: the canonical direction prime is forced to be a bad prime of the character polynomial, so one should not expect it to supply generic character cancellation.

## 4. Auxiliary good-prime character cancellation

Let `chi_lambda` be the quadratic character modulo an odd prime `lambda` with

\[
\lambda\nmid\Delta.
\]

Then `f_{a,b}` is squarefree of degree four modulo `lambda`. The standard Weil bound for a quadratic character evaluated at a squarefree quartic gives

\[
\boxed{
\left|
\sum_{t\bmod\lambda}
\chi_\lambda(f_{a,b}(t))
\right|
\le3\sqrt\lambda.
}
\tag{30.9}
\]

Equivalently, the genus-one double cover

\[
y^2=f_{a,b}(t)
\]

has Hasse-size trace. Thus the auxiliary square condition has genuine local density approximately `1/2`, rather than being a tautology.

For two distinct good auxiliary primes `lambda,mu`, CRT gives exact factorisation of the complete correlation, and therefore

\[
\boxed{
\left|
\sum_{t\bmod\lambda\mu}
\chi_\lambda(f(t))\chi_\mu(f(t))
\right|
\le9\sqrt{\lambda\mu}.
}
\tag{30.10}
\]

This is precisely the kind of off-diagonal correlation input a square sieve wants.

## 5. Independence from the canonical visible incidence line

Let `ell|Delta` be the canonical visible direction prime, and let `lambda` be an auxiliary prime with

\[
\lambda\nmid\ell\Delta.
\]

The t29 condition fixes one projective residue class of `(p:q)` modulo `ell`:

```text
C column          p=0 or q=0 mod ell
ru difference     p=+q or p=-q mod ell
D sum             q=+rho p or q=-rho p mod ell
```

Modulo `lambda`, however, no such relation is imposed. By CRT, the `ell` incidence state and the `lambda` projective ratio vary independently. Therefore the good-prime character cancellation in (30.9) survives after conditioning on the canonical large-prime line.

So the correct architecture is now exact:

```text
canonical direction prime ell | Delta
    -> bad-reduction prime
    -> large incidence modulus

auxiliary prime lambda not | Delta
    -> good-reduction prime
    -> independent quadratic-character gate
```

This separation replaces the unsuccessful attempt to make one prime perform both jobs.

## 6. Why this still does not prove the visible power saving

The complete local estimates (30.9)--(30.10) are not yet the required global theorem.

The Stage14 count is anisotropic and projected:

- `(a,b)` move in a direction shell `D~X`;
- `(p,q)` are constrained by the physical interval and the sharp disk `p^2+q^2<=2B`;
- one canonical congruence line modulo a moving large prime `ell` is imposed;
- only directions for which at least one physical point exists are counted;
- the actual scale/reconstruction cutoff must be retained;
- kernel-invisible directions use the separate Gaussian/dual t26 states.

The missing estimate is therefore a moving-family incomplete correlation average over the auxiliary primes, after the large incidence line has already been imposed.

A fixed-direction complete Weil bound alone cannot be summed naively to obtain

\[
A_{1,1}(B)=O(B^{1/2-\delta}).
\]

## 7. Literature boundary

Two existing analytic tools are close but not direct black boxes.

### Pierce--Xu

Pierce--Xu prove multidimensional Burgess bounds for multiplicative characters evaluated at admissible forms. For two variables their general threshold corresponds to box sidelength exceeding approximately `lambda^(1/3+epsilon)`. This is a plausible tool for incomplete auxiliary sums once a fixed admissible packet and a suitable box are isolated.

The present problem still has a moving direction, a moving canonical modulus, anisotropic physical ranges and an existential projection, so t30 does not claim a direct application.

Reference: L. B. Pierce and J. Xu, *Burgess bounds for short character sums evaluated at forms*, Algebra & Number Theory 14 (2020), arXiv:1907.03108.

### Bonolis--Pierce polynomial sieve

Bonolis--Pierce explicitly treat counting parameter vectors for which an auxiliary polynomial equation is solvable, which is structurally close to the Stage14 projection problem. Their main theorem, however, assumes a nonsingular weighted hypersurface.

The naive total Stage14 double cover

\[
Y^2=g_1g_2g_3g_4
\]

is singular along intersections of branch components `g_i=g_j=Y=0`. Thus their theorem is not directly applicable to this factorised cover.

Reference: D. Bonolis and L. B. Pierce, *Application of a polynomial sieve: beyond separation of variables*, Algebra & Number Theory 18 (2024), arXiv:2209.02494; current arXiv v3 includes the published correction.

## 8. Frozen finite audit

The t30 standard-library audit keeps the t29 box `a,b,p,q<=40` and verifies the new statements.

It checks:

- all `239121` primitive physical-interval tuples satisfy the exact denominator identity and the derived `S<=2B_min` inequality;
- all `6371` canonical rational matching incidences satisfy the relevant rational routing;
- after removing the `33` matching torsion incidences, all `6338` non-torsion incidences satisfy the column-specific height bounds;
- every incidence with `ell>2 sqrt(B_min)` is in the sum / `D` column;
- the discriminant identity `disc(f)=Delta^4`;
- squarefreeness and the `3 sqrt(lambda)` complete character bound for all sampled good auxiliary primes through `97`;
- two-prime CRT correlation bounds.

These are algebraic/finite diagnostics only; they are not promoted to an asymptotic density statement.

## Boundary

```text
STAGE14_T30=COMPLETE_PHYSICAL_DENOMINATOR_AND_BAD_GOOD_PRIME_SEPARATION
PHYSICAL_PQ_DISK_BOUND=P2_PLUS_Q2_LE_2B
VISIBLE_C_COLUMN_PRIME_LE_SQRT_2B=true
VISIBLE_RU_DIFFERENCE_PRIME_LE_2SQRT_B_NON_TORSION=true
SUPER_SQRT_VISIBLE_ONLY_D_SUM_COLUMN=true
AUXILIARY_QUARTIC_DISCRIMINANT_EQUALS_DELTA4=true
DIRECTION_PRIMES_ARE_AUXILIARY_QUARTIC_BAD_PRIMES=true
GOOD_AUXILIARY_PRIME_WEIL_CANCELLATION=true
GOOD_AUXILIARY_TWO_PRIME_CORRELATION=true
CANONICAL_INCIDENCE_AND_AUXILIARY_CHARACTER_CRT_INDEPENDENT=true
BONOLIS_PIERCE_DIRECT_APPLICATION=false
PIERCE_XU_DIRECT_POWER_SAVING_PROVED=false
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t31 prove a moving-family auxiliary-prime correlation bound on the visible D/sum incidence branch, using the p^2+q^2<=2B disk, and derive the analogous good-prime averaging object for the t26 Gaussian/dual invisible branch
```
