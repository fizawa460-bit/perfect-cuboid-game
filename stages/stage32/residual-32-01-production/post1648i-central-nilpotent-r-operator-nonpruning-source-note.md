# Stage32 post1648I central nilpotent operator nonpruning

Scope: fixed `g1-d186`, `O=210`, `q'=4`, `Q=602`. This is an absolute-marking route closure only.

post1648C leaves 48 symplectic conjugacies between the source Bolza `J(C0)[2]` model and the retained `(e1,e2,r*e1,r*e2)` model. All 48 already send the source Richelot plane `W` to `span(r*e1,r*e2)`, but realize all six permutations of its three nonzero lines.

There is a natural stronger finite test that does not require asserting an unsupported geometric self-isogeny. On the source module, ask for a nonzero endomorphism `N` that

- commutes with the full order-24 curve action used in post1648C;
- satisfies `N^2=0`;
- has rank two;
- has `ker(N)=im(N)=W`.

Exact enumeration of `M4(F2)` shows this `N` is unique. On the retained module, scalar multiplication by `r=sqrt(-2)` reduces modulo two to a rank-two square-zero operator with `ker=im=span(r*e1,r*e2)`, and it is likewise the unique nonzero operator with these properties in the full retained-group centralizer.

The decisive check is negative: every one of the 48 post1648C symplectic group conjugacies sends the unique source operator `N` to the retained scalar-`r` operator. Therefore even granting the stronger conditional identification `N = r mod 2` gives zero pruning: 48 conjugacies and all six W-line bijections remain.

This note deliberately does **not** claim that the source operator has independently been source-locked as the geometric `sqrt(-2)` self-Richelot endomorphism. The negative result is stronger: even if that identification were supplied, it would not select `delta_0inf` among `L1,L2,L3`.

Current credit remains `[73,97,235]`; `Q602_excluded=false`; `O210_excluded=false`. The next admissible datum must be noncentral/marked, e.g. a named curve automorphism bound to a named retained lattice generator.
