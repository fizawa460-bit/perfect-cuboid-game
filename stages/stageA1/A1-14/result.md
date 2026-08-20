# StageA1 A1-14 — second 7-adic depth on the delta=1 multiplier sieve

## Scope

Continue only the audited StageA1 delta=1 receiver

`Q(z)=v^2, z+2=s^2, z-2=t^2`

on

`E: y^2=x^3+x^2+95x+703`, `E(Q)=Z P`, `P=(3,32)`.

A1-13 proved the necessary local condition

`n mod 63 in {0,1,2,-1}`

and reduced the A1-12 global multiplier set to 256 classes modulo 3416490. A1-14 deepens the same p=7 condition by one further formal-group level; it does not add unrelated primes.

## 1. Formal-group depth

Use the standard local parameter `tau=-x/y` at O. Exact rational group law gives

- `v7(tau(63P))=2`;
- `(tau(63P)/49) mod 7 = 2`;
- `v7(tau(441P))=3`.

Thus `63P` lies in `E_2 \ E_3`, while `441P` lies in `E_3`. For `k=1,...,6`, the formal-group law gives

`tau(k*63P)/49 = k*(tau(63P)/49) mod 7`.

So each A1-13 residue center has seven lifts modulo 441, indexed by `k mod 7`.

## 2. Square criterion at the four centers

For odd p, a nonzero rational number is a square in Q_7 iff its 7-adic valuation is even and its unit residue mod 7 is a quadratic residue. The nonzero square residues mod 7 are `{1,2,4}`.

Let `T=63P`. Exact representatives at the four A1-13 centers give the following units for the `k=1` lift:

- near `O`: at `T`, both `z+2` and `z-2` have valuation `-2` and unit `4`;
- near `P`: at `P+T=64P`, both have valuation `-2` and unit `3`;
- near `2P`: at `2P+T=65P`, `z+2` is a unit with residue `4`, while `z-2` has valuation `2` and unit `5`;
- near `-P`: at `-P+T=62P`, `z+2` is a unit with residue `4`, while `z-2` has valuation `2` and unit `2`.

Because `z` has simple poles at `O,P`, the pole units scale by `k^{-1}`. Because `z-2` has simple zeros at `2P,-P`, its zero unit scales by `k`. The `k=0` lift is retained conservatively because it lies one formal-group level deeper.

Therefore the surviving `k mod 7` are exactly:

- center `0`: `{0,1,2,4}`;
- center `1`: `{0,3,5,6}`;
- center `2`: `{0,3,5,6}`;
- center `-1`: `{0,1,2,4}`.

Equivalently the exact necessary classes modulo 441 are

`{0,63,126,252, 1,190,316,379, 2,191,317,380, 440,62,125,251}`.

This set is invariant under `n -> 1-n`.

## 3. Global refinement

The A1-13 modulus is

`M=3416490`,

which contains the factor 63 but not 441. Passing to

`M14=lcm(M,441)=23915430=7M`

lifts the 256 A1-13 classes to `256*7=1792` classes before the new depth-two test. Exactly 1024 survive the modulo-441 condition above.

Thus the surviving density is multiplied by `4/7` relative to A1-13. The exact sorted set modulo 23915430 has SHA-256

`ca2472c7077bac47b0cced38211ea26aa20223dd65e7f2c548d78cca93117251`.

This is strict structural narrowing. It is not a finite-height search and not an unrelated-prime scan.

## 4. Remaining wall

A1-14 does not prove global emptiness. The surviving 1024 classes may still contain global points. A next batch may pursue a third 7-adic depth, another structurally related prime-power condition, an elliptic-divisibility/denominator recurrence, or a certified full MW-sieve / elliptic-Chabauty computation. Merely restating the same modulo-441 receiver does not count as progress.

## Firewalls

All statements remain specific to the corrected equation-(6) StageA1 family. No arbitrary-perfect-cuboid necessary condition is claimed; no perfect cuboid is found or excluded; Stage27 and StructureRadar are unchanged.

```text
A1_14_STATUS=SUBMITTED_FOR_AUDIT
A1_14_V7_T_63P=2
A1_14_T_63P_OVER_49_MOD7=2
A1_14_V7_T_441P=3
A1_14_ALLOWED_MOD441_COUNT=16
A1_14_GLOBAL_MODULUS=23915430
A1_14_PRETEST_LIFTS=1792
A1_14_SURVIVING_CLASSES=1024
A1_14_SURVIVING_CLASS_SHA256=ca2472c7077bac47b0cced38211ea26aa20223dd65e7f2c548d78cca93117251
A1_14_COMPLETE_DELTA1_CLOSURE=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```