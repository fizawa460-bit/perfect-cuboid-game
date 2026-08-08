# Stage14-e9 — gcd/lcm local control and mod-2/mod-3 completion blockers

> STATUS: `STAGE14_E9_COMPLETE_GCD_LCM_LOCAL_CONTROL_AND_2_3_BLOCKERS`
>
> TRACK: post-e8 ambient gcd/lcm and local-statistics control
>
> INPUT: Stage14-e1 primitive face-pair bijection + Stage14-e2 exact ambient census + Stage14-e8 Euler-brick thin-count gap
>
> IMPORTANT: this stage proves an exact gcd/lcm inverse and two elementary local blockers for third-face-square completion. The observed gcd/lcm distributions remain finite diagnostics only.

## 1. E8 handoff

Stage14-e8 proves an independent Euler-brick upper envelope

\[
R_{\rm EB}(B)\ll B\log B\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)=B^{1+o(1)},
\]

while the exact physical census contains only `219` primitive Euler bricks at `B=10^6`.

E9 asks which arithmetic strata in the much larger two-face ambient population are already forbidden from completing the third face.

## 2. Exact gcd/lcm inverse from the physical tuple

Take a primitive ambient object

\[
(e,x,y),\qquad x<y,
\]

with

\[
e^2+x^2=h_1^2,\qquad e^2+y^2=h_2^2,
\qquad \gcd(e,x,y)=1.
\]

Define

\[
\boxed{u=\gcd(e,x)},\qquad
\boxed{v=\gcd(e,y)}.
\]

Primitivity gives

\[
\boxed{\gcd(u,v)=1}.
\]

The reduced primitive shared-leg denominators are

\[
S_1=\frac e u,\qquad S_2=\frac e v.
\]

Since `u` and `v` are coprime,

\[
\boxed{g=\frac e{uv}=\gcd(S_1,S_2)}.
\]

Consequently

\[
\boxed{S_1=gv},\qquad
\boxed{S_2=gu},\qquad
\boxed{\operatorname{lcm}(S_1,S_2)=guv=e}.
\]

In the frozen e1 notation this is exactly

\[
\boxed{u=\beta=S_2/g},\qquad
\boxed{v=\alpha=S_1/g}.
\]

Thus the face-pair gcd/lcm coordinates are recovered from the physical tuple with two gcd operations and one division; no Euclid-parameter reconstruction is required.

## 3. Six prime-support states

For a prime `p`, record whether `p` divides `g,u,v`. Since `gcd(u,v)=1`, `p` cannot divide both `u` and `v`. The only possible states are

```text
none, G, U, V, GU, GV
```

and `UV`, `GUV` are impossible.

In denominator valuations:

```text
none : vp(S1)=vp(S2)=0
U    : vp(S2)>0=vp(S1)
V    : vp(S1)>0=vp(S2)
G    : vp(S1)=vp(S2)>0
GU   : vp(S2)>vp(S1)>0
GV   : vp(S1)>vp(S2)>0
```

This is the local state space audited at `p=2,3,5,7,11,13`.

## 4. The `p=2`, state-G completion blocker

Assume the `p=2` state is `G`. Then

\[
2\mid g,\qquad 2\nmid u,\qquad 2\nmid v.
\]

Hence `e=guv` is even. Since

\[
u=\gcd(e,x),\qquad v=\gcd(e,y)
\]

are odd, neither `x` nor `y` is even. Thus both are odd and

\[
x^2+y^2\equiv1+1\equiv2\pmod4.
\]

A square is never `2 mod 4`, so

\[
\boxed{
p=2\text{ state }G\Longrightarrow x^2+y^2\ne\square.
}
\]

Therefore every `p=2,G` ambient point is rigorously excluded from Euler-brick completion.

## 5. The `p=3`, state-G completion blocker

Assume the `p=3` state is `G`. Then

\[
3\mid g,\qquad 3\nmid u,\qquad 3\nmid v.
\]

Thus `3|e`. If `3|x`, then `3|gcd(e,x)=u`, contradiction; similarly `3\nmid y`. Therefore

\[
x^2\equiv y^2\equiv1\pmod3
\]

and

\[
x^2+y^2\equiv2\pmod3.
\]

Since a square modulo `3` is only `0` or `1`,

\[
\boxed{
p=3\text{ state }G\Longrightarrow x^2+y^2\ne\square.
}
\]

Hence `p=3,G` is a second rigorous Euler-completion blocker.

## 6. Deterministic census and e2 compatibility

The e9 script performs one edge-first enumeration through `B=200,000`, accumulates the e2 cutoffs, reconstructs `(g,u,v)` for every raw ambient object, and reproduces all e2 locks:

| B | raw ambient | exactly two | Euler bricks | `(a,b,c)` exactly two |
|---:|---:|---:|---:|---:|
| 2,000 | 4,833 | 4,812 | 7 | (1,342, 2,136, 1,334) |
| 10,000 | 41,720 | 41,666 | 18 | (12,464, 18,198, 11,004) |
| 50,000 | 331,857 | 331,731 | 42 | (103,892, 142,403, 85,436) |
| 200,000 | 1,896,751 | 1,896,505 | 82 | (612,678, 805,875, 477,952) |

At `B=200,000`, the rigorous blocker counts in the raw ambient population are

```text
p=2 state G             = 453,380
p=3 state G             = 561,484
union (p=2 G or p=3 G)  = 884,186
third-square incidences in the union = 0
```

Thus the two elementary blockers already certify non-completion for

\[
\boxed{
\frac{884186}{1896751}\approx46.6158\%
}
\]

of the finite raw ambient census at this cutoff.

The zero third-square incidence is theorem-backed by §§4–5, not inferred from the finite table.

## 7. Finite gcd/lcm distribution

Among the `1,896,505` exactly-two objects at `B=200,000` there are `19,726` distinct observed `g` values. The leading counts are

```text
g=4   : 79,637
g=3   : 68,106
g=12  : 61,421
g=1   : 58,662
g=5   : 40,961
g=20  : 37,179
```

The `g=1` stratum therefore occupies only

\[
\frac{58662}{1896505}\approx3.09316\%
\]

at this finite cutoff.

Since

\[
\frac ge=\frac1{uv},
\]

the ratio `g/e` measures how much of the shared-edge lcm comes from the common gcd rather than the coprime gluing cofactors. At `B=200,000`:

```text
g/e = 1               : 27,242
1/2 <= g/e < 1        : 29,087
1/10 <= g/e < 1/2     : 178,078
1/100 <= g/e < 1/10   : 457,679
1/1000 <= g/e < 1/100 : 603,996
g/e < 1/1000          : 600,423
```

Hence `1,204,419`, about `63.5073%`, lie in `g/e<1/100`.

These percentages are finite diagnostics. No limiting `g` or `g/e` law is claimed.

## 8. Finite directional separation

At `B=200,000`, the exactly-two `g=1` fractions are approximately

```text
a : 26,070 / 612,678  = 4.25509%
b : 23,327 / 805,875  = 2.89462%
c :  9,265 / 477,952  = 1.93848%
```

For the cofactor-dominated stratum `g/e<1/100` they are approximately

```text
a : 362,472 / 612,678 = 59.1619%
b : 508,799 / 805,875 = 63.1362%
c : 333,148 / 477,952 = 69.7032%
```

This supplies a concrete arithmetic control variable for the directional-bias decomposition isolated in e5, but it is not a limiting direction theorem.

## 9. Completion incidence by `g/e` bin

The same audit records raw ambient counts and third-square incidences at `B=200,000`:

| `g/e` bin | raw | third-square incidences |
|---|---:|---:|
| `1` | 27,242 | 0 |
| `[1/2,1)` | 29,087 | 0 |
| `[1/10,1/2)` | 178,093 | 15 |
| `[1/100,1/10)` | 457,746 | 67 |
| `[1/1000,1/100)` | 604,106 | 110 |
| `<1/1000` | 600,477 | 54 |

The first two zeroes are finite observations only. E9 does not promote them to an infinite-family obstruction.

## 10. Local ledgers beyond the proved blockers

For every audited cutoff, e9 records the six support states at

```text
p=2,3,5,7,11,13
```

for both the exactly-two population and the third-square incidences.

At `B=200,000`, the third-square ledger has

```text
p=2: G=0
p=3: G=0
```

as forced by §§4–5. The distributions for the other states and primes remain finite data. No independence across primes is asserted.

## 11. Literature boundary

The literature refresh classifies common-side Pythagorean formulas as adjacent/reusable arithmetic, toric adelic equidistribution as the natural theorem-level mechanism for future local-mass calculations, and recent coprime-Pythagorean-pair Euler-brick work as adjacent geometry.

Current gate:

```text
OCHIENG_ET_AL_COMMON_SIDE_FORMULAS=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
HUANG_TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD
PESCHMANN_COPRIME_PYTHAGOREAN_PAIR_GEOMETRY=ADJACENT_RESULT
DIRECT_STAGE14_E9_GCD_LCM_REAL_HEIGHT_DISTRIBUTION=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

No novelty claim is made from search absence.

## 12. Locked boundary

E9 closes the requested gcd/lcm control layer at the following level:

```text
STAGE14_E9=COMPLETE_GCD_LCM_LOCAL_CONTROL_AND_2_3_BLOCKERS
EXACT_GCD_LCM_INVERSE_LOCKED=true
LOCAL_PRIME_STATE_DECOMPOSITION_LOCKED=true
P2_STATE_G_EULER_COMPLETION_BLOCKED=true
P3_STATE_G_EULER_COMPLETION_BLOCKED=true
FINITE_CENSUS_REGENERATES_E2_LOCKS=true
MAX_LOCAL_AUDIT_B=200000
ASYMPTOTIC_GCD_LCM_DISTRIBUTION_PROVED=false
FIXED_RELATIVE_EULER_BRICK_SAVING_PROVED=false
```

The natural optional refinement is an explicit adelic-mass calculation for the six local states, followed by a stronger residue-state sieve. No Stage14-e10 is defined here.
