# Stage32 post1532 Q602 single-b3 commutator reduction

## Scope

This leaf uses only already hostile-audited Stage32 mod-2 correspondence data and the already source-locked principal Bolza `G12` action. It asks one bounded question:

> Is exact commutation of the actual correspondence operator `T=(f1)_*(f2)^*` with the single principal Bolza automorphism `b3` compatible with any of the audited Q602 mod-2 survivors?

It does not prove that the carrier or correspondence is `b3`-equivariant.

## Exact retained inputs

1. Audited Weierstrass/transvection refinement:
   - `post1505-o210-q602-weierstrass-parity-transvection-refinement.json`
   - canonical SHA-256 `83fd16fdaac674a3f63b4b2dac498136f1bc584c9e06d89f1aa1a7bdc4c30386`
   - hostile re-audit review `5102652713`
   - exact Q602 survivors in the retained basis `(e1,e2,r*e1,r*e2)` are `73,97,235`.

2. Audited marked gauge orbit:
   - `post1505-o210-q602-marked-w-line-gauge-orbit.json`
   - canonical SHA-256 `7ad84e3c0a567119933ee0941b3b125ebcdb80651973033e13dbf12b553bfc92`
   - hostile re-audit review `5108049622`
   - the principal Bolza automorphism is source-locked in the same `Z[r]^2`, `r^2=-2`, coordinates as

     `b3 = [[-1,-1],[1,0]]`.

The gauge certificate also records that `73,97,235` form one principal-Bolza conjugacy orbit. This leaf does **not** select the canonical representative 73 to obtain the exclusion; all three audited residues are checked separately.

## Exact mod-2 calculation

A residue byte is decoded exactly as in the audited transvection verifier. Writing its four `F2[eps]/(eps^2)` entries in row-major order and letting `eps = r mod 2`, each 2x2 matrix acts on the retained four-dimensional `F2` basis `(e1,e2,r*e1,r*e2)`.

The three audited residues give

- `73`: `[[1,0,0,0],[0,1,0,0],[0,1,1,0],[0,0,0,1]]`,
- `97`: `[[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,0,0,1]]`,
- `235`: `[[1,0,0,0],[0,1,0,0],[1,1,1,0],[1,1,0,1]]`.

The source-locked `b3` acts mod 2 as

`[[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,0,1,0]]`.

For every one of `73,97,235`, the commutator `T*b3-b3*T` is nonzero over `F2`. Hence no audited Q602 residue commutes with `b3` even after reduction mod 2.

Exact integral commutation would reduce to mod-2 commutation. Therefore

`[T,b3]=0  =>  Q(T) != 602`

at the fixed O210 Stage32 branch.

This is a genuinely weaker conditional premise than the post1522/post1526 two-generator scalar-centralizer route: one exact `b3` commutator is sufficient. No scalarity or valence hypothesis is used here.

As a control, `b4` alone is not an exclusion: residue `73` commutes with `b4 mod 2`, while `97` and `235` do not. Thus the single-generator reduction is specific to `b3` and is not being inferred merely from membership in the principal Bolza group.

## Decision / firewall

This leaf proves only the conditional implication above. It does not prove `b3`-equivariance of the hypothetical carrier, either projection, the common cover, or the actual correspondence.

Therefore:

- `Q602` is not unconditionally excluded;
- `O210` remains OPEN;
- `O212+` remains BLOCKED;
- the controller is not modified;
- no receiver / route / theorem / endpoint / FULL178 / effectivity / perfect-cuboid credit is promoted.

The next exact geometric target is now narrower:

> prove or refute `[T,b3]=0` from a source-locked carrier-map equivariance, quotient-normalizer identity, or exact correspondence/divisor identity.

Re-running the already-closed retained-Stoll H-orbit symmetry search is not a valid substitute for this geometric commutator.