# Stage14-4cc — critical-xi saturation barrier and the transverse k-shell support receiver

## Purpose

Merged Stage14-4cb and Stage14-s7-14 isolate the current whole-family bound

```text
V(B) << B^(7/8+o(1))
```

at the shared squarefree label

```text
xi = ab = cd = ker(PQ),
```

with exponent-critical geometry

```text
xi ~ B^(3/4),
a,b,c,d ~ B^(3/8),
P,Q ~ B^(1/2),
x,y ~ B^(1/16).
```

Stage14-4cb recorded a sufficient route: any genuine power sparsity in the physically realized `xi` support would beat `7/8`. Stage14-s7-14 then showed that `xi` alone is not enough and introduced the transverse label

```text
k = ker(Q^2-P^2),
gcd(k,xi)=1.
```

Stage14-4cc does two things.

1. It proves an explicit **ambient saturation family** with `B^(3/4-o(1))` distinct critical `xi` labels satisfying the exact shared-label four-cell geometry. Therefore no positive power sparsity in `xi` can be deduced from the four-cell/shared-label constraints alone.
2. It adds a new unconditional support receiver for the transverse `k` shell by factoring
   `Q^2-P^2=(Q-P)(Q+P)`. A `k~B^kappa` shell contains only
   `B^((1+kappa)/2+o(1))` reduced coordinates. Hence every fixed subcritical shell `k<=B^(3/4-delta)` already lies below the current `7/8` ceiling by `delta/2`.

The current exponent remains `7/8`, but the live critical family is narrowed to

```text
xi = B^(3/4+o(1)),
k  >= B^(3/4-o(1)),
n=xi*k >= B^(3/2-o(1)).
```

No physical saturation statement is made.

---

## 1. Merged inputs

We use the following merged results.

### 1.1 Stage14-s7-14 / 4cb shared-label shell

For a reduced coordinate

```text
u=P/Q,
P=a*x^2,
Q=b*y^2,
```

with `a,b` coprime squarefree and

```text
xi=ab,
```

write

```text
xi ~ B^gamma.
```

The merged shell receivers are

```text
N_xi-support(gamma) << B^((1+gamma)/2+o(1)),
N_xi-2cell(gamma)   << B^(1-gamma/6+o(1)).
```

They are two upper bounds on the same shell and are combined by `min`, not multiplication. Their unique crossing is

```text
gamma=3/4,
exponent=7/8.
```

Thus any `xi` shell a fixed positive distance away from `3/4` is already subcritical.

### 1.2 Exact four-cell decomposition

For a physical pair with the same shared label,

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j,
```

where `r,s,t,j` are pairwise coprime squarefree cells.

### 1.3 Transverse label from s7-14

Define

```text
k=ker(Q^2-P^2).
```

Reducedness gives the exact coprimality

```text
gcd(k,xi)=1.
```

The physical edge problem on the critical shell is an off-diagonal collision problem for the pair `(xi,k)`.

### 1.4 Stage14-t50 status

Merged Stage14-t50 closes the external bad-auxiliary aggregate but leaves the selector-sensitive two-modulus Gaussian second moment open. In particular

```text
TH14_NEEDED=true,
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false.
```

Stage14-4cc does not consume an unproved tH14 theorem.

---

## 2. Ambient critical-xi saturation family

The point of this section is a **method barrier**, not a physical lower bound.

Let

```text
T = B^(1/16).
```

Choose four disjoint short prime intervals with scales

```text
r ~ T^4,
j ~ T^4,
s ~ T^2,
t ~ T^2,
```

with the two `T^4` intervals disjoint from one another and the two `T^2` intervals disjoint from one another. For definiteness, fixed disjoint constant-multiple subintervals may be used.

By the standard prime-counting lower bound on fixed relative intervals, the numbers of available primes are

```text
#r = T^(4-o(1)),
#j = T^(4-o(1)),
#s = T^(2-o(1)),
#t = T^(2-o(1)).
```

For each four-tuple define

```text
xi = r*s*t*j,
a  = r*s,
b  = t*j,
c  = r*t,
d  = s*j.
```

Because the prime intervals are pairwise disjoint, the four prime factors of `xi` recover the tuple uniquely. Therefore distinct tuples give distinct labels.

The exponent scales are exactly

```text
xi : 4+4+2+2 = 12 powers of T = B^(3/4),
a,b,c,d : 6 powers of T = B^(3/8).
```

Hence the number of distinct structurally admissible critical labels is

```text
boxed:
# {xi in this family}
  = T^(12-o(1))
  = B^(3/4-o(1)).
```

This family satisfies the exact pairwise-coprime four-cell factorization used by the proof architecture.

Consequently no statement of the form

```text
# structurally admissible critical xi
  << B^(3/4-delta)
```

with fixed `delta>0` can be derived from the shared-label/four-cell algebra alone.

### Important scope lock

This is **not** a lower bound for physically realized perfect-cuboid candidate labels. The construction does not impose the remaining same-kernel / elliptic / physical reconstruction constraints. It only proves that the `xi` algebra itself has enough ambient room to saturate the `3/4` exponent.

Thus

```text
AMBIENT_XI_SATURATION_PROVED=true,
PHYSICAL_XI_SATURATION_PROVED=false.
```

---

## 3. Critical reduced-coordinate geometry can also be saturated algebraically

The same model can be placed on the s7-13 canonical squarepart scale.

Choose two auxiliary primes, independent of the four cells, at scale

```text
x ~ T,
y ~ T,
```

in disjoint intervals. Put

```text
P=a*x^2,
Q=b*y^2.
```

Then

```text
P,Q ~ T^8 = B^(1/2),
x,y ~ B^(1/16),
a,b ~ B^(3/8).
```

Because all six prime ranges are disjoint,

```text
gcd(P,Q)=1.
```

By choosing the constant windows asymmetrically one may ensure `0<P<Q` throughout the model.

Therefore even the canonical reduced-coordinate support geometry at the critical exponents does not itself force a positive power loss in the number of `xi` labels.

Again, no same-`k` physical collision is asserted.

---

## 4. Exact difference-of-squares receiver for k

Now return to a genuine reduced coordinate `0<P<Q`, `gcd(P,Q)=1` and define

```text
D = Q^2-P^2,
D = k*h^2,
```

with `k` squarefree.

Since the physical height range has

```text
P,Q <= B^(1/2+o(1)),
```

we have

```text
D <= B^(1+o(1)).
```

Dyadically suppose

```text
k ~ B^kappa.
```

Then

```text
h <= B^((1-kappa)/2+o(1)).                         (4.1)
```

For fixed `(k,h)`, the integer `D=k*h^2` is fixed. Every positive solution `(P,Q)` is obtained from

```text
u = Q-P,
v = Q+P,
uv=D,
v>u,
u == v (mod 2),
```

via

```text
Q=(u+v)/2,
P=(v-u)/2.
```

Thus the number of `(P,Q)` for fixed `D` is at most the divisor count

```text
tau(D)=B^o(1).
```

Therefore a fixed squarefree `k` in this shell supports at most

```text
boxed:
B^((1-kappa)/2+o(1))
```

reduced coordinates.

There are at most `B^(kappa+o(1))` squarefree `k` in the shell. Summing gives the new shell support bound

```text
boxed:
N_k-support(kappa)
 << B^((1+kappa)/2+o(1)).                          (4.2)
```

The fixed-coordinate `B^o(1)` physical multiplicity transfers (4.2) to the physical family without changing the power exponent.

---

## 5. The k-shell threshold is also 3/4

At

```text
kappa=3/4,
```

(4.2) gives

```text
(1+kappa)/2 = 7/8.
```

More generally, if

```text
kappa <= 3/4-delta,
```

then

```text
boxed:
N_k-support
 << B^(7/8-delta/2+o(1)).                          (5.1)
```

Hence every fixed positive-distance lower `k` shell is already strictly below the current whole-family ceiling.

This is a new unconditional localization:

```text
any 7/8-critical mass must satisfy
k >= B^(3/4-o(1)).
```

There is no corresponding upper localization from this support bound alone; `k` may range up to `B^(1+o(1))`.

---

## 6. Large-twist residual band

On the only `xi` shell capable of attaining the current bound,

```text
xi = B^(3/4+o(1)).
```

Section 5 shows that a `7/8`-critical residual must also satisfy

```text
k >= B^(3/4-o(1)).
```

Since merged s7-14 gives

```text
gcd(xi,k)=1,
n=xi*k,
k<=B^(1+o(1)),
```

we obtain the residual twist band

```text
boxed:
B^(3/2-o(1)) <= n <= B^(7/4+o(1)).                 (6.1)
```

This does not by itself give a new counting exponent. It identifies the only twist-size range in which the present `7/8` architecture can remain critical.

---

## 7. What 4cc closes

Stage14-4cc rules out the naive next theorem

```text
"critical xi labels are automatically power-sparse
because of the shared four-cell decomposition".
```

They are not: the ambient algebra admits `B^(3/4-o(1))` distinct labels on the exact critical cell scales.

It also proves that the transverse `k` label is not optional bookkeeping. The low-`k` shells already save power by elementary difference-of-squares support, so the unresolved family is simultaneously

```text
xi ~ B^(3/4),
k  >= B^(3/4),
```

up to `B^o(1)` exponent widths.

The next genuine task is therefore an **average recurrence / off-diagonal collision theorem for `(xi,k)` in the large-twist band**, not another `xi`-support estimate.

---

## 8. tH decision

Merged Stage14-t50 has changed the project-level tH status.

```text
TH14_NEEDED=true.
```

Stage14-tH14 should attack the selector-sensitive two-modulus Gaussian second moment while retaining:

- signed common-refinement aggregation;
- shared `U/V` modulus group;
- divisor-coupled hyperbola;
- canonical/physical selector;
- two distinct split auxiliary primes;
- t32 completion before pair collapse.

The target contract is the t50 bound

```text
sum_{p!=q} |sum_R S_R(p,q)|^2
  << P^2 * (sum_R ||w_R||_2^2) * B^o(1).
```

4cc does not assume this theorem.

---

## 9. Stage boundary

```text
STAGE14_4CC=CRITICAL_XI_AMBIENT_SATURATION_AND_TRANSVERSE_K_SHELL_LOCALIZATION
MERGED_4CB_IMPORTED=true
MERGED_S7_14_IMPORTED=true
MERGED_T50_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
CRITICAL_XI_EXPONENT=3/4
AMBIENT_CRITICAL_XI_SATURATION=B^(3/4-o(1))
AMBIENT_XI_SATURATION_PROVED=true
PHYSICAL_XI_SATURATION_PROVED=false
FOUR_CELL_GEOMETRY_ALONE_IMPLIES_XI_POWER_SPARSITY=false
TRANSVERSE_LABEL_K=ker(Q^2-P^2)
K_SHELL_COORDINATE_SUPPORT_EXPONENT=(1+kappa)/2
LOW_K_SHELL_SAVING=delta/2_for_kappa<=3/4-delta
SEVEN_EIGHT_CRITICAL_K_LOWER_EXPONENT=3/4
CRITICAL_RESIDUAL_TWIST_LOWER_EXPONENT=3/2
CRITICAL_RESIDUAL_TWIST_UPPER_EXPONENT=7/4
OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false
REALIZED_LABEL_SPARSITY_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH14_NEEDED=true
NEXT=Stage14-4cd
```
