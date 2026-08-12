# Stage15-6bk — joint norm-core / coordinate-core endpoint audit

Base: Stage15-6bj. Audit verdict: `BLOCK` for a fresh endpoint-spacing route.

Use the exact four-cell notation of Stage15-6al:

\[
x=\kappa_{xp}\kappa_{xq}X^2,\quad
y=\kappa_{yp}\kappa_{yq}Y^2,
\]
\[
p=\kappa_{xp}\kappa_{yp}P^2,\quad
q=\kappa_{xq}\kappa_{yq}Q^2.
\]

Set

\[
\kappa_{sw}=\kappa_{xq}\kappa_{yp},\qquad
\kappa_{ag}=\kappa_{xp}\kappa_{yq},
\]

and

\[
A=\kappa_{xp}XP,\ B=\kappa_{yq}YQ,\ C=\kappa_{xq}XQ,\ D=\kappa_{yp}YP.
\]

Then exactly

\[
xp=\kappa_{sw}A^2,\quad yq=\kappa_{sw}B^2,
\]
\[
xq=\kappa_{ag}C^2,\quad yp=\kappa_{ag}D^2.
\]

Hence the four endpoints are

\[
E_1=\kappa_{sw}(A^2-B^2),\quad
E_3=\kappa_{sw}(A^2+B^2),
\]
\[
E_2=\kappa_{ag}(C^2+D^2),\quad
E_4=\kappa_{ag}(D^2-C^2).
\]

Stage15-6bi also says the odd O-core divides both `E1,E2`, while the odd S-core divides both `E3,E4`. Since Stage15-6al proved `(k,kappa)=1`, these divisibilities descend to

\[
k_O\mid A^2-B^2,\qquad k_O\mid C^2+D^2,
\]
\[
k_S\mid A^2+B^2,\qquad k_S\mid D^2-C^2.
\]

At first sight these look like new joint-core root lines. They are not. Stage15-6al gives

\[
\frac mn=\frac AB,\qquad \frac rs=\frac CD
\]

before reduction. Therefore the four congruences above are precisely the Stage15-6aa two-channel determinant lock transported through the four-cell coordinates:

```text
O: m^2-n^2=0, r^2+s^2=0 mod k_O
S: m^2+n^2=0, r^2-s^2=0 mod k_S.
```

So the endpoint route has looped back to the original global-core charging obstruction. Charging these congruences again after the Gaussian-square and coordinate-core reductions would violate the AR-028 accounting firewall unless a genuinely new whole-family measure theorem is supplied.

This is a stable obstruction, not a contradiction: the long causal audit has shown that the elliptic, diagonal-support, equal-hypotenuse and endpoint formulations all return to the same two-channel global charging problem.

```text
STAGE15_6_SUBSTAGE=6bk
STAGE15_6BK_AUDIT_VERDICT=BLOCK
STAGE15_6BK_ENDPOINT_CELL_FACTORIZATION_EXACT=true
STAGE15_6BK_JOINT_CORE_CONGRUENCES=true
STAGE15_6BK_JOINT_CORE_CONGRUENCES_NEW=false
STAGE15_6BK_REDUCES_EXACTLY_TO_6AA_TWO_CHANNEL_LOCK=true
STAGE15_6BK_AR028_RECHARGE_FORBIDDEN=true
STAGE15_6BK_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6BK_EXIT=STABLE_GLOBAL_TWO_CHANNEL_CHARGE_OBSTRUCTION_RECONFIRMED
```
