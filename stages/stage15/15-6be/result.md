# Stage15-6be — fixed physical-diagonal fiber has only subpolynomial multiplicity

Base: Stage15-6bd in the current cycle. We now fix the exact diagonal-product variable

\[
S=\sqrt{F_1F_2}=kZW\le2B
\]

and count the complete Stage15 decorated fiber above this single value.

Audit verdict: `PASS`.

## 1. The quartic values are divisors of S^2

For a fixed positive integer `S`, every retained pair satisfies

\[
F_1F_2=S^2.
\]

Therefore `F_1|S^2` and `F_2=S^2/F_1`. The number of ordered choices is at most

\[
\tau(S^2)=B^{o(1)}
\]

uniformly for `S<=2B` by the standard divisor bound (AR-016).

## 2. A fixed F has divisor-many primitive coordinate pairs

For one fixed `F`, the reduced coordinate pair satisfies

\[
\boxed{f^2+g^2=F,\qquad (f,g)=1,\qquad f,g>0.}
\]

The total number of integral representations is

\[
r_2(F)\le4\tau(F)=B^{o(1)}.
\]

Primitivity and positivity only reduce this number.

For each such `(f,g)`, the squareclass split is **unique**:

\[
\kappa_f=\operatorname{sf}(f),\qquad
c=\sqrt{f/\kappa_f},
\]

\[
\kappa_g=\operatorname{sf}(g),\qquad
e=\sqrt{g/\kappa_g}.
\]

Hence `kappa=sf(fg)=kappa_f*kappa_g` is reconstructed rather than summed independently.

## 3. Gaussian lift and physical reconstruction add only B^o(1)

The common norm core is already fixed by

\[
k=\operatorname{sf}(F).
\]

For a primitive Gaussian integer `f+i g` of norm `k*Z^2`, Gaussian unique factorization gives only unit/orientation/divisor-many choices for writing

\[
f+i g=Kz^2,\qquad N(K)=k.
\]

This is the same finite/subpolynomial Gaussian core decoration already admitted in 6ak/6ar and costs `B^o(1)`.

After the two coordinate pairs are chosen, the condition that their coordinate cores agree is only a filter. Stage15-6ak then reconstructs the primitive toric pairs `(m,n),(r,s)` and the cross-gcd normalizers uniquely. Positivity, canonical order, exactly-two and direction masks are postfilters.

## 4. Fixed-S fiber theorem

Combining the divisor choices of `F_1`, the sum-of-two-squares representations of `F_i`, the Gaussian decorations and the unique toric reconstruction gives

\[
\boxed{
\#\{\text{Stage15 physical survivors above fixed }S\}
\ll B^{o(1)}.
}
\]

Uniformly for `S<=2B`.

Equivalently, if `\mathcal S(B)` denotes the set of admissible diagonal-product values occurring in the retained population, then

\[
\boxed{N_2(B)\ll |\mathcal S(B)|B^{o(1)}.}
\]

The reverse inequality `|\mathcal S(B)|<=N_2(B)` is immediate after accounting for the absolute `gamma in {2,4}` decoration, so the whole-family exponent is now equivalent, up to `B^o(1)`, to the exponent of admissible diagonal support.

## 5. Consequence for the 6bc theorem gate

The 6bc phrase

```text
same-twist / same-2-descent-cell weighted rational-point second moment
```

was a legitimate conditioned formulation, but it is **not the minimal global obstruction**. After 6bd-6be, the multiplicity per physical diagonal is already subpolynomial without any average-rank, Selmer, or integral-point theorem.

Thus the external second-moment route is superseded as a packet-multiplicity requirement.

```text
AR-016=DIRECT_REUSE_FOR_DIVISOR_MULTIPLICITY
AR-023/024=PASS
AR-028=PASS_NO_RECHARGE
```

## 6. Frozen exit

```text
STAGE15_6_SUBSTAGE=6be
STAGE15_6BE_AUDIT_VERDICT=PASS
STAGE15_6BE_FIXED_S_DIVISOR_PAIRS=B^o(1)
STAGE15_6BE_FIXED_F_SUM_OF_TWO_SQUARES_REPRESENTATIONS=B^o(1)
STAGE15_6BE_COORDINATE_SQUARECLASS_SPLIT_UNIQUE=true
STAGE15_6BE_TORIC_RECONSTRUCTION_UNIQUE=true
STAGE15_6BE_FIXED_S_PHYSICAL_FIBER=B^o(1)
STAGE15_6BE_WEIGHTED_SECOND_MOMENT_PACKET_GATE_SUPERSEDED=true
STAGE15_6BE_HALF_POWER_SUPPORT_BOUND_PROVED=false
STAGE15_6BE_EXIT=ADMISSIBLE_PHYSICAL_DIAGONAL_SUPPORT_AUDIT_READY
```

Next: Stage15-6bf audits what existing twist/integral-point second-moment theorems actually say and records why they are no longer the minimal receiver; then the cycle should identify the exact support-count theorem species.
