# Stage35-EX Goal4BJ source lock — support-cleaned global Gaussian quartic orientation carrier

Scope: continue Goal4BI after exact-head verification. Audited authority remains V74 / Goal4AK. Goal4BJ asks whether the Goal4BH primewise `sigma_i(ell)` bits can be assembled into one source-derived global Gaussian object while removing all non-reservoir prime-ideal support.

The answer is **yes for a global quartic orientation carrier, but no for a reciprocity obstruction**. The source-canonical `Sigma_i` and space square roots `Psi_i` admit exact Gaussian gcds that partition the reservoir primes into same-orientation, conjugate-orientation, and nonsecondary sets. Their quotient globalizes the `sigma_i` as signed valuations supported only on the selected reservoir prime ideals. Quadratic `K_2`/Hilbert data still forgets the sign; the remaining missing object is a source-derived **dual quartic character/pairing**, not support cleaning.

## 1. Input from Goal4BF/BG/BH

For direction `a`, Goal4BF has the squarefree primary reservoir kernel

```text
Sigma_a = product_{ell|s_a} pi_{a,ell},
N(Sigma_a)=s_a,
```

where `pi_{a,ell}` generates the selected Gaussian prime `p_{a,ell}`.

Goal4BG gives the primary space square root

```text
Omega_a = nu_a*Psi_a^2,
N(Psi_a)=W/h_a,                                      (BJ-Psi)
```

and Goal4BH says, at a secondary `ell|s_a`,

```text
sigma_a=-1 <=> p_{a,ell} divides Omega_a,
sigma_a=+1 <=> bar(p_{a,ell}) divides Omega_a.        (BJ-BH)
```

If the secondary condition does not occur, `ell` does not divide `W/h_a`.

Cyclic analogues hold for `b,c`.

## 2. Primary Gaussian gcds split the reservoir kernel into three source-canonical parts

Because `Z[i]` is a UFD and every prime factor of `Sigma_a` is already primary, define the unique primary associates

```text
M_a^- = gcd(Sigma_a, Psi_a),
M_a^+ = gcd(Sigma_a, bar(Psi_a)).                     (BJ-Mpm)
```

The reduced space triple is primitive, so `Psi_a` and `bar(Psi_a)` are coprime in `Z[i]`. Hence

```text
gcd(M_a^-,M_a^+)=1,
M_a^-*M_a^+ | Sigma_a.                                (BJ-coprime)
```

Define the remaining primary divisor

```text
M_a^0 = Sigma_a/(M_a^-*M_a^+).                       (BJ-M0)
```

Then exactly

```text
Sigma_a=M_a^-*M_a^+*M_a^0.                           (BJ-partition)
```

No non-reservoir Gaussian prime can enter any `M_a^*`, because all three are literal divisors of the squarefree reservoir kernel `Sigma_a`.

## 3. Primewise meaning of the partition

Fix `ell|s_a` with selected prime `p=p_{a,ell}`.

If the secondary space orientation is absent, Goal4BH gives

```text
ell does not divide W/h_a.
```

Since `N(Psi_a)=W/h_a`, neither `p` nor `bar p` divides `Psi_a`. Therefore

```text
p | M_a^0.                                            (BJ-zero)
```

If the secondary orientation is present and `sigma_a=-1`, then `p|Omega_a=nu_a*Psi_a^2`, so

```text
p | Psi_a,
p | M_a^-.                                            (BJ-minus)
```

If the secondary orientation is present and `sigma_a=+1`, then `bar p|Omega_a`, equivalently `p|bar(Omega_a)=bar(nu_a)*bar(Psi_a)^2`, so

```text
p | bar(Psi_a),
p | M_a^+.                                            (BJ-plus)
```

Because `Sigma_a` is squarefree and the three factors in `(BJ-partition)` are pairwise coprime, these cases are mutually exclusive and exhaustive.

Thus the source globally partitions the selected reservoir primes into

```text
M_a^- : secondary, sigma_a=-1,
M_a^+ : secondary, sigma_a=+1,
M_a^0 : no secondary orientation.                    (BJ-status)
```

Cyclically the same holds for `b,c`.

## 4. A support-cleaned global Gaussian orientation carrier

Define

```text
Xi_a = M_a^-/M_a^+ in Q(i)^*,
Xi_b = M_b^-/M_b^+,
Xi_c = M_c^-/M_c^+,
Xi   = Xi_a*Xi_b*Xi_c.                                (BJ-Xi)
```

The rational reservoir kernels `s_a,s_b,s_c` are pairwise coprime, so the selected Gaussian supports of the three `Xi_i` are disjoint.

At `p_{a,ell}` one has exactly

```text
v_p(Xi)=+1  if secondary and sigma_a=-1,
v_p(Xi)=-1  if secondary and sigma_a=+1,
v_p(Xi)= 0  if nonsecondary.                         (BJ-val)
```

Cyclic analogues hold.

Every finite prime-ideal valuation of `Xi` outside the selected reservoir primes is zero. Hence Goal4BI's support-cleaning problem is solved exactly by source-canonical Gaussian gcds.

Since every `M_i^+` and `M_i^-` is a product of primary primes, they are congruent to `1 mod (1+i)^3`. Their quotient is a 2-adic unit with

```text
Xi == 1 mod (1+i)^3.                                 (BJ-2clean)
```

Thus no extra finite divisor support is introduced at the ramified prime above `2`.

## 5. The quartic class records the orientation; the quadratic class does not

Local valuation in a fourth-power class is read modulo `4`. Therefore `(BJ-val)` becomes

```text
+1 mod 4  for sigma=-1,
-1 mod 4 = 3 mod 4 for sigma=+1,
0 mod 4  for nonsecondary.                            (BJ-mod4)
```

Consequently the single global class

```text
[Xi]_4 in Q(i)^*/Q(i)^{*4}                            (BJ-quartic-class)
```

recovers every Goal4BH orientation bit together with the information of whether a secondary orientation occurs.

By contrast, in the squareclass quotient

```text
+1 == -1 mod 2.
```

Hence

```text
[Xi]_2 in Q(i)^*/Q(i)^{*2}                            (BJ-squareclass)
```

cannot distinguish `sigma=+1` from `sigma=-1`. Any quadratic Hilbert/K2 pairing whose first entry factors only through this squareclass loses the orientation sign even over `Q(i)`.

Thus Goal4BI is sharpened: moving from `Q` to `Q(i)` is necessary but **quadratic** `mu_2` reciprocity is still insufficient. The surviving information is genuinely quartic.

## 6. Norm-one anti-invariant form

Define

```text
J = Xi/bar(Xi).                                       (BJ-J)
```

Then

```text
N_{Q(i)/Q}(J)=1,
bar(J)=J^{-1}.                                        (BJ-normone)
```

At a selected pair `p,bar p`, the divisor of `J` has opposite exponents. In the secondary case,

```text
sigma=-1 => (v_p(J),v_bar_p(J))=(+1,-1),
sigma=+1 => (v_p(J),v_bar_p(J))=(-1,+1).             (BJ-anti)
```

So `J` is a single global norm-one orientation carrier.

But this norm-one condition supplies no obstruction by itself: `(BJ-J)` already writes `J` explicitly as `Xi/bar(Xi)`, i.e. it is a tautological Hilbert-90 presentation. Principality/norm-one therefore imposes no new relation among the orientation bits.

## 7. Why a dual quartic character is still missing

The global carrier solves two tasks:

```text
all sigma_i globalized = yes;
non-reservoir finite support removed = yes.           (BJ-solved)
```

What it does **not** provide is a global product contradiction.

To turn `[Xi]_4` into a reciprocity obstruction one needs a source-derived dual datum, for example a fixed quartic Hilbert-symbol second entry, quartic Hecke character, or equivalent `mu_4` pairing whose local values at every selected reservoir prime have order four and therefore distinguish exponent `+1` from `-1`.

No retained identity from Goal4BF–Goal4BI supplies such a single dual character. The existing BF quartic symbols are pairwise reservoir-dependent and retain the cross-conjugate phase gauge; they do not become a fixed character of `[Xi]_4` merely because `Xi` is now global.

Therefore the global Gaussian-adapter problem is only half closed: the **carrier** exists, the **dual quartic functional** does not.

## 8. Verdict

Certified provisionally:

```text
PRIMARY_GAUSSIAN_GCD_PARTITION=true;
RESERVOIR_STATUS_PARTITION_EXACT=true;
SUPPORT_CLEANING_ADAPTER_OBTAINED=true;
GLOBAL_GAUSSIAN_ORIENTATION_CARRIER_XI=true;
GLOBAL_NORM_ONE_CARRIER_J=true;
QUARTIC_CLASS_RECOVERS_SIGMA=true;
QUADRATIC_K2_HILBERT_RECOVERS_SIGMA=false;
DUAL_QUARTIC_CHARACTER_CONSTRUCTED=false;
GLOBAL_RECIPROCITY_CONTRADICTION=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
universal sigma product;
quartic Hecke/K2 obstruction;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next unit:

```text
35EX-35_GOAL4BK_DUAL_QUARTIC_CHARACTER_COFACTOR_UNIT_PREFLIGHT
```

Question: use the complementary Gaussian face/space cofactors and BH leading units to construct a single source-derived order-four dual character of `[Xi]_4`; test whether its local values are fully controlled and whether global quartic reciprocity yields a nontrivial relation. If the source supplies no such dual functional, fail-close the Gaussian reciprocity route rather than mistaking the existence of the global carrier for an obstruction.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
