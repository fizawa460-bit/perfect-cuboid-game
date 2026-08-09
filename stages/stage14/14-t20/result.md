# Stage14-t20 — raw-edge squareclass collision factorization

## Purpose

Stage14-t19 identified the conditioned discriminant squareclass with the missing third-face squareclass on the frozen exactly-two ledger. Before using its collision energy asymptotically, one population correction is necessary: triple objects are not members of the exactly-two-object set.

Stage14-t20 therefore moves the collision problem to the canonical **raw-pair edge population**. An exactly-two object contributes one raw-pair edge; a triple object contributes its three unordered pairs of integral faces. This is the same edge population already used by the Stage14 graph identity

\[
E(B)=N_2(B)+3T(B).
\]

On that corrected population, the trivial missing-face squareclass detects triples exactly.

## 1. Correct edge-level collision energy

For a raw-pair edge `e`, let `s_e` be the side shared by the two integral faces and let `d_e` be the integer space diagonal. The third, possibly missing, face has squared length

\[
m_e=d_e^2-s_e^2.
\]

Define

\[
\kappa(e)=[m_e]\in\mathbf Q^\times/\mathbf Q^{\times2}.
\]

For each squareclass `k`, put

\[
n_k(B)=\#\{e:d_e\le B,\ \kappa(e)=k\},
\qquad
Q_{\rm edge}(B)=\sum_k n_k(B)^2.
\]

An exactly-two object has a nonsquare third face, so its unique edge has `kappa != 1`. A triple object has three raw-pair edges and on every one the third face is integral, so all three have `kappa=1`. Consequently

\[
\boxed{n_1(B)=3T(B)}
\]

and hence

\[
\boxed{9T(B)^2\le Q_{\rm edge}(B).}
\]

Therefore the corrected sufficient target is

\[
\boxed{Q_{\rm edge}(B)=o(B)}
\quad\Longrightarrow\quad
T(B)=o(\sqrt B).
\]

This supersedes the t19 asymptotic sentence that used collision energy on exactly-two objects only. The t19 finite ledger itself is unchanged because `T(B)=0` at all frozen cutoffs through `2,000,000`, so the exactly-two objects and raw-pair edges coincide there.

## 2. Coprime difference-of-squares factorization

Fix a raw-pair edge and write

\[
g=\gcd(d,s),\qquad D=d/g,\qquad C=s/g,
\]

so `gcd(D,C)=1`. Put

\[
h=\gcd(D-C,D+C).
\]

Because `D` and `C` are coprime,

\[
h\in\{1,2\}.
\]

Define

\[
A=\frac{D-C}{h},\qquad B=\frac{D+C}{h}.
\]

Then

\[
\gcd(A,B)=1
\]

and

\[
m=d^2-s^2=g^2h^2AB.
\]

Thus the edge squareclass is exactly

\[
\boxed{\kappa(e)=[AB].}
\]

Write the two coprime positive integers uniquely as

\[
A=\alpha r^2,\qquad B=\beta u^2,
\]

where `alpha,beta` are positive squarefree integers. Coprimality gives

\[
\gcd(\alpha,\beta)=1,
\qquad
\boxed{k=\alpha\beta}.
\]

Equivalently,

\[
D-C=h\alpha r^2,
\qquad
D+C=h\beta u^2,
\]

so

\[
2D=h(\alpha r^2+\beta u^2),
\qquad
2C=h(\beta u^2-\alpha r^2).
\]

For a fixed squareclass `k`, every edge therefore chooses a coprime squarefree partition

\[
k=\alpha\beta.
\]

This converts an equality of opaque global squareclasses into a finite partition problem plus square variables.

## 3. Sum-of-two-squares support restriction

The third face is also the sum of squares of its two side lengths. Remove their gcd and write

\[
m=g_0^2(U^2+V^2),\qquad \gcd(U,V)=1.
\]

If an odd prime `p = 3 mod 4` divided `U^2+V^2`, then `-1` would be a quadratic residue modulo `p`; equivalently the standard sum-of-two-squares argument forces `p` to divide both `U` and `V`, contradicting primitivity. Therefore every prime in the squarefree kernel satisfies

\[
\boxed{p=2\quad\text{or}\quad p\equiv1\pmod4.}
\]

So the collision kernel lives entirely on the split Gaussian-prime support (plus `2`). This is an exact arithmetic restriction, not a density estimate.

## 4. Partition-resolved collision energy

For coprime squarefree `alpha,beta`, define

\[
N_{\alpha,\beta}(B)
=\#\{e:d_e\le B,\ A_e=\alpha r^2,\ B_e=\beta u^2\}.
\]

For `k` squarefree,

\[
n_k(B)=\sum_{\substack{\alpha\beta=k\\(\alpha,\beta)=1}}
N_{\alpha,\beta}(B).
\]

There are at most `2^{omega(k)}` such ordered partitions. Cauchy--Schwarz therefore gives

\[
n_k(B)^2
\le
2^{\omega(k)}
\sum_{\alpha\beta=k}N_{\alpha,\beta}(B)^2.
\]

Since `m_e<d_e^2<=B^2`, every observed kernel has `k<=B^2`; hence uniformly

\[
2^{\omega(k)}=B^{o(1)}.
\]

Define the stricter split energy

\[
Q_{\rm split}(B)
=\sum_{\alpha,\beta}N_{\alpha,\beta}(B)^2.
\]

Then the exact partition reduction yields

\[
\boxed{Q_{\rm edge}(B)\le B^{o(1)}Q_{\rm split}(B).}
\]

In particular, any fixed power saving

\[
Q_{\rm split}(B)=O(B^{1-\delta})
\quad(\delta>0)
\]

would imply `Q_edge(B)=o(B)` and therefore `T(B)=o(sqrt(B))`.

This is the first collision target in the t-track where equal squareclasses are replaced by an explicit coprime factor-kernel correlation.

## 5. Frozen finite audit

The deterministic audit regenerates the exact Stage14 graph through `B=2,000,000`, expands every object into raw-pair edges, and checks on every edge:

- `m=d^2-s^2` is the third-face squared length;
- `h=gcd(D-C,D+C)` is `1` or `2`;
- `A,B` are coprime;
- `[m]=[AB]=alpha*beta`;
- the kernel primes are only `2` or `1 mod 4`;
- triple edges, if present, have trivial class and exactly-two edges have nontrivial class.

At the frozen ceiling `T=0`, so there are 356 raw-pair edges, all 356 squareclasses are distinct, and both

\[
Q_{\rm edge}=Q_{\rm split}=356.
\]

The same equality holds at all 11 frozen cutoffs. This remains finite evidence only.

## 6. Next theorem problem

The remaining analytic task is no longer merely “show squareclasses rarely collide.” It is to count repeated solutions of

\[
D-C=h\alpha r^2,
\qquad
D+C=h\beta u^2,
\]

for the same coprime squarefree pair `(alpha,beta)`, **subject to the two already-integral face conditions that define a raw Stage14 edge** and the physical bound `d<=B`.

That is a substantially more rigid correlation problem than equality of arbitrary squareclasses. Stage14-t21 should attack `Q_split(B)` directly, using the raw-pair Pythagorean parametrization and the split-prime support.

## Locked boundary

```text
STAGE14_T20=COMPLETE_RAW_EDGE_COLLISION_CORRECTION_AND_COPRIME_FACTOR_REDUCTION
ASYMPTOTIC_COLLISION_POPULATION=RAW_PAIR_EDGES
RAW_EDGE_IDENTITY=E(B)=N2(B)+3T(B)
TRIVIAL_CLASS_EDGE_COUNT=3T(B)
NINE_T_SQUARED_LE_Q_EDGE=true
Q_EDGE_O_B_SUFFICIENT_FOR_T_O_SQRT_B=true
T19_EXACTLY_TWO_COLLISION_ASYMPTOTIC_STATEMENT_SUPERSEDED=true
MISSING_FACE_CLASS_EQUALS_DIFFERENCE_OF_SQUARES_KERNEL=true
COPRIME_FACTORIZATION_M_EQUALS_G2_H2_A_B=true
H_IN_1_2=true
KERNEL_EQUALS_ALPHA_BETA=true
KERNEL_PRIME_SUPPORT_ONLY_2_OR_1MOD4=true
PARTITION_RESOLVED_COLLISION_REDUCTION=true
Q_EDGE_LE_B_O1_Q_SPLIT=true
FINITE_Q_EDGE_EQUALS_Q_SPLIT_EQUALS_356_AT_B2M=true
Q_SPLIT_POWER_SAVING_PROVED=false
Q_EDGE_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t21 attack partition-resolved collision energy Q_split(B) using the raw-pair Pythagorean parametrization
```
