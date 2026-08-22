# Stage29-13 — adversarial audit contract

Audit this submission independently from the exact source files and certified repository inputs. Do not accept either positive family closure merely because the external paper states it.

## 1. StageA2 transfer firewall

Re-read `stages/stageA2/A2-3`, `A2-4`, `A2-5`, and `A2-CLOSE`.

Verify that 29-13 transfers only the method species

```text
exact/source-locked low-dimensional receiver
 -> exact reduction/squareclass or lift condition
 -> explicit cover
 -> complete arithmetic closure
 -> reconstruction/boundary audit
```

and does **not** generalize the published equation-(6) `-18` family exclusion.

## 2. Saunderson closure — highest-priority hostile reconstruction

Use the exact external source `weiqi-kids/perfect-cuboid-problem/paper-a/paper.tex`, but independently rederive each load-bearing step.

Verify symbolically:

```text
Sa(u,v,w)=(u(4v^2-w^2),v(4u^2-w^2),4uvw)
u^2+v^2=w^2

a^2+b^2+c^2=w^2(w^4+16u^2v^2).
```

With

```text
u=p^2-q^2, v=2pq, w=p^2+q^2, t=p/q
```

verify exactly

```text
T^2=t^8+68t^6-122t^4+68t^2+1.
```

Then verify the quotient/lift chain

```text
W=t+1/t
S=T/t^2
S^2=W^4+64W^2-256
W^2-4=(t-1/t)^2
T0=t-1/t
C0: S^2=T0^4+72T0^2+16.
```

The lift condition is load-bearing. Check both directions and all excluded values `t=0, +/-1, infinity`.

Independently identify `Jac(C0)` and certify the complete rational point set. Do not rely on a bounded rational-point search. Verify the claimed Cremona/LMFDB model `80a1`, rank zero, torsion `(Z/2)^2`, and that the four visible points on `C0` exhaust `C0(Q)`.

Finally verify the reconstruction:

```text
T0=0 -> t=+/-1 -> u=0 -> degenerate
T0=infinity -> t=0/infinity -> v=0 -> degenerate.
```

Required disposition:

```text
R29_EXT_CHANG_A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
```

only if the entire chain survives. The source's erroneous historical sentence about the smallest Euler brick is non-load-bearing but must remain recorded as a source-quality warning.

## 3. Case B at p=1 — independent Pell/Lucas audit

Use `paper-b/paper.tex`, but independently verify

```text
B(q)=(4q,q^2-4,2(q^2-1))
a^2+b^2=(q^2+4)^2
a^2+c^2=(2(q^2+1))^2
b^2+c^2=5q^4-16q^2+20
a^2+b^2+c^2=5q^4+20.
```

Record that only two face conditions are automatic. The introductory stronger sentence is false and must not enter the proof.

Audit the necessary-space-condition chain

```text
g^2-5Y^2=20, Y=q^2
5|g
Y^2-5h^2=-4
Y=L_{2n-1}.
```

Source-check the exact Cohn theorem used for square Lucas numbers and its sequence convention. Verify it leaves only `Y=1,4`, hence `q=1,2`, and verify both are degenerate.

Do not use or credit the genus-five Jacobian decomposition unless independently proved; it is unnecessary for this family closure.

## 4. Paper C scope firewall

Read the theorem and remark in Paper C directly. Confirm whether the proved range is finite and whether the all-multiples extension is explicitly conjectural.

If the source still says the universal extension requires a missing effective primitive-divisor theorem, retain

```text
R29_EXT_CHANG_C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY.
```

A title or finite database computation is not a global theorem.

## 5. Paper D scope

Verify Paper D's actual mathematical output and whether it supplies any theorem that closes a perfect-cuboid family or gives the uniform positive canonical-height lower bound needed for a global orbit argument.

If not, retain structural/Arsenal-input status only.

## 6. Paper E — attack the submitted rejection

The submission does **not** certify Paper E. Try to repair it rather than simply repeating the criticism.

Re-read its quartic and elliptic models. Independently verify the `800a3`/LMFDB model, rank, torsion and integral points. Then locate the explicit birational maps, if present anywhere in the external repository/scripts, and determine whether there is a proved integrality implication from every relevant quartic integral point to the enumerated elliptic integral points.

Inspect the claimed height-completeness step. The source admits `mu<=2.93` is sampled. Determine whether another committed script/output actually runs a rigorous `IntegralPoints` algorithm or produces a valid elliptic-logarithm certificate. If such evidence exists, repair the submission positively. If not, retain

```text
R29_EXT_CHANG_E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE.
```

Do not treat Siegel finiteness plus a bounded search as a complete integral-point enumeration.

## 7. Parent route / coverage consequences

Even if A and B pass, verify their coverage exactly. They are family closures, not global endpoint coverage.

Check whether either family is already completely subsumed by an audited stronger family theorem in the repository. If so, mark the new child as `ALREADY_COVERED` rather than awarding duplicate attack credit.

Reclassify `J12-PARAMETRIC` only if the new closures or another audited input actually closes a globally covering endpoint mechanism. The current expected parent status is AMBER because Master-Hit coverage is global but `R29-PESCH-E1` remains conjectural.

Verify:

```text
P_OVER_M3_SCALE_KNOWN=false
ATTACK_ROUTE_COUNT=11
```

unless new proof evidence changes them.

## 8. Required output

Create `stages/stage29/29-13/audit.md` and repair this same PR branch as needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
R29_EXT_CHANG_A=<audited disposition>
R29_EXT_CHANG_B=<audited disposition>
R29_EXT_CHANG_C=<audited disposition>
R29_EXT_CHANG_D=<audited disposition>
R29_EXT_CHANG_E=<audited disposition>
CERTIFIED_NEW_FAMILY_CLOSURE_COUNT_29_13=<integer>
A2_STYLE_SUCCESSFUL_TRANSFER_COUNT=<integer>
J12_PARAMETRIC=GREEN|AMBER|RED|MERGED
ATTACK_ROUTE_COUNT=<integer>
GREEN_ROUTE_COUNT=<integer>
AMBER_ROUTE_COUNT=<integer>
P_OVER_M3_SCALE_KNOWN=true|false
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the submitted overall routing survives, the next item is

```text
29-14_NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST.
```
