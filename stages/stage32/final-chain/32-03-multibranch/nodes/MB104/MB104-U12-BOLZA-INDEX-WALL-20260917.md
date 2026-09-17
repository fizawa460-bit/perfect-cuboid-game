# Stage32 MB104 — U12 Bolza Hecke-index wall — 2026-09-17

Status: **DEGREE/INDEX SUBROUTE BLOCKED / SPIN PASSPORT STILL LIVE / NO CREDIT**

## Scope

Continue from `MB104-U12-BOLZA-SPIN-PASSPORT-20260917.md`.  Any dangerous realization produces a primitive birational correspondence

```text
B -> C2,
B -> C2,
```

where `C2` is the Bolza genus-two curve, both projections are finite etale of exact degree

```text
56l,
```

and the packet additionally forces the unsquared theta-characteristic equality

```text
p_2^* O_C2(w0) ~= p_1^* O_C2(w1).              (SPIN)
```

This note asks only whether the degree shape `56l` can be excluded by arithmetic commensurator/index considerations before using `(SPIN)`.

## 1. Bolza quaternion algebra is split at every non-dyadic finite prime

Katz--Katz--Schein--Vishne describe the arithmetic quaternion algebra `D_B` of the Bolza surface over

```text
K = Q(sqrt(2)).
```

Their Proposition 5.5 states that `D_B` ramifies at the unique prime `(sqrt(2))` above `2` and is split at every other nonarchimedean place.

Thus every prime ideal

```text
pfrak not dividing (sqrt(2))
```

is a good split place for the local `PGL_2` Hecke/Bruhat--Tits correspondence.

## 2. Good-prime Hecke degree

At such a split prime ideal `pfrak`, the local Bruhat--Tits tree has

```text
N(pfrak)+1
```

neighbors at each vertex.  Equivalently the standard prime Hecke double coset gives an equal-degree correspondence of bidegree

```text
(N(pfrak)+1, N(pfrak)+1).
```

This is the quaternionic Shimura-curve analogue of the usual prime Hecke correspondence.  Only this degree statement is used here.

## 3. Infinitely many Hecke degrees are exact multiples `56l`

Choose a rational prime

```text
p == 55 (mod 56).
```

Then

```text
p == 7 (mod 8),
```

so the quadratic reciprocity formula for `2` gives

```text
(2/p)=+1.
```

Hence `p` splits in `K=Q(sqrt(2))`.  In particular there is a prime ideal `pfrak` of `O_K` with

```text
N(pfrak)=p.
```

Since `p` is odd, `pfrak` is not the unique ramified dyadic prime of `D_B`, so the good-prime Hecke correspondence exists and has degree

```text
N(pfrak)+1 = p+1 = 56l,
l=(p+1)/56.
```

Dirichlet's theorem gives infinitely many rational primes in the progression

```text
p == 55 (mod 56),
```

because `gcd(55,56)=1`.

Therefore there are infinitely many arithmetic good-prime correspondence degrees of the **exact same numerical form** required by MB104:

```text
56l.
```

## 4. Consequence

The subroute

```text
Bolza arithmetic commensurator
-> allowed correspondence degree/index spectrum
-> hope that 56l is eventually impossible
```

is false.

So U12 does **not** yield U4 from degree/index arithmetic alone.  The load-bearing new datum is precisely the packet-sensitive unsquared condition

```text
p_2^* O_C2(w0) ~= p_1^* O_C2(w1),
```

possibly together with the exact `000707` node/stabilizer passport.

The current U12 split is therefore

```text
U12-DEGREE-INDEX : BLOCKED / DOMINATED;
U12-SPIN         : LIVE_UNTESTED.
```

## 5. Spin warning

One must not assume that the relevant odd theta characteristic is automatically invariant under all Bolza symmetries.  Kallel--Sjerve's genus-two spin calculation shows that the Bolza curve has no spin structure invariant under its full conformal automorphism group: a cyclic order-four subgroup fixes two odd spin structures, while another involution exchanges them.

Thus the exact `(SPIN)` condition is a genuine finite-level restriction, not a formal consequence of full Bolza symmetry.

The next admissible target is:

```text
U12-SPIN-HECKE:
  compute the action of the relevant Bolza commensurator/Hecke double cosets
  on the six odd theta characteristics (equivalently the Weierstrass-point
  differences in J(C2)[2]) and determine whether infinitely many degree-56l
  correspondences satisfy the specified pullback equality.
```

If infinitely many do, park U12 completely.  If the spin condition excludes all but finitely many double cosets, then U12 becomes a genuine U4 finite-backend route.

## Sources

- Katz, Katz, Schein, Vishne, *Bolza Quaternion Order and Asymptotics of Systoles Along Congruence Subgroups*, especially Proposition 5.5.
- Standard unramified Hecke/Bruhat--Tits local degree `N(pfrak)+1` at a split quaternionic prime.
- Kallel--Sjerve, *Invariant Spin Structures on Riemann Surfaces*, genus-two/Bolza case.

## Firewalls

```text
U12_degree_index_large_l_bound=false
U12_spin_passport_resolved=false
U12_closes_000707=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
