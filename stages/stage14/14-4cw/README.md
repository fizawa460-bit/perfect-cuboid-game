# Stage14-4cw

This stage consumes merged `X11` / `s7-37` and the merged `4cv` row/column reconstruction.

Entering theorem:

```text
V(B) << B^(19/34+o(1)).
```

New observation: the endpoint-linear column step needs the joint residual/Cayley core `J`, but once that step reconstructs `M`, the Cayley row CRT can be run on the larger full Cayley-good core `C_Cayley`.

```text
J | C_Cayley | C,
C/C_Cayley | B^o(1)*(H_star H_other)^2,
j >= chi-4a-2b,
c_y >= chi-2a-2b.
```

The sequential complete count is

```text
E_FR
 <= 2phi
    +(4a+2b-d)
    +max(0,2a+2b-d),
d=chi-1/4.
```

Together with

```text
E_H<=3phi-1/8-3a-3b
```

and the merged `E_s,E_k` complete counts, exact minimax gives

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20.
```

Unique equality profile:

```text
theta=11/40,
phi=1/4,
chi=3/10,
a=1/40,
b=0,
j=1/5,
c_y=1/4.
```

The full Cayley row has no fixed-power `N` lift there; only one `B^(1/20)` linear-column cofactor support remains.

Receiver:

```text
ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence
```

No external H/tH theorem is required. Next: `Stage14-4cx`.
