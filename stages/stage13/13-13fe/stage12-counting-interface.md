# Stage13-13fe — complete Stage12 R09 counting and factor-two interface

> STATUS: `STAGE13_13FE_STAGE12_COUNTING_INTERFACE`
>
> PURPOSE: close R05 Gate E by copying the exact frozen Stage12 counting object, orientation convention, constant normalization and the exact Stage13 projection fiber into one review-facing interface.
>
> STAGE12_BUNDLE: `PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09`
>
> STAGE12_CONTENT_SHA256: `0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848`
>
> STAGE12_REOPENED: `false`

This gate introduces no new analytic theorem. It removes an exposition gap in R04: a reader should not have to infer what Stage12 means by `C_prim(B)`, why it is oriented, what `kappa` denotes, or why the Stage12-to-Stage13 projection has fiber size exactly two.

---

## 1. Frozen Stage12 parameter object

For positive integers `h,r,s`, Stage12 sets

\[
p=hrs,
\qquad
c=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\]

with

\[
1\le r<s,
\qquad
(r,s)=1.
\]

The admissible parameter set is

\[
\boxed{
\mathcal D_B
=
\left\{(h,r,s)\in\mathbf N^3:
1\le r<s,
(r,s)=1,
h(r^2+s^2)\le2B,
h(r^2+s^2)\equiv0\pmod2
\right\}.
}
\]

Since

\[
d=\frac{h(r^2+s^2)}2,
\]

the Stage12 cutoff in this definition is exactly `d<=B`.

The parity condition means:

- for odd--odd `(r,s)`, no additional parity restriction is imposed on `h`;
- for opposite parity `(r,s)`, `h` is even.

Because `(r,s)=1`, there is no both-even branch.

---

## 2. Frozen multiplicity and raw count

For a prime `q`, let `v_q(n)` denote the `q`-adic valuation and define

\[
\boxed{
G(n)
=
\prod_{\substack{q\mid n\\q\equiv1\pmod4}}
(2v_q(n)+1).
}
\]

The Stage12 raw multiplicity is exactly

\[
G(hrs)-1.
\]

Hence the raw oriented count is

\[
\boxed{
C_{\rm raw}(B)
=
\sum_{(h,r,s)\in\mathcal D_B}
\bigl(G(hrs)-1\bigr).
}
\]

The `-1` is part of the frozen counting convention. It is not replaced by another representation convention in Stage13.

---

## 3. What “oriented” means in Stage12

The Stage12 count is oriented in three simultaneous senses.

1. The outer Pythagorean parameter pair obeys `r<s`; the exchange `r<->s` is not counted again.
2. The construction retains a **distinguished integral face** and its construction direction.
3. Stage12 does **not** quotient by all permutations of the three cuboid edges.

Repeated-side contribution was proved identically zero in the frozen Stage12 chain, so there is no main-term tie boundary to repair when later sorting the three edges canonically.

Therefore the statement

\[
C_{\rm prim}(B)
\neq
\text{canonical exactly-one count}
\]

must be respected at the interface. Stage12 never supplied a canonical directional theorem.

---

## 4. Exact primitive definition

Classify every raw object by its common integer scale. Stage12 has the exact content decomposition

\[
C_{\rm raw}(B)
=
\sum_{k\le B}
C_{\rm prim}(\lfloor B/k\rfloor).
\]

Möbius inversion therefore defines

\[
\boxed{
C_{\rm prim}(B)
=
\sum_{k\le B}
\mu(k)
C_{\rm raw}(\lfloor B/k\rfloor).
}
\]

This is an exact counting identity, not an asymptotic approximation.

After passing to actual cuboid edge lengths, removing the common integer scale is exactly the Stage13 condition

\[
\gcd(a,b,c)=1.
\]

Sorting the three edges and exchanging the two legs of the distinguished face preserve this gcd. Thus the primitive definitions match across the bridge.

---

## 5. Frozen Stage12 theorem

R09 freezes only

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
}
\]

The theorem scope is the primitive oriented distinguished-face record count defined above.

It does not assert:

- a canonical count asymptotic;
- a directional category asymptotic;
- an exactly-one-face asymptotic;
- perfect-cuboid existence or nonexistence.

---

## 6. Exact definition of `kappa`

For `q congruent 1 mod 4`, define

\[
F_q(1)=\frac{q^2+6q+1}{q^2-1}.
\]

The frozen Stage12 constant is

\[
\boxed{
\begin{aligned}
\kappa
:={}&
\left(\frac\pi4\right)^3
\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}
(1-q^{-1})^6.
\end{aligned}
}
\]

The normalized local factors are `1+O(l^-2)`, so the product is absolutely convergent.

Stage12 also defines

\[
\boxed{
\begin{aligned}
\eta
:={}&
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2\\
&\times
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\end{aligned}
}
\]

Prime-by-prime comparison gives

\[
\frac{\eta_p}{\kappa_p}=(1-p^{-2})^{-1},
\qquad
\frac{\eta_q}{\kappa_q}=(1-q^{-2})^{-1},
\]

while the front-factor ratio is `8/pi`. Since

\[
\prod_{\ell\ \mathrm{odd}}(1-\ell^{-2})^{-1}
=\frac{\pi^2}{8},
\]

one obtains the exact frozen identity

\[
\boxed{\eta=\pi\kappa.}
\]

This is the only relation between `eta` and `kappa` used by Stage13.

---

## 7. Stage12 front-factor/orientation ledger

The frozen Stage12 residue calculation has:

```text
fixed-height residue normalization     B/pi
parity-weighted rectangle residue      C_lambda^(0)=8 eta/pi^2
full-quadrant radial cubic integral    pi/48
outer orientation r<s                  1/2
```

Thus

\[
\frac B\pi
\cdot
\frac12
\cdot
\frac\pi{48}
\cdot
\frac{8\eta}{\pi^2}
(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3
=
\frac{\kappa}{12\pi}B(\log B)^3.
\]

This `1/2` is the Stage12 outer-parameter orientation `r<s`. It must not be confused with the separate Stage13 projection fiber below.

---

## 8. Exact object map to Stage13

A Stage12 oriented record contains:

1. a distinguished integral face with ordered legs `(x,y)` and face diagonal `P`,
   \[
   x^2+y^2=P^2;
   \]
2. a complementary edge `z` with
   \[
   P^2+z^2=d^2;
   \]
3. the unique supported outer `(r,s)` record under the Stage12 `r<s` convention.

The Stage13 projection is:

1. forget the order of the distinguished face legs `(x,y)`;
2. sort the three positive edges into
   \[
   0<a<b<c;
   \]
3. retain the identity of the canonical face containing `{x,y}`. Call that face
   \[
   q\in\{ab,ac,bc\}.
   \]

Let

\[
C^{\rm proj}_{\rm prim,q}(B)
\]

be the number of Stage12 primitive oriented records whose distinguished face projects to canonical category `q`.

The space diagonal is unchanged by sorting, so the cutoff remains exactly `d<=B`.

---

## 9. Exact factor-two fiber

Fix a primitive canonical raw incidence counted by `A_q(B)`. Thus the cuboid is canonically sorted and face `q` has an integral diagonal, with overlaps with other integral faces allowed.

For that **fixed distinguished incidence**, Stage12 has exactly two preimages:

\[
(x,y)
\qquad\text{and}\qquad
(y,x),
\]

the two orders of the two legs of the distinguished integral face.

There is no further factor because:

- the complementary Pythagorean triple `(P,z,d)` has one supported outer `r<s` parameter record;
- Stage12 already quotients the outer exchange by imposing `r<s`;
- sorting the three physical edges does not create a new primitive or cutoff multiplicity;
- repeated-side contribution is zero, so there is no tie fiber;
- OE and EE parity branches preserve the same two-element leg-order fiber, so there is no extra 2-adic projection factor.

Therefore, for every `B` and every category `q`,

\[
\boxed{
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B).
}
\]

Summing the three distinguished-face categories gives the exact total identity

\[
\boxed{
C_{\rm prim}(B)
=
2\bigl(A_{ab}(B)+A_{ac}(B)+A_{bc}(B)\bigr).
}
\]

This factor is finite and exact. It is neither fitted from data nor obtained asymptotically.

---

## 10. Why overlaps do not change the factor two

`A_q` is a **raw incidence** count: the face `q` remains distinguished even if another face is also integral.

Hence:

- an exactly-two-face cuboid contributes two canonical raw incidences and therefore four Stage12 oriented records;
- an exactly-three-face cuboid contributes three canonical raw incidences and therefore six Stage12 oriented records.

So multi-face objects do not change the fiber size of a single distinguished incidence. This is why the categorywise identity in §9 remains exact before any overlap subtraction.

No assumption about nonexistence of perfect cuboids enters this argument.

---

## 11. Finite checksum

At `B=100000`, the retained bridge fixture is

```text
Stage12 projected = (168424, 86472, 81520)
Stage13 raw A_q    = ( 84212, 43236, 40760)
```

and direction by direction

```text
168424 = 2*84212
 86472 = 2*43236
 81520 = 2*40760.
```

The totals satisfy

```text
336416 = 2*168208.
```

This finite checksum is reproducibility evidence only. The proof of the factor two is the object-level fiber argument above.

---

## 12. Exact division of responsibility

### Frozen Stage12 supplies

- the definition of `D_B`, `G`, `C_raw`, and `C_prim`;
- its primitive/oriented convention;
- exact compatibility of its cutoff with `d<=B`;
- the Euler-product definition of `kappa` and `eta=pi*kappa`;
- the total theorem
  \[
  C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3.
  \]

### Stage13 supplies

- canonical sorting and face labels `ab,ac,bc`;
- the exact two-element projection fiber;
- categorywise chamber constants and raw asymptotics;
- pair/triple overlap lower-order estimates;
- the exactly-one transfer.

In particular Stage13 does **not** retroactively claim that Stage12 proved directionality.

---

## 13. Gate E locks

```text
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE12_R09_BUNDLE=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
STAGE12_R09_CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_CUTOFF=d<=B
STAGE12_THEOREM=C_prim(B)~kappa/(12*pi)B(log B)^3
KAPPA_EULER_PRODUCT_EXPLICIT=true
ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
PROJECTION_PARITY_STRATIFIED=true
EXTRA_2ADIC_PROJECTION_FACTOR=false
MULTI_FACE_FACTOR_TWO_EXACT=true
C_PRIM_Q_PROJ=2*A_q
C_PRIM_TOTAL=2*sum_q_A_q
STAGE12_REOPENED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13ff
```

Gate E closes the R04/DeepSeek objection that the Stage12 object and factor-two interface were not fully stated inside the review-facing proof. Gate F remains responsible for the exact external Hecke/Dirichlet/Vaaler theorem contracts.