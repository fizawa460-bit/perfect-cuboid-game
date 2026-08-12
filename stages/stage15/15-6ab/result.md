# Stage15-6ab — measure-preserving charge of the moving two-channel core

Base: merged Stage15-6aa (`PR #833`, merge commit `c80e24c`). Stage15-6aa proved the exact odd-core split

\[
k^\circ=k_Sk_O,
\]

with

\[
k_S\mid m^2+n^2,\qquad k_S\mid r^2-s^2,
\]

and

\[
k_O\mid m^2-n^2,\qquad k_O\mid r^2+s^2.
\]

Its only open gate was whether the moving pair `(k_S,k_O)` can be fixed and charged before root-line counting without changing the physical Stage15 `R<=B` measure. Stage15-6ab closes that gate. It does **not** derive a new thinning exponent.

## 1. Frozen verdict

For every physical exactly-two survivor with `R<=B`, use the unique Stage15-4 inverse

\[
\frac mn=\frac{u+x}{e},\qquad
\frac rs=\frac{v+y}{e}
\]

in lowest terms. Fix the first toric pair `(m,n)` as outer data.

Then the actual odd channel core satisfies

\[
\boxed{k_S\mid H_+(m,n):=m^2+n^2,}
\]

\[
\boxed{k_O\mid H_-(m,n):=m^2-n^2.}
\]

Because `(m,n)=1`,

\[
\gcd(H_+,H_-)\mid2,
\]

so their odd parts are coprime. Thus every actual `(k_S,k_O)` lies in the fixed outer candidate set

\[
\mathscr K(m,n)=
\{(d_+,d_-):d_+\mid H_+,\ d_-\mid H_-,\ d_+,d_-\text{ squarefree odd and supported on }p\equiv1\pmod4\}.
\]

The crucial point is that this set is divisor-many **after the physical outer pair has been fixed**.

```text
STAGE15_6_SUBSTAGE=6ab
STAGE15_6AB_OUTER_PAIR=(m,n)
STAGE15_6AB_CORE_CANDIDATE_SET_FIXED_FROM_OUTER=true
STAGE15_6AB_GLOBAL_CORE_CHARGE_PROVED=true
STAGE15_6AB_PHYSICAL_MEASURE_ADAPTER_PROVED=true
STAGE15_6AB_AR009_FIBERWISE_GLOBALIZATION_LEGAL=true
STAGE15_6AB_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AB_EXIT=MOVING_CORE_CHARGED_ROOT_SPACING_READY
```

## 2. Physical height gives polynomial parameter bounds

A physical shared-edge incidence has positive integers

\[
e,x,y,u,v
\]

with

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2,
\qquad R^2=e^2+x^2+y^2\le B^2.
\]

Hence

\[
e,x,y,u,v\le B.
\]

Reducing `(u+x)/e` to `m/n` gives

\[
\boxed{m\le u+x\le2B,\qquad n\le e\le B.}
\]

Likewise

\[
\boxed{r\le v+y\le2B,\qquad s\le e\le B.}
\]

Therefore

\[
H_+=m^2+n^2\le5B^2,
\qquad
0<H_-=m^2-n^2<4B^2.
\]

In particular every outer host used to choose the moving core is polynomially bounded in the **physical** height. This is not a raw toric-box substitution; it is a consequence of the exact inverse on each physical object.

## 3. The moving core costs only `B^o(1)` per physical outer pair

For fixed `(m,n)`,

\[
\#\mathscr K(m,n)
\le \tau(H_+)\tau(H_-).
\]

By Arsenal AR-016, since `H_+,H_-<=B^O(1)`, uniformly

\[
\boxed{\#\mathscr K(m,n)=B^{o(1)}.}
\]

The 2-primary flag `eta in {0,1}` costs only an absolute factor two.

This is the desired **core charge**. The pair `(k_S,k_O)` is no longer a free whole-family variable. It is a divisor-many decoration of an already fixed physical outer pair.

The order of quantifiers is essential:

```text
physical object
-> unique toric pair ((m,n),(r,s))
-> fix outer (m,n)
-> choose/label actual (k_S,k_O) among B^o(1) outer divisors
-> count the inner primitive pair (r,s)
```

Reversing this order and summing unrestricted cores before fixing a physical outer pair is not licensed.

## 4. Exact disintegration of the physical measure

Let `P_B` be the physical Stage15 survivor population in one chosen shared-edge chamber, retaining

- positivity;
- primitive canonical box convention;
- the unique shared-edge representation;
- `R<=B`;
- exactly-two postfilter `x^2+y^2` nonsquare;
- the chosen direction chamber.

The Stage15-4 inverse maps each object of `P_B` to one unique pair `((m,n),(r,s))`. Therefore the count disintegrates exactly as

\[
\#P_B
=
\sum_{(m,n)}
\#\mathcal F_B(m,n),
\]

where `F_B(m,n)` is the set of inner primitive pairs `(r,s)` that reconstruct physical objects satisfying all the original filters.

Now partition each exact fiber by its **actual** channel core:

\[
\mathcal F_B(m,n)
=
\bigsqcup_{(k_S,k_O)\in\mathscr K(m,n)}
\mathcal F_B(m,n;k_S,k_O).
\]

Some candidate labels may be empty. The nonempty exact fibers are disjoint because the Stage15-4 squarefree core and the Stage15-6aa channel assignment are unique.

Thus fixing the core does not scalarize the population and does not replace the outer pair measure. This is the required AR-023/024 firewall pass.

## 5. Inner root-line form after the core is charged

Fix one outer pair `(m,n)` and one candidate label `(k_S,k_O)` that occurs on a survivor. Put

\[
q=k_Sk_O.
\]

Stage15-6aa gives, for the inner primitive pair,

\[
r^2\equiv s^2\pmod{k_S},
\qquad
r^2\equiv-s^2\pmod{k_O},
\]

and every odd prime of `q` is a unit on `rs`.

For a fixed primewise orientation this is equivalent to

\[
r\equiv\rho s\pmod q,
\]

where

\[
\rho^2\equiv1\pmod{k_S},
\qquad
\rho^2\equiv-1\pmod{k_O}.
\]

There are at most

\[
2^{\omega(q)}=B^{o(1)}
\]

such CRT roots. The `k_O` part is exactly the Gaussian root-line mechanism of AR-009; the `k_S` part is the elementary diagonal `+/-1` line. CRT combines them into one primitive root line modulo `q`.

Because `q|H_+H_-=m^4-n^4` and `m<=2B`,

\[
q\le20B^4,
\]

so all orientation counts remain subpolynomial.

## 6. AR-009 is now legal fiberwise on the whole physical family

The inner physical fiber is curved by the condition `R<=B`, but this causes no measure problem for an upper bound. From Section 2,

\[
1\le s<r\le2B.
\]

Partition this rectangle into `O((log B)^2)=B^o(1)` dyadic boxes. Intersecting each box with the exact physical fiber only removes points.

For a box `r~R_0`, `s~S_0`, fixed `(m,n)`, fixed `(k_S,k_O)`, and fixed CRT orientation, the primitive root-line lattice estimate underlying AR-009 gives

\[
\boxed{
\#\{(r,s)\text{ in the box on the line}\}
\ll 1+\frac{R_0S_0}{q}.
}
\]

The fixed outer core choices, root orientations, 2-primary decoration, and dyadic boxes together cost only `B^o(1)`.

Therefore AR-009 has advanced from the Stage15-6aa status

```text
EXACT_LOCAL_ADAPTER_PROVED_GLOBAL_CHARGE_OPEN
```

to

```text
AR-009=FIBERWISE_GLOBALIZATION_LEGAL_AFTER_OUTER_CORE_CHARGE
```

This statement is about legality and multiplicity. It is **not** yet a whole-family fixed-power saving.

## 7. Why no causal exponent is claimed yet

The root-line bound contains

\[
1+\frac{R_0S_0}{q}.
\]

A large modulus `q` gives genuine spacing. A small modulus does not. Stage15-6ab has proved that summing over possible `q` costs only `B^o(1)` per outer pair, but it has **not** proved that the physical survivor mass is concentrated on sufficiently large `q`.

In particular, the low-core region, including `q=1`, cannot be discarded merely because the core is now chargeable.

Hence none of the following is proved here:

- a self-contained rederivation of the Stage15-5 half-power thinning;
- a lower bound on `q` for every survivor;
- negligibility of the low-core branch;
- a strict sub-square-root numerator bound;
- a matching survival exponent.

The exact next obstruction is now isolated: **core size versus physical inner support**.

## 8. Arsenal accounting

### AR-016 — direct reuse

`H_+` and `H_-` are fixed polynomially bounded positive integers after `(m,n)` is fixed. Therefore divisor-many core labels cost `B^o(1)` exactly as AR-016 permits.

### AR-009 — whole-family fiberwise adapter completed

The Gaussian root component was proved in 6aa. Stage15-6ab supplies the missing charge order and physical fiber disintegration. The elementary `+/-1` component is combined by CRT. No Stage14 exponent is imported.

### AR-017 — legal only after the same core charge

Once `(m,n;k_S,k_O)` and Gaussian orientations are fixed, the Stage15-6aa Gaussian divisor `Pi_alpha` is now fixed before the inner pair is counted. The AR-017 quotient dictionary is therefore legally available inside that fiber. It is not counted as an additional modulus after the same core has already been charged.

### AR-023 / AR-024 — firewall pass

No replacement by a scalar host `H_+H_-`, `q`, or `k` is made. Those integers only label subfibers of the original physical outer-pair count.

### AR-028 — no-double-charge pass

The cost of `(k_S,k_O)` is paid once as a divisor decoration of `(m,n)`. Its Gaussian orientations and CRT roots are finite/subpolynomial decorations of that same charge, not independent density savings.

### AR-014 — still not needed

The counted inner pair `(r,s)` is primitive. No new nonprimitive common-gcd loss has appeared, so AR-014 remains a watch item rather than an active ingredient.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ab
STAGE15_6AB_STARTING_GATE=MOVING_CORE_CHARGE_ON_PHYSICAL_MEASURE
STAGE15_6AB_PHYSICAL_PARAMETER_POLYNOMIAL_BOUND=true
STAGE15_6AB_OUTER_HOSTS=HPLUS=m^2+n^2,HMINUS=m^2-n^2
STAGE15_6AB_CORE_CANDIDATE_COUNT=B^o(1)_PER_OUTER_PAIR
STAGE15_6AB_GLOBAL_CORE_CHARGE_PROVED=true
STAGE15_6AB_PHYSICAL_MEASURE_DISINTEGRATION_PROVED=true
STAGE15_6AB_MIXED_CRT_ROOT_LINE_PROVED=true
STAGE15_6AB_AR009_FIBERWISE_GLOBALIZATION_LEGAL=true
STAGE15_6AB_AR017_CHARGE_ORDER_LEGAL=true
STAGE15_6AB_AR023_FIREWALL_PASS=true
STAGE15_6AB_AR024_FIREWALL_PASS=true
STAGE15_6AB_AR028_NO_DOUBLE_CHARGE_PASS=true
STAGE15_6AB_LOW_CORE_NEGLIGIBLE_PROVED=false
STAGE15_6AB_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AB_STAGE15_5_REPROVED=false
STAGE15_6AB_EXIT=MOVING_CORE_CHARGED_ROOT_SPACING_READY
```

## 10. Next narrow gate

The next Stage15-6 substage should quantify the modulus actually available to the root-line bound:

> after the legal outer-pair/core disintegration, can the physical population be split into a high-core region where `q=k_Sk_O` supplies a provable spacing saving and a low-core region that is controlled by a different exact mechanism?

No new Stage14 route is needed until that high-core/low-core dichotomy is written in the physical measure.