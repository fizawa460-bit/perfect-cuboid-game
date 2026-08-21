# Stage29-09 — exact local regression checkpoint

```text
SCRIPT=stages/stage29/29-09/local_density_check.py
ARITHMETIC=EXACT_INTEGER_AND_RATIONAL
CHECK_RANGE=ODD_PRIMES_BELOW_50_DISPLAYED
STATUS=PASS
```

Columns: `host0=(p-3)^2`; `A_k` is the eligible common-character count at branch depth `k`; `Sbar` is reconstructed from `64A0+32A1+16A2+8A3`.

| p | eps | eta | aE | host0 | A0 | A1 | A2 | A3 | Sbar |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | -1 | -1 | 0 | 0 | 0 | 0 | 0 | 3 | 24 |
| 5 | 1 | -1 | -2 | 4 | 0 | 0 | 0 | 6 | 48 |
| 7 | -1 | 1 | 0 | 16 | 0 | 3 | 0 | 3 | 120 |
| 11 | -1 | -1 | 0 | 64 | 0 | 6 | 0 | 3 | 216 |
| 13 | 1 | -1 | 6 | 100 | 0 | 8 | 0 | 6 | 304 |
| 17 | 1 | 1 | 2 | 196 | 0 | 12 | 3 | 6 | 480 |
| 19 | -1 | -1 | 0 | 256 | 0 | 12 | 0 | 3 | 408 |
| 23 | -1 | 1 | 0 | 400 | 4 | 15 | 0 | 3 | 760 |
| 29 | 1 | -1 | -10 | 676 | 0 | 36 | 0 | 6 | 1200 |
| 31 | -1 | 1 | 0 | 784 | 9 | 21 | 0 | 3 | 1272 |
| 37 | 1 | -1 | -2 | 1156 | 0 | 44 | 0 | 6 | 1456 |
| 41 | 1 | 1 | 10 | 1444 | 12 | 42 | 3 | 6 | 2208 |
| 43 | -1 | -1 | 0 | 1600 | 18 | 30 | 0 | 3 | 2136 |
| 47 | -1 | 1 | 0 | 1936 | 25 | 33 | 0 | 3 | 2680 |

The script's default range is all odd primes below 100 and asserts every branch formula before printing the final PASS line.

Two small-prime features are intentional: `A0` can vanish while branch neighborhoods still carry local points, and the `p=2` place is not represented by this odd-prime table.
