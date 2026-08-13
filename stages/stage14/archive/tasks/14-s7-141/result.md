# Stage14-s7-141 — exact q17-good pushforward intersection support

## Status

`COMPLETE_Q17_GOOD_PACKET_PUSHFORWARD_INTERSECTION_ENCODING`

Consumes merged `Stage14-s7-138..140` and merged `Stage14-Work-chX46` from main `43ed9a782d57986791644f8b9c1a9aa451445dbf`.

## 1. Freeze the two supports on one principal cell

Let `Lambda` be the already-charged retained filtered-tau3 witness support and let

```text
pi : Lambda -> Theta
```

be the deterministic pushforward to the frozen q17 reciprocal-CRT packet space from s7-138. Let

```text
P := pi(Lambda) subset Theta.
```

Let `G subset Theta` denote the q17-good packet support relevant to the already-frozen reciprocal-CRT receiver on the same packet cell. No new q17 arithmetic estimate is inserted here; `G` is only the target good support whose coverage must be tested.

Then the exact covered packet support is

```text
H := G intersect P.
```

and the uncovered good support is

```text
M := G \ P.
```

Thus exactly

```text
#G = #H + #M.
```

## 2. Coverage is an intersection problem, not an upper-fiber problem

Merged s7-140 and Work-chX46 give only the one-sided fiber envelope

```text
#{lambda in Lambda : pi(lambda)=theta} <= B^o(1).
```

That envelope does not control `#H/#G`. The unresolved lower-coverage direction is precisely the size of `G intersect pi(Lambda)`.

```text
S_Q17_GOOD_PUSHFORWARD_INTERSECTION_DEFINED=true
S_Q17_GOOD_PACKET_MISSING_SUPPORT_DEFINED=true
PUSHFORWARD_UPPER_ENVELOPE_RECHARGED=false
Q17_INNER_KERNEL_DEFICIT_RECHARGED=false
```

## 3. Scalar and pair measures remain distinct

For the scalar endpoint/fixed-product realizations, `Lambda` carries the scalar charged baseline. For the polynomial realization it carries the charged outer `(E,m)` baseline. The same set-theoretic intersection definition applies, but the two `Lambda` spaces are not identified and the pair branch is not scalarized through `Em`.

```text
S_GOOD_INTERSECTION_MEASURE_VARIANT_COUNT=2
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

## Boundary

```text
STAGE14_S7_141=COMPLETE_Q17_GOOD_PACKET_PUSHFORWARD_INTERSECTION_ENCODING
S_Q17_GOOD_PUSHFORWARD_INTERSECTION_DEFINED=true
S_Q17_GOOD_PACKET_COVERAGE_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-142
```
