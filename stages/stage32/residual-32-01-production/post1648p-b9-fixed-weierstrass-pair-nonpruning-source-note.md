# Stage32 post1648P scratch source note — B9 fixed Weierstrass pair

This leaf is scratch-only and carries no MAIN or arithmetic credit.

post1648N source-locks the Bolza automorphism B.9 / KKK `mu1` as `x -> i*x`. On the six branch points `{0, infinity, ±1, ±i}`, its fixed Weierstrass pair is exactly `{0,infinity}`. In the source `J[2]` coordinates retained by post1648D, their difference is `Z3=delta_0inf`.

post1648O materializes the six residual target affine order-8 candidates. For each candidate the equation `t=(I-A)s` has exactly two solutions `s in A[2]`; these are precisely its two fixed 2-torsion points.

The present verifier checks the stronger marked-pair condition omitted by O: both fixed points for every candidate lie in Deraux's explicit six-point order-2 orbit. The six target orbit points split into exactly three fixed pairs, one pair for each retained W-line:

- L1: `{[1,1,0,1],[1,1,1,1]}`;
- L2: `{[0,0,1,0],[0,0,1,1]}`;
- L3: `{[1,0,0,0],[1,0,1,1]}`.

The difference of each pair is exactly the corresponding W-line vector. Two residual target order-8 candidates realize each pair. Therefore even requiring that the source fixed pair `{0,infinity}` map to the target six-point orbit does not select one retained Richelot line.

The remaining datum is not another unmarked orbit condition. It is the actual KRR conjugating automorphism `g`, or an equivalent marked theta/half-period normalization that says which one of the three target fixed pairs is `g({0,infinity})`.
