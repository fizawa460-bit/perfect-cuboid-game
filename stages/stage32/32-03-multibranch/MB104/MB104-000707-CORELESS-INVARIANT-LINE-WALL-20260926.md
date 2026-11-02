# Stage32 MB104 — 000707 coreless invariant-line shortcut wall

Status: **EXACT PRE-AUDIT ROUTE CLOSURE / ZERO CREDIT / CORELESS CASE STILL OPEN**

## Scope

Continue only the retained balanced e=2 branch after rational-core closure.

The current surviving structural branch is

```text
CORELESS + NO NONEMPTY CLUMP
```

for the retained etale self-correspondence

```text
C8 <-f1- Z -f2-> C8
```

with diagonal

```text
H=<T',TT'R> ~= (Z/2)^2,
E=Z/H,
R=C8/H ~= P1_r,
pi_H:C8->R,
psi_i:E->R.
```

This note tests, and closes as insufficient, the tempting shortcut

```text
M_1^2 ~= M_2^2
  -> positive invariant line bundle
  -> Krishnamoorthy Cor. 8.13
  -> contradiction.
```

No contradiction follows from that chain.

## 1. Retained factor-line identity

The retained common-H-cover factor-line note defines

```text
M_i := psi_i^* O_R(1)
```

and proves

```text
M_1^2 ~= M_2^2.
```

The quotient square commutes:

```text
pi_H o f_i = psi_i o p,
p:Z->E.
```

Therefore with

```text
L := pi_H^* O_R(2)
```

one obtains

```text
f_1^*L
 = p^*M_1^2
 ~= p^*M_2^2
 = f_2^*L.
```

Thus `L` does define a positive-degree invariant line bundle on the original
correspondence in the sense of Krishnamoorthy Definition 8.1.

## 2. The bundle is exactly canonical

Use the retained affine model of the V4 quotient

```text
u^2=(r^4+4)/4,
v^2=(r^4-4)/4.
```

The map `pi_H:C8->P1_r` has degree 4 and exactly eight order-two branch
values, the roots of `r^4=4` and `r^4=-4`.  Infinity is unramified.

Let `Ram(pi_H)` be the ramification divisor.  The product `u v` has a simple
zero at every ramification point.  At each of the four points over infinity it
has pole order 4.  Hence

```text
Ram(pi_H) ~ 4*pi_H^{-1}(infinity)
          = pi_H^* O_R(4).
```

Hurwitz then gives

```text
K_C8
 ~= pi_H^* K_R tensor O(Ram(pi_H))
 ~= pi_H^* O_R(-2) tensor pi_H^* O_R(4)
 ~= pi_H^* O_R(2)
 = L.
```

So the invariant bundle produced by `M_1^2 ~= M_2^2` is not a new positive
invariant class: it is the canonical invariant bundle.

## 3. Why Corollary 8.13 does not close the branch

Krishnamoorthy Definition 8.1 defines

```text
H^0(mathcal L)
```

to be the space of **invariant sections**, i.e. pairs of sections on the two
base curves whose pullbacks agree under the chosen invariant-bundle
isomorphism.

Corollary 8.13 says that a nontrivial invariant line bundle on a coreless
etale correspondence in characteristic zero has no nonzero **invariant
section**.

The retained identity

```text
M_1^2 ~= M_2^2
```

supplies only the invariant line-bundle isomorphism.  It does not supply
sections `s_1,s_2` with

```text
f_1^*s_1 = f_2^*s_2.
```

Moreover the resulting invariant bundle is `K_C8`, whose invariance is
already automatic for an etale correspondence:

```text
f_i^* K_C8 ~= K_Z.
```

Therefore Corollary 8.13 cannot be invoked from the factor-line identity
alone.

Corollary 8.10 is likewise compatible with the retained geometry: the
positive invariant bundle just found already equals the canonical bundle, so
its required power relation with the canonical invariant bundle is tautological.

## 4. Exact next algebraic interface

The common-H-cover structure does give a stronger function-field interface
than the line-bundle shortcut.

Write the two quotient functions on `E` as `r_1,r_2`.  Because the same
character-labelled H-cover `Z->E` is obtained by pulling back

```text
u^2=(r^4+4)/4,
v^2=(r^4-4)/4
```

along either `r_i`, the two character square classes agree.  Hence there
exist `A,B in k(E)^*` with

```text
r_1^4+4 = A^2 (r_2^4+4),
r_1^4-4 = B^2 (r_2^4-4).
```

Equivalently,

```text
8 = (A^2-B^2) r_2^4 + 4(A^2+B^2).
```

This is the correct next coreless interface: it retains the full two-character
common-cover information, unlike `M_1^2 ~= M_2^2`, which forgets the
sections/divisors.

Any downstream use must still source-lock the character labels and must not
replace equality of square classes by equality of branch divisors.

## Firewalls

- No invariant section is proved.
- No nonempty clump is proved.
- No core is proved.
- The rational-core branch remains closed only by the preceding relative-H
  bidegree gate.
- The coreless/no-clump branch remains open.
- Balanced bulk remains open.
- e=2 remains open.
- No receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit.
- No heavy compute is armed.
- No merge or rebase authorization.

## Literature source

Raju Krishnamoorthy, *Correspondences without a Core*, Algebra & Number
Theory 12 (2018), 1173–1214, DOI 10.2140/ant.2018.12.1173:
Definition 8.1, Corollaries 8.10 and 8.13.
