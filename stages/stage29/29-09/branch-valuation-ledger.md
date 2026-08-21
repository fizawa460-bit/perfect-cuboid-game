# Stage29-09 — branch valuation transition ledger

```text
ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
RECEIVER=R29-KUM-LOC2
STATUS=SUBMISSION_PENDING_AUDIT
ODD_PRIMES=EXACT
REAL_PLACE=NO_POSITIVE_CHAMBER_OBSTRUCTION
P2=BAD_PRIME_SEPARATE
```

Fix an odd prime `p`. On a primitive `P^2(Q_p)` base point, at least one of the seven branch forms is a unit. A `Q_p` lift to the full sign cover exists exactly when all seven branch values have one common class in `Q_p^*/Q_p^{*2}`. For odd `p`, a unit squareclass is determined by its Legendre symbol and every vanishing branch value must have even valuation.

Let a reduction point be eligible as in `seven-form-local-density.md`, and let `k` be the number of branch lines through it. Conditional on that reduction cylinder, define `q_k(p)` as the probability that the vanishing forms continue to the same `Q_p` squareclass as the nonvanishing unit forms.

## 1. Smooth branch: one vanishing form

Write the vanishing parameter as `L=pT`. To have the unit squareclass `c`, `v_p(T)` must be odd and the first unit of `T` must have character `c`. Hence

\[
\begin{aligned}
q_1(p)
&=\frac12(1-p^{-1})\sum_{j\ge0}p^{-(2j+1)}\\
&=\boxed{\frac1{2(p+1)}}.
\end{aligned}
\]

## 2. Ordinary double point: two transverse branches

The two local branch parameters are independent. At each of the three eligible double points their unit multipliers are squares, so

\[
\boxed{q_2(p)=q_1(p)^2=\frac1{4(p+1)^2}}.
\]

This case occurs only when `p=1 mod 8`, because otherwise `A_2(p)=0`.

## 3. Triple point: exact correlated transition

At every eligible triple point the three vanishing branch forms can be chosen as

\[
r,\ s,\ r+s.
\]

The third condition is therefore not independent. Put `epsilon=chi(-1)`. Let `nu` be the Haar measure in `Z_p^2` for which `R,S,R+S` all have even valuations and a prescribed common unit character. The number of residue pairs `u,v in F_p^*` with

\[
\chi(u)=\chi(v)=\chi(u+v)=c
\]

is

\[
N_c=\frac{(p-1)(p-4-\epsilon)}8,
\]

independent of the choice `c=+1` or `-1`. The residue class `u+v=0` contributes only for `epsilon=1`; the one-zero residue classes use the single-branch transition; and the both-zero class recurs after division by `p^2`. Thus

\[
\nu=
\frac{N_c}{p^2}
+\frac{(p-1)(1+\epsilon)}{4p^2}q_1
+\frac{p-1}{p^2}q_1
+p^{-4}\nu.
\]

At a triple reduction we already have `r=pR,s=pS`, so the desired valuations of `R,S,R+S` are odd and

\[
q_3(p)=p^{-2}\nu.
\]

Solving the recurrence gives

\[
\boxed{
q_3(p)=
\frac{p^2-(3+\epsilon)p+1}
{8(p+1)^2(p^2+1)}.
}
\]

In particular

```text
p=1 mod 4 : numerator = p^2-4p+1
p=3 mod 4 : numerator = (p-1)^2
```

and `q_3` is not `q_1^3`. This is an exact branch-correlation datum genuinely belonging to the joint endpoint architecture.

## 4. Exact odd-prime Q_p density

Every `F_p` projective residue cylinder has normalized Haar mass `1/(p^2+p+1)`. Therefore, with the exact `A_k(p)` from the companion local-density note,

\[
\boxed{
\Delta_p=
\frac{A_0(p)+A_1(p)q_1(p)+A_2(p)q_2(p)+A_3(p)q_3(p)}
{p^2+p+1}.
}
\]

This is the exact normalized `P^2(Q_p)` Haar density of base points whose seven branch values lie in one common `Q_p` squareclass for every odd prime `p`.

Since `A_0=p^2/64+O(p)` and the branch corrections are lower order,

\[
\Delta_p=\frac1{64}+O(1/p).
\]

This constant leading density is **not** an Euler-product factor on the Stage19/20 physical populations. A global application first needs the rational-height/physical-height equidistribution adapter specified in the route contract.

## 5. Real place

On the physical chamber `x,y,z>0`, all seven forms are positive. Hence the real squareclass condition contributes no local obstruction to the physical endpoint chamber.

```text
R29-KUM-LOC2-INFINITY=DISCHARGED_NO_POSITIVE_CHAMBER_OBSTRUCTION
```

## 6. The prime 2 is genuinely exceptional

The odd-prime ledger does not transfer to `p=2`: the seven-line arrangement collapses modulo 2 and `Q_2^*/Q_2^{*2}` needs valuation parity plus the odd unit modulo 8.

There is nevertheless no blanket 2-adic obstruction. The classical Euler brick

```text
(a,b,c)=(44,117,240)
```

has all three face sums square and

\[
a^2+b^2+c^2=73225\equiv1\pmod8,
\]

so the space sum is a square in `Q_2`. Thus its squared-edge base gives an explicit `Q_2` lift to the full endpoint sign cover, even though `73225` is not a square in `Q`.

The exact normalized 2-adic density/state automaton is left as a bounded bad-prime receiver rather than guessed from odd-prime formulas.

```text
R29-KUM-LOC2-ODD=DISCHARGED_CANDIDATE_EXACT_VALUATION_LEDGER
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
R29-KUM-LOC2=PARTIAL_DISCHARGE_ODD_PRIMES_AND_INFINITY_DONE_P2_OPEN
JOINT_TRIPLE_BRANCH_CORRELATION_EXACT=true
INDEPENDENT_BRANCH_PRODUCT_ASSUMED=false
AUDIT_REQUIRED=true
```
