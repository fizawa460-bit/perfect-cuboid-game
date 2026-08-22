# Stage29-12 — joint, local, parametric, and population-interaction attack portfolio — audited

```text
STAGE=Stage29
ITEM=29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
STATUS=AUDITED_PASS_AFTER_MATERIAL_POSITIVE_REPAIR
ATTACK_ROUTE_COUNT_RETAINED=11
NEW_ATTACK_ROUTE_CREATED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Audit verdict

The submitted route colors survive fresh audit:

```text
J12-JOINT-V4          = AMBER
J12-LOCAL-SQUARECLASS = AMBER
J12-PARAMETRIC        = AMBER
J12-POP-INTERACTION   = GREEN
```

The GREEN route is strengthened materially. The original two relative-density claims are correct, but the same certified inputs also close a larger exact incidence/nested-host survival ladder.

## 2. Exact object/cutoff identification behind the GREEN route

Stage14's raw unordered two-face incidence graph and Stage29's selected-two-face incidence are the same object on the integral-space locus.

Stage14:

```text
E(B)=N2(B)+3T(B).
```

Gap Scan B proves object-for-object

```text
T(B)=P(B),
R=d on the endpoint,
```

under the same primitive canonical convention `0<a<b<c`, `gcd(a,b,c)=1` and the same physical cutoff.

Stage29-07 proves

```text
I2^S=N2+3P.
```

The coefficient `3` is selected unordered two-face incidence multiplicity for a triple-face object, not V4 sheet multiplicity. Hence

```text
Stage14 E(B)=Stage29 I2^S(B)
```

exactly.

The frozen Stage14 proof therefore gives, for every `epsilon>0`,

```text
I2^S(B) <<_epsilon B^(1/2+epsilon).
```

No hidden exact-two filter, ordered-pair factor, primitive rescaling, canonical permutation factor, or height loss appears.

## 3. Material positive repair — exact incidence survival ladder

Stage29-07 gives

```text
I1   = M1+2M2+3M3,
I1^S = N1+2N2+3P,
I2   = M2+3M3,
I2^S = N2+3P,
I3   = M3,
I3^S = P.
```

Stage29-04 gives

```text
M1 ~ (3/(4*pi^2))*B^2*log B,
N1 ~ (kappa/(24*pi))*B*(log B)^3,
M2 ~ C_M2*B*(log B)^5,  C_M2>0,
M2=o(M1),
M3=o(M2),
B^(1/4) << N2 <<_epsilon B^(1/2+epsilon).
```

Gap Scan B gives

```text
P <<_epsilon B^(1/2+epsilon).
```

Choose any fixed `epsilon<1/2` when comparing with `N1`. Then `N2,P=o(N1)` and therefore

\[
\boxed{
\frac{I_1^S(B)}{I_1(B)}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
}
\]

For selected two-face incidences, the Stage14 upper and the certified `N2` lower give the full corridor

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
\frac{I_2^S(B)}{I_2(B)}
\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

Hence `I2^S/I2 -> 0`.

The final selected-three-face incidence remains

```text
I3^S/I3=P/M3,
```

whose global scale is still unknown.

```text
R29-POP-I1S=DISCHARGED_EXACT_ONE_FACE_INCIDENCE_SPACE_SURVIVAL_ASYMPTOTIC
R29-POP-I2S=DISCHARGED_SELECTED_TWO_FACE_SPACE_SURVIVAL_CORRIDOR
P_OVER_M3_SCALE_KNOWN=false
```

## 4. Material positive repair — legal nested-host survival ladder

The exact Stage29 hosts are

```text
H_ge1=M1 disjoint_union M2 disjoint_union M3,
H_ge2=M2 disjoint_union M3,
H_ge3=M3,
```

with space intersections

```text
S cap H_ge1=N1 disjoint_union N2 disjoint_union P,
S cap H_ge2=N2 disjoint_union P,
S cap H_ge3=P.
```

Because `M2,M3=o(M1)` and `N2,P=o(N1)`, the first literal nested survival ratio has the exact asymptotic

\[
\boxed{
\frac{N_1+N_2+P}{M_1+M_2+M_3}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
}
\]

For the at-least-two-face host, the lower bound comes from `N2` and the upper from `N2+P`:

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
\frac{N_2+P}{M_2+M_3}
\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

Thus the space-diagonal condition has density zero on the full legal `H_ge2` host.

The endpoint itself satisfies the stronger-subset upper bound

\[
\boxed{
\frac{P(B)}{M_2(B)+M_3(B)}
\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

But the last literal survival step is still

```text
(S cap H_ge3)/H_ge3=P/M3,
```

and remains globally unknown.

```text
R29-POP-H1S=DISCHARGED_SPACE_SURVIVAL_ASYMPTOTIC_ON_H_GE1
R29-POP-H2S=DISCHARGED_SPACE_SURVIVAL_CORRIDOR_ON_H_GE2
R29-POP-H2=DISCHARGED_ENDPOINT_DENSITY_ZERO_IN_H_GE2
```

These are density/survival theorems, not emptiness or nonexistence theorems.

## 5. J12-JOINT-V4 — AMBER

The exact residual cells remain

```text
third NO,  space NO  : M2-N2
third NO,  space YES : N2
third YES, space NO  : 3*(M3-P)
third YES, space YES : 3P.
```

The new whole-column and nested-host bounds do not determine a genuinely joint final conditional. In particular neither

```text
P/M3
```

nor

```text
3P/(N2+3P)
```

has a nontrivial certified asymptotic scale.

`R29-X1` remains `OPEN_BOUNDED_GLOBAL_ADE_ENUMERATION`; closing the ADE ledger alone would not exclude endpoint rational points.

```text
J12-JOINT-V4=AMBER_EXACT_JOINT_MODEL_NO_JOINT_ENDPOINT_OBSTRUCTION
```

## 6. J12-LOCAL-SQUARECLASS — AMBER with p=2 child discharged

29-09's exact odd-prime laws are consumed without new credit. No physical-height/equidistribution transfer closing `R29-KUM-LOC3` was found downstream.

At

```text
[x:y:z]=[44^2:117^2:240^2]
```

the seven F7 branch values are exactly

```text
1936, 13689, 57600, 15625, 59536, 71289, 73225.
```

The first six are rational squares. The last satisfies

```text
73225 == 1 (mod 8),
```

so it is a nonzero square in `Q2`. Since `Q2^{*2}` is open and all seven forms are nonzero, the simultaneous all-square locus contains a nonempty Q2-open projective neighbourhood and hence has positive Haar measure.

Therefore

```text
R29-KUM-LOC2-2A=DISCHARGED_POSITIVE_Q2_LIFT_CYLINDER
R29-KUM-LOC2-2=OPEN_EXACT_TWO_ADIC_STATE_DENSITY
R29-KUM-LOC3=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER
J12-LOCAL-SQUARECLASS=AMBER_EXACT_LOCAL_DATA_NO_GLOBAL_TRANSFER
```

Positive local measure is not an exact Q2 density and not a global rational-point theorem.

## 7. J12-PARAMETRIC — AMBER

29-08's independently audited proof that every primitive Euler brick is represented after gcd normalization by a Master-Hit remains the global coverage input and is not re-credited.

Fresh current-source review of `arXiv:2605.00573v1` confirms that the universal exponent-one assertion is still explicitly `Conjecture 4.1`, finitely verified on the database, with its proof left open.

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER
PESCH_E1_IF_PROVED_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=true
PESCH_E1_CURRENTLY_PROVED=false
```

Bounded Mordell-Weil enumeration remains non-exhaustive and the parameter-height/multiplicity adapters remain open.

```text
J12-PARAMETRIC=AMBER_GLOBAL_COVERAGE_WITH_CONJECTURAL_DECISIVE_BLOCKER
```

## 8. Final portfolio classification

```text
J12-JOINT-V4          = AMBER
J12-LOCAL-SQUARECLASS = AMBER
J12-PARAMETRIC        = AMBER
J12-POP-INTERACTION   = GREEN

GREEN_ROUTE_COUNT_29_12=1
AMBER_ROUTE_COUNT_29_12=3
ATTACK_ROUTE_COUNT_RETAINED=11
```

The GREEN credit is for the new certified normalized incidence/nested-host survival theorems. It does not re-credit the Stage14 upper bound itself.

## 9. Handoff

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
MATERIAL_POSITIVE_REPAIR=NESTED_HOST_AND_INCIDENCE_SPACE_SURVIVAL_LADDER_PLUS_Q2_POSITIVE_CYLINDER_CERTIFICATION
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=GAP_SCAN_C_ROADMAP_REVIEW_C
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
