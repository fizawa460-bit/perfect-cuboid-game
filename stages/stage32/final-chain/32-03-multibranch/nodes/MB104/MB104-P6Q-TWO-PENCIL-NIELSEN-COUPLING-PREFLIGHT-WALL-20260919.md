# MB104 P6Q — two-pencil Nielsen coupling preflight wall — 2026-09-19

Status: **PRE-AUDIT EXACT KUMMER-EQUIVALENCE WALL / NO CREDIT**

## Input

Retained P6D2/P6H give two degree-`56l` maps

```text
psi_1, psi_2 : E -> P1
```

whose pullbacks of the fixed full deck cover reconstruct the same labelled

```text
G ~= (Z/2)^3
```

cover

```text
Z -> E.
```

P6K already records the three basis-character equalities in

```text
k(E)^* / k(E)^{*2}.
```

P6Q asks whether simultaneous Nielsen/monodromy coupling of the two pencils contains any further invariant.

## 1. Labelled elementary-2 covers are Kummer data

Over the retained characteristic-zero function field `K=k(E)`, a labelled elementary abelian 2-extension with group

```text
G=(Z/2)^3
```

is determined by a three-dimensional labelled Kummer subspace

```text
V subset K^*/K^{*2}.
```

After choosing the retained basis characters `chi_1,chi_2,chi_3`, one may write

```text
K(Z)=K(sqrt(f_1),sqrt(f_2),sqrt(f_3)).
```

Equality of the same labelled cover is exactly equality of these three character square classes, up to multiplication by squares in `K^*`.

This is precisely the content frozen in P6K:

```text
[q_j o psi_1] = [q_j o psi_2]
    in K^*/K^{*2},   j=1,2,3.
```

All four remaining nontrivial characters are products of the basis three and therefore add no independent square-class datum.

## 2. What Nielsen data would additionally require

A Nielsen class for a map to `P1` also remembers a chosen ordered/unordered branch-value configuration and local monodromy tuples around those branch values.

The common labelled cover `Z->E` does not by itself identify:

- the individual six branch values of `psi_1` with those of `psi_2`;
- an ordering of those values;
- a factorwise node-to-branch-value pairing;
- braid/Nielsen representatives for the two `P1` maps.

Those are exactly the missing data encountered in P6N/P6O.

Hence any simultaneous Nielsen invariant that compares the two `P1` presentations beyond their common labelled Kummer extension needs branch-value/presentation data not retained by the current packet.

## 3. Exact disposition

```text
same labelled G-cover                        = exact,
three basis-character square classes equal  = exact,
remaining character classes                 = products of the basis classes,
extra intrinsic labelled-cover invariant    = none at this level,
simultaneous branch-value Nielsen class      = not defined from retained data.
```

Therefore P6Q reduces to P6K at the intrinsic common-cover level. Repackaging the same three square classes as a Nielsen constraint is not a new obstruction.

## 4. Next shallow route

The P6H--P6Q two-pencil/common-cover package has now exhausted:

- line-bundle equality;
- character square classes;
- complex centralizer;
- branch-value incidence without a modular adapter;
- Wronskian class data;
- intrinsic labelled-cover/Nielsen coupling.

Rotate back to the surface-side isolated-carrier information from P6F.

Next leaf:

```text
MB104-P6R-EQUIGENERIC-ISOLATION-VERSUS-LINEAR-SYSTEM-DIMENSION-PREFLIGHT
```

Target: compare the exact zero equigeneric tangent space from P6F with the dimension of the complete linear system `|lP|` and the expected codimension imposed by the exact genus drop

```text
delta = 168 l^2 + 56 l.
```

The gate must remain dimension-theoretic only: determine whether isolation plus Riemann--Roch/vanishing can produce a contradiction or a finite-`l` window. Stop immediately if the Severi expected codimension exactly cancels the quadratic growth or if required vanishing is unavailable.

## Firewalls

```text
new_nielsen_obstruction=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
