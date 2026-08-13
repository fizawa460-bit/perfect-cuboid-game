# Stage14-s7-18 — integer divisibility kills same-split collisions and isolates large split disagreement

## Status

`COMPLETE_SAME_SPLIT_COLLISION_ELIMINATION_AND_LARGE_CROSS_SPLIT_DISAGREEMENT_REDUCTION`

Stage14-s7-17 reduced the fixed split-`k` centered receiver to primitive projective slopes.  Stage14-s7-18 now imports the exact split-`k` factorization itself one step earlier and observes that, on the large `(xi,k)` shells relevant to the current `7/8` barrier, a repeated squarefree label cannot occur twice inside one fixed split at all.

More generally, for two states with the same `(xi,k)` but different allocations of the prime factors of `k` between `Q-P` and `Q+P`, the common part of the two allocations must be small.  Equivalently the product of the primes that switch side between the two states must be large.

This is an unconditional integer-divisibility statement.  It does not use the unproved prime-pair projective dispersion theorem and it does not use tH14/tH15.

The current whole-family exponent remains `7/8`: cross-split collisions are still live.  However the s7-17 fixed-split principal dispersion is no longer the minimal obstruction.

---

## 1. Exact split-k coordinates

For a reduced coordinate

```text
0<P<Q<=X,
gcd(P,Q)=1,
```

put

```text
g=gcd(Q-P,Q+P) in {1,2},
u=(Q-P)/g,
v=(Q+P)/g.
```

Then

```text
gcd(u,v)=1.
```

Write

```text
u=k_- r^2,
v=k_+ s^2,
```

with `k_-,k_+` squarefree.  Since `u,v` are coprime,

```text
gcd(k_-,k_+)=1,
gcd(r,s)=1,
k=k_- k_+=ker(Q^2-P^2).
```

Also

```text
F:=k_+^2 s^4-k_-^2 r^4
  =v^2-u^2
  =4PQ/g^2.
```

If

```text
xi=ker(PQ),
```

then there is an integer `z>0` with

```text
boxed:
F=xi*z^2.                                           (1.1)
```

Explicitly, if `PQ=xi*w^2`, then `z=2w/g`; this is integral for both parity cases.

The elementary size bounds are

```text
r^2 <= X/k_-,
s^2 <= 2X/k_+,
z^2 <= 4X^2/xi.                                    (1.2)
```

Finally every prime dividing `k` is coprime to `xi*z`: if `ell|k_-`, then `ell|u` but `ell∤v`, so `F=v^2-u^2` is nonzero modulo `ell`; the `k_+` case is symmetric.  Thus

```text
boxed:
gcd(k,xi*z)=1.                                     (1.3)
```

---

## 2. Fixed split: repeated xi forces equality once k^2 xi dominates X^4

Take two reduced states in the same fixed split

```text
(k_-,k_+)
```

with the same squarefree label `xi`:

```text
k_+^2 s_1^4-k_-^2 r_1^4 = xi z_1^2,
k_+^2 s_2^4-k_-^2 r_2^4 = xi z_2^2.                (2.1)
```

Cross multiplication gives

```text
k_+^2 (s_1^4 z_2^2-s_2^4 z_1^2)
 =k_-^2 (r_1^4 z_2^2-r_2^4 z_1^2).                (2.2)
```

Since `gcd(k_-,k_+)=1`,

```text
k_-^2 | s_1^4 z_2^2-s_2^4 z_1^2,
k_+^2 | r_1^4 z_2^2-r_2^4 z_1^2.                  (2.3)
```

By (1.2),

```text
|s_1^4 z_2^2-s_2^4 z_1^2|
 <= 32 X^4/(k_+^2 xi),

|r_1^4 z_2^2-r_2^4 z_1^2|
 <= 8 X^4/(k_-^2 xi).                              (2.4)
```

Therefore if

```text
boxed:
k^2 xi > 32 X^4,                                  (2.5)
```

both integers in (2.3) have absolute value strictly smaller than their nonzero divisors and hence both vanish.  Positivity then gives

```text
s_1^2 z_2=s_2^2 z_1,
r_1^2 z_2=r_2^2 z_1.
```

Thus

```text
r_1/s_1=r_2/s_2.
```

Both pairs are primitive positive pairs, so

```text
boxed:
(r_1,s_1)=(r_2,s_2).                               (2.6)
```

Hence:

```text
FixedSplitXiInjectivity:
if k^2 xi > 32 X^4, a fixed split (k_-,k_+) contains at most one state with a given xi.
```

No character sum or auxiliary prime is involved.

---

## 3. The current 7/8 critical shell lies deep inside the injective range

Write

```text
xi~B^gamma,
k~B^kappa,
X<=B^(1/2+o(1)).
```

Condition (2.5) is satisfied with fixed-power room whenever

```text
boxed:
2*kappa+gamma>2.                                   (3.1)
```

The merged s7-14/4cc `7/8` residual has

```text
gamma=3/4+o(1),
kappa>=3/4-o(1).
```

Therefore

```text
2*kappa+gamma
 >= 9/4-o(1),
```

leaving the exact exponent margin

```text
boxed:
9/4-2=1/4.                                         (3.2)
```

So every same-split off-diagonal `(xi,k)` collision is absent on the entire old `7/8` critical residual, not merely at the maximal-`k` endpoint of 4cd.

Consequently the s7-17 fixed-split `PrimePairProjectiveSlopeDispersion` is mathematically valid as a transfer statement but is not the minimal principal obstruction on the critical shell: the principal same-`xi` fiber in one split is already a singleton.

---

## 4. Two different splits of the same k: exact four-cell decomposition

A genuine same-`(xi,k)` collision can still use different allocations of the prime factors of `k` between the minus and plus factors.

For two states write

```text
k_{-,1}, k_{+,1},
k_{-,2}, k_{+,2},
```

with

```text
k_{-,1}k_{+,1}=k_{-,2}k_{+,2}=k.
```

Because each pair is a coprime squarefree factorization of `k`, there are unique pairwise-coprime squarefree cells

```text
alpha, beta, gamma, delta
```

such that

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
alpha*beta*gamma*delta=k.                           (4.1)
```

Interpretation:

- `alpha`: minus in both states;
- `delta`: plus in both states;
- `beta`: minus in state 1, plus in state 2;
- `gamma`: plus in state 1, minus in state 2.

Define

```text
K_agree=alpha*delta,
K_switch=beta*gamma=k/K_agree.                      (4.2)
```

The two splits are identical exactly when

```text
K_switch=1.
```

---

## 5. Same xi gives a square-divisibility system on the four k-cells

For a same-`xi` pair, (1.1) becomes

```text
(gamma*delta)^2 s_1^4-(alpha*beta)^2 r_1^4 = xi z_1^2,
(beta*delta)^2 s_2^4-(alpha*gamma)^2 r_2^4 = xi z_2^2.  (5.1)
```

Cross multiplication and grouping by the agreement cells gives

```text
delta^2(
  gamma^2 s_1^4 z_2^2-beta^2 s_2^4 z_1^2
)
=
alpha^2(
  beta^2 r_1^4 z_2^2-gamma^2 r_2^4 z_1^2
).                                                  (5.2)
```

Since `gcd(alpha,delta)=1`,

```text
alpha^2 |
  gamma^2 s_1^4 z_2^2-beta^2 s_2^4 z_1^2,

delta^2 |
  beta^2 r_1^4 z_2^2-gamma^2 r_2^4 z_1^2.          (5.3)
```

Using the state-specific bounds

```text
s_1^2 <= 2X/(gamma*delta),
s_2^2 <= 2X/(beta*delta),
r_1^2 <= X/(alpha*beta),
r_2^2 <= X/(alpha*gamma),
z_i^2 <= 4X^2/xi,
```

we obtain

```text
|gamma^2 s_1^4 z_2^2-beta^2 s_2^4 z_1^2|
 <= 32 X^4/(delta^2 xi),

|beta^2 r_1^4 z_2^2-gamma^2 r_2^4 z_1^2|
 <= 8 X^4/(alpha^2 xi).                             (5.4)
```

Hence if

```text
(K_agree)^2 xi
=(alpha*delta)^2 xi
>32 X^4,                                            (5.5)
```

both divisibility brackets vanish.

But if `beta>1`, choose a prime `ell|beta`.  The first vanishing equality gives

```text
gamma^2 s_1^4 z_2^2=beta^2 s_2^4 z_1^2.
```

The left side would then be divisible by `ell`.  This is impossible because:

- `ell|k_{-,1}` and `gcd(u_1,v_1)=1`, so `ell∤s_1`;
- `ell|k_{+,2}` and (1.3), so `ell∤z_2`;
- `ell∤gamma` by pairwise coprimality.

Thus `beta=1`.  The same argument with a prime divisor of `gamma` gives `gamma=1`.

Therefore (5.5) forces the two splits to coincide; Section 2 then forces the two states to coincide.

We have proved the stronger pair theorem:

```text
boxed:
Any off-diagonal same-(xi,k) collision satisfies
(K_agree)^2 xi <= 32 X^4.                           (5.6)
```

---

## 6. Every surviving critical collision has large split disagreement

From (5.6),

```text
K_agree <= sqrt(32) X^2/sqrt(xi).
```

Since `K_switch=k/K_agree`, every off-diagonal collision satisfies

```text
boxed:
K_switch
 >= k*sqrt(xi)/(sqrt(32) X^2).                     (6.1)
```

At exponent scale this is

```text
boxed:
log_B K_switch
 >= kappa+gamma/2-1-o(1).                          (6.2)
```

On the old `7/8` critical residual

```text
gamma=3/4+o(1),
kappa>=3/4-o(1),
```

so

```text
boxed:
K_switch >= B^(1/8-o(1)).                          (6.3)
```

Thus every critical collision must move a positive-power portion of the squarefree `k` support from `Q-P` to `Q+P` between the two states.

After merged 4cd localizes any still-`7/8` mainline endpoint to

```text
kappa=1-o(1),
```

the same formula strengthens to

```text
boxed:
K_switch >= B^(3/8-o(1)).                          (6.4)
```

This is a genuine transverse split condition, not a residue alias or local Fourier issue.

---

## 7. Why this does not yet improve 7/8 by itself

For fixed squarefree `k`, the number of coprime splits `k=k_-k_+` is

```text
2^omega(k)=B^o(1).
```

Therefore the existence of a large switching product does not by itself imply that the number of split pairs is power-small: a divisor allocation can move a large product while the total number of allocations remains subpower.

Likewise, fixed `(xi,k)` bounded-height multiplicity remains only `B^o(1)`, which is insufficient to turn a near-linear collision bound into a fixed-power saving.

So Stage14-s7-18 does **not** promote the whole-family exponent.

The new point is narrower and exact:

1. same-split collisions are completely absent in the critical region;
2. all surviving collisions are cross-split;
3. every surviving critical pair has `K_switch>=B^(1/8-o(1))`;
4. on the 4cd maximal-`k` endpoint this becomes `K_switch>=B^(3/8-o(1))`.

---

## 8. Corrected live receiver after s7-18

The s-route no longer needs a theorem for arbitrary fixed-split projective principal fibers on the critical shell.

The live object is now

```text
LargeDisagreementCrossSplitKCollision:

same xi,
same k,
different (k_-,k_+) allocations,
K_switch=beta*gamma >= B^(1/8-o(1))
```

with the exact square-divisibility constraints (5.3).

A future prime-pair/projective dispersion argument is useful only if it is extended to this **mixed-split** pair space.  Treating one fixed split at a time cannot see the surviving principal collisions.

The preferred order is now

```text
same (xi,k) pair
-> four-cell k-split comparison (alpha,beta,gamma,delta)
-> integer square-divisibility (5.3)
-> force large K_switch
-> exploit cross-split bilinear/divisor geometry
-> only then auxiliary-prime dispersion if still needed.
```

This order is compatible with merged 4cd's independent endpoint `(a,b)` versus `(k_-,k_+)` bilinear-residue direction.

---

## 9. tH / auxiliary-line decision

Stage14-t54 independently requests tH15 for the t-route `SharedUBipartiteSquareclassEnergy`.  Stage14-s7-18 does not create an additional supervisor request and does not depend on tH15.

```text
TH15_NEEDED_BY_S7_18=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
```

Merged tH14 R2 and any later tH15 result may be read as reference material, but the theorem above is elementary and self-contained.

---

## 10. Quantitative ledger

Old critical shell:

```text
gamma=3/4,
kappa>=3/4,
X exponent=1/2.
```

Fixed-split injectivity margin:

```text
2*kappa+gamma-2
 >= 2*(3/4)+3/4-2
 = 1/4.
```

Cross-split switching lower exponent:

```text
kappa+gamma/2-1
 >= 3/4+3/8-1
 = 1/8.
```

4cd endpoint switching lower exponent:

```text
1+3/8-1=3/8.
```

No new unconditional exponent is claimed:

```text
V(B) << B^(7/8+o(1)).
```

The conditional `6/7` prime-amplifier line from s7-15/s7-17 is not promoted and is no longer the preferred next step until mixed-split geometry is consumed.

---

## 11. Next receiver

Stage14-s7-19 should attack

```text
LargeDisagreementCrossSplitKCollision
```

directly.  The concrete data to preserve are

```text
alpha*beta*gamma*delta=k,
K_switch=beta*gamma,
K_switch>=B^(1/8-o(1))
```

on the old critical shell, together with the square-divisibility system

```text
alpha^2 | gamma^2 s_1^4 z_2^2-beta^2 s_2^4 z_1^2,
delta^2 | beta^2 r_1^4 z_2^2-gamma^2 r_2^4 z_1^2.
```

The first target should be a power-saving count for the cross-split pairs before introducing any new auxiliary character average.

---

## 12. Stage boundary

```text
STAGE14_S7_18=COMPLETE_SAME_SPLIT_COLLISION_ELIMINATION_AND_LARGE_CROSS_SPLIT_DISAGREEMENT_REDUCTION
MERGED_S7_17_IMPORTED=true
MERGED_S7_14_COLLISION_RECEIVER_IMPORTED=true
MERGED_4CC_K_SHELL_IMPORTED=true
MERGED_4CD_MAXIMAL_K_ENDPOINT_REFERENCE=true
SPLIT_K_EXACT_F=xi*z^2=true
GCD_K_XI_Z=1
FIXED_SPLIT_XI_INJECTIVE_IF_k2_xi_GT_32_X4=true
FIXED_SPLIT_CRITICAL_COLLISIONS_EXIST=false
FIXED_SPLIT_CRITICAL_INJECTIVITY_EXPONENT_MARGIN=1/4
CROSS_SPLIT_FOUR_CELL_K_DECOMPOSITION=true
CROSS_SPLIT_AGREEMENT_NECESSARY_BOUND=(alpha*delta)^2*xi<=32*X^4
CRITICAL_SWITCH_PRODUCT_LOWER_EXPONENT=1/8
FOUR_CD_ENDPOINT_SWITCH_PRODUCT_LOWER_EXPONENT=3/8
PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_IS_MINIMAL_OBSTRUCTION=false
LARGE_DISAGREEMENT_CROSS_SPLIT_K_COLLISION_REQUIRED=true
LARGE_DISAGREEMENT_CROSS_SPLIT_K_COLLISION_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH15_NEEDED_BY_S7_18=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14_OR_TH15=false
NEXT=Stage14-s7-19
```
