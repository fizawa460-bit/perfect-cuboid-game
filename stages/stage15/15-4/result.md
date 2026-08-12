# Stage15-4 — minimal exact normal form for the integral space diagonal

Base: merged Stage15-3 (`PR #829`) and merged Stage14 Arsenal (`PR #830`). This stage stops after fixing the exact arithmetic normal form for `R in Z`, matching its trigger signature against the Arsenal, and deciding whether Stage15-5 is ready to begin. It does **not** execute a survival/thinning proof.

## 1. Frozen verdict

For the positive shared-edge toric coordinates `(m:n),(r:s)`, define

\[
A=m^2r^2+n^2s^2=N(mr+i\,ns),
\qquad
B=m^2s^2+n^2r^2=N(ms+i\,nr).
\]

Then the integral-space-diagonal condition is exactly

\[
\boxed{R\in\mathbf Z\iff AB\text{ is a square}\iff \operatorname{sf}(A)=\operatorname{sf}(B).}
\]

Here `sf` is the positive squarefree kernel. Equivalently there is a unique squarefree integer `k>0` and positive integers `P,Q` such that

\[
\boxed{A=kP^2,\qquad B=kQ^2.}
\]

This is the Stage15-4 **minimal exact normal form**. It is a paired Gaussian-norm squareclass-coincidence condition. The raw toric space diagonal is then

\[
D_{\rm raw}=2kPQ.
\]

The squarefree core `k` is supported only on `2` and primes `p=1 mod 4`.

```text
STAGE15_4_MINIMAL_EXACT_NORMAL_FORM=PAIRED_GAUSSIAN_NORM_SQUARECLASS_COINCIDENCE
STAGE15_4_NORMAL_FORM_FIXED=true
STAGE15_4_NORMAL_FORM_EQUATION=sf(N(mr+i*ns))=sf(N(ms+i*nr))
STAGE15_4_UNIQUE_SQUAREFREE_CORE=true
STAGE15_4_AUTOCONTINUE_TO_5=false
STAGE15_5_READY_WITH_ARSENAL=true
STAGE15_5_DIRECT_SAVING_WEAPON_IDENTIFIED=false
STAGE15_5_SURVIVAL_PROOF_STARTED=false
```

`STAGE15_5_READY_WITH_ARSENAL=true` means the exact Stage15 obstruction is now fixed and the merged Arsenal has concrete trigger matches with explicit adapter requirements. It does **not** mean that the thinning theorem is already proved or that any Stage14 saving can be cross-promoted directly.

## 2. Exact ambient toric coordinates and inverse

Use the Stage15-2a toric parametrization

\[
\begin{aligned}
E&=4mnrs,\\
X&=2rs(m^2-n^2),\\
Y&=2mn(r^2-s^2),\\
U&=2rs(m^2+n^2),\\
V&=2mn(r^2+s^2).
\end{aligned}
\]

Take coprime positive pairs

\[
m>n>0,\qquad r>s>0,
\]

and let

\[
G=\gcd(E,X,Y)=\gcd(E,X,Y,U,V).
\]

The primitive physical shared-edge incidence is

\[
(e,x,y,u,v)=\frac1G(E,X,Y,U,V).
\]

The positive chamber additionally imposes `x<y`; the physical exactly-two population imposes that `x^2+y^2` is not a square. The canonical position of `e` among the three edges determines the Stage15 direction `a,b,c`.

The toric parameters are not merely a cover with uncontrolled multiplicity. From a primitive physical incidence one recovers them uniquely by

\[
\frac mn=\frac{u+x}{e},
\qquad
\frac rs=\frac{v+y}{e},
\]

reduced to coprime positive numerator/denominator pairs. Indeed

\[
\frac{m^2-n^2}{2mn}=\frac xe,
\qquad
\frac{m^2+n^2}{2mn}=\frac ue,
\]

and likewise for `(r,s)` and `(y,v)`.

Thus, after choosing the unique shared edge and `x<y`, the positive toric parameter pair is unique. No extra Stage15-4 parameter multiplicity is being hidden in the normal form.

## 3. Derivation of the space-diagonal identity

The raw squared geometric height is

\[
R_{\rm raw}^2=E^2+X^2+Y^2.
\]

Direct expansion gives

\[
\begin{aligned}
E^2+X^2+Y^2
&=4\bigl(m^2r^2+n^2s^2\bigr)
       \bigl(m^2s^2+n^2r^2\bigr)\\
&=4AB.
\end{aligned}
\]

Since the physical primitive coordinates are obtained by division by `G`,

\[
G^2R^2=4AB.
\]

Because `G^2` and `4` are squares,

\[
R\in\mathbf Z
\iff 4AB\in\mathbf Z^2
\iff AB\in\mathbf Z^2.
\]

If `4AB=T^2`, then `G^2|T^2`, hence `G|T`; so the implication back to an integral primitive space diagonal has no divisibility gap.

## 4. Minimal squareclass form

For a positive integer `n`, let

\[
\operatorname{sf}(n)=\prod_{v_p(n)\text{ odd}}p.
\]

The product `AB` is a square exactly when the prime-valuation parity vectors of `A` and `B` agree. Hence

\[
AB\in\mathbf Z^2
\iff \operatorname{sf}(A)=\operatorname{sf}(B).
\]

Let their common squarefree kernel be `k`. Then uniquely

\[
A=kP^2,\qquad B=kQ^2,
\]

and

\[
R_{\rm raw}=2kPQ.
\]

This is more informative than the quartic equation `4AB=D^2` and smaller than introducing a new high-dimensional auxiliary variety: the extra condition is one equality of two rational norm squareclasses.

The equivalent quotient form is

\[
\frac{A}{B}\in\mathbf Q^{\times2}.
\]

The squarefree-core form is frozen as canonical because it exposes the arithmetic object that Stage15-5 must count.

## 5. Gaussian interpretation

Set

\[
\alpha=mr+i\,ns,
\qquad
\beta=ms+i\,nr.
\]

Then

\[
A=N(\alpha),\qquad B=N(\beta),
\]

so the Stage15 survivor condition is

\[
\boxed{\operatorname{sf}(N\alpha)=\operatorname{sf}(N\beta).}
\]

For any prime `p=3 mod 4`, its valuation in a Gaussian norm is even. Therefore the common squarefree core satisfies

\[
\operatorname{supp}(k)\subseteq\{2\}\cup\{p:p=1\pmod4\}.
\]

This is consistent with the Stage15-3 local exclusion. The important distinction is that Stage15-4 has now identified the exact moving object: not a random integer square test, but equality of the squareclasses of two coupled Gaussian norms.

## 6. Secondary exact identities

The two norm factors also obey

\[
A+B=(m^2+n^2)(r^2+s^2),
\]

and

\[
A-B=(m^2-n^2)(r^2-s^2).
\]

On survivors this becomes

\[
k(P^2+Q^2)=(m^2+n^2)(r^2+s^2),
\]

\[
k(P^2-Q^2)=(m^2-n^2)(r^2-s^2).
\]

These identities are retained for Stage15-5 reconstruction attempts, but they are **not** promoted to the canonical normal form. Their right-hand sides are still moving with both toric pairs, so they do not yet instantiate Stage14's fixed reciprocal difference-of-squares receiver.

## 7. Physical filters and multiplicity

The normal form is imposed on the ambient positive shared-edge surface before the final physical filters. The map back to Stage15 objects preserves the required conventions as follows.

1. **Primitivity:** divide the raw toric coordinates by their common gcd `G`; this is exact and does not alter whether `AB` is square because the height changes by the square factor `G^2`.
2. **Canonical ordering:** choose the unique shared edge `e`; order the other edges by `x<y`; then sort `(e,x,y)` only for the canonical physical label. No arithmetic multiplicity is introduced.
3. **Exactly two faces:** the toric surface supplies the two faces through `e`; the condition `x^2+y^2` nonsquare is retained as an explicit post-filter. Triple-face objects are not folded into `M_2`.
4. **Direction:** the three chambers `e<x<y`, `x<e<y`, `x<y<e` are retained separately if a directional statement is attempted.
5. **Height:** the exact Stage15 cutoff is the primitive `R<=B`; the raw toric height is `GR`, so no raw-parameter box may be silently substituted for the physical height measure.

Therefore the normal form is exact for `A_2 subset B_2`, but any Stage15-5 count must retain the physical outer measure rather than count unrestricted `(m,n,r,s)` boxes and identify them with `M_2(B)`.

## 8. Stage14 Arsenal trigger-signature match

The merged Arsenal is now authoritative. The exact normal form changes several entries from “inspect after Stage15-4” into concrete classifications.

### 8.1 Triggered, exact adapter still required

**AR-017 — Gaussian quotient and cross-resultant dictionary: `TRIGGERED_ADAPTER_REQUIRED`.**

The normal form contains two explicit Gaussian quadratic values `alpha,beta` and a common rational norm squareclass `k`. This is the closest structural match. However Stage15 has not yet produced a **fixed Gaussian divisor** `Pi_C` with a proved charged measure. Stage15-5 may use AR-017 only after defining which Gaussian prime orientations belong to fixed common-core data and which are generated by the point. No root modulus may be recharged merely because it divides `N(alpha)` or `N(beta)`.

**AR-009 — primitive Gaussian root-line lattice count: `TRIGGERED_ADAPTER_REQUIRED`.**

The common core is supported on `1 mod 4` primes and the norms are sums of two squares, but the current normal form is an equality of squareclasses, not yet a congruence

`C0 | a0^2 U^2 + b0^2 V^2`

with primitive `(U,V)`, fixed `C0`, unit coefficients, and a fixed root orientation. Stage15-5 must derive that exact root-line shape before using the spacing bound.

**AR-018 — Gaussian squareclass orientation split: `LOCAL_TRIGGER_ADAPTER_REQUIRED`.**

The squarefree `k` admits primewise Gaussian orientations. What is missing is the Stage14 Cayley structure giving simultaneous `M-N` / `M+N` divisibilities. The orientation bookkeeping is relevant; the Stage14 saving is not directly reusable.

### 8.2 Direct proof-accounting tools

**AR-016 — divisor/finite-fiber adapter: `DIRECT_REUSE`.** Any fixed factorization or finite Gaussian orientation fiber may cost `B^o(1)` after its outer data are fixed. This is multiplicity only, never the thinning saving.

**AR-023 / AR-024 — measure firewalls: `DIRECT_REUSE`.** The natural host is the coupled toric pair `((m,n),(r,s))` with physical filters. Replacing it by `A`, `B`, `AB`, or `k` is not measure-preserving merely because factorization fibers are divisor-many. A familiar Stage14 kernel does not transfer its saving unless the Stage15 ambient/survivor measure is explicitly preserved.

**AR-028 — no-double-charge ledger: `DIRECT_REUSE`.** Once `k` or a Gaussian divisor of `k` is charged as common-core data, prime/root orientation derived from the same point cannot be charged again as independent spacing.

**AR-026 / AR-027 — target-class and average-to-pointwise firewalls: `DIRECT_REUSE_IF_ANALYTIC_ROUTE_APPEARS`.** A character second moment or an averaged modulus theorem will not by itself prove survival/thinning in every charged Stage15 packet.

### 8.3 Not triggered by the minimal normal form

**AR-012 — reverse reciprocal difference-of-squares: `NOT_TRIGGERED`.** The identities involving `P^2-Q^2` have moving right-hand sides and no two-stage reciprocal reconstruction. Do not force this weapon onto Stage15 merely because a difference of squares appears.

**AR-013 — CRT lift filter: `NOT_TRIGGERED`.** No independent Stage15 CRT lift has yet appeared.

**AR-014 — fixed-outer gcd square-divisor adapter: `WATCH_AFTER_CORE_DECOMPOSITION`.** The common squarefree `k` divides both norms, but this is not the AR-014 hypothesis `h^2|W` with `W` fixed before the counted pair. A separate square-divisor lock must be proved.

**AR-010 — primitive-ratio reconstruction: `WATCH_IF_GENUS_ONE_ROUTE_APPEARS`.** No coefficient should be frozen as independent before checking whether the two norm equations reconstruct it.

AR-007/008/015/019/020/021/022/025 are not activated by the Stage15-4 minimal normal form. No MAIN/T/S route is restarted.

## 9. Stage15-5 readiness

The exact normal form and Arsenal trigger map are sufficient to start Stage15-5 cleanly without rereading Stage14 history:

```text
STAGE15_5_READY_WITH_ARSENAL=true
STAGE15_5_STARTING_NORMAL_FORM=sf(N(mr+i*ns))=sf(N(ms+i*nr))
STAGE15_5_PRIMARY_ARSENAL_CANDIDATES=AR-017,AR-009,AR-018
STAGE15_5_DIRECT_ACCOUNTING_TOOLS=AR-016,AR-023,AR-024,AR-028,AR-026,AR-027
STAGE15_5_AR012_TRIGGERED=false
STAGE15_5_DIRECT_SAVING_WEAPON_IDENTIFIED=false
STAGE15_5_SURVIVAL_PROOF_STARTED=false
```

The first Stage15-5 question should therefore be narrowly phrased: can the common squarefree norm core `k` be decomposed into a **fixed, charged Gaussian common core** plus primitive residual variables in a way that preserves the physical toric-pair measure? Only after that adapter is exact should AR-017 or AR-009 be invoked.

Stage15-4 stops here, as required.
