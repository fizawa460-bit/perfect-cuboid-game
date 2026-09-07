# Stage32 post1648J — Cecotti B.7/B.8 trace-orientation correction

## Scope

This leaf corrects the orientation preflight in post1648B for the fixed Stage32 target
`g1-d186`, `O=210`, `q'=4`, `Q=602`.

Current arithmetic credit remains

`[73,97,235]`.

Post1648B deliberately treated

`phi2 -> S=b4`, `phi6 -> T=-b3`

as a conditional marked-generator hypothesis. It was never promoted. The present leaf
tests that *specific* hypothesis against the holomorphic-differential representation of
the explicit Cecotti B.7/B.8 curve automorphisms.

## External source

Cecotti, arXiv `2509.24605v1`, Appendix B:

- (B.3): `S=b4`, `T=-b3`;
- (B.6): the ppav is the Jacobian of `C0: y^2=x^5-x`;
- (B.7):
  `x -> -(x+i)/(1+i*x)`,
  `y -> 2*sqrt(2)*y/(1+i*x)^3`;
- (B.8):
  `x -> i*(x-1)/(x+1)`,
  `y -> 8*y/((1-i)^3*(x+1)^3)`.

The source still does not explicitly identify B.7 with `S`, nor B.8 with `T` or
`T^-1`.

## Exact differential calculation

Use the standard basis

`omega1=dx/y`, `omega2=x*dx/y`

of `H^0(C0,Omega^1)`.

For a map

`x'=(a*x+b)/(c*x+d)`, `y'=k*y/(c*x+d)^3`,

the pullback is

`phi^*(omega1)=(ad-bc)/k * (d*omega1+c*omega2)`

and

`phi^*(omega2)=(ad-bc)/k * (b*omega1+a*omega2)`.

Therefore B.7 has matrix

```
M2 = 1/sqrt(2) * [ -1   i ]
                    [ -i   1 ]
```

and B.8 has matrix

```
M6 = 1/2 * [ 1-i   -1-i ]
             [ 1-i    1+i ].
```

These satisfy exactly

`M2^2=I`, `M6^3=-I`, `(M2*M6)^4=-I`.

With `r=i*sqrt(2)`,

`tr(M2)=0`,
`tr(M6)=1`,
`tr(M2*M6)=+r`.

## Comparison with the named retained lattice pair

Cecotti's named matrices are

```
S=b4 = [ 1  1+r ]
       [ 0   -1  ]

T=-b3 = [  1  1 ]
        [ -1  0 ].
```

They satisfy the same presentation, but

`tr(S*T)=-r`

whereas

`tr(S*T^-1)=+r`.

Trace on the tangent/cotangent representation is invariant under conjugacy.
Consequently the specific B.7/B.8 ordered pair cannot be simultaneously identified
with the literal named pair `(S,T)` on one marked ppav.

Thus the post1648B hypothesis that conditionally produced residue `235` is now ruled
out for the *specific* B.7/B.8 pair. This does not invalidate post1648B's finite
conditional implication; it closes that hypothesis as an actual Cecotti B.7/B.8
source-binding candidate.

## Exact ordered-pair enumeration in G12

Generate the retained order-48 group from `S,T` over `Q(r)`, `r^2=-2`, and enumerate
ordered generating pairs `(s,t)` satisfying

`s^2=I`, `t^3=-I`, `(s*t)^4=-I`.

There are exactly 48 such pairs. They split into two simultaneous inner-conjugacy
orbits of size 24:

- `tr(s*t)=-r`: the orbit of `(S,T)`;
- `tr(s*t)=+r`: the orbit of `(S,T^-1)`.

The explicit B.7/B.8 pair belongs to the `+r` orientation class.

## W-line consequence

On the Richelot source plane the exact pair actions are retained from post1648B:

- `phi2`: `Z1` fixed, `Z2 <-> Z3`;
- `phi6`: `Z1 -> Z3 -> Z2 -> Z1`.

For the *literal* `+r` representative

`phi2 -> S`, `phi6 -> T^-1`

there is one equivariant W-line marking:

`Z1 -> L1`,
`Z2 -> L3`,
`Z3=delta_0inf -> L2`.

Hence that additional literal marking would conditionally select residue `97`,
not `235`.

But the source has not fixed the inner conjugating element. Across all 24 inner
conjugates of `(S,T^-1)`:

- all six bijections `{Z1,Z2,Z3}->{L1,L2,L3}` occur;
- each occurs four times;
- `delta_0inf=Z3` lands in each of `L1,L2,L3` exactly eight times.

Therefore the trace orientation alone gives no current residue contraction.

## Decision

New exact credit:

`CECOTTI_B7_B8_TRACE_SELECTS_PLUS_R_ORDERED_GENERATOR_ORBIT_AND_EXCLUDES_NAMED_S_T_ORIENTATION`.

Still fail-closed:

- `absolute_delta0inf_retained_W_line_identified=false`;
- survivors remain `[73,97,235]`;
- conditional literal `97` is not current credit;
- old conditional `235` is no longer a viable binding for the specific B.7/B.8 pair;
- `Q602_excluded=false`;
- `O210_excluded=false`;
- `O212_plus_advance_allowed=false`;
- no controller, receiver, route, theorem, endpoint, or perfect-cuboid credit.

Next exact route:

`SOURCE_BIND_THE_INNER_CONJUGATING_ELEMENT_FOR_CECOTTI_B7_B8_TO_THE_RETAINED_G12_MARKING_OR_EXPLICITLY_IDENTIFY_B7_WITH_S_AND_B8_WITH_T_INVERSE_ON_THE_MARKED_PPAV`.
