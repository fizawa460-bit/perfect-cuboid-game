# Stage32 MB104 global-classification checkpoint

Status: **FROZEN FOR INTERMEDIATE HOSTILE AUDIT / UNIFORM P5 GEOMETRIC CORE 864 / MB104 EQUALITY-PACKET CORE 768 / 000707 JOINT PAIR BIRATIONAL + SATURATED BOUNDARY FIBERS / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of a standalone `R8<d/4+O(1)` inequality remains frozen unless a genuinely new lever appears.

The most recent hostile-audited retained boundary is

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`.

The retained continuation has now reached the repository's long-lived shared-PR warning zone. Treat this exact retained checkpoint as frozen for the next intermediate delta-bounded `stage32mb` hostile audit. Do not append another substantial retained research wave to this shared PR before that audit result. Scratch-only exploration may continue off the shared retained surface when permitted.

## 1. Scope

For the displayed uniform genus-one P5 ray,

```text
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
d=112l,
l>=1.
```

The dangerous MB104 packet is stronger:

```text
r_i=M_i=8l on all 14 supported nodes,
all branches FSM-minimal (A,B)=(1,1), m=1,
R=R8=M=r_odd=d=112l.
```

The Picard class and this branch packet must not be conflated.

## 2. Geometric and equality-packet frontiers

For the displayed ray, fixed-component reductions plus the exact two-zero-quartic gluing obstruction leave the geometric arbitrary-branch support population

```text
864 = 48+48+768
```

on

```text
0000770000ff,
00007b0000ff,
000707000f0f.
```

All retained zero-pairing quartics on these supports are nonfixed for every `l>=1`; the known zero-quartic route is exhausted.

The Beauville equality route applies only to the dangerous packet. It forces product-cover projections to be finite etale of degree `14el`. The two one-type size48 packets are excluded for all `l>=1` by the CM inert-7 contradiction. Therefore

```text
geometric arbitrary-branch core: 864;
MB104 dangerous equality-packet core: 768,
```

and the latter consists only of

```text
000707000f0f.
```

## 3. `000707` current exact reductions

The support has node-type counts

```text
(7,7,0).
```

Two used outside involutions exclude `e=1`, leaving

```text
e=2 or e=4.
```

Let

```text
H=<s1,s2> ~= (Z/2)^2,
Q=Z/H,
R=C8/H ~= P1.
```

Then `g(Q)=1` and the two descended factor maps

```text
psi1,psi2:Q->R
```

have common degree

```text
e=2: 28l;
e=4: 56l.
```

The joint map

```text
Psi=(psi1,psi2):Q->R x R
```

is birational onto its image. Exact `Aut(S)` replay shows the support stabilizer has order two, with its unique nonidentity swapping the two used node types; hence there is no nontrivial type-preserving relative deck symmetry. The image bidegree is therefore exactly

```text
e=2: (28l,28l);
e=4: (56l,56l),
```

with normalization genus one.

## 4. Satake-boundary two-fiber saturation

The two zero quartics

```text
Q0: b1=0, i*a2-a3=0, a1-c=0,
Q1: b2=0, i*a3+a1=0, a2-c=0
```

are Satake-boundary components. Each contains eight box nodes, seven supported by `000707`.

For a fixed zero quartic, its relevant four-cusp `G`-orbit splits into exactly two `H`-orbits on the fixed factor. Consequently all dangerous-packet branches from those seven nodes lie over two specific factor-quotient values.

For `e=2`,

```text
7*(8l)=56l=2*(28l),
```

so the two specific degree-`28l` fibers are reduced, unramified, and fully saturated, each containing `28l` supported points.

For `e=4`, the residual etale double cover doubles the supported points on `Q=Z/H`:

```text
2*7*(8l)=112l=2*(56l),
```

so the two corresponding degree-`56l` fibers are also reduced, unramified, and fully saturated, each containing `56l` supported points.

No per-node concentration, equal split of the `8l` branches at a node, or orientation relation between the two zero quartics is assumed.

## 5. Exact missing datum after freeze

The retained equality packet now satisfies simultaneously

```text
e in {2,4};
Psi birational of bidegree (28l,28l) or (56l,56l);
for each zero quartic, two specific factor fibers are completely saturated and unramified.
```

The missing invariant is the residual product-cover sheet/character assignment: compute the restriction of the remaining nontrivial character(s) of the free `G0` cover to the carrier pullback, or derive an algebraic incompatibility between the two birational factor maps and the saturated fiber pairs.

That is the post-audit next leaf:

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.
```

## 6. Evidence and audit handoff

New active evidence includes:

- `GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md` + certificate/verifier;
- `BEAUVILLE-SATAKE-BOUNDARY-SOURCE-NOTE.md`;
- `GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md` + certificate/verifier;
- size48 CM inert-7 evidence and the earlier balanced16 continuation since the last hostile PASS.

The new boundary-fiber verifier is fail-closed on its declared Git blob identities. No exact-head CI/local replay is claimed; no automatic MB workflow is required. The intermediate hostile audit should run the relevant fail-closed verifiers directly on the frozen exact head and audit the retained delta since `39a56d2a9abda0c051145172ff61d67eef0bdb14` plus transitive load-bearing dependencies.

## Firewalls

- geometric arbitrary-branch uniform-ray support core remains `864`;
- only the dangerous equality-packet core is `768`;
- `000707` remains open for both `e=2` and `e=4`;
- support-span five is not fully closed;
- arbitrary unequal exceptional coefficients remain open;
- genus-one P6 and genus-zero P6 remain open;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and finite Picard enumeration is unreleased;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
