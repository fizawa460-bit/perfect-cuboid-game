# Stage29-07 — fresh adversarial audit contract

Fresh audit must treat every proposed discharge in 29-07 as attackable.

Required checks:

1. Re-derive the finite map
   `T2bar={e^2+x^2=p^2,e^2+y^2=q^2} -> P2_[e^2:x^2:y^2]`
   and verify global well-definedness, finiteness, generic degree `16`, and generic deck `(Z/2)^4`.
2. Independently compute the singular locus of `T2bar`; verify exactly four points and verify each is `A1`.
3. Check from audited Stage18/20/28 sources that `Y=Bl_4(P1xP1)` is genuinely the resolution/anticanonical model adapter for this same `T2bar`, not merely another birational rational surface.
4. Re-derive the global projection `Sbar -> T2bar` forgetting `z,d`; verify finiteness, generic degree `4`, and that the two residual quadratic characters are exactly third-face and space completion. Attack `R29-KUM3B=DISCHARGED` if any boundary or projective issue invalidates the global statement.
5. Verify the normalization identity
   `normalization(Y x_T2bar Sbar)=normalization of Y in Q(Y)(sqrt(f_face),sqrt(f_sp))`
   and its relation to the audited Stage29 joint V4 model.
6. Recheck the tower degree factorization `4,8,16,32,64`. Confirm simultaneous global sign is accounted for exactly once.
7. Attack the claim that the selected physical predicates form a literal rational-lift tower while `M1,M2,M3` do not form successive tower floors.
8. Re-derive the incidence formulas
   `Ij=sum_{k>=j} C(k,j) Mk` and `Ij^S=sum C(k,j) Nk`, with `N3=P`.
9. In particular recheck the two-face residual V4 cell counts
   `M2-N2`, `N2`, `3(M3-P)`, `3P` and their sum `M2+3M3`.
10. Attack the primitive normalization argument: from a positive rational partial-cover point, verify that clearing denominators and dividing by `gcd(a,b,c)` preserves every already-required integral diagonal.
11. Attack the height claim. Verify the exact cutoff is the primitive Euclidean norm `R`, including on the `S=NO` complement, and ensure no standard Weil-height equivalence is silently claimed.
12. Verify algebraic sign-sheet multiplicity is not counted as physical-object multiplicity.
13. Decide whether `R29-KUM4B` is fully discharged or only partially discharged. If any of common host, lift/nonlift semantics, map direction, sign multiplicity, height, primitivity, canonical ordering, or population multiplicity remains unresolved, do not accept full discharge.
14. Decide whether KUM4B closure removes the conditional Stage16-28 backflow watch. No backflow removal by policy alone.
15. Recheck `R29-G1b`: accept discharge only for the exact scope actually proved. Do not call the entire exceptional-curve ledger complete if it is not enumerated.
16. Recheck `R29-X1`: the submission intentionally leaves full global ADE enumeration open. Confirm downstream reassignment to `J12-JOINT-V4` is coherent and does not hide an infrastructure blocker.
17. Preserve the 29-06 canonical-model/resolution split and do not collapse normal models with smooth resolutions.
18. Verify no new population asymptotic, independence product, perfect-cuboid existence claim, or nonexistence claim is introduced.
19. If audit writes the canonical controller, preserve all unrelated audited Stage29 metadata and synchronize merged PR #1312 only.

Allowed bridge verdicts include partial discharge. Do not repair a failed exact bridge by analogy.
