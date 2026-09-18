# Stage32 MB104 — W16-A1 solo: direct ramification-image pushforward — 2026-09-19

Status: **A1 CLOSED NEGATIVE AS A DIRECT-IMAGE ENHANCEMENT / W16 STILL OPEN / NO MATHEMATICAL CREDIT**

## Scope

This checkpoint advances W16-A1 only.

Start from the exact normalization ramification divisor

`R_phi` on `E`, `deg R_phi=112l`,

and push it directly through the normalization

`nu:E->C subset S`.

The goal is to decide whether the direct finite pushforward retains branch/multiplicity/trace information in a canonical surface object stronger than the A2 reduced lci support `Z_red`, while staying within the linear `112l` budget.

## 1. The exact pushforward object is a module, not generally a scheme

Define

`M := nu_* O_{R_phi}`.

Because `nu` is finite, `M` is a canonical finite-length `O_C`-module and

`length(M)=length(O_{R_phi})=112l`.

So direct pushforward preserves the exact linear budget.

The problem is cyclicity. If two or more ramification preimages lie over one singular carrier point, the corresponding local summands survive separately in `M`. The module then needs more than one local generator and cannot be the structure sheaf `O_Z` of a zero-dimensional subscheme.

## 2. Exact two-branch collision model

Work in the smooth surface local ring

`R=k[[x,y]]`

with nodal carrier

`A=R/(xy)`.

Suppose the ramification divisor has branch lengths `m,n>=1` on the two normalization branches. The direct pushforward module is

`M_mn = R/(y,x^m) direct_sum R/(x,y^n)`.

It has

`length(M_mn)=m+n`

and

`dim_k M_mn/(x,y)M_mn =2`.

Hence it needs two local generators and is not cyclic. In particular, it is not `O_Z` for any zero-dimensional subscheme `Z` of the surface.

## 3. The canonical scheme functors either thicken or collapse

### Annihilator support

The annihilator is

`Ann_R(M_mn)=(xy,x^m,y^n)`.

The quotient has length

`m+n-1`.

If both `m,n>1`, the ideal is genuinely three-generated in the two-dimensional regular local ring, so the zero-dimensional scheme is not lci.

If one branch length equals one, one generator becomes redundant and the annihilator scheme is curvilinear lci, but it has already collapsed part of the branch information.

### Zeroth Fitting scheme

Using multiplicativity of zeroth Fitting ideals for direct sums,

`Fitt_0(M_mn)`
` =(y,x^m)(x,y^n)`
` =(xy,x^(m+1),y^(n+1))`.

The quotient has length

`m+n+1`.

It has the same underlying support but is thicker than the exact module length and is again non-lci in the genuine two-branch case.

This is the standard Fitting phenomenon: `Fitt_0(M)` has the same set-theoretic support as `M`, but it can carry a thicker scheme structure. See Stacks Project tags `07ZA` and `0C3C`.

### Reduced support

Taking the radical gives

`(x,y)`.

This is a length-one lci point on the smooth surface. Globally this is exactly the A2 object

`Z_red=(nu(R_phi))_red`.

Thus the only canonical direct-image scheme that is automatically lci at arbitrary collisions is the reduced support already retained in A2.

## 4. The simplest collision already shows the trichotomy

Take `m=n=1`: two reduced ramification points upstairs map to one node downstairs.

Then

- exact pushforward module length = `2`, but it is two-generated and not `O_Z`;
- annihilator/reduced-support scheme length = `1`, lci but branch information is lost;
- zeroth Fitting scheme length = `3`, thicker and non-lci.

So even the minimal collision has no canonical length-two lci direct-image scheme.

## 5. Trace and norm do not create the CB relation

The finite ramification algebra over one reduced image point has the form

`prod_i k[t_i]/(t_i^(m_i))`.

For a surface function or local section with value `s(p)` at the image point, multiplication on each factor is upper triangular with diagonal entry `s(p)`. Therefore the algebra trace is

`Tr(s)=sum_i m_i * s(p)`.

The norm is

`Nm(s)=s(p)^(sum_i m_i)`.

Thus both canonical scalarizations factor through the ordinary reduced point value. They do not produce a new linear relation among evaluations of `|D_l|` on `Z_red`.

The trace-zero part does remember branch/nilpotent differences, but those data are invisible to reduced point evaluation. B2 already showed that the missing Serre class is precisely an all-nonzero annihilating vector for the reduced evaluation map. Trace/norm do not supply such a vector.

## 6. Jet/residue refinements do not solve A1 canonically

One can choose residue functionals on the branch Artin algebras that see higher coefficients and branch jets. But those are jet functionals, whereas CB for `Z_red` is a dependency among point values.

To turn branch jets into a surface scheme one must keep a nonreduced union of branch jets. The direct union ideal in the node model is exactly

`(xy,x^m,y^n)`.

When both branch lengths exceed one this is not lci. Choosing one branch or one quotient to restore lci is a branch choice, not a canonical direct descent.

Therefore branch orientation/residue information cannot be retained canonically in the Hartshorne--Serre lci object without either:

- losing the branch information and returning to `Z_red`, or
- keeping a multi-branch thickening that is not lci / may exceed the usable length budget.

## A1 disposition

`W16-A1 = CLOSED_NEGATIVE_AS_DIRECT_IMAGE_ENHANCEMENT`.

This does **not** close W16. A2 remains a genuine positive asset:

`Z_red` is canonical relative to `phi`, nonempty, lci, and has length `<=112l`.

What A1 proves is that direct pushforward, annihilator/Fitting, trace, norm, or branch-jet packaging does not add a canonical CB-producing structure beyond A2.

The next useful solo branch is therefore the actual remaining load-bearing problem:

`W16-B1 = CB-first`.

## Firewalls

- No statement that `Z_red` fails CB.
- No statement that every imaginable noncanonical thickening fails.
- No locally-free Serre extension is proved.
- No `l>=2` exclusion.
- No MB104/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
