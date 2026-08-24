# Stage33-05 CI evidence

Latest exact production checkpoint:

```text
workflow_run = 32685844234
conclusion   = success
artifact_id  = 9505615578
artifact_zip_sha256 = 2a912e061bda1d6b0d86fd4050a668e99f963d8b3fb1501d695c1344a02fc754
```

Certificates:

```text
branch-galois-certificate.json
  sha256 = b8ecf7fcc710f736f23748f0f414e10a748d8006435e4b080294c820429a24e2

cv-dimension-certificate.json
  canonical sha256 = 0683014445edb29a9b5790ed77e3e7fe19055557b30dbb97cc96856910ab0484
```

Exact checked structural output:

```text
branch components = 2 smooth (2,2) genus-one curves over Q(i)
intersection nodes = 8, all transverse
dual graph b1      = 7
Jac(B)[2] dim      = 4
L_E dim            = 9
L_{c,E} dim        = 9
im(x-alpha) dim    = 7
Br quotient dim    = 2
```

This checkpoint does not materialize the explicit 9-element `L_{c,E}` function basis, the rank-7 relation matrix, quotient symbol representatives, or the Q(i)/Q action on the quotient. Therefore Stage33-05 remains RUNNING and no downstream release occurs.
