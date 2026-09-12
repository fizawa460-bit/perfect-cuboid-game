# Stage32 MB104 — Riemann--Roch effectivity survives; the explicit `F1-P5` Picard ray is forced reducible

Status: **RETAINED GLOBAL CLASSIFICATION PROGRESS / EFFECTIVITY SURVIVES / F1-P5 EXACT RAY IRREDUCIBLE CARRIER EXCLUDED / MB104 INCOMPLETE / NO CREDIT**

## Purpose

`FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY` moved the three hard-sector formal packets into honest integral Picard classes. The next priority leaf asks whether these classes are effective and, if so, whether an irreducible low-genus carrier can occur.

This leaf gives two distinct conclusions:

1. **all three displayed infinite Picard subsequences are effective** by Riemann--Roch;
2. the explicit genus-one span-5 class `F1-P5-PIC` is nevertheless **never irreducible**, because at least one strict transform of a `c=0` conic has negative intersection with the class. For the retained explicit support, three such conics are forced fixed components.

Thus Picard integrality and effectivity both survive, but the first explicit span-5 actual-carrier attempt fails at irreducibility.

## Source-locked canonical data

Stoll--Testa give on the minimal resolution `S`

```text
K_S=H=b^*O_barS(1),
H^2=16,
chi(O_S)=8,
H is big and nef.
```

The exact source note is `STOLL-CANONICAL-C0-SOURCE-NOTE.md`.

The retained MB104 Picard classes are

```text
F0-P6-PIC:
  l>=0,
  D0=(7l+5)H-(4l+3) sum_{S_P6} E_i,
  d=H.D0=112l+80,
  D0^2=336l^2+448l+148.

F1-P5-PIC:
  l>=1,
  D15=7l H-4l sum_{S_P5} E_i,
  d=112l,
  D15^2=336l^2.

F1-P6-PIC:
  l>=1,
  D16=7l H-4l sum_{S_P6} E_i,
  d=112l,
  D16^2=336l^2.
```

## Riemann--Roch: all three classes are effective

For any divisor `D` on the smooth surface,

```text
chi(O_S(D)) = chi(O_S) + (D.(D-K_S))/2.
```

For `F0-P6-PIC`,

```text
chi(O(D0))
 = 8 + (D0^2-d)/2
 = 168l^2+168l+42 > 0.
```

For either genus-one Picard family,

```text
chi(O(D1))
 = 8 + (336l^2-112l)/2
 = 168l^2-56l+8 > 0     (l>=1).
```

Moreover,

```text
H.(K_S-D)=16-d < 0
```

for every displayed parameter value. Since `H` is nef, an effective divisor cannot have negative intersection with `H`. Hence `K_S-D` is not effective, so by Serre duality

```text
h^2(O(D)) = h^0(O(K_S-D)) = 0.
```

Therefore

```text
h^0(O(D)) = chi(O(D)) + h^1(O(D)) >= chi(O(D)) > 0.
```

So every displayed `D0`, `D15`, and `D16` is effective. The effectivity obstruction is closed for these exact rays.

This does **not** imply a reduced, irreducible, or low-normalization-genus member.

## The `c=0` conic incidence wall for `F1-P5-PIC`

Stoll--Testa identify

```text
bar S cap {c=0}
```

as the reduced union of eight smooth conics `Q_eps`, indexed by `eps=(eps1,eps2,eps3) in {+1,-1}^3`.

Every `c=0` box node lies on exactly two of these eight conics. On the minimal resolution, for the strict transform `tilde Q_eps`,

```text
H.tildeQ_eps = 2,
E_i.tildeQ_eps = 1 if node i lies on Q_eps,
E_i.tildeQ_eps = 0 otherwise.
```

The retained `F1-P5` support consists of 14 distinct nodes in `c=0`. Let

```text
n_eps = # {supported nodes lying on Q_eps}.
```

Then each supported node contributes to exactly two conics, hence

```text
sum_eps n_eps = 2*14 = 28.
```

There are only eight conics, so

```text
max_eps n_eps >= ceil(28/8)=4.
```

For

```text
D15 = 7l H - 4l sum_{i in S_P5} E_i,
```

we obtain

```text
D15.tildeQ_eps
 = 7l*(H.tildeQ_eps) - 4l*n_eps
 = 14l - 4l n_eps
 = 2l(7-2n_eps).
```

Therefore any `n_eps>=4` gives

```text
D15.tildeQ_eps <= -2l < 0.
```

If an effective divisor has negative intersection with an irreducible curve, that curve is a component of the divisor. Thus **every effective divisor in class `D15` contains a `c=0` conic component**.

Since `H.D15=112l>2=H.tildeQ_eps`, no divisor in class `D15` can equal that conic. Consequently:

```text
NO EFFECTIVE DIVISOR IN |D15| IS IRREDUCIBLE.
```

Hence the retained explicit `F1-P5-PIC` formal infinite family cannot produce the required integral genus-one carrier.

## Exact retained support: three forced conics

For the explicit 14-node support already retained in `FORMAL-INFINITE-FAMILY-FEASIBILITY`, the eight incidence counts are

```text
[5,4,3,3,4,3,3,3]
```

in the verifier's fixed sign-triple order. Therefore three conics have negative intersection:

```text
n=5: D15.tildeQ = -6l,
n=4: D15.tildeQ = -2l,
n=4: D15.tildeQ = -2l.
```

So the explicit class has at least three distinct forced `c=0` conic components.

## Scope

This closes the displayed `F1-P5-PIC` ray as an **actual irreducible carrier**. It does not yet classify every genus-one span-5 carrier.

The next useful question is finite and global:

```text
CLASSIFY HYPERPLANES CONTAINING >=14 OF THE 48 BOX NODES.
```

If every span-5 support of size at least 14 is carried by an Aut(S)-translate of one of the four conic hyperplanes, or by another hyperplane with an analogous fixed-component incidence inequality, the same argument can be promoted from the explicit ray to the whole genus-one span-5 hard sector.

For the surviving explicit full-span rays `F0-P6-PIC` and `F1-P6-PIC`, effectivity is now proved, so the unresolved obstruction is irreducibility/geometric genus/global incidence rather than effectivity.

## Firewalls

- `effectivity_proved=true` only for the three displayed Picard subsequences/classes.
- `F1_P5_explicit_picard_ray_irreducible_member_exists=false`.
- No statement is made that every genus-one span-5 support is contained in a `c=0`-type conic hyperplane.
- No actual genus-zero or genus-one carrier is constructed for the surviving P6 rays.
- No population-wide finite degree window is proved.
- MB104 remains incomplete; MB105 remains gated.
- No receiver/effectivity-final-milestone/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
