# Stage33 Kummer-B — exact no-gain obstruction

Status: scratch / noncredit / no-merge. This note does not edit or promote Stage33 authority.

## Source lock and exact scope

The Stage33-13 finite-V4 Kummer source is the fixed proper invariant receiver

\[
P=\operatorname{Br}(\bar S)[2]^{G_{\mathbf Q}},\qquad \dim_{\mathbf F_2}P=10,
\]

with target \(H^1(V_4,\operatorname{Pic}(\bar S)/2)\) of dimension 75. The lane starts with one of the ten adapted source-basis directions materialized. Let \(M\subset P\) denote the source subspace already covered by that exact materialized direction. Because it is a member of the adapted basis,

\[
\dim_{\mathbf F_2}M=1,\qquad \dim_{\mathbf F_2}(P/M)=9.
\]

This statement concerns the dimension of the covered **source** subspace, not the rank or nonzeroness of its 75-entry Kummer image column.

## Admissible same-receiver basis changes

Let \(B=(b_1,\ldots,b_{10})\) be the retained/adapted basis of \(P\). Every basis redesign allowed by this lane has the form

\[
C=B A,\qquad A\in GL_{10}(\mathbf F_2).
\]

Invertibility is exactly what preserves the same receiver: \(\langle C\rangle=P\). If \(T_A:P\to P\) is the induced automorphism, then

\[
\dim T_A(M)=\dim M=1,
\qquad
\dim(P/T_A(M))=9.
\]

Therefore every basis obtained solely by an admissible invertible same-receiver change still leaves nine independent source directions outside the transported one-dimensional materialized subspace.

## Exact obstruction

**Proposition.** A receiver basis change alone cannot reduce the independent additional lift burden below nine source directions.

**Proof.** The only information being transported by a basis change is the already materialized one-dimensional source subspace. Any \(A\in GL_{10}(\mathbf F_2)\) preserves its dimension, so its quotient in the fixed ten-dimensional receiver has dimension nine. Any exact completion that obtains the remaining source values solely by adding independently materialized source directions must span that quotient, hence requires at least nine directions independent modulo the known subspace. Conversely, nine quotient-basis directions suffice abstractly. Thus the independent-direction burden is exactly nine and is invariant under all admissible same-receiver basis changes. \(\square\)

The proposition does **not** say that all representatives cost the same to construct. Degree, sparsity, height, support, or a theorem that jointly determines several directions could lower wall-clock or symbolic construction cost. Such a saving would use additional geometric/arithmetic structure, not invertible source-basis redesign by itself. No such extra relation is asserted here.

## Matrix transport formula

Let \(\kappa:P\to H^1(V_4,\operatorname{Pic}(\bar S)/2)\) be the finite-V4 Kummer restriction and write its 75x10 matrices in bases \(B\) and \(C\) as \(K_B\) and \(K_C\). From \(C=B A\) and \(\mathbf F_2\)-linearity,

\[
K_C=K_B A,
\qquad
K_B=K_C A^{-1}.
\]

Hence the inverse adapter back to the retained basis is exact for every admissible \(A\), but it does not change the codimension-nine source-information deficit.

## Checkpoint verdict

Kummer-B reaches checkpoint **(B)**:

```text
EXACT_NO_GAIN_OBSTRUCTION=true
FIXED_RECEIVER_DIM_F2=10
STARTING_MATERIALIZED_SOURCE_DIM_F2=1
UNMATERIALIZED_QUOTIENT_DIM_F2=9
MIN_ADDITIONAL_INDEPENDENT_SOURCE_DIRECTIONS_UNDER_BASIS_CHANGE_ONLY=9
SAME_RECEIVER_BASIS_CHANGE_CAN_REDUCE_THIS_COUNT=false
CHEAPER_REPRESENTATIVE_SEED_PROVED=false
AUTHORITY_CREDIT=false
MAIN_STATE_EDITED=false
MERGE_ALLOWED=false
```

This closes only the lane question "can an invertible same-receiver basis redesign itself reduce the independent lift count?" It does not close the 75x10 Kummer matrix, produce the remaining nine columns, or alter MAIN V36/Stage33 authority.