# Stage14-e10 derivation notes

This note is intentionally short. The complete proof is in `result.md`; the purpose here is to freeze the three crosswalks most likely to be reused downstream.

## e6 shells -> e9 states

For odd `p`,

\[
a=v_p(S_1)=|v_p(q_1)|,\qquad b=v_p(S_2)=|v_p(q_2)|.
\]

For `p=2`, a unit `q_i` gives denominator valuation zero while a nonunit gives `|v_2(q_i)|+1`.  Partitioning `(a,b)` into `none,G,U,V,GU,GV` and summing the e6 weighted shells gives the exact e10 six-state law.

## state G -> residue blocker

For odd `p`, state `G` makes `x,y` p-adic units. Their leading unit residues are uniform under the local invariant measure. With `r=x/y`, third-face squareness requires `r^2+1` to be a square or zero modulo `p`. The nonsquare fraction is

\[
\frac{p-\chi_4(p)}{2(p-1)}.
\]

## e8 K3 -> Huang fibration theorem

The e8 Euler-brick compactification is the minimal resolution of a double cover of

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

branched in `-2K_Y`. The resolved surface is a proper smooth geometrically integral K3 and the map to `Y` is dominant proper and generically finite of degree `2`. This is the exact hypothesis bridge to Huang v3, Theorem 1.6(1).
