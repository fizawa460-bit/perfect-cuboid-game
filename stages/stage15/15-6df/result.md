# Stage15-6df — exact moving gcd structure of the double-eliminant sign factors

Base: merged Stage15-6de after fresh audit PASS. Execute the selected `DOUBLE_ELIMINANT_MIXED_FACTOR_INCIDENCE` route before any dispersion promotion.

Keep the exact cross-gcd-cell normal form
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\qquad H=abcd,
\qquad HMNUV\le B,
\]
and the exact survivor equations
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
b^4M^2V^2+c^4N^2U^2=kQ^2.
\]
Put
\[
X=abM,\qquad Y=cdN,\qquad \Delta=X^4-Y^4>0.
\]
The double eliminants are
\[
\Delta U^2=kR_-R_+,
\qquad
R_\pm=b^2MP\pm d^2NQ,
\]
\[
\Delta V^2=kS_-S_+,
\qquad
S_\pm=a^2MQ\pm c^2NP.
\]

## 1. Primitive-coordinate coprimality

The reduced Gaussian coordinates are
\[
\alpha_0=a^2MU+i\,d^2NV,
\qquad
\beta_0=b^2MV+i\,c^2NU.
\]
By the exact cross-gcd normalization they are primitive as rational-coordinate pairs:
\[
\gcd(a^2MU,d^2NV)=1,
\qquad
\gcd(b^2MV,c^2NU)=1.
\]
For a primitive pair `x,y` satisfying `x^2+y^2=kT^2`, every prime dividing `xy` is absent from `kT`, because modulo such a prime the other coordinate is a unit. Hence
\[
\gcd(kP,adMNUV)=1,
\qquad
\gcd(kQ,bcMNUV)=1.
\]
In particular
\[
\boxed{\gcd(k,HMNUV)=1.}
\]
Let
\[
g:=\gcd(P,Q),\qquad P=gp,\quad Q=gq,\quad \gcd(p,q)=1.
\]
Combining the two primitive-coordinate statements gives
\[
\boxed{\gcd(g,HMNUV)=1.}
\]
Thus neither the charged core `k` nor the moving common square factor `g` is hidden in the physical cross-gcd normalizer or residual variables.

## 2. Exact gcd of each sign pair

The coefficient pairs satisfy
\[
\gcd(b^2M,d^2N)=1,
\qquad
\gcd(a^2M,c^2N)=1.
\]
Moreover `P` is coprime to `dN` and `aM`, while `Q` is coprime to `bM` and `cN`. Therefore
\[
\gcd(b^2MP,d^2NQ)=g,
\qquad
\gcd(a^2MQ,c^2NP)=g.
\]
After dividing by `g`, the two summands in each sign pair are coprime. Hence the elementary identity
\[
\gcd(A-B,A+B)\in\{1,2\}\quad\text{when }\gcd(A,B)=1
\]
gives the exact classification
\[
\boxed{\gcd(R_-,R_+)=\varepsilon_R g,\qquad \varepsilon_R\in\{1,2\},}
\]
\[
\boxed{\gcd(S_-,S_+)=\varepsilon_S g,\qquad \varepsilon_S\in\{1,2\}.}
\]
Here `epsilon_R=2` exactly when both `b^2Mp` and `d^2Nq` are odd; otherwise it is `1`. Likewise `epsilon_S=2` exactly when both `a^2Mq` and `c^2Np` are odd. Thus the only bounded exceptional common factor is the explicit parity factor. Every unbounded moving common factor is exactly `g=gcd(P,Q)`.

No bounded-exceptional-support assumption has been made.

## 3. The moving common factor is forced into Delta

Because `R_-R_+` and `S_-S_+` are both divisible by `g^2`, the two eliminants imply
\[
kg^2\mid \Delta U^2,
\qquad
kg^2\mid \Delta V^2.
\]
The residual pair `(U,V)` is primitive, so `gcd(U,V)=1`. Therefore
\[
\gcd(\Delta U^2,\Delta V^2)=\Delta,
\]
and consequently
\[
\boxed{kg^2\mid\Delta.}
\]
Equivalently
\[
\boxed{g^2\mid \Delta/k.}
\]
This absorbs the entire moving common-factor support into an exact square-divisor condition on the already-fixed fourth-power difference. In particular, for fixed cells and `(M,N,k)`, the possible values of `g` are divisor-many.

## 4. Primewise classification and local orientations

Let `ell` be an odd prime dividing `kg`. Since `gcd(kg,HMNUV)=1`, all toric variables are units modulo `ell`. Also `ell` divides both exact norms. The two-channel determinant lock therefore applies without a new adapter: `ell` lies in exactly one legal S/O orientation and necessarily
\[
\ell\equiv1\pmod4.
\]
If
\[
\kappa_\ell=v_\ell(k)\in\{0,1\},
\qquad e_\ell=v_\ell(g),
\]
then the exact square-divisor lock gives
\[
\boxed{v_\ell(\Delta)\ge \kappa_\ell+2e_\ell.}
\]
Thus the moving cases are completely classified:

- `e_ell=0, kappa_ell=1`: charged core only;
- `e_ell>0, kappa_ell=0`: common square factor only;
- `e_ell>0, kappa_ell=1`: charged core plus additional even common valuation;
- `ell=2`: handled only by the explicit `epsilon_R,epsilon_S` parity factors and the already-isolated bounded 2-primary core convention.

There is no additional unclassified moving sign-pair gcd support.

```text
STAGE15_6_SUBSTAGE=6df
STAGE15_6DF_PRIMITIVE_COORDINATE_COPRIMALITY=true
STAGE15_6DF_G=gcd(P,Q)
STAGE15_6DF_G_COPRIME_TO_HMNUV=true
STAGE15_6DF_SIGN_PAIR_GCD_R=epsilon_R*g
STAGE15_6DF_SIGN_PAIR_GCD_S=epsilon_S*g
STAGE15_6DF_EPSILON_IN={1,2}
STAGE15_6DF_MOVING_COMMON_SUPPORT_EXACTLY_G=true
STAGE15_6DF_K_G_SQUARED_DIVIDES_DELTA=true
STAGE15_6DF_ODD_KG_PRIMES_HAVE_LEGAL_SO_ORIENTATION=true
STAGE15_6DF_BOUNDED_EXCEPTIONAL_SUPPORT_ASSUMED=false
STAGE15_6DF_EXIT=NORMALIZED_DOUBLE_FACTOR_SPARSITY_TEST_READY
```