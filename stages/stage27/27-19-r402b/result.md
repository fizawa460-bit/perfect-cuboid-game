# Stage27-19-r402b — fixed-tau physical fiber preflight

```text
TASK_ID=Stage27-19-r402b
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
ROUTE_LABEL=FIXED_TAU_PHYSICAL_FIBER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_UPPER_EXPONENT=1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Parent boundary

Stage27-19-r402a passed hostile audit and PR #1038 merged at

```text
e94dd7652c1c60cc32617ff00240f67734d39bed
```

The accepted tau-support corridor remains

\[
B^{1/4}\ll \#\mathcal T(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

and the reduced tau height satisfies

\[
H(\tau)<2B^2.
\]

The height/cardinality route alone did not prove a strict support exponent below `1/2`. This route therefore audits the second r402 interface: fixed-tau physical fibers.

## 2. Exact fixed-tau ambient conic

Write the reduced positive toric slopes as

\[
x=m/n,\qquad y=r/s,
\]

and let a fixed positive tau value be

\[
\tau=t=p/q,\qquad \gcd(p,q)=1,\quad p,q>0.
\]

The hostile-audited r402 identity is

\[
\tau=\frac{x^2+1}{y^2-1}.
\]

Therefore the whole ambient two-face fiber over `t=p/q` satisfies exactly

\[
\boxed{q(x^2+1)=p(y^2-1)}
\]

or equivalently

\[
\boxed{p y^2-q x^2=p+q.}
\]

In homogeneous toric variables this is

\[
\boxed{p n^2(r^2-s^2)=q s^2(m^2+n^2).}
\]

This is the same equality obtained by fixing the r402 outer label. It is a conic condition on the ambient two-face host; it is not yet the integral-space condition.

```text
FIXED_TAU_AMBIENT_CONIC_DERIVED=true
FIXED_TAU_TORIC_EQUATION_DERIVED=true
FIXED_TAU_CONIC_ALONE_IMPLIES_SPACE=false
```

## 3. Integral-space condition restores the genus-one fiber

The Stage19 master receiver is

\[
x^2y^2+1=z^2(x^2+y^2).
\]

For fixed `tau=t`, r401a parametrizes the first conic by

\[
D=u^2-t-1,
\]

\[
z=\frac{t+(u-1)^2}{D},
\qquad
x=\frac{2tu-t-u^2+2u-1}{D},
\]

and the remaining square condition becomes

\[
\boxed{
t V^2=(u^2+t+1)
\Bigl((t+2)u^2-4(t+1)u+(t+1)(t+2)\Bigr).
}
\]

The binary-quartic discriminant is already hostile-audited as

\[
4096\,t^2(t+1)^8.
\]

Every physical tau is positive, so `t!=0,-1`; hence every physical fixed-tau projective fiber is smooth genus one.

The map from a canonical positive Stage19 object to this fiber is finite-to-one with an absolute constant, and on the frozen positive shared-edge chart it is birational away from the already excluded boundary `z=1`.

```text
FIXED_TAU_STAGE19_FIBER_GENUS=1
FIXED_TAU_PHYSICAL_FIBER_SMOOTH=true
FIXED_TAU_PHYSICAL_TO_GENUS_ONE_BOUNDED_MULTIPLICITY=true
```

## 4. Physical cutoff gives polynomial fiber-coordinate height

r402a proves on `R<=B`

\[
m^2+n^2<2B,
\qquad
r^2+s^2<2B,
\qquad
n^2<B,
\qquad
s^2<B.
\]

For a Stage19 survivor,

\[
z^2=
\frac{m^2r^2+n^2s^2}{m^2s^2+n^2r^2}.
\]

Write reduced `z=P/Q>0`. Since the numerator is less than `5B^2` and the denominator is less than `4B^2`, reduction to the rational square gives the safe uniform bound

\[
\boxed{H(z)<3B.}
\]

Also

\[
H(x-1)<\sqrt{2B}.
\]

Because the physical chart excludes `z=1`, the line parameter is

\[
u=\frac{x-1}{z-1}.
\]

Consequently

\[
\boxed{H(u)<5B^{3/2}}
\]

is a safe coarse bound. The remaining coordinate `V=y(u^2-t-1)` is therefore polynomially bounded in `B` for every fixed `t`.

Thus, for each fixed rational `t`, physical points in the `R<=B` fiber land in a projective height ball on the fixed genus-one curve `C_t` whose logarithmic height is `O_t(log B)`.

```text
FIXED_TAU_Z_HEIGHT_BOUND_PROVED=true
FIXED_TAU_Z_HEIGHT_BOUND=H(z)<3B
FIXED_TAU_U_HEIGHT_BOUND_PROVED=true
FIXED_TAU_U_HEIGHT_BOUND=H(u)<5B^(3/2)
FIXED_TAU_PROJECTIVE_HEIGHT_POLYNOMIAL_IN_B=true
```

## 5. Pointwise fixed-tau count

Fix once and for all a rational `t>0`.

If `C_t(Q)` is empty, then the Stage19 physical fiber over `t` is empty. If it is nonempty, choose a rational point; the smooth genus-one curve is then identified with its elliptic Jacobian `E_t` up to a fixed rational translation.

By the standard Mordell-Weil theorem and the positive-definite Neron-Tate height pairing on `E_t(Q)/E_t(Q)_tors`, the rational points with canonical height `O_t(log B)` form lattice points in a Euclidean ball of radius `O_t(sqrt(log B))`. If `r_t=rank E_t(Q)`, this gives

\[
\boxed{
w_B(t)\ll_t (1+\log B)^{r_t/2}=B^{o_t(1)}.
}
\]

The statement is deliberately **pointwise in fixed `t`**. The implied constants, the Mordell-Weil rank, the choice of generators, and the comparison between naive and canonical height may depend on `t`.

```text
POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true
POINTWISE_FIXED_TAU_BOUND=polylog_B_with_t_dependent_rank_and_constant
MORDELL_WEIL_HEIGHT_LATTICE_USED=true
UNIFORM_IN_T=false
```

## 6. Why this is not the uniform max-fiber theorem

The r402 upper interface needs

\[
\max_{t\in\mathcal T(B)} w_B(t)\ll B^{\phi+o(1)}
\]

with a bound uniform as `t` itself varies with `B` through

\[
H(t)<2B^2.
\]

The pointwise theorem above does not supply this. In particular, no repo-native theorem presently bounds uniformly across this moving family all of

- Mordell-Weil rank,
- minimal positive canonical height,
- regulator / generator geometry,
- naive-to-canonical height comparison,
- or the number of rational points in the resulting moving height ball

at the strength required to deduce

\[
\max_{t\in\mathcal T(B)}w_B(t)=B^{o(1)}.
\]

No such uniform statement is inferred from the fixed-curve Mordell-Weil theorem.

```text
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
UNIFORM_MOVING_TAU_RANK_BOUND_PROVED=false
UNIFORM_MOVING_TAU_HEIGHT_LATTICE_BOUND_PROVED=false
POINTWISE_TO_UNIFORM_PROMOTION_FORBIDDEN=true
```

## 7. Fiber-alone cannot break the half-power wall at the present support boundary

Even granting the stronger hypothetical theorem

\[
\max_t w_B(t)=B^{o(1)},
\]

r402 gives only

\[
N_2(B)\le \#\mathcal T(B)\max_t w_B(t).
\]

The best certified support upper from r402a is still

\[
\#\mathcal T(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Hence uniform subpower fibers by themselves would reproduce only

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

not a strict sub-half theorem.

This exactly matches the older checkpoint40 boundary that improving only an already-subpower vertical/elliptic multiplicity cannot remove the horizontal half-power saturation. A fixed-tau theorem becomes exponent-effective only jointly with a strict tau-support upper `sigma<1/2` (or another same-measure horizontal deficit).

```text
FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true
FIBER_PLUS_STRICT_SUPPORT_CAN_REOPEN=true
STRICT_TAU_SUPPORT_STILL_REQUIRED_FOR_MAX_FIBER_ROUTE=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
```

## 8. Next exact route

The first two naive tau-pushforward shortcuts are now separated:

1. raw tau height/cardinality does not give `sigma<1/2` (`r402a`);
2. fixed-tau Mordell-Weil sparsity is only pointwise, and even a hypothetical uniform subpower fiber does not beat half without a strict horizontal support deficit (`r402b`).

The remaining r402-native quantitative object is the exact same-tau collision receiver. The next route `r402c` should audit the actual weighted collision energy / horizontal correlation rather than another pointwise fiber theorem.

It must retain the same physical measure and must not treat tau-cardinality or pointwise Mordell-Weil finiteness as a fixed-power saving.

```text
NEXT_DERIVED_ROUTE=27-19-r402c
NEXT_ROUTE_KIND=TAU_COLLISION_ENERGY_PREFLIGHT
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```