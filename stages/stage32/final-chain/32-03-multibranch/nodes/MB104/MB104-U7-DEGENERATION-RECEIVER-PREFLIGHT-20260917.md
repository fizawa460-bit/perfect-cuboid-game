# MB104 U7 receiver-preserving degeneration preflight — 2026-09-17

## Scope

This is a zero-credit preflight for the MB104 uniform-closure replacement-theorem search. It does not change MAIN, theorem, receiver, effectivity, endpoint, or merge credit.

The target is the retained balanced genus-one ray

```text
D_l = 7 l H - 4 l sum_(p in Sigma) E_p,
|Sigma| = 14,
l >= 1,
```

with the dangerous support mask `000707000f0f`, balanced exceptional contact `D_l.E_p = 8l` on each supported node, normalization genus one, and retained product-cover degree `e in {2,4}`.

## Exact receiver that a degeneration must preserve

A degeneration is useful only if a hypothetical MB104 carrier maps into a proper relative/logarithmic moduli problem preserving, with an exact semantic adapter, all load-bearing receiver data:

1. divisor class `D_l` (or an exactly identified specialization of it);
2. normalization genus one rather than merely arithmetic genus;
3. the exact fourteen-node support / mask `000707000f0f`;
4. the balanced contact total `8l` at every supported exceptional locus, without identifying contact mass, normalization-preimage count, and delta invariant;
5. the retained branch/contact passport needed by the MB104 local accounting;
6. the product-cover alternative `e in {2,4}` or an exact special-fiber replacement carrying the same obstruction;
7. no untracked splitting, vertical components, redistributed contacts, or new boundary components that weaken the receiver.

A degeneration of the divisor class or of `|D_l|` alone is insufficient.

## Repository preflight

Targeted repository searches for an MB104 degeneration, toric model, relative stable-map adapter, logarithmic stable-map adapter, or an existing `000707` degeneration produced no source-locked receiver-preserving adapter.

The archived MB104 research already records that fixed-component / conic / zero-quartic / local-jet variants do not by themselves close the balanced ray. Therefore those are not substitutes for the missing relative receiver.

## Why ordinary specialization is not enough

Properness of a stable-map compactification by itself does not preserve the MB104 semantic packet. A family of irreducible genus-one carriers can specialize to a reducible stable map; contact can move to extra components or boundary strata; and singularity/contact data can be redistributed while the total divisor class remains fixed.

Consequently, proving emptiness of a convenient special-fiber linear system would not imply MB104 emptiness unless the specialization map is first shown to carry every hypothetical MB104 carrier into the exact special-fiber receiver being excluded.

## Required new adapter

U7 becomes live only after source-locking both pieces below.

### A. Receiver-preserving proper specialization

Construct a relative/logarithmic moduli problem and prove an exact map

```text
MB104 hypothetical carrier
  -> relative/log stable object
  -> special-fiber receiver
```

that preserves the seven items above.

### B. Uniform special-fiber emptiness

On the resulting special fiber, prove either

```text
no receiver object exists for every l >= 1,
```

or

```text
no receiver object exists for l > L
```

with an explicit finite backend for `1 <= l <= L`.

## Verdict

```text
U7_STATUS=BLOCKED_PENDING_TARGET_DEGENERATION_ADAPTER
REPOSITORY_SOURCE_LOCKED_MB104_DEGENERATION_ADAPTER=false
DIVISOR_CLASS_ONLY_DEGENERATION_SUFFICIENT=false
ORDINARY_STABLE_MAP_PROPERNESS_SUFFICIENT=false
RECEIVER_PRESERVING_RELATIVE_LOG_ADAPTER_REQUIRED=true
U7_EXHAUSTED_GLOBALLY=false
MAIN_CREDIT=0
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
EFFECTIVITY_CREDIT=false
ENDPOINT_CREDIT=false
MERGE_AUTHORIZED=false
```

U7 is therefore parked, not mathematically disproved. The next high-level route should be a packet-sensitive global-incidence obstruction (U3) that acts directly on the simultaneous genus-one + balanced fourteen-node + product-cover receiver, rather than another divisor-class-only or counting-only argument.
