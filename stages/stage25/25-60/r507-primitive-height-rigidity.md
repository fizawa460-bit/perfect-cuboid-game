# Stage25-r507 — primitive-height rigidity of the r501 family

STATUS=PROVED_SUBMITTED_WITH_CHECKPOINT60
ROLE=DEEP_LOWER_LANE_CEILING

Let the audited Stage25-r501 raw family be

\[
A=16m^2n^2(m^4-9n^4),
\]
\[
B=(m^4-10m^2n^2+9n^4)(m^4+2m^2n^2+9n^4),
\]
\[
C=4mn(m^2+3n^2)(m^4-10m^2n^2+9n^4),
\]
\[
D=m^8+46m^4n^4+81n^8,
\]
for coprime positive `m,n` in the fixed physical cone `7/2<m/n<4`. Put

\[
g=\gcd(A,B,C).
\]

The audited Pythagorean identities imply `g|D`, so the primitive space height is `D_prim=D/g`.

## Exact gcd theorem

Define

\[
\epsilon_2=1\iff m,n\text{ are both odd},
\qquad
\epsilon_3=1\iff 3\mid m.
\]

Then

\[
\boxed{g=2^{7\epsilon_2}3^{4\epsilon_3}.}
\]

In particular

\[
\boxed{g\le 2^7 3^4=10368.}
\]

### No prime larger than 3

Write

\[
F=(m^2-n^2)(m^2-9n^2),\qquad
G=m^4+2m^2n^2+9n^4,
\]
so `B=FG` and `C=4mn(m^2+3n^2)F`.

Let a prime `ell>3` divide `g`. Coprimality excludes `ell` dividing both `m,n`.

- If `ell|m`, then `B\equiv81n^8 (mod ell)`, impossible.
- If `ell|n`, then `B\equiv m^8 (mod ell)`, impossible.
- Otherwise set `r=m^2/n^2 mod ell`. From `ell|A` we get `r^2=9`. If `ell|F`, then `r=1` or `9`; intersecting with `r=3` or `-3` forces `ell|2,4,6,12`, impossible for `ell>3`. If `ell|G`, then using `r^2=9` gives `G/n^4=18+2r`, equal to `24` or `12`, again impossible for `ell>3`.

Hence only `2,3` can divide `g`.

### The 2-adic part

If `m,n` have opposite parity, `B` is odd, so `v_2(g)=0`.

If both are odd, `m^4\equiv n^4\equiv1 (mod16)`, hence

\[
m^4-9n^4\equiv-8\pmod{16},
\]

so `v_2(A)=4+3=7`. Meanwhile both factors of `F` are divisible by `8`, and `G` is divisible by `4`, so `v_2(B)>=8`; also `v_2(C)>=10`. Therefore `v_2(g)=7`.

### The 3-adic part

If `3\nmid m`, then either `3|n`, in which case `B\equiv m^8 (mod3)`, or `3\nmid n`, in which case `A` is nonzero modulo `3`. Hence `v_3(g)=0`.

If `3|m`, coprimality gives `3\nmid n`. All three edges are divisible by `3^4`: `A` has `m^2` and `m^4-9n^4`, `B` has at least `3^2` from each of `m^2-9n^2` and `G`, and `C` has at least one factor from `m`, one from `m^2+3n^2`, and two from `m^2-9n^2`. On the other hand

\[
D=m^8+46m^4n^4+81n^8
\]

has `v_3(D)=4` whenever `3|m,3\nmid n`; after division by `81`, the remaining expression is nonzero modulo `3`. Since `g|D`, `v_3(g)=4` exactly.

This proves the formula.

## Exact growth class of this family

The checkpoint50 hostile audit proved a lower count `N_{r501}(B)>>B^{1/4}` after removing the finite third-face-square exceptions and bounded similarity fibers.

The gcd theorem supplies the reverse order bound. Since `D>=m^8` and `g<=10368`,

\[
D_{prim}=D/g\ge m^8/10368.
\]

Therefore `D_prim<=B` implies

\[
m\le (10368B)^{1/8}.
\]

The cone has `n<m`, so even before coprimality/cone restrictions the number of parameter pairs is `O(B^{1/4})`. Hence

\[
\boxed{N_{r501}(B)=\Theta(B^{1/4}).}
\]

Consequences:

- the r501 degree-eight lane is saturated at exponent `1/4`;
- hidden primitive gcd growth cannot upgrade it;
- any global lower exponent above `1/4` must come from a genuinely larger family/extra parameter dimension or a different lower-height mechanism, not from re-estimating this same family.

```text
R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R501_GCD_EXACT_FORMULA=2^(7*both_odd)*3^(4*(3|m))
R501_GCD_GLOBAL_BOUND=10368
R501_HIDDEN_GCD_EXPONENT_UPGRADE=false
GLOBAL_N2_EXPONENT_CEILING_FROM_THIS=false
FINITE_DATA_USED_AS_PROOF=false
```
