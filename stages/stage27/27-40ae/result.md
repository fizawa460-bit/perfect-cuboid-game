# Stage27-40ae — outer-U physical weighted averaging attack

```text
TASK_ID=Stage27-40ae
OWNER_STAGE=Stage27
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_ONLY
ROUTE_LABEL=T_OUTER_U_WEIGHTED_AVERAGING
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## Source boundary

Stage27-40ad closed averaging that lives only inside one fixed-`U` Gaussian residue/projective-class universe: the frozen Stage14 T receiver has `d=B^o(1)`, hence only `B^o(1)` such labels. The 40ad audit explicitly leaves one possible averaged rescue: range over a genuinely polynomial-size **outer physical family** and retain the actual physical packet weights.

Stage14 final Lemma 3.4 gives the relevant outer coordinates on the surviving nonproportional cells,

\[
U=L_x^+,\qquad V=L_x^-,\qquad (U,V)=1,
\]

and charges the primitive root-line pair support by

\[
B^{2\phi-\chi+o(1)}.
\]

On the fully balanced wall the dyadic scales of `U,V` are polynomial in `B`; thus an outer-parameter family is not automatically subpolynomial. But its cardinality is already part of the Stage14 complete-host ledger.

## 1. Outer cardinality is not a second saving

Let `P_U` denote the physical fixed-`U` packets surviving all previously charged Stage14 data, and let

\[
T_U\ge0
\]

be the actual T-route incidence count in that fiber. Let `M_U\ge0` denote the corresponding principal baseline against which the terminal prime-occupancy theorem is formulated. Then

\[
T=\sum_U T_U,\qquad M=\sum_U M_U.
\]

The fact that many `U` values occur does not imply that the mass `M_U` is spread uniformly. It may concentrate on a small subset of the available outer labels. Moreover the primitive `(U,V)` support has already been charged in Stage14 Lemma 3.4 / Proposition 3.6. Therefore multiplying the half-power ledger by an additional generic factor such as `#U^{-1}`, `#U^{-1/2}`, or a random-class heuristic would recharge already-counted support.

```text
OUTER_U_CARDINALITY_POLYNOMIAL_POSSIBLE=true
OUTER_U_SUPPORT_ALREADY_CHARGED_IN_STAGE14_HOST=true
OUTER_U_CARDINALITY_ALONE_FIXED_POWER_SAVING=false
GENERIC_CAUCHY_GAIN_FROM_NUMBER_OF_U_ALLOWED=false
```

## 2. Exact weighted exceptional-mass contract

Suppose an averaged prime theorem identifies a bad outer set `E` of `U`-fibers. A legal transfer to the physical Stage27 measure requires a bound of the form

\[
\boxed{
\sum_{U\in E} M_U
\ll B^{-\delta+o(1)}\sum_U M_U
}
\]

for some fixed `delta>0`, or the same statement with the actual physical weight naturally supplied by the theorem. An unweighted cardinality estimate

\[
|E|\ll B^{-\eta+o(1)}|\mathcal U|
\]

is insufficient unless an independent theorem also controls the fiber weights `M_U` strongly enough that the cardinality saving survives the complete Stage14 ledger.

This is the exact outer analogue of the fixed-class pushforward warning from 40ab, but now the outer universe can genuinely be polynomial-size.

## 3. Exact weighted second-moment contract

A sufficient mean-square adapter may be stated directly in physical units. For example, a theorem implying

\[
\sum_U \frac{|T_U-M_U|^2}{M_U+1}
\ll B^{-\delta+o(1)}\sum_U M_U
\]

with fixed `delta>0`, uniformly on the retained critical-wall cells and with all modulus/sector/headroom decorations matching the frozen T receiver, would make the bad physical baseline chargeable by Chebyshev/Cauchy--Schwarz. Equivalent weighted BDH/BV formulations are acceptable.

The denominator and normalization matter: a standard unweighted mean square over moduli/classes does not automatically imply this physical-fiber statement.

```text
OUTER_WEIGHTED_EXCEPTIONAL_MASS_CONTRACT_DEFINED=true
OUTER_WEIGHTED_SECOND_MOMENT_CONTRACT_DEFINED=true
STANDARD_UNWEIGHTED_BV_BDH_AUTOMATICALLY_SUFFICIENT=false
```

## 4. Interaction with the Stage14 complete host

The Stage14 whole-family proof counts the primitive `(U,V)` root-line support and later reconstructs the remaining variables with `B^o(1)` multiplicity. Thus any new averaged theorem may use `U` as an averaging parameter only if its saving is a theorem about **occupancy/discrepancy of the already-counted physical fibers**, not a new combinatorial charge for choosing `U`.

This separates two logically different quantities:

1. the number of admissible outer labels, already included in the host;
2. the distribution of prime-incidence mass across those labels, not controlled by the host.

Only (2) can still produce a new fixed-power deficit without double counting.

## Outcome

Stage27-40ae does not prove a strict sub-square-root upper bound. It narrows the surviving averaged T route to a same-measure theorem over the **outer physical U-fibers**: a fixed-power weighted exceptional-mass bound or an equivalently strong weighted second moment after the exact Stage14 decorations and capacity ledger.

No claim is made that no such external theorem exists. The repository currently supplies the host/cardinality structure, not this weighted physical discrepancy estimate.

```text
T_OUTER_U_WEIGHTED_AVERAGING_ATTACK_EXECUTED=true
OUTER_U_CARDINALITY_ALONE_ROUTE_CLOSED=true
OUTER_U_DOUBLE_CHARGE_FIREWALL=true
OUTER_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_BOUND_PROVED=false
OUTER_PHYSICAL_WEIGHTED_SECOND_MOMENT_PROVED=false
T_EXACT_REOPEN_GATE=OUTER_U_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_OR_WEIGHTED_SECOND_MOMENT
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=Stage27-audit
```
