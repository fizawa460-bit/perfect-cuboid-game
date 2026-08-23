# Stage32 source lock — LOWGENUS-PICARD-PRODUCTION

## Internal authoritative inputs

Stage32 consumes the following already-audited repository records without rewriting their historical claims:

```text
stages/stage29/29-02c-LG2/result.md
stages/stage29/29-02c-LG2/audit.md
stages/stage29/29-02c-LG2/finite-search-contract.md
stages/stage29/29-02c-LG2/computational-feasibility.md
stages/stage29/29-02c-LG2/upstream-code-lock.md
stages/stage29/29-15/open-receiver-triage.json
stages/stage29/29-16/active-kernel-ledger.json
stages/stage31/controller.json
```

Stage31 is closed on main before Stage32 roadmap creation:

```text
main=e1e44bfe04b3194c6d1732c9c099642b49741444
Stage31 status=STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION
post-Stage31 active kernels=11
post-Stage31 Class2=2
post-Stage31 Class3=9
```

## Frozen Stage29 receiver semantics

```text
K16-C2-LOWGENUS-PICARD-PRODUCTION
children:
  R29-LG2
  R29-LG2-EFF
  R29-LG2-MB
parent route:
  G10-LOWGENUS-PICARD
```

Exact wall:

```text
symmetry-reduced effectivity-aware multibranch Picard-lattice enumeration
to the audited d<=176/192 bounds
```

Completion consequence:

```text
complete bounded low-genus carrier census only
```

Coverage firewall:

```text
no theorem says every endpoint rational point lies on a rational or elliptic carrier
```

## Frozen finite-search contract

Audited unibranch windows:

```text
G0: geometric genus 0, even 2<=d<=176
G1: geometric genus 1, even 4<=d<=192
```

With `H=K_S`, `H^2=16`, `d=H.C`,

```text
r=gcd(d,16)
m=16/r
n=d/r
y=m*C-n*H
H.y=0
C=(y+nH)/m
```

and

```text
G0: -y^2 <= m^2*(d^2/16+d+2)
G1: -y^2 <= m^2*(d^2/16+d)
```

subject to exact divisibility in `Pic(S)`.

Necessary filters from the audited contract include exact degree/divisibility, adjunction, known-curve intersections, exceptional incidence/Lemma 21, automorphism-orbit deduplication, low-degree subtraction, physical-chamber compatibility where explicit, and the bijective-normalization hypothesis.

These filters are not effectivity certificates.

## Upstream public computation lock

Freshly re-read at the immutable commit during Stage32 roadmap creation:

```text
UPSTREAM_REPO=https://github.com/MichaelStollBayreuth/Verification
UPSTREAM_COMMIT=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
UPSTREAM_FILE=Cuboids/cuboids.magma
UPSTREAM_BLOB=0422b69847f2afb97cb7b3ed02ebef91279f61b1
UPSTREAM_LICENSE=GPL-3.0
```

Load-bearing objects visible in the frozen source:

```text
48 singular points
known curve configuration
rank-64 known-curve intersection lattice
PicL
HinPicL
automorphism action
Galois action
CloseVectors templates
K3 quotient / lifting machinery
known-curve intersection filters
```

The source explicitly constructs `AutS` in `GL(64,Z)` and the Stage29 theorem/source package records `#Aut(S)=1536`.

The degree-6 lifting helper uses a rank-44 negative-definite kernel and estimates close-vector volume by

```text
LkertrcE_vol * bound^(Dimension(LkertrcE)/2)
```

with exponent `22`.

## Attribution firewall

```text
CODE_CONSTRUCTS_KNOWN_CURVE_RANK64_LATTICE=true
TESTA_STOLL_THEOREM_IDENTIFIES_FULL_PICARD_GROUP=true
CODE_ALONE_PROVES_FULL_PICARD_GROUP=false
FULL_PICARD_LATTICE_AVAILABLE_AFTER_THEOREM_PLUS_CODE=true
```

Stage32 must preserve this distinction.

## Scope firewalls

```text
NUMERICAL_CLASS_SURVIVES_FILTERS => EFFECTIVE           false
UNIBRANCH_WINDOW_COMPLETE => ALL_LOW_GENUS_COMPLETE    false
LOW_GENUS_CARRIER_CENSUS => ENDPOINT_NONEXISTENCE      false
ISOLATED_RATIONAL_POINTS_EXCLUDED                      false
ROUTE_COLOR_CHANGE_AUTHORIZED                          false
PERFECT_CUBOID_EXISTENCE_CLAIM                         false
PERFECT_CUBOID_NONEXISTENCE_CLAIM                      false
```
