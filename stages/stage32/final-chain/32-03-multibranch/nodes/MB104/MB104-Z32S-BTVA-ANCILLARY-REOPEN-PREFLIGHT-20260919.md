# MB104 Z32S — BTVA ancillary reopen preflight — 2026-09-19

Status: **PARALLEL RESEARCH PREFLIGHT / REOPEN CANDIDATE / NO CREDIT**

## Purpose

This note deliberately does not follow the current P6N active leaf. It tests a parked child from the
span-five branch:

```text
MB104-Z32R-PRIMITIVE-SUPPORT-HILBERT-GROWTH
```

The Z32R wall parks this route because the retained repository surface has no executable exact
general-`m` generator for the reflexive symmetric-differential spaces and their local extension
maps.

## External source recovery

Bruin--Thomas--Várilly-Alvarado,
*Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*,
Algebra & Number Theory 16 (2022), arXiv:1912.08908, gives an explicit graded-module
construction for the reflexive symmetric differentials on nodal complete intersections.

The paper states that these module operations are executable by Gröbner-basis software and
provides electronic resources specifically for the perfect-cuboid surface. The arXiv ancillary
inventory includes

```text
perfectcuboid_script.m
perfectcuboid.out
readme.txt
```

and the paper's Section 5 describes the construction from the projective cotangent module,
the conormal relations, symmetric powers, and double dual.

This matters because the previous Z32R disposition only searched the retained repository and
historical MB archive. It did not treat the published BTVA ancillary package as an executable
source surface.

## What this does NOT yet reopen

The same paper explicitly says that current technology executes these constructions for
small symmetric order `m`. Z32R requires substantially more:

```text
V_m(T)=ker(W_m -> direct_sum_{s in T} Q_{s,m})
```

as a graded family in `m`, together with enough multiplication/Hilbert data to separate the
support-hyperplane-generated architecture and certify a primitive cubic coefficient.

Therefore the mere existence of `perfectcuboid_script.m` does not satisfy the Z32R reopen
trigger.

In particular, no inference of the following form is authorized:

```text
published fixed-m Magma computation
=> symbolic general-m module
=> primitive Hilbert coefficient > 0.
```

## New legal subgate

The parked child now has a narrower externally sourced subgate:

1. recover and source-lock the BTVA perfect-cuboid ancillary script/output;
2. determine whether the script builds the abstract module from the defining quadrics for an
   input symmetric order, or only replays a fixed order;
3. isolate which objects can be made uniform in `m` without rebuilding the whole BTVA
   machinery;
4. test whether the exact local A1 extension codimensions plus a global Hilbert polynomial
   already give a support-specific cubic lower bound for `V_m(T)`;
5. only if that coefficient is positive, address subtraction of the known support-hyperplane
   submodule.

A negative answer at steps 2--4 restores the Z32R wall. A positive answer would genuinely
satisfy the missing-interface part of the reopen trigger.

## External source locks

- arXiv:1912.08908v3, ancillary inventory:
  `perfectcuboid_script.m`, `perfectcuboid.out`, `readme.txt`;
- BTVA22 Section 5: explicit graded-module construction of reflexive symmetric differentials;
- BTVA22 Theorem 1.4 / A1 local Euler-characteristic formulas: possible asymptotic
  coefficient source, but not yet adapted to the support-specific primitive kernel.

## Current conclusion

```text
Z32R mathematically closed = false
Z32R executable from retained repo alone = false
published external generator candidate found = true
general-m uniformity proved = false
primitive cubic coefficient proved positive = false
finite_degree_window_proved = false
MB104_complete = false
receiver_credit = false
theorem_credit = false
endpoint_credit = false
merge_authorized = false
```

This note is intentionally parallel-only and does not change `STATE.json` or the current active
P6 frontier.
