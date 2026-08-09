# Stage13-13fw — Claude R07 review adjudication

Review target:

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260810-R07
CONTENT_SHA256=52b660f6ff234da4b73d241cec981744d6d3d9cdcd406ab5fe2c1f746b784578
```

Reviewer: `Claude`

## Verdict

```text
CLAUDE_R07_VERDICT=OPEN
CLAUDE_R07_LABEL=REPAIRABLE
CLAUDE_R07_CLOSED_VOTE_COUNTED=false
```

Claude's review is accepted as a fresh R07 review. It does not identify a contradiction in the Stage13 theorem or constants, but it identifies two review-target defects that prevent treating this immutable R07 bundle as fully self-contained.

## Accepted finding 1 — `QR_0(F_p)` is undefined

The R07 canonical proof uses

```text
W_p(x,z)=1_{x^2+z^2 in QR_0(F_p)}
```

and later counts the zero states separately in deriving

```text
|Omega^W_{p,U}|=(p+1)^2/2.
```

The intended meaning is recoverable from the calculation and from the global implication `x^2+z^2=w^2`, but the symbol itself is never explicitly defined in the immutable review target. The intended definition is

\[
QR_0(\mathbf F_p):=\{t^2:t\in\mathbf F_p\},
\]

so `0` is included.

If a reviewer instead reads `QR_0` as the nonzero quadratic residues, the local count changes. Therefore this is not merely typographical decoration: it is a semantic self-containedness defect in the predicate that defines Gate B.

Classification:

```text
QR0_UNDEFINED=ACCEPTED
QR0_DEFECT_CLASS=SELF_CONTAINED_SEMANTIC_BLOCKER
QR0_CHANGES_INTENDED_THEOREM=false
```

## Accepted finding 2 — full Jacobi-sum reduction is not embedded

R07 does reproduce the principal chain

```text
S=S0+S1+S2+S3=0+(p-1)+(p+1)-2=2(p-1)
|Omega^W_{p,U}|=((p^2-1)+2(p-1)+4)/2=(p+1)^2/2
```

so the final local formula is not absent from the bundle. However, the bundle does not expand the internal proof of the four `S_i` evaluations, especially the `S3=-2` reduction using the quadratic-character identity, `J(chi,chi)=1`, and the `A+B-C-D` decomposition that is explicit in Stage13-12ag.

Because the artifact calls itself `SELF-CONTAINED`, a reviewer should not have to leave the bundle to audit this local identity. This is therefore accepted as a bundle-level explicitness blocker, not a new theorem-level contradiction.

Classification:

```text
JACOBI_SUM_FINAL_FORM_PRESENT=true
JACOBI_SUM_FULL_REDUCTION_EMBEDDED=false
JACOBI_SUM_SELF_CONTAINED_BLOCKER=ACCEPTED
JACOBI_SUM_THEOREM_CONTRADICTION=false
```

## Findings not promoted to blockers

Claude found the R07 Gate B structural repair effective: the global second-face square reduces directly to the actual local test; positive valuation strata pass for an explicit inertness/primitivity reason; and the `p=3` hand check agrees with `alpha_3=1` and `lambda_3=1` under the intended `QR_0` definition.

Gate C's separation of the angular Vaaler approximation from the physical cutoff is accepted as logically sound. Gate A's fixed-S Phragmen--Lindelof existence argument is also not challenged as a theorem defect merely because no numerical values of `C_S` or `delta_S` are supplied.

## Adjudication

R07 remains immutable. These defects are not repaired in place.

```text
R07_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
R07_UNRESOLVED_SELF_CONTAINED_BLOCKERS=2
R08_REQUIRED=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
```
