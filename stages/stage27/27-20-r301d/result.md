# Stage27-20-r301d — exact state-G blocker transfer to the space diagonal

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
SOURCE_STAGE=Stage20
PARENT_ROUTE=Stage27-20-r301a-c

## 1. Common physical host

Use the audited shared-edge two-face host

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,
\]

with primitive/canonical physical cutoff

\[
R=\sqrt{e^2+x^2+y^2}\le B.
\]

A Stage27 space-diagonal completion is an integer `W` satisfying

\[
W^2=e^2+x^2+y^2.
\]

Stage20's third-face target instead asks that `x^2+y^2` be a square.  Globally these are different completion conditions, so Stage27-20-r301 correctly forbids copying Stage20 local factors without a new derivation.

## 2. The state-G reduction is nevertheless identical

Fix a prime `p`.  On the audited Stage14-e9/e10 state

\[
G:\qquad p\mid e,\qquad p\nmid xy,
\]

the space-diagonal equation reduces modulo `p` to

\[
W^2\equiv x^2+y^2\pmod p.
\]

For odd `p`, put

\[
r=x/y\in\mathbf F_p^*.
\]

Then a necessary condition for a space-diagonal completion is

\[
r^2+1\text{ is a quadratic residue modulo }p.
\]

Therefore every state-G residue class for which `r^2+1` is a nonsquare is an exact Stage27 blocker.  This is the same residue subset used by Stage14-e10 for third-face completion, but its reuse here is now justified by the displayed congruence rather than by population analogy.

At `p=2`, state G means `e` is even and `x,y` are odd, so

\[
e^2+x^2+y^2\equiv 2\pmod 4,
\]

which is not a square.  Thus the complete `p=2` state-G mass is blocked.

## 3. Exact blocker masses inherited from the host law

Stage14-e10 proves on this same physical two-face host that for odd `p`

\[
D_p=p^2+6p+1,
\]

the state-G Tamagawa mass is

\[
\frac{4(p-1)}{D_p},
\]

and conditioned on state G the ratio `r=x/y` is uniform in `F_p^*`.  The number of `r` for which `r^2+1` is a nonsquare is

\[
\frac{p-\chi_4(p)}2.
\]

Hence the exact Stage27 space-diagonal blocker mass is

\[
\boxed{\delta_2^{\rm sp}=\frac29},
\]

and, for odd `p`,

\[
\boxed{
\delta_p^{\rm sp}
=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2}).
}
\]

Thus the state-G blocker masses coincide numerically with Stage20's third-face blocker masses, but only after this exact target-specific reduction.

## 4. Scope firewall

What transfers:

- the common-host six-state Tamagawa law;
- the state-G ratio uniformity;
- the particular nonsquare blocker subset described above.

What does not automatically transfer:

- any other Stage20 local condition;
- Stage20 Euler population identities;
- independence with a different Stage27 receiver;
- a fixed-power saving relative to the existing `B^(1/2+epsilon)` Stage27 theorem.

```text
STAGE27_20_R301D_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SPACE_DIAGONAL_STATE_G_REDUCTION_PROVED=true
SPACE_DIAGONAL_LOCAL_BLOCKER_MASS_FORMULA_PROVED=true
SPACE_DIAGONAL_DELTA_2=2/9
SPACE_DIAGONAL_DELTA_P=2(p-chi4(p))/(p^2+6p+1)
ALL_STAGE20_LOCAL_FACTORS_TRANSFER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301e
```
