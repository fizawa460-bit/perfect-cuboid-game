# Stage32 post-1505 O210 Q602 marked W-line gauge-orbit compression

Scope: fixed recovered V6 class `g1-d186`, retained `O=210`, `q'=4`, `Q=602`. This leaf starts from the hostile-audited Weierstrass/transvection `16 -> 3` boundary. It does **not** identify `[P_0-P_infinity]` with an absolute retained W-line. Instead it proves that the three surviving retained coordinate representatives are one orbit under the exact principal-polarization automorphism action, so a marked gauge may be fixed without loss of geometric generality.

## Audited input

The hostile-audited predecessor has residues

`73, 97, 235`

with respective transvection image lines in

`W=span_F2{r*e1,r*e2}`

```
73  -> L1 = r*e1
97  -> L2 = r*e2
235 -> L3 = r*(e1+e2).
```

The predecessor deliberately did not choose which `Li` is the absolute image of

`delta_0inf=[P_0-P_infinity]`.

## Source-locked principal automorphisms

Primary public source: Sergio Cecotti, *Symplectic Singularities, Color Confinement, and the Quantum Dirac Sheaf*, arXiv:2509.24605v1, Appendix B, equations (B.1)-(B.6), especially (B.1).

Put `r=sqrt(-2)`. Appendix B (B.1) gives, among the maximal Bolza/G12 automorphisms on `Z[r]^2`,

```
b3 = [[-1,-1],[1,0]],
b4 = [[1,1+r],[0,-1]].
```

The already source-locked principal Hermitian form is

```
H = [[2,1+r],[1-r,2]].
```

Direct exact multiplication gives

```
bar(b3)^t H b3 = H,
bar(b4)^t H b4 = H.
```

Thus conjugation by `b3,b4` preserves the principal Rosati involution and every conjugacy-invariant Rosati norm condition, in particular the fixed `Q(T)=602` layer. Both matrices commute with scalar multiplication by `r`, hence preserve `W=ker(r)`.

## Exact action on the three W-lines

Reduce modulo `2`, writing `eps=r mod 2`, so `eps^2=0`. On `W=eps*F2^2`, only the ordinary coefficients of a `Z[r]` matrix act. Hence

```
b3|W = [[1,1],[1,0]],
b4|W = [[1,1],[0,1]].
```

Therefore

```
b3: L1 -> L3 -> L2 -> L1,
b4: L1 -> L1, L2 <-> L3.
```

The induced action is the full `GL2(F2) ~= S3` on the three nonzero W-lines.

## Exact conjugacy of the three Q602 residues

Using the predecessor's exact 8-bit encoding of `M_2(F2[eps]/(eps^2))`, reconstruct each retained 4x4 F2 operator and conjugate it by the exact mod-2 matrices above. The result is

```
b3: 73 -> 235 -> 97 -> 73,
b4: 73 -> 73, 97 <-> 235.
```

Thus `{73,97,235}` is one orbit. More strongly, the pair `(T, im(T-I))` has a unique representative after the gauge condition

```
im(T-I) = L1 = span_F2(r*e1).
```

Indeed:

```
73  -- identity --> 73,  L1 -> L1
97  -- b3      --> 73,  L2 -> L1
235 -- b3^2    --> 73,  L3 -> L1.
```

So the canonical marked-gauge representative is residue `73`.

## Meaning of `3 -> 1`

This is **orbit compression, not arithmetic exclusion**. It does not prove that two of the three residues are impossible in a pre-existing absolute retained marking. Rather, the current source locks leave the individual W-line unmarked; changing that retained marking by a principal Bolza automorphism changes `T` and `delta` simultaneously. The three coordinate residues therefore represent one marked-equivalence class.

Authorized credit is exactly:

```
Q602_THREE_RESIDUES_ONE_MARKED_GAUGE_ORBIT=true
CANONICAL_GAUGE_DELTA_LINE=L1
CANONICAL_GAUGE_RESIDUE=73
Q602_EXCLUDED=false
O210_EXCLUDED=false
```

No `3 -> 1` **exclusion** credit is claimed. O212+ remains blocked. No heavy compute, receiver, route, theorem, or endpoint credit follows.

## External marking boundary

Cecotti Appendix B also displays the Bolza curve `y^2=x^5-x` and explicit curve automorphisms, but it does not source-lock an individual correspondence between the three Richelot root-pair classes and `(r*e1,r*e2,r*(e1+e2))` in the retained Stage32 basis. That missing absolute adapter is therefore not invented here and is no longer needed merely to choose a canonical representative of the single orbit.