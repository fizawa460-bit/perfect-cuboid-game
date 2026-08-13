# Stage14-4cf — balanced eight-cell Gaussian square-divisor descent

## Status

`COMPLETE_BALANCED_EIGHT_CELL_GAUSSIAN_SQUARE_DIVISOR_DESCENT`

Stage14-4ce reduced the current `7/8` endpoint to a dual switch collision with exact primewise residue lock. Merged Stage14-s7-20 then strengthened the same physical pair to `BalancedDoubleAllocationSquareDivisibility`: all four `k` cells and all four `xi` cells lie in positive-power balanced ranges, and the switched cells satisfy positive divisibility by a square.

Stage14-4cf converts those positive divisibilities into an exact Gaussian-integer square descent. The local Legendre conditions are therefore no longer treated as heuristic half-density information: every odd switched cell is the norm of an actual Gaussian divisor whose **square** divides an explicit physical Gaussian host.

No whole-family exponent improvement is claimed here. The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

The remaining obstruction is a moving-host Gaussian square-divisor incidence, not a local residue-density problem.

---

## 1. Imported balanced endpoint

For an off-diagonal same-`(xi,k)` endpoint collision, keep the merged s7-20 cells

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
```

and

```text
a_1=R*S,
b_1=T*J,
a_2=R*T,
b_2=S*J.
```

At the merged 4cd endpoint,

```text
alpha,beta,gamma,delta in [B^(3/16-o(1)), B^(5/16+o(1))],
R,S,T,J                 in [B^(1/8-o(1)),  B^(1/4+o(1))].
```

The switched cells are `beta,gamma` on the `k` allocation and `S,T` on the `xi` allocation. Merged 4ce gives, for every odd prime in a switched cell,

```text
p == 1 mod 4.
```

The finite 2-primary convention is separated throughout and costs only `O(1)` cases.

---

## 2. Positive switched-cell norm divisibilities

Use the s7-20 variables. The switched `k` cells satisfy

```text
beta^2 |
 alpha^2*r_2^4*z_1^2 + delta^2*s_1^4*z_2^2,

gamma^2 |
 delta^2*s_2^4*z_1^2 + alpha^2*r_1^4*z_2^2.
```

Define the Gaussian hosts

```text
Z_beta  = alpha*r_2^2*z_1 + i*delta*s_1^2*z_2,
Z_gamma = delta*s_2^2*z_1 + i*alpha*r_1^2*z_2.
```

Then exactly

```text
beta^2  | N(Z_beta),
gamma^2 | N(Z_gamma).
```

Similarly the switched `xi` cells satisfy

```text
S^2 |
 R^2*x_2^4*omega_1^2 + J^2*y_1^4*omega_2^2,

T^2 |
 J^2*y_2^4*omega_1^2 + R^2*x_1^4*omega_2^2.
```

Define

```text
Z_S = R*x_2^2*omega_1 + i*J*y_1^2*omega_2,
Z_T = J*y_2^2*omega_1 + i*R*x_1^2*omega_2.
```

Thus

```text
S^2 | N(Z_S),
T^2 | N(Z_T).
```

The normalized split coprimalities imply that an odd prime in the relevant switched cell divides neither coordinate of its host. For example, `p|beta` lies in `k_{-,1}` and `k_{+,2}`; hence it cannot divide the opposite square roots `s_1,r_2`, and merged `gcd(k,xi*z_1*z_2)=1` excludes the remaining factors. The `xi` side is identical using `gcd(P_i,Q_i)=1` and merged `gcd(xi,k*omega_1*omega_2)=1`.

---

## 3. Gaussian square-divisor lemma

Let `c` be odd, squarefree and supported on primes `1 mod 4`. Let

```text
Z=A+iB in Z[i],
gcd(c,A*B)=1,
c^2 | A^2+B^2.
```

Then there exists `lambda in Z[i]`, unique up to a Gaussian unit, such that

```text
N(lambda)=c,
lambda^2 | Z.
```

Equivalently

```text
Z=lambda^2*W,
N(W)=(A^2+B^2)/c^2.
```

### Proof

For each `p|c`, choose `p=pi*bar(pi)` in `Z[i]`. Since `p^2|N(Z)` and `p` does not divide both `A,B`, the two conjugate Gaussian primes cannot both divide `Z`. Therefore the full `p`-adic norm valuation is carried by exactly one orientation:

```text
pi^2 | Z  xor  bar(pi)^2 | Z.
```

Choose that orientation and multiply over the pairwise-coprime primes `p|c`. The product is `lambda`, has norm `c`, and its square divides `Z`. The orientation at each prime is forced by `Z`, so the resulting divisor is unique up to a unit.

This is an integral statement; no independent local-density multiplication is used.

---

## 4. Four exact Gaussian descents

After fixing the finite 2-adic case, the lemma applies to the four switched cells. Hence there are Gaussian integers

```text
lambda_beta, lambda_gamma, lambda_S, lambda_T
```

and residual hosts

```text
W_beta, W_gamma, W_S, W_T
```

such that

```text
Z_beta  = lambda_beta^2  * W_beta,   N(lambda_beta)=beta_odd,
Z_gamma = lambda_gamma^2 * W_gamma,  N(lambda_gamma)=gamma_odd,
Z_S     = lambda_S^2     * W_S,      N(lambda_S)=S_odd,
Z_T     = lambda_T^2     * W_T,      N(lambda_T)=T_odd.
```

The four residual norms are the exact integer quotients

```text
q_beta  = N(Z_beta) / beta_odd^2,
q_gamma = N(Z_gamma)/ gamma_odd^2,
q_S     = N(Z_S)    / S_odd^2,
q_T     = N(Z_T)    / T_odd^2.
```

Thus the primewise residue lock of 4ce has been globally assembled into four physical Gaussian square divisors.

---

## 5. Residual-norm defect ledger

Write the balanced `k` cells at exponent scale as

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
3/16 <= theta <= 5/16.
```

Merged endpoint bounds give

```text
r_i,s_i=B^o(1),
z_i=B^(1/8+o(1)).
```

Therefore

```text
N(Z_beta),N(Z_gamma) <= B^(2*theta+1/4+o(1)).
```

Since `beta^2,gamma^2=B^(1-2*theta+o(1))`,

```text
q_beta,q_gamma <= B^(4*theta-3/4+o(1)).
```

Hence

```text
0 <= 4*theta-3/4 <= 1/2.
```

Likewise write

```text
R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)),
1/8 <= phi <= 1/4.
```

Because `x_i,y_i=B^(1/16+o(1))` and `omega_i=B^o(1)`,

```text
N(Z_S),N(Z_T) <= B^(2*phi+1/4+o(1)),
```

and therefore

```text
q_S,q_T <= B^(4*phi-1/2+o(1)),
0 <= 4*phi-1/2 <= 1/2.
```

So every endpoint collision has four Gaussian square descents with residual norms at most `B^(1/2+o(1))`. At the lower balanced edges `theta=3/16` or `phi=1/8`, the corresponding residual norms are only `B^o(1)`.

---

## 6. What this closes, and what it does not

For a **fixed Gaussian host** `Z`, the possible squarefree norm divisors `c` with `lambda^2|Z` are divisor-bounded; in particular their multiplicity is `B^o(1)` for polynomial-size `Z`.

That fact does **not** globalize to a fixed-power saving here because the four hosts themselves move with the physical collision pair. Applying a divisor bound after fixing each moving host and then summing over all hosts merely recovers the ambient host count.

Therefore the following shortcut is invalid:

```text
fixed-host Gaussian divisor multiplicity B^o(1)
=> whole balanced-eight-cell collision saving.
```

The missing theorem is a joint incidence/dispersion estimate across the moving host family.

---

## 7. New minimal mainline receiver

The post-4cf receiver is

```text
BalancedFourHostGaussianSquareDivisorIncidence
```

with the following data retained simultaneously:

```text
same physical (xi,k) pair,
all eight balanced squarefree cells,
Z_beta,Z_gamma,Z_S,Z_T,
lambda_c^2 | Z_c for c in {beta,gamma,S,T},
N(lambda_c)=c_odd,
q_c=N(Z_c)/c_odd^2 <= B^(1/2+o(1)),
canonical interval/reconstruction conditions,
all original coprimality and branch data.
```

A fixed-power gain may come from a genuine moving-host Gaussian incidence theorem, a centered average over the four hosts, or a further determinant/resultant relation coupling the two `k` hosts to the two `xi` hosts. It may not come from multiplying local `1/2` densities or from fixed-host divisor counting.

Merged toolbox-at labels the s-side input as `BalancedDoubleAllocationSquareDivisibility`; 4cf is a compatible physical-lift refinement of that receiver and does not alter the fixed-U/t56 obligation line.

---

## 8. H-line decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

The new step is elementary unique factorization in `Z[i]` plus endpoint size bookkeeping. No new analytic adapter or theorem-hypothesis audit is required yet. A new H line should be opened only if 4cg reaches a genuinely external moving-host Gaussian incidence theorem whose hypotheses need independent certification.

---

## 9. Stage boundary

```text
STAGE14_4CF=COMPLETE_BALANCED_EIGHT_CELL_GAUSSIAN_SQUARE_DIVISOR_DESCENT
MERGED_4CE_IMPORTED=true
MERGED_S7_20_IMPORTED=true
MERGED_TOOLBOX_AT_IMPORTED=true
ODD_SWITCH_CELL_GAUSSIAN_SQUARE_DIVISOR_DESCENT=true
GAUSSIAN_SWITCH_ORIENTATION_UNIQUE_UP_TO_UNIT=true
K_SWITCH_RESIDUAL_NORM_EXPONENT_MAX=1/2
XI_SWITCH_RESIDUAL_NORM_EXPONENT_MAX=1/2
LOWER_BALANCED_EDGE_RESIDUAL_NORM_SUBPOLY=true
FIXED_HOST_GAUSSIAN_SQUARE_DIVISOR_MULTIPLICITY=Bo1
FIXED_HOST_BOUND_GLOBALIZES_TO_POWER_SAVING=false
BALANCED_FOUR_HOST_GAUSSIAN_SQUARE_DIVISOR_INCIDENCE_REQUIRED=true
BALANCED_FOUR_HOST_GAUSSIAN_SQUARE_DIVISOR_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cg attack BalancedFourHostGaussianSquareDivisorIncidence by coupling the two k-host descents and two xi-host descents before any fixed-host divisor summation
```
