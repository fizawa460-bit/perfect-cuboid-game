# Stage14-Work-bpX28 receiver / capacity matrix

| Route | Outer coordinate | Support exponent | Atomic/fiber exponent | Required mass information | Live obstruction |
|---|---|---:|---:|---|---|
| Mainline heavy ray | exact radial scale `h` | `<=1/24` | `0` (`B^o(1)` reverse fiber) | concentrated exact-`C` mass exponent `eta>0`, but no uniform `eta>1/24` | short radial mass-capacity gap |
| s heavy factor A | squarefree kernel `kappa=sqf(F_*)` | polynomial on branch A | unresolved physical atomic capacity | polynomial factor support forced by s7-82/83 | correlated kernel support |
| s heavy factor B | square part `a` with fixed `kappa_*` | polynomial on branch B | unresolved physical atomic capacity | polynomial factor support forced by s7-82/83 | fixed-kernel square-part incidence |
| fixed-U boundary | scalar norm `g` on `k0*m*g in {1,2}` | `0` (`<=2` atoms) | uncontrolled principal atomic weight | support deficit requires near-total boundary weight | finite-boundary atomic concentration |
| fixed-U selected class | selected projective prime class | subpolynomial class dictionary | prime occupancy weight unresolved | near-total depletion required | selected-class depletion |

## Shared charged-once inequality

For nonnegative outer weights,

```text
M=sum_{x in S} w(x) <= |S| max_x w(x).
```

If

```text
|S|<=B^(sigma+o(1)),
max_x w(x)<=B^(omega+o(1)),
```

then

```text
M<=B^(sigma+omega+o(1)).
```

A required mass `B^(eta-o(1))` is impossible if `sigma+omega<eta`.

```text
OUTER_SUPPORT_CARDINALITY_AND_ATOMIC_WEIGHT_DOUBLE_CHARGE_FORBIDDEN=true
SUBPOLYNOMIAL_INNER_FIBER_RECHARGE_FORBIDDEN=true
COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false
COMMON_ATOMIC_WEIGHT_THEOREM_PROVED=false
```

The matrix intentionally does not identify `h`, `kappa/a`, and fixed-U `g`; only the abstract support-capacity accounting is common.
