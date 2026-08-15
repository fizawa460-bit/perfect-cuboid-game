# Stage25-50 r501 — parametric positive-power lower candidate

STATUS=PROVED_SUBMITTED_FOR_FRESH_AUDIT
ROLE=DEEP_LOWER_SUBLANE_A
TARGET=Stage19 exactly-two-face plus integral-space primitive canonical population

## 1. Why this lane was opened

The audited Stage24-50 construction proves

\[
N_2(B)\gg \sqrt{\log B}
\]

from the positive-rank quartic `C_17`. That construction is sparse because elliptic multiples have exponential height growth.

A separate primary-source structure exists: Meskhishvili's one-parameter rational nearly-perfect-cuboid formulas (arXiv:1502.02375). The present argument does **not** import the paper as a black-box counting theorem. We copy one formula family, homogenize it, verify the two integral faces and space diagonal algebraically, prove a fixed physical cone, control similarity multiplicity, and isolate the third-face-square exceptions on a genus-seven curve.

The resulting Stage19 lower candidate is

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

This would be the first certified positive-power lower bound if fresh audit passes.

## 2. Homogeneous integer family

Let `m,n` be coprime positive integers and put `t=m/n`. Define homogeneous degree-eight integers

\[
A=16m^2n^2(m^4-9n^4),
\]

\[
B=(m^4-10m^2n^2+9n^4)(m^4+2m^2n^2+9n^4),
\]

\[
C=4mn(m^2+3n^2)(m^4-10m^2n^2+9n^4),
\]

and

\[
D_{AC}=4mn(m^2+3n^2)(m^4-2m^2n^2+9n^4),
\]

\[
D_{BC}=(m^4-n^4)(m^4-81n^4),
\]

\[
D=m^8+46m^4n^4+81n^8.
\]

Direct expansion gives

\[
A^2+C^2=D_{AC}^2,
\qquad
B^2+C^2=D_{BC}^2,
\qquad
A^2+B^2+C^2=D^2.
\]

Thus the raw integer box `(A,B,C)` has two integral face diagonals and integral space diagonal `D`.

These are exactly the first one-parameter rational formulas of Meskhishvili after multiplying by `n^8`; the proof below is repo-native and uses only the displayed homogeneous identities.

## 3. Fixed physical cone and canonical ordering

Restrict to

\[
\boxed{\frac72<t<4.}
\]

All three edges are positive because `t>3`.

For `C-B`, direct factorization in the dehomogenized variable gives

\[
C-B=-(t-3)(t-1)(t+1)(t+3)
\bigl(t^4-4t^3+2t^2-12t+9\bigr).
\]

Let

\[
Q_1(t)=t^4-4t^3+2t^2-12t+9.
\]

Then

\[
Q_1'(t)=4(t-3)(t^2+1)>0\qquad(t>3),
\]

and `Q_1(4)=-7`, hence `Q_1(t)<0` throughout `(7/2,4)`. Therefore `C>B`.

Likewise

\[
A-C=-4t(t^2+3)
\bigl(t^4-4t^3-10t^2+12t+9\bigr).
\]

For `t in (7/2,4)`, the first two terms satisfy `t^4-4t^3=t^3(t-4)<0`, while

\[
-10t^2+12t+9<0
\]

already at `t=7/2` and decreases thereafter. Hence the bracket is negative and `A>C`.

Thus throughout the cone

\[
\boxed{0<B<C<A.}
\]

After primitive reduction, the canonical ordered box is therefore

\[
(a,b,c)=(B/g,C/g,A/g),
\qquad g=\gcd(A,B,C).
\]

## 4. Primitive reduction preserves every required integer diagonal

Because `g` divides each edge, `g^2` divides each of

\[
D_{AC}^2=A^2+C^2,
\quad
D_{BC}^2=B^2+C^2,
\quad
D^2=A^2+B^2+C^2.
\]

Prime-by-prime valuation then gives

\[
g\mid D_{AC},\qquad g\mid D_{BC},\qquad g\mid D.
\]

Hence dividing by `g` produces a primitive integer box with the same two integral faces and integral space diagonal.

No unproved bound on `g` is needed for the lower bound: primitive reduction can only decrease the height.

## 5. The remaining face-square exceptions form a genus-seven curve

The only remaining face is the pair `(A,B)`. Dehomogenizing by `t=m/n`, direct factorization gives

\[
a(t)^2+b(t)^2=P(t),
\]

where

\[
\boxed{
P(t)=t^{16}-16t^{14}+316t^{12}-112t^{10}-3290t^8
-1008t^6+25596t^4-11664t^2+6561.
}
\]

Equivalently,

\[
P(t)=F_-(t)F_+(t)
\]

with

\[
F_\pm(t)=t^8\pm4t^7\mp28t^5+46t^4\mp84t^3\pm108t+81.
\]

The third face is rational exactly when

\[
w^2=P(t)
\]

has a rational point with that `t`.

### Squarefreeness certificate

Modulo `5`, write `u=t^2`. Then

\[
P(t)\equiv Q(t^2)\pmod5,
\]

where

\[
Q(u)=u^8+4u^7+u^6+3u^5+2u^3+u^2+u+1.
\]

The committed audit script verifies the explicit Bezout identity

\[
S(u)Q(u)+T(u)Q'(u)\equiv1\pmod5
\]

for

\[
S=2u^6+2u^5+u^4+2u^3+u+2,
\]

\[
T=u^7-u^6+2u^5+2u^4-u^3-u-1.
\]

Thus `Q` is squarefree over `F_5`. Also `Q(0)=1`, so `P(t)=Q(t^2)` is squarefree modulo `5`, hence squarefree over `Q`.

Therefore the smooth projective model of

\[
w^2=P(t)
\]

is hyperelliptic of genus

\[
\boxed{g=(16-2)/2=7.}
\]

By Faltings' theorem, it has only finitely many rational points. Consequently only finitely many rational parameters `t` in our cone make the third face rational. Removing them leaves asymptotically all parameters in the counting family and produces **exactly two** integral faces.

This use of Faltings is qualitative and potentially ineffective; no effective exceptional threshold is claimed.

## 6. Bounded multiplicity of the parameter map

Primitive reduction forgets the overall scale, so we count similarity classes first.

On the fixed cone, `A` is always the largest edge. The similarity invariant

\[
r(t)=\frac{A}{D}
=\frac{16t^2(t^4-9)}{t^8+46t^4+81}
\]

is determined by the primitive canonical box.

For any fixed rational value `r_0`, the equation `r(t)=r_0` is a nonzero polynomial equation of degree at most `8`:

\[
r_0(t^8+46t^4+81)-16t^2(t^4-9)=0.
\]

Hence each primitive canonical similarity class has at most `8` rational parameters `t` in this lane.

No injectivity claim stronger than this bounded-fiber statement is used.

## 7. Quadratically many reduced rational parameters

Let `T` be large and set

\[
X=\lfloor T/4\rfloor.
\]

For every `n<=X`, choose

\[
m=4n-k,
\qquad 1\le k<n/2,
\qquad \gcd(k,n)=1.
\]

Then

\[
\frac72<\frac mn<4,
\qquad
\gcd(m,n)=\gcd(k,n)=1,
\qquad
m<T.
\]

For `n>2`, exactly half of the reduced residues modulo `n` lie below `n/2`, so there are `phi(n)/2` admissible `k`.

Therefore the number of reduced rational parameters produced with `m,n<=T` is

\[
\frac12\sum_{n\le X}\varphi(n)+O(1)
\asymp X^2
\asymp T^2.
\]

For completeness, the standard estimate

\[
\sum_{n\le X}\varphi(n)=\frac{3}{\pi^2}X^2+O(X\log X)
\]

follows by Möbius inversion from

\[
\sum_{d\le X}\mu(d)\lfloor X/d\rfloor^2
=\frac{6}{\pi^2}X^2+O(X\log X).
\]

Thus this is a genuine two-dimensional rational-height count, not a one-integer subsequence.

## 8. Height conversion

For `m,n<=T`,

\[
D=m^8+46m^4n^4+81n^8
\le128T^8.
\]

Primitive reduction only decreases `D`. Hence every admissible parameter with

\[
T\le (B/128)^{1/8}
\]

produces a primitive Stage19 box of height at most `B`, except for the finite genus-seven exceptional set.

There are `gg T^2` admissible reduced parameters, and each primitive box has at most eight preimages. Therefore

\[
N_2(B)\gg T^2\gg B^{1/4}.
\]

So the candidate theorem is

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

Combining with the audited whole-family upper gives

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

For the Stage25 endpoint ratio, using

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\]

this would sharpen the lower side to

\[
\boxed{
\frac{N_2(B)}{M_1(B)}\gg B^{-7/4}(\log B)^{-1}.
}
\]

The audited upper remains

\[
\frac{N_2(B)}{M_1(B)}\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

## 9. What is and is not claimed

Proposed for fresh audit:

- an explicit rational two-height parameter lane;
- exact integer two-face-plus-space identities after homogenization;
- a fixed canonical cone;
- primitive reduction with no height loss problem;
- finite third-face-square exceptions by a genus-seven hyperelliptic curve;
- bounded similarity multiplicity at most eight;
- `N2(B)>>B^(1/4)`;
- Stage25 ratio lower `N2/M1 >> B^(-7/4)(log B)^(-1)`.

Not claimed:

- `N2(B)>>B^delta` for any `delta>1/4`;
- matching half-power lower;
- an asymptotic for `N2`;
- the true target exponent;
- an effective description of every Faltings exception;
- any perfect-cuboid existence/nonexistence statement;
- novelty of the underlying rational NPC parametrization.

## 10. Primary-source provenance

Primary source for the rational family:

- Mamuka Meskhishvili, *Parametric Solutions for a Nearly-Perfect Cuboid*, arXiv:1502.02375 (2015), first parametrization.

Independent modern structural corroboration:

- Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825, revision dated 2026-03-22; rational face cuboids are parametrized via elliptic-curve data and infinitely many similarity classes are proved.

Neither paper is used as a substitute for the Stage19 primitive/canonical/exactly-two/height adapter above.

```text
SUBLANE=Stage25-r501
BREAKTHROUGH_CANDIDATE=true
POSITIVE_POWER_LOWER_BOUND_CANDIDATE=true
CANDIDATE_LOWER=N2(B)>>B^(1/4)
CANDIDATE_STAGE25_RATIO_LOWER=N2/M1>>B^(-7/4)(log B)^(-1)
THIRD_FACE_EXCEPTION_CURVE_GENUS=7
THIRD_FACE_EXCEPTION_SET_FINITE_BY_FALTINGS=true
PARAMETER_FIBER_BOUND=8
HEIGHT_DEGREE=8
PARAMETER_COUNT_DEGREE=2
FINITE_DATA_USED_AS_PROOF=false
FRESH_AUDIT_REQUIRED=true
```
