# Stage13-13fe — R05 Gate E result

> STATUS: `COMPLETE_STAGE12_COUNTING_INTERFACE`
>
> INPUT: Gates A-D complete; Stage12 R09 immutable.
>
> NEXT: `13-13ff` — exact external Hecke/Dirichlet/Vaaler contracts.

## Result

Gate E closes the missing Stage12 interface in R04 without reopening Stage12.

The new proof-facing interface is

```text
stages/stage13/13-13fe/stage12-counting-interface.md
```

and it includes, in one place:

- the exact Stage12 parameter set `D_B` and cutoff `d=h(r^2+s^2)/2<=B`;
- the multiplicity `G(hrs)-1` and raw oriented count;
- the exact Möbius/common-scale definition of `C_prim(B)`;
- the meaning of the Stage12 orientation convention;
- the frozen R09 theorem;
- the full Euler-product definition of `kappa` and the exact identity `eta=pi*kappa`;
- the exact Stage12-to-Stage13 object map;
- the proof that the projection fiber is exactly two;
- the overlap and parity compatibility of that factor two;
- the explicit division between what Stage12 supplies and what Stage13 proves.

## Frozen Stage12 theorem

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3,
\qquad
\eta=\pi\kappa.
\]

The imported object is only the primitive oriented distinguished-face record count.

## Exact projection

For each canonical face category `q`,

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

for every `B`, and therefore

\[
C_{\rm prim}(B)=2\sum_q A_q(B).
\]

The fiber consists exactly of the two orders of the distinguished face legs. The Stage12 outer parameter already satisfies `r<s`, so it contributes no extra order. The same two-element fiber holds separately in the parity strata and remains exact on multi-face objects because raw incidence retains the distinguished face.

## Finite checksum

At `B=100000`,

```text
projected Stage12 = (168424, 86472, 81520)
canonical raw     = ( 84212, 43236, 40760)
```

so every coordinate and the total satisfy the exact factor-two identity.

## Scope

The finite checksum is consistency evidence only. The object-fiber argument is the proof.

No directional asymptotic is attributed to Stage12. Stage12 remains frozen at R09; the category projection, directional constants and overlap removal remain Stage13 mathematics.

```text
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE12_R09_BUNDLE=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
STAGE12_R09_CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_CUTOFF=d<=B
STAGE12_THEOREM=C_prim(B)~kappa/(12*pi)B(log B)^3
KAPPA_EULER_PRODUCT_EXPLICIT=true
ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
PROJECTION_PARITY_STRATIFIED=true
EXTRA_2ADIC_PROJECTION_FACTOR=false
MULTI_FACE_FACTOR_TWO_EXACT=true
C_PRIM_Q_PROJ=2*A_q
C_PRIM_TOTAL=2*sum_q_A_q
STAGE12_REOPENED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13ff
```