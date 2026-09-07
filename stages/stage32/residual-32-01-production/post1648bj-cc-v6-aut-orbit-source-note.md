# Stage32 post1648BJ — `cc(V6)` versus the retained Aut orbit

Scratch-only bounded source/semantics note. This file grants no MAIN, receiver, route, theorem, endpoint, or perfect-cuboid credit.

## Question

Post1648BI proved that the retained V6 Picard class is not fixed by the retained `cc` action (actual complex conjugation). A possible repair would be that `cc(V6)` differs from `V6` only by an element of the retained surface automorphism group Aut of order 1536. If so, a semilinear class stabilizer could be formed by combining complex conjugation with an automorphism.

BJ tests exactly that finite question in saturated retained Picard64 coordinates.

## Source-bound actions

The V6 class is locked by

`stages/stage32/32-21/post1473-v6-witness-body-recovered.json`

with canonical SHA256

`d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`.

The retained known140/Picard64 adapter is loaded runner-side through

`stages/stage32/residual-32-01-production/hperp_integral_adapter.py`.

The two denylisted retained payloads are imported only on the runner; they are not whole-fetched into assistant/chat context.

For each retained Aut permutation `p` on known140 curves, BJ reconstructs its exact 64x64 Picard row-action matrix by mapping each retained Picard basis curve to the known140 coordinate row of `p(C)`. The diagnostic checks this action on all 140 known curve coordinate rows and checks the Picard Gram isometry identity.

Complex conjugation uses retained `picard_action_cc_64x64`; its semantic identification with actual complex conjugation comes from the already source-bound Stage33/33-07 Galois action chain used by BI.

## Exact finite result

The Aut orbit of V6 has size 1536, equal to the full retained Aut group order. Hence the V6 stabilizer in retained Aut is trivial.

Nevertheless `cc(V6)` is not in that 1536-element orbit. Equivalently, zero retained Aut elements send `V6` to `cc(V6)`.

Therefore the BI failure of pointwise complex-conjugation invariance cannot be repaired by composing complex conjugation with any retained Aut element.

## Historical V7/V8 hash clarification

`post1473-v6-witness-body-recovered.json` records fields named `prior_v6_artifact_canonical_sha256`, `prior_v7_artifact_canonical_sha256`, and `prior_v8_artifact_canonical_sha256`. These are versioned certificate/artifact commitments for the same retained V6 witness as it passed successive V6/V7/V8 verification layers; they are not three distinct Picard candidate classes.

The historical recovery producer at source head

`65ff870c15b8a1d859c4d9b84cd39ce89d9640c9`

wraps the unchanged V6 exact replay and reconstructs the same reduced translation, original translation, Picard coordinates, and all140 pairings only when the retained body hashes match. It does not materialize separate V7 or V8 class bodies. Future routing must not interpret those versioned hashes as candidate targets for `cc(V6)`.

## Scope firewall

BJ proves only a class-level finite orbit separation:

`cc(V6) notin Aut * V6`.

It does **not** prove that a V6 carrier exists or does not exist, does not produce a distinguished member of `|V6|`, and does not localize the normalization nonbijectivity required by post1648AH. In particular it gives no Q602/O210/O212+ advance.

The correct next mathematical route returns to the official member-level frontier: constrain the location/type of nonbijective normalization for any hypothetical integral genus-one V6 carrier, using genuinely new member-level or global singularity input rather than a Q-definedness/Aut repair argument.
