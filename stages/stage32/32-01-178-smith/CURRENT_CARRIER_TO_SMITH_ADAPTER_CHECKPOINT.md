# Stage32 32-01-178 Smith — current carrier-to-Smith adapter checkpoint

Status: `PROVISIONAL_SEMANTIC_BRIDGE_CLOSURE_CANDIDATE / HOSTILE_AUDIT_REQUIRED / NO_MAIN_CREDIT`.

This checkpoint supersedes the interpretation that the whole fixed-X8 common-cover/H-equivariant assembly must be re-proved separately for current FULL178. The ambient cover and the cellular Smith target are fixed surface geometry. The only carrier-dependent input needed by the one-bit Smith obstruction is the induced integral H-equivariant correspondence class and its marked mod-2 transvection.

## 1. Current target semantics

Stage32 FULL178 enumerates numerical classes of hypothetical **integral nonexceptional curves** `C` on the smooth minimal resolution `S`, with geometric genus `g in {0,1}` and the audited degree windows. If such a numerical class is represented by an actual carrier, its image on the singular box surface `B` is an integral curve; let `N` be its normalization.

This checkpoint is conditional on actual effectivity only in the usual necessary-condition sense: it proves an obstruction that every such actual carrier would have to satisfy. It does not assert that a numerical terminal is effective.

## 2. The common degree-two cover is ambient, not V6-specific

Retained Stage32 group-quotient geometry has

- `Z = X(8)`,
- `G = Gamma[4]/Gamma[8]`, `|G|=8`,
- `H ~= (Z/2)^2`, normal of index two in `G`,
- `B = (Z x Z)/G_diag`,
- `S0 = (Z x Z)/H_diag`,
- `C2 = Z/H`, `X4 = Z/G`.

For either factor, `S0` is the normalization of `B x_{X4} C2`; both factor pullbacks give the same generic quadratic extension. Therefore for any actual integral carrier normalization `N -> B`, the normalization of `N x_B S0` is the same degree-two common pullback through either factor. This conclusion comes from the ambient quotient square; the old `(g,d,e)=(1,186,266)` values are not used in the generic fibre argument.

Source: `post1484-o210-q4-common-double-cover-cartesian-identity.json`. The old artifact was created inside the O210 route; the present population-scope broadening is a new adapter claim and receives no authority until hostile audit.

## 3. The pullback is connected for every current genus-0/1 carrier

The fixed surface `S0=(X(8)xX(8))/H_diag` has a finite etale map to `C2 x C2`, where `C2` has genus two. Hence `S0` contains no curve whose normalization has genus zero or one: an integral curve in `S0` has a nonconstant projection to at least one factor `C2`, and Riemann--Hurwitz forbids a nonconstant map from a genus-0 or genus-1 smooth curve to a genus-2 curve.

If the quadratic pullback of `N` to `S0` split, one component would map isomorphically to `N` and give a lift `N -> S0`, contradicting the preceding fact. Thus for every current `g in {0,1}` actual carrier the common quadratic pullback is connected and integral at the generic point. This extends the retained EX1-05A connectedness argument from genus one to genus zero without using V6 numerical data.

## 4. Arbitrary-contact parity and fixed-point exhaustion become formal

For either retained factor, current N355 source-locks every special fibre in the resolved model as

`F_b = 2 E_b + sum_{j in I_b} E_j`, `|I_b|=8`,

with the six `I_b` partitioning exceptional labels `93..140`.

At a normalized carrier branch with exceptional contact multiplicity `m` and boundary-elliptic contact multiplicity `ell`, the common quadratic pullback has local exponent

`k = m + 2 ell`.

Hence a fixed point occurs iff `m` is odd. For a marked exceptional group with contact masses `m_r`, the number of odd contacts has parity

`#{r:m_r odd} == sum_r m_r (mod 2)`.

Away from the six special fibres the ambient double cover is etale; a smooth boundary-only contact has even exponent because the boundary component occurs with coefficient two. Therefore there is no additional tau-fixed parity contribution beyond odd exceptional contacts. The previous scratch parity/exhaustion notes are thus consequences of the ambient common-cover adapter plus the current N355 fibre divisor; they are not independent remaining hypotheses.

## 5. Why the old 105/81 and Q602 numerics are not needed by the one-bit obstruction

The audited S32-PW10 cellular target is the fixed topological pullback

`p^*: H2(S0,Z)_free -> H2(X(8)xX(8),Z)^H`

with cokernel `(Z/2)^3 x (Z/4)^2`.

For an actual carrier pullback divisor `D0` on `S0`, its class `p^*[D0]` is tautologically in the image of `p^*`, so every Smith cokernel coordinate must vanish.

The current Smith replay `verify_smith_all_prym_parity_transvection_gluing.py` removes the old numerical magnitudes from the detecting coordinate. It exhausts, for each of the three marked transvection actions,

- all `2^8=256` invariant-part mod-4 lifts,
- all `2^3=8` Prym parity types,

for `3*256*8=6144` builds. It explicitly does **not** use the historical projection degrees or historical Gaussian norm magnitudes. Integrality itself selects the allowed center/Prym alignment, and every integral build forces the tracked Smith source bit to one.

The retained Smith projection identifies that bit with Smith coordinate 0 (`B[4,4] mod 2`). Therefore any integral H-equivariant correspondence class inducing one of the three marked single-transposition actions has nonzero Smith class, independently of the old fixed-V6 values `105,81,Q_Rosati=602`.

## 6. Current conditional contradiction

Take an actual current FULL178 carrier whose exact twelve marked exceptional pair-mass parity signature is one of the three single-transposition signatures already identified by `CURRENT_NUMERICAL_MARKING_CLOSURE.json`.

1. Sections 2--4 give the source-compatible common quadratic pullback and identify its marked mod-2 action with that single Weierstrass transposition.
2. Pulling the resulting divisor class to `X(8)xX(8)` gives an integral H-equivariant correspondence class.
3. The all-Prym/all-mod4 Smith replay forces Smith coordinate 0 to equal one for such an integral transvection class.
4. But any actual divisor class pulled back from `S0` lies in `im(p^*)`, where every Smith cokernel coordinate is zero.

Contradiction.

Thus, provisionally:

> **Every actual current FULL178 genus-0/1 carrier with one of the three marked single-transposition pair-mass signatures is impossible.**

This is a semantic bridge closure candidate, not MAIN pruning credit.

## 7. Remaining gate is now numerical/data exposure only

The current N355 prefix does not determine all twelve true pair-mass parities. The exact current rowspace calculation leaves residual pair-mass parity rank two. It can be closed by either:

- materializing two additional true marked four-exceptional group sums, or
- materializing a sufficient individual-exceptional extension (one known minimum uses five labels).

After that, the current survivor population can be censused for the three single-transposition signatures. That census plus this adapter must then receive hostile audit before any Stage32 MAIN pruning credit.

## Firewalls

- No historical O210/Q602 residue is treated as a current survivor.
- No fixed V6 bidegree, Rosati norm, or deck-trace package is imported into current FULL178.
- No numerical terminal is promoted to an effective carrier.
- No MAIN pruning count is claimed in this checkpoint.
- No N350 producer, production COMPLETE, N104 release, FULL178 completion, theorem, receiver, endpoint, Stage32 closure, Perfect Cuboid existence/nonexistence, heavy-compute, or merge authorization is claimed.
