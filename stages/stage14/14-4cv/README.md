# Stage14-4cv

Stage14-4cv consumes merged 4cu and merged s7-33 and refines the `19/32` receiver by reading the same joint core `J` in two directions.

- Cayley rows: `J_C- | M-N`, `J_C+ | M+N`.
- endpoint-linear columns: `J_L- | L_-`, `J_L+ | L_+`.
- the resulting four cells are a partition of one already-charged modulus, not four new spacing moduli.

Column cofactors reconstruct `(z1,z2)` and therefore `M`; row CRT then fixes `N=abcd` modulo `J`, after which the signed quotient quadruple is divisor-bounded.

The alternative complete count is

```text
E_RC <= 2phi+1/2-2j
     <= 2phi+1/2-2chi+6rho,
```

while the selected xi-host count is

```text
E_xi <= 3phi-1/8-rho.
```

Combining these with merged s7-32 gives

```text
V(B) << B^(7/12+o(1)).
```

The unique equality profile of the proved envelope is

```text
theta=7/24,
phi=1/4,
chi=1/3,
rho=1/24,
j=5/24,
linear cofactor exponent=1/24,
CRT lift exponent=1/24.
```

Merged s7-33's strong-`S/T` split counterexample is retained as a guard: Stage14-4cv does not use a canonical Gaussian associate split and does not double-charge the common-core orientation.

H decision:

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

Next: `Stage14-4cw`, compare the two surviving `1/24` cofactors directly.