# S316 standalone finite replay (verified separately from mathematical proof)

Source proof: [S316.md](../S316.md), [root dependency map](../../../ACTIVE-ANCESTOR-DEPENDENCY-MAP.md).

| Item | Original Google Drive source | SHA256 of exact bytes |
|---|---|---|
| [section316_verify.py](section316_verify.py) | https://drive.google.com/file/d/1szxMh3gl_nnPmnbF4jxwyS2QH4QuGujn/view | `ae90b51447fa0422e4c48d69caa4107b6be296b6e4dff4cef0832e337ddd25de` |
| [section316_verify_result.json](section316_verify_result.json) | https://drive.google.com/file/d/11GQ6u2lGO6I3lPM0fYWLSGGl6hDqimF9/view | `ae894fc201396b32de173d111e9837e35193c18dcc89c1bf38b5d2a341fa2a57` |

Run using Python 3 with standard library only, from this directory:

```sh
python3 -I section316_verify.py > section316_actual.json
cmp section316_actual.json section316_verify_result.json
sha256sum section316_verify.py section316_verify_result.json section316_actual.json
```

**Execution recorded 2026-11-09:** the original standalone script was inspected, run in isolated Python mode (`python3 -I`), and yielded an output of 5,384 bytes byte-identical to the downloaded expected JSON. All reported counts agreed: 21 exact original formal-depth checks, 2,724 low-C integer floor controls, 1,225 high-stratum cutoff controls, and 8 oriented Euclid panels. The expected replay JSON digest excluding its digest field was also equal. Original Drive file SHA256 values were checked against the historical S316 readback receipt.

**Evidence scope:** independent execution of the `section316_verify.py` finite diagnostics and JSON equality is PASS. Independent mathematical checking of the universal height inequalities, the asymptotic original-source census, underlying S252/S291/S308/S270 assumptions, and applicability to every physical mask is **NOT PERFORMED**. This evidence does **not** prove physical source nonexistence, all LOW, −30, or Branch B closure. Source proof and its historical status retain their own caveats.

The generated `section316_actual.json` need not be separately stored because it must equal the retained `section316_verify_result.json` byte-for-byte.
