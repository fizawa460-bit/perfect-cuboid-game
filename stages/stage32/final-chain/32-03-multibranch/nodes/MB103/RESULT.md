# Stage32 MB103 — exact Aut(S) node-profile quotient and orbit invariants

Status: **RETAINED CHECKPOINT / NO RECEIVER CREDIT**

## Scope

This node supplies the symmetry adapter required by the `R29-LG2-MB` multibranch lane. It does not prove a finite degree window and it does not start Picard enumeration.

Let `S` be the smooth minimal resolution of the cuboid surface and let `E={E_1,...,E_48}` be the exceptional configuration over the 48 singular points. Stage29 already source-locks Michael Stoll's verification code at

```text
repo   = MichaelStollBayreuth/Verification
commit = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file   = Cuboids/cuboids.magma
blob   = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The fixed source constructs the 48 singular points, gives nine explicit coordinate substitutions generating the automorphism action, computes their permutations on the known curves plus the 48 singularities, descends the action to `Pic(S)`, and constructs `AutS`; the audited Stage29 record fixes `#Aut(S)=1536` as the symmetry action used for orbit reduction.

## Geometric node packet

For a multibranch carrier with strict transform `D`, the MB101/MB102 record at node `i` is not reduced merely to `(r_i,M_i)`. Define the geometric node packet `Q_i(D)` to retain:

- `r_i`, the number of normalization branches over the node;
- every branch multiplicity `m_ij=D_branch.E_i`;
- the partition of those branches by their **actual resolved landing point** on `E_i`;
- intrinsic branch delta values at each resolved landing point;
- pairwise local intersection multiplicities for branches sharing that resolved point;
- the resulting exceptional local contribution `Delta_i_exc`.

The chart labels `A<B`, `A>B`, and `A=B` are construction coordinates from MB101. They are not promoted to orbit invariants by themselves. An automorphism may change the chosen local chart. What is transported is the geometric exceptional curve, the actual landing points on it, branch multiplicities, and local singularity/intersection data.

## Exact Aut(S) transport

For `phi in Aut(S)`, transport `D` to `phi(D)`. The fixed automorphism action permutes the 48 singular points and therefore the corresponding exceptional curves. If `sigma_phi` is the induced node permutation, then

```text
Q_{sigma_phi(i)}(phi(D)) = phi_* Q_i(D)
```

where `phi_*` maps resolved landing points and normalization branches by the induced local isomorphism.

Because local intersection multiplicity and delta invariant are preserved by isomorphism, the following data are preserved exactly under transport:

```text
r_i,
M_i = sum_j m_ij,
multiset_j(m_ij),
resolved-landing partition shape,
intrinsic branch delta data,
pairwise intersection multiplicity data,
Delta_i_exc,
multibranch status r_i>=2.
```

The node labels may change, but the transported packet does not lose any MB101/MB102 information required by the mission.

## Quotient semantics

Let `P_MB` be the set of complete 48-node MB profiles. Define

```text
P_MB / Aut(S)
```

using the exact geometric transport above. Two profiles are equivalent only when some element of the fixed order-1536 action carries one complete profile to the other.

For production canonicalization, a complete orbit key may be formed by applying every element of the fixed action to a fixed serialization of the 48 transported node packets and taking the lexicographically least serialization. This is a **complete quotient key** once the fixed node permutation table is materialized from the source-locked action.

Scalar summaries such as the following are only necessary orbit invariants and must not be treated as complete orbit identifiers:

```text
N       = #{i:r_i>0},
N_MB    = #{i:r_i>=2},
R       = sum_i r_i,
M       = sum_i M_i,
Delta_exc = sum_i Delta_i_exc,
histogram of node-packet scalar signatures,
multiset of r_i,
multiset of M_i.
```

The global data `d=H.D`, `D^2`, normalization genus `g`, and `Delta_total` are also Aut(S)-invariant because automorphisms preserve the canonical class and intersection form.

## What MB103 does and does not release

MB103 therefore closes the **semantic symmetry gap**: there is now an exact quotient object that preserves every load-bearing MB101/MB102 field and is tied to the published order-1536 action rather than to ad hoc node relabeling.

It does **not** claim:

- that scalar histograms are complete orbit invariants;
- that the 1536-element node-permutation table has already been materialized in this repository;
- that symmetry alone gives a finite degree/intersection window;
- that a finite Picard search is released;
- that `R29-LG2-MB` is discharged.

The next mathematical obligation is MB104: obtain a population-wide finite degree/intersection restriction using MB101 plus the MB102 genus/delta identity. MB103 can then be consumed by MB105 to symmetry-reduce whatever finite carrier backend MB104 legitimately releases.
