# Stage14-4cm

Stage14-4cm consumes merged `14-4cl` and reuses the exact common-core definitions from merged `14-4cg`.

The key correction is that the formal quadratic cyclotomic branches retained in 4cl are empty on physical agreement support.  Taking odd parts in the two residual-product identities gives

```text
oddpart(H_k^-)=oddpart(R*J)*oddpart(u_res),
oddpart(H_xi^-)=oddpart(alpha*delta)*oddpart(v_res).
```

Hence all odd agreement primes already lie in the two linear factors:

```text
R*J     -> D-A or D+A,
alpha*delta -> V-U or V+U.
```

The leftover linear quotient pairs multiply to the fixed reduced residuals `u_res` and `v_res`, so their decoration costs only `B^o(1)`.

The remaining receiver is the exact coupled system

```text
(a_+ m_+)^2-(a_- m_-)^2
 =4*epsilon_k*r*s*n_-*n_+,

(b_+ n_+)^2-(b_- n_-)^2
 =4*epsilon_xi*X*Y*m_-*m_+.
```

Thus the mainline obstruction is no longer a generic binary-quartic energy problem.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cn
```
