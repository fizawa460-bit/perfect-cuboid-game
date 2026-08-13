# Stage14-4cs

Stage14-4cs imports merged 4cr and merged s7-31.

Mainline result:

```text
V(B) << B^(5/8+o(1)).
```

The improvement over the merged 4cr `2/3` bound is `1/24`.

The key exact identification is

```text
oddpart(gcd(c_k^+,c_k^-))
 = oddpart(gcd(P,Q))
 = oddpart(gcd(X,Y)).
```

Thus the second common-core gcd-square peel of 4cq/4cr is the same odd common-root gcd that s7-31 proves satisfies

```text
H^2 | C*u_res.
```

Since also `H^2|X*Y`, the bad common-core part is controlled by `H^2` plus endpoint-small `r*s`, giving

```text
C_bad <= B^(1/4+o(1)).
```

The `5/8` saturation splits into two different components:

```text
upper edge:
  theta=5/16,
  3/16<=phi<=1/4;

lower corner:
  theta=phi=3/16.
```

On the upper edge the second signed quotient pair is already `B^o(1)` and the live structure is the first primitive root line plus the Cayley `C_-/C_+` Gaussian orientation.

On the lower corner

```text
C=u_res=B^o(1),
oddpart(gcd(X,Y))=B^o(1),
```

so common-core Gaussian spacing has no fixed-power leverage; the obstruction is a nearly coprime two-primitive-pair reciprocal factorization problem.

No additional H/tH audit is requested at this stage.

Next: `Stage14-4ct`.
