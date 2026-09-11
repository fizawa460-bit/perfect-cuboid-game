# MB104 post-V8 handoff

Parent main checkpoint remains `STAGE32_MB104_FINITE_WINDOW_COEFFICIENT_BARRIER_V8`.

This continuation adds two retained adapters without promoting the parent certificate:

1. `BTVA-LOW-SUPPORT-FINITENESS.*`
   - Section 7 of Bruin--Thomas--Varilly-Alvarado applies Proposition 3.1 with `r=35` and obtains `h0=(1/108)m^3+O(m^2)`.
   - Therefore genus-0/1 curves meeting at most 13 box nodes form a finite set.
   - An abstract maximum degree `D_13` exists, but no numerical `D_13` or explicit list is retained.
   - Consequently any pairwise-distinct unbounded-degree low-genus sequence must eventually satisfy `N>=14`.

2. `BEAUVILLE-BLOWUP-BRIDGE.*`
   - ramification bookkeeping is on `Xhat->S`, with `(K^2,c2)=(-16,64)`;
   - the 48 ramification curves are `(-1)` and blowing them down gives minimal Beauville `X` with `(32,16)`;
   - favorable-Chern Miyaoka is applied on minimal `X`, not on `Xhat`.

Executable overlay: `verify_mb104_post_v8_globalization_overlay.py`.

Next research leaf:

`MB104_N_GE_14_GLOBALIZATION_OR_EFFECTIVE_LOW_SUPPORT_BOUND`.

Priority routes:
- make the finite `N<=13` theorem effective enough to certify a numerical cutoff; or
- on `N>=14`, exploit global symmetric differentials/foliations to bound tangent/landing directions, or obtain a global jet/member obstruction.

No finite Picard release, receiver/theorem/endpoint credit, or merge authorization.
