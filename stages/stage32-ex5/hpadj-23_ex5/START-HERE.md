# Stage32EX5 HPADJ23 — exact feasible-t support producer

Status: **BOUNDED STRUCTURAL STRICTNESS RETAINED / PRODUCER ONLY / ZERO MAIN CREDIT**

## Why this leaf exists

V48 consumes a 384-coordinate support-qBC refinement, but that consumer deliberately replaces the true feasible `t` set by a parity interval hull. The 32-01-178 research note already records preserving feasible `t` holes as `UNTESTED`; therefore EX5 must not duplicate the 178 consumer computation.

EX5 instead owns the producer refinement: retain exact `t` in the HPADJ22 joint BC state, producing a histogram keyed by `(b,c,support,required_parity,qBC,t)`.

## Retained bounded gate

The independent H=4 replay proves the proposed producer is genuinely stricter than the current hull representation:

- 686 valid canonical BC tuples;
- 151 exact bins with required parity; 91 are strict against the current hull;
- 146 hull-only `t` points are removed across those strict bins;
- after marginalizing required parity, 101 bins remain and 52 are still strict;
- 74 hull-only `t` points remain removable after that marginalization;
- witness: `(b,c,support,qBC)=(0,4,1,16)` has exact `t={0}`, while the current safe hull is `{0,2,4}`.

This is structural producer evidence only. No V48 coordinate was recomputed and no global numerical tightening is claimed.

## Ownership / anti-duplication

- producer: Stage32EX5;
- producer output: exact joint BC/t histogram interface;
- downstream consumer: `32-01-178`, which retains ownership of any V48-or-successor same-population intersection;
- EX5 does not run the 178 consumer or claim its savings;
- MAIN promotion requires a later source/target adapter and hostile audit.

## Next exact gate

Implement a scalable source-locked histogram builder keyed by `(b,c,support,required_parity,qBC,t)`. It must reproduce the existing HPADJ22 qBC and required-parity marginals exactly before any downstream handoff. Keep heavy scaleout cold.

Merge is not authorized.
