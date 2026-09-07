# Stage35-EX Goal4AI — degree-31 homogeneous principalization existence source lock

## Scope

This leaf proves an **existence statement only** for the remaining class-B `Q(i)/Q` cyclic target. It proves that the exact Goal4Z/4AA divisor target has a Q-rational principal function which may be represented as a ratio of two homogeneous degree-31 sections on the cuboid canonical model. It does **not** compute the coefficients of those sections and therefore does not materialize an evaluable literal `F_B`.

## Exact parent packets

Parent authority:

- schema `STAGE35_EX_PESCH_E1_STATE_V71_GOAL4AH_DEGREE31_RR_EFFECTIVITY_PROVED_LITERAL_F_B_PENDING_AUDIT`;
- snapshot `stages/stage35-ex/snapshots/MAIN-STATE-V71-a8d275311cbd.json`;
- Goal4AH artifact `stages/stage35-ex/35ex-35/goal4ah-degree31-rr-effectivity.json`, canonical SHA256 `958d9de580794f2bd40c1c7defd1e9d487cca4074e1389613e08a5126089d1b9`;
- Goal4AA artifact `stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json`;
- exact retained diagnostics `diagnose_stage35_ex_35_goal4ag_degree25_residual.py` and `diagnose_stage35_ex_35_goal4ah_degree31_rr.py`.

The exact Goal4AA target is a Q-defined formal divisor

`T = P - N = D_B + cc(D_B) - E_B`

with 69 nonzero retained components and exact geometric Picard class zero. The degree-25 diagnostic reconstructs the positive and negative classes and verifies literally

`[P] = [N] = Pc`

in the primitive marked Picard64 lattice, with

`H.Pc = 396`, `H^2 = 16`.

## Common degree-31 residual

For homogeneous degree `d`, the common residual class is

`R_d = d H - Pc`.

At `d=31`, Goal4AH performs the exact retained fixed-component strip on `R_31`. After 325 forced subtractions the stripped class `D` has

- `H.D = 96`,
- `D^2 = 212`,
- `chi(O_S(D)) = 66`,
- `H.(K_S-D) = -80`.

Using `K_S=H`, `chi(O_S)=8`, and nefness of `H`, Goal4AH proves `h^0(D) >= 66`. The full strip multiplicity vector and `D` are invariant under the exact `cc,ct` Galois generators, so a Q-defined effective stripped divisor exists. Reattaching the Q-defined forced components gives a Q-defined effective divisor

`R in |31H-Pc|`.

Because `[P]=[N]=Pc`, this same `R` is simultaneously a residual for both sides:

`P+R ~ 31H`,
`N+R ~ 31H`.

## Q-rational descent of the principal function

Goal4AA already proves `[T]=0` in `Pic(S_bar)`, and Goal4AH proves `T` is Q-defined. Hence over `Qbar` there is `f` with `div(f)=T`. For every Galois element `sigma`, the quotient `sigma(f)/f` has zero divisor and is therefore a constant in `Qbar^*`. These constants form a 1-cocycle. Hilbert 90 kills this cocycle, so after rescaling `f` one obtains

`F_B in Q(S)^*`, `div(F_B)=T`.

This is an existence/descent statement only; no coefficients of `F_B` are extracted.

## Homogeneous degree-31 realization

Michael Stoll and Damiano Testa, *The surface parametrizing cuboids* (arXiv:1009.0388), Lemma 3 and its immediate consequences give the retained geometry used here:

- the canonical model `Sbar` is a normal complete intersection of four quadrics in `P^6` with 48 `A_1` rational double points;
- `Sbar` is projectively normal;
- for the minimal resolution `b:S->Sbar`, `H=K_S=b^*O_Sbar(1)`.

Because the singularities are rational double points, `b_*O_S=O_Sbar`; hence

`H^0(S,O_S(31H)) = H^0(Sbar,O_Sbar(31))`.

Projective normality makes the restriction map

`H^0(P^6,O(31)) -> H^0(Sbar,O_Sbar(31))`

surjective. Therefore the Q-defined divisors `P+R` and `N+R` are cut out by Q-rational homogeneous degree-31 sections `A` and `B` on the canonical model. Their ratio satisfies

`div_S(A/B) = (P+R)-(N+R) = P-N = T`.

Thus a degree-31 homogeneous principalization exists over Q.

## Firewall

Proved here:

- Q-rational principal-function existence for the fixed class-B target;
- existence of a Q-rational homogeneous degree-31 numerator/denominator pair;
- degree 31 is an achieved homogeneous principalization degree, not merely a surviving lower-bound candidate.

Still not proved/materialized:

- literal coefficients of the degree-31 numerator or denominator;
- an evaluable explicit formula for `F_B`;
- local evaluations of class B;
- the full algebraic Brauer group of the open receiver;
- verticality;
- a Brauer-Manin obstruction;
- E1, `R29-PESCH-E1`, `R29-FIB2`, Stage35 closure, or any perfect-cuboid existence/nonexistence theorem.

The next legal leaf is literal degree-31 section coefficient extraction, not local evaluation.
