# Stage14-4co

Stage14-4co consumes merged `14-4cn`, `14-s7-28`, and `14-X5` and attacks only the physical singular branch `lambda=4`.

The singular relation

```text
D*(Q-P)=A*(Q+P)
```

is combined with the two original reciprocal modulus equations, not merely with the scale-free `(2,2)` curve.

After fixing the divisor-many signed quotient decoration, write

```text
a=c_x^+, b=c_x^-, c=c_k^+, d=c_k^-,
u=L_x^+, v=L_x^-, n=L_k^+, m=L_k^-.
```

The singular Mobius relation gives

```text
n/m = d*(a*u+b*v) / (c*(a*u-b*v)).
```

If

```text
G_k=gcd(d*(a*u+b*v), c*(a*u-b*v)),
```

then primitive reduction and the first reciprocal equation force

```text
G_k^2 = 4*r*s*epsilon_k*c*d.
```

Dually,

```text
G_x^2 = 4*X*Y*epsilon_x*a*b.
```

Therefore the odd residual squareclasses are locked exactly:

```text
sf(oddpart(v_res)) = sf(oddpart(r*s)),
sf(oddpart(u_res)) = sf(oddpart(X*Y)).
```

This is a strong necessary condition, but it does not make the singular rational branch divisor-many. A synthetic infinite primitive family is frozen in the audit to prevent that overclaim.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4cp
```
