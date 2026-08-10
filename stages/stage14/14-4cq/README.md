# Stage14-4cq

Stage14-4cq refines the new `3/4` mainline barrier after merged 4cp.

The common core `C` divides both plus hosts

```text
D^2+A^2,
Q^2+P^2.
```

After peeling the two coordinate gcd-squares, the good common-core part `C_*` sees the two Cayley ratios as square roots of `-1`. Combining this with the exact reciprocal Edwards equation yields

```text
C_* |
(4*r*s*X*Y*epsilon_x*epsilon_k-a*b*c*d)
(4*r*s*X*Y*epsilon_x*epsilon_k+a*b*c*d).
```

The removed bad part divides `(r*s*X*Y)^2`. Hence, after fixing residual/quotient data and `XY`, the common core has only divisor-many possibilities.

This gives the alternative block bound

```text
E_dual <= 1/2+2*phi-c,
```

to be combined with s7-29

```text
E_s7 <= 2*phi+1/4.
```

On `phi=1/4`, the exact common-core size is

```text
c=2*theta-1/4,
```

so every `theta>1/4` block is power-saved. The only remaining `3/4` saturation corner is

```text
theta=phi=1/4,
c=1/4.
```

The whole-family exponent remains `3/4`. No new H request is opened; the next exact target is the Cayley/Gaussian divisor allocation at the symmetric corner.
