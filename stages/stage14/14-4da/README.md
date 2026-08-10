# Stage14-4da

Stage14-4da consumes merged `Stage14-4cz`, merged `Stage14-s7-41`, and the earlier exact reciprocal reconstruction / common-core column results on latest main.

The entering canonical theorem is

```text
V(B) << B^(23/44+o(1)).
```

The decisive point is a quantifier bridge that is stronger than the final bookkeeping of merged s7-41.

Merged s7-41 correctly proves that the first residual and the two short row/column coordinates are finite-fiber descriptions of the same `1/11` freedom, and correctly forbids reusing the common-core root line in the reverse direction without a bridge. Stage14-4da does **not** reuse that root line.

Instead, after the legal column order has fixed the primitive pair `(U,V)` and reconstructed the integer `M`, use the two original reciprocal identities in reverse:

```text
(aU)^2-(bV)^2 = 4rs epsilon_k pq,
(cp)^2-(dq)^2 = 4XY epsilon_x UV.
```

The column-fixed `M` fixes `XY` up to endpoint-small data already conditioned at `B^o(1)` cost. Hence the second equation has fixed right-hand side and its positive difference-of-squares factorization gives only divisor-many `(c,d,p,q)`. Those values fix the right-hand side of the first equation, which then gives only divisor-many `(a,b)`.

Therefore

```text
fixed legal outer decoration + (U,V,M)
=> #(a,b,c,d,p,q)=B^o(1)
=> #N=abcd=B^o(1).
```

The Cayley-row `N` lift is consequently a filter, not an independent polynomial support:

```text
ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false.
```

On the surviving nonproportional low-core region `chi<=1/4`, the only fixed-power costs are

```text
common core C                         : chi,
primitive common-core pair (U,V)     : 2phi-chi,
reduced endpoint-linear column       : 1/4-chi,
post-column reverse reciprocal row   : 0.
```

Thus

```text
E_RRF <= 2phi+1/4-chi = 1-2theta.
```

Combine this with:

```text
E_k <= 3theta-1/4,
E_prop <= 7/16,
chi>1/4 nonproportional fixed-power packets empty.
```

For `theta<=1/4`, `E_k<=1/2`. For `theta>=1/4`, the reverse-reciprocal bound is `<=1/2` whenever the packet is nonempty. Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
IMPROVEMENT_OVER_23_44=1/44
SQRT_B_UPPER_BOUND_PROVED=true
V(B) << B^(1/2+o(1)).
```

No fixed positive saving below `1/2` is claimed.

The possible square-root saturation band is now

```text
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4,
```

where `H=B^(s+o(1))`. The remaining receiver for any strict sub-square-root improvement is

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence.
```

### H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
S7_41_MAINLINE_H_GATE_SUPERSEDED=true
GENERIC_GENUS_ONE_H_REOPENED=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
```

The s7-41 H request was a valid request at its receiver boundary, but it is no longer a mainline blocker because 4da supplies the missing deterministic quantifier bridge without reverse root-line reuse.

Parallel X13 contains a compatible reverse-reciprocal square-root result, but it is not used as a hard predecessor or CI dependency of 4da.

Next: `Stage14-4db`.
