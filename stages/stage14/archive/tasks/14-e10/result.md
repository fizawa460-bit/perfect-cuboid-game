# Stage14-e10 — adelic six-state law, residue completion sieve, and thin-cover log saving

> STATUS: `STAGE14_E10_COMPLETE_ADELIC_STATE_LAW_LOCAL_SIEVE_AND_THIN_COVER_LOG_SAVING`
>
> INPUT: e6 physical Tamagawa shells + e8 Euler-brick K3 double cover + e9 exact `(g,u,v)` inverse.
>
> PURPOSE: turn e9's finite prime-state tables into exact limiting laws, strengthen the third-face-square residue sieve, and record the quantitative thin-cover theorem now available from Huang v3.

## 1. Frozen ambient coordinates

For a primitive two-face ambient tuple

\[
(e,x,y),\qquad x<y,
\]

e9 defines

\[
u=\gcd(e,x),\qquad v=\gcd(e,y),\qquad g=\frac e{uv},
\]

and reconstructs the two primitive shared-leg denominators as

\[
S_1=gv,\qquad S_2=gu,\qquad \operatorname{lcm}(S_1,S_2)=e.
\]

On the e3 torus write

\[
q_i\in\mathbf Q^\times,
\qquad
 t_i=\frac{q_i-q_i^{-1}}2,
\]

so that the physical shape is `[1:t1:t2]`.

For a prime `p` put

\[
a=v_p(S_1),\qquad b=v_p(S_2).
\]

Then the e9 states are exactly

```text
none : a=b=0
G    : a=b>0
U    : b>a=0
V    : a>b=0
GU   : b>a>0
GV   : a>b>0
```

and no other support state occurs.

## 2. State coordinates at odd primes

Fix an odd prime `p`.  Because `2` is a p-adic unit,

\[
v_p(t(q))=-|v_p(q)|
\]

whenever `v_p(q) != 0`, while `t(q)` is p-integral on the unit shell.  Therefore

\[
\boxed{a=|v_p(q_1)|,\qquad b=|v_p(q_2)|.}
\]

E6 computes the local physical height shell measure.  Put

\[
c=1-p^{-1}.
\]

In one variable, valuation level `0` has multiplicative-Haar mass `c`, while every positive absolute level `k>=1` has mass `2c`.  In two variables the height weight is

\[
p^{-\max(a,b)}.
\]

The unregularized total local integral is

\[
J_p=1+\frac6p+\frac1{p^2}
=\frac{D_p}{p^2},
\qquad
\boxed{D_p=p^2+6p+1}.
\]

The common Peyre convergence factor cancels when a state is normalized inside the local probability space.

### 2.1 none

The mass is simply

\[
c^2=\frac{(p-1)^2}{p^2},
\]

hence

\[
\boxed{\mu_p(\mathrm{none})=\frac{(p-1)^2}{D_p}.}
\]

### 2.2 G

At each `k>=1`, both coordinates have absolute valuation `k`; there are four sign choices.  Thus

\[
4c^2\sum_{k\ge1}p^{-k}
=\frac{4(p-1)}{p^2},
\]

so

\[
\boxed{\mu_p(G)=\frac{4(p-1)}{D_p}.}
\]

### 2.3 U and V

For `U`, the first coordinate is on level zero and the second on a positive level.  Hence

\[
2c^2\sum_{k\ge1}p^{-k}
=\frac{2(p-1)}{p^2},
\]

and by symmetry

\[
\boxed{\mu_p(U)=\mu_p(V)=\frac{2(p-1)}{D_p}.}
\]

### 2.4 GU and GV

For `GU`, sum over `1<=a<b`.  The four sign choices give

\[
4c^2\sum_{b\ge2}(b-1)p^{-b}
=\frac4{p^2}.
\]

Therefore

\[
\boxed{\mu_p(GU)=\mu_p(GV)=\frac4{D_p}.}
\]

The six expressions sum to one:

\[
(p-1)^2+8(p-1)+8=p^2+6p+1=D_p.
\]

Thus for every odd prime,

\[
\boxed{
(\mu_{none},\mu_G,\mu_U,\mu_V,\mu_{GU},\mu_{GV})
=\frac1{D_p}
\bigl((p-1)^2,4(p-1),2(p-1),2(p-1),4,4\bigr).
}
\]

## 3. The physical 2-adic law

E6 already records the exceptional physical 2-adic levels:

```text
level 0 : mass 1/2
level 1 : mass 0
level k>=2 : mass 1
```

and total unregularized integral

\[
J_2=\frac94.
\]

In terms of the e9 denominator valuations,

\[
a=0\quad\text{if }v_2(q_1)=0,
\]

and otherwise

\[
a=|v_2(q_1)|+1,
\]

with the analogous rule for `b`.  Summing the six regions gives

\[
\boxed{
(\mu_2(\mathrm{none}),\mu_2(G),\mu_2(U),\mu_2(V),\mu_2(GU),\mu_2(GV))
=\frac19(1,2,1,1,2,2).
}
\]

This is a physical-metric law; substituting `p=2` into the odd-prime formula would be wrong, exactly as in e6.

## 4. Fixed finite sets of primes

Huang v3 proves Manin--Peyre equidistribution for the present smooth proper split toric base.  A state such as `G` is an infinite union of valuation shells rather than a single compact-open set, so the proof is made in the correct order:

1. truncate all relevant valuations by `|v_p(q_i)|<=K`;
2. the truncated event is a finite union of p-adic open-closed sets;
3. apply fixed-adelic equidistribution;
4. send `K->infinity`; the discarded Tamagawa tail tends to zero by the convergent local height integral.

Therefore, for every fixed finite prime set `S` and prescribed state `sigma_p` at each `p in S`,

\[
\boxed{
\lim_{B\to\infty}
\frac{\#\{\text{raw ambient points of height }\le B:\sigma_p\text{ for all }p\in S\}}
{E_{\rm raw}(B)}
=
\prod_{p\in S}\mu_p(\sigma_p).
}
\]

The same statement holds after intersecting with any one of the three real direction chambers `a,b,c`: the finite-place Tamagawa factor and the archimedean chamber factor separate.  Hence the limiting local six-state law is direction-independent.

This is the theorem-level upgrade of e9's finite state tables.

## 5. A stronger third-face-square residue blocker

A third-face completion requires

\[
x^2+y^2=z^2
\]

for an integer `z`.

The old e9 blockers used only the entire state `G` at `p=2` and `p=3`.  E10 extracts a blocker at every prime.

### 5.1 p=2

Retain the e9 blocker

\[
B_2:=\{\text{state }G\text{ at }2\}.
\]

Then `e` is even and `x,y` are odd, so

\[
x^2+y^2\equiv2\pmod4,
\]

which is not a square.  Its exact asymptotic ambient mass is

\[
\boxed{\delta_2=\mu_2(G)=\frac29.}
\]

### 5.2 odd p

Inside odd-prime state `G`, both `x` and `y` are p-adic units.  On each fixed common valuation shell, their leading unit residues are independent and uniform in `F_p^*`; the sign of the valuation of each `q_i` only composes this residue with inversion and multiplication by a fixed unit.

Put

\[
r=x/y\in\mathbf F_p^*.
\]

Then

\[
\chi(x^2+y^2)=\chi(r^2+1),
\]

where `chi` is the quadratic character.

The standard quadratic character identity

\[
\sum_{r\in\mathbf F_p}\chi(r^2+1)=-1
\]

implies, after removing `r=0` and the roots of `r^2=-1`, that

\[
\#\{r\in\mathbf F_p^*:r^2+1\text{ is a nonsquare}\}
=\frac{p-\chi_4(p)}2,
\]

where

\[
\chi_4(p)=
\begin{cases}
1,&p\equiv1\pmod4,\\
-1,&p\equiv3\pmod4.
\end{cases}
\]

Hence the conditional nonsquare proportion inside state `G` is

\[
\frac{p-\chi_4(p)}{2(p-1)}.
\]

Define `B_p` to be the subevent of `G` on which `x^2+y^2` is a nonzero quadratic nonsquare modulo `p`.  Its exact local mass is

\[
\boxed{
\delta_p
=\mu_p(G)\frac{p-\chi_4(p)}{2(p-1)}
=\frac{2(p-\chi_4(p))}{p^2+6p+1}
\qquad(p\text{ odd}).
}
\]

Every rational/integer square avoids every `B_p`.

For example,

\[
\delta_3=\frac27,
\quad
\delta_5=\frac17,
\quad
\delta_7=\frac4{23},
\quad
\delta_{11}=\frac6{47},
\quad
\delta_{13}=\frac3{31}.
\]

The deterministic audit verifies the finite-field count for every odd prime through `199`.

## 6. Exact fixed-prime survival products

For any fixed finite prime set `S`, the proportion of ambient points avoiding all e10 blockers tends to

\[
\boxed{
\prod_{p\in S}(1-\delta_p).
}
\]

For `S={2,3}`,

\[
(1-\delta_2)(1-\delta_3)
=\frac79\frac57
=\boxed{\frac59}.
\]

Thus e9's two elementary blockers have exact asymptotic blocked mass

\[
\boxed{\frac49}.
\]

At `B=200000`, e9 observed `884186/1896751=0.466158...`, compared with the limiting `4/9=0.444444...`; the discrepancy is finite/pre-asymptotic and is not used as a theorem input.

For

\[
S=\{2,3,5,7,11,13\},
\]

the exact asymptotic survivor fraction is

\[
\boxed{\frac{31160}{100533}=0.3099479772\ldots},
\]

so these six primes already exclude asymptotically

\[
\boxed{\frac{69373}{100533}=0.6900520227\ldots}
\]

of the raw ambient population from Euler-brick completion.

## 7. Infinite local product and a second zero-density proof

For odd primes,

\[
\delta_p
=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2}).
\]

Therefore

\[
\log(1-\delta_p)=-\frac2p+O(p^{-2}).
\]

Mertens' prime product theorem gives

\[
\boxed{
P(z):=\prod_{p\le z}(1-\delta_p)
\sim\frac{C_{\rm sieve}}{(\log z)^2}
}
\]

for some `C_sieve>0`.

This yields a clean two-limit proof of zero density which is independent of the e4 thin-set argument.  Given `epsilon>0`, choose a fixed `z` with `P(z)<epsilon`.  For this fixed finite set of primes, adelic equidistribution gives ambient survivor density `P(z)`.  Every Euler brick lies in that survivor set.  Hence

\[
\limsup_{B\to\infty}
\frac{R_{\rm EB}(B)}{B(\log B)^5}
\ll P(z)<\epsilon.
\]

Since `epsilon` is arbitrary,

\[
\boxed{R_{\rm EB}(B)=o(B(\log B)^5).}
\]

This proof deliberately takes `B->infinity` with `z` fixed before sending `z->infinity`.

It does **not** justify inserting a growing `z=z(B)` into the fixed-neighbourhood asymptotic.  Therefore the elementary local sieve by itself does not prove

\[
R_{\rm EB}(B)\ll B(\log B)^3
\]

or any other explicit global logarithmic saving.

## 8. Huang v3 gives a genuine quantitative log saving

The e8 compactification gives a double cover of the toric base whose branch divisor is `-2K_Y`.  After normalization and minimal resolution let

\[
f:Z\longrightarrow Y,
\]

where `Z` is the smooth proper geometrically integral Euler-brick K3 surface.  The morphism is dominant and generically finite of degree `2`.

Huang v3, Theorem 1.6(1), applies to a dominant proper generically finite morphism of degree greater than one onto a smooth proper split toric variety with globally generated anticanonical bundle.  It gives

\[
\mathcal N_{\rm loc}(f;B)
=O\left(B(\log B)^{\rho(Y)-1-\iota_f}\right),
\qquad 0<\iota_f<1,
\]

for toric anticanonical height.

Every rational Euler-brick point maps into `f(Z(Q))`, and therefore into the larger adelic image counted by `N_loc`.  Since

\[
\rho(Y)=6,
\]

there exists

\[
\eta_{\rm EB}:=\iota_f\in(0,1)
\]

such that

\[
\boxed{
R_{\rm EB}(B)\ll B(\log B)^{5-\eta_{\rm EB}}.
}
\]

The physical Euclidean anticanonical height and Huang's canonical toric anticanonical height are fixed multiplicatively comparable on the projective base, so replacing one cutoff by the other changes `B` only by an absolute multiplicative constant and preserves the logarithmic saving.

This is the first theorem-level fixed relative logarithmic saving in the e-supplement track.

E10 does **not** evaluate `eta_EB`.  It also does not imply the finite `sqrt(B)` signal is asymptotic.

## 9. What changed relative to e8/e9

E8 and e9 intentionally froze

```text
QUANTITATIVE_RELATIVE_SAVING_PROVED=false
```

because their then-used inputs supplied only thin-set zero density plus the elementary `B^(1+o(1))` multiplicity envelope.

E10 does not mutate those historical stage records.  It adds the new theorem-level input from Huang v3 and upgrades the current downstream state to

```text
QUANTITATIVE_RELATIVE_SAVING_PROVED=true
```

with an unspecified positive logarithmic exponent.

## 10. Locked boundary

```text
STAGE14_E10=COMPLETE_ADELIC_STATE_LAW_LOCAL_SIEVE_AND_THIN_COVER_LOG_SAVING
SIX_STATE_ADELIC_LAW_PROVED=true
FIXED_FINITE_PRIME_PRODUCT_LAW_PROVED=true
DIRECTIONWISE_SAME_LOCAL_LAW_PROVED=true
LOCAL_BLOCKER_MASS_FORMULA_PROVED=true
P2_P3_ASYMPTOTIC_BLOCKED_MASS=4/9
LOCAL_SIEVE_ZERO_DENSITY_REPROVED=true
HUANG_GENERIC_FINITE_LOG_SAVING_APPLIES=true
QUANTITATIVE_RELATIVE_SAVING_PROVED=true
EXPLICIT_ETA_EB_EVALUATED=false
ELEMENTARY_GROWING_PRIME_UNIFORMITY_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT_E_SUPPLEMENT=Stage14-e11 explicit thin-cover exponent / growing-prime uniformity
```
