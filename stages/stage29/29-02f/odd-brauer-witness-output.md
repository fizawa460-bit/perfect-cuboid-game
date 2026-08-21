# Stage29-02f — exact odd-Brauer witness checkpoint

```text
SCRIPT=stages/stage29/29-02f/odd_brauer_frobenius_witness.py
ARITHMETIC=EXACT_INTEGER
STATUS=PASS
```

| p | 2p-a(h16) | 2p-a(h32) | 2p-a(h8) |
|---:|---:|---:|---:|
| 3 | 6 | 4 | 8 |
| 5 | 16 | 10 | 10 |
| 7 | 14 | 14 | 14 |
| 11 | 22 | 36 | 8 |
| 13 | 16 | 26 | 26 |
| 17 | 64 | 32 | 32 |
| 19 | 38 | 4 | 72 |
| 23 | 46 | 46 | 46 |
| 29 | 16 | 58 | 58 |
| 31 | 62 | 62 | 62 |
| 37 | 144 | 74 | 74 |
| 41 | 64 | 128 | 128 |
| 43 | 86 | 100 | 72 |
| 47 | 94 | 94 | 94 |

Exact gcds:

```text
gcd(2p-a(h16)) = 2
gcd(2p-a(h32)) = 2
gcd(2p-a(h8))  = 2

gcd((2p-a16)^3*(2p-a32)*(2p-a8)^3) = 128.
```

For each `ell` in the displayed prime set, deleting the row `p=ell` leaves a determinant gcd that is still a power of two.  Therefore every odd `ell` has an admissible witness prime `p!=ell` at which the twisted transcendental determinant at eigenvalue one is nonzero modulo `ell`.

The mathematical Brauer consequence still depends on the Kummer/Picard-saturation adapter and is audit-facing, not self-certified by this output alone.
