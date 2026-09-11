# Stage36 36-09EG — fixed-p=2 parameter-orbit impact source lock

## Scope

This leaf consumes only already-audited Stage36 authority:

- 36-09O: the physical top cover for an allowed rational physical base parameter `p`,
- 36-09EF: hostile-audited physical receiver exclusion at `p=2`,
- the 36-09EF hostile-audit PASS consumption receipt.

It asks how far the **same literal top curve** propagates the audited `p=2` exclusion in the positive physical parameter domain. It does not construct a finite exhaustive parameter ledger and does not claim full receiver closure.

## Generic physical top cover

From hostile-audited 36-09O,

```text
c(p) = (p+1)/(p-1)
C3_p: y^2 = (t^2+p^2)(t^2+p^(-2))(t^2+c(p)^2)(t^2+c(p)^(-2)).
```

The retained top boundary is always

```text
t = 0, +1, -1, infinity.
```

The positive fixed-p convention used by 36-09AW is primitive `p=a/b` with `a,b>0`, `gcd(a,b)=1`, `a!=b`; hence all of `2,1/2,3,1/3` are admissible physical base parameters.

## Exact p=2 literal-curve orbit

For `p=2`, `c(2)=3`, so the unordered coefficient multiset is

```text
S_2 = {4, 1/4, 9, 1/9}.
```

Direct exact substitutions give:

```text
p=2:   c=3,   S={4,1/4,9,1/9}
p=1/2: c=-3,  S={1/4,4,9,1/9}
p=3:   c=2,   S={9,1/9,4,1/4}
p=1/3: c=-2,  S={1/9,9,4,1/4}.
```

Therefore the four normalized genus-3 equations are literally identical over Q; no change of variable, twist, scalar extension, or squareclass branch is used.

Equivalently, the two elementary parameter operations visible in the coefficient set are

```text
p -> 1/p,
p -> (p+1)/(p-1),
```

with sign irrelevant after squaring the second operation. Starting from the positive parameter `2`, the positive literal-equation orbit is exactly

```text
{1/3, 1/2, 2, 3}.
```

Exactness of this positive literal-equation orbit is immediate: if a positive rational `q` has the same coefficient multiset as `C3_2`, then `q^2` itself is one of `4,1/4,9,1/9`, so `q` is one of the four displayed values. Each of the four passes the direct substitution above.

## Receiver consequence

36-09EF, hostile-audited on exact PR #1741 head `5ea451cdf0efdd87f57fc87d5ada881ac637a183` by review `5150902901`, proves

```text
U_ret(C3_2)(Q) = empty
```

and consumes the generic 36-09O forward physical adapter.

For every

```text
q in {1/3,1/2,2,3},
```

`C3_q` is literally `C3_2` and has the same retained boundary. Hence a retained physical receiver point over `q` would give a rational point of the same empty retained curve. Thus every one of these four positive fixed-p receiver sectors is empty.

## Credit ceiling

New exact mathematical impact intended by 36-09EG:

```text
excluded_positive_parameter_values = {1/3,1/2,2,3}
fixed_parameter_exclusion_registry_expanded = true
literal_C3_2_positive_parameter_orbit_complete = true
```

The following remain false:

```text
candidate_parameter_set_shrunk
receiver_emptiness_proved
R29_CAMP2_closed
Q11_CAMPEDELLI_closed
endpoint_closed
perfect_cuboid_nonexistence_claim
```

Reason: Stage36 has not consumed an authority-level finite exhaustive candidate ledger of physical rational parameters. Removing four points from the infinite positive rational parameter domain is genuine fixed-parameter exclusion progress, but it is not the repository's finite-candidate shrink credit.

## Next pressure point

The useful new question is no longer the already-excluded literal `C3_2` orbit. It is whether the p=2 Brauer mechanism, especially the rank-zero `rho` quotient and Q2 torsion forcing, extends to a nontrivial parameter family beyond this four-point literal-equation orbit.
