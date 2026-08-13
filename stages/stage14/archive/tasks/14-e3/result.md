# Stage14-e3 — total ambient growth via a toric anticanonical model

> STATUS: `STAGE14_E3_COMPLETE_TOTAL_GROWTH_ORDER`
>
> RESULT: `E_2(B) \asymp B (log B)^5`
>
> INPUT: Stage14-e1 bijection, Stage14-e2 finite census, Batyrev–Tschinkel toric Manin theorem, Huang toric adelic equidistribution
>
> IMPORTANT: this stage proves the **order**, not an exactly-two leading constant.

## 1. Target

Stage14-e counts primitive integer triples `(e,x,y)` with `x<y`,

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
\gcd(e,x,y)=1,
\]

under

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B.
\]

There is no rational/integer condition on `D_R`.

The raw ambient population allows `x^2+y^2` to be square. The exactly-two ambient population counted by `E_2(B)` excludes that third-face-square locus.

Stage14-e2 observed finite stability near `B(log B)^3`. Stage14-e3 determines the actual theorem-level growth order independently of that fit.

## 2. Rational torus coordinates for one Pythagorean slope

Let

\[
t=\frac Xe>0,
\qquad
h=\frac ue>0.
\]

The face equation gives

\[
h^2-t^2=1.
\]

Define

\[
q=h+t.
\]

Then

\[
q^{-1}=h-t,
\]

and hence

\[
\boxed{
 t=\frac{q-q^{-1}}2,
 \qquad
 h=\frac{q+q^{-1}}2.
}
\]

For positive `t,h`, one has `q>1`. Conversely every rational `q>1` gives a positive rational Pythagorean slope.

Thus a raw two-face shape is represented by

\[
(q_1,q_2)\in(\mathbf Q_{>1})^2,
\]

with

\[
t_i=\frac{q_i-q_i^{-1}}2,
\qquad t_1<t_2.
\]

The positive real branch is one-to-one: the other algebraic root of the quadratic relation is `-q_i^{-1}<0` and is excluded by `q_i>1`.

## 3. Projective primitive coordinates recover the Stage14-e object

Map the rational torus to projective shape coordinates by

\[
(q_1,q_2)\longmapsto[1:t_1:t_2].
\]

Write this rational projective point in its unique primitive positive integer representative

\[
[e:x:y].
\]

Then

\[
t_1=x/e,
\qquad
t_2=y/e.
\]

Because each `t_i` is a rational Pythagorean slope, multiplying its rational hypotenuse by the common denominator `e` gives integral face hypotenuses. Therefore

\[
e^2+x^2=\square,
\qquad
e^2+y^2=\square.
\]

Conversely every primitive raw Stage14-e object gives these two slopes and hence unique positive `q_1,q_2`.

So, after the real inequalities `q_i>1` and `t_1<t_2` are imposed, raw Stage14-e objects are exactly rational points of this torus model.

## 4. Compactification and the three anticanonical sections

Compactify the torus by

\[
X_0=\mathbf P^1\times\mathbf P^1.
\]

Use homogeneous coordinates

\[
q_1=[u_1:v_1],
\qquad
q_2=[u_2:v_2].
\]

Then

\[
t_1=\frac{u_1^2-v_1^2}{2u_1v_1},
\qquad
t_2=\frac{u_2^2-v_2^2}{2u_2v_2}.
\]

The projective map `[1:t_1:t_2]` is represented by the three bidegree `(2,2)` sections

\[
\begin{aligned}
s_0&=4u_1v_1u_2v_2,\\
s_1&=2(u_1^2-v_1^2)u_2v_2,\\
s_2&=2(u_2^2-v_2^2)u_1v_1.
\end{aligned}
\]

Hence they lie in

\[
\mathcal O_{\mathbf P^1\times\mathbf P^1}(2,2)
=-K_{X_0}.
\]

Their common base locus is exactly the four torus-fixed corners where one boundary component from each `P^1` factor meets. Locally the base ideal has the form `(x,y)`, so each corner is a simple base point.

Blow up the four corners:

\[
\pi:Y=\operatorname{Bl}_{4}(\mathbf P^1\times\mathbf P^1)\to X_0.
\]

Let `H_1,H_2` denote the two ruling classes and `E_1,...,E_4` the exceptional divisors. The resolved linear system has line bundle

\[
L=2H_1+2H_2-\sum_{j=1}^4E_j.
\]

But

\[
K_Y=-2H_1-2H_2+\sum_{j=1}^4E_j,
\]

so

\[
\boxed{L=-K_Y.}
\]

The blowups are torus-equivariant because all four centers are torus-fixed. Thus `Y` is a smooth projective split toric surface.

## 5. Picard rank and the logarithmic exponent

The starting surface has

\[
\rho(\mathbf P^1\times\mathbf P^1)=2.
\]

Each point blowup increases the Picard rank by one. Hence

\[
\boxed{\rho(Y)=2+4=6.}
\]

For anticanonical height on the open torus of a smooth projective toric variety, the Batyrev–Tschinkel Manin theorem gives logarithmic power

\[
\rho(Y)-1=5.
\]

Thus for a standard toric anticanonical height `H_T`,

\[
N_T(B)\asymp B(\log B)^5,
\]

and in fact the cited theorem gives a full asymptotic for its standard setting.

Stage14-e3 only needs the order statement.

## 6. Comparison with the physical real height

The resolved morphism

\[
Y\to\mathbf P^2,
\qquad
(q_1,q_2)\mapsto[1:t_1:t_2],
\]

satisfies

\[
\phi^*\mathcal O_{\mathbf P^2}(1)=L=-K_Y.
\]

For a primitive representative `[e:x:y]`, the usual max projective height is

\[
H_{\max}=\max(e,x,y).
\]

The Stage14-e height satisfies the uniform comparison

\[
H_{\max}\le D_{\mathbf R}\le\sqrt3\,H_{\max}.
\]

Moreover `H_max` and any fixed standard toric anticanonical height `H_T` are heights attached to the same line bundle `-K_Y`; fixed adelic metrics on the same line bundle differ by bounded multiplicative factors.

Therefore there exist constants `c_1,c_2>0` such that on the rational torus

\[
c_1H_T\le D_{\mathbf R}\le c_2H_T.
\]

Consequently replacing the standard toric height by the physical Euclidean height cannot change the power of `B` or `log B`.

## 7. Raw ambient upper and lower bounds

Every raw Stage14-e object is a torus rational point, so Batyrev–Tschinkel plus height comparison gives

\[
E_{\rm raw}(B)\ll B(\log B)^5.
\]

For a lower bound, choose any nonempty real open box inside

\[
q_1>1,
\qquad q_2>1,
\qquad t_1<t_2.
\]

Huang's adelic equidistribution theorem gives a positive asymptotic proportion of toric rational points in such a real neighbourhood under `H_T`. Height comparison then yields

\[
E_{\rm raw}(B)\gg B(\log B)^5.
\]

Hence

\[
\boxed{E_{\rm raw}(B)\asymp B(\log B)^5.}
\]

No exact raw leading constant in the physical Euclidean metric is frozen here.

## 8. Exactly-two lower bound without assuming Euler-brick sparsity

The nontrivial issue is that

\[
E_2(B)\le E_{\rm raw}(B),
\]

and it is not enough to say informally that the third-face-square locus “should be thin”. A thin set is not automatically negligible for every height problem.

Instead impose a fixed 5-adic open condition.

Let

\[
q_1\equiv2\pmod5,
\qquad
q_2\equiv3\pmod5.
\]

Modulo 5,

\[
2^{-1}=3,
\qquad3^{-1}=2,
\]

so

\[
t_1=\frac{q_1-q_1^{-1}}2\equiv2,
\qquad
t_2=\frac{q_2-q_2^{-1}}2\equiv3.
\]

The individual face conditions remain Pythagorean, while

\[
t_1^2+t_2^2\equiv4+9\equiv3\pmod5.
\]

The quadratic residues modulo 5 are `0,1,4`, so `3` is a nonsquare unit. Therefore `t_1^2+t_2^2` is not a square in `Q_5`, hence not a square in `Q`.

If the third face were integral, then

\[
x^2+y^2=z^2
\]

would imply

\[
t_1^2+t_2^2=(z/e)^2
\]

in `Q`, contradiction.

Thus every rational point in this 5-adic neighbourhood belongs to the exactly-two ambient population.

Take simultaneously a nonempty real open neighbourhood inside the desired positive ordered chamber. The product is a nonempty adelic neighbourhood with positive Tamagawa measure. Huang's equidistribution theorem therefore supplies

\[
E_2(B)\gg B(\log B)^5.
\]

Combining with the raw upper bound gives the e3 theorem

\[
\boxed{
E_2(B)\asymp B(\log B)^5.
}
\]

## 9. What happened to the e2 `B(log B)^3` fit?

It is rejected as the asymptotic order.

The e2 values through `10^6` showed

\[
E_2(B)/(B(\log B)^3)
\]

nearly flat. The toric compactification gives a structural logarithmic exponent five, so that finite stability is now classified as pre-asymptotic behaviour.

This is exactly why the e-track requires literature/theorem checks before promoting a finite fit.

Stage14-e3 does not attempt to fit the crossover scale or the lower logarithmic terms.

## 10. External theorem boundary

Repository-local proof obligations completed here:

```text
positive Pythagorean slope <-> q in Q_{>1}
raw two-face object <-> ordered positive real torus branch
homogeneous bidegree-(2,2) map written explicitly
four simple torus-fixed base points identified
four-point blowup resolved
L = 2H1+2H2-sum(Ej) = -K_Y
Y smooth projective split toric
rho(Y)=6
physical D_R height comparable to anticanonical height
explicit p=5 exactly-two blocker
```

External theorem inputs:

```text
Batyrev–Tschinkel: anticanonical Manin asymptotic for smooth projective toric varieties
Huang: Manin–Peyre equidistribution / asymptotics in adelic neighbourhoods for smooth projective split toric varieties over Q
```

Stage14-e3 does not reprove those general toric theorems.

## 11. Literature classification

The 2019 common-side Pythagorean paper is adjacent and reusable for fixed-leg arithmetic. The toric theorems are reusable theorem-level inputs. No source found in the current search states the exact Stage14-e cuboid-language theorem with this real Euclidean height and exactly-two filter.

This is not a novelty certificate.

## 12. Locked conclusion

```text
STAGE14_E3=COMPLETE_TOTAL_GROWTH_ORDER
TORIC_MODEL=P1xP1_BLOWUP_AT_FOUR_TORUS_FIXED_CORNERS
ANTICANONICAL_HEIGHT_IDENTIFICATION=true
PICARD_RANK=6
TORIC_LOG_POWER=5
RAW_AMBIENT_ORDER=B_LOG5
EXACTLY_TWO_5ADIC_BLOCKER=p5_q1eq2_q2eq3
EXACTLY_TWO_TOTAL_ORDER=B_LOG5
E2_B_LOG3_FINITE_CANDIDATE=REJECTED_AS_ASYMPTOTIC_ORDER
EXACT_LEADING_CONSTANT_PROVED=false
DIRECTIONAL_ASYMPTOTIC_PROVED=false
NOVELTY_BY_SEARCH_ABSENCE=false
NEXT_E_TASK=Stage14-e4 directionwise ambient asymptotic via real-chamber toric measures
```
