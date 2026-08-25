# Stage32-18O — b14 resource-safe exact packet design

Stage32-18M rejected raw parent-prefix population as a runtime proxy. Stage32-18N then calibrated exact descendant work against the known b12 pathological residue: `26 mod 1024` rises from raw c54 rank 744 to c50 descendant-probe rank 32 and c48 rank 3. The matching b14 p50/p48 profiles are therefore used as a risk signal for the next production layout.

This leaf still does **not** launch the full b14 census. It constructs a deterministic 256-packet candidate partition over the exact existing c54 / mod-1024 residue classes and runs six representative full b14 packet pilots.

The risk score for residue `r` is

`max(p50_probe_prefixes(r)/mean_p50, p48_probe_prefixes(r)/mean_p48)`.

Packet policy:

- hybrid ranks 1..64: 64 singleton packets;
- ranks 65..256: 96 two-residue packets, pairing highest with lowest inside the tier;
- ranks 257..1024: 96 eight-residue packets, capacity-8 LPT-balanced by hybrid risk;
- exactly 256 packets cover all 1024 residues exactly once.

The historical b12 pathological residue 26 has hybrid rank 16 and is therefore isolated as packet 15. This is a calibration-derived safety margin rather than an assumption that residue 26 itself remains the b14 worst case.

The packet runner does not introduce a new C++ partition semantics. Each packet sequentially invokes the immutable exact 18E certifier once for every listed mod-1024 residue and then unions the completed exact outputs. Thus every unit of coverage is still the audited-style `h54 mod 1024 == residue` traversal with exact rational cap/symmetry rejection and full Aut canonicalization. Packet telemetry is explicitly the sum of independent residue runs and includes repeated pre-c54 work.

Pilot packets are `[0,15,63,64,173,210]`: highest-risk singleton, historical residue26 singleton, singleton boundary, highest-risk pair, highest-risk octet, and median-risk octet. Any node-cap wall is evidence for redesign/refinement, not a numerical result.

Firewalls: `D16_B14_NUMERICAL_CREDIT=false`, `GLOBAL_B14_AGGREGATION_COMPLETE=false`, `FULL_D16_G0_ROW_COMPLETE=false`, `THEOREM_CREDIT=false`, `RECEIVER_CREDIT=false`, `CONTROLLER_MODIFIED=false`.
