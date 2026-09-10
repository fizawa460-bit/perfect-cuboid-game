# Stage35-EX Goal4CE source lock — post-canonical-gcd local completion parking audit

Scope: consume exact-green Goal4CD and execute the Cycle Exploration Safety Protocol after the Goal4BT material reopen has been fully spent through Goal4BU–Goal4CD. This leaf proves an exact common-leg gcd completeness statement for the two E1 norm orientations, classifies the fresh-prime remainder against the historical receiver ledger, and decides whether the cycle can return to the Goal4BS parking boundary. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent and audit freshness

Goal4CD is exact-green at

```text
head = 2d9380224f70f24530799f6d9fd6b5693351b0d4
Goal4CD run = 34425516973 SUCCESS
aggregate run = 34425516998 SUCCESS
```

The last hostile-audited intermediate checkpoint remains

```text
Goal4BS exact head = d6f5151c9d95304afe7081c92f40f1d25cc4aa3b
review = 5151846948 PASS.
```

The current parent is 49 commits beyond that checkpoint, so the long-lived-PR warning threshold is not approached.

Goal4BS parked the retained cycle because no live route remained from the then-retained inputs. Goal4BT legally reopened it by proving that the Master hypotenuse and bridge reservoir

```text
H=sqrt((V1*U2)^2+(U1*V2)^2)/(c*q),
e=gcd(c,H)
```

are source-computable before any E1-failure assumption. Goal4BU–Goal4BY exhausted quadratic/quartic bridge consequences; Goal4BZ–Goal4CB exhausted the ordinary local-square test at `e`; Goal4CC–Goal4CD then exhausted the companion canonical cross-gcd families `p` and `d`.

The question here is whether that material reopen exposed any further source-selected gcd-local family that has not been consumed.

## 2. Exact common-leg gcd classification of both E1 norm orientations

Keep primitive Euclid triples

```text
U1=a^2-b^2, V1=2ab, W1=a^2+b^2,
U2=m^2-n^2, V2=2mn, W2=m^2+n^2,
```

with

```text
c=gcd(U1,U2),
p=gcd(W1,V2),
d=gcd(V1,W2),
q=gcd(V1,V2).
```

The same raw E1 radicand has the two exact presentations

```text
F_E1=(W1*U2)^2+(U1*V2)^2,                         (CE-Fp)
F_E1=(U1*W2)^2+(V1*U2)^2.                         (CE-Fd)
```

For `(CE-Fp)`, a prime common to the two raw legs can only cross through

```text
W1 <-> V2,
U2 <-> U1,
```

because `gcd(W1,U1)=gcd(U2,V2)=1`. Primewise this gives exactly

```text
gcd(W1*U2,U1*V2)=p*c.                             (CE-gp)
```

For `(CE-Fd)`, primitivity similarly leaves only

```text
U1 <-> U2,
W2 <-> V1,
```

so exactly

```text
gcd(U1*W2,V1*U2)=c*d.                             (CE-gd)
```

Therefore the complete source-selected common-leg gcd universe of the two E1 orientations is

```text
{c,p,d}.                                           (CE-common)
```

There is no fourth cross-gcd cancellation channel hidden by either norm presentation.

The Master gcd `q=gcd(V1,V2)` is not an E1 common-leg channel. For every odd `ell|q`, primitivity gives

```text
ell∤W1*U2,
```

while `ell|U1*V2`; hence

```text
F_E1 == (W1*U2)^2 != 0 (mod ell).                  (CE-q-neutral)
```

Thus `F_E1` is automatically an `ell`-adic square at the residue-unit layer there; `q` cannot supply a new cancellation-depth family. The 2-adic source normalization is already fixed by the primitive Euclid parity and the 35EX-02 Master dichotomy, so no new `q`-2-adic E1 channel is created either.

The same one-summand argument applies to any source gcd that places both of its factors inside one raw E1 summand rather than across the two summands: the opposite summand is an `ell`-adic unit square modulo `ell`, so such a prime is not a cancellation family.

Hence `(CE-common)` is exact, not heuristic.

## 3. The c-channel is already exactly refined by e

Goal4CA gives

```text
F_E1=(c*e)^2*B_e,
B_e=(q*H/e)^2+(c*D*T/e)^2,
D=U1/c,
T=U2/c.                                            (CE-Be)
```

Let `ell|c`.

If `ell∤H`, then `ell∤e`; the first leg `qH/e` is an `ell`-adic unit and the second is divisible by `ell`. Therefore

```text
B_e == (qH/e)^2 != 0 (mod ell),
```

so the local square condition is automatic.

If `ell|H`, then `ell|e`. Goal4CA proves that unequal valuations `v_ell(c) != v_ell(H)` again force `v_ell(B_e)=0` with square residue, while the balanced stratum is the only nontrivial depth stratum. Goal4CB supplies the complete odd-prime square test there: even valuation plus square residual unit.

Consequently

```text
c-channel nontrivial local content = exactly the Goal4CA/CB e-family.  (CE-c=e)
```

No residual `c/e` family remains.

## 4. The p- and d-channels are already complete

Goal4CD proves for every odd `ell|p=gcd(W1,V2)`:

```text
v_ell(W1) != v_ell(V2) => local E1 square automatic,
```

while in the balanced stratum the reduced norm `R_p,ell` is a square in `Q_ell` iff its valuation is even and its residual unit is a quadratic residue.

The exact index-swapped statement holds for every odd `ell|d=gcd(V1,W2)` using `R_d,ell`.

Thus

```text
p-channel complete = Goal4CD,
d-channel complete = Goal4CD.                       (CE-pd-complete)
```

Combining `(CE-c=e)` and `(CE-pd-complete)` with `(CE-common)` proves

```text
ALL_SOURCE_SELECTED_E1_COMMON_GCD_LOCAL_FAMILIES_COMPLETE=true.  (CE-local-complete)
```

This is the precise scope of completeness: source-selected common-leg gcd local tests for the two E1 norm orientations. It is not a claim that every possible local or global theorem has been exhausted.

## 5. Fresh norm primes are the endpoint receiver, not a fourth source family

Goal4CD's genuine Master-Hit

```text
(a,b,m,n)=(4,3,16,5)
```

has

```text
c=7,p=5,d=1,q=8,H=101,e=1,
B_e=706225=5^2*13*41*53.
```

The selected `p/d/e` tests all pass; the nonsquare is witnessed by the fresh primes

```text
13,41,53.
```

These primes are not selected in advance by a canonical common-leg gcd. Factoring them and requiring even valuation for every fresh prime is exactly the global condition

```text
B_e is a square,
```

which is equivalent to E1 itself.

The historical exact factorization makes the equivalence even more explicit:

```text
F_E1=(p*d)^2*Lminus*Lplus,
gcd(Lminus,Lplus)=1,
E1 failure <=> Lminus and Lplus are both squares.    (CE-Lpm)
```

35EX-14/15 prove that after the first factor is square, residual nonsquare support of `Lplus` can move to fresh `1 mod4` split primes outside the old source support. Therefore

```text
FRESH_NORM_PRIME_FACTORING=ENDPOINT_EQUIVALENT_DYNAMIC_SUPPORT.   (CE-fresh)
```

It is not a legal fourth source-gcd sieve.

## 6. Blind breadth pass from the strengthened receiver

Before consulting historical route names, the exact post-CD receiver suggests the following materially different lenses.

1. **Another source gcd/local cancellation family.** Exact classification `(CE-common)` plus `(CE-c=e)` and Goal4CD shows this is exhausted.
2. **Fresh-prime valuation/local-square testing.** By `(CE-fresh)` this is the moving full square receiver, not a source-selected finite family.
3. **Factor the norm into coprime plus/minus factors and attack their intersection.** This is a cleaner exact receiver, but it does not by itself create a contradiction.
4. **Global reciprocity/Jacobi/Hilbert coupling of the residual split primes.** This would require a source-fixed product relation among moving split-prime phases.
5. **Gaussian/quartic orientation of split primes.** This can sharpen orientation data but needs a source-fixed global functional value to prune universally.
6. **Same-type descent/product-hypotenuse reconstruction.** This would require a source-preserving strictly decreasing successor.
7. **S-unit/Thue or factor-squareclass enumeration.** This requires a source-independent fixed finite support or fixed finite coefficient family.
8. **Receiver-specific genus-one/global-surface geometry.** This requires an exact global adapter plus a theorem controlling the whole moving source family, not merely generic sections or one specialization.
9. **Height/counting/amplification.** This requires the quantitative lower/upper-height or super-square-root adapter previously frozen.
10. **Adelic/Brauer compactness.** This requires a global rational-realization/height adapter; finite local packets alone can escape toward the removed boundary.

No Arsenal route recommendation was used to generate this list.

## 7. Historical/Arsenal dedup after the blind pass

Now compare the blind list with the retained ledger.

- **Coprime `Lminus/Lplus` receiver and fresh split support:** 35EX-14/15. Exact adapter exists; direct joint-local close freezes at moving split support.
- **Global Jacobi/Hilbert coupling:** 35EX-16. Clean channels give `+1`; unresolved ramification moves.
- **Product-hypotenuse descent:** 35EX-17. No source-preserving strict same-type self-map.
- **Gaussian coordinate/orientation:** 35EX-18 and later Goal4BF–Goal4BO; the newer Goal4BV–Goal4BY bridge sequence further source-fixes the bridge orientation but ends with a source-redundant integer adapter, not universal pruning.
- **Receiver-specific genus-one / paired quartic / total-surface views:** 35EX-19 onward were explicitly broadened; the retained Goal4BS parking audit already classifies the surviving global theorem needs rather than leaving an immediately actionable retained route.
- **S-unit/Thue:** 35EX-12 freezes at dynamic source support.
- **Height/discriminant:** Goal4AW freezes the missing quantitative adapters.
- **Amplification:** Goal4AZ freezes the missing super-square-root amplifier.
- **Finite/full Brauer and boundary escape:** Goal4BB/AQ/BQ establish finite nonobstruction, endpoint equivalence of the full unit-character layer, and explicit boundary-depth escape without rational realization.
- **Derived fourth-square defect:** Goal4BR is a genuine invariant but not a required square receiver.

The Arsenal adds no already-retained weapon whose hypotheses are newly unlocked merely by Goal4CD. In particular S34-W01 still lacks a fixed finite squareclass support and S34-W03's direct receiver-restricted local use remains frozen at moving split support.

## 8. Reopen accounting against Goal4BS

Goal4BS parked with three explicit missing-object classes:

```text
A. GLOBAL_RATIONAL_REALIZATION_WITH_HEIGHT_CONTROL,
B. NEW_SOURCE_FIXED_E1_INVARIANT,
C. QUANTITATIVE_HEIGHT_DISCRIMINANT_ADAPTER.
```

Goal4BT supplied a genuine instance of class B by making `e` source-known. The retained chain then spent that new information as follows:

```text
BT: source-known H,e
BU: three source-known quadratic reservoirs
BV/BW/BX/BY: bridge quartic/orientation/global-product/integer-adapter layer
BZ: fresh audit after quartic saturation
CA/CB: complete e-prime local-square test
CC: fresh audit selecting p/d
CD: complete p/d local-square test
CE: prove no additional common-leg source-gcd family remains
```

Neither class A nor C has received a new adapter in this reopen. After `(CE-local-complete)`, the class-B information introduced by Goal4BT has no unprocessed local/common-gcd consequence left in the generated candidate set.

Therefore the post-BT reopen can legally return to the Goal4BS parking boundary without claiming E1 or Stage35 closure.

## 9. Parking ledger

```text
LIVE:
  none

UNTESTED_AND_IMMEDIATELY_ACTIONABLE_FROM_CURRENT_RETAINED_INPUTS:
  none

BLOCKED:
  BQ boundary-depth -> source-marked rational realization with height control
  AW elliptic/marked height -> quantitative discriminant/height adapters
  AZ amplification -> new super-square-root amplifier
  fixed-S S-unit/Thue or finite squareclass enumeration -> dynamic support
  direct receiver-local/global close -> moving fresh split-prime support
  same-type product-hypotenuse descent -> missing source reconstruction/decrease

EQUIVALENT_OR_DOMINATED:
  another e/p/d/q/common-gcd local sieve -> CE local-completeness theorem
  fresh norm-prime factoring -> B_e square / Lminus+Lplus exact E1 receiver
  another bridge quadratic/quartic rewrite -> BU–BY
  Gaussian ray/character deepening -> BF–BO/BV–BY boundaries
  finite/full Brauer reformulation -> BB/AQ endpoint boundary
```

The generated candidate set has no unprocessed live route from current retained inputs. This is a parking statement under the repository protocol, not an impossibility theorem.

## 10. Cycle exit

```text
CYCLE_ROUTE_STATUS=BLOCKED_NO_NEW_INFORMATION
CYCLE_ACTIVE_RECEIVER=PESCH_E1_MASTER_HIT_WITH_COMPLETE_SOURCE_SELECTED_COMMON_GCD_LOCAL_FAMILIES
CYCLE_LIVE_CANDIDATES=0
CYCLE_UNTESTED_CANDIDATES=0
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true
CYCLE_BLIND_REDISCOVERY=true
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=true
ALL_SOURCE_SELECTED_E1_COMMON_GCD_LOCAL_FAMILIES_COMPLETE=true
RETURN_TO_GOAL4BS_PARKING_BOUNDARY=true
```

Exact reopen conditions are the Goal4BS missing objects, sharpened by the present cycle:

```text
1. a new source-fixed E1 invariant not reducible to e/p/d/common-leg local square data or the exact B_e/Lminus/Lplus endpoint receiver;
2. a global rational-realization theorem with quantitative height control for the BQ boundary-depth packets;
3. the missing quantitative height/discriminant adapter of Goal4AW;
4. a genuinely new amplifier meeting the Goal4AZ threshold;
5. a theorem coupling moving fresh split-prime support globally without merely restating B_e square.
```

No hostile-audit credit. No E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid credit. MAIN-STATE remains V74 / Goal4AK. No merge.