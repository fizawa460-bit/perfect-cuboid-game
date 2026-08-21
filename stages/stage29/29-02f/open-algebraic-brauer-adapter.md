# Stage29-02f — open algebraic Brauer grading adapter

This note is the bounded audit repair for the algebraic Brauer calculation on the nonproper physical open.

Let

```text
U = S \ D
```

with `S/Q` smooth proper and `D` the audited 72-component geometric boundary.  Over `Qbar`, use the two-term extended-Picard model

```text
C_D = [ Div_D(S_Qbar) -> Pic(S_Qbar) ]
```

with the degree convention

```text
Div_D in degree -1,
Pic(S_Qbar) in degree 0.
```

The divisor/unit/Picard exact sequence

```text
0 -> Qbar^* -> O(U_Qbar)^* -> Div_D(S_Qbar)
  -> Pic(S_Qbar) -> Pic(U_Qbar) -> 0
```

identifies this complex, up to the standard constants removal, with the extended Picard complex controlling

```text
Br_a(U)=Br_1(U)/im Br(Q).
```

For the cuboid surface, both `Div_D` and `Pic(S_Qbar)` and the differential between them have Galois action factoring through

```text
G = Gal(Q(i,sqrt(2))/Q) ~= V4.
```

With the above grading, the relevant `H^1` hypercohomology contains only positive finite-group cohomology of the lattice cohomology modules; there is no spurious free `H^0(coker)` contribution.  Positive-degree cohomology of the finite group `G` is annihilated by `|G|=4`.  Hence

```text
Br_a(U)[odd] = 0.
```

Equivalently, every new algebraic Brauer class on the physical open beyond constants is 2-primary.

This does not compute the 2-primary group itself.  The exact integral boundary image, saturation, unit kernel, quotient, and `V4` cohomology remain the finite receivers

```text
R29-BR0A
R29-BR0B.
```

It also does not address geometric/open-boundary transcendental classes with nonzero residues; those remain in `R29-BR0G`.
