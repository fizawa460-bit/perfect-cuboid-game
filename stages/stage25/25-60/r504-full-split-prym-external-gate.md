# Stage25-60 R504 exceptional full-split Prym / E0 gate

STATUS=EXTERNAL_THEOREM_GATE_CANDIDATE_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60

This round begins from the hostile-audited PASS of PR #997:

- the complete split degree-two family is
  \[
  \phi(u)=\frac{Au^2+B}{Cu^2+D},\qquad AD-BC\ne0;
  \]
- the genus-three untwisting cover is `C: Y^2=Q(u^2)` with
  \[
  Q(x)=(Ax+B)^4+(Cx+D)^4;
  \]
- the quotient by `u -> -u` is the inherited elliptic `E0` direction;
- the complementary dimension-two Prym has
  \[
  \operatorname{Hom}_{K}(P_\eta,E_{0,K})=0,
  \qquad K=\mathbf Q(A,B,C,D),
  \]
  so an `E0` factor is not generic over the rational generic base field.

The remaining object is therefore only the exceptional rational-specialization jump locus.

## 1. Effective moduli dimension is two

The matrix
\[
M=\begin{pmatrix}A&B\\ C&D\end{pmatrix}
\]
is projective, so common scalar multiplication does not change the cover after scaling `Y`.

There is also a one-dimensional source-scaling equivalence.  Replacing
\[
(A,C)\mapsto (\lambda^2A,\lambda^2C)
\]
gives
\[
Q_{M'}(u^2)=Q_M((\lambda u)^2),
\]
so the corresponding genus-three covers and Pryms are isomorphic after `u -> lambda*u`.

Thus the full split `PGL2` parameter space has one further one-dimensional isomorphism action, leaving a generically two-dimensional Prym-moduli image (up to the finite target/source symmetries already handled in the split normal-form audit).

Two convenient generic invariants are
\[
r_1=\frac{AB}{CD},\qquad r_2=\frac{AD}{BC},
\]
where defined; both survive common matrix scaling and first-column source scaling and vary independently on a dense chart.

```text
R504_FULL_SPLIT_RAW_PGL2_DIMENSION=3
R504_FULL_SPLIT_SOURCE_SCALING_DIMENSION=1
R504_FULL_SPLIT_PRYM_MODULI_DIMENSION=2
```

## 2. Fixed-complexity E0-factor conditions are proper algebraic loci

For a positive integer complexity/isogeny degree `N`, let `Z_N` denote the locus of full-split specializations for which the Prym admits a nonzero Q-defined homomorphism to `E0` of the corresponding bounded polarization/isogeny complexity.

This is a fixed-complexity Hecke/Humbert-type algebraic condition in the moduli of principally polarized abelian surfaces.  It is proper for every fixed `N`: if one such condition contained the generic point of the full-split Prym surface, then the generic Prym would have a K-defined `E0` homomorphism, contradicting the hostile-audited PR #997 theorem.

Hence the rational exceptional locus has the form
\[
Z_{\mathrm{exc}}(\mathbf Q)
\subseteq
\bigcup_{N\ge1} Z_N(\mathbf Q),
\]
with every fixed `Z_N` proper, but with `N` unbounded.

This is the precise point where finite symbolic elimination stops being a closure mechanism: any finite cutoff `N <= N0` checks only finitely many proper loci and gives no theorem for the remaining degrees.

## 3. What repository-native work has already eliminated

The following mechanisms are already audited and are not reopened:

1. complete Q-degree-two source descent;
2. complete split normal form;
3. Q-rational reciprocal / commuting extra-involution loci;
4. explicit nonsplit rank-jump example and its second section;
5. exact mod-2 physical coset inside the known rank-two sublattice;
6. fixed-class and growing-coefficient rank-two height aggregation;
7. generic full-split Prym `E0` homomorphism over `K`.

So the remaining full-split issue is not another missing addition formula, degree cancellation, finite section search, or unexecuted source-normal-form branch.  It is the union over unbounded isogeny complexity of proper exceptional Hom/Hecke loci.

## 4. New finite-field hostile sieve — evidence only

As a targeted repo-native sanity check, the accompanying verifier enumerates every split `PGL2(F_p)` class for `p=7` and `p=11`.

For each matrix class it computes exactly:

- `#C(F_p)` and `#C(F_{p^2})` for the genus-three cover;
- `#E(F_p)` and `#E(F_{p^2})` for the elliptic quotient;
- the resulting degree-four Prym Frobenius polynomial;
- whether the supersingular `E0` Frobenius factor `1+pT^2` divides it.

The exact census is:

```text
p=7:  PGL2 classes=336,  E0-factor hits=36
p=11: PGL2 classes=1320, E0-factor hits=80
```

Every hit lies in the already classified reciprocal candidate divisor
\[
(AB-CD)(AB+CD)(AD+BC)=0.
\]

This is useful negative evidence against an overlooked low-complexity non-bielliptic mechanism, but it is deliberately **not** promoted to a characteristic-zero theorem.  Two finite primes cannot prove that every rational exceptional specialization lies on the reciprocal divisor.

```text
R504_PRYM_EXCEPTIONAL_FINITE_FIELD_SIEVE=PASS
R504_PRYM_EXCEPTIONAL_FINITE_FIELD_SIEVE_IS_PROOF=false
FINITE_DATA_USED_AS_PROOF=false
```

## 5. External theorem class

After the generic Hom obstruction, the remaining task is uniform control of rational points on a two-dimensional Prym-moduli image intersected with the union of Hecke-factor loci attached to the fixed CM elliptic curve `E0` while the isogeny degree is unbounded.

This is an unlikely-intersection / isogeny-orbit problem in `A_2`, not a finite symbolic branch search.  Known work in this area uses ingredients such as Hecke correspondences, large Galois-orbit estimates, Faltings/isogeny height bounds and Pila-Zannier methods.  In particular, the literature contains results for curves and for `E x CM` special curves in `A_2`, but those results are not silently asserted here to cover this two-dimensional Prym image.

Therefore this submission does **not** claim that the exceptional locus is empty or finite.  It classifies the remaining closure problem as requiring a genuinely external uniform theorem (or a new theorem proving an a priori global isogeny-degree bound specialized to this Prym surface).

The exact gate is:

```text
R504_FULL_SPLIT_GENERIC_PRYM_E0_HOM_OVER_K=0
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_LOCUS=OPEN_EXTERNAL
R504_FULL_SPLIT_EXCEPTIONAL_ISOGENY_DEGREE_BOUND=UNKNOWN
R504_FULL_SPLIT_EXCEPTIONAL_FIXED_DEGREE_LOCI=PROPER_ALGEBRAIC
R504_FULL_SPLIT_EXCEPTIONAL_UNBOUNDED_UNION=REQUIRES_UNIFORM_EXTERNAL_CONTROL
R504_FULL_SPLIT_PRYM_ROUTE=EXTERNAL_THEOREM_GATE_CANDIDATE
```

## 6. Scope firewall

This gate is only about the rational Stage25 rank-jump mechanism.

It does not prove

- geometric `Hom_{Kbar}(P_eta,E0)=0`;
- emptiness of every exceptional specialization;
- finiteness of rational exceptional specializations;
- a bound for the isogeny degree;
- any new Stage19 population lower bound.

The global lower remains
\[
N_2(B)\gg B^{1/4}.
\]

Checkpoint60 is not closed by this submission alone.  Fresh audit must decide whether the external-gate classification is sufficient under the normative checkpoint60 stop rule and whether any other assigned route/backflow synchronization remains before checkpoint70.

```text
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```
