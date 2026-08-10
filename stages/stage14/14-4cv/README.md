# Stage14-4cv

Latest-main revision after merged s7-34.

Stage14-4cv reads the same joint core `J` in two exact directions:

```text
Cayley rows:   J_C- | M-N,  J_C+ | M+N
linear columns: J_L- | L_-, J_L+ | L_+
```

The four intersections form a pairwise-coprime 2x2 partition of **one** already-charged modulus.  Column cofactors reconstruct `(z1,z2)` and `M`; row CRT fixes `N=abcd mod J`, after which the signed quotient quadruple is divisor-bounded.

This gives

```text
E_RC<=2phi+1/2-2j
    <=2phi+1/2-2chi+6rho.
```

Combining with the selected xi-host count

```text
E_xi<=3phi-1/8-rho
```

and merged s7-32 yields

```text
V(B) << B^(7/12+o(1)).
```

Unique equality profile:

```text
theta=7/24,
phi=1/4,
chi=1/3,
rho=1/24,
j=5/24.
```

Merged s7-34 is compatible.  Its `H^4|q_xi` condition allows `H=B^o(1)` at this profile, leaving an extra residual gcd of scale `B^(1/24)`; hence it does not automatically improve the 7/12 theorem.

Current receiver:

```text
SevenTwelfthsExtraResidualGcdRowColumnTwinShortCofactorIncidence
```

H decision remains false.  Next: `Stage14-4cw`.