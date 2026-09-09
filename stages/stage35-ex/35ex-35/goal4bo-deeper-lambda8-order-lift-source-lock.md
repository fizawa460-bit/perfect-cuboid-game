# Stage35-EX Goal4BO source lock — deeper lambda^8 order lift and unbounded ramified ray tower

Scope: continue Goal4BN after exact-head verification. Audited authority remains V74 / Goal4AK. Goal4BO asks whether moving one conductor level deeper repairs the Goal4BM/BN order-two blind class represented by the selected primary prime

```text
pi=5+4*i.
```

The answer is **yes for detection, no for obstruction**. At conductor `lambda^8`, the class of `pi` has order four and a ray character can distinguish valuation `+1` from `-1`. But this does not create a source constraint on the BJ carrier `Xi`: no retained face/space identity supplies an independent fixed value for the deeper character. Moreover the order of `pi` keeps growing without bound as the ramified conductor increases. Therefore blindly continuing to `lambda^9,lambda^10,...` is an unbounded character tower, not a closing argument.

## 1. Exact principal-unit form of the blind prime

Put

```text
lambda=1+i.
```

Then

```text
lambda^4=-4,
lambda^5=-4-4*i,
pi=5+4*i=1-lambda^5.                                 (BO-pi)
```

Hence

```text
v_lambda(pi-1)=5.                                    (BO-v0)
```

For

```text
x_k=pi^(2^k)-1,
```

one has

```text
x_{k+1}=x_k*(2+x_k).                                 (BO-rec)
```

Since `v_lambda(2)=2` and `v_lambda(x_k)>=5`, the ultrametric inequality gives exactly

```text
v_lambda(2+x_k)=2.
```

Therefore induction yields

```text
v_lambda(pi^(2^k)-1)=5+2*k.                          (BO-valuation)
```

This is an exact identity for every `k>=0`.

## 2. Exact order at every deeper conductor

Because `pi` lies in the principal unit group `1+lambda^5`, its order modulo `lambda^n` is a power of two. By `(BO-valuation)`, for `n>=6`,

```text
ord_{lambda^n}(pi)=2^ceil((n-5)/2).                  (BO-order)
```

Thus

```text
mod lambda^7 : order 2,
mod lambda^8 : order 4,
mod lambda^9 : order 4,
mod lambda^10: order 8,
mod lambda^11: order 8,
...                                                   (BO-order-table)
```

The Goal4BM blindness at `lambda^7` is therefore not permanent: a deeper ray character can see the orientation. But the required character order grows indefinitely with conductor.

## 3. The complete primary lambda^8 ray group

Since

```text
lambda^8=(1+i)^8=16,
```

primary ray classes modulo `lambda^8` are represented by the `32` pairs

```text
(A,B) mod 16,
A odd,
B even,
A+B == 1 mod 4.                                     (BO-G8)
```

Under Gaussian multiplication modulo `16`, this group is

```text
G_8 ~= C8 x C4.                                      (BO-structure)
```

One explicit generating pair is

```text
g=3+2*i,  ord(g)=8,
h=1+4*i,  ord(h)=4.                                  (BO-generators)
```

Every primary class occurs uniquely as

```text
g^u*h^v,
0<=u<8,
0<=v<4.
```

The formerly blind prime has coordinates

```text
pi=5+4*i = g^2*h^2,
pi^(-1)=13+12*i = g^6*h^2.                           (BO-pi-coords)
```

Thus its class has order four modulo `lambda^8`.

## 4. A lambda^8 character detects the two orientations

Let `zeta_8` be a primitive eighth root of unity. Define the ray character

```text
chi_8(g)=zeta_8,
chi_8(h)=1.                                          (BO-chi8)
```

Then

```text
chi_8(pi)=zeta_8^2=i,
chi_8(pi^(-1))=zeta_8^6=-i.                          (BO-detect)
```

So a selected BJ valuation `+1` and `-1` at `pi=5+4*i` are distinguished at conductor `lambda^8`.

This proves that Goal4BM's order-two blindness was a **finite-conductor** phenomenon, not a statement that all deeper ray characters are blind.

## 5. Why detection is still not an obstruction

Goal4BN produced a full `41`-adic face-plus-space model with the same selected prime `pi=5+4*i` and both secondary signs

```text
sigma_a=-1,
sigma_a=+1.                                          (BO-BN-flex)
```

The common `W` equations therefore do not fix which local exponent of `pi` appears in the BJ carrier.

The deeper character `chi_8` simply evaluates that exponent:

```text
v_pi(Xi)=+1 -> chi_8 contribution i,
v_pi(Xi)=-1 -> chi_8 contribution -i.                (BO-eval)
```

No retained identity from Goal4BG through Goal4BN supplies a second, source-independent value for `chi_8(Xi)`. In particular, the common-`W` norm relations of Goal4BN constrain rational norms and explicit norm-one quotients, not this deeper principal-unit ray coordinate.

Hence

```text
lambda8 detects orientation = yes;
source fixes lambda8 character value = no;
new reciprocity equation = no;
branch pruning = no.                                 (BO-no-obstruction)
```

This is the same carrier-versus-functional distinction already encountered at Goal4BJ, now at a strictly deeper ramified conductor.

## 6. Why the deeper-character route must not be iterated mechanically

Equation `(BO-order)` gives an unbounded tower:

```text
ord_{lambda^(5+2r)}(pi)=2^r,
ord_{lambda^(6+2r)}(pi)=2^(r+1)                     (r>=0),
```

with the obvious overlap at the first levels. Equivalently, every two additional powers of `lambda` expose one more binary layer of the principal-unit class of `pi`.

Therefore, after `lambda^8`, simply asking for `lambda^9`, then `lambda^10`, and so on cannot close the route unless an **independent source theorem** bounds or fixes the deeper ray class of `Xi`. The retained source currently provides no such theorem.

Goal4BO therefore fail-closes the strategy

```text
"increase ramified conductor until a character detects sigma"
```

as a standalone obstruction route. Detection exists; source control does not.

This does **not** prove that no deeper global theorem exists. It proves that deeper ray-character evaluation alone is not progress toward a contradiction without a new source-derived fixed-value relation.

## 7. Verdict

Certified provisionally:

```text
PI_5_PLUS_4I_EQUALS_1_MINUS_LAMBDA5=true;
V_LAMBDA_PI_2K_MINUS_1_EQUALS_5_PLUS_2K=true;
PI_RAY_ORDER_FORMULA=true;
PRIMARY_LAMBDA8_RAY_GROUP_ORDER=32;
PRIMARY_LAMBDA8_RAY_GROUP_STRUCTURE=C8xC4;
PI_LAMBDA8_ORDER=4;
EXPLICIT_LAMBDA8_CHARACTER_DETECTS_ORIENTATION=true;
SOURCE_FIXED_LAMBDA8_CHARACTER_VALUE=false;
DEEPER_RAY_ORDER_UNBOUNDED=true;
MECHANICAL_DEEPER_CONDUCTOR_ROUTE_FAIL_CLOSED=true;
GLOBAL_RECIPROCITY_CONTRADICTION=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
nonexistence of a future source theorem controlling the ray class;
universal sigma product;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next exact leaf:

```text
35EX-35_GOAL4BP_POST_GAUSSIAN_RAY_TOWER_FRESH_ROUTE_AUDIT
```

Question: stop increasing the ramified conductor. Re-audit the post-Goal4AS candidate ledger using the exact new information from Goal4AT–Goal4BO, and select only a route that introduces a genuinely new source-fixed invariant rather than another evaluation of the already-flexible Gaussian orientation carrier.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
