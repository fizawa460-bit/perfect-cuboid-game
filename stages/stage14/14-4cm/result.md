# Stage14-4cm — eliminate the quadratic cyclotomic branches and collapse to residual linear factor pairs

## Status

`COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_RESIDUAL_LINEAR_FACTOR_PAIR_COLLAPSE`

Stage14-4cl reduced the physical endpoint obstruction to an off-proportional reciprocal cyclotomic quartic incidence.  It retained three formal branch labels on each agreement product,

```text
-, +, i,
```

coming from

```text
D^4-A^4=(D-A)(D+A)(D^2+A^2),
V^4-U^4=(V-U)(V+U)(V^2+U^2).
```

Stage14-4cm returns the merged 4cg common-core definition to the two residual-product identities before doing any branch counting.  This gives a stronger exact statement that was not used in 4cl:

```text
oddpart(H_k^-)=oddpart(RJ)*oddpart(u_res),
oddpart(H_xi^-)=oddpart(alpha*delta)*oddpart(v_res).
```

Since

```text
H_k^-=D^2-A^2=(D-A)(D+A),
H_xi^-=V^2-U^2=(V-U)(V+U),
```

every odd agreement prime already lies in one of the two **linear** factors.  Therefore both formal quadratic `i` branches are empty on every physical packet.

The `3 x 3 = 9` dominant-branch split of 4cl is consequently an over-refinement of the physical receiver.  The actual odd agreement support is a two-way linear allocation on each side.  Moreover the quotients left after removing the agreement moduli multiply to the already fixed reduced residuals `u_res` and `v_res`.  Hence, after fixing `(C,u_res,v_res)`, the quotient decorations cost only `B^o(1)`.

The remaining cell problem is no longer a binary-quartic energy problem.  It is an exact pair of reciprocal difference-of-squares equations in four linear branch moduli.

No whole-family fixed-power saving is claimed in this stage.  The unconditional endpoint remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported physical packet

Keep the merged 4cl/4ck notation

```text
A = alpha*r,
D = delta*s,
U = R*X,
V = J*Y,
```

where

```text
r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,
```

and

```text
D>A>0,
V>U>0.
```

The agreement and switched products are

```text
K_agree=alpha*delta,
K_switch=beta*gamma,
Xi_agree=R*J,
Xi_switch=S*T.
```

Merged 4cg gives

```text
q_k=C*u_res,
q_xi=C*v_res,
```

with `C` odd, together with

```text
xi*q_k=H_k^+*H_k^-,
k*q_xi=H_xi^+*H_xi^-,
```

where

```text
H_k^+  = D^2+A^2,
H_k^-  = D^2-A^2,
H_xi^+ = V^2+U^2,
H_xi^- = V^2-U^2.
```

The plus-factor common-core definition is

```text
C = oddpart(H_k^+/oddpart(S*T))
  = oddpart(H_xi^+/oddpart(beta*gamma)).
```

Equivalently,

```text
oddpart(H_k^+)  = C*oddpart(S*T),
oddpart(H_xi^+) = C*oddpart(beta*gamma).            (1.1)
```

All statements below are on the same charged-once physical packet.  No independent common-core and cyclotomic savings are multiplied.

---

## 2. Exact odd factorization of the two minus factors

Take odd parts in

```text
xi*q_k=H_k^+*H_k^-.
```

Since

```text
xi=(R*J)*(S*T),
q_k=C*u_res,
oddpart(H_k^+)=C*oddpart(S*T),
```

we obtain

```text
oddpart(RJ)*oddpart(ST)*C*oddpart(u_res)
 = C*oddpart(ST)*oddpart(H_k^-).
```

All cancelled quantities are positive odd integers.  Hence

```text
boxed:
oddpart(H_k^-)
 = oddpart(RJ)*oddpart(u_res).                       (2.1)
```

Similarly, from

```text
k*q_xi=H_xi^+*H_xi^-,
k=(alpha*delta)*(beta*gamma),
q_xi=C*v_res,
oddpart(H_xi^+)=C*oddpart(beta*gamma),
```

we get

```text
boxed:
oddpart(H_xi^-)
 = oddpart(alpha*delta)*oddpart(v_res).              (2.2)
```

These are exact identities, not upper bounds and not density statements.

In particular,

```text
boxed:
oddpart(RJ) | D^2-A^2,                              (2.3)

boxed:
oddpart(alpha*delta) | V^2-U^2.                     (2.4)
```

This is strictly stronger than the fourth-difference divisibilities retained in 4cl.

---

## 3. Both formal quadratic `i` branches are empty

Merged 4cl defines

```text
M_xi^- = gcd(oddpart(RJ),D-A),
M_xi^+ = gcd(oddpart(RJ),D+A),
M_xi^i = gcd(oddpart(RJ),D^2+A^2),
```

and similarly

```text
M_k^- = gcd(oddpart(alpha*delta),V-U),
M_k^+ = gcd(oddpart(alpha*delta),V+U),
M_k^i = gcd(oddpart(alpha*delta),V^2+U^2).
```

For an odd prime `p|RJ`, merged 4cl gives `p∤A*D`.  Since (2.3) gives

```text
p | (D-A)(D+A),
```

and an odd `p` coprime to `D` cannot divide both `D-A` and `D+A`, `p` has exactly one of the two linear labels `-` or `+`.

It cannot have the `i` label.  Indeed if

```text
p | D^2+A^2
```

as well as `p | D^2-A^2`, then `p|2D^2` and `p|2A^2`, contradicting `p∤AD`.

Therefore

```text
boxed:
M_xi^i=1,                                           (3.1)

boxed:
M_xi^-*M_xi^+=oddpart(RJ).                          (3.2)
```

The same proof on the `k` side gives

```text
boxed:
M_k^i=1,                                            (3.3)

boxed:
M_k^-*M_k^+=oddpart(alpha*delta).                   (3.4)
```

Thus the physical three-way allocation is actually an exact two-way linear allocation.

The `1 mod 4` Gaussian branch retained in 4cl is empty on physical agreement support; no Gaussian large-sieve or quadratic-branch estimate is needed for this receiver.

---

## 4. The linear quotients multiply to the fixed reduced residuals

Define the odd linear quotients

```text
e_xi^- = oddpart(D-A)/M_xi^-,
e_xi^+ = oddpart(D+A)/M_xi^+,

e_k^-  = oddpart(V-U)/M_k^-,
e_k^+  = oddpart(V+U)/M_k^+.
```

Using

```text
H_k^-=(D-A)(D+A)
```

with (2.1) and (3.2),

```text
boxed:
e_xi^-*e_xi^+=oddpart(u_res).                       (4.1)
```

Likewise (2.2) and (3.4) give

```text
boxed:
e_k^-*e_k^+=oddpart(v_res).                         (4.2)
```

Therefore, after fixing `(C,u_res,v_res)`, the four odd quotient values have only divisor-many possibilities:

```text
# {(e_xi^-,e_xi^+,e_k^-,e_k^+)}
 <= tau(oddpart(u_res))*tau(oddpart(v_res))
 = B^o(1).                                           (4.3)
```

The powers of two in `D-A,D+A,V-U,V+U` are conditioned separately.  There are only logarithmically many valuation patterns, hence another `B^o(1)` refinement.  After this refinement one may write full positive quotient coefficients

```text
a_-,a_+,b_-,b_+
```

such that

```text
D-A = a_-*M_xi^-,
D+A = a_+*M_xi^+,
V-U = b_-*M_k^-,
V+U = b_+*M_k^+,                                    (4.4)
```

with the complete tuple `(a_-,a_+,b_-,b_+)` ranging over only `B^o(1)` possibilities for fixed residual data.

This removes the apparent fixed-power quotient boxes from the 4cl branch analysis.

---

## 5. Sharp-corner linear moduli are stronger than the 4cl 1/3-pigeonhole moduli

Because the `i` branches vanish,

```text
M_xi^-*M_xi^+=oddpart(RJ),
M_k^-*M_k^+=oddpart(alpha*delta).
```

Hence

```text
max(M_xi^-,M_xi^+) >= oddpart(RJ)^(1/2),            (5.1)
max(M_k^-,M_k^+)   >= oddpart(alpha*delta)^(1/2).   (5.2)
```

In a `(theta,phi)` block,

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(theta+o(1)),
```

so the dominant **linear** moduli have exponents at least

```text
xi side: phi-o(1),
k side:  theta-o(1).                                (5.3)
```

At the unique 4cl sharp corner

```text
(theta,phi)=(5/16,1/4),
```

this improves the old 4cl lower bounds

```text
1/6 -> 1/4  on the xi side,
5/24 -> 5/16 on the k side.                         (5.4)
```

Since

```text
D,A=B^(5/16+o(1)),
V,U=B^(3/8+o(1)),
```

the quotient attached to a dominant linear modulus satisfies

```text
boxed:
|D +/- A|/M_xi,dom <= B^(1/16+o(1)),                (5.5)

boxed:
|V +/- U|/M_k,dom <= B^(1/16+o(1)).                 (5.6)
```

The pointwise box bounds (5.5)-(5.6) are secondary to Section 4: for fixed residual data the quotient coefficients are already divisor-many.

The dominant branch label is now only a sign on each side.  Thus the formal `3 x 3 = 9` dominant types reduce to

```text
(-,-),(-,+),(+,-),(+,+),                            (5.7)
```

and all four are instances of the same linear algebraic template.

---

## 6. Exact reciprocal difference-of-squares system

After the `B^o(1)` quotient and 2-primary refinement, abbreviate

```text
m_- = M_xi^-,
m_+ = M_xi^+,
n_- = M_k^-,
n_+ = M_k^+.
```

Equation (4.4) gives

```text
2D = a_-*m_- + a_+*m_+,
2A = a_+*m_+ - a_-*m_-,                             (6.1)

2V = b_-*n_- + b_+*n_+,
2U = b_+*n_+ - b_-*n_-.                             (6.2)
```

Recall

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y.
```

Let

```text
epsilon_k  = 2^v2(alpha*delta) in {1,2},
epsilon_xi = 2^v2(RJ)          in {1,2}.
```

Because the cells inside each family are squarefree and pairwise coprime,

```text
alpha*delta=epsilon_k*n_-*n_+,
R*J=epsilon_xi*m_-*m_+.                             (6.3)
```

Now subtract the squares in (6.1):

```text
(a_+*m_+)^2-(a_-*m_-)^2
 = 4*A*D
 = 4*r*s*alpha*delta.
```

Using (6.3),

```text
boxed:
(a_+*m_+)^2-(a_-*m_-)^2
 = 4*epsilon_k*r*s*n_-*n_+.                         (6.4)
```

Likewise

```text
boxed:
(b_+*n_+)^2-(b_-*n_-)^2
 = 4*epsilon_xi*X*Y*m_-*m_+.                        (6.5)
```

Equations (6.4)-(6.5) are an exact coupled reciprocal difference-of-squares system.

Conversely, once a legal solution `(m_-,m_+,n_-,n_+)` of (6.4)-(6.5) is fixed together with the quotient/2-primary decoration, (6.1)-(6.2) reconstruct `A,D,U,V`, hence candidate

```text
alpha=A/r,
delta=D/s,
R=U/X,
J=V/Y.
```

The original integrality, positivity, squarefree, coprimality, dyadic, switch-product, orientation, and reconstruction conditions only discard candidates.

Therefore the post-4cl cell fiber reduces, at `B^o(1)` cost, to the solution count of (6.4)-(6.5).

---

## 7. New minimal receiver

Define

```text
CoupledResidualLinearFactorPairDifferenceSquareIncidence
```

to count, after fixing

```text
(C,u_res,v_res),
primitive physical root line,
endpoint-small roots,
2-primary pattern,
one divisor-pair decoration of u_res and v_res,
```

the legal positive squarefree/coprime quadruples

```text
(m_-,m_+,n_-,n_+)
```

satisfying (6.4)-(6.5) and all physical reconstruction masks.

Then

```text
boxed:
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
 <= B^o(1)
    * CoupledResidualLinearFactorPairDifferenceSquareIncidence. (7.1)
```

This is a genuine reduction of algebraic degree and branch complexity:

```text
split quartic equal-value incidence
 -> reciprocal fourth-difference 3-way branches
 -> exact two-way linear factor pairs
 -> two coupled difference-of-squares equations.      (7.2)
```

A generic binary-quartic energy theorem is therefore no longer the correct mainline target.

---

## 8. What this proves and what it does not

Closed in 4cm:

```text
- exact odd factorization of H_k^- and H_xi^- by agreement product times reduced residual;
- xi quadratic cyclotomic branch eliminated;
- k quadratic cyclotomic branch eliminated;
- 3-way allocations replaced by exact 2-way linear allocations;
- linear quotient products identified with fixed u_res and v_res;
- quotient decoration reduced to B^o(1);
- sharp-corner dominant linear moduli strengthened to exponents 1/4 and 5/16;
- dominant linear quotients bounded by B^(1/16+o(1));
- exact reciprocal difference-of-squares system (6.4)-(6.5).
```

Still open:

```text
COUPLED_RESIDUAL_LINEAR_FACTOR_PAIR_DIFFERENCE_SQUARE_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_CELL_FIBER_BO1_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
```

The current unconditional whole-family exponent remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

The finite audit may show very small fibers, but no asymptotic injectivity claim is inferred from finite data.

---

## 9. Relation to parallel routes

At the branch snapshot used for 4cm, Stage14-s7-25 was still an open draft PR and is **not used as a theorem input**.  Its proposed alternate quantifier order may be compared after merge, but no statement from an open PR is needed for Sections 2-7.

Merged X3 is already contained transitively through merged 4cl.  Its relaxed diagonal obstruction remains physically eliminated by 4cl and is not reintroduced by the linear-factor-pair reduction.

The fixed-U `t/tH` coefficient space remains separate.

---

## 10. H-line decision

No external theorem is needed for Stage14-4cm.

The branchwise attack has shown that the quadratic/Gaussian branch is not a live physical branch at all, and the generic binary-quartic energy problem has disappeared.  The remaining object (6.4)-(6.5) is a much narrower exact arithmetic system with residual coefficients whose factor-pair decorations are divisor-bounded.

It is premature to request an external quartic-energy H audit.  Stage14-4cn should first attack the coupled difference-of-squares system directly by cross multiplication, primitive gcd decomposition, and possible factor-pair reconstruction.  A mainline H audit is justified only if that exact system leaves a genuine positive-dimensional average incidence requiring an external theorem.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
```

---

## Stage boundary

```text
STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_RESIDUAL_LINEAR_FACTOR_PAIR_COLLAPSE
MERGED_4CL_IMPORTED=true
MERGED_4CG_COMMON_CORE_REUSED=true
COMMON_CORE_MINUS_ODD_FACTOR_IDENTITY_PROVED=true
ODD_HK_MINUS=oddpart(RJ)*oddpart(u_res)
ODD_HXI_MINUS=oddpart(alpha*delta)*oddpart(v_res)
XI_CYCLOTOMIC_I_BRANCH=1
K_CYCLOTOMIC_I_BRANCH=1
XI_LINEAR_ALLOCATION_PRODUCT=oddpart(RJ)
K_LINEAR_ALLOCATION_PRODUCT=oddpart(alpha*delta)
XI_LINEAR_QUOTIENT_PRODUCT=oddpart(u_res)
K_LINEAR_QUOTIENT_PRODUCT=oddpart(v_res)
FIXED_RESIDUAL_LINEAR_QUOTIENT_DECORATION_COST=Bo1
EXTREME_CORNER_XI_DOMINANT_LINEAR_EXPONENT=1/4
EXTREME_CORNER_K_DOMINANT_LINEAR_EXPONENT=5/16
EXTREME_CORNER_XI_DOMINANT_QUOTIENT_EXPONENT_MAX=1/16
EXTREME_CORNER_K_DOMINANT_QUOTIENT_EXPONENT_MAX=1/16
EXTREME_CORNER_DOMINANT_BRANCH_TYPE_COUNT=4
RECIPROCAL_COUPLED_DIFFERENCE_SQUARE_SYSTEM_PROVED=true
COUPLED_RESIDUAL_LINEAR_FACTOR_PAIR_DIFFERENCE_SQUARE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cn attack CoupledResidualLinearFactorPairDifferenceSquareIncidence by cross multiplication, primitive gcd decomposition, and factor-pair reconstruction before deciding whether any external H theorem is genuinely needed
```
