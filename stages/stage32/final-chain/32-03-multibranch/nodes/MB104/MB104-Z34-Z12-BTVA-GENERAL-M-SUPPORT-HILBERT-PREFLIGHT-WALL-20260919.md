# MB104 Z34 / Z12 — BTVA general-m support-Hilbert preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-COMPLETE ASYMPTOTIC SIGN + EXTERNAL-ANCILLARY INTERFACE WALL / NO CREDIT**

## Target

Z32R was parked because the retained repository had no executable general-`m` generator for

```text
V_m(T)=ker(W_m -> direct_sum_(s in T) Q_(s,m))
```

together with multiplication/Hilbert data separating the known support-hyperplane-generated submodule.

Z32S located the published BTVA perfect-cuboid ancillary package. Z34 checks whether that publication surface actually supplies the missing general-`m` interface.

## Published source

Bruin--Thomas--Várilly-Alvarado,
*Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*,
Algebra & Number Theory 16 (2022), arXiv:1912.08908v3.

The arXiv v3 record lists the ancillary files

```text
perfectcuboid_script.m
perfectcuboid.out
readme.txt
```

among the electronic resources.

The paper's Section 5 gives an abstract construction for arbitrary symmetric order `m`:

```text
M_X
 -> S^m M_X
 -> (S^m M_X)^{vee vee},
```

implemented in principle by Gröbner-basis software.

However the paper explicitly states that current technology executes these ideas only for small values of `m`.

For the perfect-cuboid surface itself, Section 7 source-locks one explicit calculation:

```text
m=2,
h^0(X, hat S^2 Omega_X^1)=13.
```

The 13 generators are the seven displayed forms together with the six linear multiples of omega_7.

The paper also says that the asymptotic Euler-characteristic lower bound for the perfect-cuboid application only becomes positive at `m>=862`, which is outside the explicit computational range used there.

Thus the publication distinguishes:

```text
abstract arbitrary-m construction          = mathematical algorithm,
perfect-cuboid executable demonstrated run = m=2,
large-m asymptotic bound                    = theorem/formula, not explicit module build.
```

The ancillary byte stream could not be independently opened through the available arXiv cache in this preflight, so no stronger claim about an undocumented script parameter is made.

## Exact N-support cubic coefficient

BTVA Proposition 3.1 gives, for `ell=48` A1 nodes and `r` exceptional components removed,

```text
h^0 >= chi(Y,S^m Omega_Y^1)
       + 48 chi^1_A1(m)
       + r chi^0_A1(m).
```

For the cuboid resolution

```text
K^2=16,
c2=80.
```

The cubic coefficients source-locked in the paper are

```text
chi(Y,S^m Omega_Y^1):  -32/3,
chi^1_A1(m):             4/27,
chi^0_A1(m):            11/108.
```

For a curve meeting at most `N` nodes, the BTVA partial-information application takes

```text
r=48-N.
```

Hence the exact cubic coefficient is

```text
c_N
 = -32/3 + 48*(4/27) + (48-N)*(11/108)
 = (144-11N)/108.
```

Therefore

```text
N=13: c_13 =  1/108 > 0,
N=14: c_14 = -10/108 = -5/54 < 0.
```

This exactly source-locks the retained Stage32 statement that ordinary BTVA changes sign at the N=14 frontier.

## Why the ancillary does not reopen Z32R

The missing object is not merely the formal recipe for `S^m M_X`. Z32R needs an executable graded family that can:

1. materialize the perfect-cuboid `W_m` and local extension maps for variable/general `m`;
2. retain multiplication maps in `m`;
3. impose the *specific* active support conditions;
4. quotient the known hyperplane-generated architecture;
5. certify a positive primitive cubic Hilbert coefficient.

The publication supplies exact local quasi-polynomials and the general abstract module construction, but its perfect-cuboid explicit application is `m=2`. It does not publish a support-specific primitive Hilbert series at `N=14`.

The ordinary asymptotic theorem is already strictly negative there:

```text
-5/54 m^3 + O(m^2).
```

Consequently neither the general formal construction nor the existence of the ancillary filenames is a source-complete replacement for the missing graded interface.

No inference

```text
perfectcuboid_script.m exists
  => executable symbolic general-m family
  => positive primitive support Hilbert coefficient
```

is authorized.

## Disposition

```text
BTVA ancillary existence source-locked           = true,
arbitrary-m abstract construction source-locked  = true,
perfect-cuboid explicit m=2 computation           = true,
N=14 cubic coefficient                            = -5/54,
general-m executable perfect-cuboid interface     = not source-locked,
primitive support-specific cubic growth positive = not proved.
```

Z34 restores the Z32R wall.

## Next route

The directly executable Z3/null-locus route has produced one 768-support orbit elimination and then hit a first-neighborhood interface. Z12 has now also returned to an external general-`m` interface.

Per the current Z1--Z30 re-audit, move to the strongest theorem-dependent population-wide candidate:

```text
MB104-Z35-Z2-ORBIFOLD-CANONICAL-DEGREE-THEOREM-PREFLIGHT
```

Target: locate a source-valid orbifold/log canonical-degree inequality that applies to an integral multibranch curve on the singular 48-A1 canonical cuboid model and has a coefficient strong enough to beat the exact N=14 equality packet. Reject smooth-curve or orbifold substitutions whose hypotheses do not include the current singular carrier.

## External source anchors

- arXiv:1912.08908v3, ancillary inventory.
- BTVA Section 1.3: explicit module methods executable for small `m`.
- BTVA Proposition 3.1: partial-regularity lower bound.
- BTVA Propositions 3.3 and 3.7: exact A1 local Euler characteristics.
- BTVA Section 7: perfect-cuboid `m=2` computation and N=13 asymptotic application.

## Firewalls

```text
general_m_generator_recovered=false
primitive_hilbert_growth_positive=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
