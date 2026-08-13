# Stage13-13fa — finite directional discrepancy and leading q-independence audit

> STATUS: `STAGE13_13FA_COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT`
>
> PARENT_GATE: Stage13-13f / R05 repair plan Gate A
>
> R04: immutable
>
> THEOREM CONTRACT REOPENED: `false`
>
> NEXT: `13-13fb`

## 1. Question audited

R04 received a substantive objection that the finite exactly-one vector is still much closer to `2:1:1` than to the claimed limiting vector

```text
P_inf =
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
```

That observation requires two logically separate checks:

1. does the complete finite trajectory actually contradict, or move against, the claimed asymptotic vector?
2. is there a still-unaccounted category-dependent arithmetic factor in the leading `j=0` proof that could invalidate the common-`Theta` conclusion?

This stage audits those two questions only. It does **not** claim an effective convergence rate.

---

## 2. Finite data audited

The deterministic audit combines:

- the historical exact-one checkpoints from PR #89 at `B=1000,3000,10000,30000`;
- the active complete enumeration `100000 <= B <= 1000000`;
- the active complete enumeration `1000000 <= B <= 5000000`.

The overlapping `B=1000000` row agrees exactly between the two active reports.

At the two endpoints central to the R04 objection:

```text
B=100000
counts = (84146, 43180, 40704)

P =
(0.500779622686425,
 0.256977920609415,
 0.242242456704160)

L1(P, 2:1:1) = 0.015515086591680
L1(P, P_inf) = 0.067914621089948
```

and

```text
B=5000000
counts = (7846274, 4018971, 3708949)

P =
(0.503799682988410,
 0.258053225739979,
 0.238147091271611)

L1(P, 2:1:1) = 0.023705817456749
L1(P, P_inf) = 0.061874500485977
```

Therefore, from `100k` to `5m`:

```text
distance to exact 2:1:1 grows by factor 1.527920409...
distance to claimed limit falls to factor 0.911063030...
```

The motion is not monotone at every intermediate cutoff, so no monotonicity claim is made. But the endpoint statement is unambiguous:

```text
the finite population does not remain stationary at 2:1:1;
over the audited 100k -> 5m interval it moves away from 2:1:1
and modestly toward the claimed limiting vector.
```

Thus the finite data are **not a contradiction** to the asymptotic theorem.

---

## 3. Why the discrepancy still looks large

Use the Stage13 deviation coordinates

```text
alpha(B) = P_ab(B) - 1/2
beta(B)  = (P_ac(B)-P_bc(B))/2.
```

The claimed limits are

```text
alpha_inf = 0.034736933231399
beta_inf  = 0.012727644447951.
```

At `B=100000`:

```text
alpha = 0.000779622686425  = 2.24% of alpha_inf
beta  = 0.007367731952628  = 57.89% of beta_inf
```

At `B=5000000`:

```text
alpha = 0.003799682988410  = 10.94% of alpha_inf
beta  = 0.009953067234170  = 78.20% of beta_inf
```

So the visually persistent near-`2:1:1` behavior is concentrated mainly in the slow `alpha` coordinate: the `ac/bc` split has moved substantially toward its claimed limiting value, while the `ab` excess above one half is still small at accessible cutoffs.

This is a finite diagnostic, not a secondary asymptotic theorem.

---

## 4. Important limitation: no proved effective rate

The canonical theorem proves

```text
A_q(B)
 = Theta J_q B(log B)^3
 + o(B(log B)^3)
```

and transfers the same leading constants to exactly-one counts after the overlap estimate.

That little-`o` statement does **not** supply an explicit numerical threshold or an effective bound of the form

```text
|P_q(B)-P_q(infinity)| <= f(B)
```

usable at `B=5m`.

Therefore the present proof does not quantitatively predict the observed `100k..5m` convergence speed.

The correct closure statement is:

```text
FINITE_DATA_CONTRADICTS_THEOREM=false
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
```

R05 must state this scope explicitly. The absence of an effective rate is not itself a contradiction of an asymptotic theorem.

---

## 5. Leading q-independence retrace

The common-`Theta` proof was retraced without using the superseded Stage13-7jb categorywise constant check.

### 5.1 Primitive split-prime zero mode

Before any chamber factor or Stage12 constant enters, the primitive raw local coefficient is

```text
Z_0(a,b) =
  2b+1   if a=0
  2      if a>=1.
```

It depends on valuation data only. No canonical face label appears.

The pure one-variable factors are likewise common:

```text
A_0(s) = zeta(s) L(s,chi_4) E_h,0(s)
B_0(s) = zeta(s)^2 L(s,chi_4) E_b,0(s).
```

### 5.2 Mixed correction

The full local factor is divided by the same pure-axis factors:

```text
C_ell = D_ell / (A_ell B_ell B_ell).
```

Pure axes cancel exactly, and every nonconstant coefficient of `C_ell-1` uses at least two coordinate variables. Its top-degree contribution is therefore one common arithmetic scalar after convolution.

The explicit norm and error details are deliberately deferred to `13-13fb` and later repair gates; Gate A only checks whether a category label enters this leading arithmetic object. It does not.

### 5.3 Odd inert and 2-adic/parity factors

The active non-circular repair explicitly records the inert coprimality factors and finite OE/EE factors as category-independent arithmetic factors. They alter the common scalar, not the zero-mode category kernel.

### 5.4 Curved-region assembly

After the arithmetic coefficient system is fixed, the category enters through the archimedean zero Fourier kernel

```text
J_q = 2 I_q/pi.
```

Thus

```text
A_q^(0)(B)
 = Theta J_q B(log B)^3
 + o(B(log B)^3)
```

with one `Theta`.

### 5.5 Nonzero harmonics

Nonzero angular modes have no scale zeta pole and are lower order at the raw `B(log B)^3` scale. Therefore they cannot supply another leading category-dependent arithmetic constant.

### 5.6 Stage12 is used only afterwards

Only after the single common `Theta` has been obtained does the proof use

```text
C_prim(B)=2 sum_q A_q(B)
```

and the frozen Stage12 total theorem to determine

```text
Theta = kappa/(6 pi^2).
```

No Stage12 directional proportion is seeded upstream of commonness.

---

## 6. Gate-A decision

No leading category-dependent arithmetic factor was found in the active `j=0` proof chain.

The Claude objection is therefore split as follows:

```text
finite-data-is-a-contradiction:
  CLOSED_BY_AUDIT

missing-leading-q-dependent-factor:
  NO_DEFECT_FOUND_AT_CURRENT_PROOF_LEVEL

effective quantitative explanation of finite convergence:
  NOT SUPPLIED BY CURRENT THEOREM
```

The last item must be disclosed in R05, but it does not force the theorem contract to be reopened.

DeepSeek's explicitness objections remain active and are not silently declared repaired here.

---

## 7. Machine-readable audit

Artifacts:

```text
stages/stage13/scripts/13-13fa/q_independence_finite_audit.py
stages/stage13/data/13-13fa/q_independence_finite_audit.json
```

The audit fails if:

- the two active reports disagree at their shared `B=1m` checkpoint;
- the `100k -> 5m` endpoint facts stated above cease to hold;
- the canonical/common-factor proof loses the required non-circular common-`Theta` lock statements.

It intentionally does not turn finite agreement into mathematical evidence for the asymptotic theorem.

---

## 8. Completion lock

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
FINITE_100K_TO_5M_MOVES_AWAY_FROM_2_1_1=true
FINITE_100K_TO_5M_ENDPOINT_DISTANCE_TO_LIMIT_DECREASES=true
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
R04_REPAIR_GATE_REMAINS_BLOCKED=true
NEXT=13-13fb
```

`13-13fb` must expose the full `529 p^{-5/4}` Wiener derivation inside the R05 repair chain rather than merely citing the older repair artifact.
