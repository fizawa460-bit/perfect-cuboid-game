# Goal4AJ degree-19 exceptional coefficients forced from exact strict vanishing

Status: provisional exact bridge only. This note does not promote MAIN authority and grants no F_B, local-evaluation, Brauer-Manin, E1, Stage35, theorem, receiver, endpoint, or perfect-cuboid credit.

## Locked inputs

1. Goal4AJ gen15 generation 2, run `34180606310`, diagnose job `101918803163`, canonical SHA256 `2a6b8b80ed8bca3b1801ac0a5a7f0300ee9ea33a6019fc4866605dd74fcb3a97`, proves that the deterministic centered lift of `8*q_mod` is a nonzero Q-coefficient homogeneous degree-19 section and satisfies all 22 prescribed strict-curve symbolic-power conditions exactly over `Q(i,sqrt(2))`. Its integer-lift SHA256 is `4acafb5681e92aae5f63efa101de72e0795d30cf4d81d936e7ef02c73dc0c7ea`, with 1542 terms and coefficient gcd 1.
2. Goal4AJ gen13, canonical SHA256 `21e9a9087e0ca955afe3ae66b5b7b352bb806cb599b9f483af92844e733def23`, verifies for every retained A1 exceptional curve `E_j` that

   `sum_i m_i (C_i . E_j) = 2 e_j`,

   where `m_i` are the active degree-19 strict multiplicities and `e_j` is the active exceptional target. The retained incidence uses `C_i.E_j in {0,1}`, while the resolution data use `E_j^2=-2`, pairwise-disjoint distinct exceptional curves, and `H.E_j=0`.
3. The Q-hyperplane peel diagnostic has canonical SHA256 `c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba`. Its exact Picard check proves that the post-peel denominator residual vector has class `19H`. The compact active-condition packet canonical SHA256 is `59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6`.

## Exact bridge

Let `pi : Xtilde -> X` be the minimal resolution and let `q` be the exact Q-coefficient degree-19 section supplied by gen15-g2. Its pullback divisor satisfies

`D_q ~ 19H`.

The exact symbolic-power checks give

`ord_{C_i}(D_q) >= m_i`

for every active strict curve. For a fixed A1 exceptional curve `E=E_j`, write

`D_q = sum_i m_i C_i + v_E E + R`,

where the displayed strict contribution is the prescribed one and `R` is effective after separating the coefficient of `E`. Distinct exceptional curves are disjoint, and every component of `R` other than `E` has nonnegative intersection with `E` on the smooth resolution. Intersecting with `E` gives

`0 = D_q.E = 19H.E = sum_i m_i(C_i.E) - 2 v_E + R.E`.

Using the gen13 identity `sum_i m_i(C_i.E)=2e_E`,

`v_E = e_E + (R.E)/2 >= e_E`.

Thus every active exceptional target is forced by the already-exact strict vanishing; no independent higher-order A1 jet computation is required for the lower-bound condition.

Let

`D_target = sum_i m_i C_i + sum_j e_j E_j`

be the exact post-peel denominator residual divisor. The previous paragraph gives `D_q >= D_target`. Both divisors have class `19H`, so

`D_q - D_target`

is effective and linearly equivalent to zero. On a projective integral surface an effective divisor linearly equivalent to zero is zero (the corresponding rational function has no poles, hence is a global regular constant). Therefore

`D_q = D_target`.

## Boundary

This bridge upgrades the gen15-g2 object from an exact Q-valued degree-19 strict candidate to an exact degree-19 denominator-residual section for the locked post-peel divisor packet, subject to later hostile audit. It does not yet multiply back the twelve peeled Q-hyperplane factors and therefore does not yet materialize the required literal degree-31 denominator. Numerator coefficients and `F_B` also remain pending.
