# Stage27-20-r301e — source justification for the growing-prime host sieve

AUDIT_REPAIR_TARGET=R301E_SELBERG_TRANSFER_CHECK
PREVIOUS_AUDIT_VERDICT=FAIL_PENDING_SOURCE_JUSTIFICATION
SOURCE_JUSTIFICATION_REPAIRED=true
FRESH_REAUDIT_REQUIRED=true

## 1. What Stage14-e11 actually sieves

Stage14-e11 does not obtain its growing-prime estimate by counting only points satisfying the third-face-square predicate.  In Section 5 it applies Huang's uniform toric Selberg sieve directly to the common two-face toric ambient population and the local bad subsets `B_p`, obtaining an upper bound for

\[
\#\{\text{ambient two-face host points avoiding every }B_p\}.
\]

The relevant Stage14-e11 inputs are:

- the same toric host `Y=Bl_4(P1 x P1)` with `rho(Y)=6`, `dim Y=2`;
- `B_p` is detected modulo `p` on the canonical smooth toric integral model;
- therefore the uniform covering-level exponent is `n0=1`;
- its normalized weight satisfies `w_p=2/p+O(p^-2)` and has sieve dimension two;
- Huang's uniform toric Selberg sieve then gives

\[
\#\{\text{ambient points avoiding every }B_p\}
\ll
B(\log B)^5
\left(\frac1{G(N)}+\frac{N^{22+\varepsilon}}{(\log B)^{1/2-\varepsilon}}\right).
\]

Choosing `N=(log B)^(1/100)` gives

\[
\#\{\text{ambient points avoiding every }B_p\}
\ll \frac{B(\log B)^5}{(\log\log B)^2}.
\]

Thus the e11 remainder/CRT mechanism is already attached to the ambient toric host plus the concrete residue subsets `B_p`; it is not a remainder theorem for the downstream third-face predicate.

## 2. Why the Stage27 space-diagonal population is inside the same sifted set

Stage27-20-r301d proves a target-specific reduction.  On state G,

\[
p\mid e,\qquad p\nmid xy,
\]

and an integral space diagonal satisfies

\[
W^2=e^2+x^2+y^2\equiv x^2+y^2\pmod p.
\]

Therefore whenever the e10/e11 local condition

\[
\chi_p(x^2+y^2)=-1
\]

holds on state G, an integral space diagonal is impossible.

Crucially, this is not merely equality of normalized masses.  It says that the actual residue subset `B_p` used by Stage14-e11 is also an actual forbidden subset for the Stage27 space-diagonal completion problem on the same ambient host.

Let `A(B)` be the common primitive/canonical two-face host under the same Euclidean cutoff, and let

\[
S(B)=\{x\in A(B):x\notin B_p\text{ for every sieved prime }p\}.
\]

Let `P_sp(B)` be the larger Stage27 population with integral space diagonal, without imposing the exactly-two third-face exclusion.  Then r301d gives the set inclusion

\[
\boxed{P_{sp}(B)\subseteq S(B)}.
\]

No transfer of a predicate-specific CRT lemma is required.  The sieve theorem has already bounded `S(B)` itself.

Hence

\[
P_{sp}(B)
\ll \frac{B(\log B)^5}{(\log\log B)^2},
\]

and since `N2(B)<=P_sp(B)`,

\[
N_2(B)
\ll \frac{B(\log B)^5}{(\log\log B)^2}.
\]

## 3. Scope firewall

This repair does **not** claim:

- that all Stage20 local factors transfer;
- that equal local masses alone would justify a Selberg transfer;
- that the Stage20 third-face thin-cover theorem transfers;
- that the host-sieve factor may be multiplied into the existing half-power receiver;
- that this improves the existing `N2(B)<<_eps B^(1/2+eps)` theorem.

The only transferred quantitative statement is the already-proved Stage14-e11 upper bound for the same ambient host points avoiding the same residue subsets `B_p`, used through the set inclusion `P_sp(B) subset S(B)`.

```text
R301E_SOURCE_JUSTIFICATION=REPAIRED_BY_IDENTICAL_BAD_SUBSET_AND_SET_INCLUSION
SAME_BAD_SUBSET_B_P_ON_COMMON_HOST=true
EQUAL_MASS_ALONE_USED=false
P_SP_SUBSET_OF_E11_SIFTED_AMBIENT_SET=true
PREDICATE_SPECIFIC_REMAINDER_TRANSFER_REQUIRED=false
SPACE_DIAGONAL_GROWING_PRIME_SIEVE_TRANSFER_PROVED=true
HOST_SIEVE_BOUND_BEATS_CURRENT_HALF_POWER=false
SIEVE_FACTOR_MULTIPLIED_WITH_HALF_POWER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
FRESH_REAUDIT_REQUIRED=true
```
