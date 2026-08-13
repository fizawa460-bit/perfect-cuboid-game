# Stage13-13fd — retained nonzero harmonics with explicit conductor bookkeeping

> STATUS: `STAGE13_13FD_HARMONIC_CONDUCTOR_LEMMA`
>
> PURPOSE: close R05 Gate D by making every dependence on the retained angular index explicit and removing the unexplained fixed choice `A=48` from the logical proof.
>
> INPUTS: Gate B phase-uniform Wiener control, Gate C core/wing decomposition, and the Stage13-13b external Hecke interface.
>
> SCOPE: nonzero angular harmonics and Vaaler bookkeeping. The exact external theorem statements themselves are restated in Gate F (`13-13ff`).

Write

\[
\Lambda=\log B,
\qquad
H_0=\exp(\Lambda^{1/4}),
\qquad
L=\lfloor\Lambda^4\rfloor.
\]

The key repair is conceptual: no numerical cancellation order such as `48` is needed. A fixed power saving in the scale variable beats every fixed polynomial loss coming from the angular conductor because the core begins at the stretched-exponential cutoff `H_0`.

---

## 1. Exact family interface used by Gate D

For `ell>=1`, the nonzero scale Dirichlet factor has the form

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s),
\]

where the residual factor is holomorphic and uniformly controlled on the fixed half-plane supplied by the Wiener argument. In this gate we use the fixed strip

\[
\boxed{\Re s\ge \frac34.}
\]

The only family consequence needed is the following.

### Hecke-family summatory interface

There exist fixed constants

\[
\delta_H>0,\qquad C_H\ge0,\qquad D_H\ge0,
\]

independent of `B`, `X`, and `ell`, such that

\[
\boxed{
S_\ell(X):=\sum_{h\le X}a_\ell(h)
\ll
X^{1-\delta_H}(1+\ell)^{C_H}(\log 2X)^{D_H}
}
\]

uniformly for every

\[
X\ge2,
\qquad
\ell\ge1.
\]

The retained restriction `ell<=floor((log B)^4)` is imposed only later, when the Vaaler modes are summed. This distinction matters: at the core lower cutoff `X=H0`, the retained `ell` range can be much larger than `(log X)^4`, so a local condition of that form would not be sufficient.

This is the proof-facing form of the finite Perron consequence of:

1. entire/holomorphic continuation of the nonzero Gaussian-Hecke factor across the strip;
2. polynomial vertical and angular-conductor growth on that fixed strip;
3. the uniform residual Euler/Wiener factor;
4. a finite Perron contour with no pole crossed.

Zeros of `L(s,xi_{8ell})` do not obstruct the shift because the Dirichlet series contains `L` itself, not `1/L`, `L'/L`, or a fractional power. Consequently the Gaussian-Hecke zero-free region is not required for this step.

Gate F will record the exact external theorem contracts behind this interface. Gate D only performs the conductor/log arithmetic once this fixed family estimate is available.

---

## 2. Why an unspecified polynomial conductor exponent is harmless

The objection to R04 was that a factor such as

\[
(1+\ell)^{C_H}
\]

was never explicitly propagated through the retained range. We do that now.

On the core,

\[
h\ge H_0.
\]

By partial summation,

\[
\sum_{H_0<h\le B}\frac{a_\ell(h)}h
=
\frac{S_\ell(B)}B-
\frac{S_\ell(H_0)}{H_0}
+\int_{H_0}^{B}\frac{S_\ell(t)}{t^2}\,dt.
\]

Applying the family bound gives

\[
\boxed{
\left|\sum_{H_0<h\le B}\frac{a_\ell(h)}h\right|
\ll
(1+\ell)^{C_H}\Lambda^{D_H}H_0^{-\delta_H}.
}
\]

Since

\[
H_0^{-\delta_H}
=
\exp(-\delta_H\Lambda^{1/4}),
\]

the scale channel already carries stretched-exponential decay in `Lambda`.

---

## 3. Base-channel bookkeeping for one harmonic

After the scale variable is summed by cancellation, the two base channels are bounded by the same positive zero-mode majorants used in the raw argument. Their logarithmic cost is at most

\[
\Lambda^2.
\]

The Gate B mixed correction is uniform in the phase and has fixed logarithmic moments, so it introduces no additional power of `ell`; fixed logarithmic shifts may be absorbed into `D_H`.

Therefore the contribution of a single nonzero retained mode satisfies

\[
\boxed{
\mathcal H_\ell(B)
\ll
B\Lambda^{D_H+2}(1+\ell)^{C_H}
\exp(-\delta_H\Lambda^{1/4}).
}
\]

This is the first place where the conductor exponent is carried explicitly instead of hidden inside an `O_A` statement.

---

## 4. Summing every retained mode

Use Vaaler degree

\[
L=\lfloor\Lambda^4\rfloor.
\]

Gate D needs only a universal bound for the nonzero Fourier coefficients of the chosen Vaaler majorant/minorant; denote it by `C_V`. Gate F records the exact external coefficient statement. Thus no positive power of `ell` is contributed by the Vaaler coefficient itself.

For fixed `C_H`,

\[
\sum_{1\le\ell\le L}(1+\ell)^{C_H}
\ll
L^{C_H+1}.
\]

Since `L<=Lambda^4`,

\[
L^{C_H+1}
\ll
\Lambda^{4C_H+4}.
\]

Hence the entire retained nonzero family on the core satisfies

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B\Lambda^{4C_H+D_H+6}
\exp(-\delta_H\Lambda^{1/4}).
}
\]

The exponent is completely accounted for:

```text
4*C_H    angular-conductor polynomial over ell<=Lambda^4
+4       number of retained modes
+D_H     fixed logarithmic loss in the Hecke-family summatory estimate
+2       two base-channel logarithms
--------------------------------
4*C_H + D_H + 6
```

No hidden `O((log B)^C)` remains in the harmonic family budget.

---

## 5. The stretched exponential beats every fixed log target

For any fixed `A>0`, fixed `C_H,D_H`, and fixed `delta_H>0`,

\[
\Lambda^{4C_H+D_H+6+A}
\exp(-\delta_H\Lambda^{1/4})\to0.
\]

Indeed, taking logarithms gives

\[
(4C_H+D_H+6+A)\log\Lambda
-\delta_H\Lambda^{1/4}\to-\infty.
\]

Therefore

\[
\boxed{
\mathcal E_{\rm harm,core}
=o_A(B\Lambda^{-A})
\quad\text{for every fixed }A>0.
}
\]

In particular it is `o(B Lambda^3)`.

This proves something stronger and cleaner than the old ledger entry `O(B(log B)^-6)`: the precise fixed conductor polynomial does not matter, provided it is polynomial with fixed exponent.

---

## 6. Why `A=48` is no longer a logical parameter

R04 converted an asserted arbitrary log saving into

\[
(\log H_0)^{-48}=\Lambda^{-12}
\]

and then paid `Lambda^4` modes and `Lambda^2` base bookkeeping. That numerical ledger is valid only after one has already proved a uniform `A=48` estimate with all conductor dependence absorbed.

Gate D removes that circular bookkeeping risk. We instead keep the conductor loss visible and use the power-saving form of the nonzero Perron estimate.

Thus

```text
FIXED_A48_REQUIRED=false
```

and no claim in R05 needs to know whether the external polynomial exponent is `2`, `20`, or any other fixed value.

---

## 7. Wings are removed before harmonic expansion

The small-height and small-coordinate pieces are not estimated by summing `L` harmonic absolute values.

The proof order is:

1. use the original positive counting majorant to remove
   `h<H0` and `min(r,s)<U`;
2. charge those pieces to the Gate C bounds

\[
O(B\Lambda^{9/4}),
\qquad
O(B\Lambda^{5/2});
\]

3. only then introduce the Vaaler Fourier expansion on the remaining core.

Therefore no spurious factor `L=Lambda^4` multiplies the wing errors.

This makes explicit a point that R04 stated too tersely.

---

## 8. Vaaler constant-term excess

The degree is `L=Lambda^4`. The Vaaler constant-term excess is `O(1/L)`. The positive raw total bound

\[
A_{ab}(B)+A_{ac}(B)+A_{bc}(B)
=O(B\Lambda^3)
\]

therefore gives

\[
\boxed{
\mathcal E_{\rm Vaaler,0}
\ll
B\Lambda^3/L
=O(B\Lambda^{-1}).
}
\]

This use of the positive total bound is only an error majorant. It does not insert a directional leading constant.

The exact Vaaler theorem statement, including the nonzero coefficient bound, is a Gate F item.

---

## 9. Combined Gate D harmonic ledger

The full nonzero-harmonic part is now

\[
\boxed{
\mathcal E_{\rm harmonic}
\ll
B\Lambda^{4C_H+D_H+6}
\exp(-\delta_H\Lambda^{1/4})
+
B\Lambda^{-1}.
}
\]

Both terms are `o(B Lambda^3)`.

The first term is smaller than every fixed negative logarithmic power; the second is the explicit Vaaler zero-mode excess.

No effective numerical convergence rate for the final directional ratio is claimed. The constants `delta_H,C_H,D_H` are existence constants in the external analytic interface, not calibrated numerical constants.

---

## 10. Gate D locks

```text
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
HECKE_STRIP_LEFT=3/4
HECKE_FAMILY_BOUND=S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H_for_all_ell>=1
RETAINED_HARMONICS=ell<=floor((log B)^4)
HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6
HARMONIC_STRETCHED_SAVING=exp(-delta_H*(log B)^(1/4))
HARMONIC_CORE=o_A(B(log B)^(-A))_for_every_fixed_A
VAALER_ZERO_MODE_EXCESS=O(B(log B)^-1)
FIXED_A48_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
WINGS_EXPANDED_HARMONIC_BY_HARMONIC=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fe
```

Gate D closes the conductor/log-bookkeeping objection. It does not yet restate the complete Stage12 counting interface (Gate E) or the exact external Hecke/Vaaler theorem contracts (Gate F).