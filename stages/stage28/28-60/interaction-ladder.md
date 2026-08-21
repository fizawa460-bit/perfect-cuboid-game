# Stage28-60 — matched interaction ladder

Checkpoint60 can compare how prior face structure changes the relative cost of later arithmetic conditions, while preserving population-ratio semantics.

## 1. Space interaction: already audited

Stage25 weapon `S25-W02` gives

\[
\mathcal I_{sp}(B)
=
\frac{N_2/M_2}{N_1/M_1}
=
\frac{N_2M_1}{M_2N_1}
\gg B^{1/4}(\log B)^{-7}
\to\infty.
\]

Thus the integral-space condition is positively enhanced on the two-face host relative to the one-face host, on the exact matched population-ratio scale. This is not a stochastic-independence statement.

## 2. New third-face interaction invariant

Define

\[
\mathcal I_{face}(B)
=
\frac{M_3/M_2}{M_2/M_1}
=
\frac{M_3M_1}{M_2^2}.
\]

The audited Stage22 asymptotics are

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5.
\]

Stage28-50-r2 proves

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}.
\]

Therefore

\[
\boxed{
\liminf_{B\to\infty}
B^{-1/3}(\log B)^9\mathcal I_{face}(B)
\ge
\frac{81}{160\pi^4 C_{M_2}^2}>0.
}
\]

In particular

\[
\boxed{\mathcal I_{face}(B)\to\infty.}
\]

So, on the matched adjacent-stratum population-ratio scale, acquisition of a third integral face is asymptotically enhanced relative to acquisition of the second integral face.

This is a new Stage28 causal deduction from audited inputs. It does not say that a particular Stage18 object has a probability of acquiring a third face, and it does not identify the true `M3` exponent.

## 3. Comparative interpretation

Both ladders are positive-divergent:

```text
SPACE_INTERACTION_TWO_FACE_VS_ONE_FACE=POSITIVE_DIVERGENT
THIRD_FACE_INTERACTION_THREE_FACE_VS_TWO_FACE=POSITIVE_DIVERGENT
```

Thus accumulated face arithmetic is associated with positive interaction enhancement in both channels. But the two divergences have different denominators and are not independent factors. Their quotient does not currently have a determined sign or limit.

The exact identity

\[
\frac{M_3}{N_2}
=
\frac{M_3/M_2}{N_2/M_2}
\]

remains the direct Stage28 bridge. Neither positive-divergent ladder resolves whether this direct ratio tends to zero, stays bounded/oscillatory, or tends to infinity.

```text
NEW_STAGE28_FACE_INTERACTION_INVARIANT_PROVED_CANDIDATE=true
FACE_INTERACTION_POSITIVE_DIVERGENT_CANDIDATE=true
FACE_INTERACTION_SCALED_LIMINF_CONSTANT=81/(160*pi^4*C_M2^2)
SPACE_AND_FACE_INTERACTIONS_MULTIPLIED=false
DIRECT_M3_N2_ORDERING_FROM_INTERACTION_LADDERS=false
```