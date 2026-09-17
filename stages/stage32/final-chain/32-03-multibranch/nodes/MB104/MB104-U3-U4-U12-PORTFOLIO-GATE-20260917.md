# Stage32 MB104 — U3/U4/U12 portfolio gate — 2026-09-17

Status: **SHALLOW PORTFOLIO UPDATE / U4 REJECTED AS DISTINCT ROUTE / U3 DIRECT IMPORT NOT FOUND / U12 HOLD / NO CREDIT**

## Scope

This note continues from exact PR-head checkpoint
`fe14314664dca817c04caa951f39f5457ae2c9fa`.  It compares the three live
high-level continuations after the split-prime `J[2]` injectivity wall.  It does
not reopen the archived ambient-`H1`/Picard, conductor-sign, fixed-jet,
counting-only, ordinary-effectivity, or generic-correspondence routes.

## U4: no separate eventual-degree route

The standard split-prime Bolza Hecke degree is `p+1`.  Degree compatibility with
the current `000707` packet permits

```text
p+1=56l,
p == 55 (mod 56).
```

Thus the arithmetic index spectrum itself has no eventual upper bound.  The
remaining node/spin/passport data are finite-level conditions.  Once a precise
finite quotient is supplied, they have the following natural dichotomy:

1. every admissible residue/double-coset class is empty, giving an all-`l`
   exclusion; or
2. an admissible class survives and is compatible with infinitely many split
   primes, so no cutoff `l>L` follows from that finite-level datum.

Consequently this computation belongs to U12, not to a distinct U4 route.
For the size-48 quotient branches the obstruction is even clearer: composition
with elliptic multiplication maps produces unbounded degrees whenever one
compatible isogeny exists.  Quotient/passport data alone cannot yield `L`.

Verdict:

```text
U4_DISTINCT_LARGE_L_ROUTE=REJECT
U4_COMPUTATION_DUPLICATES_U12=true
```

## U3: global theorem imports fail at the first adapter gate

No retained Arsenal card simultaneously consumes normalization genus one, the
exact balanced fourteen-node packet, and the product-cover passport.

The strongest shallow candidate was a divisor-morphism extension theorem:
extend one degree-two map from the dangerous lifted curve to the smooth
Beauville surface `Y`.  The direct adapter fails before its numerical
hypotheses can be used.  The retained object

```text
pi:B->E
```

is the normalization of the pullback of a singular carrier to `Y`; it is not
source-locked as a smooth closed divisor embedded in `Y`.  Replacing its
singular image by a strict transform requires resolving precisely the
collision/conductor geometry that the portfolio firewall parks.  Therefore a
smooth-divisor extension theorem is not a legal direct import.

Stable-spin-boundary and spin-Hurwitz alternatives also lack an adapter:
surface-node normalization branches have not been converted to stable-curve
nodes/admissible-cover data, and the relevant simple ramification is not the
standard odd-profile spin-Hurwitz input.

Verdict:

```text
U3_READY_GLOBAL_THEOREM_FOUND=false
U3_SMOOTH_DIVISOR_EXTENSION_DIRECTLY_APPLICABLE=false
U3_REENTRY_REQUIRES_NEW_SINGULAR_IMAGE_PACKET_THEOREM=true
```

## U12: exact finite test exists, but its inputs are absent

For one explicit primitive split-prime double coset, compare the two pullbacks
of the six odd spin structures on a Reidemeister--Schreier generating set of
the common subgroup.  Equivalently, compare the two metaplectic/spin
multipliers directly; this is a cross-leg equality test, not a one-leg kernel
argument.

The first prime compatible with the elementary degree congruence is

```text
p=167,
p+1=168=56*3,
g(B)=169.
```

The finite test would perform `6*6=36` comparisons.  The current repository,
however, source-locks only the reduction/Borel model and the linear `J[2]`
injectivity.  It does not materialize both of the following inputs:

- an explicit quaternion/double-coset representative giving the second
  subgroup embedding at `p=167`;
- compatible explicit lifts of the six odd theta multipliers to the required
  spin/metaplectic extension.

Without those inputs the `p=167` test is not executable from the current
checkpoint.  Even a successful single-prime exclusion closes only that double
coset and its symmetry orbit.  All-`l` promotion would additionally require a
proof that the cross-leg affine spin difference factors through one fixed
finite quotient, followed by exhaustive enumeration of its classes.

Verdict:

```text
U12_SINGLE_DOUBLE_COSET_METHOD=HOLD
U12_P167_EXECUTABLE_FROM_CURRENT_REPO=false
U12_FIXED_FINITE_QUOTIENT_FACTORIZATION_PROVED=false
```

## Updated frontier

The shallow portfolio has not produced a new closure theorem.  It does remove
U4 as a separate branch and prevents an invalid direct U3 import.  The only
precise retained continuation is:

```text
U12-FINITE-LEVEL-ADAPTER:
  source-lock an explicit split-prime double-coset representative and odd-spin
  lifts, then determine whether the cross-leg spin/passport predicate factors
  through a fixed finite quotient.
```

If that factorization cannot be proved, U12 remains a collection of isolated
finite tests and must not be presented as an all-`l` replacement theorem.

## Firewalls

```text
MB104_complete=false
finite_degree_window_proved=false
all_l_exclusion_proved=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
