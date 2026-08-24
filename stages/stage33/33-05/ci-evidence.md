# Stage33-05 CI evidence

The old `L_{c,E}=9` pilot remains superseded.  The authoritative chain now includes the exact five-function lift, extension mixing, and two direct `x-alpha` rows.

Latest authoritative CI:

```text
HEAD_SHA=660e3ba1246d49c807f99e11fb136ab696293a9f
WORKFLOW_RUN=32704125630
CONCLUSION=success
ARTIFACT_ID=9511597079
ARTIFACT_ZIP_SHA256=1ad3869ba3e2a851815bee3761a453a928cf4988d9d204ce30c78eba5b23b898
ARTIFACT_NAME=stage33-05-k3-branch-preflight
```

The successful workflow reruns the complete Stage33-05 exact chain and certifies

```text
branch components                    = 2 smooth (2,2) genus-one curves over Q(i)
intersection nodes                   = 8, all transverse
Jac(B)[2] dim                        = 4
dual graph b1                        = 7
special even-e fiber count           = 8
L_E=L_{c,E} dim                      = 5
im(x-alpha) dim                      = 3
Br(K_cbar)[2] dim                    = 2
full explicit L_{c,E} basis          = materialized
CV divisor conditions for basis      = complete
extension mixing for basis           = complete
explicit x-alpha rows                = 2
explicit x-alpha row rank            = 2
remaining x-alpha relation dimension = 1
remaining graph-line candidates      = 7
geometric Br[2] quotient action       = identity
geometric G_Q-invariant dimension     = 2
```

The two certified rows in basis order `[J1,J2,q1,q2,q3]` are

```text
s=1 -> [1,0,0,0,0]
s=t -> [1,1,0,0,0].
```

The last relation can therefore be row-normalized to `[0,0,a,b,c]` with nonzero `(a,b,c)`.  Because the exact field action modifies `q_i` only by the already-killed Jacobian plane, the induced action on the final two-dimensional geometric Brauer quotient is identity regardless of which one of the seven graph lines is selected.

Still open:

```text
FULL_XALPHA_MATRIX_MATERIALIZED=false
FINAL_GRAPH_LINE_SELECTED=false
EXPLICIT_TWO_SYMBOL_BRAUER_BASIS=false
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
UNIT_STATUS=RUNNING
```
