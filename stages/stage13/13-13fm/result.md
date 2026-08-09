# Stage13-13fm result

`13-13fm` closes R06 Gate C, the final theorem-level objection carried from the R05 external reviews.

The repaired proof-facing lemma is

```text
stages/stage13/13-13fm/principal-pole-sector-closure.md
```

It replaces the R05 §14 shorthand by the following explicit structure:

- the pole-producing factor slots are `H,R1,R2,S1,S2`, coming from `zeta(s_h)`, `zeta(s_r)^2`, `zeta(s_s)^2`;
- admissible local residues are treated as a constrained finite set inside an ambient finite abelian unit group, not falsely assumed to be a group themselves;
- ambient auxiliary characters that act identically on the constrained set are identified before pole classification;
- the principal sector is the kernel of the reduced five-slot pole-signature map;
- the whole kernel contribution is identified with a linear principal-residue functional and therefore reproduces the exact local ratio `product lambda_p`;
- the unconstrained tagged population has the exact finite cardinality `2*A_q(B)`, and every true pair overlap injects through its unique shared edge, proving the factor two cannot undercount;
- outside the kernel at least one explicit pole slot is genuinely nonprincipal after aliasing, while the mixed Wiener correction is holomorphic and cannot restore that pole.

Thus for every fixed finite inert set `S`,

```text
A_tag_q,S(B)
 = 2*D_q*product_{p in S}(lambda_p)*B(log B)^3
   + o_S(B(log B)^3)
```

and the fixed-`S`-then-`B`-then-enlarge-`S` squeeze again gives

```text
O_qr(B)=o(B(log B)^3)
T(B)=o(B(log B)^3).
```

No growing-modulus estimate is introduced.

```text
STAGE13_13FM=COMPLETE_FIXED_S_PRINCIPAL_POLE_SECTOR_CLOSURE
R06_GATE_C=COMPLETE
POLE_CHANNELS=H,R1,R2,S1,S2
ACTUAL_CONSTRAINED_RESIDUE_SET_USED=true
AUXILIARY_CHARACTER_ALIASING_QUOTIENTED_BEFORE_POLE_CLASSIFICATION=true
PRINCIPAL_POLE_SECTOR=KER_REDUCED_POLE_SIGNATURE_MAP
PRINCIPAL_SECTOR_RESIDUE_FUNCTIONAL_PROOF_COMPLETE=true
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
TAGGED_AMBIENT_CARDINALITY=2*A_q(B)
TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true
NONPRINCIPAL_POLE_LOSS_PROVED=true
MIXED_CORRECTION_CANNOT_RESTORE_POLE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
R06_MANDATORY_THEOREM_LEVEL_GATES_A_B_C_COMPLETE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fn
```

`13-13fn` is the R06 proof-facing explicitness/synthesis hardening gate before a new immutable R06 bundle is built.