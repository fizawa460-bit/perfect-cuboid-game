# Stage33-05 CI evidence

The earlier dimension pilot that reported `L_{c,E}=9` is superseded because it omitted the four nodal ruling fibers from the Creutz--Viray even-`e(b/w)` set.

Corrected checker branch head is tracked by the latest PR #1358 commit. The authoritative run must include `cv_dimension_check.py` schema

```text
STAGE33_05_CV_DIMENSION_SKELETON_V2_NODE_FIBERS_INCLUDED
```

and must certify

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

This checkpoint still does not materialize the explicit five-element `L_{c,E}` function basis, rank-three relation matrix, quotient symbol representatives, or the Q(i)/Q action on the quotient. Stage33-05 remains RUNNING.
