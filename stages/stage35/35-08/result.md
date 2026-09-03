# Stage35 35-08 — proof experiments and exact quotient structure

```text
UNIT=35-08_PROOF_EXPERIMENTS_AND_COUNTEREXAMPLE_SEARCH
VERDICT=NEW_EXACT_STRUCTURE_NO_CLOSURE
FIVE_ELLIPTIC_QUOTIENTS_EXPLICIT=true
ALL_QUOTIENTS_SMOOTH_FOR_Q_GT_1=true
COUNTEREXAMPLE_TO_T35_R3_PHYS_EMPTY_FOUND=false
BOUNDED_FIBER_SEARCH_PERFORMED=false
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-09_DECISION_CERTIFICATE_OR_PARK
```

The selected fiber is put in the standard diagonal genus-5 form

```text
alpha*d^2+x^2=p^2
beta*d^2-x^2=y^2
d^2-x^2=q^2
alpha=((t^2-1)/(t^2+1))^2
beta=1-alpha.
```

Using González-Jiménez's exact diagonal-genus-5 formulas gives five elliptic quotient Jacobians `E0,...,E4`; all have full rational 2-torsion over `Q(t)`. `verify_35_08.py` computes `disc_X(f)` for each displayed monic cubic right-hand side `Y^2=f(X)`. These cubic RHS discriminants are nonzero for every rational `t>1`; the corresponding displayed Weierstrass discriminants are `16*disc_X(f)`, so the same smoothness conclusion follows. The earlier V1 wording that called `disc_X(f)` itself the elliptic/Weierstrass discriminant was a terminology error only; no nonvanishing conclusion changes.

Two generic boundary families are explicit after `d=1`: `x=0` gives `p=+/-sqrt(alpha)`, `y=+/-sqrt(beta)`, `q=+/-1`; `y=0` gives `x=+/-sqrt(beta)`, `p=+/-1`, `q=+/-sqrt(alpha)`. Since both square roots are rational functions of `t`, these provide at least 16 explicit `Q(t)` sections, all receiver-degenerate.

This does not prove that these are all generic sections. More importantly, even a complete `C(Q(t))` classification would not prove that every specialized `C_tau(Q)` point comes from a generic section. The load-bearing wall remains uniform exclusion of specialization-new physical points for all rational `tau>1`.

The Stage35 aggregate verifier/CI is the execution authority for this unit together with the other 35-01--35-09 promoted certificates; standalone verifier execution is not independently claimed.
