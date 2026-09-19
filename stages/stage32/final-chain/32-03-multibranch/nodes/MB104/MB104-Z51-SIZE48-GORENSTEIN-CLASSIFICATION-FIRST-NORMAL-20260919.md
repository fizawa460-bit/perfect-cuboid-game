# MB104 Z51 — size48 Gorenstein cover classification preflight and first-normal residual — 2026-09-19

Status: **PRE-AUDIT SOURCE-CLASSIFICATION WALL + EXACT FIRST-NORMAL RESIDUAL / NO CREDIT**

## Input

Use the exact Z50 canonical-cover resolution

```text
D =
E_1(-2,g=1)
-- R_1(-2)
-- R_2(-2)
-- R_3(-2)
-- R_4(-2)
-- R_5(-2)
-- E_2(-2,g=1),
```

with

```text
j(E_1)=j(E_2)=1728,
Z=D is the fundamental cycle,
p_a(Z)=2,
Z_K=2Z.
```

The two elliptic endpoints each have one marked attachment point, denoted p_1,p_2.

## 1. Exact normal bundle of each elliptic endpoint

Because the canonical cover germ is Gorenstein and Z50 gives discrepancy -2 on every exceptional
component,

```text
K_X = f^*K_{Y#} - 2D.
```

Restrict to an elliptic endpoint E with marked attachment point p.

Since `f^*K_{Y#}|E` is trivial and `K_E` is trivial,

```text
K_X|E ~= O_E(-2D|E),
K_X|E ~= N_{E/X}^{-1}
```

by adjunction.

Now

```text
O_E(D) ~= N_{E/X} tensor O_E(p).
```

Therefore

```text
N^{-1}
 ~= (N tensor O(p))^{-2}
 ~= N^{-2} tensor O(-2p),
```

so

```text
N_{E/X} ~= O_E(-2p).                            (END-NORMAL)
```

Thus the elliptic endpoint data are exactly

```text
(E_1728, p, O_E(-2p)).
```

There is no remaining Pic^(-2) ambiguity in the endpoint normal bundle.

## 2. First-normal Picard layer of the full exceptional chain

For the Cartier exceptional divisor D on the smooth resolved cover,

```text
I_D^n/I_D^(n+1) ~= O_D(-nD).
```

Set

```text
L_n=O_D(-nD).
```

On either elliptic endpoint,

```text
D.E=-1
```

and (END-NORMAL) gives more precisely

```text
L_n|E ~= O_E(np).
```

On each of the five interior rational -2 components,

```text
D.R_j=0,
L_n|R_j ~= O_{P1}.
```

### n=1

For `O_E(p)` on an elliptic curve,

```text
h0=1,
h1=0,
```

and its unique section vanishes at the marked point p.  Hence its evaluation at the attachment
node is zero.

Normalize the seven-component chain.  The five rational components contribute five independent
constants.  Their node-difference map has rank five inside the six node-value slots.  Since the
two elliptic endpoint sections evaluate to zero at the end nodes, the normalization exact
sequence leaves a one-dimensional cokernel:

```text
H^1(D,O_D(-D)) ~= C.                            (FIRST-NORMAL)
```

### n>=2

For `n>=2`, the line bundle `O_E(np)` has degree at least two and is globally generated.
Therefore each elliptic endpoint can prescribe its attachment-node value arbitrarily.

Together with the constants on the rational chain, the normalization evaluation map to the six
node slots is surjective. Hence

```text
H^1(D,O_D(-nD))=0,  n>=2.                       (HIGHER-VANISH)
```

So the additive Picard transition kernel is concentrated at the first normal layer:

```text
ker(Pic(2D)->Pic(D)) ~= C,
Pic((n+1)D)->Pic(nD) has zero infinitesimal kernel for n>=2.
```

This is an exact residual formal parameter.  It is **not** by itself a classification of analytic
surface neighborhoods.

## 3. Literature classification preflight

The closest source-complete literature found is the fundamental-genus-two work of Kazuhiro Konno:

- chain-connected decomposition of the canonical cycle for numerically Gorenstein singularities
  of fundamental genus two;
- Yau-cycle/canonical-cycle relations;
- for certain extremal general-type singularities, rough resolution-graph classification and
  formulas for geometric genus, multiplicity and embedding dimension.

These results organize the numerical/cycle theory of `p_f=2` singularities, but the located
sources do not provide an analytic normal form or complete local equation classification for the
specific marked resolution

```text
(E_1728,-2)--5(P1,-2)--(E_1728,-2),
Z_K=2Z.
```

The standard weakly-elliptic/maximally-elliptic Gorenstein classification is not applicable:
it concerns fundamental genus one and, in the strongest graph-determined results, rational
homology sphere links.  The present resolution has positive-genus exceptional components and
`p_f=2`.

Therefore no source-complete hypersurface, complete-intersection, splice, quotient, or
quasihomogeneous normal form is currently justified.

## 4. Exact residual interface

The marked first-order component data are now fixed:

```text
elliptic complex structures: j=1728,
elliptic marked points: fixed,
elliptic normal bundles: O(-2p),
rational components: P1 with O(-2),
dual graph: fixed tree,
canonical cycle: 2D.
```

The only explicitly detected nonzero finite-formal Picard layer is the one-dimensional class
(FIRST-NORMAL).

A future analytic classification must determine whether the actual cuboid canonical-cover
neighborhood selects a distinguished value of this first-normal class and whether that value
controls the analytic contraction germ.  The required cuboid-side datum is an explicit
first-normal transition coefficient for the resolved canonical cover.

No claim is made that `H^1(D,O_D(-D))` is the full equisingular deformation space of the
surface germ.

## 5. Route disposition

```text
source-complete analytic normal form found = false,
marked endpoint normal bundles exact       = true,
first-normal formal residual dimension     = 1,
higher additive Picard residuals           = 0.
```

Thus Z51 does not reopen local Euler/Chern formulas yet.  It narrows the missing analytic datum
from an arbitrary germ to a first-normal transition coefficient plus any genuinely non-Picard
analytic neighborhood data not captured by this calculation.

## External source anchors

- Kazuhiro Konno, work on chain-connected decomposition of the canonical cycle for numerically
  Gorenstein surface singularities of fundamental genus two.
- Kazuhiro Konno, *On the Yau cycle of a normal surface singularity*.
- Kazuhiro Konno, *Certain normal surface singularities of general type*.

These sources are used only for the classification-scope statement above; the normal-bundle and
formal-layer computations are exact consequences of the retained Z50 resolution data.

## Firewalls

```text
endpoint_normal_bundle_exact=true
first_normal_picard_residual_dimension=1
higher_picard_residual_dimension_zero=true
full_analytic_moduli_identified=false
explicit_affine_normal_form_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
