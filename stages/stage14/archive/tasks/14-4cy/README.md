# Stage14-4cy

Stage14-4cy consumes merged `4cx` and merged `s7-39` on latest main.

The entering theorem is

```text
V(B) << B^(23/44+o(1)).
```

Stage14-4cx left a saturation segment

```text
theta=23/88,
19/88<=phi<=21/88,
H=B^(s+o(1)),
s=phi-19/88,
```

with one column residual and one Cayley-row lift.

The new exact observation is that the same cross-root square `H^2` divides both Cayley numerator and quotient product:

```text
H^2 | M,
H^2 | N=abcd.
```

Since merged s7-39/4cx gives

```text
gcd(C_Cayley,H)=1,
```

the full Cayley-row congruence descends to

```text
M_H=M/H^2,
N_H=N/H^2
```

with the same row modulus.  The row lift therefore loses `2s`, exactly as the endpoint-linear column cofactor product does after removing the common factor `H` from both columns.

Thus on `chi<=1/4`

```text
E_col,H <= max(0,1/4-j-2s),
E_row,H <= max(0,1/4-j-2s),
```

and because `j>=chi-2s-o(1)`, both are at most

```text
max(0,1/4-chi).
```

This does **not** improve the whole-family exponent below `23/44`, but it collapses the entire old saturation segment to one unique point:

```text
theta=23/88,
phi=19/88,
chi=9/44,
H=B^o(1),
C=J=C_Cayley at fixed-power scale.
```

At this point the two remaining fixed-power short coordinates are exactly

```text
column residual support = B^(1/22+o(1)),
reduced row lift        = B^(1/22+o(1)).
```

Merged s7-31 also gives the opposite signed quotient pair `(c,d)` with only `B^o(1)` multiplicity at this point because `nu<chi`.

The new receiver is

```text
TwentyThreeFortyFourthsCrossRootFreeEqualCoreTwinOneTwentySecondLiftIncidence
```

No mainline H/tH theorem is required.  Next: `Stage14-4cz`.
