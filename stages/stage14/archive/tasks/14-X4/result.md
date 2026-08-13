# Stage14-X4 — physical diagonal elimination in the charged-once X packet

## Status

`COMPLETE_PHYSICAL_PROPORTIONAL_BRANCH_ELIMINATION_AND_X_ROUTE_ALIGNMENT`

Stage14-X3 reduced the charged-once X1/X2 packet to the split quartic equality

```text
G*q_k*r*s*F(U,V) = 2*q_xi*X*Y*F(A,D),
F(a,b)=a*b*(b-a)*(b+a),
```

with moving agreement cells

```text
A=alpha*r, D=delta*s, U=R*X, V=J*Y,
```

and left the relaxed coefficient-diagonal/proportional family as the first object that X4 had to test against the omitted physical constraints.

Since X3 merged, Stage14-4cl independently solved exactly this physical proportional branch on main. X4 therefore does not claim priority for that theorem. Its role is to import the merged 4cl elimination into the X1 -> X3 charged-once quantifier order, independently recheck the logical bridge, and freeze the next X-specific receiver.

The unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

No canonical index or exponent ledger is modified.

---

## 1. X3 quantifier order is preserved

Condition exactly as in X3 on

```text
(C,u_res,v_res),
primitive positive xi-root line X_root=(x1,y1,x2,y2),
endpoint-small roots (r1,r2,s1,s2,g1,g2).
```

Put

```text
q_k=C*u_res,
q_xi=C*v_res,
r=r1*r2,
s=s1*s2,
X=x1*x2,
Y=y1*y2,
G=g1*g2.
```

The only fixed-power quantity still moving is the balanced agreement-cell packet `(alpha,delta,R,J)`, followed by divisor-many switched-cell completion. Thus importing 4cl here does not double-charge common-core or dual-CRT data: the X1 charged-once packet is retained.

The physical coprimality inherited from `gcd(xi,k)=1` is

```text
gcd(alpha,delta)=1,
gcd(R,J)=1,
gcd(alpha*delta,R*J)=1.                 (1.1)
```

---

## 2. The whole proportional branch is physically empty

The relaxed X3 obstruction contains the coefficient diagonal `(U,V)=(A,D)`. More generally test the full proportional branch

```text
U/A = V/D,
```

or

```text
U*D=V*A.                                (2.1)
```

Substituting the physical cells gives

```text
R*delta*X*s = J*alpha*Y*r.              (2.2)
```

By (1.1), `R*delta` and `J*alpha` are coprime away from the finite 2-primary convention. Euclid's lemma therefore gives

```text
oddpart(R*delta) | Y*r,
oddpart(J*alpha) | X*s.                  (2.3)
```

At the balanced endpoint,

```text
R,J = B^(phi+o(1)),
alpha,delta = B^(theta+o(1)),
X,Y = B^(1/8+o(1)),
r,s = B^o(1),
theta+phi >= 3/8-o(1).                  (2.4)
```

Hence (2.3) would force

```text
B^(theta+phi-o(1)) <= B^(1/8+o(1)),
```

contradicting (2.4) by the fixed exponent gap

```text
3/8 - 1/8 = 1/4.                        (2.5)
```

Therefore

```text
PHYSICAL_PROPORTIONAL_QUARTIC_BRANCH_EMPTY=true.
```

In particular the exact relaxed diagonal family constructed in X3 cannot survive the physical X packet. X3's relaxed fixed-power obstruction is a valid guard against a quartic-energy shortcut, but it is not a physical counterexample.

This elimination is stronger than required by the X3 instruction: both switch-product integrality conditions may be retained throughout, but the proportional branch already dies before they are needed.

---

## 3. Both switch-product integrality conditions remain active off diagonal

For the surviving off-proportional branch, X3/4ck give

```text
S*T = H_k^+ H_k^- /(q_k R J),
beta*gamma = H_xi^+ H_xi^- /(q_xi alpha delta),
```

with

```text
H_k^+ H_k^- = D^4-A^4,
H_xi^+ H_xi^- = V^4-U^4.
```

Thus exact physical integrality forces

```text
D^4-A^4 = q_k*(R*J)*(S*T),              (3.1)
V^4-U^4 = q_xi*(alpha*delta)*(beta*gamma), (3.2)
```

and in particular

```text
R*J | D^4-A^4,
alpha*delta | V^4-U^4.                  (3.3)
```

These are not optional decorations. Any X-route off-diagonal theorem must keep them before taking absolute values or collapsing to a generic quartic equal-value energy.

---

## 4. Cross-role prime locks refine the off-diagonal equality

After the divisor-many moving gcds are conditioned, primitive quartic factors

```text
a, b, b-a, b+a
```

have pairwise disjoint odd support. Therefore every odd good prime in the off-diagonal equality has a unique left-factor/right-factor allocation cell in a `4 x 4` matrix.

The reciprocal divisibilities (3.3) then allocate agreement primes on each side to one of

```text
-, +, i
```

corresponding to

```text
b-a, b+a, b^2+a^2.
```

For the `i` branch, every odd prime is `1 mod 4` by the primitive sum-of-two-squares criterion.

This is the exact physical structure missing from the relaxed X3 countermodel. X4 imports the merged 4cl theorem here only after preserving the X1/X2 charged-once coefficient space.

---

## 5. What X4 closes and what remains

X4 closes:

```text
- X3 relaxed coefficient diagonal as a physical possibility;
- the entire physical proportional quartic branch;
- the ambiguity over whether the X route may use the merged 4cl elimination without double counting;
- the requirement that both switch integrality constraints and cross-role prime locks remain attached off diagonal.
```

X4 does not close:

```text
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence.
```

The sharp endpoint still has the nine dominant reciprocal cyclotomic branch types identified by 4cl. Therefore no new whole-family power saving follows here.

The correct X continuation is to keep the X1 charged-once outer data fixed and attack those off-diagonal branch types directly, rather than returning to generic binary-quartic energy.

---

## 6. H / tH decision

No X4-specific H line is needed.

The proportional obstruction has been eliminated algebraically, while the surviving object is already more structured than generic quartic energy: it carries reciprocal fourth-difference moduli, a `4 x 4` prime-allocation matrix, and the `-,+,i` branch labels. An external quartic-energy audit before using those constraints would enlarge the coefficient space and lose the point of X4.

```text
X4_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
```

---

## Boundary

```text
STAGE14_X4=COMPLETE_PHYSICAL_PROPORTIONAL_BRANCH_ELIMINATION_AND_X_ROUTE_ALIGNMENT
MERGED_X3_IMPORTED=true
MERGED_4CL_IMPORTED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
RELAXED_DIAGONAL_FIXED_POWER_OBSTRUCTION_IMPORTED=true
PHYSICAL_PROPORTIONAL_QUARTIC_BRANCH_EMPTY=true
RELAXED_DIAGONAL_OBSTRUCTION_SURVIVES_PHYSICAL_MASKS=false
PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false
PROPORTIONAL_BRANCH_ENDPOINT_EXPONENT_GAP=1/4
BOTH_SWITCH_PRODUCT_INTEGRALITY_CONDITIONS_RETAINED=true
CROSS_ROLE_PRIME_LOCKS_RETAINED=true
QUARTIC_GOOD_PRIME_ALLOCATION_MATRIX_4X4_IMPORTED=true
RECIPROCAL_THREE_WAY_CYCLOTOMIC_ALLOCATION_IMPORTED=true
REMAINING_RECEIVER=OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
OFF_DIAGONAL_RECIPROCAL_CYCLOTOMIC_QUARTIC_ALLOCATION_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X4_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
NEXT_RECOMMENDED=Stage14-X5 attack the nine off-diagonal reciprocal cyclotomic branch types in the X1 charged-once quantifier order
```
