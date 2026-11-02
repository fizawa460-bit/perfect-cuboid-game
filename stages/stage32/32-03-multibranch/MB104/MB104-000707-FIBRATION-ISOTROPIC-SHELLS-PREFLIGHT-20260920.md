# MB104 — 000707 degree-10/12 fibration isotropic-shell preflight — 2026-09-20

Status: **PRE-AUDIT / COLD EXECUTION PREFLIGHT / NO NUMERICAL RESULT / NO CREDIT**

## Purpose

This is the MB-native finite enumeration requested for the only remaining possible improvements to the known
`P.F=40` size-768 fibration value on support `000707000f0f`.

It does not repeat the 32-01 FULL178 fibration-nef weighted-pruning route.  It reuses only the retained exact
Picard64 / H-perp machinery and the MB Z40 `CloseVectors` pattern.

## Exact shells

For
`P=7H-4 sum E_i`, `P^2=336`, `H.P=112`, the four numerical workunits are:

- degree 10, `P.F=30`, support mass 10, `x=8F-5H`, `-x^2=400`, `x.P=-320`;
- degree 10, `P.F=34`, support mass 9, `x=8F-5H`, `-x^2=400`, `x.P=-288`;
- degree 10, `P.F=38`, support mass 8, `x=8F-5H`, `-x^2=400`, `x.P=-256`;
- degree 12, `P.F=36`, support mass 12, `y=4F-3H`, `-y^2=144`, `y.P=-192`.

The fixed-P-pairing problem is an affine coset of the rank-62 kernel inside rank-63 H-perp.  The runner completes
the quadratic form exactly, clears denominators, and calls Magma `CloseVectors`.

A candidate is retained only after:

1. exact Picard64 divisibility/integrality of F;
2. nonnegative pairing with all retained known 140 curves;
3. primitivity in the integral Picard basis.

The certificate deliberately calls this **known140-nonnegative**, not global nef.

## Resume/storage boundary

The four shells are independently executable workunits.  The conservative pilot is shell 0 (degree 10,
norm 400).  Scale-out is not authorized until a pilot measures runtime and compact-certificate size.

Planned effective heavy concurrency is 1, leaving 17 Stage slots of headroom.  Raw Magma stdout is not persisted;
only a verified compact certificate may be uploaded, with one-day retention if execution is later authorized.

## Why execution is cold here

The current lane `STATE.json` is 68,425 bytes, above the repository's 64 KiB context-safe whole-fetch boundary.
It still names the now-completed R4 shallow portfolio as `next_obligation`.  This session therefore does not
silently whole-fetch/replace STATE and does not claim an ACTIVE_AUTO transition.

The dedicated runkey is generation 0 / COLD / unarmed.  A future exact state transition may promote this leaf and
arm one pilot generation; unrelated PR synchronizations must remain cold.

## Result interpretation

If all four numerical candidate sets are empty, that is still a numerical Picard64 statement first.  Combining it
with the retained degree-8 exhaustiveness and Z40B degree reduction into a global `min P.F=40` theorem requires
its own audited composition step.

If candidates remain, the next geometry is already finite:

- degree 10: sextic residual = quartic+conic or conic+conic+conic, plus exceptional components;
- degree 12: `QA+QB+degree4 residual`, plus exceptional components.

No MAIN, theorem, effectivity, receiver, endpoint, MB104-completion, Perfect-Cuboid, merge, or global-fibration-
optimum credit is granted here.
