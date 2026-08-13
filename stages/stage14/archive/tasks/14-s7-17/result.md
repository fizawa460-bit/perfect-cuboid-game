# Stage14-s7-17 — projective slope reduction of the centered split-k dispersion

## Status

`COMPLETE_PROJECTIVE_SLOPE_REDUCTION_AND_ALIAS_FREE_CENTERED_TRANSFER`

Stage14-s7-16 proved exact inert-prime Fourier self-duality for the split-`k` quartic

```text
F_(A,B0)(r,s)=A s^4-B0 r^4,
A=k_+^2,
B0=k_-^2,
```

and showed that modulus-by-modulus absolute completion destroys the diagonal subtraction needed by the s-route.  Stage14-s7-17 keeps the subtraction, uses the critical `k`-shell geometry, and reduces the remaining two-dimensional dual-frequency object to a one-dimensional projective-slope dispersion with an injective physical selector.

No new whole-family power saving is claimed.  The unconditional exponent remains `7/8`; the `6/7` line remains conditional.

---

## 1. Fixed split-k block and coordinate determinant

Fix a parity/split block

```text
g in {1,2},
k=k_- k_+,
gcd(k_-,k_+)=1,
(Q-P)/g = k_- r^2,
(Q+P)/g = k_+ s^2.
```

Write the reduced-coordinate cap as

```text
0<P<Q<=X,
X<=B^(1/2+o(1)).
```

Then

```text
r <= (X/k_-)^(1/2),
s <= (2X/k_+)^(1/2).
```

Hence for two states `(r1,s1),(r2,s2)` in the same split block,

```text
|r1 s2-r2 s1|
 <= 2 max(r) max(s)
 <= 2 sqrt(2) X/sqrt(k).
```

On the only `7/8`-critical residual, merged 4cc/s7-16 give

```text
k>=B^(3/4-o(1)).
```

Therefore

```text
boxed:
|r1 s2-r2 s1| <= B^(1/8+o(1)).
```

This determinant scale is strictly smaller than an auxiliary inert prime

```text
p~B^rho
```

whenever

```text
rho>1/8.
```

For the concrete conditional amplifier `rho=1/7`, the exponent margin is

```text
1/7-1/8 = 1/56.
```

---

## 2. Primitive slopes and no projective alias

Because

```text
gcd((Q-P)/g,(Q+P)/g)=1,
```

we also have

```text
gcd(r,s)=1.
```

Let `p` be an inert auxiliary prime, `p=3 mod 4`, satisfying the usual good-prime conditions and in particular `p not| s A B0`.  Define the projective slope

```text
t_p(r,s) = -r s^(-1) mod p.
```

If two states in the same split block have equal slope modulo `p`, then

```text
p | r1 s2-r2 s1.
```

For `rho>1/8`, the determinant bound above is eventually smaller than `p`, so

```text
r1 s2-r2 s1=0.
```

Both pairs are primitive and positive, hence

```text
(r1,s1)=(r2,s2).
```

Thus:

```text
boxed:
critical fixed-split slope map (r,s) -> t_p is injective
for every good p~B^rho with rho>1/8.
```

For two distinct good inert primes `p,q`, the CRT slope

```text
t_pq(r,s) mod pq
```

is injective as well.

This removes projective residue alias as a possible source of the remaining centered dispersion.

---

## 3. Exact one-dimensional character reduction

Let

```text
m=pq
```

with distinct inert good primes.  For a good state, `s` is invertible modulo `m`, and

```text
F(r,s)=s^4 (A-B0 t_m(r,s)^4) mod m.
```

Since `s^4` is a square,

```text
boxed:
chi_m(F(r,s)) = chi_m(A-B0 t_m(r,s)^4).
```

Therefore the two-prime split-`k` sum

```text
S_m = sum_(z in Z_m) chi_m(F(z))
```

is exactly

```text
boxed:
S_m = sum_(t in T_m) chi_m(A-B0 t^4),
```

where `T_m` is the reduction of the physical primitive rational slopes in the fixed split block.  By Section 2,

```text
#T_m = H_m:=#Z_m
```

and its indicator is `0/1`.

Thus the 2D Fourier receiver from s7-16 has an exact 1D projective form on the critical physical family.

---

## 4. Complete projective trace

For every inert prime `p` with `p not| A B0`, both `A` and `B0` are nonzero squares modulo `p`.  The s7-16 quartic trace gives

```text
sum_(t mod p) chi_p(t^4-c)=-1.
```

Since `chi_p(-B0)=-1`, it follows that

```text
boxed:
sum_(t mod p) chi_p(A-B0 t^4)=1.
```

For `m=pq`, CRT therefore gives

```text
boxed:
sum_(t mod m) chi_m(A-B0 t^4)=1.
```

The complete projective mean is exactly `1/m`, not an uncontrolled main term.

---

## 5. Centered slope selector and exact energy

Let

```text
nu_m(t)=1_(t in T_m),
H_m=#T_m,
b_m(t)=nu_m(t)-H_m/m.
```

Then

```text
sum_t b_m(t)=0.
```

Because the slope map is injective,

```text
nu_m(t) in {0,1},
```

and therefore

```text
boxed:
||b_m||_2^2 = H_m-H_m^2/m.
```

Set

```text
X_m(t)=chi_m(A-B0 t^4).
```

Using the complete trace from Section 4,

```text
boxed:
S_m = <b_m,X_m> + H_m/m.
```

So the physical selector has been converted into a mean-zero `0/1` projective selector with exact near-linear energy.

No arbitrary sparse-selector loss is introduced in this reduction.

---

## 6. The diagonal subtraction survives projectivization

On the good core, every selected `F(z)` is nonzero modulo `m`, hence the state diagonal is

```text
D_m=H_m.
```

Put

```text
Y_m=<b_m,X_m>,
mu_m=H_m/m.
```

Then

```text
|S_m|^2-D_m
 = (|Y_m|^2-||b_m||_2^2)
   + 2 mu_m Re(Y_m)
   + H_m^2/m^2-H_m^2/m.
```

Moreover

```text
||b_m||_1 = 2H_m(1-H_m/m) <= 2H_m,
```

so `|Y_m|<=2H_m`.  Hence the difference between the original centered term and the centered projective projection is bounded by

```text
boxed:
| (|S_m|^2-H_m) - (|Y_m|^2-||b_m||_2^2) |
 <= 6 H_m^2/m.
```

This is the key s7-17 transfer: the subtraction is preserved before absolute values, with only a deterministic `H_m^2/m` correction.

For primes `p,q~L`, `m~L^2`, and an amplifier of `M=L^(1+o(1))` primes,

```text
sum_(p!=q) H_m^2/(pq)
 <= H^2 (sum_p 1/p)^2
 = H^2 B^o(1),
```

which is below the desired centered scale

```text
H^2 M B^o(1).
```

Thus the complete-trace mean correction is harmless after the prime-pair average.

---

## 7. What is now closed

The following possible obstructions are no longer live on the critical fixed-split block:

1. **2D local Fourier loss** — closed by s7-16 exact self-duality.
2. **projective residue alias** — closed here for `rho>1/8`.
3. **large slope-selector L2 energy** — closed exactly:
   `||b_m||_2^2=H_m-H_m^2/m`.
4. **complete projective mean** — exact trace `1`, producing only `H_m/m`.
5. **loss of the state-diagonal subtraction under dualization** — closed up to the harmless `O(H_m^2/m)` correction.

The conditional `rho=1/7` amplifier lies safely inside the alias-free regime.

---

## 8. The live theorem is one-dimensional and modulus-coherent

After removing the already-controlled prime diagonal `p=q`, the remaining theorem is equivalent, up to the harmless correction above, to

```text
ProjectiveCenteredSlopeDispersion:

sum_(p!=q)
(
  | < b_pq, chi_pq(A-B0 t^4) > |^2
  - ||b_pq||_2^2
)
 << H^2 M B^o(1).
```

The selectors `b_pq` are not arbitrary functions.  They are the CRT reductions of one fixed set of primitive rational slopes

```text
-r/s,
```

with cross-determinant size

```text
|r1 s2-r2 s1| <= B^(1/8+o(1)).
```

This modulus coherence is the remaining physical input that a successful dispersion theorem must exploit.

A Cauchy estimate on each modulus is still useless: it replaces the character covariance by the full slope-space size `m` and loses the prime-average gain.  Likewise, collapsing ordered state pairs to squareclass/product-kernel coefficients before exploiting the rational-slope geometry reintroduces the same principal collision energy being estimated.

So s7-17 does **not** claim the projective centered theorem; it identifies its exact coefficient space and removes the alias/mean/diagonal bookkeeping around it.

---

## 9. Relation to tH/toolbox lines

Merged tH14 R2 remains reference-only for the s-route.  Its unresolved `PhysicalWeightedSquareclassFiberEnergy` is not imported.

Merged toolbox-an independently identifies the intersection of critical `(xi,k)` collision and selector-sensitive dispersion.  The projective reduction above gives a concrete s-route interface for that intersection, but s7-17 does not edit toolbox canonical files and does not require a new H line.

```text
TH15_NEEDED=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14=false
```

---

## 10. Quantitative ledger

Critical split-`k` source size:

```text
H_k <= B^(1/8+o(1)).
```

Projective determinant scale:

```text
Delta_slope <= B^(1/8+o(1)).
```

Concrete auxiliary prime scale:

```text
p~B^(1/7),
1/7-1/8=1/56>0.
```

Hence a **single** auxiliary prime is already large enough to eliminate projective alias; the product `pq` is not needed for that step.

If `ProjectiveCenteredSlopeDispersion` is proved at the natural centered scale, the s7-15 amplifier ledger is unchanged and still gives the conditional whole-family bound

```text
V(B) << B^(6/7+o(1)).
```

No such theorem is proved here, so the unconditional record remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 11. Next receiver

Stage14-s7-18 should attack

```text
PrimePairProjectiveSlopeDispersion
```

directly on the modulus-coherent primitive rational slope set.  It must keep

```text
|<b_pq,X_pq>|^2-||b_pq||_2^2
```

centered through the `p,q` average and exploit the small determinant/rational-height geometry before any pair-to-squareclass collapse.

The preferred order is:

```text
fixed split-k block
-> primitive rational slopes
-> rho>1/8 no-alias
-> centered slope selectors b_pq
-> joint p,q dispersion
-> only then pair/squareclass bookkeeping.
```

---

## 12. Stage boundary

```text
STAGE14_S7_17=COMPLETE_PROJECTIVE_SLOPE_REDUCTION_AND_ALIAS_FREE_CENTERED_TRANSFER
MERGED_S7_16_IMPORTED=true
MERGED_4CC_CRITICAL_K_SHELL_IMPORTED=true
MERGED_TH14_R2_REFERENCE_ONLY=true
MERGED_TOOLBOX_AN_REFERENCE_ONLY=true
FIXED_SPLIT_K_PRIMITIVE_RS=true
CRITICAL_SLOPE_DETERMINANT_EXPONENT=1/8
PROJECTIVE_SLOPE_NO_ALIAS_FOR_RHO_GT_ONE_EIGHTH=true
CONDITIONAL_RHO_ONE_SEVENTH_ALIAS_MARGIN=1/56
TWO_PRIME_CHARACTER_SUM_REDUCED_TO_PROJECTIVE_SLOPES=true
INERT_PROJECTIVE_COMPLETE_TRACE=1
PROJECTIVE_SELECTOR_ZERO_ONE=true
PROJECTIVE_CENTERED_SELECTOR_ENERGY=H-H^2/m
CENTERED_DIAGONAL_TRANSFER_CORRECTION=O(H^2/m)
CENTERED_DIAGONAL_TRANSFER_CORRECTION_HARMLESS_IN_PRIME_PAIR_AVERAGE=true
PROJECTIVE_RESIDUE_ALIAS_OBSTRUCTION_CLOSED=true
PROJECTIVE_SELECTOR_L2_OBSTRUCTION_CLOSED=true
PROJECTIVE_COMPLETE_MEAN_OBSTRUCTION_CLOSED=true
PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_REQUIRED=true
PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_PROVED=false
DUAL_FREQUENCY_CENTERED_DISPERSION_PROVED=false
CONDITIONAL_PHYSICAL_UPPER_BOUND_EXPONENT=6/7
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH15_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH14=false
NEXT=Stage14-s7-18
```
