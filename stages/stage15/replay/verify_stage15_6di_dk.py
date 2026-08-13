from pathlib import Path

base=Path('stages/stage15')
di=(base/'15-6di/result.md').read_text()
dj=(base/'15-6dj/result.md').read_text()
dk=(base/'15-6dk/result.md').read_text()
dl=(base/'15-6dl/result.md').read_text()

assert 'RECONSTRUCTED_GRAPH_PACKET_EXACT=true' in di
assert 'LOCAL_MAIN_DENSITY_PER_ORIENTATION=q^-2' in di
assert 'EXACT_PHI_WEIGHTS_PRESERVED=true' in di

assert 'ORIENTATION_MEAN_DECOMPOSITION_EXACT=true' in dj
assert 'MODULUS_OCCUPANCY_BIAS_TERM_DEFINED=true' in dj
assert 'SIGNED_ERROR_EQUALS_OCCUPANCY_RESIDUAL=true' in dj
assert 'COLLISION_ENERGY_CONTROLS_ORIENTATION_VARIANCE_ONLY=true' in dj
assert 'SQRT_COLLISION_ALONE_IMPLIES_DELTA=false' in dj
assert 'OCCUPANCY_PAIR_KERNEL_EXACT=true' in dj
assert 'OCCUPANCY_SQRT_TARGET_PROVED=false' in dj

assert 'EXHAUSTIVE_VIEW_AUDIT=true' in dk
assert 'OCCUPANCY_BIAS_IS_PRIMARY_ERROR_GATE=true' in dk
assert 'OCCUPIED_Q_DIVIDES_DELTA=true' in dk
assert 'ORIENTATION_BLIND_PAIR_RESULTANT_SQUARE_LOCK=true' in dk
assert 'PAIR_LOCK=q^2_divides_R_pair' in dk
assert 'OCCUPANCY_SQRT_TARGET_PROVED=false' in dk
assert 'KG2_DELTA_ALONE_SUFFICIENT=false' in dk
assert 'DIVISOR_SWITCH_OCCUPANCY_GAIN_PROVED=false' in dk

assert 'BLIND_REDISCOVERY=true' in dl
assert 'LIVE_CANDIDATES_PRESERVED=true' in dl
assert 'SELECTED_ROUTE=ORIENTATION_BLIND_PAIR_RESULTANT_OCCUPANCY_ENERGY' in dl
assert 'GENERAL_CONDITIONAL_DELTA=(1-kappa)/2-theta/2' in dl
assert 'DELTA_PROVED=false' in dl and 'SIGMA_PROVED=false' in dl
assert 'EXECUTABLE_OVERLAP_WINDOW=false' in dl
assert 'AUDIT_REQUIRED=true' in dl and 'MERGE_ALLOWED=false' in dl
print('Stage15-6 main-batch di-dl repaired: PASS')
