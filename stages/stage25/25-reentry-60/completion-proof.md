# Stage25-reentry-60 completion-rate proof

STATUS=SUBMITTED_PENDING_FRESH_AUDIT
TASK_ID=Stage25-u20-r006a

## A. Exact incidence accounting

For each primitive canonical exactly-two/Euler cuboid under `R<=B`, choose a shared edge of two integral faces. In directional chamber `j` there is exactly one such incidence for an exactly-two cuboid whose unique shared edge is `j`, while every Euler cuboid contributes exactly one incidence to each `j=a,b,c` chamber.

Hence

\[
P_j=M_{2,j}+M_3,
\qquad
P=M_2+3M_3.
\]

No asymptotic enters this step.

## B. Host asymptotic

Stage18/Stage15-2b and r010a give

\[
M_{2,j}\sim C_jB(\log B)^5,
\qquad C_j>0,
\]

and Stage20 gives `M3=o(B(log B)^5)`. Therefore

\[
P_j\sim C_jB(\log B)^5.
\]

Summing yields

\[
P\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}=C_a+C_b+C_c.
\]

## C. Lower completion floor

S20-W02 supplies an explicit lower family

\[
M_3(B)\ge \left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
\]

for all sufficiently large `B`, hence `M3>>B^(1/6)`.

Since `P_j<<_j B(log B)^5` and `P<<B(log B)^5`,

\[
\Theta_j=\frac{M_3}{P_j}
\gg_j B^{-5/6}(\log B)^{-5},
\]

\[
\Theta=\frac{3M_3}{P}
\gg B^{-5/6}(\log B)^{-5}.
\]

The constants may depend on the fixed directional chamber in the first display only.

## D. Upper completion ceiling

For every fixed `eta<1/46`, S20-W01 gives

\[
M_3\ll_\eta B(\log B)^{5-\eta}.
\]

Since `P_j>>_j B(log B)^5` and `P>>B(log B)^5`,

\[
\Theta_j\ll_{j,\eta}(\log B)^{-\eta},
\qquad
\Theta\ll_\eta(\log B)^{-\eta}.
\]

Therefore all completion rates tend to zero.

## E. Directional ratio theorem

For any fixed `j,k`, the numerator cancels exactly:

\[
\frac{\Theta_j}{\Theta_k}
=\frac{M_3/P_j}{M_3/P_k}
=\frac{P_k}{P_j}.
\]

The explicit Saunderson family proves `M3(B)>0` for all sufficiently large `B`, so the ratio is eventually defined. Using the host asymptotics,

\[
\frac{P_k}{P_j}\to\frac{C_k}{C_j}.
\]

Thus

\[
\boxed{\Theta_j/\Theta_k\to C_k/C_j.}
\]

This conclusion does not assume an asymptotic law for `M3`.

## F. Object-ratio corridor

From `M2~C_M2 B(log B)^5`, the same Stage20 bounds give

\[
B^{-5/6}(\log B)^{-5}\ll M_3/M_2
\ll_\eta(\log B)^{-\eta}.
\]

This is explicitly labeled an adjacent-stratum population-size ratio. The literal completion probability is instead `Theta=3M3/(M2+3M3)`.

## G. Compatibility audit map

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
CUTOFF=R<=B
PRIMITIVE_MATCH=true
CANONICAL_MATCH=true
RAW_PAIR_MULTIPLICITY_MATCH=true
M2_OBJECT_MULTIPLICITY=1
M3_RAW_PAIR_MULTIPLICITY=3_total;1_per_direction
MEASURE_MATCH=true_on_raw_pair_incidence_host
QUANTIFIER_MATCH=true
ETA_QUANTIFIER=fix_eta<1/46_then_B_to_infinity
FINITE_DATA_USED=false
```

## H. Firewall

The K3 cover is not assigned a fake `(a,b)` difference from the host. No product of S20-W01 and S20-W03 is taken as independent saving. The local blocker remains causal/sieve input, while the thin-cover upper remains the certified quantitative ceiling.

```text
COMPLETION_PROOF_COMPLETE=true
ABSOLUTE_M3_ASYMPTOTIC_PROVED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
```
