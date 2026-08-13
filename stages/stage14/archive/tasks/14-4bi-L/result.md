# Stage14-4bi-L — composite edge-kernel incidence and large-kernel dichotomy

## Purpose

Stage14-4bh and merged Stage14-s6-02 proved the first direct post-local incidence saving by selecting one large odd kernel prime `ell` on a fixed packet edge.  This L-branch strengthens that prime-level statement to the **entire odd squarefree edge kernel** and isolates the exact complement to be handed to the S-branch.

The fixed global witness packet from merged Stage14-s6-01 is

```text
d0 = tau0 * a * b,
d1 = tau1 * a * c,
d2 = tau2 * b * c,
```

where

```text
taui in {+1,-1,+2,-2},
a | rad_odd(S),
b | rad_odd(X),
c | rad_odd(H),
gcd(a,b)=gcd(a,c)=gcd(b,c)=1.
```

The two primary equations are

\[
\tau_0ab\,u_0^2-\tau_1ac\,u_1^2=S^2D^2,
\tag{L.1}
\]

\[
\tau_2bc\,u_2^2-\tau_0ab\,u_0^2=X^2D^2,
\tag{L.2}
\]

and subtraction gives

\[
\tau_2bc\,u_2^2-\tau_1ac\,u_1^2=H^2D^2.
\tag{L.3}
\]

Stage14-4bi-L proves that each of `a,b,c` itself, not merely its largest prime factor, is a usable global incidence modulus.  Consequently a kernel may be very smooth and still give the full congruence gain when its composite size is large.

The final large-kernel dichotomy is:

> Let `K=max(a,b,c)`, and let `U_*` be the larger dyadic size of the two square variables incident to the edge carrying `K`.  For any thresholds `kappa,upsilon>0`, if `K>=B^kappa`, then either
>
> 1. `U_*>=B^upsilon`, in which case the packet square-variable layer gains
>    \[
>    B^{-\min(\kappa,\upsilon)+\epsilon},
>    \]
>    relative to the unconstrained incident rectangle; or
> 2. `U_*<B^upsilon`, in which case the denominator is forced into
>    \[
>    D\ll B^\upsilon.
>    \]

Thus the L-route leaves **no arbitrary large-kernel remainder**.  It leaves only a small-denominator remainder, which is an appropriate interface to the S/height route.

No full family `delta_post>0` is claimed here: converting this packet-level dichotomy into a global count still requires the S-branch estimate for the complementary small-kernel / small-denominator region.

---

## 1. Exact composite-modulus normalization

Because `a|rad_odd(S)`, the squarefree integer `a` divides `S`.  Factoring `a` from (L.1) gives

\[
a\bigl(\tau_0b u_0^2-\tau_1c u_1^2\bigr)=S^2D^2.
\]

Since `S=a(S/a)`, division by `a` is exact and gives

\[
\boxed{
\tau_0b u_0^2-\tau_1c u_1^2
=a\left(\frac Sa\right)^2D^2.
}
\tag{L.a}
\]

Similarly,

\[
\boxed{
\tau_2c u_2^2-\tau_0a u_0^2
=b\left(\frac Xb\right)^2D^2,
}
\tag{L.b}
\]

and

\[
\boxed{
\tau_2b u_2^2-\tau_1a u_1^2
=c\left(\frac Hc\right)^2D^2.
}
\tag{L.c}
\]

These are stronger than selecting one prime divisor.  They retain every odd prime in the relevant edge packet simultaneously.

Reducing modulo the whole composite edge modulus gives

```text
mod a: tau0*b*u0^2 == tau1*c*u1^2,
mod b: tau2*c*u2^2 == tau0*a*u0^2,
mod c: tau2*b*u2^2 == tau1*a*u1^2.
```

Because `a,b,c` are pairwise coprime and odd, all displayed coefficients on the corresponding modulus are units.

---

## 2. Composite squarefree congruence-line lemma

Let `q` be odd and squarefree, and let `A,B` be units modulo `q`.  Consider

\[
A x^2\equiv B y^2\pmod q.
\tag{L.4}
\]

For each prime `p|q`:

- if `B/A` is a quadratic residue mod `p`, the solutions are contained in the two lines
  \[
  x\equiv \pm r_p y\pmod p;
  \]
- if `B/A` is a nonresidue, the only exact solution with one coordinate a unit is absent, and the residual solution `(0,0)` mod `p` is contained in any chosen line, so one line is enough for an upper cover.

Hence the full solution set modulo `q` is contained in at most

\[
2^{\omega(q)}
\]

CRT products of one linear congruence at every `p|q`.  Each CRT product is a rank-two sublattice of `Z^2` of index `q`.

Therefore, in a positive dyadic rectangle of side lengths `U,V`,

\[
\boxed{
N_q(U,V)
\ll
2^{\omega(q)}
\left(\frac{UV}{q}+\min(U,V)+1\right).
}
\tag{L.5}
\]

Since `q<=B^{O(1)}` in the Stage14 physical witness box and

\[
2^{\omega(q)}\ll_\epsilon q^\epsilon,
\]

we may write

\[
\boxed{
N_q(U,V)
\ll_\epsilon
B^\epsilon
\left(\frac{UV}{q}+\min(U,V)+1\right).
}
\tag{L.6}
\]

This is the composite-kernel replacement for the prime-level two-line bound of 4bh/s6-02.

---

## 3. Application to all three kernel edges

For the `a` edge, (L.a) yields

\[
\tau_0b u_0^2\equiv \tau_1c u_1^2\pmod a,
\]

so

\[
\boxed{
N_a(U_0,U_1)
\ll_\epsilon B^\epsilon
\left(\frac{U_0U_1}{a}+\min(U_0,U_1)+1\right).
}
\tag{L.7a}
\]

For the `b` edge,

\[
\boxed{
N_b(U_0,U_2)
\ll_\epsilon B^\epsilon
\left(\frac{U_0U_2}{b}+\min(U_0,U_2)+1\right).
}
\tag{L.7b}
\]

For the `c` edge,

\[
\boxed{
N_c(U_1,U_2)
\ll_\epsilon B^\epsilon
\left(\frac{U_1U_2}{c}+\min(U_1,U_2)+1\right).
}
\tag{L.7c}
\]

Thus a large **smooth** edge kernel is just as useful as a large prime edge kernel at this stage.  The prior condition

```text
P^+(abc) >= B^eta
```

is sufficient but no longer necessary.  The natural L-route size variable is now

\[
\boxed{K=\max(a,b,c).}
\]

---

## 4. Quantitative long-incident gain

Suppose the maximum edge kernel is `K=a`; the other cases are symmetric.  Put

\[
U_* = \max(U_0,U_1).
\]

Relative to the unconstrained incident rectangle `U_0U_1`, (L.7a) gives

\[
\frac{N_a(U_0,U_1)}{U_0U_1}
\ll_\epsilon
B^\epsilon
\left(
\frac1a+\frac1{U_*}+\frac1{U_0U_1}
\right).
\tag{L.8}
\]

If

\[
a\ge B^\kappa,
\qquad
U_*\ge B^\upsilon,
\]

then `U_0,U_1>=1` implies `U_0U_1>=U_*`, and therefore

\[
\boxed{
\frac{N_a(U_0,U_1)}{U_0U_1}
\ll_\epsilon
B^{-\min(\kappa,\upsilon)+\epsilon}.
}
\tag{L.9}
\]

Exactly the same statement holds when the largest edge kernel is `b` or `c`.

This is a genuine restriction on the actual global witness variables, not a local-character reweighting.

---

## 5. The short-incident branch forces a small denominator

The previous stage left `U_*` short as an apparently separate obstruction.  Once the **largest composite edge kernel** is used, this branch has a deterministic consequence.

Again assume `K=a=max(a,b,c)`.  From (L.a),

\[
a\left(\frac Sa\right)^2D^2
=
\left|\tau_0b u_0^2-\tau_1c u_1^2\right|.
\]

Because

```text
|tau0|,|tau1| <= 2,
b<=a,
c<=a,
(S/a)^2 >= 1,
```

we obtain

\[
aD^2
\le
2b u_0^2+2c u_1^2
\le
2a(u_0^2+u_1^2).
\]

Canceling `a` gives

\[
\boxed{D^2\le2(u_0^2+u_1^2).}
\tag{L.10a}
\]

Therefore

\[
\boxed{D\le2\max(u_0,u_1).}
\tag{L.10b}
\]

The same argument applied to (L.b) or (L.c) yields the symmetric statement:

> If `K=max(a,b,c)` lies on edge `ij`, then
> \[
> \boxed{D\le2\max(u_i,u_j).}
> \]

Consequently, if the incident dyadic maximum satisfies

\[
U_*<B^\upsilon,
\]

then every witness in that box satisfies

\[
\boxed{D<2B^\upsilon.}
\tag{L.11}
\]

Thus the short-variable complement is not an uncontrolled large-kernel sector.  It is a **small-denominator sector**.

---

## 6. Large-kernel dichotomy

Combine Sections 4 and 5.

Fix `kappa,upsilon>0`.  In every fixed packet/dyadic witness box with

\[
K=\max(a,b,c)\ge B^\kappa,
\]

choose an edge attaining `K` and let `U_*` be the larger incident square-variable scale.

Then exactly one of the following holds.

### L-long

\[
U_*\ge B^\upsilon.
\]

The composite congruence-line theorem gives a relative square-variable incidence saving

\[
\boxed{B^{-\min(\kappa,\upsilon)+\epsilon}.}
\]

### L-short

\[
U_*<B^\upsilon.
\]

The packet equation forces

\[
\boxed{D<2B^\upsilon.}
\]

So the entire large-kernel route reduces to

```text
K >= B^kappa
    -> composite incidence saving
       OR
       D << B^upsilon.
```

For the symmetric one-parameter choice `kappa=upsilon=eta`,

```text
K >= B^eta
    -> B^(-eta+epsilon) incidence gain
       OR
       D < 2 B^eta.
```

This is the clean interface intended for later 14-4bj assembly with the S-route.

---

## 7. What changed relative to 4bh / s6-02

The previous prime-level split left

```text
P^+(abc) < B^eta
```

as a `tiny/smooth kernel` complement.  That condition mixes two genuinely different phenomena:

1. the edge kernels themselves are small;
2. an edge kernel is large but composed only of small primes.

The composite-modulus lemma eliminates the second phenomenon from the hard complement.

A very smooth number such as

```text
a = p1 p2 ... pr
```

still imposes one CRT projective line condition at every prime and therefore a rank-two lattice of total index `a`, up to only `2^omega(a)=a^o(1)` line multiplicity.

Accordingly the L-route hard complement is now measured by

```text
max(a,b,c) < B^kappa,
```

not by a largest-prime condition.

This is a strict structural improvement.

---

## 8. Interaction with the S-route

Stage14-4bi-L is deliberately not a second copy of the smooth/tiny-kernel analysis.

Its receiver contract for `14-4bi-S` / later `14-4bj` is:

```text
L-route closed region:
  K=max(a,b,c) >= B^kappa
  and U_* >= B^upsilon
  -> B^(-min(kappa,upsilon)+epsilon) incidence gain.

L-route transferred region:
  K=max(a,b,c) >= B^kappa
  and U_* < B^upsilon
  -> D < 2 B^upsilon.

S-route intrinsic region:
  K=max(a,b,c) < B^kappa.
```

Thus S only needs to quantify

- genuinely small edge kernels; and/or
- small denominators produced by the L-short transfer.

It no longer needs a separate `large but smooth kernel` theorem.

---

## 9. Exponent ledger

The global pre-post-local upper bound remains

\[
N_{\rm loc}(B)\ll B^{41/42+\epsilon}.
\]

The square-root upper-bound target still needs total post-local saving

\[
\boxed{\frac{10}{21}}.
\]

4bi-L does **not** claim that the packet-level factor in the L-long region automatically multiplies the full `B^(41/42)` count without further bookkeeping.  The correct statement is sectoral and conditional on the dyadic split.

If later S proves that the union

```text
K < B^kappa
OR
D < 2 B^upsilon
```

has a global saving `delta_S>0`, then 14-4bj may combine the two branches with

\[
\delta_{post}
=\min\{\min(\kappa,\upsilon),\delta_S\}
\]

up to the already-controlled `B^epsilon` packet/dyadic multiplicities.

This assembly formula is a target contract, not yet a theorem that `delta_S>0` exists.

---

## Boundary

```text
STAGE14_4BI_L=COMPOSITE_EDGE_KERNEL_INCIDENCE_AND_LARGE_KERNEL_DICHOTOMY_CLOSED
S6_01_EDGE_PACKET_FACTORIZATION_IMPORTED=true
S6_02_PRIME_LEVEL_INCIDENCE_IMPORTED=true
COMPOSITE_EDGE_KERNEL_NORMALIZATION_EXACT=true
COMPOSITE_SQUAREFREE_LINE_COVER_COUNT=2^omega(q)
COMPOSITE_EDGE_LATTICE_INDEX_EQUALS_KERNEL=true
COMPOSITE_EDGE_RECTANGLE_BOUND_PROVED=true
SMOOTH_LARGE_EDGE_KERNEL_INCIDENCE_CLOSED=true
LARGE_KERNEL_SIZE_VARIABLE=K=max(a,b,c)
LARGE_KERNEL_LONG_INCIDENT_GAIN=B^(-min(kappa,upsilon)+epsilon)
LARGEST_KERNEL_SHORT_INCIDENT_IMPLIES_D_LE_2_USTAR=true
LARGE_KERNEL_SHORT_INCIDENT_TRANSFERS_TO_SMALL_DENOMINATOR=true
ARBITRARY_LARGE_KERNEL_REMAINDER_OPEN=false
S_ROUTE_RECEIVES_SMALL_KERNEL_OR_SMALL_DENOMINATOR=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bj after 14-4bi-S, assemble the L-route composite-kernel dichotomy with the S-route small-kernel/small-denominator estimate and test whether a global delta_post>0 follows
```
