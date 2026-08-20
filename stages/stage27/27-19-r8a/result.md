# Stage27-19-r8a — lower construction degree-ledger search

```text
TASK_ID=Stage27-19-r8a
PARENT_ROUTE=Stage27-19-r401d
ROUTE_KIND=LOWER_NEW_CONSTRUCTION_SEARCH
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The audited lower calibration gives the exact one-parameter progress gate

\[
h_{alg}=2d_x+2d_y-g<8.
\]

Here `d_x,d_y` are the homogeneous degrees of the two toric Pythagorean parameters and `g` is the degree of a common polynomial factor removed from all three reconstructed physical edges.

This immediately partitions every possible strict-improvement mechanism:

1. **low raw degree:** `d_x+d_y<=3` already gives `h_raw<=6`;
2. **moderate raw degree with cancellation:** `d_x+d_y=4` requires `g>=1`, while `d_x+d_y=5` requires `g>=3`, etc.;
3. **thick-family route:** retain `h_alg=8` but obtain effective source-count exponent `>2`.

The previous r401 search already closes rational sections, constant-u shortcuts, and the full affine-linear moving-u genus-zero ansatz. Therefore a new one-parameter curve cannot be certified merely by repeating those low-degree ansatz classes.

A useful new structural observation is that any strict one-parameter improvement must be visible **before arithmetic gcd normalization** in this ledger: bounded residual gcd cannot change the exponent. Hence searches for accidental numerical gcd growth without a polynomial common factor cannot produce a certified lower exponent improvement.

For a rational curve with quadratically many primitive source pairs of height `<=T` and physical size `B~T^h`, the resulting exponent is `2/h`. Thus the first admissible targets are:

- `h=7` -> exponent `2/7>1/4`;
- `h=6` -> exponent `1/3`;
- lower `h` would be stronger.

No new physical curve is proved in this step. The next search should therefore target a genuinely nonlinear multisection whose toric degree ledger is one of the above admissible types, rather than another section/affine-bisection search.

```text
LOWER_PROGRESS_LEDGER_RESTATED=true
BOUNDED_ARITHMETIC_GCD_CANNOT_IMPROVE_EXPONENT=true
STRICT_ONE_PARAMETER_TARGETS=h_alg<=7
H7_IMPLIED_LOWER_EXPONENT=2/7
H6_IMPLIED_LOWER_EXPONENT=1/3
NEW_CURVE_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r8b
```
