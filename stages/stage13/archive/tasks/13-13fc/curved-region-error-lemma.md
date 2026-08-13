# Stage13-13fc — explicit curved-region and box-error accumulation

> STATUS: `STAGE13_13FC_CURVED_REGION_ERROR_LEMMA`
>
> PURPOSE: close R05 Gate C by replacing the phrases “polylogarithmically many boxes” and “smaller than every fixed negative power of log B” with an explicit global accumulation argument.
>
> INPUTS:
>
> - the zero-mode one-variable Perron/residue expansions from the canonical proof;
> - the phase-independent mixed-correction moment bounds, with Gate B (`13-13fb`) supplying the fully explicit Wiener estimate;
> - the physical cutoff `h(r^2+s^2)<=2B`.
>
> SCOPE: zero angular mode only. Retained nonzero harmonics and their conductor dependence remain Gate D (`13-13fd`).

The theorem statement is not altered. This lemma makes the quantitative passage from uniform core rectangles to the curved physical region independently auditable.

---

## 1. Fixed parameters

Write

\[
\Lambda=\log B.
\]

For sufficiently large `B`, fix

\[
H_0=U=\exp(\Lambda^{1/4}),
\]

\[
\eta=\Lambda^{-8},
\]

and, for the rectangle power-tail estimate,

\[
\varepsilon=\frac1{16}.
\]

For the finite-order logarithmic remainders in the zero-mode one-variable Perron expansions choose once and for all

\[
N=64.
\]

The core is

\[
h\ge H_0,\qquad r\ge U,\qquad s\ge U,
\]

inside

\[
h(r^2+s^2)\le2B.
\]

The wing pieces are

```text
small height:      h < H0
small coordinate:  min(r,s) < U.
```

---

## 2. Uniform zero-mode rectangle interface

For a multiplicative rectangle

\[
\mathcal R(H,R,S):
\quad
H<h\le e^\eta H,\quad
R<r\le e^\eta R,\quad
S<s\le e^\eta S,
\]

the zero-mode factorization and the mixed-correction logarithmic moments give a uniform expansion of the form

\[
\mathcal N_0(\mathcal R)
=
\mathcal M_0(\mathcal R)
+
\mathcal E_{\rm pow}(\mathcal R)
+
\mathcal E_N(\mathcal R).
\]

The leading rectangle term is the common arithmetic scalar times the local archimedean volume and a polynomial of logarithmic degree at most two in the two base variables. The exact coefficient is not needed for the error accumulation in this gate.

The power-tail term satisfies, for one fixed `C_rect` independent of the rectangle,

\[
\mathcal E_{\rm pow}(\mathcal R)
\ll
\Lambda^{C_{\rm rect}}
\left(
H^{3/4+\varepsilon}RS
+
HR^{3/4+\varepsilon}S
+
HRS^{3/4+\varepsilon}
\right).
\]

The finite-order endpoint remainders from the three one-variable Perron expansions satisfy

\[
\boxed{
\mathcal E_N(\mathcal R)
\ll_N
B\Lambda^{2-N}.
}
\]

Here is the uniform reason for the last display. On any core box meeting or lying below the physical cutoff, multiplicative variation of the three coordinates changes

\[
h(r^2+s^2)
\]

by at most `e^{3 eta}`. Therefore

\[
H(R^2+S^2)\ll B.
\]

Since

\[
2RS\le R^2+S^2,
\]

we have

\[
HRS\ll B.
\]

A remainder in the `h` channel contributes at worst

\[
H\Lambda^{-N}\cdot R\Lambda\cdot S\Lambda
\ll
B\Lambda^{2-N}.
\]

A remainder in one base channel costs at most one remaining base logarithm and is smaller. Products of two or three remainder terms are smaller still. The mixed correction does not change this uniformity because Gate B and the logarithmic-moment lemma give absolute summability of all fixed logarithmic shifts.

With `N=64`,

\[
\boxed{
\mathcal E_{64}(\mathcal R)
\ll B\Lambda^{-62}.
}
\]

This is a per-box statement.

---

## 3. Exact logarithmic box count

Partition each positive coordinate multiplicatively by intervals

\[
[e^{j\eta},e^{(j+1)\eta}).
\]

Inside the physical region,

\[
h\le B
\]

because `r^2+s^2>=2`, and

\[
r,s\le\sqrt{2B}<2B.
\]

Thus every relevant coordinate lies in `[1,2B]`.

For `B` sufficiently large,

\[
\log(2B)\le2\Lambda.
\]

The number of mesh intervals required for one coordinate is therefore at most

\[
2+\frac{\log(2B)}{\eta}
\le
2+2\Lambda^9
=
O(\Lambda^9).
\]

Hence the total number of three-dimensional boxes is

\[
\boxed{
N_{\rm box}(B)=O(\Lambda^{27}).
}
\]

This is the exponent that was left implicit in R04.

For the machine-readable contract:

```text
BOX_COUNT=O((log B)^27)
```

No claim in this lemma relies on an unspecified number of boxes.

---

## 4. Accumulation of the finite-order Perron remainders

From §2, each core rectangle has

\[
\mathcal E_{64}(\mathcal R)
\ll
B\Lambda^{-62}.
\]

Summing this crude uniform bound over all

\[
O(\Lambda^{27})
\]

boxes gives

\[
\sum_{\mathcal R}\mathcal E_{64}(\mathcal R)
\ll
B\Lambda^{27-62}.
\]

Therefore

\[
\boxed{
\mathcal E_{\rm finite}
\ll
B\Lambda^{-35}.
}
\]

For the machine-readable contract:

```text
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
```

In particular this is far below the main scale `B Lambda^3`.

More generally, the argument shows that any fixed `N>30+A` would yield an accumulated `O(B Lambda^{-A})` remainder. The choice `N=64` is merely a fixed explicit ledger value.

---

## 5. Accumulation of the rectangle power tails

Take

\[
\varepsilon=\frac1{16}.
\]

Then

\[
\frac14-\varepsilon
=
\frac3{16}.
\]

For the first rectangle power term,

\[
H^{3/4+\varepsilon}RS
=
HRS\cdot H^{-1/4+\varepsilon}.
\]

Using `HRS << B` and `H>=H0` gives

\[
H^{3/4+\varepsilon}RS
\ll
B H_0^{-3/16}.
\]

Similarly the two base-channel terms are bounded by

\[
B U^{-3/16}.
\]

Since

\[
H_0=U=e^{\Lambda^{1/4}},
\]

we obtain per box

\[
\mathcal E_{\rm pow}(\mathcal R)
\ll
B\Lambda^{C_{\rm rect}}
\exp\!\left(-\frac3{16}\Lambda^{1/4}\right).
\]

After all `O(Lambda^27)` boxes,

\[
\boxed{
\mathcal E_{\rm pow,total}
\ll
B\Lambda^{C_{\rm rect}+27}
\exp\!\left(-\frac3{16}\Lambda^{1/4}\right).
}
\]

For every fixed `A>0`,

\[
\Lambda^{C_{\rm rect}+27+A}
\exp\!\left(-\frac3{16}\Lambda^{1/4}\right)
\to0.
\]

Hence

\[
\boxed{
\mathcal E_{\rm pow,total}
=
o_A(B\Lambda^{-A})
\quad\text{for every fixed }A>0.
}
\]

The previously compressed “stretched exponential beats all polylogarithms” step is therefore valid after the actual box exponent `27` is inserted.

For the machine-readable contract:

```text
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
```

---

## 6. Small-height wing

The positive zero-mode summatory estimates imply by partial summation

\[
\sum_{h\le H_0}\frac{a_0(h)}h
\ll
\log H_0.
\]

The two base variables contribute at most two logarithms at the crude positive-majorant level. Hence

\[
\mathcal E_{\rm small\,h}
\ll
B\Lambda^2\log H_0.
\]

Since

\[
\log H_0=\Lambda^{1/4},
\]

we get

\[
\boxed{
\mathcal E_{\rm small\,h}
\ll
B\Lambda^{9/4}.
}
\]

Because `9/4<3`, this is `o(B Lambda^3)`.

---

## 7. Small-coordinate wing

Likewise,

\[
\sum_{r\le U}\frac{b_0(r)}r
\ll
(\log U)^2.
\]

Taking the union of `r<U` and `s<U` only changes the constant. The remaining variables are bounded by the same positive zero-mode majorant, giving

\[
\mathcal E_{\rm small\,coord}
\ll
B\Lambda^2(\log U)^2.
\]

Since

\[
\log U=\Lambda^{1/4},
\]

we obtain

\[
\boxed{
\mathcal E_{\rm small\,coord}
\ll
B\Lambda^{5/2}.
}
\]

Again `5/2<3`.

---

## 8. Mixed-correction logarithmic shifts

Write the global correction as

\[
C_0(\mathbf s)
=
\sum_{u,v,w}
\frac{c_0(u,v,w)}
{u^{s_h}v^{s_r}w^{s_s}}.
\]

Gate B gives absolute convergence in the `5/8` Wiener region, and the canonical logarithmic-moment argument gives, for every fixed `m`,

\[
\sum_{u,v,w}
\frac{|c_0(u,v,w)|(1+\log(uvw))^m}{uvw}
<\infty.
\]

The top rectangle polynomial has logarithmic degree three only after the radial summation. Replacing a main logarithm by one correction logarithm, such as

\[
\log R\mapsto\log R-\log v,
\]

lowers the degree in `Lambda` by at least one. Therefore all correction terms containing a nonconstant logarithmic shift contribute globally at most

\[
\boxed{
\mathcal E_{\rm shift}
\ll
B\Lambda^2.
}
\]

This is below `B Lambda^3`; it is not multiplied by the number of boxes because the correction is convolved globally and its logarithmic moments are summed absolutely before the final geometric Riemann sum.

---

## 9. Boxes meeting the curved boundary

Let

\[
F(h,r,s)=h(r^2+s^2).
\]

Inside one multiplicative box every coordinate changes by at most `e^eta`. Therefore `h` changes by `e^eta`, while `r^2+s^2` changes by at most `e^{2eta}`. Hence `F` changes by at most

\[
e^{3\eta}.
\]

Consequently, if a box intersects

\[
F=2B,
\]

the entire box lies inside the shell

\[
2B e^{-3\eta}
\le
F
\le
2B e^{3\eta}.
\]

The shell has logarithmic thickness `6 eta`.

Now sum the rectangle **main polynomials** over this shell. The zero-mode main measure is homogeneous of degree one in `B`, with logarithmic degree at most three. Equivalently, after the radial change of variables used to derive `J_q`, its cumulative main expression has the form

\[
B\,P_3(\Lambda;\text{bounded angular variables}),
\]

where the coefficients and their first derivatives on each fixed parity/canonical sector are bounded independently of `B`. Replacing `B` by `e^\tau B` with `|\tau|\le3eta` and applying the mean-value theorem therefore changes the cumulative main by

\[
O(\eta B\Lambda^3).
\]

Thus the sum of the main terms of all boundary-intersecting boxes is

\[
O(\eta B\Lambda^3).
\]

Their rectangle remainders are a subset of the already accumulated global remainders from §§4–5. Hence

\[
\boxed{
\mathcal E_{\rm boundary}
\ll
\eta B\Lambda^3
+
B\Lambda^{-35}
+
B\Lambda^{C_{\rm rect}+27}
e^{-(3/16)\Lambda^{1/4}}.
}
\]

Since `eta=Lambda^-8`,

\[
\boxed{
\mathcal E_{\rm boundary}
=
O(B\Lambda^{-5})
+
\text{lower-order ledger}.
}
\]

For the machine-readable contract:

```text
CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger
```

This is the precise meaning of the boundary estimate: the displayed `-5` is the shell main term, while all boxwise analytic remainders have already been accounted for separately and are smaller.

---

## 10. Interior Riemann-sum mesh error

Discard the boundary-intersecting boxes. On every remaining core box the physical indicator is constant.

The rectangle main polynomial, expressed in logarithmic radial variables and the fixed angular coordinate, is piecewise `C^1` on the canonical core sector. Its total first-variation majorant has the same scale as the zero-mode main measure,

\[
O(B\Lambda^3).
\]

A multiplicative mesh `e^eta` is an additive mesh of size `eta` in each logarithmic coordinate. The standard first-order Riemann-sum estimate therefore gives

\[
\mathcal E_{\rm mesh}
\ll
\eta B\Lambda^3.
\]

Substituting `eta=Lambda^-8`,

\[
\boxed{
\mathcal E_{\rm mesh}
=
O(B\Lambda^{-5}).
}
\]

For the machine-readable contract:

```text
MESH_ERROR=O(B(log B)^-5)
```

No extra factor `N_box` is inserted here: the Riemann-sum estimate controls the **sum of local cell variations**, i.e. total variation times the mesh width. Multiplying a worst-case cell error by all boxes would double-count the integration argument.

---

## 11. Gate C zero-mode ledger

With

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
epsilon = 1/16
N = 64
N_box = O((log B)^27)
```

the global zero-mode error ledger is:

| source | global bound |
|---|---|
| small height | `O(B (log B)^(9/4))` |
| small coordinate | `O(B (log B)^(5/2))` |
| mixed-correction log shifts | `O(B (log B)^2)` |
| all finite-order Perron remainders over all boxes | `O(B (log B)^(-35))` |
| all rectangle power tails | `B (log B)^(C_rect+27) exp(-(3/16)(log B)^(1/4))` |
| curved boundary shell | `O(B (log B)^(-5)) + lower-order ledger` |
| interior Riemann mesh | `O(B (log B)^(-5))` |

Every row is

\[
o(B(\log B)^3).
\]

Therefore the zero-mode rectangle-to-curved-region passage is quantitatively closed:

\[
\boxed{
A_q^{(0)}(B)
=
\Theta J_q B(\log B)^3
+
o(B(\log B)^3).
}
\]

This statement remains before Stage12 calibration and therefore does not manufacture directionality from the Stage12 total theorem.

---

## 12. What Gate C does and does not close

Gate C closes the R04/DeepSeek objection that the curved-region proof did not expose:

- the actual number of multiplicative boxes;
- how finite-order Perron errors survive summation over all boxes;
- how the rectangle power saving survives the same summation;
- how the boundary-shell estimate is separated from the analytic rectangle remainders;
- how the Riemann mesh estimate is global rather than a worst-box-times-box-count argument.

It does **not** close the retained nonzero-harmonic family estimate. In particular, it does not justify the old fixed choice `A=48` against an unspecified conductor-growth exponent. That is deliberately deferred to `13-13fd`.

It also does not mutate R04 or the canonical R03 history.

```text
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
BOX_COUNT=O((log B)^27)
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger
MESH_ERROR=O(B(log B)^-5)
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fd
```
