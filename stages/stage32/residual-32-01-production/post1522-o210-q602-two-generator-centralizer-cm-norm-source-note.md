# Stage32 post-1522 O210 Q602 two-generator centralizer / CM-norm route

Scope: fixed recovered V6 class `g1-d186`, `d=186`, `e=266`,
`z=(-15,62,-44,26,32)`, at the retained `O=210`, `Q(T)=602` boundary.
This leaf does **not** prove that the actual correspondence commutes with the
Bolza automorphisms below. It proves that such commutation would already exclude
the residual case, without first proving integral valence.

## Retained source locks

The post-1490 correspondence note identifies the fixed target with the Bolza
curve

`C0 : y^2 = x^5-x`

and source-locks, as an unpolarized complex Abelian variety,

`J(C0) ~= E^2`, `E=C/Z[i*sqrt(2)]`,

hence

`End(J(C0)) ~= M_2(Z[sqrt(-2)])`.

The post-1500 hostile-audit repair fixes

`Tr_Q(T^dagger*T)=2*Q(T)` and `Q(T)=602`.

The post-1521 route proves only the conditional valence exclusion and leaves
the actual valence/symmetry problem open. The Arsenal check in that route is
retained: no registered card directly supplies the missing
correspondence-geometry-to-scalar implication.

## Two explicit Bolza automorphisms

Over `C`, define

`alpha(x,y)=(-x, i*y)`,
`beta(x,y)=(1/x, i*y/x^3)`.

They preserve `C0` exactly:

- for `alpha`,
  `(-x)^5-(-x)=-(x^5-x)=(i*y)^2` on `C0`;
- for `beta`,
  `(1/x)^5-(1/x)=-(x^5-x)/x^6=(i*y/x^3)^2` on `C0`.

On the holomorphic differential basis

`omega1=dx/y`, `omega2=x*dx/y`,

their pullbacks are

`alpha^*(omega1)=i*omega1`,
`alpha^*(omega2)=-i*omega2`,

and

`beta^*(omega1)=i*omega2`,
`beta^*(omega2)=i*omega1`.

Thus their analytic matrices are

`A=diag(i,-i)`,
`B=i*[[0,1],[1,0]]`.

## Exact centralizer lemma

Let the analytic representation of an endomorphism be

`L=[[p,q],[r,s]]`.

From `LA=AL` we obtain `q=r=0`. With `L=diag(p,s)`, the second relation
`LB=BL` gives `p=s`. Therefore

`Cent_{M_2(C)}(A,B) = C * I`.

Consequently, if the actual Stage32 operator

`T=(f1)_*(f2)^*`

commutes with both `alpha_*` and `beta_*` on `J(C0)`, then its analytic
representation is `lambda*I`.

This statement is basis-independent: a scalar matrix remains scalar after
changing from the differential basis above to the source-locked `E^2`
coordinates. Since `T` is an integral endomorphism and

`End(J(C0)) ~= M_2(Z[sqrt(-2)])`,

the scalar lies in the CM order:

`lambda=a+b*sqrt(-2)`, `a,b in Z`.

## CM norm obstruction at Q=602

No product-polarization assumption is needed. For any polarization represented
analytically by a positive Hermitian matrix `H`, the Rosati adjoint of a scalar
matrix is

`(lambda*I)^dagger = H^(-1) * conjugate(lambda*I)^t * H
                    = conjugate(lambda)*I`.

Hence

`T^dagger*T = (a^2+2*b^2) * I`.

On an Abelian surface, the rational trace of multiplication by an integer `n`
is `4*n`. Therefore the retained normalization gives

`2*Q(T) = Tr_Q(T^dagger*T) = 4*(a^2+2*b^2)`,

so

`Q(T)=2*(a^2+2*b^2)`.

At `Q(T)=602`, this requires

`a^2+2*b^2=301`.

But squares modulo eight are `{0,1,4}`, so
`a^2+2*b^2 (mod 8)` lies in `{0,1,2,3,4,6}`, whereas
`301 == 5 (mod 8)`. Contradiction.

Thus:

`[T,alpha_*]=[T,beta_*]=0  =>  Q(T) != 602`.

This strictly weakens the previous sufficient hypothesis "Gamma has integral
valence": CM-scalar endomorphisms are allowed a priori, and the norm congruence
still excludes `Q=602`.

## Decision boundary

PROVED in this leaf:

1. `alpha` and `beta` are exact automorphisms of the fixed Bolza model.
2. Their joint analytic centralizer is scalar.
3. Any integral scalar endomorphism lies in `Z[sqrt(-2)]`.
4. Any such scalar has `Q(T)=2*(a^2+2*b^2)`, so `Q(T)=602` is impossible.
5. Therefore commutation with these **two** automorphisms is sufficient to
   exclude the residual Q602 operator.

NOT proved:

- the actual correspondence `Gamma`, the carrier maps `f1,f2`, or the induced
  `T` commute with `alpha` or `beta`;
- `Gamma` has valence;
- `Q=602` or `O=210` is unconditionally excluded.

The next exact question is therefore smaller than the post-1521 valence
question:

`Does the actual correspondence operator T commute with alpha_* and beta_*?`

Authorized next routes are exact carrier-map equivariance, quotient-normalizer
data, or an exact divisor/correspondence identity that implies these two
commutators vanish.

## Firewalls

- This is a conditional exclusion only; Stage32 stays open.
- O212..266 remain blocked behind O210.
- No Rosati self-adjointness of `T` is assumed.
- No product polarization on `E^2` is assumed.
- Scalar over `C` is not silently replaced by scalar over `Z`; the
  `Z[sqrt(-2)]` source lock is used explicitly.
- No q2/mod3/7-adic route is reopened.
- No numerical Neron-Severi guess is promoted.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
