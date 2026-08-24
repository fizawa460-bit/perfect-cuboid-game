# Stage33-05 CI evidence

The earlier dimension pilot that reported `L_{c,E}=9` is superseded because it omitted the four nodal ruling fibers from the Creutz--Viray even-`e(b/w)` set.

Corrected authoritative CI:

```text
HEAD_SHA=0683e5e1300025550620df1eb42664fe06b8ad68
WORKFLOW_RUN=32686188288
CONCLUSION=success
ARTIFACT_ID=9505728365
ARTIFACT_ZIP_SHA256=16a3c9d9537d0a0cae76fd6bb81db20e60cc45d65b0229ea8187000ae6fdb9e0
BRANCH_CERTIFICATE_SHA256=b8ecf7fcc710f736f23748f0f414e10a748d8006435e4b080294c820429a24e2
CV_DIMENSION_CANONICAL_SHA256=2f56fb20b25af27f68639e0154713ba1b4995113715f516a014c0a605b2fc976
CV_DIMENSION_SCHEMA=STAGE33_05_CV_DIMENSION_SKELETON_V2_NODE_FIBERS_INCLUDED
```

The corrected checker certifies

```text
branch components = 2 smooth (2,2) genus-one curves over Q(i)
intersection nodes = 8, all transverse
dual graph b1      = 7
Jac(B)[2] dim      = 4
smooth ramification fibers with even e = 4
nodal fibers with e(b/w)=1+1=2        = 4
special even-e fiber count             = 8
K-squareclass kernel dim                = 1
raw generator subspace dim              = 12
kernel to K*L*2 dim                     = 7
L_E dim                                 = 5
L_{c,E} dim                             = 5
im(x-alpha) dim                         = 3
Br quotient dim                         = 2
```

Do not cite the superseded `9/7` dimension pilot for receiver credit.

This checkpoint still does not materialize the explicit five-element `L_{c,E}` function basis, rank-three relation matrix, quotient symbol representatives, or the Q(i)/Q action on the quotient. Stage33-05 remains RUNNING and no downstream release occurs.
