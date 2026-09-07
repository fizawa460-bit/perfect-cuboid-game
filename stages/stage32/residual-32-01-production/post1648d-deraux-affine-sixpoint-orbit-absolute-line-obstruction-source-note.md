# Stage32 post1648D — Deraux affine six-point orbit absolute-line obstruction

Scope: fixed Stage32 target `g1-d186`, `O=210`, `q'=4`, `Q=602`. This leaf tests whether the missing absolute map `delta_0inf -> L_i` can be recovered without choosing the Koziarz--Rito--Roulleau conjugating automorphism, by adding the explicit affine `G48` action and its distinguished six-point 2-torsion orbit from Deraux.

The answer is no. The affine six-point orbit is stronger data than the unmarked linear group used in post1648C, but it still leaves all six permutations of the three nonzero Richelot-kernel lines.

## Locked Stage32 inputs

- post1648B fixes the exact Bolza branch-point actions of
  `phi2(x)=-(x+i)/(1+i*x)` and `phi6(x)=i*(x-1)/(x+1)`.
- post1648C fixes the even-subset `J(C0)[2]` model and principal Weil form.
- the retained principal Rosati lock fixes the target lattice basis
  `(e1,e2,r*e1,r*e2)`, `r^2=-2`, and its principal Riemann form.
- the retained marked-W gauge asset fixes
  `L1=r*e1`, `L2=r*e2`, `L3=r*(e1+e2)` with residues `73,97,235`.

## Deraux affine source lock

Primary source: Martin Deraux, *Non-arithmetic ball quotients from a configuration of elliptic curves in an Abelian surface*, arXiv:1611.05112v2.

Use exactly Section 4.

Definition 4.1 gives affine generators, in homogeneous affine coordinates,

`R1 = [[1,0,0],[0,1,0],[0,1-r,-1]]`,

`R2 = [[1,0,0],[0,-1+r,2],[0,1+r,1-r]]`,

`R3 = [[1,0,0],[(1+r)/2,1,-1-r],[1,0,-1]]`,

where `r=i*sqrt(2)`. The paragraph immediately following Definition 4.1 states that the lower-right `2x2` block is the linear part and the lower-left `2x1` block is the translation part. The translation lattice is

`Lambda=(Z+r Z)^2`.

Proposition 4.2 and the following paragraph identify the finite action as

`F=G/T_Lambda`

on `A=C^2/Lambda`, with order `48` before the central `-1` becomes trivial on `A[2]`.

Proposition 4.4 and Table 2 give an orbit with isotropy order `8`, represented by

`(1/2,(1+r)/2)`.

Its orbit therefore has `48/8=6` points. Reduction to `A[2]` in the retained basis gives the representative numerator `[1,1,0,1]`.

Reducing the three affine generators modulo `2 Lambda` gives the exact affine transformations stored in the certificate. Their linear parts all preserve the locked principal Weil form. They generate a group of order `24` on `A[2]`, as expected because the central `-1` acts trivially on 2-torsion.

The orbit of `[1,1,0,1]` is exactly

`{[0,0,1,0],[0,0,1,1],[1,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,1]}`.

## Curve-side six-point affine action

Use the post1648C coordinate basis represented by the pair classes

`{+1,-1}`, `{+1,+i}`, `{+1,-i}`, `{+1,0}`.

Taking `infinity` as the zero Abel--Jacobi point, the six Weierstrass points have coordinates

- `+1  -> [1,1,1,1]`
- `-1  -> [0,1,1,1]`
- `+i  -> [1,0,1,1]`
- `-i  -> [1,1,0,1]`
- `0   -> [1,1,1,0]`
- `infinity -> [0,0,0,0]`.

The post1648B exact point permutations induce affine maps. Their linear parts are exactly the post1648C `phi2` and `phi6` matrices; both translations are `[1,0,1,1]`, the coordinate of the image of `infinity` (`+i`). The generated affine group again has order `24`.

The three Richelot differences remain

`Z1=[1,0,0,0]`, `Z2=[0,1,1,0]`, `Z3=[1,1,1,0]`.

## Koziarz--Rito--Roulleau conjugacy scope

Koziarz--Rito--Roulleau, *The Bolza curve and some orbifold ball quotient surfaces*, arXiv:1904.00793v4, Section 4 Corollary 6, proves that the curve-induced group `H48` and Deraux's `G48` are conjugate by an automorphism `g` of `A`:

`H48 = g G48 g^{-1}`.

The following paragraph explicitly permits replacing the Bolza embedding by composition with this `g` before identifying the two actions. The cited passage does not give a distinguished matrix of `g` on the retained `A[2]` coordinates. Therefore the correct finite question is to enumerate every affine symplectic conjugacy compatible with the explicit six-point orbit, not to select one by naming convention.

## Exact finite audit

Enumerate all `|GL_4(F2)|=20160` invertible linear maps and all 16 translations.

1. Require the linear map to carry the source Weil form to the retained target Weil form.
2. Require the affine map to send the six source Weierstrass points onto Deraux's explicit six-point orbit.
3. Require conjugation of the full source affine group onto the full Deraux affine group.

There are:

- `720` symplectic affine maps satisfying the six-point-set condition;
- exactly `48` full affine-group conjugacies.

Every one of the 48 carries the source Richelot plane onto the already-retained plane

`span_F2(r*e1,r*e2)`.

But their induced bijections on the three nonzero lines realize all `3! = 6` permutations, each exactly eight times. In particular

`Z3=delta_0inf`

occurs as `L1`, `L2`, and `L3` among valid affine conjugacies.

Therefore the explicit Deraux six-point 2-torsion orbit plus the full affine action still does not select an absolute retained line.

## Decision / anti-loop boundary

Current arithmetic credit remains

`survivors=[73,97,235]`, `Q602_excluded=false`, `O210_excluded=false`.

Do not repeat any of the following as a proposed absolute-marking route:

- unmarked full linear `J[2]` group conjugacy (closed by post1648C);
- unmarked affine group conjugacy;
- matching the six Weierstrass points merely as the unique Deraux isotropy-8 orbit.

The remaining load-bearing datum must distinguish one conjugacy inside the 48, for example an explicit matrix for the Koziarz--Rito--Roulleau `g` on `A[2]`, or enough named curve/lattice generator bindings to kill the residual `S3` action on the three Richelot lines.

No controller, receiver, route, theorem, endpoint, or perfect-cuboid credit is released here.
