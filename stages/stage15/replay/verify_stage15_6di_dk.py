from pathlib import Path

base=Path('stages/stage15')
di=(base/'15-6di/result.md').read_text()
dj=(base/'15-6dj/result.md').read_text()
dk=(base/'15-6dk/result.md').read_text()

assert 'RECONSTRUCTED_GRAPH_PACKET_EXACT=true' in di
assert 'LOCAL_MAIN_DENSITY_PER_ORIENTATION=q^-2' in di
assert 'EXACT_PHI_WEIGHTS_PRESERVED=true' in di
assert 'WHOLE_FAMILY_SECOND_MOMENT_DEFINED=true' in dj
assert 'SAME_ORIENTATION_COLLISION_IMPLIES_Q_DIVIDES_J=true' in dj
assert 'DIAGONAL_BOUND=GRAPH_MASS*Q0*B^o(1)' in dj
assert 'SQRT_COLLISION_TARGET_PROVED=false' in dj
assert 'DISPERSION_IDENTITY_CERTIFIED=true' in dk
assert 'SQRT_COLLISION_ENERGY_PROVED=false' in dk
assert 'DELTA_PROVED=false' in dk and 'SIGMA_PROVED=false' in dk
assert 'STAGE14_FIXED_PACKET_TRANSFER=false' in dk
assert 'AUDIT_REQUIRED=true' in dk and 'MERGE_ALLOWED=false' in dk
print('Stage15-6 main-batch di-dk: PASS')