# MB104 Z51 — size48 canonical cover as an even Gorenstein type-(ii.a) singularity — 2026-09-19

Status: **PRE-AUDIT SOURCE-CLASSIFIED EVEN GORENSTEIN / MULTIPLICITY-EMBEDDING DIMENSION EXACT / NO CREDIT**

## Input from Z50

The minimal good resolution of one size48 canonical-cover singularity has reduced exceptional cycle

```
Z =
E_L(-2,g=1)
 -- C1(-2)
 -- C2(-2)
 -- C3(-2)
 -- C4(-2)
 -- C5(-2)
 -- E_R(-2,g=1).
```

Z50 proves

```
Z^2=-2,
p_a(Z)=2,
Z_K=2Z,
```

and the germ is Gorenstein.

Let

```
Gamma=C1+C2+C3+C4+C5.
```

Then Gamma is the fundamental cycle of the rational double point chain A5.

## 1. Fundamental genus and nef canonical sheaf on Z

By definition,

```
p_f=p_a(Z)=2.
```

For the dualizing line bundle of Z,

```
deg(K_Z|E_L)=deg(K_Z|E_R)=1,
deg(K_Z|C_i)=0.
```

Indeed K_X.E_L=K_X.E_R=2 and Z.E_L=Z.E_R=-1, while K_X.C_i=0 and
Z.C_i=0.

Thus K_Z is nef.

Konno's fundamental-genus-two even-singularity results apply.  For a numerically Gorenstein
singularity with p_f=2 and nef K_Z, the arithmetic genus is p_a=2 and the canonical cycle is 2Z
when Z^2=-2.  This independently matches the exact Z50 computation.

Because the canonical cover germ is Gorenstein, the geometric genus is

```
p_g=3.
```

## 2. Exact Konno type

Take

```
Delta=E_L,
Delta_1=E_R,
Gamma=C1+...+C5.
```

Then

```
Z=Delta+Gamma+Delta_1,
Delta.Gamma=1,
Delta_1.Gamma=1,
Delta.Delta_1=0,
```

and Gamma is a simple A5 chain of (-2)-curves.

This is exactly Konno Proposition 2.7 type

```
(ii.a):
Z=Delta+Delta_1+Gamma
```

with Gamma the fixed rational-double-point chain of the canonical system.

It is important that this is **not** type A7 in the rational-double-point sense: only the
intersection matrix is the A7 Cartan matrix; the two endpoint curves are elliptic.

## 3. Maximal ideal cycle and multiplicity

For p_a=p_f=2 we have m=1 in Konno's notation.

For type (ii), Theorem 4.1 / Lemma 4.2 gives the maximal ideal cycle

```
F=Z+Gamma.
```

Thus its coefficients along the seven-chain are

```
(1,2,2,2,2,2,1).
```

Direct intersection gives

```
F^2=-4.
```

Konno Corollary 4.7 therefore gives

```
mult(Y#,y#)=4.
```

## 4. Embedding dimension

Konno Lemma 5.6 treats type (II) with m=1 and gives

```
embdim(Y#,y#)=4.
```

Therefore the canonical cover is a two-dimensional Gorenstein local analytic germ with embedding
dimension four:

```
dimension=2,
embedding codimension=2.
```

## 5. Complete-intersection consequence

A codimension-two Gorenstein ideal in a regular local ring is a complete intersection.

Hence the completed local ring has a presentation

```
O^_(Y#,y#)
 ~= C[[x1,x2,x3,x4]]/(f,g)
```

for a regular sequence f,g.

This is the first source-complete structural presentation of the size48 canonical cover.

The equations f,g are not yet identified.

## 6. Quantitative local package now fixed

```
Gorenstein                  true
fundamental genus           2
arithmetic genus            2
geometric genus             3
Konno class                 (ii.a)
fixed RDP chain             A5
canonical cycle             2Z
multiplicity                4
embedding dimension         4
embedding codimension       2
complete intersection       true
explicit equations          unknown
```

## 7. Next leaf

```
MB104-Z52-SIZE48-QUADRATIC-CI-TANGENT-CONE-PREFLIGHT
```

Use multiplicity four plus codimension-two complete-intersection structure.

Target:

1. prove the minimal defining regular sequence has quadratic initial order (2,2);
2. classify the resulting pencil of tangent quadrics compatible with the two j=1728 elliptic end
   neighborhoods and the A5 fixed chain;
3. determine whether the cuboid marked plumbing selects a finite quadratic pencil / explicit
   normal form;
4. if so, feed that analytic model back to the local-Chern/Euler route.

Do not identify the local equations with Konno's sample examples solely from the common type.

## Literature source

Kazuhiro Konno, *Certain normal surface singularities of general type*, Methods and Applications
of Analysis 24 (2017), 71--98.

Used source-level statements:

- Koyama inequality / even singularities;
- p_f=2, nef K_Z and Z^2=-2 -> p_a=2 and Z_K=2Z;
- Proposition 2.7 type (ii.a);
- Gorenstein p_a=p_f=2 -> p_g=3;
- Theorem 4.1 / Corollary 4.7 maximal ideal cycle and multiplicity;
- Lemma 5.6 embedding dimension four for type (II), m=1.

## Firewalls

```
explicit_local_equations_known=false
quadratic_tangent_pencil_classified=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
