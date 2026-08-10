# Stage14-s7-11 — multicell torus quotient and the 13/14 architecture barrier

## Purpose

Merged Stage14-s7-10 and merged Stage14-4by prove the current unconditional whole-family bound

```text
V(B) << B^(13/14+o(1)).
```

The thin branch uses the adjacent two-cell detector

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2)
```

and the uniform inert-prime mixed Fourier estimate from s7-10 / 4by to obtain

```text
N_2cell(A,B) << (AB)^(2/3) B^o(1),
```

so a forced adjacent coefficient `C=AB` receives relative saving

```text
C^(-1/3).
```

A natural next attempt is to vary three or all four squarefree cells simultaneously and hope that a higher-dimensional square sieve produces a stronger relative saving. This stage audits that idea exactly.

The conclusion is negative and structural:

1. the three-cell detector factors through the same two-variable quotient and has a one-dimensional torus kernel;
2. the four-cell detector factors through the same two-variable quotient and has a two-dimensional torus kernel;
3. even an *ideal* d-dimensional square-root Fourier theorem combined with the ordinary square sieve gives relative saving only `V^(-1/(d+1))`, so d=3 and d=4 are weaker than the proved two-cell `V^(-1/3)` receiver;
4. pairwise applications of the same two-cell square detector cannot have their savings multiplied without a new independent arithmetic condition;
5. with the merged thick saving `H^(-4/5)` and the proved two-cell coefficient saving `C^(-1/3)`, the exact threshold barrier remains `13/14`.

No new whole-family exponent is claimed in s7-11.

---

## 1. Merged inputs and current ledger

We use only merged inputs.

### 1.1 s7-10 / 4by two-cell theorem

For the universal adjacent-cell detector

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2),
```

all inert-prime additive Fourier modes satisfy the required `O(p)` bound. The corresponding rectangle square sieve gives

```text
N_2cell(A,B) << (AB)^(2/3) B^o(1).                 (1.1)
```

Thus an adjacent coefficient `C=AB` gains

```text
C^(-1/3).                                           (1.2)
```

### 1.2 4bx optimized thick theorem

For square-part packet thickness `Hmin`, merged 4bx proves

```text
N_packet << M * Hmin^(-4/5) B^o(1).                (1.3)
```

### 1.3 current whole-family bound

Combining (1.1)--(1.3) with the denominator/numerator split gives

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14.       (1.4)
```

The current optimal cutoffs are

```text
lambda = 13/28,
nu     = 11/28,
tau    = 5/56.                                      (1.5)
```

---

## 2. Four-cell coordinates

After the product-square descent, the shared squarefree label is written

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j,
```

with pairwise-coprime squarefree cells `r,s,t,j`.

Ignoring the fixed square-part squares, which only contribute rational square scalings to the quadratic character, the same-kernel detector is

```text
G4(r,s,t,j)
 = ((t*j)^2-(r*s)^2) * ((s*j)^2-(r*t)^2).          (2.1)
```

The physical reduced coordinates are proportional to

```text
u ~ r*s/(t*j),
v ~ r*t/(s*j).                                     (2.2)
```

The quadratic character of (2.1) depends only on these two ratios.

---

## 3. Three cells collapse to the two-cell detector

Fix `j` and vary `r,s,t`. After absorbing fixed rational squares, put

```text
G3(R,S,T)
 = (T^2-R^2*S^2) * (S^2-R^2*T^2).                 (3.1)
```

For `T!=0`, set

```text
q=S/T.
```

Then exact algebra gives

```text
G3(R,S,T)
 = T^4 * (1-R^2*q^2) * (q^2-R^2)
 = T^4 * H(R,q).                                   (3.2)
```

Therefore for every odd good prime,

```text
chi(G3(R,S,T)) = chi(H(R,S/T)).                    (3.3)
```

The detector is invariant under

```text
(S,T) -> (lambda*S, lambda*T),                     (3.4)
```

because `G3` is multiplied by `lambda^4`.

Hence the three-cell local detector has only two effective multiplicative variables. Its torus-kernel dimension is one.

---

## 4. Four cells collapse to the same two-cell detector

On the torus `r*s*t*j != 0`, set

```text
alpha=r/j,
beta =s/t.
```

Then

```text
boxed:
G4(r,s,t,j)=(t*j)^4 * H(alpha,beta).                (4.1)
```

Indeed,

```text
(t*j)^4 H(r/j,s/t)
 = ((t*j)^2-(r*s)^2) * ((s*j)^2-(r*t)^2).
```

Thus

```text
chi(G4)=chi(H(r/j,s/t)).                            (4.2)
```

There are two independent torus-kernel scalings:

```text
(r,j) -> (alpha0*r, alpha0*j),
(s,t) -> (beta0*s,  beta0*t).                      (4.3)
```

Under (4.3), `G4` is multiplied by `(alpha0*beta0)^4`, so its quadratic character is unchanged.

Hence the four-cell detector has quotient rank two and torus-kernel dimension two.

The integer conditions that the cells are squarefree and pairwise coprime are important for the exact parametrisation, but they do not create a second local square detector at good auxiliary primes. They therefore cannot by themselves justify multiplying independent square-sieve savings.

---

## 5. Exact Fourier-fiber identity for three cells

The torus quotient is visible directly in the complete Fourier transform.

Let

```text
f(R,q)=chi(H(R,q))
```

on `(F_p^*)^2`, and define

```text
T3(h,k,l)
 = sum_{R,S,T in F_p^*}
   chi(G3(R,S,T)) e_p(hR+kS+lT).                   (5.1)
```

Substitute `S=qT`. Then

```text
T3(h,k,l)
 = sum_{R,q} f(R,q)e_p(hR)
   sum_{T!=0} e_p(T(kq+l)).                        (5.2)
```

For

```text
A(c)=sum_{T!=0}e_p(cT),
```

we have

```text
A(0)=p-1,
A(c)=-1  (c!=0).                                   (5.3)
```

Consequently, if `k!=0` and `q0=-l/k` is nonzero,

```text
T3(h,k,l)
 = p * sum_R f(R,q0)e_p(hR)
   - sum_{R,q}f(R,q)e_p(hR).                       (5.4)
```

If `k!=0` but `q0=0`, the first term is absent. If `k=0,l!=0`, only the negative two-cell partial transform remains. If `k=l=0`,

```text
boxed:
T3(h,0,0)
 = (p-1) * sum_{R,q} f(R,q)e_p(hR).                (5.5)
```

Thus the inherited two-cell axis transform is amplified by an entire torus fiber. The three-cell transform is not a new independent character geometry; it is a fibered lift of the two-cell transform.

---

## 6. Exact Fourier-fiber identity for four cells

Similarly, on `(F_p^*)^4`, write

```text
r=alpha*j,
s=beta*t.
```

For additive frequencies `(h_r,h_s,h_t,h_j)`, the complete transform equals

```text
T4
 = sum_{alpha,beta} f(alpha,beta)
   A(h_r*alpha+h_j)
   A(h_s*beta+h_t),                                (6.1)
```

with the same function `A` from (5.3).

So every four-cell Fourier mode is an explicit linear combination of:

- the complete two-cell trace;
- one-dimensional row/column slices of the two-cell detector;
- individual values of the two-cell detector.

This is an exact rank-two quotient identity. Extra cell variables create torus fibers, not new independent Kummer monodromy.

---

## 7. Why an ideal higher-dimensional square sieve is already weaker

There is a second, independent obstruction.

Suppose optimistically that a d-variable detector on a rectangle of volume `V` had perfect square-root complete Fourier control, so the square-sieve correlation term at auxiliary-prime scale `L` behaved like

```text
L^d.
```

The usual square-sieve diagonal is

```text
V/L.
```

Balancing

```text
V/L = L^d
```

gives

```text
L=V^(1/(d+1)),
N_d(V) << V^(d/(d+1)+o(1)).                        (7.1)
```

Thus the best relative saving available from this idealized one-square-condition mechanism is

```text
boxed:
V^(-1/(d+1)).                                      (7.2)
```

In particular,

```text
d=1 : V^(-1/2),
d=2 : V^(-1/3),
d=3 : V^(-1/4),
d=4 : V^(-1/5).                                   (7.3)
```

The proved two-cell receiver is therefore the strongest member of this sequence after the one-cell case. Passing from two cells to three or four cells makes the square-sieve exponent *worse*, even before accounting for the torus degeneracy of Sections 3--6.

---

## 8. Multiple two-cell bounds do not multiply automatically

One might instead apply the proved two-cell theorem to several adjacent pairs and try to multiply the savings.

This is not valid from the present theorem set.

Every pairwise receiver is testing the same single square condition

```text
G1*G2 = square.
```

Abstractly, if a universe has `N` states and each of several pairwise receivers individually proves a bound `N^(2/3)`, all receivers may be saturated by the same exceptional subset of size `N^(2/3)`. Their intersection can therefore still have size `N^(2/3)`.

Without a second independent arithmetic condition or a proved transverse correlation theorem, the valid operation is taking the minimum of compatible pairwise bounds, not multiplying their relative savings.

Therefore

```text
PAIRWISE_TWO_CELL_SAVINGS_MULTIPLY=false.           (8.1)
```

---

## 9. Exact current architecture barrier

Let

```text
lambda : denominator cutoff,
nu     : numerator cutoff,
tau    : square-part thickness cutoff.
```

Merged 4bx and s7-10 give the active exponent ledger

```text
E1 = 2*lambda,
E2 = 1+nu-lambda,
E3 = 1-4*tau/5,
E4 = 1-(nu-2*tau)/3.                               (9.1)
```

The denominator-thin analogue is smaller at the optimum.

Suppose all active terms were at most `E`. Then

```text
lambda <= E/2,
nu <= E-1+lambda <= 3E/2-1,
tau >= (5/4)(1-E),
nu >= 2*tau+3(1-E) >= (11/2)(1-E).                (9.2)
```

Combining the upper and lower bounds for `nu`,

```text
(11/2)(1-E) <= 3E/2-1,
```

which is equivalent to

```text
boxed:
E >= 13/14.                                        (9.3)
```

Equality is attained by

```text
lambda=13/28,
nu=11/28,
tau=5/56.                                          (9.4)
```

Hence `13/14` is the exact threshold barrier of the current optimized-thick + one-square-condition two-cell architecture.

### 9.1 Even optimistic 3-cell / 4-cell substitution regresses

If one replaced the proved coefficient saving exponent `1/3` by the ideal d-cell square-sieve exponent `1/(d+1)`, while keeping the same thick theorem, the corresponding optimistic minimax barriers would be

```text
ideal 3-cell (gamma=1/4): E >= 15/16,
ideal 4-cell (gamma=1/5): E >= 17/18.               (9.5)
```

Both are worse than `13/14`.

So no threshold retuning of a direct 3-cell or 4-cell square sieve can improve the current theorem.

---

## 10. What must change next

The multicell extension is closed as a primary route.

To break `13/14`, at least one qualitatively new input is required. The most immediate target is not a higher-dimensional version of the same square sieve, but an **unbalanced first-point incidence theorem** that attacks the branches currently charged trivially by

```text
small denominator:  2*lambda,
small numerator:    1+nu-lambda.                  (10.1)
```

The already-proved two-cell mixed transform should be retained inside those unbalanced sectors instead of discarding them before the squareclass analysis. A successful unbalanced rectangle/collision theorem would correlate the first-coordinate size with the partner/twist condition and could move the minimax without introducing a redundant third or fourth cell variable.

A second possible route would require a genuinely independent detector sensitive to the torus fibers. Pairwise coprimality alone is exponent-neutral and is not such a detector.

Therefore the next s7 task is:

```text
Stage14-s7-12:
construct an unbalanced denominator/numerator two-point incidence receiver,
using the proved two-cell mixed Fourier theorem inside the small-coordinate sectors;
if that cannot save, isolate its exact barrier and identify the required second detector.
```

---

## 11. Stage boundary

```text
STAGE14_S7_11=COMPLETE_MULTICELL_TORUS_QUOTIENT_AND_13_14_ARCHITECTURE_BARRIER
MERGED_S7_10_IMPORTED=true
MERGED_4BY_IMPORTED=true
THREE_CELL_DETECTOR_FACTORS_THROUGH_TWO_CELL_QUOTIENT=true
FOUR_CELL_DETECTOR_FACTORS_THROUGH_TWO_CELL_QUOTIENT=true
THREE_CELL_TORUS_KERNEL_DIMENSION=1
FOUR_CELL_TORUS_KERNEL_DIMENSION=2
THREE_CELL_FOURIER_FIBER_IDENTITY_EXACT=true
FOUR_CELL_FOURIER_FIBER_IDENTITY_EXACT=true
IDEAL_D_CELL_SQUARE_SIEVE_RELATIVE_SAVING=V^(-1/(d+1))
IDEAL_THREE_CELL_RELATIVE_SAVING=V^(-1/4)
IDEAL_FOUR_CELL_RELATIVE_SAVING=V^(-1/5)
MULTICELL_IMPROVES_PROVED_TWO_CELL_SAVING=false
PAIRWISE_TWO_CELL_SAVINGS_MULTIPLY=false
OPTIMIZED_THICK_TWO_CELL_ARCHITECTURE_BARRIER=13/14
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-12
```
