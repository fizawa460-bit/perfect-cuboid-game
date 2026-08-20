# Stage28-40 — Huang v3 toric growing-prime adapter

```text
TASK_ID=Stage28-40-U5/U6
STATUS=DERIVED_LITERATURE_ADAPTATION_PENDING_FRESH_AUDIT
SOURCE=Zhizhong Huang, arXiv:2111.01509v3 (17 Jul 2026)
TARGET=Stage19 space-diagonal selector on the common two-face toric host
NUMERIC_STRONGEST_N2_UPPER_IMPROVED=false
STRUCTURAL_GROWING_PRIME_GAP_IMPROVED=true
```

## 1. Why this is new relative to the frozen Stage19 interface

The frozen Stage19 local proof has the quantifier order

```text
fix finite prime set S -> B->infinity -> enlarge S
```

and therefore proves zero density but does not itself support a prime cutoff growing with `B`.

Huang v3 supplies an effective Selberg-sieve framework for rational points of bounded anticanonical height on smooth proper split toric varieties. The relevant source locators are:

- Theorem 1.4: effective equidistribution with polynomial dependence on finite adelic covering level;
- Theorem 3.11 / Corollary 3.13: Selberg sieve for local conditions detected modulo a uniform prime power;
- Corollary 6.2: for split toric `X`, condition (EE) holds with
  `gamma=dim X+rank Pic(X)+epsilon` and `h(B)=(log B)^(-1/2+epsilon)`;
- Theorem 1.6(1): effective logarithmic thinning for the adelic image of any generically finite cover of degree greater than one.

This v3 is a substantial revision dated 17 July 2026 and postdates the earlier StructureRadar literature campaign.

## 2. Exact host adapter

The already-audited Stage24/Stage27 geometry gives the common shared-edge two-face host

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\]

which is a smooth proper split toric surface. On the physical open set, the Euclidean radius `R` is the frozen anticanonical height. The Picard rank is `6` and the dimension is `2`.

For a Stage19 candidate write the frozen Gaussian-norm quantities

\[
A=N(mr+i ns),\qquad B_0=N(ms+i nr).
\]

(The notation `B_0` avoids collision with the height cutoff.) The exact space condition is

\[
R\in\mathbf Z
\iff
v_p(A)\equiv v_p(B_0)\pmod2
\quad\text{for every prime }p.
\]

For a good split prime `p=1 mod 4`, the frozen full parity-acceptance density is

\[
\rho_p=1-\frac4p+O(p^{-2}).
\]

## 3. A mod-p^2 bad subset contained in the true obstruction

Define the truncated bad event

\[
\mathcal B_p^{(1)}=
\{v_p(A)=1,\ v_p(B_0)=0\}
\cup
\{v_p(B_0)=1,\ v_p(A)=0\}.
\]

Every point in `B_p^(1)` fails the exact Stage19 parity condition, so every genuine Stage19 survivor lies in

\[
\Omega_p:=Y(\mathbf Z_p)\setminus\mathcal B_p^{(1)}.
\]

The event `B_p^(1)` is detected modulo `p^2`; hence its covering exponent is bounded by `p^2`, so Huang's Theorem 3.11 may be used with `n0=2` after removing finitely many bad primes.

At a good split prime the norm divisors are reduced on the toric open orbit. The part of the full parity-mismatch event having `v_p(A)>=2` or `v_p(B_0)>=2` has p-adic mass `O(p^-2)`. Therefore the frozen exact parity law gives

\[
\omega_p(\mathcal B_p^{(1)})
=\frac4p+O(p^{-2})
\qquad(p=1\bmod4).
\]

For inert primes no sieve condition is imposed. Thus the truncated system retains sieve dimension `2`: coefficient `4/p` on a density-one-half set of primes.

```text
TRUE_STAGE19_SURVIVOR_SUBSET_OF_ALL_OMEGA_P=true
LOCAL_CONDITION_DETECTED_MOD_P2=true
N0=2
TRUNCATED_REJECTION_SPLIT_PRIME=4/p+O(p^-2)
TRUNCATED_SIEVE_DIMENSION=2
```

## 4. Quantitative growing-prime consequence

For this toric surface,

```text
dim Y=2
rank Pic(Y)=6
gamma=8+epsilon
h(B)=(log B)^(-1/2+epsilon)
```

by Huang Corollary 6.2.

Using the conservative exponent from the proof/Corollary 3.13, the normalized survivor count for primes below `N` is bounded by

\[
\ll G(N)^{-1}
+N^{44+\varepsilon}(\log B)^{-1/2+\varepsilon}.
\]

The local density above and Mertens' theorem in the progression `1 mod 4` give

\[
G(N)\gg(\log N)^2.
\]

Choose

\[
N=(\log B)^\lambda,
\qquad 0<\lambda<1/88
\]

(for example `lambda=1/100`). Restoring the toric main scale `B(log B)^5`, and summing over the finitely many canonical shared-edge chambers, yields the new derived upper-sieve interface

\[
\boxed{
N_2(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}
}
\]

up to harmless fixed bad-prime/chamber constants.

This is **not** a new strongest whole-family upper: the already-certified

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]

is enormously stronger. The new theorem is useful because it removes the former theorem-species asymmetry: Stage19 now has a candidate effective growing-prime dimension-two upper sieve on the same qualitative scale as the Stage20 growing-prime dimension-two sieve.

```text
STAGE19_GROWING_PRIME_UPPER_SIEVE_DERIVED=true
STAGE19_GROWING_PRIME_UPPER_SIEVE_PENDING_AUDIT=true
STAGE19_LOCAL_UPPER_SIEVE_DIMENSION=2
STAGE20_LOCAL_UPPER_SIEVE_DIMENSION=2
CURRENT_GLOBAL_N2_UPPER_REPLACED=false
M3_OVER_N2_ORDERING_RESOLVED=false
```

## 5. Independent Huang thin-cover consequence

The Stage19 space cover and Stage20 third-face cover are each generically finite degree-two covers of the same toric base. Huang Theorem 1.6(1), applied after resolution, gives for each cover an effective positive logarithmic saving for base points lying in its adelic image:

\[
O\bigl(B(\log B)^{5-\iota}\bigr)
\quad\text{for some }0<\iota<1.
\]

A global rational lift is automatically an adelic lift, so this provides a quantitative version of the previously qualitative thin-cover zero-density route for Stage19. It still does not compare the two unknown constants `iota_sp` and `iota_face`, and it remains weaker than the frozen strongest endpoint upper theorems.

```text
HUANG_EFFECTIVE_THIN_COVER_APPLIES_TO_SPACE_COVER=true
HUANG_EFFECTIVE_THIN_COVER_APPLIES_TO_THIRD_FACE_COVER=true
COVER_LOG_SAVING_RELATIVE_ORDERING_PROVED=false
```

## 6. Scope / audit boundary

The load-bearing new adapter is the mod-`p^2` truncated bad subset. Fresh audit should independently check:

1. the good-prime reduced-divisor / `p^2` tail estimate `O(p^-2)` on the exact toric open;
2. the raw shared-edge toric host to primitive/canonical physical upper-inclusion adapter;
3. the `n0=2`, `r=6`, `dim=2` substitution into Huang Theorem 3.11/Corollary 3.13;
4. the `G(N)>> (log N)^2` deduction;
5. that this new upper-sieve theorem is not misreported as improving the certified `B^(1/2+epsilon)` global upper.

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
```