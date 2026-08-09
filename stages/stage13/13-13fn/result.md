# Stage13-13fn — R06 canonical synthesis result

> STATUS: `COMPLETE_R06_CANONICAL_PROOF_SYNTHESIS`

`13-13fn` integrates the three mandatory R06 theorem-level repair gates and the remaining proof-facing explicitness requests into one canonical proof entrypoint:

```text
stages/stage13/13-13fn/stage13-r06-canonical-proof.md
```

## Mandatory R06 repairs integrated

1. `sum_q I_q=pi^2/8` is proved analytically by positive-octant symmetry and an exact spherical-coordinate integral; numerical quadrature is validation only.
2. The Gaussian-Hecke normalization is matched to Huang--Liu--Rudnick: Stage13 Fourier exponent `m=8 ell` corresponds to HLR Hecke index `k=2 ell`, with completed gamma shift `4 ell`.
3. The fixed-`S` overlap transfer explicitly identifies the five zero-mode pole slots, removes auxiliary-character aliasing on the actual constrained residue set before pole classification, defines the principal sector as the kernel of the reduced pole-signature map, proves the exact `prod lambda_p` principal multiplier, proves the factor-two tagged upper bound, and proves nonprincipal pole loss.

## Explicitness hardening integrated

The R06 proof also exposes:

- the Wiener mixed term `M` before its norm estimate;
- the complete exceptional `p=5` calculation ending at `431.99676036<432`;
- `ell>=1` at `C_{ell,p}` first use;
- `lambda_3=1`, so contraction starts at inert `p>=7`;
- the stronger finite-data nonclaim;
- Gelfand--Leray factor `1/(P/d)`;
- branchwise OE/EE face-independence;
- `O(log(2B)/eta)=O((log B)^9)` per mesh coordinate and `O((log B)^27)` total boxes;
- the decomposition `(4*C_H+4)+D_H+2=4*C_H+D_H+6`;
- Vaaler endpoint convention and equality-wall handling;
- strict `theta` / `vartheta` notation separation;
- Riesz/Perron transition-majorant and mixed-log-shift details;
- elementary `1+O(p^-2)` expansions for absolute convergence of `kappa`.

## Gate decision

```text
STAGE13_13FN=COMPLETE_R06_CANONICAL_PROOF_SYNTHESIS
R06_CANONICAL_PROOF=stages/stage13/13-13fn/stage13-r06-canonical-proof.md
R06_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
R06_MANDATORY_THEOREM_LEVEL_GATES_A_B_C_COMPLETE=true
R06_EXPLICITNESS_GATE_D_INTEGRATED=true
R06_SYNTHESIS_READY=true
R06_BUNDLE_CREATED=false
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R05_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fo
```

`13-13fo` is reserved for building the new immutable R06 self-contained review bundle and manifest from a fixed merged source snapshot. External review counts must restart from zero on R06.
