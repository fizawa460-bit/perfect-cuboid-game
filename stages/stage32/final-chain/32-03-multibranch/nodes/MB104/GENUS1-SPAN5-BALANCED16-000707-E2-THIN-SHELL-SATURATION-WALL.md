# Stage32 MB104 — `000707000f0f` e=2 thin-shell saturation wall

Status: **RETAINED EXACT FORMAL-ALLOCATION COUNTEREXAMPLE / SATURATION PLUS RETAINED MOD-4 TORSION CAN REACH `delta_same=0` / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

For `l=2m`, the retained node-orbit/allocation variables satisfy

```text
d_j=2*x_j-8*l,
x_j=2*y_j,
b_j=y_j-4*m,
```

hence exactly `d_j=4*b_j`. The two centered saturation equations become

```text
b0-b1+b2-b3-b24+b25-b26 = 0,                  (Q0-b)
b8+b9+b10+b11+b32+b33+b34 = 0,                (Q1-b)
```

with `-4m<=b_j<=4m`.

The retained energy identity and jet-budget shell are

```text
Q=sum_j b_j^2,
delta_same=336*m^2+112*m-2*Q,
Q>=168*m^2-56*m+6.
```

The retained zero-quartic torsion refinement also imposes

```text
x24+x25+x26 = 0 mod 4,
x32+x33+x34 = 0 mod 4.                         (MOD4)
```

## Exact endpoint witness at m=4

Take `m=4`, so `l=8`, `8*l=64`, and set

```text
(b0,b1,b2,b3,b24,b25,b26)
 =(-16,16,-16,-8,-12,12,-16),

(b8,b9,b10,b11,b32,b33,b34)
 =(-16,-16,-16,0,16,16,16).
```

Then `(Q0-b)` and `(Q1-b)` both vanish. The corresponding branch allocations

```text
x_j=2*(b_j+16)
```

are

```text
Q0: (0,64,0,16,8,56,0),
Q1: (0,0,0,32,64,64,64).
```

Thus every `x_j` lies in `[0,64]`, and direct substitution gives

```text
x0-x1+x2-x3-x24+x25-x26 = -32 = -4*l,
x8+x9+x10+x11+x32+x33+x34 = 224 = 28*l.
```

The retained mod-4 bits also hold:

```text
x24+x25+x26 = 8+56+0 = 64 = 0 mod 4,
x32+x33+x34 = 64+64+64 = 192 = 0 mod 4.
```

The square energy is

```text
Q=2912=168*m^2+56*m,
```

hence exactly

```text
delta_same=336*m^2+112*m-2*Q=0.
```

So the retained saturation equations, branch bounds, and zero-quartic mod-4 torsion bits jointly admit a formal allocation at the endpoint of the Hodge-allowed energy range.

For the same witness the retained source-minus-target lower bound is

```text
336*m^2-112*m+12-2*Q
 = delta_same-224*m+12
 = -884.
```

Dimension counting therefore does not force a kernel there.

The arithmetic equalities were independently replayed by an exact Wolfram Language evaluation. This sharpens the earlier uniform mod-4 thin-shell witness (`delta_same=112m`) at the specific degree `m=4`: even after the retained torsion bits, `delta_same=0` is formally allowed.

## Route consequence

The package

```text
node-orbit saturation
+ branch bounds
+ retained quadratic energy
+ retained zero-quartic mod-4 torsion
```

cannot by itself yield any universal positive lower bound on `delta_same`, and therefore cannot close the high-energy shell.

The witness is only formal allocation data. It is **not** asserted to come from an actual curve, eigensection pair, conductor normalization, or geometric carrier.

Accordingly the next useful computation remains genuinely global: the modified invariant/anti-invariant eigensection evaluation/base-locus geometry under the adaptive normal-jet conditions, or another geometric relation not implied by the retained saturation/torsion package.

## Firewalls

- No geometric realizability of the witness is claimed.
- No individual conductor branch receives a residual sheet label.
- No global jet-evaluation rank is claimed.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, `000707000f0f`, MB104 and span5 remain open.
- No finite degree window, receiver, effectivity, theorem or endpoint credit.
- No heavy compute is armed.
- No merge or rebase authorization.
