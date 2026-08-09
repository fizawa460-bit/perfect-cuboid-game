# Stage14-s5c supported-prime derivation note

Let

```text
z1=d1*u1^2, z2=d2*u2^2, z3=d3*u3^2.
```

Then

```text
z1-z2=S^2,
z3-z1=X^2,
z3-z2=H^2.
```

At an odd bad prime of a primitive Euclid pair exactly one right-hand side is p-divisible.  If p is selected in the descent support, exactly two of the `di` have odd p-valuation.  Those two indices must be the endpoints of the p-divisible difference: any other placement leaves a unit-valued difference between terms of incompatible valuation parity.  This proves

```text
p|S -> 12,
p|X -> 13,
p|H -> 23.
```

Writing `di=p^ei ai` with unit `ai`, divide out the common supported p and reduce the p-divisible difference.  Its two unit-leading terms must have equal square class, giving respectively

```text
S: (a1 a2|p)=1,
X: (a1 a3|p)=1,
H: (a2 a3|p)=1.
```

The remaining coordinate is obtained from a unit-square right-hand side:

```text
S: z3=z1+X^2 -> (a3|p)=1,
X: z2=z1-S^2 -> (-a2|p)=1,
H: z1=z2+S^2 -> (a1|p)=1.
```

Once the residue square classes match, the supported p-divisible binary difference has a nonsingular unit solution modulo p and can be lifted p-adically by the usual one-variable Hensel adjustment.  This proves the supported-prime rows recorded in `result.md`.

This note does not claim that the same formulas describe a bad prime omitted from all three `di`; those rows have additional residue branches and are explicitly deferred.
