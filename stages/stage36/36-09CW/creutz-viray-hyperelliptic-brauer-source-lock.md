# Creutz--Viray hyperelliptic 2-torsion Brauer source lock

## Source

Brendan Creutz and Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, Manuscripta Mathematica 147 (2015), 139--167, DOI 10.1007/s00229-014-0721-7, arXiv:1403.2924.

Exact source used: Theorem 1.1 and the construction in Sections 1.1 and 2.1 (including Proposition 2.4 for quaternion expansion).

## Frozen theorem interface

Let `K` have characteristic different from 2 and let an even hyperelliptic double cover be written

`C: z^2 = c f(t)`

with `f` squarefree monic. Put `L=K[t]/f`, let `alpha` be the image of `t`, and define

`gamma'(ell)=Cor_{K(C)\otimes_K L / K(C)}((ell,t-alpha)_2)`.

For an even cover, Theorem 1.1 says that `gamma'(ell)` is an unramified element of `Br(C)[2]` exactly when the squareclass norm of `ell` lies in the squareclass of `c`. In particular, when `c=1`, square norm is sufficient and necessary for this construction to land in `Br(C)[2]`.

The paper also shows that the corestriction can be expanded as a finite sum/tensor product of quaternion algebras over the base function field; Proposition 2.4 gives an explicit Euclidean-algorithm formula.

## Stage36 specialization permitted by this lock

The audited physical top genus-three curve has

`C3_p: z^2=(t^2+p^2)(t^2+p^(-2))(t^2+c_p^2)(t^2+c_p^(-2))`,

where `c_p=(p+1)/(p-1)` and retained rational `p` excludes `0,+/-1`. The four quadratic factors are pairwise distinct on the retained rational open and each defines the same quadratic field `Q(i)` after adjoining one root. Thus the branch algebra is

`L_p ~= Q(i)^4`.

For `d in Q^*` and one factor index `j`, let `ell_{d,j}` be the element of `L_p^*` whose `j`-th component is `d` and whose other three components are `1`. Then

`Norm_{L_p/Q}(ell_{d,j})=d^2`,

so the Creutz--Viray norm condition is automatically satisfied. By the projection formula for corestriction of quaternion symbols, the resulting class has the literal representative

`A_{d,j}=(d,t^2+a_j^2)_2 in Br(C3_p)[2]`,

with `a_j in {p,p^(-1),c_p,c_p^(-1)}`.

More generally, a subset `S` of the four factors gives

`A_{d,S}=(d, product_{j in S}(t^2+a_j^2))_2`,

and `S` and its complement differ by `(d,z^2)=0` on the curve.

## Firewalls

This source lock grants only the explicit **unramified class construction** on the fixed hyperelliptic receiver model.

It does **not** prove that any `A_{d,j}` is nonconstant modulo `Br(Q)`, that its evaluation varies on receiver local points, that it lies outside the CU five-root-monomial family after all birational coordinate changes, that one fixed `d` works uniformly in `p`, or that it gives a Brauer--Manin obstruction.

Those are separate Stage36 obligations.
