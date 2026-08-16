# Stage25-reentry r011a discovery ledger

STATUS=SUBMITTED_PENDING_FRESH_AUDIT

## D011-01 — common log-exponent ledger

Existing audited asymptotics share the same Stage21/22 denominator `M1`:

- `M1 ~ 3/(4*pi^2) B^2 log B`;
- `N1 ~ kappa/(24*pi) B(log B)^3`;
- `M2 ~ C_M2 B(log B)^5`.

Therefore the net log-exponent changes are exactly `+2` and `+4`, while both targets lose one polynomial power of `B` relative to `M1`.

VERDICT=PROVED_EXISTING_INTERFACES

## D011-02 — source log1 is explicit

E-1d derives the source logarithm from

`sum_{primitive hypotenuse h<=B} 1/h ~ (1/(2*pi)) log B`.

VERDICT=PROVED_EXISTING_INTERFACE

## D011-03 — Stage12 target log3 is explicit

The active Stage12 proof reduces its leading radial term to

`double_integral log(x)log(y)/(x^2+y^2) dx dy = (pi/48)(log B)^3 + O((log B)^2)`.

Thus two rectangle-density logarithms and one radial harmonic integration are visible internally.  No adapter identifying the Euler source harmonic slot with the Stage12 radial slot is currently proved.

VERDICT=PROVED_INTERNAL_STRUCTURE_WITH_SLOT_ADAPTER_OPEN

## D011-04 — one-face Euler geometry

The raw distinguished-face source is the quadric cone

`u^2=e^2+x^2` in `P3_[e:x:y:u]`.

Its minimal resolution is `F_2`; with negative section `S` and ruling `F`, the projective hyperplane pullback is `H=S+2F` and `K=-2S-4F=-2H`.  Hence the generalized height invariants are `(a,b)=(2,2)`.  This predicts `B^2(log B)^(2-1)` and matches E-1d/E-1e.

VERDICT=NEW_GEOMETRIC_LEDGER_CANDIDATE

## D011-05 — nested one-face-plus-space surface is a quadratic twist

For

`X_S: p^2=a^2+b^2, d^2=p^2+c^2`,

the map over `Q(i)`

`[E:X:Y:U:V]=[p:i*b:c:a:d]`

identifies `X_S` with the Stage15 shared-edge model

`U^2=E^2+X^2, V^2=E^2+Y^2`.

Complex conjugation becomes `X->-X`.  Under the Stage15 toric parametrization this is `(m:n)<->(n:m)` and leaves `(r:s)` fixed.

VERDICT=EXACT_ALGEBRAIC_IDENTITY

## D011-06 — rational Picard rank four for the twist

Stage15 gives the split resolution `Bl_4(P1xP1)` with basis

`F1,F2,E00,E10,E01,E11`.

The twist Galois involution fixes `F1,F2` and swaps `E00<->E10`, `E01<->E11`.  Hence the invariant subspace has basis

`F1, F2, E00+E10, E01+E11`

and rank four.

Since a quartic complete intersection of two quadrics has `K=-H` and the four `A1` resolutions are crepant, the nested target has `(a,b)=(1,4)`.

VERDICT=NEW_GEOMETRIC_LEDGER_CANDIDATE

## D011-07 — Stage15 split target

Stage15-2a/2b already prove the split toric resolution has Picard rank six and anticanonical physical height, hence `(a,b)=(1,6)` and `M2~C_M2 B(log B)^5`.

VERDICT=PROVED_EXISTING_INTERFACE

## D011-08 — geometric mechanism for log2/log4

The ledger is

`M1: (2,2)`
`N1: (1,4)`
`M2: (1,6)`.

Thus

- Stage21: `Delta a=-1`, `Delta b=+2`;
- Stage22: `Delta a=-1`, `Delta b=+4`;
- cross-target: `Delta a=0`, `Delta b=+2`.

This explains the shared `B^-1` polynomial cost and the different log enhancements.  Algebraically

`b_M2-b_M1=(b_N1-b_M1)+(b_M2-b_N1)=2+2`.

VERDICT=NEW_FINE_MECHANISM_CANDIDATE

## D011-09 — independent factors still not proved

Nothing in D011-08 identifies four independent local probabilities, four independent Dirichlet poles, or an `H-one-log times L-one-log` product.

VERDICT=FIREWALL_RETAINED

## D011-10 — endpoint relevance

This work explains neighboring population exponents only.  It neither produces nor excludes a three-face integral cuboid.

VERDICT=NO_PERFECT_CUBOID_CONCLUSION
