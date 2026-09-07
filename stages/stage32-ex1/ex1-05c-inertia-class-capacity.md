# EX1-05C — inertia-class capacity reduction

Status: provisional same-PR candidate. No hostile-audit, Stage32 MAIN, or full-target credit is granted here.

## Source-side ordering and the three inertia classes

Stoll–Testa verification code `Cuboids/cuboids.magma` constructs the known curves as `Cs := C1s cat C2s cat C3s`, then appends the 48 singular points `pts` as the exceptional-divisor part of the pairing matrix. Hence the last 48 entries of the retained Stage32 `all140_pairings` use exactly the source-side `pts[1]..pts[48]` exceptional sequence.

The same source lists the 12 `C2` genus-one curves in three consecutive four-curve groups:

- indices 33..36: `b1=0`;
- indices 37..40: `b2=0`;
- indices 41..44: `b3=0`.

In the Stoll–Testa product model the diagonal `G0=(Z/2)^3` invariants satisfy

`U=u1*u2=2b1`, `V=v1*v2=2b2`, `W=w1*w2=2b3`.

Thus the three 16-node single-sign inertia classes are exactly u-sign=`b1=0`, v-sign=`b2=0`, w-sign=`b3=0`.

## Class-mass adapter

On the minimal resolution, pairing the pullback of the canonical hyperplane `bj=0` with V6 gives

`sum_{nodes bj=0} V6.E = K.V6 - sum_{four C2 components} V6.C2`.

Hence the three inertia contact masses are

- u-sign: `186-(11+26+31+22)=96`;
- v-sign: `186-(16+26+25+11)=108`;
- w-sign: `186-(28+40+34+22)=62`.

Replay: `96+108+62=266`.

## Exhaustive h=2 stabilizer classification

Write `G0=F2^3` with single-sign elements `u,v,w` and even-sign subgroup

`G0plus={0,uv,uw,vw}`.

For `h=2`, the full component stabilizer `M` has order 4 and `H=M∩G0plus` has order 2. There are exactly seven order-4 subgroups of `F2^3`; one is `G0plus` itself and belongs to the `h=4` case. Therefore exactly six subgroups occur in the `h=2` case.

They are:

- `<u,v>={0,u,v,uv}`: allowed single-sign inertia `{u,v}`, capacity `96+108=204`;
- `<u,w>={0,u,w,uw}`: allowed `{u,w}`, capacity `96+62=158`;
- `<v,w>={0,v,w,vw}`: allowed `{v,w}`, capacity `108+62=170`;
- `<uv,w>={0,uv,w,uvw}`: allowed `{w}`, capacity `62`;
- `<uw,v>={0,uw,v,uvw}`: allowed `{v}`, capacity `108`;
- `<vw,u>={0,vw,u,uvw}`: allowed `{u}`, capacity `96`.

Only single-sign elements occur as node inertia. Ramified local inertia must lie in `M`, so `Q` cannot exceed the total V6 contact mass of the allowed single-sign classes. EX1-05B gives `Q>=188` in the h=2 case. Therefore five of the six subgroups are excluded by capacity alone. The unique capacity-compatible subgroup is

`M=<u,v>={0,u,v,uv}`,

with the w-sign / `b3=0` class forbidden and `188<=Q<=204`.

This repairs the previous unjustified strengthening from “at most two single-sign inertia types” to “exactly two.” The exhaustion now includes the three one-single-plus-triple-sign subgroups explicitly.

## Reduced parity gate

For the unique surviving h=2 subgroup, ramification is forbidden on the w-sign class, so `q_i=0` on each of its 16 nodes. EX1-05B gives `q_i congruent m_i (mod 2)`. Therefore all sixteen V6 exceptional pairings on `b3=0` must be even.

If any one is odd, h=2 is excluded and h=4 is forced at the component-stabilizer layer.

The remaining h=2 numerical range before that parity test is

`Q=188+2t`, `0<=t<=8`.

The forbidden w-class mass 62 contributes 31 units to the half-contact-excess, leaving `(204-Q)/2=8-t` on the allowed u/v classes. Hence at most `8-t` ramified allowed branches can have contact order at least 3, and at least `180+3t` ramified allowed branches are simple transverse contacts of order 1.

Next route remains `EX1-05D_B3_NODE_PARITY_ADAPTER_OR_H4_FORCING`.