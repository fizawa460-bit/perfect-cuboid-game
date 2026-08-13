# Stage13-13fw — R08 repair plan after Claude R07 review

R07 is immutable. R08 is a non-theorem-changing self-containedness repair.

## R08-A — define the local square set exactly

Insert before first use:

\[
QR_0(\mathbf F_p):=\{t^2:t\in\mathbf F_p\}.
\]

Thus `0 in QR_0(F_p)`. Distinguish, if ever needed, the nonzero square set by a different symbol such as `QR(F_p)=QR_0(F_p)\setminus\{0\}`.

The Gate B predicate must then read literally

\[
W_p(x,z)=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}.
\]

Add a one-line `p=3` sanity check showing all eight unit states are accepted and `alpha_3=lambda_3=1`.

## R08-B — inline the complete inert unit character sum

Do not say merely that Stage13-12ag proves the count. Embed the full symbolic reduction in the canonical proof and the future bundle:

1. define the quadratic character `chi`, extended by `chi(0)=0`;
2. express the accepted indicator including the zero correction;
3. derive the four character sums `S0,S1,S2,S3`;
4. include the degree-two character identity used for the single-variable sums;
5. state and use `J(chi,chi)=1` for `p=3 mod 4` under the chosen convention;
6. reproduce the `S3=A+B-C-D=-2` reduction, including the antisymmetry step;
7. conclude

```text
S=2(p-1)
T=p^2-1
Z0=4
Nacc=(T+S+Z0)/2=(p+1)^2/2
alpha_p=(p+1)/(2(p-1))
lambda_p=(p+5)/(2(p+1)).
```

The repository's Stage13-12ag proof may remain provenance, but the R08 review target must contain the full argument itself.

## R08-C — regenerate and reset reviews

After the repaired canonical proof is merged:

- build a new immutable `R08` HTML bundle from one fixed merged snapshot;
- assign a new bundle ID and SHA-256;
- keep R07 immutable;
- carry forward zero R07 verdicts to R08;
- restart independent `CLOSED` count at zero;
- require at least two fresh independent `CLOSED` verdicts and zero unresolved theorem-level or self-containedness blockers before final freeze.

## Contract locks

```text
R08_REQUIRED=true
R08_QR0_DEFINITION_REQUIRED=true
R08_FULL_JACOBI_SUM_EMBED_REQUIRED=true
R08_THEOREM_CHANGE_REQUIRED=false
R07_IMMUTABLE=true
THEOREM_CHANGED=false
```
