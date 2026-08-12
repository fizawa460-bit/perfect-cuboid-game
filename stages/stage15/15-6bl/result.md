# Stage15-6bl — joint two-channel congruence lattice

Base: merged PR #852. This stage returns directly to the Stage15-6aa S/O channel core.

Let `q=k_S*k_O` be the odd actual norm core, with `(k_S,k_O)=1`. For every prime of `q`, Stage15-6aa proved all four toric parameters are units and exactly one S/O orientation holds. After CRT there are roots `lambda,mu mod q` with

\[
m\equiv\lambda n\pmod q,\qquad r\equiv\mu s\pmod q,
\]

where primewise `lambda^2=-1, mu^2=+1` on `k_S` and `lambda^2=+1, mu^2=-1` on `k_O`.

Each congruence is one primitive rank-one residue line in one toric parameter pair. Their product is therefore one joint four-variable congruence lattice of index exactly `q^2`. The orientation multiplicity is `2^{O(omega(q))}=B^o(1)`.

This is not an AR-028 double charge: we do not count the outer and inner restrictions as two independent arithmetic savings. The single common-core condition defines one product congruence locus whose local density is `q^{-2}`.

The point-generated nature of `q` remains important. This stage proves the fixed-actual-core local geometry only; it does not replace `q` by an arbitrary divisor and does not sum over `q`.

```text
STAGE15_6_SUBSTAGE=6bl
STAGE15_6BL_AUDIT_VERDICT=PASS
STAGE15_6BL_JOINT_ROOTLINE_MODULUS=q=k_S*k_O
STAGE15_6BL_OUTER_ROOTLINE=true
STAGE15_6BL_INNER_ROOTLINE=true
STAGE15_6BL_JOINT_CONGRUENCE_INDEX=q^2
STAGE15_6BL_ORIENTATION_MULTIPLICITY=Bo1
STAGE15_6BL_AR028_DOUBLE_CHARGE=false
STAGE15_6BL_GLOBAL_MOVING_q_SUM_PROVED=false
STAGE15_6BL_EXIT=TORIC_CONGRUENCE_NEIGHBOURHOOD_ADAPTER_READY
```