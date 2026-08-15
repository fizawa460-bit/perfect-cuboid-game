# Stage25-60 R502 — primitive-height / multiplicity / no-upgrade certificate

STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R502
ROLE=HOSTILE_AUDIT_REPAIR
SOURCE=Meskhishvili 2015 third one-parameter NPC parametrization
TARGET=Stage19 primitive canonical exactly-two-face plus integral-space population

## 1. Why this certificate is required

The first checkpoint60 hostile audit accepted the causal theorem, R501 rigidity and R504 moving section, but rejected the treatment of R502. At checkpoint50 R502 was explicitly left open as a same-exponent fallback. Merely observing that its homogeneous formulas have degree eight does not prove that primitive reduction preserves degree-eight physical height.

This repair therefore applies the same standard used for R501/R507: source-level formulas, a fixed physical cone, exact primitive-gcd control, exactly-two control, bounded parameter multiplicity, and a two-sided family count.

The conclusion is

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4}).}
\]

Thus R502 is a genuine positive-power Stage19 family, but it cannot by itself improve the global lower exponent beyond `1/4`.

## 2. Source-level homogeneous formulas

Meskhishvili's third parametrization is

\[
a=(t^4-1)(t^4-81),
\]
\[
b=4t(t^2-3)(t^4+2t^2+9),
\]
\[
c=16t^2(t^4-9),
\]
\[
d_{ac}=t^8+46t^4+81,
\]
\[
d_{bc}=4t(t^2-3)(t^4+10t^2+9),
\]
\[
d_s=(t^4-2t^2+9)(t^4+10t^2+9).
\]

Put `t=m/n` with coprime positive integers `m,n` and multiply by `n^8`. Define

\[
A=(m^4-n^4)(m^4-81n^4),
\]
\[
B=4mn(m^2-3n^2)(m^4+2m^2n^2+9n^4),
\]
\[
C=16m^2n^2(m^4-9n^4),
\]
\[
D_{AC}=m^8+46m^4n^4+81n^8,
\]
\[
D_{BC}=4mn(m^2-3n^2)(m^4+10m^2n^2+9n^4),
\]
\[
D=(m^4-2m^2n^2+9n^4)(m^4+10m^2n^2+9n^4).
\]

Direct expansion gives

\[
A^2+C^2=D_{AC}^2,
\qquad
B^2+C^2=D_{BC}^2,
\qquad
A^2+B^2+C^2=D^2.
\]

Hence the raw integer family has two integral faces and integral space diagonal.

## 3. Fixed physical cone and canonical order

Restrict again to

\[
\boxed{\frac72<t<4.}
\]

All three edges are positive. We have

\[
B-A=-(t^2-4t-3)
\bigl(t^6+3t^4+16t^3-9t^2-27\bigr).
\]

On `(7/2,4)`, `t^2-4t-3<0`. The second factor is positive because

\[
t^6-9t^2=t^2(t^4-9)>0
\]

and `3t^4+16t^3-27>0`. Therefore `B>A`.

Also

\[
C-B=-4t(t^2-3)
\bigl(t^4-4t^3+2t^2-12t+9\bigr).
\]

Write the final factor as

\[
t^3(t-4)+2(t-3)^2-9.
\]

On `(7/2,4)`, the first term is nonpositive and `2(t-3)^2-9\le -7`, so the factor is negative. Thus `C>B`.

Therefore

\[
\boxed{0<A<B<C}
\]

throughout the cone. After primitive reduction the canonical order remains `(A/g,B/g,C/g)`.

## 4. Exact primitive gcd

Let

\[
g=\gcd(A,B,C)
\]

for coprime positive `m,n` in the cone. Then

\[
\boxed{
g=2^{5\,[m,n\text{ both odd}]}3^{4\,[3\mid m]}.
}
\]

In particular

\[
\boxed{g\le 2^5 3^4=2592.}
\]

### No prime larger than 3

Let `p>3` divide `g`.

If `p|m`, then coprimality gives `p\nmid n`, while

\[
A\equiv81n^8\not\equiv0\pmod p,
\]

contradiction. If `p|n`, then `A\equiv m^8\not\equiv0`, contradiction. Hence `p\nmid mn`.

Since `p|C`,

\[
m^4\equiv9n^4\pmod p.
\]

Put `r=m^2n^{-2}`. Then `r^2\equiv9`, so `r\equiv\pm3` for odd `p>3`.

If `r=3`, the remaining factors of `A` reduce to `8n^4` and `-72n^4`; if `r=-3`, the same values occur because `r^2=9`. Thus `p|A` would force `p|576`, impossible for `p>3`. Hence no prime larger than `3` divides `g`.

### Exact 2-adic part

If `m,n` have opposite parity, both factors of `A` are odd, so `v_2(g)=0`.

If both are odd, then

- `v_2(B)=2+1+2=5`, since `m^2-3n^2\equiv2 mod 4` and `m^4+2m^2n^2+9n^4\equiv12 mod 16`;
- `v_2(C)=4+3=7`, since `m^4-9n^4\equiv8 mod 16`;
- both factors of `A` are divisible by `16`, so `v_2(A)\ge8`.

Therefore `v_2(g)=5` exactly.

### Exact 3-adic part

If `3\nmid m`, then either `3|n`, in which case `A\not\equiv0 mod 3`, or `3\nmid n`, in which case `C\not\equiv0 mod 3`. Thus `v_3(g)=0`.

Now assume `3|m`; then `3\nmid n`. Write `e=v_3(m)\ge1`.

- `m^4-n^4` is a 3-adic unit and `m^4-81n^4` is divisible by at least `3^4`, so `v_3(A)\ge4`; for `e\ge2` the second factor has valuation exactly `4`.
- `m^2-3n^2` has valuation exactly `1`, and `m^4+2m^2n^2+9n^4` has valuation at least `2`, so `v_3(B)\ge e+3\ge4`.
- `m^4-9n^4` has valuation exactly `2`, hence `v_3(C)=2e+2`; this is exactly `4` when `e=1`.

Thus in every case with `3|m`, the minimum valuation is exactly `4`. Hence `v_3(g)=4`.

Combining the prime analysis proves the displayed gcd formula.

## 5. Primitive height remains degree eight

Because `g` divides the edges, the same valuation argument used for R501 shows

\[
g\mid D_{AC},\qquad g\mid D_{BC},\qquad g\mid D.
\]

The primitive space height is therefore `D/g`.

Expanding `D`,

\[
D=m^8+8m^6n^2-2m^4n^4+72m^2n^6+81n^8.
\]

On the physical cone `m>n`,

\[
8m^6n^2-2m^4n^4=2m^4n^2(4m^2-n^2)>0,
\]

so

\[
D\ge m^8.
\]

Together with `g\le2592`,

\[
\boxed{D/g\ge m^8/2592.}
\]

Thus primitive height `<=B` forces

\[
m\ll B^{1/8},
\]

and hence there are only `O(B^{1/4})` reduced rational parameters in the fixed cone. Primitive gcd growth cannot create an exponent above `1/4`.

For the forward height bound, if `m,n<=T`, then

\[
D\le (1+2+9)(1+10+9)T^8=240T^8.
\]

So the family still supplies `gg T^2` reduced parameters at height `O(T^8)`.

## 6. Exactly-two exceptions form a genus-seven curve

The only potentially nonintegral face is `(A,B)`. Dehomogenizing gives

\[
A(t)^2+B(t)^2=P_{502}(t),
\]

where

\[
\boxed{
P_{502}(t)=t^{16}+16t^{14}-196t^{12}+112t^{10}+5926t^8
+1008t^6-15876t^4+11664t^2+6561.
}
\]

It factors as

\[
P_{502}(t)=
(t^8-8t^6-2t^4+216t^2+81)
(t^8+24t^6-2t^4-72t^2+81).
\]

The committed checkpoint60 verifier mechanically computes `gcd(P_502,P_502')=1` modulo `5`. Hence `P_502` is squarefree over `Q`.

Therefore the smooth projective model

\[
w^2=P_{502}(t)
\]

has genus `7`. By Faltings' theorem it has only finitely many rational points. Consequently only finitely many reduced rational parameters in the cone acquire the third rational face. Removing those finitely many parameters leaves exactly-two Stage19 objects.

Primitive scaling does not change this condition: `(A/g)^2+(B/g)^2` is a rational square exactly when `A^2+B^2` is.

## 7. Bounded parameter multiplicity

On the cone, `C` is the largest edge. The scale-free invariant

\[
r(t)=\frac{C}{D}
=\frac{16t^2(t^4-9)}{(t^4-2t^2+9)(t^4+10t^2+9)}
\]

is determined by the primitive canonical box.

For fixed rational `r_0`, clearing denominators gives a nonzero polynomial equation of degree at most `8` in `t`. Thus every primitive canonical similarity class has at most `8` R502 parameters in the cone.

## 8. Two-sided family count

Use the same reduced-rational subset as R501:

\[
m=4n-k,\qquad1\le k<n/2,\qquad\gcd(k,n)=1.
\]

This gives `7/2<m/n<4`, `gcd(m,n)=1`, and `gg T^2` parameters with `m,n<=T`.

The forward bound `D<=240T^8`, finite third-face exceptions, and parameter-fiber bound `<=8` give

\[
N_{R502}(B)\gg B^{1/4}.
\]

Conversely, `D/g>=m^8/2592` implies every R502 Stage19 object of primitive height `<=B` comes from a reduced parameter with `m,n=O(B^{1/8})`. Hence

\[
N_{R502}(B)\ll B^{1/4}.
\]

Therefore

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4}).}
\]

This is a family-specific theorem, not a global upper bound for `N_2(B)`.

## 9. Repair conclusion

The checkpoint60 FAIL is repaired by the stronger option requested by the auditor: R502 receives its own primitive-height / multiplicity / exactly-two certificate rather than merely being restored to the live set.

```text
R502_SOURCE_FORMULAS_BOUND=true
R502_PHYSICAL_CONE=7/2<t<4
R502_CANONICAL_ORDER=0<A<B<C
R502_EXACT_GCD=g=2^(5*both_odd)*3^(4*(3|m))
R502_GCD_GLOBAL_BOUND=2592
R502_PRIMITIVE_HEIGHT_DEGREE=8
R502_THIRD_FACE_EXCEPTION_CURVE_GENUS=7
R502_THIRD_FACE_EXCEPTION_SET_FINITE_BY_FALTINGS=true
R502_PARAMETER_FIBER_BOUND=8
R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R502_HIDDEN_GCD_EXPONENT_UPGRADE=false
R502_ROUTE_BOUNDARY_CERTIFICATE=SUBMITTED_FOR_FRESH_AUDIT
R502_GLOBAL_EXPONENT_UPGRADE=false
FINITE_DATA_USED_AS_PROOF=false
```
