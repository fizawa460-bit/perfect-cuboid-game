# Stage35-EX 35EX-16 — coprime-pair global reciprocity and moving ramification freeze

## Scope

Continue from the exact 35EX-15 boundary. Work on

```text
B35 := primitive Master-Hit source conditions + Lminus=x^2,
```

with

```text
Lminus=(W1*W2-V1*V2)/(p*d),
Lplus =(W1*W2+V1*V2)/(p*d),
gcd(Lminus,Lplus)=1,
Lplus == 1 mod8.
```

35EX-15 proved that any residual nonsquare squareclass of `Lplus` is supported only on moving `1 mod4` split primes. The fresh breadth audit retained a possible global Jacobi/Hilbert coupling as the next route.

This leaf tests the natural global reciprocity relations supplied by the coprime pair and the source gcd channels. They do not close. The source pieces genuinely coprime to the common odd-leg gcd `c` are forced to Jacobi symbol `+1`, while primes shared by `c` with `D=U1/c` or `T=U2/c` remain in the moving `c`-ramified layer together with `p,d` and the residual split kernel.

No E1 theorem or receiver-close credit is claimed.

## 1. Pair reciprocity is tautological on B35

Since

```text
Lminus=x^2,
gcd(Lminus,Lplus)=1,
```

we have immediately

```text
(Lminus / Lplus) = +1.
```

Also the denominator `Lminus=x^2` is an odd square, so

```text
(Lplus / Lminus) = +1.
```

Here the symbols are Jacobi symbols. Moreover 35EX-15 gives

```text
Lminus == Lplus == 1 mod8,
```

so quadratic reciprocity introduces no sign. Therefore the bare coprime pair gives only

```text
PAIR_JACOBI_RELATION=+1_TAUTOLOGY.              (PAIR)
```

There is no forced `-1` available from the pair itself.

## 2. Only the c-coprime parts of D and T are clean

Write

```text
U1=c*D,
U2=c*T,
gcd(D,T)=1.
```

There is no theorem here that `gcd(c,D)=gcd(c,T)=1`. In fact the bounded Master-Hit panel contains both phenomena:

```text
(a,b,m,n)=(11,2,8,5): c=39, D=3,
(a,b,m,n)=(8,5,11,2): c=39, T=3.
```

Therefore define the exact clean parts by deleting every prime whose support meets `c`:

```text
D_clean = largest divisor of D coprime to c,
T_clean = largest divisor of T coprime to c.
```

Equivalently, primewise,

```text
v_ell(D_clean)=v_ell(D) if ell does not divide c, and 0 otherwise,
v_ell(T_clean)=v_ell(T) if ell does not divide c, and 0 otherwise.
```

Put also

```text
D_ram=D/D_clean,
T_ram=T/T_clean.
```

Then every prime of `D_ram*T_ram` divides `c`; those primes are not treated as clean below.

Let `ell` be an odd prime dividing `D_clean`. Then

```text
ell|U1,
ell does not divide c,
ell does not divide T,
```

so `ell` does not divide `U2=c*T`. Primitivity also gives `ell` coprime to `p*d`.

Exactly one of

```text
a-b,
a+b
```

vanishes modulo `ell`.

If `a=b mod ell`, then

```text
Pminus=W1W2-V1V2 = V1*(m-n)^2 mod ell,
Pplus =W1W2+V1V2 = V1*(m+n)^2 mod ell.
```

Because `ell` does not divide `U2`, neither `m-n` nor `m+n` vanishes. Hence

```text
Pplus/Pminus = ((m+n)/(m-n))^2 mod ell.
```

If `a=-b mod ell`, the same computation gives

```text
Pplus/Pminus = ((m-n)/(m+n))^2 mod ell.
```

Since `p*d` is a unit modulo `ell`, the same ratio holds for `Lplus/Lminus`. On `B35`, `Lminus=x^2` is a nonzero square modulo `ell`. Therefore

```text
(Lplus/ell)=+1
```

for every odd `ell|D_clean`.

The argument is symmetric for every odd `ell|T_clean`. Thus exactly

```text
(Lplus/D_clean)=+1,
(Lplus/T_clean)=+1.                            (DT-CLEAN-JACOBI)
```

and

```text
gcd(Lplus,D_clean*T_clean)=1.
```

Because `Lplus=1 mod4`, reciprocity returns

```text
(D_clean/Lplus)=+1,
(T_clean/Lplus)=+1.                            (DT-CLEAN-RECIP)
```

No claim is made for the full `D` or full `T`. The removed factors `D_ram,T_ram` remain in the `c`-ramified layer.

## 3. The common even-leg channel q is automatically +1

Put

```text
q=gcd(V1,V2),
q_odd=odd part of q.
```

For an odd prime `ell|q`, primitivity of the two source Pythagorean triples gives

```text
ell does not divide W1*W2.
```

Also `ell` is coprime to `p*d`. Modulo `ell`,

```text
Pminus = Pplus = W1*W2 != 0.
```

Hence

```text
Lminus = Lplus mod ell.
```

Since `Lminus` is a square on `B35`, every odd `ell|q` satisfies

```text
(Lplus/ell)=+1.
```

Therefore

```text
(Lplus/q_odd)=+1,
(q_odd/Lplus)=+1.                              (Q-JACOBI)
```

Again the second equality uses `Lplus=1 mod4`, so reciprocity contributes no sign.

Thus the old `q` source channel is globally neutral at this layer.

## 4. Residual squarefree kernel and genuinely unramified source support

Let

```text
S = sf(Lplus).
```

35EX-15 proves every prime of `S` is `1 mod4`; hence

```text
S == 1 mod4.
```

Since `Lplus=S*y^2` for an integer `y`, every source integer `M` coprime to `Lplus` satisfies

```text
(M/Lplus)=(M/S).
```

Applying this only to the proved clean channels gives

```text
(D_clean/S)=+1,
(T_clean/S)=+1,
(q_odd/S)=+1.
```

Because all primes of `S` are `1 mod4`, reciprocity again has no sign:

```text
(S/D_clean)=+1,
(S/T_clean)=+1,
(S/q_odd)=+1.                                 (S-CLEAN)
```

These are compatibility identities, not contradictions.

No corresponding universal `+1` statement is asserted for `D_ram` or `T_ram`; their prime support lies inside `supp(c)` and remains ramified.

## 5. Where nontrivial ramification can still live

The clean relations do not exhaust the source gcd data.

### 5A. c, including c-shared D/T support, is sign-ramified

For an odd prime `ell|c`, write

```text
a = eps1*b mod ell,
m = eps2*n mod ell,
eps1,eps2 in {+1,-1}.
```

Then

```text
eps1*eps2=+1  => ell|Pminus and ell does not divide Pplus,
eps1*eps2=-1  => ell|Pplus  and ell does not divide Pminus.
```

Since `p*d` is coprime to `c`, the same support allocation holds for `Lminus,Lplus`.

A prime may also divide `D` or `T` after one copy of the common gcd has been removed; precisely those contributions lie in `D_ram` or `T_ram`. They are therefore retained in this same `c`-ramified layer rather than promoted to a clean Jacobi channel.

Thus the prime support of `c` and its higher-valuation overlap with `D/T` is dynamically allocated by source signs and valuations. There is no fixed global symbol for this full layer supplied by the current identities.

### 5B. p and d are normalization-ramified split primes

Every odd prime of `p*d` is `1 mod4`. Its behavior after dividing the common gcd from `Pminus,Pplus` depends on the relative cross valuations and leading residues in

```text
W1 versus V2,
V1 versus W2.
```

When the cross valuations balance, one normalized factor may acquire extra valuation; when they do not balance, the two normalized factors remain units with a `+1` or `-1` ratio, and `-1` is already a square because the prime is `1 mod4`.

Thus `p,d` provide no fixed reciprocity sign either. Their potentially nontrivial contributions are moving split-prime ramification data.

### 5C. the residual kernel S is moving

35EX-15 already gives an exact branch witness with

```text
S=29*101
```

outside the prior odd source support. No fixed finite support or fixed modulus for `S` has been proved.

So the potentially nontrivial global reciprocity layer is confined to a moving ramified set built from

```text
c (including D_ram,T_ram), p, d, S,
```

with no source-locked parity relation coupling those split-prime allocations.

## 6. Hilbert/Jacobi route boundary

The global product formula for Hilbert symbols is not itself a contradiction: it requires fixed local symbol information at all ramified places. Here the genuinely unramified source channels are already `+1`, while the remaining ramified places move with the source parameters and have no proved fixed local values.

Restricting `D,T` to `D_clean,T_clean` enlarges, rather than shrinks, the unresolved ramified layer. Therefore the exact legal conclusion remains

```text
CURRENT_COPRIME_PAIR_GLOBAL_JACOBI_LAYER_GIVES_NO_CONTRADICTION=true
ALL_GLOBAL_RECIPROCITY_OR_HILBERT_ARGUMENTS_RULED_OUT=false
CURRENT_COPRIME_PAIR_GLOBAL_RECIPROCITY_ROUTE=FROZEN_MOVING_RAMIFICATION
```

This does not assert that a deeper reciprocity theorem cannot exist. It freezes the current natural Jacobi/Hilbert layer because every proved clean source contribution is `+1` and all remaining nontrivial contributions are moving ramification.

The current Arsenal registry has no formal card matching a new global Jacobi/Hilbert coupling theorem for this receiver.

## 7. Route decision

The fresh breadth audit now has one preserved untested route left:

```text
E1-PRODUCT-HYPOTENUSE-NONNAIVE-DESCENT.
```

The next active leaf is therefore

```text
35EX-17_PRODUCT_HYPOTENUSE_SUCCESSOR_OR_NO_SELF_MAP
```

It must use the exact primitive triple forced by full receiver failure,

```text
2*R*S      = V1*V2/(p*d),
R^2+S^2    = W1*W2/(p*d),
R^2-S^2    = sqrt(N)/(p*d),
```

and test whether it reconstructs a new admissible Master-Hit + E1-counterexample tuple with a strictly smaller well-founded height. If the original two Euclid triples and their canonical gcd channels cannot be recovered in a same-type decreasing way, freeze the descent route and trigger the parking/breadth protocol rather than inventing a successor.

## Credit boundary

```text
PAIR_JACOBI_RELATION_TAUTOLOGICAL=true
DT_CLEAN_MEANS_C_COPRIME_PARTS_ONLY=true
D_RAM_T_RAM_RETAINED_IN_C_RAMIFIED_LAYER=true
DT_AND_Q_CLEAN_CHANNELS_JACOBI_PLUS_ONE=true
CURRENT_COPRIME_PAIR_GLOBAL_RECIPROCITY_ROUTE_FROZEN_MOVING_RAMIFICATION=true
ALL_GLOBAL_RECIPROCITY_OR_HILBERT_ARGUMENTS_RULED_OUT=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
