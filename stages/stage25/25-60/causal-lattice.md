# Stage25-60 causal interaction lattice

Let

\[
F(B)=\frac{M_2}{M_1},\qquad
S(B)=\frac{N_1}{M_1},\qquad
A(B)=\frac{N_2}{M_2},\qquad
T(B)=\frac{N_2}{N_1}.
\]

Here `F` is the Stage22 adjacent-stratum population ratio, `S` is the Stage21 one-face space ratio, `A` is the Stage24 two-face space ratio, and `T` is the Stage23 space-conditioned second-face ratio. These are population-size ratios, not objectwise probabilities.

Define the exact interaction cross-ratio

\[
\boxed{
I(B)=\frac{A(B)}{S(B)}
=\frac{T(B)}{F(B)}
=\frac{N_2(B)M_1(B)}{M_2(B)N_1(B)}.
}
\]

Then the Stage25 endpoint ratio has three exact decompositions:

\[
\boxed{
\frac{N_2}{M_1}=F\,A=S\,T=F\,S\,I.
}
\]

The third identity is the precise correction to the formerly-invalid naive product `F*S`. The naive product is not itself the endpoint ratio; multiplying by `I` makes it exact.

## Certified scales after checkpoint50

From Stage21 and Stage22,

\[
S\asymp B^{-1}(\log B)^2,
\qquad
F\asymp B^{-1}(\log B)^4.
\]

From the audited Stage25 backflow to Stage23/24,

\[
B^{-3/4}(\log B)^{-5}
\ll A
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5},
\]

\[
B^{-3/4}(\log B)^{-3}
\ll T
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Therefore both exact definitions of `I` give

\[
\boxed{
B^{1/4}(\log B)^{-7}
\ll I(B)
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-7}.
}
\]

In particular

\[
\boxed{I(B)\to\infty.}
\]

This is a rigorous **positive divergent population-ratio interaction**. It is not a stochastic-independence theorem.

The exact corrected-product decomposition gives

\[
F S\asymp B^{-2}(\log B)^6,
\]
while multiplication by the interaction factor yields

\[
\boxed{
B^{-7/4}(\log B)^{-1}
\ll
\frac{N_2}{M_1}
\ll_\varepsilon
B^{-3/2+\varepsilon}(\log B)^{-1}.
}
\]

Thus the independent-looking product scale undercounts the actual combined population by the divergent factor `I`.

## Ambient space baseline hierarchy

Let

\[
S_0(B)=\frac{N_S^{all}(B)}{U(B)}\asymp B^{-1}
\]
be the audited Stage16S ambient space-diagonal ratio.

The one-face interaction is

\[
J_1=\frac{S}{S_0}\asymp(\log B)^2\to\infty.
\]

The two-face interaction is

\[
J_2=\frac{A}{S_0},
\]
so

\[
\boxed{
B^{1/4}(\log B)^{-5}
\ll J_2
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-5}.
}
\]

Hence `J2->infinity`, and moreover

\[
\boxed{\frac{J_2}{J_1}=I\to\infty.}
\]

The interaction class therefore strengthens from a logarithmic enhancement after one face to at least a polynomial-over-log enhancement after two faces.

## Order-of-conditions interpretation

Because

\[
I=\frac{A}{S}=\frac{T}{F},
\]
the same positive divergent multiplier appears in both orders:

- compare imposing the space condition on the two-face stratum versus on the one-face stratum: `A/S=I`;
- compare the two-face population ratio after imposing space versus before imposing space: `T/F=I`.

So the order comparison is algebraically symmetric at the cross-ratio level. This does **not** turn the exactly-one and exactly-two strata into literal nested subsets and does not license probabilistic language.

```text
CAUSAL_CROSS_RATIO_IDENTITY=PASS
CORRECTED_PRODUCT_IDENTITY=N2/M1=(M2/M1)*(N1/M1)*I
INTERACTION_SIGN=POSITIVE_DIVERGENT
INTERACTION_LOWER=I>>B^(1/4)(log B)^(-7)
ONE_FACE_AMBIENT_INTERACTION=Theta((log B)^2)
TWO_FACE_AMBIENT_INTERACTION_LOWER=J2>>B^(1/4)(log B)^(-5)
INTERACTION_CLASS_UPGRADE=LOGARITHMIC_TO_POLYNOMIAL_OVER_LOG
PROBABILISTIC_INDEPENDENCE_INFERRED=false
LITERAL_SUBSET_TRANSITION_INFERRED=false
DOUBLE_CHARGE_CHECK=PASS
```
