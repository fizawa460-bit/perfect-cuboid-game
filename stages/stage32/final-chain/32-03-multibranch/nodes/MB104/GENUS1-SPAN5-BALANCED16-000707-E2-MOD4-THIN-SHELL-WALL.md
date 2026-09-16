# Stage32 MB104 — `000707000f0f` e=2 mod-4 thin-shell wall

Status: **RETAINED EXACT NEGATIVE ROUTE / NEW ZERO-QUARTIC MOD-4 BITS DO NOT REMOVE ADAPTIVE-JET THIN SHELL / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

This note combines two retained inputs in the even case `l=2m`, `m>=1`:

1. the adaptive-cancellation jet budget, with

```text
Q=sum_j b_j^2,
delta_same=336m^2+112m-2Q,
raw jet rank can matter only when 0<=delta_same<=224m-12;
```

2. the zero-quartic torsion congruences, which add one mod-2 condition in the centered `b` variables on each seven-node block.

The purpose is to test whether the new mod-4 information automatically pushes every formal allocation out of the high-energy thin shell. It does not.

## 1. Oriented seven-node variables

For `Q0`, absorb the retained orientation signs into

```text
c=(b0,-b1,b2,-b3,-b24,b25,-b26).
```

Then the centered saturation equation is simply

```text
sum c_i=0.
```

The new zero-quartic torsion condition is, modulo two,

```text
c5+c6+c7=0 mod 2,
```

because signs disappear mod two. For `Q1` no orientation change is needed; it has the same abstract constraints.

Thus both seven-node blocks have the same exact integer model:

```text
-4m <= c_i <= 4m,
sum_i c_i=0,
c5+c6+c7 even.
```

## 2. Uniform formal witness inside the thin shell

For every integer `m>=1`, take on each oriented seven-node block

```text
(c1,...,c7)=m*(-4,-4,3,3,-4,3,3).             (W)
```

Then

```text
sum c_i=0,
c5+c6+c7=2m,
```

so both the centered saturation equation and the new torsion parity hold. All entries satisfy the bound `|c_i|<=4m`.

The square energy of one block is

```text
(3*16+4*9)m^2=84m^2.
```

Using the same witness on both zero-quartic blocks gives

```text
Q=168m^2.                                       (QW)
```

For `Q0`, undoing the orientation yields

```text
(b0,b1,b2,b3,b24,b25,b26)
 =m*(-4,4,3,-3,4,3,-3),
```

and hence, since `x_j=2(b_j+4m)`,

```text
(x0,x1,x2,x3,x24,x25,x26)
 =(0,16m,14m,2m,16m,14m,2m).
```

For `Q1` the witness gives

```text
(x8,x9,x10,x11,x32,x33,x34)
 =(0,0,14m,14m,0,14m,14m).
```

These satisfy the retained integer saturation equations and the two new mod-4 congruences. They are formal allocation data only; no geometric carrier is asserted.

## 3. Exact position in the adaptive-jet shell

Substituting `(QW)` into the retained same-sheet formula gives

```text
delta_same
 =336m^2+112m-2*(168m^2)
 =112m.                                          (DW)
```

For every `m>=1`,

```text
0 <= 112m <= 224m-12.
```

Therefore the witness lies inside the exact high-energy thin shell for every even `l>=2`.

The adaptive source-minus-target lower bound on this witness is

```text
336m^2-112m+12-2Q
 =12-112m < 0.
```

Thus raw injective jet obstruction remains dimensionally possible on this formal family. The new mod-4 conditions do not make it disappear by dimension alone.

## Route consequence

The implication

```text
zero-quartic mod-4 congruences
  => all formal allocations leave the adaptive-jet thin shell
```

is false.

The two new torsion bits remain genuine necessary conditions, but they do not by themselves improve the shell bound `delta_same<=224m-12` or produce an `e=2` contradiction. Any successful continuation must use more than these congruences and the raw dimension budget: an exact simultaneous jet-evaluation rank, a conductor-preimage residual-sheet evaluation, or another global relation on the `b_j` is still required.

## Independent arithmetic check

Wolfram arithmetic independently confirmed

```text
2*(3*(4m)^2+4*(3m)^2)=168m^2,
336m^2+112m-2*(168m^2)=112m,
112m<=224m-12 for m>=1.
```

This external arithmetic check is convenience only; the retained proof is the exact integer calculation above.

## Firewalls

- The witness is formal and does not construct a curve.
- No individual conductor pair is assigned a residual sign.
- No global jet-evaluation rank is claimed.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, `000707000f0f`, MB104, span5, receiver, effectivity, theorem and endpoint credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
