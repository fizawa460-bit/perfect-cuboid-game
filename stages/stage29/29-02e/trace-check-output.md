# Stage29-02e — exact finite-field K3 trace checkpoint

```text
SCRIPT=stages/stage29/29-02e/k3_trace_check.py
ARITHMETIC=EXACT_INTEGER_MOD_P
PRIMES=3,5,7,11,13,17,19,23,29,31,37,41,43,47
P2_EXCLUDED=true
STATUS=PASS_ALL_ASSERTIONS
```

For each singular three-quadric model, `pts` is the exact projective `F_p` point count, `nodes` is the number of rational Jacobian-rank-defect points, and

```text
T = (pts + p*nodes) - 1 - p^2
```

is the `H^2` trace of the smooth K3 resolution at these good odd primes. The displayed `pred` column is the corresponding modular/Tate candidate formula.

| p | Kc pts | nodes | T | pred | Kb pts | nodes | T | pred | Ka pts | nodes | T | pred |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 12 | 12 | 38 | 38 | 16 | 8 | 30 | 30 | 20 | 4 | 22 | 22 |
| 5 | 36 | 12 | 70 | 70 | 40 | 16 | 94 | 94 | 36 | 12 | 70 | 70 |
| 7 | 92 | 12 | 126 | 126 | 64 | 8 | 70 | 70 | 92 | 4 | 70 | 70 |
| 11 | 108 | 12 | 118 | 118 | 144 | 8 | 110 | 110 | 180 | 4 | 102 | 102 |
| 13 | 196 | 12 | 182 | 182 | 232 | 16 | 270 | 270 | 196 | 12 | 182 | 182 |
| 17 | 428 | 12 | 342 | 342 | 328 | 16 | 310 | 310 | 428 | 12 | 342 | 342 |
| 19 | 396 | 12 | 262 | 262 | 400 | 8 | 190 | 190 | 404 | 4 | 118 | 118 |
| 23 | 668 | 12 | 414 | 414 | 576 | 8 | 230 | 230 | 668 | 4 | 230 | 230 |
| 29 | 900 | 12 | 406 | 406 | 1000 | 16 | 622 | 622 | 900 | 12 | 406 | 406 |
| 31 | 1148 | 12 | 558 | 558 | 1024 | 8 | 310 | 310 | 1148 | 4 | 310 | 310 |
| 37 | 1444 | 12 | 518 | 518 | 1448 | 16 | 670 | 670 | 1444 | 12 | 518 | 518 |
| 41 | 1964 | 12 | 774 | 774 | 1864 | 16 | 838 | 838 | 1964 | 12 | 774 | 774 |
| 43 | 1836 | 12 | 502 | 502 | 1936 | 8 | 430 | 430 | 2036 | 4 | 358 | 358 |
| 47 | 2492 | 12 | 846 | 846 | 2304 | 8 | 470 | 470 | 2492 | 4 | 470 | 470 |

The formulas matched exactly at all 14 tested primes:

```text
K_c:
 T_Kc(p) = a_p(h32) + p*(16 + chi_-1(p) + 3 chi_2(p)).

K_b:
 T_Kb(p) = a_p(h16) + p*(15 + 5 chi_-1(p)).

K_a:
 T_Ka(p) = a_p(h8)
           + p*(13 + 4 chi_-1(p) + 2 chi_2(p) + chi_-2(p)).
```

At a prime splitting in all displayed quadratic fields, the algebraic-character multiplicities sum to `20` for each K3, consistent with a singular K3 / geometric Picard-rank-20 pattern. `K_c` rank 20 is independently source-locked by Testa--Stoll. For `K_a,K_b`, the finite-prime pattern itself is not promoted to a global Picard theorem here.

## Interpretation firewall

This exact regression makes the modular identification highly constrained, but equality at finitely many primes alone is not a proof of global equality of l-adic representations. Fresh audit must decide whether the source quotient decomposition plus these exact traces is enough to promote `R29-L3`, or whether a formal Faltings/CM/quotient-action adapter remains.

```text
FINITE_FIELD_REGRESSION=PASS_EXACT
GLOBAL_GALOIS_IDENTIFICATION_SELF_CERTIFIED=false
AUDIT_REQUIRED=true
```
