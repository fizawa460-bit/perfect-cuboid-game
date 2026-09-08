# Goal4AJ literal degree-31 denominator source lock

Status: provisional exact diagnostic source lock only. This note does not promote MAIN authority and grants no numerator, F_B, local-evaluation, Brauer-Manin, E1, Stage35, theorem, receiver, endpoint, or perfect-cuboid credit.

## Exact successful run

- PR: `#1698`
- branch: `stage35-ex-goal4aj-degree19-truncated-kernel`
- run: `34182361333`
- diagnose job: `101923866397`
- run head: `efae49350e514ea562208434e1e01e5d8f7074ff`
- gen16 schema: `STAGE35_EX_GOAL4AJ_DEGREE31_DENOMINATOR_MATERIALIZE_GEN16_DIAGNOSTIC_V1`
- canonical SHA256: `09683e1623b6c57ba1f96864fbcc47e51a878f032273a1da74327fa1b6b9122f`

## Exact polynomial commitments

The degree-19 primitive residual is the gen15-g2 exact Q-section with integer-lift SHA256

`4acafb5681e92aae5f63efa101de72e0795d30cf4d81d936e7ef02c73dc0c7ea`.

The source-locked Q-hyperplane peel selects denominator singleton orbit `0` once and singleton orbit `3` eleven times. Exact reconstruction gives

- `L0 = c`, primitive coefficient vector `[0,0,0,0,0,0,1]`;
- `L3 = b1`, primitive coefficient vector `[0,0,0,1,0,0,0]`.

Hence the literal degree-31 denominator is

`q31_den = q19 * c * b1^11`.

The expanded primitive integer representative has:

- homogeneous degree: `31`;
- term count: `1542`;
- coefficient gcd: `1`;
- maximum absolute coefficient: `11188`;
- literal text bytes: `42489`;
- literal polynomial SHA256: `28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29`;
- coefficient-stream SHA256: `76bde7ae4a5ab6879dcc33a0e6a78a5eed59cf8e077f886d3685ceb329089918`.

The complete literal polynomial was persisted in the successful Actions job log. No artifact upload was used.

## Source locks

- Q-hyperplane peel script blob: `e5b41410e570d5e442afe985dd5b7f3355d5d653`
- Q-hyperplane peel canonical: `c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba`
- Q-hyperplane peel run/job: `34092066114 / 101647794285`
- gen11 script blob: `1722fdf949915443985ce1c512b4d5474b18cd1e`
- gen11 canonical: `8c457f6c9a89f89548c382e1d371298e8ca45022e526a4a09f2618e364b2ab1f`
- gen15-g2 canonical: `2a6b8b80ed8bca3b1801ac0a5a7f0300ee9ea33a6019fc4866605dd74fcb3a97`
- gen15-g2 run/job: `34180606310 / 101918803163`
- exact exceptional bridge blob: `c125b09be3fcf572e5264f0c0b1db41ae9b74cf2`

## Credit firewall

This establishes a literal Q-coefficient degree-31 **denominator** representative for Goal4AJ. The Goal4AJ completion condition still requires a literal degree-31 numerator representative. `F_B`, local evaluation, Brauer-Manin obstruction, E1, Stage35 closure, theorem, receiver, endpoint, and perfect-cuboid credit remain false.
