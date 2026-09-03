# Stage35-35-10 — Peschmann material-input source note

## Purpose

This note checks whether Peschmann's 2026 perfect-cuboid papers provide a **material reopen input for the exact Stage35 moving-fiber receiver** `R29-FIB2 / T35-R3-PHYS-EMPTY`. It is a routing/source note only. It grants no theorem, receiver, parent-route, Stage35, or perfect-cuboid credit.

## External sources inspected

### arXiv:2604.28072 — *A torsion-intersection proof of perfect-cuboid nonexistence on 1072 explicit master-tuple fibers*

Current arXiv metadata identifies v1 as submitted 2026-04-30; the current HTML displays `Date: April 30, 2026`.

Load-bearing source facts:

- Theorem 2.4 / Theorem 1.2 proves that every primitive Euler brick, after choosing the unique odd edge `X`, comes from a unique master tuple `(a,b,m,n)` up to the stated `Y/Z` swap, with

  ```text
  X=U1*U2/g,
  Y=V1*U2/g,
  Z=U1*V2/g,
  g=gcd(U1,U2).
  ```

- This global master-tuple coverage theorem is **already independently audited in Stage29-08** (`source-refresh.md`, `peschmann-exact-crosswalk.md`). It is therefore not new Stage35 theorem credit.
- The torsion-intersection theorem is unconditional only on fixed `(m,n)` fibers satisfying a rank-zero plus exact torsion-lift hypothesis. The paper exhibits 1,072 such fibers. This is a proof-capable **fixed-fiber terminal method**, not a uniform theorem over every parameter.

### arXiv:2605.00573 — *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*

Current arXiv metadata records only v1, submitted 2026-05-01; no later arXiv version or 2026-08-24 manuscript date is asserted here.

Load-bearing source facts:

- For a Master-Hit, define

  ```text
  f1=(W1*U2)^2+(U1*V2)^2,
  g0=gcd(W1*U2,U1*V2),
  xi=(W1*U2)/g0,
  eta=(U1*V2)/g0.
  ```

- Lemma 4.13 gives the exact identity

  ```text
  f1=g0^2*(xi^2+eta^2),  gcd(xi,eta)=1.
  ```

- Conjecture 4.7 (basis form) says every Master-Hit has at least one blocker. This is enough to exclude a perfect cuboid **within the Master-Hit population**.
- Conjecture 4.14 (`Conjecture E1`) sharpens the proof target to

  ```text
  xi^2+eta^2 is never a square for a Master-Hit.
  ```

  Proposition 4.15 shows this implies the basis blocker conjecture and hence the conditional nonexistence conclusion.
- The paper explicitly leaves the proof open. Its proposed route combines the Master condition with hypothetical Pythagoreity of `(xi,eta)` and seeks a height/discriminant contradiction on `E_mn`; it states that the general discriminant is not sufficiently factor-controllable and that the proof stalls there.
- The verification on 151,575 fully factored Master-Hits and the exact non-perfect check on 1,284,670 database Master-Hits are finite evidence only.
- The paper's genus-one `H_mn -> E_mn` construction is already crosswalked in Stage29-08. Bounded Mordell-Weil enumeration is not exhaustive.

### arXiv:2604.09328 — *Quartic reductions and elliptic obstructions for perfect Euler bricks*

This source supplies the genus-3 `C_A`, Kummer-character and 2-descent obstructions. It explicitly says the remaining descent classes are open and presents a genus-5 covering obstruction only as a possible future route. No uniform all-parameter closure theorem is supplied.

## Exact repo cross-check

Stage29 already owns a sibling Class-3 kernel

```text
K16-C3-PESCH-EXPONENT-ONE
child: R29-PESCH-E1
needed: proof of the universal exponent-one blocker or a replacement theorem with the same global Master-Hit coverage consequence
```

and Stage29-08 already certified global endpoint coverage through the master-tuple reduction theorem.

Stage35 instead owns

```text
K16-C3-MOVING-FIBER-ARITHMETIC
child: R29-FIB2
exact selected route: TS-S-R3-Q1
remaining target: T35-R3-PHYS-EMPTY
```

where the missing quantifier is uniform emptiness of the physical open for **every rational `t>1`**.

## Source-level conclusion

The inspected material is mathematically relevant but does **not** prove or directly strengthen `T35-R3-PHYS-EMPTY`:

- Conjecture E1 is an alternative global Master-Hit replacement target and belongs primarily to the sibling `K16-C3-PESCH-EXPONENT-ONE` kernel.
- The 1,072-fiber torsion-intersection theorem is a proof-capable fixed-fiber closure tool, but Stage35 has no globally exhaustive reduction from all `t in Q_{>1}` to those fibers.
- Kummer/2-descent/genus-5-cover material remains incomplete and does not uniformly exclude specialization-new physical points on `TS-S-R3-Q1`.

Therefore this source check is a **material-input routing assessment**, not a Stage35 research reopen or closure certificate.

```text
NEW_STAGE35_UNIFORM_THEOREM=false
NEW_STAGE35_GLOBAL_FINITE_REDUCTION=false
NEW_STAGE35_UNIFORM_RECEIVER_OBSTRUCTION=false
PESCHMANN_E1_IS_SIBLING_KERNEL_REPLACEMENT_TARGET=true
FIXED_FIBER_TORSION_INTERSECTION_IS_PROOF_CAPABLE_TERMINAL_METHOD=true
R29_FIB2_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
```
