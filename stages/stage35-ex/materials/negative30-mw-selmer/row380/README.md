# Row380 evidence

Use Python 3.11+ with python-flint. Run from the extracted directory.

```sh
sha256sum -c SHA256SUMS
python verify_row380.py > replay.json
cmp replay.json row380_exact.json
```

The fixed witnesses certify ideal support with integer resultants, modular
factorization, Hensel lifting when needed, and exact binary linear algebra.
The three additional units use the row373 arithmetic and row374 local model.
Parent facts used by this replay are the maximal order and discriminant
(row373–374), ordinary Artin characters (row376), the full paired table
(row378), and the independently audited tail root counts (row379). The
conditional calculation uses the row379 trial-function arithmetic. The
analytic envelope uses the same tail counts and Arb intervals. Independently
recreating the tail table is optional using the included audit C++ source.

The numeric search for witnesses and the optional root count recreation do
not enter the default replay. An independent mathematical audit of row380
is pending.
