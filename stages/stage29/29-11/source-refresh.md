# Stage29-11 source refresh

```text
STATUS=SUBMISSION_SOURCE_REFRESH
CURRENT_WEB_REFRESH_ATTEMPTED=true
CURRENT_WEB_REFRESH_AVAILABLE=false_SERVICE_ERROR
REPO_AUDITED_SOURCE_LOCKS_USED=true
```

The live-web refresh attempted during this batch returned a service error, so no unverified fresh web claim is promoted. The submission uses the already audited primary-source locks in the repository and marks any new source-level interpretation for fresh audit.

## Campedelli

- A. Calabri, M. Mendes Lopes, R. Pardini, *Involutions on numerical Campedelli surfaces*, Tohoku Math. J. 60 (2008), 1--22, DOI `10.2748/tmj/1206734404`.
- Existing repo source lock: `stages/stage29/29-02hb/source-lock.md`, especially Section 5 / Example 1 and the geometric rational/Enriques involution-quotient terminology.
- M. Mendes Lopes, R. Pardini, M. Reid, *Campedelli surfaces with fundamental group of order 8*, Geom. Dedicata 139 (2009), 49--55, arXiv:0805.0006.

29-11 proposes only a **geometric** partial discharge for `R29-CAMP3`. Audit must verify the exact involution theorem locator and must not promote geometric rationality to Q-rationality.

## Beauville

- A. Beauville, *A tale of two surfaces* (the source used by audited 29-02d for the irregular degree-two cover, etale V4 tower and Albanese structure).
- Repo source files: `29-02d/q-form-adapter.md`, `lift-twist-ledger.md`, `albanese-bolza-target.md`, `source-lock.md`.
- Fite--Sutherland arithmetic field-of-definition firewall for the Bolza Jacobian remains load-bearing.

There is a locator discrepancy in surviving source descriptions of Beauville's etale tower (`Remark 1` versus another surfaced version/description using `Remark 2`). The mathematical tower was already audited, but 29-11 fresh audit should reconcile the exact edition/remark locator rather than silently rewriting history.

Recent genus-two 2-Selmer/Cassels--Tate algorithms are relevant as computational tools for individual Beauville-induced twists. No uniform theorem over the infinite physical twist family is imported.

## Modular

- Testa--Stoll, cuboid surface paper, Section 4: modular presentation using `X(8)`, kernel `G0`, quotient residual `PSL2(Z/4) ~= S4`, and the Q-rational conjugate-self level datum.
- 29-02g exact repo adapters remain authoritative for the current arithmetic scope.
- Fisher's ordinary symplectic 8-congruence surface remains a firewall: ordinary 8-congruence is abundant and is not an endpoint obstruction.

The abstract coincidence between the arrangement `S4` and modular residual `S4` is not promoted to `R29-KUM5` closure without an action/cocycle calculation.

## Brauer

- Testa--Stoll Theorem 10 remains the proper algebraic Brauer input.
- 29-02f's Frobenius/integral audit remains the proper odd-primary transcendental input.
- The physical-open boundary/UPic/Gersten/two-primary problem remains separate.

No new Brauer--Manin obstruction is claimed in this source refresh.
