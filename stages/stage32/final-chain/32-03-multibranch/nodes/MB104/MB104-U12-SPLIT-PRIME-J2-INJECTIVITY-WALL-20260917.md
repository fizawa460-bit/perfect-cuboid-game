# Stage32 MB104 — U12 split-prime `J[2]` injectivity wall — 2026-09-17

Status: **GENERAL GOOD-PRIME LEMMA / SINGLE SPIN EQUALITY REMAINS CROSS-LEG / NO CLOSURE / NO CREDIT**

## Scope

Continue the U12 Bolza spin-passport route.  The previous dyadic note shows that the ramified place `(sqrt(2))` normalizes the Bolza local level and contributes no local index.  Nontrivial primitive arithmetic correspondence degree therefore comes from split finite places.

This note records a general fact for one good split prime and explains why a single U12 spin equality cannot be reduced to the vanishing of one `J[2]` class on one projection.

## 1. Full reduction of the Bolza group at a good prime

Let

```text
Gamma = pi_1(C2)
```

be the Bolza surface group, viewed as the normal index-24 subgroup of

```text
P Q_B^1 ~= Delta(3,3,4).
```

Let `I` be a prime ideal of `Z[sqrt(2)]` with residue field `k` of odd characteristic, prime to `6`.  Katz--Katz--Schein--Vishne prove by splitting of the quaternion order and strong approximation that

```text
P Q_B^1 / P Q_B^1(I) ~= PSL2(k).                (RED)
```

The image of `Gamma` under `(RED)` is normal because `Gamma` is normal in `P Q_B^1`.

For `|k|>=5`, `PSL2(k)` is simple (with the usual small-field exceptions absent here).  Thus the image of `Gamma` is either trivial or all of `PSL2(k)`.

It cannot be trivial: otherwise `(RED)` would factor through

```text
P Q_B^1/Gamma,
```

which has order `24`, while `PSL2(k)` has order larger than `24` for every good split prime relevant here.  Therefore

```text
rho_I: Gamma -> PSL2(k)
```

is surjective.                                            `(SURJ)`

## 2. Primitive one-prime Hecke source

For the standard elementary Hecke double coset at `I`, the canonical primitive source subgroup is the inverse image of a point stabilizer in the projective-line action:

```text
Lambda = rho_I^(-1)(Borel),
[Gamma:Lambda]=|P1(k)|=|k|+1.                  (BOREL)
```

This is the group-theoretic form of the standard prime Hecke correspondence.

## 3. Mod-two cohomology restriction is injective

Suppose a character

```text
chi in H^1(Gamma,F2)=Hom(Gamma,F2)
```

restricts trivially to `Lambda`.

Because `ker(rho_I) <= Lambda`, the character factors through `(SURJ)`:

```text
Gamma -> PSL2(k) -> F2.
```

But `PSL2(k)` has no nontrivial quotient of order two for `|k|>=5`.  Hence `chi=0`.

Therefore

```text
res : H^1(Gamma,F2) -> H^1(Lambda,F2)
```

is injective.  Equivalently for the corresponding etale projection

```text
p:B->C2,
```

```text
p^*:J(C2)[2] -> J(B)[2]
```

is injective.                                          `(J2-INJ)`

The same conclusion holds for the other leg of the primitive prime correspondence.

## 4. Consequence for the U12 spin passport

The packet requires

```text
p2^*theta0 ~= p1^*theta1
```

for two specified odd theta characteristics.  By `(J2-INJ)`, neither leg can kill a nonzero base `2`-torsion class by itself.

Thus a valid continuation may **not** argue

```text
spin equality
 -> p_i^*(nonzero delta)=0
 -> contradiction.
```

That implication is false unless one has extra equalities allowing one leg to be cancelled.  The previous fully `S4`-equivariant subclass supplied exactly such extra equalities by transporting the spin passport around the 24-element adjacent-pair orbit; that is why the equivariant subclass could be excluded.

For a general non-`S4`-invariant primitive split-prime double coset, the remaining condition is genuinely affine/cross-leg:

```text
p1^*{six odd theta characteristics}
  intersect
p2^*{six odd theta characteristics}
```

must contain the specified pair.

The linear `J[2]` pullbacks are both injective, so their relative position inside `J(B)[2]`, together with the affine spin offset, is the load-bearing object.

## 5. Refined next target

The U12 problem is now sharply isolated as

```text
U12-SPIN-TRANSFER:
  compute the relative affine position of the two six-point odd-theta
  pullback sets for a primitive split-prime Bolza Hecke correspondence.
```

Equivalent possible interfaces include:

- the spin-lift/Sergeev character of the two subgroup embeddings;
- the divisor class `p2^*(w0)-p1^*(w1)` in the Prym/new part of `J(B)`;
- the dimension of `H^0(B,p_i^*theta)` and whether the same theta characteristic can arise from both legs;
- an exact metaplectic/local-system description of the Hecke correspondence at level two.

## Source boundary

Katz--Katz--Schein--Vishne, *Bolza Quaternion Order and Asymptotics of Systoles Along Congruence Subgroups*:

- Corollary 14.2: the good-prime projective reduction is `PSL2(O_K/I)` by strong approximation;
- Lemma 14.3: for split rational primes the two algebraic-prime quotients are the two `PSL2(F_p)` congruence quotients;
- Proposition 10.3 / Corollary 10.4: `Gamma` is the normal index-24 Bolza surface subgroup.

The Borel-preimage description is the standard primitive local Hecke double-coset model at a split unramified prime.

## Firewalls

```text
good_prime_J2_pullback_injective=true
single_spin_reduced_to_one_leg_kernel=false
spin_transfer_classified=false
arbitrary_commensurator_excluded=false
U12_closes_000707=false
U12_large_l_bound_proved=false
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
