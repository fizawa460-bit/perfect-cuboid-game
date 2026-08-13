# Stage14-4ci

Stage14-4ci intersects merged 4ch with merged s7-22 on the same balanced physical pair.

Main exact upgrades:

```text
JointCommonCoreCRTPhysicalFiberLemma = proved (by 4ch, which fixes less data),
primitive z direction itself lies in Lambda_k,
k-side dual saturation order = k^2,
k-side dual defect = 1,
gcd(z1,z2)^2 | q_k = C*u_res,
gcd(omega1,omega2)^2 | q_xi = C*v_res.
```

After removing the two common scales, the four positive host equations become an exact normalized coupled diagonal-form system.  The remaining cell multiplicity is therefore refined by the full-order k dual datum and the s7-22 xi rank/dual-resonance split.

No whole-family power saving is claimed here.  The current bound remains `B^(7/8+o(1))`.

```text
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cj
```
