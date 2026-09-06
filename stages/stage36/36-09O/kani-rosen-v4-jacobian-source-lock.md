# Stage36 36-09O source lock: Klein-four Jacobian decomposition

Accessed: 2026-09-06

Primary reference:
- E. Kani and M. Rosen, *Idempotent relations and factors of Jacobians*, Mathematische Annalen 284 (1989), 307–328.
- DOI: https://doi.org/10.1007/BF01442878
- EuDML bibliographic record: https://eudml.org/doc/164555

Exact consequence used in 36-09O:

For a curve `C` with a Klein four subgroup `G={1,sigma,tau,sigma*tau}` and its three order-two subgroups `H_sigma,H_tau,H_sigma_tau`, the Kani–Rosen idempotent relation gives

`Jac(C) x Jac(C/G)^2  ~  Jac(C/H_sigma) x Jac(C/H_tau) x Jac(C/H_sigma_tau)`

up to isogeny.

In the Stage36 36-09O family, the full `G` quotient is genus zero, so its Jacobian is trivial. Hence the exact specialized consequence is

`Jac(C3) ~ E_sigma x E_tau x E_sigma_tau`.

Independent Stage36 check:
- the three quotient maps are written explicitly;
- their pulled-back invariant differentials are respectively proportional to
  `t dt/y`, `(1-t^2) dt/y`, `(1+t^2) dt/y`;
- these three forms are linearly independent and span the genus-three hyperelliptic differential space.

Thus the source theorem and the direct differential calculation agree on the decomposition used here.

Credit boundary:
- this source grants an isogeny decomposition only;
- it does not compute the Mordell–Weil ranks of the two newly exposed quotient families;
- it does not classify `C3(Q)`, exclude physical square lifts, exclude rank jumps, or close the Stage36 receiver.
