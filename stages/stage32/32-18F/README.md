# Stage32-18F — exact b12 shard26 rescue

Purpose: provide a bounded exact fallback for Stage32-18E run `32877018247` if 64-way shard 26 hits its 180-minute/resource wall.

The inherited partition is `h % 64 == shard_id` at split coordinate 54. Therefore parent shard 26 is exactly and disjointly

`h % 256 in {26, 90, 154, 218}`.

The rescue workflow reuses the immutable Stage32-18E prepared artifact `9574308138`, runs those four 256-way exact subshards with the same bound, 256 genuine Aut breakers, exact rational Cauchy–Schwarz branch rejection, and full leaf canonicalization, then synthesizes a replacement 64-way shard-26 JSON/bin accepted by the existing Stage32-18E aggregate contract.

This leaf does **not** perform global b12 aggregation and grants no numerical/theorem/receiver credit. It remains pending global aggregation and hostile audit. If the original 64-way shard 26 completes, the rescue result may be retained only as an independent exact partition cross-check.
