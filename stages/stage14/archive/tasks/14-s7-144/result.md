# Stage14-s7-144 — exact good-packet indicator correlation encoding

## Status

`COMPLETE_Q21_GOOD_PACKET_INDICATOR_CORRELATION_ENCODING`

Consumes merged Stage14-s7-141..143 and merged Work-ciX47/q21.

Let `Lambda` be the retained conditioned s witness set on one frozen principal cell, `pi: Lambda -> Theta` the already-proved deterministic pushforward to q17 reciprocal-CRT packets, and `G subset Theta` the q17-good packet support frozen by the preceding stages.

Define the Boolean good-packet indicator on witnesses

```text
Y(lambda) := 1_G(pi(lambda)).
```

Then the q17-good hit-witness support is exactly

```text
Lambda_G := {lambda in Lambda : Y(lambda)=1}
```

and its cardinality is the exact correlation first moment

```text
M1_G := sum_{lambda in Lambda} Y(lambda) = #Lambda_G.
```

Equivalently, with packet occupancy

```text
a(theta) := #{lambda in Lambda : pi(lambda)=theta},
```

we have

```text
M1_G = sum_{theta in G} a(theta).
```

This is an identity, not an independence statement. All filtered-tau3 conditioning, frozen packet labels, primitive/orientation conditions, and branch-specific charged measure remain inside `Lambda` and `a(theta)`.

For the polynomial branch the outer charged variable remains `(E,m)`; the notation `theta` does not scalarize the outer pair through `Em`.

```text
Q21_GOOD_PACKET_INDICATOR_CORRELATION_ENCODING_TEST=PASS
S_GOOD_PACKET_INDICATOR_FIRST_MOMENT_EXACT=true
S_GOOD_PACKET_FIRST_MOMENT_EQUALS_HIT_WITNESS_SUPPORT=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
Q17_INNER_KERNEL_DEFICIT_RECHARGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-145
```