# Stage13-13fd — R05 Gate D result

> STATUS: `COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING`
>
> INPUT: Gates A–C complete; R04 immutable.
>
> NEXT: `13-13fe` — complete Stage12 R09 counting / factor-two interface.

## Result

The retained nonzero-harmonic estimate no longer depends on the unexplained fixed choice `A=48`.

For the nonzero Gaussian angular factor, Gate D uses the fixed-strip family interface

\[
S_\ell(X)
\ll
X^{1-\delta_H}(1+\ell)^{C_H}(\log 2X)^{D_H}
\]

for fixed `delta_H>0`, `C_H,D_H>=0`, uniformly for every `X>=2` and `ell>=1`. The retained Vaaler range is imposed only later:

\[
1\le\ell\le L=\lfloor(\log B)^4\rfloor.
\]

This avoids the local-`X` range mismatch that would occur near `X=H0` if one required `ell<=(log X)^4`.

On the core `h>=H0=exp((log B)^(1/4))`, partial summation gives

\[
\sum_{H_0<h\le B}\frac{a_\ell(h)}h
\ll
(1+\ell)^{C_H}(\log B)^{D_H}
\exp(-\delta_H(\log B)^{1/4}).
\]

The two base channels cost at most `(log B)^2`. Summing all retained modes costs

\[
\sum_{\ell\le L}(1+\ell)^{C_H}
\ll
(\log B)^{4C_H+4}.
\]

Therefore

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B(\log B)^{4C_H+D_H+6}
\exp(-\delta_H(\log B)^{1/4}).
}
\]

For every fixed `A>0`, this is

\[
o_A(B(\log B)^{-A}).
\]

The conductor polynomial is therefore fully exposed and harmless without knowing its optimized numerical exponent.

The proof removes the small-height and small-coordinate wings before harmonic expansion, so no spurious factor `(log B)^4` multiplies their Gate C estimates.

The Vaaler constant-term excess remains

\[
O(B(\log B)^{-1})
\]

at degree `L=(log B)^4`.

## Consequence for the R04 objection

DeepSeek's conductor/log-bookkeeping objection is closed at the internal-proof level:

- the fixed strip is visible (`Re s>=3/4`);
- angular-conductor growth appears as `(1+ell)^C_H`;
- the whole retained range is summed explicitly;
- the final log exponent is `4*C_H+D_H+6`;
- the core cutoff supplies `exp(-delta_H(log B)^(1/4))`, which beats every fixed log power;
- `A=48` is no longer a logical input.

The exact external Hecke and Vaaler theorem statements remain Gate F, so this stage does not overstate self-containment.

## Locks

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