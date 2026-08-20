# StageA1 A1-13 — 7-adic prime-power refinement of the delta=1 MW sieve

## Scope

A1-12 reduced the true StageA1 first-two-cover receiver to the rank-one curve

```text
E: y^2=x^3+x^2+95x+703,
P=(3,32),
E(Q)=Z P,
```

with quartic coordinate

```text
z=-(y+32)/(x-3),
```

and proved that every rational survivor must satisfy, at `p=7`,

```text
n mod 9 in {0,1,2,-1}.
```

A1-13 does not append another unrelated good prime. It deepens this same `p=7` condition from reduction mod `7` to first-order 7-adic / mod-`49` information.

All statements remain specific to the corrected equation-(6) StageA1 family.

## 1. Formal-group depth of `9P`

The prime `7` is a good-reduction prime. Let

```text
t=-x/y
```

be the standard local parameter at the identity.

Exact rational group-law calculation gives

```text
9P = (
  244695292924563763 / 53070230469113361,
 -434024672226074853059906272 / 12225776733946406608383609
).
```

Hence

```text
t(9P)
 = 56370398106419088508080747
   / 434024672226074853059906272,

v_7(t(9P))=1,
(t(9P)/7) mod 7 = 2 != 0.
```

Thus `9P` lies in the first formal-group filtration step `E_1(Q_7)` but not `E_2(Q_7)`. Since `E_1/E_2 ~= F_7`, the seven points

```text
rP + k(9P),  k mod 7,
```

run through the seven first-order 7-adic lifts of `rP` for each fixed `r`.

Equivalently, the order of the reduction of `P` grows from

```text
ord_7(P)=9
```

to

```text
ord_49(P)=63.
```

As an exact check, direct rational multiplication gives

```text
v_7(t(63P))=2.
```

## 2. Local behavior of the two square functions

The StageA1 conditions are

```text
z+2 is a rational square,
z-2 is a rational square.
```

There are four A1-12 residue centers `r in {0,1,2,-1}`.

### Centers `r=0,1`

The function `z` has a simple pole at both `O` and `P`:

- `n=0` corresponds to `O`, one quartic point at infinity;
- `n=1` corresponds to `P`, the other quartic point at infinity.

Therefore `z+2` and `z-2` also have simple poles at these two centers. A first-order displacement from either center has

```text
v_7(z+2)=v_7(z-2)=-1,
```

which is impossible for a square in `Q_7`.

The only lift not rejected at first order is the depth-2 class itself:

```text
n == 0 mod 63  or  n == 1 mod 63.
```

These two classes are retained conservatively; A1-13 does not assume a denominator parity beyond the proved first-order statement.

### Centers `r=2,-1`

The exact A1-12 map gives

```text
2P  -> z=2,
-P  -> z=2.
```

Moreover

```text
z-2 = -(y+2x+26)/(x-3),
```

and the line identity

```text
(-2x-26)^2-(x^3+x^2+95x+703)
 = -(x-3)^2(x+3)
```

shows that `z-2` has a simple zero at both `2P` and `-P` after cancellation at `-P`.

Hence every non-depth-2 first-order lift has

```text
v_7(z-2)=1,
```

again impossible for a square in `Q_7`. The only retained lifts are

```text
n == 2 mod 63  or  n == -1 mod 63.
```

## 3. Exact representative valuation table

The formal-group argument is independently mirrored by exact rational multiples. Writing `n=r+9k`, `k=0,...,6`:

```text
r=0:
  n=0 retained;
  n=9,18,27,36,45,54 have v7(z+2)=v7(z-2)=-1.

r=1:
  n=1 retained;
  n=10,19,28,37,46,55 have v7(z+2)=v7(z-2)=-1.

r=2:
  n=2 has z-2=0;
  n=11,20,29,38,47,56 have v7(z-2)=1.

r=-1:
  n=-1 has z-2=0;
  n=8,17,26,35,44,53 have v7(z-2)=1.
```

Thus the A1-12 `p=7` restriction sharpens exactly to the necessary condition

```text
n mod 63 in {0,1,2,-1}.                         (A1.13.1)
```

This is a genuine prime-power refinement: it distinguishes the seven lifts of each old class modulo `9`.

## 4. Interaction with the six-prime A1-12 sieve

A1-12 produced

```text
M=3416490,
|S_A1_12|=384,
```

and `63 | M`. Therefore the 7-adic refinement does not enlarge the combined modulus; it cuts the existing residue set inside the same modulus.

Filtering the exact A1-12 set by (A1.13.1) gives

```text
|S_A1_13|=256,
S_A1_13 subset S_A1_12,
```

with deterministic sorted-set SHA-256

```text
f08de28f142bf79dd88bbee5725e87c4dd0692091d0e85a645275dc1bfca6fc0.
```

Hence every nondegenerate StageA1 survivor must satisfy

```text
n mod 3416490 in S_A1_13,
|S_A1_13|=256.                                  (A1.13.2)
```

The surviving density is

```text
256/3416490 ~= 7.49307e-5,
```

about one multiplier class in `13346`.

The set remains invariant under the quartic involution `n -> 1-n`.

## 5. What A1-13 does and does not close

A1-13 is structural progress beyond A1-12:

1. it uses the formal group at the already-active prime `7` rather than appending unrelated primes;
2. it proves `9P in E_1 \ E_2` and raises the relevant multiplier modulus from `9` to `63` locally;
3. it proves the exact first-order valuation obstruction at all four A1-12 residue centers;
4. it cuts the global A1-12 residue set from `384` to `256` classes without increasing the global modulus.

It does not prove that the 256 classes contain no global survivor. The four depth-2 classes modulo `63` are intentionally retained. A next substantive batch may deepen one or more retained classes to `7^3`, derive an elliptic-divisibility/denominator recurrence, or attach a certified full MW-sieve/elliptic-Chabauty computation.

Merely restating (A1.13.1), increasing an `x`-height bound, or appending many unrelated good primes is not a valid next step.

## 6. Firewalls

This result is equation-(6)-family-specific. It does not make equation (6) universal, does not produce a necessary condition for arbitrary perfect cuboids, and does not prove perfect-cuboid existence or nonexistence. Stage27 and StructureRadar are unchanged.

```text
A1_13_STATUS=SUBMITTED_FOR_AUDIT
A1_13_P=7
A1_13_ORD_P_MOD7=9
A1_13_ORD_P_MOD49=63
A1_13_ALLOWED_MOD63=0,1,2,-1
A1_13_COMBINED_MODULUS=3416490
A1_13_SURVIVING_MULTIPLIER_CLASSES=256
A1_13_SURVIVING_CLASS_SHA256=f08de28f142bf79dd88bbee5725e87c4dd0692091d0e85a645275dc1bfca6fc0
A1_13_COMPLETE_DELTA1_CLOSURE=false
A1_13_NEW_ARBITRARY_CUBE_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
