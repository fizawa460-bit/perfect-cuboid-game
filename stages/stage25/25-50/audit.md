# Stage25-50 hostile fresh audit

Status: **PASS — positive-power lower accepted**

## Scope

This is a hostile audit of the theorem-class-changing checkpoint50 claim

\[
N_2(B)\gg B^{1/4}.
\]

The audit does not treat the submission CI or literature provenance as a substitute for the Stage19 population adapter. The following points were independently attacked:

1. exact homogeneous cuboid identities;
2. physical cone and canonical ordering;
3. primitive reduction and preservation of required integer diagonals;
4. equivalence of the missing primitive face to the raw missing-face square condition;
5. squarefreeness/genus of the missing-face exception curve;
6. use of Faltings only for qualitative finiteness;
7. reduced rational-parameter count;
8. height conversion;
9. similarity multiplicity;
10. cross-stage backflow and interaction-sign consequences.

## Primary-source provenance check

Meskhishvili's first one-parameter NPC parametrization is correctly transcribed in dehomogenized form:

\[
a=16t^2(t^4-9),
\]
\[
b=(t^4-10t^2+9)(t^4+2t^2+9),
\]
\[
c=4t(t^2+3)(t^4-10t^2+9),
\]
\[
d_{ac}=4t(t^2+3)(t^4-2t^2+9),
\]
\[
d_{bc}=(t^4-1)(t^4-81),
\]
\[
d_s=t^8+46t^4+81.
\]

The Stage25 theorem does not import a counting theorem from that source; the primitive/canonical/exactly-two/height argument is repo-native.

```text
PRIMARY_SOURCE_PROVENANCE_CHECK=PASS
MESKHISHVILI_FIRST_PARAMETRIZATION_MATCH=PASS
PRIMARY_LITERATURE_USED_AS_BLACK_BOX_COUNT=false
```

## Algebraic family audit

For coprime positive `m,n`, the degree-eight homogeneous family satisfies exactly

\[
A^2+C^2=D_{AC}^2,
\qquad
B^2+C^2=D_{BC}^2,
\qquad
A^2+B^2+C^2=D^2.
\]

The fixed cone

\[
7/2<m/n<4
\]

indeed gives

\[
0<B<C<A.
\]

Hence after primitive reduction by `g=gcd(A,B,C)`, the canonical assignment is

\[
(a,b,c)=(B/g,C/g,A/g).
\]

Since `g^2` divides each squared required diagonal and the diagonals are integers, prime-by-prime valuation gives

\[
g\mid D_{AC},\quad g\mid D_{BC},\quad g\mid D.
\]

Thus primitive reduction preserves the two guaranteed integral faces and integral space diagonal.

The guaranteed canonical faces are

```text
raw AC -> canonical bc
raw BC -> canonical ab
```

so this family lies in the shared-`b` exactly-two channel once the raw `AB` face is excluded.

```text
HOMOGENEOUS_IDENTITIES_CHECK=PASS
PHYSICAL_CONE_CHECK=PASS
CANONICAL_EDGE_MAP=(a,b,c)=(B/g,C/g,A/g)
GUARANTEED_CANONICAL_FACES=ab,bc
SHARED_EDGE_CHANNEL=b
PRIMITIVE_REQUIRED_DIAGONALS_CHECK=PASS
```

## Missing-face exception audit

The remaining raw face satisfies

\[
A^2+B^2=n^{16}P(m/n),
\]

where

\[
P(t)=t^{16}-16t^{14}+316t^{12}-112t^{10}-3290t^8
-1008t^6+25596t^4-11664t^2+6561.
\]

After primitive reduction, the missing face becomes integral if and only if the raw missing face was integral: if `(A^2+B^2)/g^2` is an integer square, then `A^2+B^2` is the square of `g` times that integer; conversely raw integrality obviously descends because `g` divides both edges and the square root.

Modulo 5,

\[
P(t)=Q(t^2),
\]

with

\[
Q(u)=u^8+4u^7+u^6+3u^5+2u^3+u^2+u+1.
\]

The submitted Bezout certificate proves `gcd(Q,Q')=1` over `F_5`. Since `Q(0)=1` and characteristic 5 is not 2, a common root of `P(t)` and `P'(t)=2tQ'(t^2)` would force either `t=0` with `Q(0)=0`, impossible, or a common root of `Q` and `Q'`, also impossible. Therefore `P` is squarefree mod 5 and hence over `Q`.

The smooth projective curve

\[
w^2=P(t)
\]

has degree 16 and genus 7. Faltings is used only in its standard qualitative form: a genus-greater-than-one curve over `Q` has finitely many rational points. Thus only finitely many rational parameters in the lane make the third face rational. No effective threshold is needed for the lower bound.

```text
MISSING_FACE_PRIMITIVE_EQUIVALENCE=PASS
P_MOD5_QT2_BINDING_REQUIRED=true
Q_BEZOUT_CERTIFICATE=PASS
P_SQUAREFREE=PASS
THIRD_FACE_EXCEPTION_CURVE_GENUS=7
FALTINGS_USAGE=QUALITATIVE_FINITE_ONLY
EXACTLY_TWO_AFTER_FINITE_EXCEPTION_REMOVAL=PASS
```

## Counting and multiplicity audit

Choose

\[
m=4n-k,\qquad 1\le k<n/2,\qquad (k,n)=1.
\]

For `n>2`, reduced residues pair as `k <-> n-k`, so exactly `phi(n)/2` lie below `n/2`. Taking `n<=floor(T/4)` gives `m,n<=T` and therefore

\[
\gg \sum_{n\le T/4}\varphi(n)\gg T^2
\]

reduced rational parameters in the physical cone.

The raw space diagonal satisfies

\[
D=m^8+46m^4n^4+81n^8\le128T^8,
\]

and primitive reduction only decreases it.

A primitive canonical similarity class determines

\[
A/D=\frac{16t^2(t^4-9)}{t^8+46t^4+81}.
\]

For any fixed value this gives a nonzero polynomial equation of degree at most 8 in `t`, so each primitive canonical box has at most eight parameters in the lane.

After removing finitely many third-face exceptions, therefore

\[
N_2(B)\gg T^2\gg B^{1/4}.
\]

```text
REDUCED_PARAMETER_COUNT=T^2
HEIGHT_DEGREE=8
PARAMETER_FIBER_BOUND=8
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_LOWER_BOUND=N2(B)>>B^(1/4)
POSITIVE_POWER_EXPONENT=1/4
```

## Stage25 endpoint consequence

Using

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\]

we accept

\[
\boxed{
\frac{N_2(B)}{M_1(B)}\gg B^{-7/4}(\log B)^{-1}.
}
\]

Together with the audited upper,

\[
\boxed{
B^{-7/4}(\log B)^{-1}
\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
}
\]

The ratio still tends to zero.

## Cross-stage backflow accepted

The new numerator lower forces the algebraic lower upgrades

\[
\frac{N_2}{M_2}\gg B^{-3/4}(\log B)^{-5},
\]

\[
\frac{N_2}{N_1}\gg B^{-3/4}(\log B)^{-3}.
\]

Relative to the audited ambient space baseline `S0~B^-1`,

\[
J_2=(N_2/M_2)/S_0\gg B^{1/4}(\log B)^{-5}\to\infty.
\]

Relative to `S1=N1/M1~B^-1(log B)^2`,

\[
I=(N_2/M_2)/(N_1/M_1)\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

Therefore both previously unresolved interaction signs are now rigorously positive/divergent.

In addition, because the new family has canonical faces `ab,bc`, it proves a new directional target/channel lower

\[
\boxed{N_{2,b}(B)\gg B^{1/4}},
\]

and the corresponding Stage17 raw pair-overlap channel obeys

\[
\boxed{A_{ab,bc}(B)\gg B^{1/4}}.
\]

This does **not** prove a Stage25 directional endpoint ratio because checkpoint30's source-channel denominator adapter remains open.

```text
STAGE24_RATIO_LOWER_BACKFLOW=N2/M2>>B^(-3/4)(log B)^(-5)
STAGE23_RATIO_LOWER_BACKFLOW=N2/N1>>B^(-3/4)(log B)^(-3)
STAGE24_GLOBAL_INTERACTION_SIGN=POSITIVE_DIVERGENT
SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT
N2_B_DIRECTION_LOWER=N2,b(B)>>B^(1/4)
A_AB_BC_OVERLAP_LOWER=A_ab,bc(B)>>B^(1/4)
STAGE25_DIRECTIONAL_RATIO_PROVED=false
```

## Hostile-audit repairs

Two non-mathematical audit hardenings are required/accepted on the audited head:

1. bind the hard-coded mod-5 polynomial `Q` mechanically to the submitted missing-face polynomial `P`; the original script checked the Bezout identity for `Q` but did not itself verify the `P mod 5 = Q(t^2)` transcription;
2. restore checkpoint40's exact `upper_provenance` path instead of replacing that durable path with a prose summary.

Neither repair changes the theorem.

## Nonclaims preserved

```text
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
LOWER_EXPONENT_GREATER_THAN_ONE_QUARTER_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
PERFECT_CUBOID_CONCLUSION=false
FINITE_DATA_USED_AS_PROOF=false
```

## Verdict

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
PRIMARY_SOURCE_PROVENANCE_CHECK=PASS
EXACT_STAGE19_ADAPTER_CHECK=PASS
EXACTLY_TWO_MASK_CHECK=PASS
SQUAREFREE_GENUS7_CHECK=PASS
FALTINGS_FINITE_EXCEPTION_CHECK=PASS
PARAMETER_COUNT_CHECK=PASS
HEIGHT_CONVERSION_CHECK=PASS
BOUNDED_MULTIPLICITY_CHECK=PASS
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_EXPONENT=1/4
STAGE25_RATIO_LOWER_ACCEPTED=true
CROSS_STAGE_BACKFLOW_REQUIRED=true
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
COUNTS_RECOMPUTE_REQUIRED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #984; then Stage25-main-batch
```
