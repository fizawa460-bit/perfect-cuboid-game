# Stage12-N1-2 limited re-review manifest R03

> **BUNDLE_ID:** `PC-N1-2-LIMITED-REREVIEW-20260807-R03`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3e`
>
> **SOURCE_SNAPSHOT_COMMIT:** `bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c`
>
> **SOURCE_LEDGER_SHA256:** `a752f5f42c17944c09d2d8ebff6432f74d772b88d5463d2aa3af0fbd5069b774`
>
> **PARENT_BUNDLE:** `PC-N1-2-REPAIRED-PROOF-20260807-R02`
>
> **LAST_SOURCE_DOCUMENT:** `docs/stage12-n1-3e-local-gap-closure.md`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT`
>
> **REVIEW_PAGE:** `review/PC-N1-2-LIMITED-REREVIEW-20260807-R03.html`

## Mandatory handshake

Before mathematical review, reproduce exactly:

```text
BUNDLE_ID=PC-N1-2-LIMITED-REREVIEW-20260807-R03
COMPLETED_THROUGH=Stage12-N1-3e
SOURCE_SNAPSHOT_COMMIT=bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c
SOURCE_LEDGER_SHA256=a752f5f42c17944c09d2d8ebff6432f74d772b88d5463d2aa3af0fbd5069b774
PARENT_BUNDLE=PC-N1-2-REPAIRED-PROOF-20260807-R02
LAST_SOURCE_DOCUMENT=docs/stage12-n1-3e-local-gap-closure.md
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT
END_OF_BUNDLE=PC-N1-2-LIMITED-REREVIEW-20260807-R03
```

If any value differs, return `STALE_SOURCE`. If the end marker cannot be read, return `UNREADABLE_SOURCE`.

## Scope

This is a **limited re-review**, not a new full proof review.

The parent R02 review returned `REPAIRABLE` with exactly two local gaps:

```text
OUTER_AVERAGE_LEMMA
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY
```

Review only whether Stage12-N1-3e closes these two items. Do not reopen MAJOR-01, MAJOR-04, MINOR-01, MINOR-02, or the radial `pi/48` calculation unless the new text creates a direct contradiction.

## Immutable source ledger

| path | Git blob SHA | role |
|---|---|---|
| `review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html` | `da7e937b195cc2c4fd43eb4bd2235217bc65f770` | parent self-contained proof bundle |
| `docs/stage12-n1-3e-local-gap-closure.md` | `a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5` | two local repairs |

Pinned links:

1. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c/review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html`
2. `https://github.com/fizawa460-bit/perfect-cuboid-game/blob/bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c/docs/stage12-n1-3e-local-gap-closure.md`

The R03 physical page embeds the complete parent R02 main content and the complete Stage12-N1-3e supplement.

## Required question A — outer average

Check all of the following.

1. Is
   \[
   W(n)=G(n)H_{\rm abs}(n)
   \]
   explicitly defined at every prime power?
2. Is the Euler factorization
   \[
   \mathcal W(s)=\zeta(s)^2L(s,\chi_4)E_W(s)
   \]
   correct?
3. Does `E_W` converge absolutely in a half-plane containing `s=1`?
4. Does the locked `z=2` Selberg--Delange input imply
   \[
   M_W(T)\ll T\log(2T)?
   \]
5. Does this imply, uniformly for `Q>=2`,
   \[
   \sum_{\substack{r<s,(r,s)=1\\Q<r^2+s^2\le2Q}}W(rs)
   \ll Q(\log(2Q))^2?
   \]
6. Does dyadic summation up to `2B/X_0` give
   \[
   O(BX_0^{-1/2}(\log B)^2)?
   \]

## Required question B — local constant

Check all of the following.

1. For odd `p`, is
   \[
   D_{\lambda,p}=1+U_p(s_1)+U_p(s_2)
   \]
   the exact coprime local factor?
2. Is the 2-adic parity factor
   \[
   D_{\lambda,2}=2+\frac{x}{1-x}+\frac{y}{1-y}
   \]
   correct, and does it give `C_{lambda,2}(1,1)=1`?
3. For `p congruent 3 mod 4`, is the normalized contribution `(1-p^-2)^3`?
4. For `q congruent 1 mod 4`, is
   \[
   J_{\beta,q}(1)^2C_{\lambda,q}(1,1)
   =(1-q^{-2})\left(1+\frac{4q}{(q+1)^2}\right)(1-q^{-1})^4?
   \]
5. Do all factors combine to
   \[
   C_\lambda^{(0)}
   =\eta\prod_{\ell\text{ odd prime}}(1-\ell^{-2})
   =\frac8{\pi^2}\eta?
   \]

## Output

Return one of:

- `CLOSED`: both local gaps are closed;
- `REPAIRABLE`: one or both have an explicit local defect and a stated repair;
- `OPEN`: a central implication in one of the two repairs is false or unsupported;
- `STALE_SOURCE`;
- `UNREADABLE_SOURCE`.

Use the machine-readable summary:

```text
VERDICT=
OUTER_AVERAGE_LEMMA=
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=
NEW_CENTRAL_GAP=
```

A generic plausibility statement is not a completed review.