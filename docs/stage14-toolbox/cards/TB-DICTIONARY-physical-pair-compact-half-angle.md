# Physical two-face pair -> compact gap / half-angle variables

```yaml
ID: TB-DICTIONARY-physical-pair-compact-half-angle
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Physical two-face gluing, compact gaps, and half-angle denominator variables
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-06
SOURCE_PR: 360
SOURCE_MERGE_SHA: 42f4315b0659bd402a94adeb8822588ea153305a
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
```

## INPUT

- Two primitive oriented Pythagorean face triples

```text
F =(S,X,H),
F2=(S2,X2,H2)
```

coming from a genuine physical two-face gluing with integer space diagonal `d`.
- The compact physical representative selected by Stage14-s6-05.

## OUTPUT

Define the physical gluing scale

```text
g=gcd(S,S2)
G=g*d.
```

Then

```text
G^2=S^2H2^2+X^2S2^2.
```

Define

```text
R=H2-S2
Nplus =H*G+S^2*H2+X^2*S2
Nminus=H*G-S^2*H2-X^2*S2
U=G-H*S2
V=H*H2-G.
```

The original physical and compact translated coordinates are

```text
Z_P=Nplus/R
Z_T=-Nminus/R=-U*V/X2^2.
```

The compact denominator is exactly

```text
D_T^2=R/gcd(Nminus,R)
     =X2^2/gcd(X2^2,U*V).
```

Hence

```text
D_T^2 | H2-S2
D_T   | X2.
```

For partner Euclid parameters `m2>n2`, define

```text
if S2=2m2n2:
    t=m2-n2
    kappa=1

if S2=m2^2-n2^2:
    t=n2
    kappa=2.
```

Then

```text
R=kappa*t^2
D_T|t
k=t/D_T
gcd(Nminus,R)=kappa*k^2.
```

The same cancellation square reappears in the compact square-kernel factors:

```text
Nminus             =kappa*k^2*e0*u0^2
H*(G-H*S2)         =kappa*k^2*e1*u1^2
H*(H*H2-G)         =kappa*k^2*e2*u2^2.
```

## VARIABLE DICTIONARY

- `S,X,H` = first primitive oriented face triple.
- `S2,X2,H2` = primitive partner face triple.
- `d` = physical integer space diagonal; not a signed kernel.
- `g` = `gcd(S,S2)`.
- `G` = physical gluing scale `g*d`; not one of `G0,G1,G2`.
- `R` = half-angle square-bearing difference `H2-S2`.
- `Nplus,Nminus` = conjugate physical numerators.
- `U,V` = positive physical gap variables `G-HS2` and `HH2-G`; not generic dyadic side lengths.
- `D_T` = compact physical denominator selector.
- `m2,n2` = Euclid parameters of the primitive partner face.
- `t` = partner half-angle parameter.
- `kappa` = orientation factor `1` or `2` in `R=kappa*t^2`.
- `k=t/D_T` = exact square-cancellation cofactor.
- `e0,e1,e2` = positive squarefree kernels in the compact `(--+)` chamber.

## USED BY

- s route from Stage14-s6-06 onward.
- main route whenever the abstract denominator gate is specialized to actual physical pair variables after a merged import.
- Toolbox recipes involving physical reconstruction, root-sign selection, or partner half-angle divisors.

## DO NOT USE FOR

- These identities require an actual physical two-face gluing and integer space diagonal; they are not identities on every abstract two-quadrics packet.
- Do not identify physical `G=g*d` with witness factors `G0,G1,G2`.
- Do not identify physical gaps `U,V` with dyadic box lengths carrying the same historical letters.
- `D_T|X2` and `D_T|t` are properties of the canonical compact physical selector, not generic `D` or `D_min`.
- The size bound `D_T<=B^(1/2)` alone does not improve the existing `B^(41/42+o(1))` upper bound; the source explicitly isolates square-cancellation/root-sign distribution as the missing information.

## PROVENANCE NOTES

- Stage14-s6-06 is the first merged source eliminating the earlier auxiliary s3 variables and expressing the compact selector entirely in physical face/space-diagonal variables.
- It depends only on merged s6-05 and earlier merged identities; open Stage14-4bk is not used as provenance for this card.
