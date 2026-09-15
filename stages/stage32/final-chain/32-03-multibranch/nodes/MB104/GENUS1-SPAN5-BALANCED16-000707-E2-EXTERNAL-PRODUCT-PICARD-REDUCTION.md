# Stage32 MB104 — `000707000f0f` e=2 external-product Picard reduction

Status: **RETAINED CANDIDATE CONSEQUENCE OF ROSATI ZERO CORRESPONDENCE / FINITE `G`-INVARIANT FACTOR-PICARD TORSORS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

This note consumes the retained candidate conclusion

```text
Phi_Z=0
```

for the product image `Zbar subset P=C8 x C8`, together with the retained product geometry

```text
Zbar ~ Tdiag(Zbar),
H_diag stabilizes Zbar,
G=<H,T>,
deg(f_1)=deg(f_2)=28l.
```

It does not assume that the e=2 carrier exists.

## 1. Picard decomposition on a product of curves

Fix basepoints on the two copies of `C8`.  For a line bundle `L` on

```text
P=C8 x C8
```

its restrictions to the two basepoint fibres give two factor line bundles, while the normalized residual part gives the standard correspondence homomorphism between the two Jacobians.  Equivalently, after rigidification, the Picard group is separated into

```text
factor Picard data  +  Hom(J(C8),J(C8)) correspondence data.
```

For the divisor line bundle

```text
L_Z=O_P(Zbar),
```

the cross component is exactly the Jacobian correspondence `Phi_Z`, up to the harmless sign convention in the rigidification.  Therefore the retained candidate equality

```text
Phi_Z=0
```

forces an actual external-product decomposition

```text
O_P(Zbar) ~= p_1^* A tensor p_2^* B                 (EXT)
```

for line bundles `A,B` on `C8`.

The two projection degrees are `28l`, so

```text
deg A = deg B = 28l.                               (DEG)
```

No numerical-only replacement is being made here: algebraically trivial line bundles on a product of two curves already lie in `Pic^0(C8) x Pic^0(C8)` and are absorbed into `A,B`.

## 2. The factor classes are full-`G` invariant

For every `h in H`, the retained component stabilizer gives

```text
(h x h)^* O_P(Zbar) ~= O_P(Zbar).
```

The retained product linearization also gives

```text
(T x T)^* O_P(Zbar) ~= O_P(Zbar).
```

Apply `(EXT)`.  If

```text
p_1^*A' tensor p_2^*B' ~= p_1^*A tensor p_2^*B,
```

restriction to `C8 x {q}` and `{q} x C8` shows separately that `A'~=A` and `B'~=B`.  Hence

```text
h^*A ~= A,  h^*B ~= B       for all h in H,
T^*A ~= A,  T^*B ~= B.
```

Since `G=<H,T>`, both factor classes lie in

```text
A,B in Pic^(28l)(C8)^G.                            (G-FIX)
```

Thus the previous product-surface problem has collapsed to two invariant line-bundle classes on the genus-five factor.

## 3. The invariant degree-`28l` ambiguity is finite 4-torsion

Use the retained support-specific subgroup

```text
H=<s1,s2> ~= (Z/2)^2.
```

The retained quotient geometry has `s1,s2` with eight fixed points each, disjoint fixed sets, and `s1*s2` fixed-point-free.  Riemann--Hurwitz for `C8 -> C8/H` gives

```text
2*5-2 = 4(2g(C8/H)-2) + 16,
```

hence

```text
g(C8/H)=0.
```

Therefore the identity component of `J(C8)^H` is zero.  The norm endomorphism

```text
N_H=sum_(h in H) h^*:J(C8)->J(C8)
```

has connected image contained in the finite fixed subgroup, so `N_H=0`.  For any `H`-fixed point `tau` of the Jacobian,

```text
0=N_H(tau)=4 tau.
```

Consequently

```text
J(C8)^G subset J(C8)^H subset J(C8)[4].            (FIX4)
```

Whenever one `G`-invariant degree-`d` line bundle exists, `Pic^d(C8)^G` is therefore a finite torsor under `J(C8)^G`, and any two such classes differ by 4-torsion.

## 4. Explicit reference classes for every `l`

The canonical bundle `K=K_C8` is `G`-invariant and has degree `8`.

If `l` is even, put

```text
A_ref(l)=K^(7l/2),
deg A_ref(l)=28l.
```

If `l` is odd, choose a point fixed by one of the singular involutions, say `s1`.  No independent nontrivial element can fix the same point, because the product would then also fix it while the remaining nonidentity elements in the retained action are fixed-point-free.  Its full `G`-orbit therefore has size `4`; let `R` be the reduced orbit divisor.  Then `O(R)` is `G`-invariant of degree `4`, and

```text
A_ref(l)=O(R) tensor K^((7l-1)/2),
deg A_ref(l)=4+8(7l-1)/2=28l.
```

Thus in both parity classes every candidate factor is of the form

```text
A ~= A_ref(l) tensor tau_1,
B ~= A_ref(l) tensor tau_2,
tau_1,tau_2 in J(C8)^G subset J(C8)[4].            (FINITE)
```

Since `g(C8)=5`, the crude ambient bound is

```text
|J(C8)[4]|=4^(2g)=4^10,
```

so the ordered factor-pair ambiguity is at most `4^20`, independent of `l`.  The actual `G`-fixed subgroup may be much smaller.

## Route consequence

The active e=2 product class no longer has a positive-dimensional Picard ambiguity once the Rosati-zero candidate is accepted.  The remaining factor-line-bundle ambiguity is a finite, `l`-uniform 4-torsion problem:

```text
(tau_1,tau_2) in J(C8)^G[4] x J(C8)^G[4].
```

A useful next target is therefore an exact computation of `J(C8)^G[4]` from the retained explicit `G` action, followed by a test of which factor pairs can support an irreducible divisor with the `000707` support passport and the retained common-etale normalization.

This finite reduction is an alternative continuation to evaluating every conductor preimage separately; it does not supersede the direct conductor-pair route unless the finite invariant-Picard test yields an obstruction.

## Firewalls

- This note inherits the candidate/audit status of the Rosati-zero and product-linearization leaves.
- `Phi_Z=0` does not mean `O_P(Zbar)` is trivial; it removes only the cross/Jacobian component.
- `G`-invariance of `A,B` is invariance of line-bundle classes; no unproved `G`-linearization is assumed.
- The bound `4^20` is only a crude ambient cardinality bound, not an enumeration or existence count.
- No claim that any displayed factor pair has a section whose zero divisor is the required irreducible `Zbar`.
- No conductor sign or weighted opposite-sheet bound is computed.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
