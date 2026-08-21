# Stage28-60-r2 — normalized interaction-curvature threshold

```text
TASK_ID=Stage28-60-r2-R15-R16
CHECKPOINT=60
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_CHECKPOINT60_PR=1280
PARENT_CHECKPOINT60_AUDIT=PASS
PARENT_CHECKPOINT60_MERGED=true
```

Checkpoint60 already proved two positive-divergent matched interaction invariants.  Write

\[
\mathcal I_{sp}(B)
=\frac{N_2/M_2}{N_1/M_1}
=\frac{N_2M_1}{M_2N_1}
\]

for the space interaction from `S25-W02`, and

\[
\mathcal I_{face}(B)
=\frac{M_3/M_2}{M_2/M_1}
=\frac{M_3M_1}{M_2^2}
\]

for the audited Stage28-60 third-face interaction.

Both are matched population-ratio invariants.  Neither is a stochastic probability and they must not be multiplied as independent factors.

## Exact quotient identity

Their quotient simplifies exactly:

\[
\boxed{
\frac{\mathcal I_{face}}{\mathcal I_{sp}}
=\frac{M_3N_1}{M_2N_2}
=\frac{M_3}{N_2}\frac{N_1}{M_2}.
}
\]

Equivalently,

\[
\boxed{
\frac{M_3}{N_2}
=\frac{M_2}{N_1}\frac{\mathcal I_{face}}{\mathcal I_{sp}}.
}
\]

This is pure algebra on the already frozen population counts; it does not introduce a new host, multiplicity or endpoint count.

## Exact asymptotic normalizer

Stage21 gives

\[
\frac{N_1(B)}{M_1(B)}
\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B},
\]

while Stage22 uses

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Therefore

\[
\boxed{
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Together with

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

we obtain

\[
\boxed{
\frac{M_2(B)}{N_1(B)}
\sim \frac{24\pi C_{M_2}}{\kappa}(\log B)^2.
}
\]

Define the normalized interaction curvature

\[
\boxed{
\mathcal K_{28}(B)
:=(\log B)^2\frac{\mathcal I_{face}(B)}{\mathcal I_{sp}(B)}.
}
\]

Then the direct Stage28 bridge satisfies the asymptotic identity

\[
\boxed{
\frac{M_3(B)}{N_2(B)}
\sim
\frac{24\pi C_{M_2}}{\kappa}\,\mathcal K_{28}(B).
}
\]

Thus the unresolved Stage19/Stage20 ordering problem is equivalent, up to one known positive constant, to the asymptotic behavior of `K_28`.

## Sharp threshold formulation

Let

\[
\mathcal J_{28}(B):=rac{\mathcal I_{face}(B)}{\mathcal I_{sp}(B)}.
\]

Since `K_28=(log B)^2 J_28`, the critical scale for the raw interaction quotient is exactly

\[
\boxed{\mathcal J_{28}(B)\asymp (\log B)^{-2}.}
\]

More precisely:

- if `J_28=o((log B)^(-2))`, then `M3/N2 -> 0`;
- if `J_28 ~ lambda (log B)^(-2)` with `0<lambda<infinity`, then
  \[
  M_3/N_2\to (24\pi C_{M_2}/\kappa)\lambda;
  \]
- if `J_28/(log B)^(-2) -> infinity`, then `M3/N2 -> infinity`.

Analogous liminf/limsup statements follow without assuming a limit.

This is a comparison theorem, not a solution of the ordering problem.  It turns the vague statement “compare the two positive interactions” into one precise threshold receiver.

```text
EXACT_INTERACTION_QUOTIENT_IDENTITY=true
N1_ASYMPTOTIC_DERIVED=true
M2_OVER_N1_ASYMPTOTIC=(24*pi*C_M2/kappa)*(logB)^2
NORMALIZED_INTERACTION_CURVATURE=K_28=(logB)^2*I_face/I_sp
BRIDGE_CURVATURE_EQUIVALENCE=M3/N2~(24*pi*C_M2/kappa)*K_28
RAW_INTERACTION_THRESHOLD=(logB)^(-2)
SOURCE_TARGET_ORDERING_RESOLVED=false
PERFECT_CUBOID_ENDPOINT_USED=false
AUDIT_REQUIRED=true
```