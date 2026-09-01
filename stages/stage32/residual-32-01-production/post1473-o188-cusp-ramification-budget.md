# Stage32 post-1473 — O=188 cusp-to-projection ramification budget

## Scope

This note continues only the fixed V6 target `g1-d186`, after hostile audit review `5078184271` promoted the universal fixed-target necessary conditions

`O >= 188`, `S1 >= 149`.

It attacks the exact `O=188` product-cover profiles retained in

`stages/stage32/residual-32-01-production/post1473-o188-product-cover-extremal-profile.json`.

No global carrier existence is assumed.

## Source lock and local coordinates

Primary source: Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv `1303.6495`, DOI `10.1307/mmj/1480734014`.

In the proof of Theorem 3.1 they use cusp coordinates on the two `X(8)` factors

`p = exp(2*pi*i*z/8)`, `q = exp(2*pi*i*w/8)`,

and a local normalized curve approaching a node with positive translation exponents `a1,a2` satisfying

`a1 == a2 == 0 mod 4`, `a1+a2 == 0 mod 8`.

The retained audited Stage32 A1-node adapter identifies the exceptional contact multiplicity with

`m = min(a1,a2)/4`.

Put `A_i=a_i/4`. Then `A1,A2` are positive integers with the same parity, hence their parity equals the parity of `m=min(A1,A2)`.

Section 4, Lemma 4.1 source-locks the free `V4=GammaPrime4/Gamma8` action on `X(8)`, so the product-cover component `D -> Y` is etale of degree `q'`.

## Local projection degree after the Beauville pullback

Let `t` be a local parameter on the normalized carrier `N` at a branch above a node.

From the cusp parametrization,

`p_i ~ t^(a_i/8) * unit = t^(A_i/2) * unit`

before passing to the Beauville double-cover normalization.

### Odd contact

If `m` is odd, then both `A_i` are odd. The normalized Beauville pullback `Y -> N` ramifies at this branch, so write `t=s^2`. Then

`p_i ~ s^(A_i) * unit`.

Thus the local degree of the `i`-th `X(8)` projection on `Y` is `A_i`. Because `D -> Y` is etale degree `q'`, there are `q'` local points above this branch and their forced total contribution to the projection ramification is

`q'*(A_i-1) >= q'*(m-1)`.

### Even contact

If `m` is even, both `A_i` are even. The Beauville pullback is unramified over this point and has two local points. At each point the local degree is `A_i/2`, so after the etale degree-`q'` pullback the forced total ramification contribution is

`2*q'*(A_i/2-1) = q'*(A_i-2) >= q'*(m-2)`.

Define the contact defect

`delta(m) = m-1` for odd `m`,
`delta(m) = m-2` for even `m`.

For each projection therefore

`R_i >= q' * sum_P delta(m_P)`.

This is only a lower bound: additional ramification away from the exceptional branches may exist.

## Apply the exact O=188 projection profiles

The audited/exact O=188 arithmetic leaves:

- `q'=2`: projection degrees `{46,47}` and ramification totals `{8,0}`;
- `q'=4`: either `{92,94}` with `{16,0}`, or `{93,93}` with `{8,8}`.

### q'=2

One projection is etale, hence its `R_i=0`. The local lower bound forces `delta(m_P)=0` at every normalized branch. Therefore every odd contact has `m=1` and every even contact has `m=2`.

Since `O=188` and total exceptional mass is `266`,

`266 = 188*1 + 39*2`.

So this profile forces exactly

- 188 odd multiplicity-one branches;
- 39 even multiplicity-two branches;
- `B=227`.

### q'=4, asymmetric {92,94}

Again one projection is etale. The same argument forces the identical contact histogram

`188 x m=1` and `39 x m=2`, with `B=227`.

### q'=4, symmetric {93,93}

Here each projection has total ramification `8`, so

`sum delta(m_P) <= 8/4 = 2`.

Because every `delta(m)` is a nonnegative even integer, only defect `0` or `2` is possible.

Using

`266 = 188 + 2*E + Delta`,

where `E` is the number of even-contact branches and `Delta=sum delta(m_P)`, the only contact histograms are:

1. `188 x m=1`, `39 x m=2`, `B=227`, `Delta=0`;
2. `187 x m=1`, `1 x m=3`, `38 x m=2`, `B=226`, `Delta=2`;
3. `188 x m=1`, `37 x m=2`, `1 x m=4`, `B=226`, `Delta=2`.

## Consequence for the former zero-slack profile

The V184 zero-slack state `S1=149` had

`149 x m=1 + 39 x m=3`.

Its contact defect is already

`39*(3-1)=78`.

That is incompatible with every O=188 projection profile: profiles with an etale projection require defect zero, while the symmetric q'=4 profile permits defect at most two.

Therefore, if the local cusp-to-projection adapter above survives hostile audit, the entire `S1=149` zero-slack O=188 profile is excluded.

## Fixed-node nonexclusion check

This new reduction does not yet exclude all O=188 carriers. The three surviving contact-histogram types are all compatible with the locked 48 exceptional totals at the integer-partition level.

Exact nodewise assignment counts are:

- `188 x m=1 + 39 x m=2`: `6851266935728760020`;
- `187 x m=1 + 1 x m=3 + 38 x m=2`: `116737713339105712855`;
- `188 x m=1 + 37 x m=2 + 1 x m=4`: `67027354848511690399`.

These counts are only a coarse nonexclusion replay. They do not certify analytic branch positions or a global curve.

## Verdict / firewall

Provisional pending hostile audit:

- the cusp exponents give a direct lower bound on each `X(8)` projection ramification budget;
- `S1=149` / `149x1+39x3` is excluded at O=188;
- q'=2 and q'=4 asymmetric force `188x1+39x2`;
- q'=4 symmetric permits only three contact histograms in total.

Still OPEN:

- analytic realization of those histograms;
- branch locations / tangent compatibility;
- all O=188 multibranch carriers;
- all fixed-V6 integral genus-one carriers;
- general genus<=1 classification.

DO NOT USE THIS FOR FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit before separate hostile audit and downstream promotion.
