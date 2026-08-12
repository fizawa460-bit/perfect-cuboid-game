# Stage15-6ad — low-core one-square reconstruction audit

Base: merged Stage15-6ac (`PR #835`, merge commit `815d23c`). Stage15-6ac reduced every low-core physical fiber, after the already-legal outer/core/cross-gcd/orientation charges, to

\[
\alpha_0=K_\alpha z^2,
\qquad
\beta_0=K_\beta w^2,
\]

where the finite unit choice has been absorbed into the fixed Gaussian cores `K_alpha,K_beta`,

\[
\alpha_0=\frac{mr+i\,ns}{h_\alpha},
\qquad
\beta_0=\frac{ms+i\,nr}{h_\beta},
\]

and `N(K_alpha)=N(K_beta)=k=2^eta q`.

Stage15-6ad performs the required AR-010-style reconstruction audit. It does **not** open a genus-one/character route and does **not** derive a new global thinning exponent.

## 1. Frozen verdict

After fixing

```text
outer pair (m,n)
charged core/orientation (K_alpha,K_beta)
cross-gcd labels h_alpha,h_beta
dyadic/physical chamber decorations
```

the two Gaussian square parameters are **not independent**.

For every candidate `z`, the first lift

\[
K_\alpha z^2=X+iY
\]

forces

\[
\boxed{
 r=\frac{h_\alpha X}{m},
 \qquad
 s=\frac{h_\alpha Y}{n}.
}
\]

Hence `(r,s)` is unique if the displayed divisibilities, positivity, primitiveness, dyadic box and physical filters hold. Those conditions only reject candidates.

The same reconstructed `(r,s)` then forces

\[
\boxed{
W_z:=\frac{ms}{h_\beta}+i\frac{nr}{h_\beta}
=K_\beta w^2.
}
\]

Thus `w^2` is uniquely determined by `z`:

\[
\boxed{
w^2=W_z/K_\beta.
}
\]

If the quotient is not an integral Gaussian square, the candidate `z` is rejected. If it is a nonzero square, `w` has only the two roots `+w,-w`. Finite unit conventions were already charged in `K_beta`.

Therefore

```text
LOW_CORE_SECOND_GAUSSIAN_PARAMETER_INDEPENDENT=false
FIXED_z_COMPLETION_FIBER=O(1)
```

and symmetrically a fixed `w` determines `z` up to the same finite square-root ambiguity.

This is the exact Stage15 realization of the reconstruction principle behind Arsenal AR-010: retaining both original coupled equations removes a fake second support variable.

## 2. Exact anti-linear transfer identity

The reconstruction can be written without first naming `r,s`. Put

\[
H_+=m^2+n^2,
\qquad
H_-=m^2-n^2,
\]

and write

\[
\alpha_0=K_\alpha z^2.
\]

From

\[
\Re\alpha_0=\frac{mr}{h_\alpha},
\qquad
\Im\alpha_0=\frac{ns}{h_\alpha},
\]

one obtains exactly

\[
\beta_0
=\frac{i h_\alpha}{2mn h_\beta}
\left(
H_+\overline{\alpha_0}-H_-\alpha_0
\right).
\]

Substituting both square lifts gives the single exact transfer equation

\[
\boxed{
2mn h_\beta K_\beta w^2
=
i h_\alpha
\left(
H_+\overline{K_\alpha z^2}
-H_-K_\alpha z^2
\right).
}
\]

Call the right-hand side

\[
\mathcal T_{m,n,h_\alpha}(K_\alpha z^2).
\]

For fixed charged data, this is an anti-linear integral expression in `z^2` and `conjugate(z)^2`. Consequently the full four-real-variable receiver from 6ac is equivalent to **one primitive Gaussian parameter `z` plus the requirement that one explicit anti-linear transfer value be a fixed-core Gaussian square**.

The symmetric identity obtained by exchanging `alpha` and `beta` shows that neither square parameter has privileged independent status.

## 3. Primitivity of the surviving square parameter

Stage15-6ac made `alpha_0` primitive as a Gaussian integer in the rational-coordinate sense:

\[
\gcd(\Re\alpha_0,\Im\alpha_0)=1.
\]

If a rational prime divided both coordinates of `z=a+ib`, then it would divide both coordinates of `K_alpha z^2`, contradicting the primitivity of `alpha_0`. Hence

\[
\boxed{\gcd(a,b)=1.}
\]

Likewise `w=c+id` is primitive.

Thus Stage15-6ad does not replace the low-core receiver by an unrestricted Gaussian square variable. The remaining host is a primitive binary pair with all original physical post-filters retained.

## 4. Polynomial size and finite-fiber legality

Stage15-6ab proved from the physical inverse and `R<=B` that

\[
m,r\le2B,
\qquad
n,s\le B.
\]

Hence

\[
|\alpha_0|\le |mr+i ns|\ll B^2.
\]

Since

\[
|\alpha_0|=|K_\alpha|\,|z|^2=\sqrt{k}\,|z|^2,
\]

we have

\[
|z|\ll B,
\]

and similarly `|w|<<B`. All reconstruction integers remain polynomially bounded in the physical height. Therefore the finite square-root/unit fibers are legitimate `B^o(1)` decorations under AR-016; they are not a new density saving.

## 5. Expanded real reconstruction

Write

\[
K_\alpha=A+iB,
\qquad z=a+ib.
\]

Define

\[
F_\alpha=A(a^2-b^2)-2Bab,
\]

\[
G_\alpha=B(a^2-b^2)+2Aab.
\]

Then

\[
\boxed{
mr=h_\alpha F_\alpha,
\qquad
ns=h_\alpha G_\alpha.
}
\]

Thus one `(a,b)` fixes `r,s` exactly when

```text
m | h_alpha F_alpha
n | h_alpha G_alpha
r>0, s>0
```

and the reconstructed pair passes the original physical masks.

For

\[
K_\beta=C+iD,
\qquad w=c+id,
\]

define `F_beta,G_beta` analogously. The other two equations are

\[
ms=h_\beta F_\beta,
\qquad
nr=h_\beta G_\beta.
\]

After `(r,s)` has been reconstructed from `z`, these equations do not create an independent `(c,d)` support. They simply test whether the already-fixed Gaussian integer

\[
\frac{ms}{h_\beta}+i\frac{nr}{h_\beta}
\]

lies in `K_beta * Z[i]^2`.

Equivalently the two cross-equations

\[
n h_\alpha F_\alpha=m h_\beta G_\beta,
\]

\[
m h_\alpha G_\alpha=n h_\beta F_\beta
\]

are reconstruction equations, not two independent quadratic families to be multiplied together.

## 6. AR-010 verdict

Arsenal AR-010 has the trigger signature:

> a generic higher-complexity receiver appears only because a moving coefficient/opposite pair was frozen and counted independently, while the original coupled equations reconstruct it.

The Stage14 reciprocal formulas are not literally the Stage15 formulas, so the Stage14 `B^o(1)` theorem is **not** cross-promoted verbatim. Instead Stage15-6ad proves an exact Stage15 adapter:

```text
AR-010=RECONSTRUCTION_FIREWALL_TRIGGERED_STAGE15_EXACT_ADAPTER_PROVED
```

The adapter is stronger than merely divisor-many completion at this point:

```text
fixed charged data + fixed z
-> unique candidate (r,s)
-> unique candidate w^2
-> at most O(1) w
```

The symmetric statement holds with `z,w` exchanged.

Consequences:

1. no independent `w` dyadic support may be charged after `z` is counted;
2. no independent genus-one coefficient may be introduced from `w` before applying the transfer identity;
3. no extra CRT/root-orientation saving may be charged after the same core/orientation has already been consumed;
4. a future count must act on the **single-square anti-linear transfer condition**, not on a product of two separate Gaussian-square counts.

## 7. What is and is not counted now

The low-core problem has now been reduced to

\[
\boxed{
K_\alpha z^2\ \xrightarrow{\text{physical reconstruction}}\ (r,s)
\ \xrightarrow{}\
W_z,
\qquad
W_z/K_\beta\in\mathbf Z[i]^2.
}
\]

This is a one-primitive-pair receiver.

Stage15-6ad does **not** prove a sharp count for the remaining `z`. In particular it does not prove:

- low-core negligibility;
- a low-core square-root bound;
- a self-contained rederivation of the Stage15-5 half-power survival theorem;
- a strict sub-square-root numerator bound;
- a matching survival exponent;
- a genus-one theorem or character-sum theorem for the transfer condition.

The point of this substage is to remove the false second support before any such theorem is considered.

## 8. Arsenal accounting after reconstruction

```text
AR-010=RECONSTRUCTION_FIREWALL_TRIGGERED_STAGE15_EXACT_ADAPTER_PROVED
AR-016=DIRECT_REUSE_FOR_FINITE_SQRT_UNIT_FIBERS
AR-017=GAUSSIAN_CORE_SQUARE_RECEIVER_RETAINED
AR-018=CORE_ORIENTATION_ALREADY_CONSUMED
AR-023=MEASURE_FIREWALL_PASS
AR-024=MEASURE_FIREWALL_PASS
AR-028=NO_DOUBLE_CHARGE_PASS
AR-012=NOT_TRIGGERED
AR-013=NOT_TRIGGERED
AR-014=NOT_NEEDED
```

AR-012 remains untriggered because there are still no two fixed reciprocal signed difference-of-squares right-hand sides. AR-013 remains untriggered because no post-reconstruction CRT lift variable has appeared. The only surviving arithmetic question is the anti-linear fixed-core Gaussian-square test on one primitive `z`.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ad
STAGE15_6AD_STARTING_GATE=AR010_RECONSTRUCTION_AUDIT_LOW_CORE_SQUARE_RECEIVER
STAGE15_6AD_ONE_SQUARE_RECONSTRUCTION=true
STAGE15_6AD_FIXED_Z_RECONSTRUCTS_RS=true
STAGE15_6AD_FIXED_Z_RECONSTRUCTS_W_SQUARED=true
STAGE15_6AD_FIXED_Z_W_FIBER=O(1)
STAGE15_6AD_SECOND_GAUSSIAN_PARAMETER_INDEPENDENT=false
STAGE15_6AD_ANTILINEAR_TRANSFER_IDENTITY=true
STAGE15_6AD_REMAINING_PARAMETER_PRIMITIVE=true
STAGE15_6AD_AR010_EXACT_STAGE15_ADAPTER=true
STAGE15_6AD_AR012_TRIGGERED=false
STAGE15_6AD_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AD_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AD_STAGE15_5_REPROVED=false
STAGE15_6AD_EXIT=LOW_CORE_ONE_SQUARE_TRANSFER_RECEIVER_READY
```

## 10. Next narrow gate

Stage15-6ae should analyze the remaining **single primitive Gaussian square transfer**

\[
2mn h_\beta K_\beta w^2
=
i h_\alpha
\left(
H_+\overline{K_\alpha z^2}-H_-K_\alpha z^2
\right)
\]

as a counting receiver in the exact physical outer fiber. Before opening a new analytic route, search the Arsenal by this trigger signature: one primitive binary pair, fixed polynomial coefficients, an anti-linear combination of a square and its conjugate, and a fixed-core Gaussian-square target.

Stage15-6ad stops here.