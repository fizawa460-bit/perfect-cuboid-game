# Stage32 post-1490 O210 Bolza V4 deck-translate defect decomposition

Scope: fixed recovered V6 class `g1-d186`, exact extremal profile `O=210`, `q'=4` only. This leaf does not exclude O210. It replaces an unconstrained request for three deck-translate intersection numbers by an exact defect decomposition and isolates the one missing source-lock needed to split the three deck characters.

## Retained exact input

From the exact birational D4+D4 reduction, the pair map

`Y -> Gamma subset Q=C0 x C0`

is birational, `g(Y)=106`, and `Gamma` has bidegree `(105,81)`. Hence on the genus-two product `Q`,

`Gamma^2 = 2*105*81 = 17010`,
`K_Q.Gamma = 2*(105+81) = 372`,
`p_a(Gamma)=1+(Gamma^2+K_Q.Gamma)/2=8692`,
so the total normalization defect is

`delta_Gamma = 8692-106 = 8586`.

The same retained reduction identifies the finite etale quotient

`q:X -> Q`

with degree four and deck group `V4`.

Let `D` be the irreducible upstairs carrier-image component whose normalization is `Y`; then `q|_D` is birational onto `Gamma`. Write

`delta_D = p_a(D)-106 >= 0`.

Because `q` is etale, `K_X=q^*K_Q`; projection gives `K_X.D=372`. Adjunction therefore gives

`D^2 = 2*(106+delta_D)-2-372 = -162+2*delta_D`.

Since `q^*Gamma` is the sum of the four deck translates of `D`, expansion of its square gives

`4*Gamma^2 = 4*D^2 + 4*sum_{t != 1} D.t(D)`.

Therefore

`sum_{t != 1} D.t(D) = 17172-2*delta_D`.

For each nonidentity involution `t`, the zero-dimensional intersection scheme `D cap t(D)` is `t`-stable. The deck action is fixed-point-free, so intersection points occur in free two-element `t`-orbits with equal local multiplicity. Thus every `D.t(D)` is even. Put

`c_t = (D.t(D))/2 in Z_{>=0}`.

The exact quotient-defect identity is then

`delta_D + c_1 + c_2 + c_3 = 8586`.

This is the precise information available before an action matrix for the three nontrivial deck involutions on the retained Picard64 basis is source-locked.

## What this resolves and what it does not

The total deck-translate collision budget is not an independent fourth large search: it is exactly the downstairs normalization defect after subtracting intrinsic upstairs singularity defect. In particular, blindly enumerating three unrelated intersection numbers is unnecessary.

The retained Picard64 witness adapter supplies one exact 64-coordinate class for the representative slice, but it does not itself supply the three 64x64 deck-action matrices or an equivalent exact permutation/action on the retained basis. The old two-character V4 torsor source locks the abstract deck group, not this Picard64 action. No identification is inferred between those interfaces.

Next exact datum: source-lock the action of the three nonidentity deck involutions on the retained Picard64 basis (or directly source-lock the three pairings `D.t(D)`). Then compute the three integers `c_t` and compare them with the marked six-Weierstrass collision constraints.

Firewalls: O186/O188 remain closed; the Abel-Jacobi-zero closure remains closed; the Rosati lattice must not be materialized; this defect identity is necessary geometry only and gives no receiver, route, theorem, endpoint, or perfect-cuboid credit.
