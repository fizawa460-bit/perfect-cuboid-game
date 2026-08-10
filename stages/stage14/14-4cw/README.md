# Stage14-4cw

Stage14-4cw starts from merged X11's `19/34` theorem and strengthens the nonproportional row/column reconstruction.

The joint core `J` is still required for the endpoint-linear column, but after that column reconstructs `M`, the Cayley row CRT can use the full already-fixed Cayley-good core `C_Cayley`:

```text
J | C_Cayley | C,
C/C_Cayley | H^2,
C/C_res | g_star^2.
```

Thus the two short losses are

```text
column: max(0,1/4-j),
row:    max(0,1/4-c_y),
```

with

```text
j>=chi-4a-2b,
c_y>=chi-2a-2b.
```

Combining this reconstruction with the fourth-power-root complete count gives

```text
V(B)<<B^(11/20+o(1)).
```

The unique saturation profile is

```text
theta=11/40,
phi=1/4,
chi=3/10,
a=1/40,
b=0,
j=1/5,
c_y=1/4.
```

The full-row `N` lift is then `B^o(1)`; only one `B^(1/20)` linear-column cofactor support remains.

Receiver:

```text
ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence
```

No auxiliary H/tH theorem is needed. Next: `Stage14-4cx`.