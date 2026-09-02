# Stage34 final — close Stage29 EXT-C receiver on all seven Paper-C fibers

```text
STAGE=Stage34
STATUS=AUDITED_FINAL_PENDING_PR_MERGE
SOURCE_RECEIVER=R29-EXT-CHANG-C
SOURCE_KERNEL=K16-C3-EXT-C-PRIMITIVE-DIVISOR
PARENT_ROUTE=J12-PARAMETRIC
RECEIVER_STATUS=CLOSED
KERNEL_STATUS=DISCHARGED_BY_STAGE34_REPLACEMENT_ROUTE
PARENT_ROUTE_STATUS=OPEN
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact population contract

Stage34 closes the Stage29 EXT-C receiver on the full hostile-audited Paper-C non-torsion population of seven elliptic fibers

```text
q = 20/21, 80/39, 24/7, 84/13, 48/55, 20/99, 60/11.
```

For the six rank-one fibers the population is

\[
Q=nP_q+T,\qquad n\ge1,\quad T\in E_q(\mathbf Q)_{tors},
\]

with all eight torsion translates included. For `q=60/11` the population is the full rank-two lattice

\[
Q=aG_1+bG_2+T,\qquad (a,b)\in\mathbf Z^2\setminus\{(0,0)\},
\]

again with every torsion translate. The audited Mordell-Weil bases span the full free parts, so this is not a bounded-multiple sample or a selected-ray statement.

The Stage34 target is exactly: no point in this authoritative non-torsion population makes the Paper-C Face-3 quantity a rational square.

## 2. Exact Face-3 reduction

On

\[
E_q:\ y^2=x(x+1)(x+q^2),
\]

Stage34 derives the exact factorization

\[
F_3(Q)=\frac{A_q(x)B_q(x)}{(q^2-x^2)^2},
\]

where

\[
A_q(x)=x^2+q^2,
\]

\[
B_q(x)=(1+q^2)x^2+4q^2x+q^2(1+q^2).
\]

Away from `x=+/-q`, Face-3 is square exactly when `A_q(x)B_q(x)` is square. Equivalently the point lifts to the genus-five cover

\[
C_q:\quad
\begin{cases}
y^2=x(x+1)(x+q^2),\\
z^2=A_q(x)B_q(x).
\end{cases}
\]

The pole points `x=+/-q` are order-four torsion and therefore lie outside the Stage34 non-torsion receiver.

## 3. Replacement route and finite descent

Rather than proving a new global primitive-divisor theorem separately on six one-dimensional sequences and the rank-two lattice, Stage34 replaces that route by an exact rational-point-cover descent.

The direct cover is split through the matching auxiliary curves `K_{q,d}`. Exact local and squareclass analysis reduces every receiver-relevant rational lift to

```text
d in {1,2}.
```

The reconstruction equations, odd-squareclass support lock, and two-adic pattern lock then force every possible matching rational solution into a finite StageA2-style factor-branch overcover.

This is the crucial funnel:

```text
receiver Face-3 square
  => rational point on C_q
  => unique receiver-relevant d=1 or d=2 matching lift
  => StageA2 reconstruction
  => finite factor branch / sign orbit
  => hostile-audited residual set.
```

The projective and pole exceptions encountered in these adapters are classified outside the non-torsion receiver and receive no hidden receiver credit.

## 4. Hostile-audited closure

The complete factor-branch assembly was hostile-reaudited and promoted with zero receiver-relevant residual branches. The subsequent receiver-level hostile audit passed and authorized exactly

```text
all_multiples_closed=true
R29_EXT_CHANG_C_closed=true
receiver_face3_square_points_remaining=0
```

for the authoritative Stage34 population.

The mathematical evidence is frozen at

```text
557aa823f41e1ff5ae31489eb1868fc32f04952e
```

with receiver-level hostile audit review `5088591887` and exact replay

```text
run=33620807240
job=100217139651
conclusion=SUCCESS
```

Thus Stage34 proves:

\[
\boxed{
\text{No non-torsion rational point in any of the seven locked Paper-C fibers has square Face-3.}
}
\]

Equivalently, the exact Stage29 receiver `R29-EXT-CHANG-C` is discharged on its full specified population.

## 5. What Stage34 did not prove

The proof is receiver-restricted. It does **not** claim a complete determination of `C_q(Q)` or of every auxiliary factor-cover rational point.

In particular:

```text
direct_cover_rational_points_complete=false
factor_cover_rational_points_complete=false
candidateB_factor_cover_pointset_empty_claim=false
J12_PARAMETRIC_closed=false
parent_route_closed=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Candidate B contributes only the exact exclusion of its intersection with the receiver. No global cover-point emptiness is inferred from that exclusion.

## 6. Stage29 compatibility writeback

Stage34 returns one exact closure to the frozen Stage29 research frontier:

```text
R29-EXT-CHANG-C = CLOSED_ALL_ADMISSIBLE_MULTIPLES_BY_STAGE34_RECEIVER_RESTRICTED_ROUTE_D
K16-C3-EXT-C-PRIMITIVE-DIVISOR = DISCHARGED_BY_STAGE34_REPLACEMENT_ROUTE
```

The historical Stage29 ledgers are intentionally not rewritten. Instead `34-09/stage29-receiver-writeback-certificate.json` is the compatibility pointer recording the new downstream theorem.

The writeback verifier passed at

```text
run=33622578539
job=100222778353
conclusion=SUCCESS
```

so the live post-Stage29 frontier changes from

```text
active kernels: 13 -> 12
Class 3:         9 -> 8
Class 2:         4 -> 4
```

without changing Stage29's frozen historical audit record.

## 7. Remaining J12-PARAMETRIC frontier

Closing EXT-C does not close its parent route. `J12-PARAMETRIC` remains open with three live kernels:

```text
K16-C3-PESCH-EXPONENT-ONE
K16-C3-MOVING-FIBER-ARITHMETIC
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
```

Stage34 therefore removes exactly one Class-3 obstruction from that route and nothing more.

## 8. Reusable Stage34 result

The downstream reusable theorem is the receiver-level implication chain

```text
full seven-fiber non-torsion MW population
  + exact Face-3 cover equivalence
  + pole=torsion firewall
  + d={1,2} split-to-receiver pullback
  + StageA2 reconstruction / squareclass / 2-adic locks
  + hostile-audited zero factor residual
  => zero Face-3-square points in R29-EXT-CHANG-C.
```

Future work may consume this as a closed receiver/kernel. It must not reopen the q=84/13 or q=80/39 classifications, the 92-factor-branch closure, the receiver implication, or the Stage29 writeback without audit revocation, source mismatch, or materially new evidence.

## 9. Final handoff

Stage34 has no remaining mathematical leaf. The next owner is the post-Stage29 research OS, operating on the remaining live kernels rather than reopening EXT-C.

```text
STAGE34_ALL_MULTIPLES_CLOSED=true
R29_EXT_CHANG_C_CLOSED=true
K16_C3_EXT_C_PRIMITIVE_DIVISOR_DISCHARGED=true
J12_PARAMETRIC_CLOSED=false
PARENT_ROUTE_CLOSED=false
POST_STAGE34_ACTIVE_KERNELS=12
POST_STAGE34_CLASS3_KERNELS=8
POST_STAGE34_CLASS2_KERNELS=4
NEXT_EXACT_LEAF=NONE_STAGE34_COMPLETE
NEXT_OWNER=POST_STAGE29_RESEARCH_OS
AUDIT_STATUS=PASS
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Detailed provenance remains in `stages/stage34/34-01/`, `stages/stage34/34-02/`, `stages/stage34/34-09/`, and `stages/stage34/MAIN-STATE.json`.