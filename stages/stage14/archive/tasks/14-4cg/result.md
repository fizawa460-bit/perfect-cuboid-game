# Stage14-4cg — pairwise residual collapse and common-core coupling

## Status

`COMPLETE_PAIRWISE_RESIDUAL_COLLAPSE_AND_COMMON_CORE_COUPLING`

Merged Stage14-4cf replaces the four switched cells `beta,gamma,S,T` by four exact Gaussian square descents

```text
Z_beta  = lambda_beta^2  W_beta,
Z_gamma = lambda_gamma^2 W_gamma,
Z_S     = lambda_S^2     W_S,
Z_T     = lambda_T^2     W_T,
```

with residual norms

```text
q_beta=N(W_beta), q_gamma=N(W_gamma),
q_S=N(W_S),       q_T=N(W_T).
```

Stage14-4cg couples the four hosts before any fixed-host divisor summation. The four residual norms are not independent: the two `k` hosts have exactly the same residual norm, the two `xi` hosts have exactly the same residual norm, and the two remaining residual norms contain a common odd core coming from one exact plus-factor identity.

No whole-family exponent improvement is claimed. The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported endpoint data

For a same-`(xi,k)` off-diagonal endpoint pair keep the s7-20 cells

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

Define

```text
K_switch=beta*gamma,
K_agree =alpha*delta,
Xi_switch=S*T,
Xi_agree =R*J.
```

At the merged endpoint write

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
3/16 <= theta <= 5/16,
```

and

```text
R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)),
1/8 <= phi <= 1/4.
```

The state variables satisfy

```text
u_i=(Q_i-P_i)/g_i=k_{-,i} r_i^2,
v_i=(Q_i+P_i)/g_i=k_{+,i} s_i^2,
```

with `g_i in {1,2}`, together with

```text
v_i^2-u_i^2=xi*z_i^2,
Q_i^2-P_i^2=k*omega_i^2.
```

At the endpoint

```text
r_i,s_i=B^o(1),
z_i=B^(1/8+o(1)),
x_i,y_i=B^(1/16+o(1)),
omega_i=B^o(1).
```

---

## 2. The two k-host residual norms are identical

Stage14-4cf has

```text
N(Z_beta)
 = alpha^2 r_2^4 z_1^2 + delta^2 s_1^4 z_2^2,

N(Z_gamma)
 = delta^2 s_2^4 z_1^2 + alpha^2 r_1^4 z_2^2,
```

and

```text
q_beta = N(Z_beta)/beta^2,
q_gamma= N(Z_gamma)/gamma^2.
```

Use the two state identities

```text
(gamma*delta)^2 s_1^4-(alpha*beta)^2 r_1^4=xi*z_1^2,
(beta*delta)^2 s_2^4-(alpha*gamma)^2 r_2^4=xi*z_2^2.
```

Multiplying the first host norm by `xi` and substituting gives exact cancellation of the mixed term:

```text
xi*N(Z_beta)
 = beta^2 [
     delta^4 s_1^4 s_2^4
     - alpha^4 r_1^4 r_2^4
   ].
```

Similarly

```text
xi*N(Z_gamma)
 = gamma^2 [
     delta^4 s_1^4 s_2^4
     - alpha^4 r_1^4 r_2^4
   ].
```

Therefore

```text
boxed:
q_beta=q_gamma=:q_k.                               (2.1)
```

Define

```text
H_k^+ = delta^2 s_1^2 s_2^2 + alpha^2 r_1^2 r_2^2,
H_k^- = delta^2 s_1^2 s_2^2 - alpha^2 r_1^2 r_2^2.
```

Because `v_i>u_i>0`, `H_k^->0`, and

```text
boxed:
xi*q_k = H_k^+ H_k^-.                              (2.2)
```

Thus the two Gaussian residual hosts `W_beta,W_gamma` lie on one common norm shell `q_k`.

---

## 3. The two xi-host residual norms are identical

Likewise Stage14-4cf gives

```text
N(Z_S)
 = R^2 x_2^4 omega_1^2 + J^2 y_1^4 omega_2^2,

N(Z_T)
 = J^2 y_2^4 omega_1^2 + R^2 x_1^4 omega_2^2,
```

with

```text
q_S=N(Z_S)/S^2,
q_T=N(Z_T)/T^2.
```

Use

```text
(TJ)^2 y_1^4-(RS)^2 x_1^4=k*omega_1^2,
(SJ)^2 y_2^4-(RT)^2 x_2^4=k*omega_2^2.
```

The same mixed-term cancellation gives

```text
k*N(Z_S)
 = S^2 [J^4 y_1^4 y_2^4-R^4 x_1^4 x_2^4],

k*N(Z_T)
 = T^2 [J^4 y_1^4 y_2^4-R^4 x_1^4 x_2^4].
```

Hence

```text
boxed:
q_S=q_T=:q_xi.                                     (3.1)
```

Define

```text
H_xi^+ = J^2 y_1^2 y_2^2 + R^2 x_1^2 x_2^2,
H_xi^- = J^2 y_1^2 y_2^2 - R^2 x_1^2 x_2^2.
```

Since `Q_1Q_2>P_1P_2`, `H_xi^->0`, and

```text
boxed:
k*q_xi = H_xi^+ H_xi^-.                           (3.2)
```

Thus `W_S,W_T` lie on one common norm shell `q_xi`.

---

## 4. Exact coupling of the two plus factors

The plus factors are not independent. From

```text
v_1v_2+u_1u_2
 = 2(Q_1Q_2+P_1P_2)/(g_1g_2)
```

and the cell factorizations,

```text
v_1v_2+u_1u_2 = K_switch * H_k^+,
Q_1Q_2+P_1P_2 = Xi_switch * H_xi^+.
```

Therefore

```text
boxed:
g_1 g_2 K_switch H_k^+
 = 2 Xi_switch H_xi^+.                              (4.1)
```

This is the first exact identity directly coupling the post-4cf `k` Gaussian hosts to the post-4cf `xi` Gaussian hosts.

The factors `g_1g_2` and `2` are purely 2-primary. Put

```text
K_o = oddpart(K_switch),
X_o = oddpart(Xi_switch).
```

Since `gcd(k,xi)=1`, `gcd(K_o,X_o)=1`. Equation (4.1) implies

```text
X_o | H_k^+,
K_o | H_xi^+.
```

Define

```text
C_k  = oddpart(H_k^+/X_o),
C_xi = oddpart(H_xi^+/K_o).
```

Taking odd parts of (4.1) gives

```text
boxed:
C_k=C_xi=:C.                                       (4.2)
```

So the two plus factors share one physical odd common core `C`.

---

## 5. The common core survives in both residual norms

The common core cannot be cancelled by the agreement cells.

### 5.1 xi-agreement primes

Let odd `p|Xi_agree`.

- if `p|R`, then `p|P_1,P_2` and `p∤Q_1Q_2`;
- if `p|J`, then `p|Q_1,Q_2` and `p∤P_1P_2`.

Since

```text
K_switch H_k^+
 = 2(Q_1Q_2+P_1P_2)/(g_1g_2),
```

the right side is nonzero modulo `p`. Also `p∤K_switch`. Hence

```text
gcd(H_k^+, oddpart(Xi_agree))=1.
```

Therefore

```text
gcd(C, oddpart(Xi_agree))=1.                       (5.1)
```

### 5.2 k-agreement primes

Let odd `p|K_agree`.

- if `p|alpha`, then `Q_i=P_i (mod p)` for both states;
- if `p|delta`, then `Q_i=-P_i (mod p)` for both states.

In either case

```text
Q_1Q_2+P_1P_2 = 2P_1P_2 != 0 (mod p).
```

Since

```text
Xi_switch H_xi^+=Q_1Q_2+P_1P_2
```

and `p∤Xi_switch`, we obtain

```text
gcd(H_xi^+, oddpart(K_agree))=1,
```

hence

```text
gcd(C, oddpart(K_agree))=1.                        (5.2)
```

Now use

```text
xi = Xi_switch*Xi_agree,
k  = K_switch*K_agree
```

in (2.2)-(3.2). The switched odd factors cancel from `H_k^+` and `H_xi^+`, while (5.1)-(5.2) prevent the common core from being cancelled by the agreement factors. Thus

```text
boxed:
C | q_k,
C | q_xi.                                          (5.3)
```

Define positive integers

```text
u=q_k/C,
v=q_xi/C.                                          (5.4)
```

The four post-4cf residual norms have therefore collapsed to

```text
q_beta=q_gamma=C*u,
q_S=q_T=C*v.                                       (5.5)
```

---

## 6. Endpoint exponent coupling

At the endpoint

```text
H_k^+ <= B^(2theta+o(1)),
X_o    = B^(3/4-2phi+o(1)),
```

so

```text
C <= B^(2theta+2phi-3/4+o(1)).                     (6.1)
```

Because `C>=1`, any fixed-power endpoint block must satisfy

```text
boxed:
theta+phi >= 3/8-o(1).                             (6.2)
```

The maximal common-core exponent over the balanced window is

```text
boxed:
log_B C <= 3/8+o(1).                                (6.3)
```

Next, from (2.2), (5.4) and the coprimality in Section 5,

```text
u <= B^(2theta-2phi+o(1)).                          (6.4)
```

Since `u>=1`,

```text
boxed:
theta >= phi-o(1).                                 (6.5)
```

Similarly

```text
v <= B^(1/4+2phi-2theta+o(1)),                     (6.6)
```

and `v>=1` forces

```text
boxed:
theta-phi <= 1/8+o(1).                             (6.7)
```

Thus the old rectangular balanced window is reduced to a diagonal strip

```text
boxed:
0 <= theta-phi <= 1/8,
theta+phi >= 3/8                                    (6.8)
```

up to `o(1)` endpoint widths.

Most importantly, multiplying (6.4) and (6.6) cancels `theta-phi`:

```text
boxed:
u*v <= B^(1/4+o(1)).                               (6.9)
```

So after removal of the common core, the two independent residual norm parameters live on a hyperbola of total exponent only `1/4`, rather than two unrelated `B^(1/2)` ranges.

---

## 7. What this closes, and what remains

4cf left four moving Gaussian residual hosts, each of norm at most `B^(1/2+o(1))`.

4cg proves the exact replacement

```text
four residual norms
-> two equal-norm pairs
-> one common odd core C
-> two reduced residuals u,v with u*v<=B^(1/4+o(1)).
```

For fixed `(C,u,v)`, the number of Gaussian integers of norms `Cu` and `Cv` is divisor-bounded. However the physical map

```text
physical collision pair
 -> (C,u,v,W_beta,W_gamma,W_S,W_T)
```

has not yet been proved to have `B^o(1)` fibers. Claiming a whole-family saving by simply counting the norm triples would therefore reverse the quantifier and is forbidden.

The next missing input is a reconstruction/fiber theorem or an incidence theorem that retains the common-core coupling.

---

## 8. New minimal receiver

The post-4cg receiver is

```text
CoupledCommonCoreGaussianResidualIncidence
```

with the data

```text
same physical (xi,k) collision pair,
all eight balanced cells,
q_beta=q_gamma=C*u,
q_S=q_T=C*v,
C odd,
C<=B^(3/8+o(1)),
u*v<=B^(1/4+o(1)),
0<=theta-phi<=1/8+o(1),
theta+phi>=3/8-o(1),
all four Gaussian square-divisor equations,
canonical interval/reconstruction masks,
all primitive coprimalities.
```

A fixed-power gain may now come from proving that this coupled residual datum has only `B^o(1)` physical lifts, or from a centered incidence estimate over the common core. It may not come from treating the four residual hosts independently.

---

## 9. H-line decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

Everything in 4cg is an exact algebraic identity, odd-part divisibility, and endpoint exponent bookkeeping. No external moving-host theorem is imported. If 4ch requires a genuine external Gaussian incidence/large-sieve theorem, H should be reconsidered there.

---

## 10. Stage boundary

```text
STAGE14_4CG=COMPLETE_PAIRWISE_RESIDUAL_COLLAPSE_AND_COMMON_CORE_COUPLING
MERGED_4CF_IMPORTED=true
K_HOST_RESIDUAL_NORMS_EQUAL=true
XI_HOST_RESIDUAL_NORMS_EQUAL=true
K_RESIDUAL_FACTOR=xi*q_k=H_k_plus*H_k_minus
XI_RESIDUAL_FACTOR=k*q_xi=H_xi_plus*H_xi_minus
PLUS_FACTOR_CROSS_IDENTITY=g1*g2*K_switch*H_k_plus=2*Xi_switch*H_xi_plus
COMMON_ODD_PLUS_CORE_EXISTS=true
COMMON_ODD_CORE_DIVIDES_BOTH_RESIDUAL_NORMS=true
COMMON_CORE_MAX_EXPONENT=3/8
ENDPOINT_THETA_PHI_SUM_LOWER=3/8
ENDPOINT_THETA_MINUS_PHI_RANGE=[0,1/8]
REDUCED_RESIDUAL_PRODUCT_MAX_EXPONENT=1/4
PHYSICAL_LIFT_FROM_COMMON_CORE_RESIDUAL_DATA_BO1_PROVED=false
COUPLED_COMMON_CORE_GAUSSIAN_RESIDUAL_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4ch prove a bounded physical-lift/reconstruction theorem for the coupled common-core residual datum, or isolate the remaining positive-dimensional fiber before invoking any external incidence theorem
```
