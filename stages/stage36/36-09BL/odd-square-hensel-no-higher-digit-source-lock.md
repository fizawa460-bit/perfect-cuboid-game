# Stage36 36-09BL source lock: odd-prime square lifting has no independent higher-digit obstruction

This leaf is self-contained and uses only the elementary odd-prime Hensel square criterion together with the already source-locked Stage36 full-cover radicands.

Let `q` be an odd prime and `G in Q_q^*`. Write

```text
G = q^v * U,
U in Z_q^*.
```

Then `G` is a square in `Q_q` if and only if

```text
v is even
and
U mod q is a nonzero quadratic residue.
```

Necessity is immediate from valuations and reduction modulo `q`. For sufficiency, after removing the even power `q^v`, choose `y0` with `y0^2 = U mod q`. Since `q` is odd and `y0` is a unit,

```text
f(y)=y^2-U,
f'(y0)=2*y0 in Z_q^*.
```

The ordinary unit-derivative Hensel recursion uniquely lifts `y0` to `y in Z_q^*` with `y^2=U`. Thus there is no additional independent obstruction in the second or later q-adic digits once the exact valuation parity and first nonzero unit residue are fixed.

For the Stage36 AY/full-cover system, the two extra radicands are

```text
Gminus = (M^2*u^2-P^2*v^2)/kappa,
Gplus  = (M^2*u^2+P^2*v^2)/2.
```

Equivalently, with `Qsum=a^2+b^2` and `T^2=2*D0/kappa`,

```text
Gminus = Qsum^2*r^2 - 4*T^2*s^2,
Gplus  = Qsum^2*s^2 - kappa^2*T^2*r^2.
```

Therefore an old-six odd bad prime can add information only by changing or constraining

```text
v_q(Gminus),  unit_q(Gminus),
v_q(Gplus),   unit_q(Gplus),
```

through cancellation or coordinate-divisible branches. Once those exact leading data are known, there is no separate higher-digit square-root-lifting layer.

This does **not** assert that the AD/AE Legendre/Jacobi rows already determine the full-cover `Gminus/Gplus` leading data. They were obtained on the earlier coupled squareclass system and must not be double-charged as a complete full-cover local analysis. The exact remaining task is narrower: classify the old-six branches where the displayed full-cover radicands acquire extra valuation/cancellation and compute their first nonzero normalized residues.

No parameter shrink, receiver emptiness, fixed finite-S family, or endpoint closure follows from this Hensel reduction alone.
