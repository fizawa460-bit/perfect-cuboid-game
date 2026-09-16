# Stage32 MB104 source note — explicit residual Kummer coordinate on `C8/H`

Status: **EXTERNAL PUBLISHED SOURCE ADAPTER / EXACT THETA ACTION AND PARAMETRIZATION ONLY / NO CLOSURE / NO CREDIT**

## Source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495 (2013), especially Theorem 2.1, Lemma 2.3, Theorem 2.4, and Section 4.

Only the following published formulas are imported.

Write, for one factor variable `w`,

```text
a = theta00(w),
e = theta10(w),
b = theta01(w),
c = theta00(2w),
d = theta10(2w).
```

The theta relations include

```text
a^2 = c^2+d^2,
b^2 = c^2-d^2,
e^2 = 2*c*d.                                  (THETA)
```

For the generators `T,T',R` of `Gamma[4]/Gamma[8] ~= (Z/2)^3`, Lemma 2.3 gives the diagonal sign actions on the ordered basis `(a,e,b,c,d)`:

```text
T  : (+,-,+,+,+),
T' : (+,+,-,+,+),
R  : (+,+,+,-,-).                             (ACT)
```

For two factor variables `z,w`, Theorem 2.4 gives, with
`x=theta00(2z)`, `y=theta10(2z)`, `X=theta00(2w)`, `Y=theta10(2w)`,

```text
C  = xX+yY,
W1 = yX+xY,
W2 = i*(yX-xY),
W3 = xX-yY,                                   (BOX)
Z1 = theta01(z)*theta01(w),
Z2 = theta00(z)*theta00(w),
Z3 = theta10(z)*theta10(w).
```

Section 4 defines the free index-two subgroup `Gamma'[4]/Gamma[8] ~= (Z/2)^2`; no stronger Stage32 identification is imported from that statement here.

## Derived fixed-type identification used downstream

Using `(ACT)` and `(THETA)`, the projective fixed locus of `T` on `C8` is `e=0`, that of `T'` is `b=0`, and that of `TT'R` is `a=0`. Under `(BOX)` these are respectively the three diagonal node types

```text
Z3=0, Z1=0, Z2=0.
```

This fixed-type identification is an elementary consequence of the imported sign matrices and theta relations; it is not quoted as a separate theorem of the paper.

## Firewall

- This note imports no branch-to-sheet assignment for a Stage32 carrier.
- It does not identify conductor normalization preimages.
- It does not assert a rational-point or arithmetic-field statement.
- All downstream use here is over the complex modular curve unless an explicit field adapter is separately supplied.
- No Stage32 credit or merge authorization follows from this source note.
