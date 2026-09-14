# Stage32 MB104 — genus-one P5 compact-etale correspondence cusp-width route (REJECTED)

Status: **REJECTED BY HOSTILE AUDIT / NON-CONSUMABLE / NO MB104 CREDIT**

## Audit receipt

- candidate exact head: `d83914576150bf0c5c6e3be0fcadf3baf7104ece`
- hostile-audit review: `5194067386`
- hostile-audit result: **FAIL**

The candidate attempted to place both compact etale projections

```text
f1,f2 : Z -> C8
```

on one punctured modular uniformization and then use `Gamma[8]` cusp widths to force degree one.

## Blocking defect

For a compact etale map, deleting the modular cusp divisor from the target deletes `f_j^{-1}(Cusps)` from `Z`. The candidate did not prove

```text
f1^{-1}(Cusps) = f2^{-1}(Cusps).
```

Therefore the two restricted maps cannot be placed on one common punctured `H/Lambda` from the retained inputs. In particular, the following candidate implications are **not retained**:

```text
Lambda = Gamma[8] cap g^{-1}Gamma[8]g
Gamma[8]-cusp-width divisibilities for both projections
det(A)=1
degree(f1)=degree(f2)=1
nonexistence of the uniform F1-P5 equality realization
```

Passing instead to the compact universal cover does not repair the route: the compact genus-five curve has a cocompact uniformizing deck group, so the punctured modular `Gamma[8]` cusp-width arithmetic is unavailable.

## Retained boundary

This rejection does not alter the previously retained `GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY` facts. It also does not close `000707` at `e=2` or `e=4`.

The authoritative MB104 active leaf remains the `000707` `e=2` residual-lift conductor-pair problem: construct or source-lock the branch/conductor normalization-preimage to residual `C8/H` / `G/H` sheet transition (equivalently the residual square-root relative sign under conductor gluing).

## Re-entry condition

This cusp-width route is non-consumable unless a later, separately hostile-audited artifact proves a source-locked equality

```text
f1^{-1}(Cusps) = f2^{-1}(Cusps)
```

or an equivalent common modular-puncture structure for the equality component.

## Firewalls

- `consumable_as_obstruction = false`
- uniform F1-P5 equality face closed here: **false**
- MB104 complete: **false**
- receiver/theorem/endpoint/Perfect-Cuboid credit: **false**
- STATE promotion: **none**
- merge authorization: **false**
