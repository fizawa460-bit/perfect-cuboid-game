# Stage27-20-r301e — growing-prime blocker sieve on the space-diagonal target

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301d
PREVIOUS_AUDIT_VERDICT=FAIL_PENDING_SOURCE_JUSTIFICATION
FINAL_AUDIT_VERDICT=PASS
SOURCE_JUSTIFICATION=stages/stage27/27-20-r301e/source-justification.md
SOURCE_JUSTIFICATION_REPAIRED=true
FRESH_REAUDIT_REQUIRED=false
AUDIT_STATUS=PASS
AUDIT_RECORD=stages/stage27/27-20-r301d-f/audit.md
PR=1043
MERGE_COMMIT=11bab78346d6535ba17fb268b42c89defff9a7eb

## 1. Larger completion population

Let `P_sp(B)` count primitive/canonical shared-edge two-face host objects under the same Euclidean cutoff `R<=B` for which the space diagonal is integral, without requiring the third face to be nonintegral.

Every Stage27 `N_2(B)` object has exactly one shared edge between its two integral faces, hence gives one object counted by `P_sp(B)`. Therefore

\[
\boxed{N_2(B)\le P_{\rm sp}(B)}.
\]

The larger population may also contain objects with a third integral face; no perfect-cuboid existence statement is used.

## 2. Exact source-level reuse of the Stage14-e11 sifted ambient set

The hostile audit correctly separated two logically different claims:

1. the Stage27 local blocker has the same normalized mass as the Stage20 blocker;
2. the Stage14-e11 weighted Selberg sieve controls the Stage27 target.

Claim 2 is **not** justified merely by claim 1.  The source-level justification is stronger and is recorded in `source-justification.md`.

Stage14-e11 Sections 3--5 prove that its concrete blocker `B_p` is detected modulo `p` on the common smooth toric integral model, with uniform covering level `n0=1`, and then apply Huang's uniform toric Selberg sieve to the ambient host itself.  Its counted set is

\[
S(B)=\{\text{ambient two-face host points avoiding every }B_p\}.
\]

Thus the e11 remainder/CRT mechanism is attached to the common host and the concrete residue subsets `B_p`; it is not a remainder theorem whose validity depends on the downstream third-face-square predicate.

Stage27-20-r301d independently proves that the **same actual subsets** `B_p` are forbidden for an integral space diagonal. On state G,

\[
p\mid e,\qquad p\nmid xy,
\]

and

\[
W^2=e^2+x^2+y^2\equiv x^2+y^2\pmod p.
\]

Hence if the Stage14-e10/e11 condition `chi_p(x^2+y^2)=-1` holds, the space diagonal cannot be integral. Therefore

\[
\boxed{P_{\rm sp}(B)\subseteq S(B)}.
\]

This is a set-inclusion argument using the same host and the same bad subsets, not a transfer based only on matching local masses.

## 3. Growing-prime bound

Stage14-e11 proves for this same sifted ambient set, using `rho(Y)=6`, `dim Y=2`, `n0=1`, sieve dimension two, and `N=(log B)^(1/100)`, that

\[
S(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}.
\]

By the inclusion above,

\[
\boxed{
P_{\rm sp}(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}
}
\]

and consequently

\[
\boxed{
N_2(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}.
}
\]

No predicate-specific Stage27 CRT/remainder theorem is needed, because the e11 theorem already bounds the larger ambient sifted set containing `P_sp(B)`.

## 4. Audited scope and non-improvement

The source-level justification has now passed hostile audit.  This theorem is valid, but Stage27 already has

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

For any fixed `epsilon<1/2`, this polynomial half-power theorem is asymptotically stronger than the host-sieve bound above. Therefore the sieve theorem does not lower the current Stage27 upper exponent.

It is also illegal to multiply the host-sieve factor by the existing half-power theorem without a new theorem showing the blocker sieve acts uniformly inside the specific half-power receiver used by Stage14/Stage27.

## 5. Boundary

```text
STAGE27_20_R301E_STATUS=AUDITED_PASS_MERGED
PREVIOUS_AUDIT_VERDICT=FAIL_PENDING_SOURCE_JUSTIFICATION
FINAL_AUDIT_VERDICT=PASS
R301E_SOURCE_JUSTIFICATION=REPAIRED_BY_IDENTICAL_BAD_SUBSET_AND_SET_INCLUSION
SAME_BAD_SUBSET_B_P_ON_COMMON_HOST=true
EQUAL_MASS_ALONE_USED=false
P_SP_SUBSET_OF_E11_SIFTED_AMBIENT_SET=true
PREDICATE_SPECIFIC_REMAINDER_TRANSFER_REQUIRED=false
SPACE_DIAGONAL_GROWING_PRIME_SIEVE_TRANSFER_PROVED=true
SPACE_DIAGONAL_HOST_SIEVE_BOUND=B(log B)^5/(log log B)^2
N2_HOST_SIEVE_BOUND_PROVED=true
HOST_SIEVE_BOUND_BEATS_CURRENT_HALF_POWER=false
SIEVE_FACTOR_MULTIPLIED_WITH_HALF_POWER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
FRESH_REAUDIT_REQUIRED=false
NEXT_DERIVED_ROUTE=27-20-r301f
```
