# Stage14-4cm

Stage14-4cm imports merged 4cl and merged s7-25.

The exact odd-part product identities imply

```text
oddpart(H_k^-)=oddpart(R*J)*oddpart(u_res),
oddpart(H_xi^-)=oddpart(alpha*delta)*oddpart(v_res).
```

Therefore all odd agreement support lies in the two linear factors of the minus terms:

```text
R*J -> (D-A),(D+A),
alpha*delta -> (V-U),(V+U).
```

The quadratic `i` branches of 4cl are empty on physical packets.  The nine cyclotomic branch types reduce to four signed linear-linear types.

Merged s7-25 already power-saves every fixed-distance block below `theta=5/16`, so only the top-theta edge remains.  There the dominant linear moduli have exponents `phi` and `5/16`, and the corresponding signed quotient pair has total raw support exponent `1/8`.

This support statement alone is not promoted to a whole-family saving because the switch-product-to-quotient fiber is still unproved.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cn
```
