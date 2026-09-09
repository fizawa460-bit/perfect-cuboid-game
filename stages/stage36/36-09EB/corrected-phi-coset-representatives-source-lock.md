# Stage36 36-09EB corrected Phi-coset representative source lock

## Purpose

36-09EA reduces the fixed-2-primary retained-open problem to four rational translations indexed by `J(Q)/Phi A(Q)`. The post-EA DW pairing correction changes the authoritative Phi-Selmer labels but retains the quotient cardinality four. After hostile re-audit PASS `5149329866` and V232 promotion consumption, only the corrected labels may be used.

This leaf materializes all four rational quotient representatives exactly.

## Locked corrected input

Let `J=Jac(C3_2)`, `A=E_tau x E_sigma x E_rho`, and `Phi:A->J` be the fixed degree-eight isogeny.

The audited DW correction gives

`Sel^Phi(A/Q) = {([1],[1],[1]), ([1],[1],[-1]), ([1],[2],[6]), ([1],[2],[-6])}`.

36-09DZ gives `Sha(A)[Phi]=0`. Therefore the finite isogeny-descent exact sequence

`0 -> J(Q)/Phi A(Q) -> Sel^Phi(A/Q) -> Sha(A)[Phi] -> 0`

identifies `J(Q)/Phi A(Q)` canonically with the corrected four-class Phi-Selmer group.

Historical DX labels are not used.

## Rational curve points

Use the rational base point

`P0=(0,1)`

and the two rational points

`P+=(1,25/3)`,

`P-=(1,-25/3)`

on `C3_2`. Define rational Jacobian divisor classes

`D+=[P+-P0]`,

`D-=[P--P0]`,

and

`Dsum=D+ + D- = [P+ + P- - 2P0]`.

All four classes below are therefore represented by explicit Q-rational degree-zero divisors:

- `r0=0`;
- `r+=D+`;
- `r-=D-`;
- `rsum=Dsum`.

## Corrected Phi-Kummer labels

DU fixes the connecting functions

`F1=(t^2+4)(t^2+1/4)`,

`F2=(t^2+4)(t^2+9)`,

`F3=2(z+(t^2-1)^2)`.

Direct evaluation relative to `P0` gives

`delta_Phi(D+)=([1],[2],[6])`,

`delta_Phi(D-)=([1],[2],[-6])`.

Because the connecting map is a group homomorphism,

`delta_Phi(Dsum)=delta_Phi(D+) delta_Phi(D-)`.

Coordinatewise multiplication modulo squares gives

`([1],[2],[6]) * ([1],[2],[-6]) = ([1],[4],[-36]) = ([1],[1],[-1])`.

Also `delta_Phi(0)=([1],[1],[1])`.

Hence the four explicit rational divisor classes map bijectively to the four corrected global Phi-Selmer classes.

Since `Sha(A)[Phi]=0`, the connecting map `J(Q)/Phi A(Q) -> Sel^Phi(A/Q)` is an isomorphism. Thus these four classes are pairwise distinct modulo `Phi A(Q)` and exhaust `J(Q)/Phi A(Q)`.

## Exact representative set

An authoritative representative set is therefore

`R={0, D+, D-, Dsum}`.

This is stronger than the abstract existence statement in EA: no representative is left implicit.

## Local translation data

For every place `v`, the four translations used in the EA decomposition are the images of the same rational divisor classes under the natural diagonal localization

`J(Q) -> J(Q_v) -> J(Q_v)^hat_2`:

- `r0,v = 0`;
- `r+,v = [P+-P0]` viewed over `Q_v`;
- `r-,v = [P--P0]` viewed over `Q_v`;
- `rsum,v = [P+ + P- - 2P0]` viewed over `Q_v`.

No choice of p-adic lift is involved: the rational divisors themselves define the local points. Their corrected local Phi-Kummer labels are obtained by localizing the four global squareclass triples above, and the verifier replays those localizations at the certified place set `S={infinity,2,3,5,7}`.

Thus the four translated sets in EA are now concrete:

`loc_J(r) + Phi(loc_A(T_2 Sel(A)))`, for `r in {0,D+,D-,Dsum}`.

## What remains open

This leaf does not decide whether any of those four translated sets meets the retained-open Abel--Jacobi image. It does not compute the three elliptic pro-Selmer groups, the four translated intersections, a global 2-primary Brauer-set conclusion, a Brauer--Manin obstruction, fixed-p exclusion, receiver closure, endpoint closure, or Perfect Cuboid nonexistence.

## Next exact obligation

The next leaf should test the four concrete translated retained-open intersections using `R={0,D+,D-,Dsum}` and only the corrected DW/DX coordinate system.
