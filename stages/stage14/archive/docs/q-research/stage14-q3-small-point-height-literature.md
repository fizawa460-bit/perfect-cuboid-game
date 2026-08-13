# Stage14-q3 — Small-point / First-point Height Literature Pass

## Status

```text
STAGE14_Q3=COMPLETE_SMALL_POINT_FIRST_POINT_HEIGHT_LITERATURE_PASS
TRIGGER_STAGE=Stage14-s3 / Stage14-4ar
EXACT_OBSTRUCTION=uniform lower-tail count for the least non-torsion canonical height in the Pythagorean full-2-torsion family
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
DIRECT_FAMILY_INVARIANT_REDUCTION_COUNT=1
PRIMARY_TRANSFER_ARCHITECTURE=LE_BOUDEC_2018_LARGE_PRIME_PLUS_COMPLETE_2_DESCENT
PETSche_NACCARATO_ROLE=FIXED_FIBER_HEIGHT_AND_MULTIPLICITY_CONTROL_NOT_FAMILY_LOWER_TAIL
AMBIENT_LANG_DENSITY_ONE_THEOREM_DIRECTLY_TRANSFERABLE=false
NEXT_Q_STAGE=Stage14-q5 K3/lattice computational refresh
```

## 1. Exact Stage14 target

Merged Stage14-s3 proves the necessary condition

```text
physical hit d <= B
  => non-torsion P in E_F(Q)
  => hhat(P) <= C_phys (log B + log H)
```

for the Pythagorean first-face family

```text
F=(S,X,H),  S^2+X^2=H^2,  gcd(S,X)=1,
E_F: W^2 = Z(Z-S^2)(Z+X^2).
```

Merged Stage14-4ar packages the true family statistic as

```text
lambda(F) = min{ hhat(P): P in E_F(Q) non-torsion },
h_{B,C}(F)=1_{lambda(F) <= C(log B+log H(F))}.
```

The required theorem is not a per-curve point count. It is a **moving-family lower-tail estimate** for the event that `lambda(F)` falls inside this physical logarithmic window.

## 2. Stage14-specific invariant audit

Write the integral model as

```text
W^2 = Z^3 + (X^2-S^2) Z^2 - S^2 X^2 Z.
```

A direct invariant calculation gives

```text
c4 = 16(S^4 + S^2 X^2 + X^4),
Delta_model = 16 S^4 X^4 H^4.
```

This recovers the exact discriminant already locked in Stage14-s1.

Because `(S,X,H)` is a primitive Pythagorean triple, the three integers are pairwise coprime. For every odd prime `p | SXH`, the factor

```text
S^4 + S^2 X^2 + X^4
```

is nonzero modulo `p`:

- if `p|S`, it is `X^4 mod p`;
- if `p|X`, it is `S^4 mod p`;
- if `p|H`, then `S^2=-X^2 mod p`, so it is again `X^4 mod p`.

Hence `v_p(c4)=0` at every odd bad prime. The displayed integral model is therefore minimal there and has multiplicative reduction. Consequently

```text
v_p(Delta_min)=4 v_p(SXH),
f_p(N_E)=1                         (odd p | SXH).
```

Thus the odd conductor/discriminant interface is exact:

```text
N_E,odd = rad((SXH)_odd),
|Delta_min|_odd = ((SXH)_odd)^4.
```

The prime 2 is deliberately not overclaimed here. Its conductor exponent is locally bounded, but the exact minimal discriminant valuation should be treated by the existing Stage14 Q2/Tate-algorithm machinery if a sharp global constant is ever needed.

### Immediate Szpiro consequence

Ignoring only the unresolved exact 2-adic normalization, the family Szpiro ratio is controlled by the radical defect of the Pythagorean product:

```text
sigma(E_F) = log|Delta_min| / log N_E
          <= (4 log(SXH)+O(1)) / log rad((SXH)_odd).
```

Therefore the height literature naturally splits the family according to the radical ratio

```text
R(F)= log rad((SXH)_odd) / log(SXH).
```

This is a useful exact Stage14 reduction even though it does not by itself prove a small-point saving.

## 3. Petsche — NEAR, but insufficient alone

**Primary source.** Clayton Petsche, *Small rational points on elliptic curves over number fields*, arXiv:math/0508160.

Petsche proves a non-torsion canonical-height lower bound with polynomial dependence on the Szpiro ratio. Naccarato, Proposition 4.4, imports it over `Q` and records the convenient weakened form

```text
hhat(P) > log|Delta_min| / (c sigma^8)
```

for an absolute effective constant `c`.

Combining this with the Stage14 invariant audit gives, schematically,

```text
lambda(F)
  >= c^-1 log|Delta_min(F)| / sigma(F)^8
  >= log((SXH)_odd) * R(F)^8 / O(1).
```

So on a radical-rich subfamily `R(F)>=rho>0`, Petsche gives

```text
lambda(F) >= c_rho log H
```

up to absolute/family normalization constants.

### Why this does not close Stage14

The physical admission window is itself logarithmic:

```text
lambda(F) <= C_phys(log B+log H).
```

A lower bound of order `log H` does not produce a power-saving count of admitted fibers unless one proves a quantitative constant separation and controls the range `H << B`. No such separation is presently available.

**Classification:** `NEAR` for per-fiber height control; **not a family lower-tail theorem**.

## 4. Naccarato — DIRECT fixed-fiber multiplicity tool, not the missing frequency theorem

**Primary source.** Francesco Naccarato, *Counting rational points on elliptic curves with a rational 2-torsion point*, arXiv:2105.04032 / Rend. Lincei Mat. Appl. 32 (2021).

Theorem 1.1 gives a subpolynomial-in-height bound for rational points on a fixed elliptic curve with rational 2-torsion. The proof uses 2-isogeny descent, a rank bound in terms of the discriminant, and Petsche's smallest-height lower bound.

Stage14 curves have full rational 2-torsion, so the structural hypothesis is stronger than required.

### Correct Stage14 role

Naccarato can control how many bounded-height rational points one **already-admitted fiber** can contribute. That is useful for multiplicity bookkeeping.

But Stage14 counts bases `F`, one base at a time. It needs to show that few positive-rank fibers possess *any* point in the physical window. A uniform fixed-fiber bound

```text
# {P in E_F(Q): h(P)<=L}
```

does not itself bound

```text
# {F: lambda(F)<=L(F)}.
```

**Classification:** `DIRECT` only as a fixed-fiber multiplicity subroutine; `BLOCKED` as a replacement for the lower-tail theorem.

## 5. Le Boudec 2019 ambient Lang-statistics theorem — strong analogy, structural mismatch

**Primary source.** Pierre Le Boudec, *A statistical view on the conjecture of Lang about the canonical height on elliptic curves*, arXiv:1902.08435.

Theorem 1 proves a strong Lang-type lower bound on a density-one subfamily of **all** positive-rank elliptic curves ordered by the standard elliptic-curve height, with exponent parameter `c<7/24` in the paper's exponential-minimum-height normalization.

The proof architecture is especially informative:

1. discard the ambient curves whose discriminants have too large a square factor;
2. compare Weil and canonical heights using local heights;
3. reduce anomalously small points to a Diophantine/congruence counting problem;
4. use analytic bounds for the remaining congruence problem.

### Literal transfer fails

The first ambient-family step is anti-matched to Stage14. Here

```text
Delta_model = 16(SXH)^4,
```

so the discriminant is structurally fourth-powerful rather than generically close to squarefree. Stage14 is also an extremely thin two-parameter Pythagorean subfamily, not a positive-density subfamily of all `(A,B)` Weierstrass coefficients.

Therefore the density-one theorem cannot be restricted to Stage14 by a density argument.

### What survives

The **architecture** remains valuable. Stage14 should replace "squarefree discriminant" by its exact conductor/radical parameter `R(F)` and then count anomalously small points directly in Pythagorean / split-2-descent coordinates.

**Classification:** `NEAR` as proof architecture; `BLOCKED` as a theorem import.

## 6. Le Boudec 2018 congruent-number lowest-point theorem — highest-priority transfer architecture

**Primary source.** Pierre Le Boudec, *Height of rational points on congruent number elliptic curves*, arXiv:1802.07136.

The paper proves a strong lower bound for the lowest non-torsion rational point for a positive proportion of squarefree congruent-number twists. PR #185 already extracted the two-step mechanism to test rather than importing the theorem blindly:

1. keep a quantitatively large parameter population possessing a uniquely identifiable large prime factor;
2. feed that prime into the complete 2-descent equations and count the divisor variables supporting an anomalously small point.

This is much closer to the actual Stage14 requirement than a generic fixed-fiber height inequality because it is a **frequency theorem for least points across a moving family**.

### Stage14 dictionary

The primitive Euclid parametrization is

```text
S=m^2-n^2,
X=2mn,
H=m^2+n^2,
```

and Stage14-s5a already shows that the moving descent support lies in

```text
m, n, m-n, m+n, m^2+n^2
```

plus 2.

The exact s1 split-cover interface is

```text
d1*u1^2 - d2*u2^2 = S^2,
d3*u3^2 - d1*u1^2 = X^2,
d1*d2*d3 = square class.
```

Therefore the correct Le-Boudec-style Stage14 experiment is not "apply the congruent-number theorem". It is:

- choose one of the five Euclid factors carrying a unique large prime `p`;
- determine which supported `d_i` must carry `p` in each local state;
- insert the physical small-height bounds on the rational point / cover variables;
- count the resulting divisor/congruence configurations;
- prove that the exceptional parameter population is `O(B^(1-delta))` or better.

This is a concrete transplant target.

### Critical mismatch

The congruent-number family is a fixed quadratic-twist family with constant `j`; Stage14 is non-isotrivial and has five correlated Euclid factors. Large-prime uniqueness, density, and the final variable count must all be re-proved.

**Classification:** `NEAR`, **highest priority for the missing height gate**.

## 7. Le Boudec 2014 quadratic-twist paper — warning / normalization

**Primary source.** Pierre Le Boudec, *Height of rational points on quadratic twists of a given elliptic curve*, arXiv:1404.7738.

The paper explicitly treats distribution of the lowest non-torsion canonical height as a deep statistic even in a one-parameter fixed-twist family, obtaining partial results rather than a universal solution.

This is useful negative calibration: Stage14 should not expect rank density, Selmer density, or a point-multiplicity estimate to automatically determine the least-point distribution.

**Classification:** `BACKGROUND / delimitation`.

## 8. Griffin--Ono--Tsai — secondary explicit lower-bound mechanism

**Primary source.** Michael Griffin, Ken Ono, Wei-Lun Tsai, *Heights of points on elliptic curves over Q*, arXiv:2007.09514.

They obtain effective canonical-height lower bounds using elliptic-curve ideal-class pairings. The lower bound depends on an auxiliary negative discriminant, class-number data, and associated curve arithmetic.

There is no current Stage14 mechanism making those auxiliary quantities uniform over primitive Pythagorean fibers, so this does not beat the Le Boudec transfer route.

**Classification:** `NEAR / secondary fallback`.

## 9. Transfer table

| Weapon | Full 2-torsion compatible | Moving-family frequency | Uses actual Stage14 height | Main missing hypothesis | q3 verdict |
|---|---:|---:|---:|---|---|
| Petsche | yes | no | canonical height yes | Szpiro/radical + constant separation | NEAR |
| Naccarato | yes | no | bounded point height | counts points per fiber, not fibers | DIRECT subroutine only |
| Le Boudec 2019 ambient Lang | not torsion-specific | yes, ambient family | canonical minimum | Stage14 is thin and discriminant is fourth-powerful | BLOCKED direct / NEAR architecture |
| Le Boudec 2018 congruent-number | yes in source family | yes | lowest non-torsion point | fixed twists vs non-isotrivial five-factor family | NEAR, highest priority |
| Le Boudec 2014 twists | yes in examples | yes/partial | lowest non-torsion point | fixed twist family | BACKGROUND |
| Griffin--Ono--Tsai | general | no | canonical height | auxiliary class-number uniformity | NEAR secondary |

## 10. Main decision

No existing theorem found in q3 can be imported unchanged to prove

```text
H_{Q,C} <= rho_ht R_Q + E_ht,
rho_ht << B^{-delta_ht}.
```

The pass nevertheless sharpens the missing height problem substantially.

### What not to do

Do **not** spend the next height-stage trying to squeeze a family power saving from Petsche alone. Even with bounded Szpiro ratio it produces the same logarithmic height scale as the physical window.

Do **not** import a density-one theorem for all elliptic curves into the Pythagorean family. The Stage14 discriminant has the special fourth-power form `16(SXH)^4`, and the parameter family is thin.

### Best human weapon to transplant

The most promising existing architecture is

```text
large prime in the moving parameter
    + exact complete 2-descent
    + small-height variable bounds
    + divisor/congruence counting.
```

Stage14 already has the two pieces that make this plausible: the five-factor Euclid support from s5a and the exact split full-2-descent equations from s1.

## 11. Recommended receiving-stage task

A future height-focused proof task should formulate a `LE_BOUDEC_TRANSFER_TEST`:

1. choose `theta>0` and define bases for which one of `m,n,m-n,m+n,m^2+n^2` has a prime divisor `p>H^theta` isolated from the other four factors;
2. prove a quantitative count for bases failing every such usable large-prime condition;
3. for each supported descent state, determine the forced location of `p` among `(d1,d2,d3)`;
4. combine the s3 physical canonical-height window with explicit rational-height bounds on the covering variables;
5. count the surviving divisor-variable configurations and test whether any fixed power saving results.

If the large-prime population itself cannot be controlled, record that as the exact height-side obstruction rather than returning to generic canonical-height inequalities.

```text
HANDOFF_HEIGHT_SIDE=LE_BOUDEC_TRANSFER_TEST_ON_FIVE_EUCLID_FACTORS
PETSche_ONLY_POWER_SAVING_EXPECTED=false
AMBIENT_DENSITY_ONE_LANG_TRANSFER_VALID=false
STAGE14_SPECIFIC_ODD_CONDUCTOR_INTERFACE_LOCKED=true
UNIFORM_SMALL_POINT_LOWER_TAIL_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
```

## Primary sources checked 2026-08-09

- Clayton Petsche, arXiv:math/0508160.
- Francesco Naccarato, arXiv:2105.04032, especially Theorem 1.1 and Proposition 4.4.
- Pierre Le Boudec, arXiv:1802.07136.
- Pierre Le Boudec, arXiv:1404.7738.
- Pierre Le Boudec, arXiv:1902.08435, especially Theorem 1 and the proof architecture described in the introduction.
- Michael Griffin, Ken Ono, Wei-Lun Tsai, arXiv:2007.09514.
