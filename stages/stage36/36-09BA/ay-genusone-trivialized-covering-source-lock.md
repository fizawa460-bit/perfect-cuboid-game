# Stage36 36-09BA source lock: rationally trivialized genus-one 2-covering

This leaf uses no new external theorem species beyond the full-2 homogeneous-space / genus-one covering framework already source-locked in 36-09AH, 36-09AI, 36-09AJ and 36-09AN.

## Locked framework

- `36-09AH` proves the common-u:v intersection is a smooth genus-one curve `C/Q`.
- `36-09AI` identifies its Jacobian as the congruent-number curve `E_n: Y^2=X^3-n^2 X` and identifies `C` as a 2-covering.
- `36-09AJ/full2-homogeneous-space-source-lock.md` source-locks the standard full-rational-2-descent homogeneous-space construction (Roberts §3.2.2, with the standard number-field proof cited there to Silverman, Chapter X §1).
- `36-09AN` gives the exact rational covering map on the affine chart and proves the normalized `E_n(Q)` torsion group is exactly `Z/2 x Z/2`.

## Standard consequence used here

For a genus-one torsor/2-covering `C` of its Jacobian `E`, a rational point `P0 in C(Q)` trivializes the torsor: after choosing `P0` as origin, `C` is an elliptic curve over `Q` isomorphic to its Jacobian `E`. Hence `C(Q)` is infinite whenever `E(Q)` has positive Mordell-Weil rank.

This is used only at the abstract genus-one/torsor level. No explicit birational-coordinate transport is claimed from this statement; S31-W01 remains required if a later leaf needs exact forward/inverse rational functions with exceptional-locus accounting.

## Stage36 specialization

The hostile-audited AY construction provides a rational point on the common-u:v genus-one covering. At that point all `u,v,r,s` are nonzero. Under the exact AN covering map its elliptic image has `y != 0`. Since AN proves the rational torsion is exactly the four 2-torsion points, this image has infinite order. Therefore `rank E_n(Q) >= 1`, and the rationally trivialized AY genus-one covering has infinitely many rational points.

The boundary equation `Lminus=0` is not promoted to an identically vanishing equation on the covering. AZ classifies its positive primitive `U:V` rational coordinate uniquely. Thus only finitely many sign/projective lifts of rational points lie over that boundary coordinate, while the genus-one covering has infinitely many rational points. Consequently there are rational points on the auxiliary AY covering with `Lminus != 0`.

## Firewall

The auxiliary common-u:v 2-covering does not by itself impose the original top receiver's two separate `Fminus` / `Fplus` square conditions. Infinite/open rational points on this genus-one covering therefore do **not** imply a Stage36 retained receiver point. The remaining task is the exact receiver-restricted intersection required by formal Arsenal card `S34-W03`.
