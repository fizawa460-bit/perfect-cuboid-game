# Stage32-18U — three-residue b14 tail rescue

Stage32-18T run `32972417382` reduced the exact bulk complement to three unfinished packets: 127, 158, and 162. Its V3 union snapshot proves that every residue in those packets is already COMPLETE except residue 436 in packet 127, residue 922 in packet 158, and residue 503 in packet 162. Each of these three individual residue traversals exceeded the 120-minute regular-packet job limit.

18U does not rerun any completed packet or completed residue. It fixes the original `h54 mod 1024` residue gate and partitions that one residue again at coordinate 45 into four exact secondary shards. The four children are recombined into an exact original-residue certificate, then combined with the carried COMPLETE residue certificates from the locked 18T snapshot. The resulting packet is independently verified by the full Aut group verifier.

The heavy phase has exactly 12 secondary-shard jobs and `max-parallel: 12`, below the requested Stage32 global cap of 15. No b14 numerical, theorem, receiver, or controller credit is granted here. Final source-union accounting remains in Stage32-18T and global b14 integration remains Stage32-18R.
