# Stage15-6aa — odd common-core two-channel adapter

Base: merged Stage15-5 (`PR #832`, merge commit `8b522fd`). Stage15-6 is the causal-mechanism phase. This first substage does **not** try to re-prove the Stage15-5 half-power thinning exponent. Its job is narrower: start from the exact Stage15-4 survivor normal form and determine whether the common squarefree norm core admits an exact local adapter to the Stage14 Arsenal.

## 1. Starting normal form

For coprime positive pairs

\[
m>n>0,\qquad r>s>0,
\]

set

\[
\alpha=mr+i\,ns,\qquad \beta=ms+i\,nr,
\]

and

\[
A=N(\alpha)=m^2r^2+n^2s^2,
\qquad
B=N(\beta)=m^2s^2+n^2r^2.
\]

Stage15-4 proved that the integral-space-diagonal condition is exactly

\[
\operatorname{sf}(A)=\operatorname{sf}(B)=k,
\]

or equivalently `A=kP^2`, `B=kQ^2` for a unique squarefree `k`.

Write

\[
k=2^\eta k^\circ,\qquad \eta\in\{0,1\},\qquad k^\circ\text{ odd}.
\]

Stage15-6aa peels the 2-primary factor and analyzes `k^circ` exactly.

## 2. Unit lemma for every odd core prime

**Lemma 15.6aa.1.** If an odd prime `p` divides the common squarefree core `k`, then

\[
p\nmid mnrs.
\]

**Proof.** Since `p|k`, both `p|A` and `p|B`. Suppose for example `p|m`. Coprimality gives `p∤n`. From

\[
A\equiv n^2s^2\pmod p
\]

we obtain `p|s`; then `p∤r` because `(r,s)=1`. But

\[
B\equiv n^2r^2\not\equiv0\pmod p,
\]

contradiction. The cases `p|n,r,s` are symmetric. ∎

Thus every odd core prime sees all four toric parameters as units. This is the missing unit hypothesis needed before any Gaussian root-line spacing can be invoked.

## 3. Exact two-channel determinant lock

Fix an odd `p|k`. Divide the two norm congruences by the unit `n^2s^2` and put

\[
X=(m/n)^2,\qquad Y=(r/s)^2\quad\text{in }\mathbf F_p^\times.
\]

The conditions `A≡B≡0 (mod p)` become

\[
XY=-1,\qquad X+Y=0.
\]

Hence `Y=-X` and `X^2=1`. Therefore exactly one of the following occurs.

### S-channel

\[
X=-1,\qquad Y=1,
\]

so

\[
p\mid m^2+n^2,
\qquad
p\mid r^2-s^2.
\]

### O-channel

\[
X=1,\qquad Y=-1,
\]

so

\[
p\mid m^2-n^2,
\qquad
p\mid r^2+s^2.
\]

The two channels are mutually exclusive for odd `p`, because membership in both would force `p|2m^2` and `p|2n^2`.

In either channel `-1` is a quadratic residue modulo `p`, so automatically

\[
p\equiv1\pmod4.
\]

This recovers the Stage15-4 prime-support statement from the local coupled equations themselves.

Define the squarefree channel factors

\[
k_S=\prod_{\substack{p\mid k^\circ\\p\text{ in S-channel}}}p,
\qquad
k_O=\prod_{\substack{p\mid k^\circ\\p\text{ in O-channel}}}p.
\]

Then uniquely

\[
\boxed{k^\circ=k_Sk_O,\qquad (k_S,k_O)=1,}
\]

with the simultaneous divisibility locks

\[
\boxed{k_S\mid m^2+n^2,\qquad k_S\mid r^2-s^2,}
\]

\[
\boxed{k_O\mid m^2-n^2,\qquad k_O\mid r^2+s^2.}
\]

Consequently

\[
\boxed{(k^\circ)^2\mid (m^4-n^4)(r^4-s^4).}
\]

This square-divisor identity is exact, but it is **not yet** an AR-014 global adapter because the right-hand side still moves with both charged toric pairs.

## 4. Root-line interpretation

The channel split exposes the local geometry more sharply than the bare equality `sf(A)=sf(B)`.

For `p|k_S`,

\[
(m/n)^2\equiv-1\pmod p,
\qquad
(r/s)^2\equiv1\pmod p.
\]

For `p|k_O`,

\[
(m/n)^2\equiv1\pmod p,
\qquad
(r/s)^2\equiv-1\pmod p.
\]

Thus every odd core prime forces one parameter pair onto a **Gaussian root line** and the other onto a **diagonal `±1` line**. Primewise choices recombine by CRT; the number of root/sign orientations is at most `2^{omega(k^circ)}=B^{o(1)}` whenever the relevant core is polynomially bounded.

This is the first concrete causal mechanism extracted in Stage15-6:

```text
TWO_CHANNEL_GAUSSIAN_DETERMINANT_LOCK
```

It is local/exact. No whole-family thinning exponent is inferred from it in this substage.

## 5. Gaussian orientation dictionary

Because every odd `p|k` satisfies `p≡1 (mod 4)` and `p∤mnrs`, write `p=pi_p conjugate(pi_p)` in `Z[i]`. Exactly one of the two conjugate Gaussian primes divides `alpha`; call that choice `pi_p`.

Since `p|N(beta)`, exactly one of `pi_p` and `conjugate(pi_p)` divides `beta`.

- if `pi_p|beta`, the prime lies in the S-channel;
- if `conjugate(pi_p)|beta`, the prime lies in the O-channel.

This is equivalent to the determinant calculation:

- common Gaussian orientation forces `p|(m^2+n^2)` and `p|(r^2-s^2)`;
- opposite Gaussian orientation forces `p|(m^2-n^2)` and `p|(r^2+s^2)`.

Hence the Stage15 `k_S/k_O` decomposition is the exact analogue of the same/opposite Gaussian-orientation split anticipated by Arsenal AR-018, but now derived in the Stage15 toric coordinates.

Taking the product of the selected `pi_p` over `p|k^circ` gives a Gaussian divisor `Pi_alpha|alpha` with

\[
N(Pi_\alpha)=k^\circ.
\]

The corresponding divisor of `beta` is obtained by conjugating precisely the O-channel prime factors. Therefore the quotient dictionary of AR-017 is locally available after `(k_S,k_O)` and the prime orientations have been fixed.

Crucially, `Pi_alpha` is still generated by the point unless the outer counting scheme fixes and charges the core first. Stage15-6aa does not count it as a second independent modulus.

## 6. Arsenal verdict after the adapter

### AR-009 — primitive Gaussian root-line lattice count

Stage15-4 status: `TRIGGERED_ADAPTER_REQUIRED`.

Stage15-6aa status:

```text
AR-009=EXACT_LOCAL_ADAPTER_PROVED_GLOBAL_CHARGE_OPEN
```

For fixed odd channel core and fixed opposite toric pair, the hypotheses are now explicit. For example, on the S-channel,

\[
k_S\mid m^2+n^2,
\qquad (m,n)=1,
\qquad (k_S,mn)=1,
\]

and every prime of `k_S` is `1 mod 4`; therefore `(m,n)` lies on one of the primitive Gaussian root lines modulo `k_S`. The same statement applies to `(r,s)` modulo `k_O`.

What remains open is not the local root-line lemma. It is whether the moving `k_S,k_O` can be fixed/charged and summed under the **physical Stage15 height measure** without losing the intended saving.

### AR-017 — Gaussian quotient / resultant dictionary

Stage15-6aa status:

```text
AR-017=LOCAL_GAUSSIAN_DIVISOR_LIFT_PROVED_GLOBAL_CHARGE_OPEN
```

The exact Gaussian divisor and same/opposite orientation dictionary now exist. The missing hypothesis is a measure-preserving whole-family charging scheme for this moving divisor.

### AR-018 — Gaussian squareclass orientation split

Stage15-6aa status:

```text
AR-018=STAGE15_ORIENTATION_SPLIT_REALIZED_NO_SAVING_TRANSFER
```

The primewise same/opposite split is exact. Stage14's Cayley `M±N` structure is absent, so no Stage14 exponent or independent modulus saving is transferred.

### AR-014 — fixed-outer gcd/square-divisor adapter

Status remains

```text
AR-014=WATCH_ONLY
```

Although `(k^circ)^2` divides `(m^4-n^4)(r^4-s^4)`, that host is not fixed before both toric pairs are counted. AR-014 cannot yet be invoked as a whole-family multiplicity reduction.

### AR-023 / AR-024 / AR-028

These remain active firewalls. The new core split is pointwise structure, not permission to scalarize the coupled toric-pair measure or recharge `k` and its Gaussian orientations separately.

## 7. Physical population guard

Nothing in the local derivation changes the Stage15 physical measure.

- the toric pair is still recovered uniquely from the physical shared-edge incidence;
- primitive reduction remains exact;
- the physical cutoff remains primitive `R<=B` rather than a raw `(m,n,r,s)` box;
- `x^2+y^2` nonsquare remains the exactly-two postfilter;
- the three shared-edge direction chambers remain separate if a directional argument is attempted.

Therefore Stage15-6aa proves a local algebraic adapter only. It does not replace the physical population by unrestricted toric parameters.

## 8. Witnesses

Three primitive exactly-two survivors exhibit all channel types.

1. **S only:** `(m,n,r,s)=(13,1,9,1)`, `k=10`, `k^circ=5`, `k_S=5`, `k_O=1`.
2. **O only:** `(m,n,r,s)=(13,4,13,1)`, `k=17`, `k_S=1`, `k_O=17`.
3. **Mixed:** `(m,n,r,s)=(9,1,27,14)`, `k=205=5*41`, `k_S=41`, `k_O=5`.

The mixed witness shows that neither channel alone describes the full survivor population; a valid global argument must retain the primewise split.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6aa
STAGE15_6AA_STARTING_NORMAL_FORM=sf(N(mr+i*ns))=sf(N(ms+i*nr))
STAGE15_6AA_ODD_CORE_UNIT_LEMMA=true
STAGE15_6AA_TWO_CHANNEL_SPLIT=true
STAGE15_6AA_CHANNEL_FACTOR_UNIQUENESS=true
STAGE15_6AA_ODD_CORE_SQUARE_DIVISOR_LOCK=true
STAGE15_6AA_CAUSAL_CANDIDATE=TWO_CHANNEL_GAUSSIAN_DETERMINANT_LOCK
STAGE15_6AA_AR009_LOCAL_ADAPTER=true
STAGE15_6AA_AR017_LOCAL_DIVISOR_LIFT=true
STAGE15_6AA_AR018_ORIENTATION_SPLIT=true
STAGE15_6AA_GLOBAL_CORE_CHARGE_PROVED=false
STAGE15_6AA_PHYSICAL_MEASURE_ADAPTER_PROVED=false
STAGE15_6AA_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AA_STAGE15_5_REPROVED=false
STAGE15_6AA_EXIT=LOCAL_CORE_ADAPTER_PROVED_GLOBAL_CHARGE_OPEN
```

## 10. Next narrow gate

The next Stage15-6 substage should not open a new Stage14 route. It should answer one question:

> Can the moving pair `(k_S,k_O)` be charged before root-line counting in a way that preserves the physical `R<=B` toric-pair measure and makes the sum over cores affordable?

Until that is proved, AR-009/017 are exact **local** adapters but not a whole-family causal thinning proof.
