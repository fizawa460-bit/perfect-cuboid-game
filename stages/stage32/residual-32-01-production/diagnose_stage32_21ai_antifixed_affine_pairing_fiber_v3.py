#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp, smith_normal_form

from direct_picard_reynolds_lattice_diagnostic import EXPECTED_FIXED_RANK, GROUP_ORDER, PICARD_RANK, csha, exact_column_lattice_basis_lowrank, load_retained
from direct_picard_reynolds_rank2_integral_projection_bound import build_reynolds_numerator
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter, RETAINED_BASIS_KNOWN_LABELS_1BASED

ANTI_RANK=PICARD_RANK-EXPECTED_FIXED_RANK; CURVES=140; ORBITS=14

def ml(m): return [[int(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]
def nzdiag(d): return tuple(abs(int(d[i,i])) for i in range(min(d.rows,d.cols)) if int(d[i,i]))

def coords_in_basis(m,b):
    piv=tuple(int(i) for i in b.T.rref()[1]); inv=b[list(piv),:].inv(); cols=[]
    if len(piv)!=EXPECTED_FIXED_RANK: raise ValueError('fixed-image pivot regression')
    for j in range(m.cols):
        x=inv*Matrix([m[i,j] for i in piv])
        if b*x!=m[:,j] or any(v.q!=1 for v in x): raise ValueError(f'im(N) coordinate regression at {j}')
        cols.append(Matrix([int(v) for v in x]))
    return Matrix.hstack(*cols)

def build(marking,bundle):
    adapter=HperpIntegralPairingAdapter.from_retained(marking,bundle); bridge=DirectPicardSliceBridge.from_retained(marking,bundle); gram=Matrix(bundle['picard_gram_64x64'])
    phi=Matrix([list(bridge.degree_functional),list(bridge.exceptional_mass_functional),list(bridge.first_normal_half_functional)])
    N,subgroup,action_sha=build_reynolds_numerator(marking,adapter,gram,phi); B,bstats=exact_column_lattice_basis_lowrank(N,EXPECTED_FIXED_RANK); C=coords_in_basis(N,B)
    if B*C!=N: raise ValueError('N=B*C regression')
    D,S,T=smith_normal_decomp(C,domain=ZZ)
    if S*C*T!=D or nzdiag(D)!=(1,1,1,1,1): raise ValueError('C Smith/surjectivity regression')
    K=T[:,EXPECTED_FIXED_RANK:]
    if K.shape!=(PICARD_RANK,ANTI_RANK) or N*K!=Matrix.zeros(PICARD_RANK,ANTI_RANK) or phi*K!=Matrix.zeros(3,ANTI_RANK): raise ValueError('anti-fixed saturated kernel regression')

    pairing=adapter.pairing_matrix; M=pairing*K; ridx=[i-1 for i in RETAINED_BASIS_KNOWN_LABELS_1BASED]; R=M.extract(ridx,list(range(ANTI_RANK)))
    if R!=gram*K: raise ValueError('retained pairing block != Gram*K')
    coords=adapter.class_coordinates_in_retained_basis
    if M!=coords*R: raise ValueError('all140 pairing rows not integral combinations of retained pairing block')
    # rows of R are a subset of rows of M; M=coords*R with integral coords.
    # Hence row_Z(M)=row_Z(R) exactly. K has independent columns and Gram is nonsingular,
    # so R and M have exact rank 59 without wide elimination.

    unvisited=set(range(CURVES)); orbits=[]
    while unvisited:
        seed=min(unvisited); orbit=tuple(sorted({g[seed] for g in subgroup})); orbits.append(orbit); unvisited.difference_update(orbit)
    if len(orbits)!=ORBITS: raise ValueError('orbit count regression')
    O=Matrix.zeros(ORBITS,CURVES)
    for oi,o in enumerate(orbits):
        for i in o: O[oi,i]=1
    if O*M!=Matrix.zeros(ORBITS,ANTI_RANK): raise ValueError('anti-fixed orbit total regression')
    pairing_B=pairing*B; totals=[]
    for o in orbits:
        row=[]
        for j in range(EXPECTED_FIXED_RANK):
            n=len(o)*int(pairing_B[o[0],j])
            if n%GROUP_ORDER: raise ValueError('projected orbit total nonintegral')
            row.append(n//GROUP_ORDER)
        totals.append(row)
    total_map=Matrix(totals)

    print(json.dumps({'phase':'retained_pairing_row_hnf_start','shape':[R.cols,R.rows]}),flush=True)
    H=hermite_normal_form(R.T)
    if H.shape!=(ANTI_RANK,ANTI_RANK) or int(H.det())==0: raise ValueError(f'row HNF regression {H.shape}')
    print(json.dumps({'phase':'retained_pairing_row_hnf_complete','shape':[H.rows,H.cols]}),flush=True)
    SD=smith_normal_form(H,domain=ZZ); sdiag=nzdiag(SD)
    if len(sdiag)!=ANTI_RANK: raise ValueError('pairing Smith rank regression')
    index=math.prod(sdiag)

    cert={
      'schema':'STAGE32_21AI_ANTIFIXED_AFFINE_PAIRING_FIBER_STRUCTURE_V3_RETAINED64_ROW_LATTICE',
      'mode':'EXACT_SATURATED_REYNOLDS_ANTIFIXED_INTEGER_KERNEL_TO_ALL140_PAIRING_LATTICE',
      'slice_stabilizer_group_order':GROUP_ORDER,'picard_rank':PICARD_RANK,'fixed_rank':EXPECTED_FIXED_RANK,'anti_fixed_integer_rank':ANTI_RANK,'known_curve_count':CURVES,
      'adapter_certificate_sha256':adapter.certificate['canonical_sha256_without_this_field'],'slice_bridge_certificate_sha256':bridge.certificate['canonical_sha256_without_this_field'],'reynolds_numerator_sha256':csha(ml(N)),'action_hashes_sha256':action_sha,
      'fixed_image_basis_sha256':csha(ml(B)),'fixed_image_column_module_stats':bstats,
      'fixed_coordinate_map':{'shape':[C.rows,C.cols],'sha256':csha(ml(C)),'smith_nonzero_diagonal':list(nzdiag(D)),'surjective_to_Z5':True},
      'anti_fixed_integer_kernel':{'shape':[K.rows,K.cols],'sha256':csha(ml(K)),'rank':ANTI_RANK,'saturated':True,'N_times_kernel_zero':True,'phi_times_kernel_zero':True},
      'all140_pairing_image':{
        'shape':[M.rows,M.cols],'sha256':csha(ml(M)),'rank':ANTI_RANK,'left_rational_relation_rank':CURVES-ANTI_RANK,
        'retained64_pairing_block_sha256':csha(ml(R)),'all140_equals_integral_coordinate_matrix_times_retained64_block':True,
        'row_Z_all140_equals_row_Z_retained64_exact':True,'row_lattice_hnf_sha256':csha(ml(H)),
        'smith_nonzero_diagonal':list(sdiag),'nonunit_smith_factor_count':sum(v!=1 for v in sdiag),'maximum_smith_factor':max(sdiag),
        'saturation_index_in_rational_span':index,'has_nontrivial_modular_coupling':index>1,
        'wide_140x59_smith_required':False,'exact_reduction':'row_Z(M)=row_Z(R), then column-HNF of R^T (59x64) followed by Smith of 59x59 HNF'},
      'stabilizer_orbit_decomposition':{
        'orbit_count':len(orbits),'orbit_sizes':sorted(len(o) for o in orbits),'orbit_sum_variation_zero_exact':True,'orbit_zero_ambient_rank':CURVES-len(orbits),
        'anti_fixed_rational_codimension_inside_orbit_zero_space':CURVES-len(orbits)-ANTI_RANK,
        'within_orbit_difference_rank':ANTI_RANK,'within_orbit_difference_rank_proof':'zero within-orbit differences plus zero orbit sums imply Mz=0; retained Gram*K block is injective',
        'projected_orbit_total_map_shape':[total_map.rows,total_map.cols],'projected_orbit_total_map_rank':int(total_map.rank()),'projected_orbit_total_map_sha256':csha(ml(total_map)),'projected_orbit_totals_integral_for_every_fixed_image_basis_generator':True},
      'interpretation':{'historical_direct_integral_coset_bound_equivalent':False,'historical_orbit_coordinate_cauchy_bound_equivalent':False,'simultaneous_nonnegative_fiber_feasibility_solved':False,'self_intersection_threshold_solved_on_fiber':False,'next_if_modular_coupling_nontrivial':'derive compact exact affine pairing-fiber membership/congruence filter before norm search','next_if_modular_coupling_trivial':'use 81 rational pairing relations and nonnegative orbit-composition constraints; skip modular-sieve leaf'},
      'safety':{'heavy_run_key_used':False,'full178_production_run':False,'legacy_prefix_dfs_run':False,'59d_cvp_run':False,'terminal_family_materialization_run':False,'unknown_is_not_unsat':True,'numerical_row_complete':False,'theorem_credit':False,'receiver_credit':False,'route_credit':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False}}
    cert['canonical_sha256_without_this_field']=csha(cert); return cert

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--retained',type=Path,required=True); ap.add_argument('--marking',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    cert=build(load_retained(a.marking,'s32_21ai_v3_marking'),load_retained(a.retained,'s32_21ai_v3_picard')); a.output.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n'); p=cert['all140_pairing_image']; o=cert['stabilizer_orbit_decomposition']
    print(json.dumps({'verdict':'PASS_STAGE32_21AI_ANTIFIXED_AFFINE_PAIRING_FIBER_STRUCTURE','anti_fixed_integer_rank':cert['anti_fixed_integer_rank'],'pairing_image_rank':p['rank'],'pairing_relation_rank':p['left_rational_relation_rank'],'nonunit_smith_factor_count':p['nonunit_smith_factor_count'],'maximum_smith_factor':p['maximum_smith_factor'],'saturation_index':str(p['saturation_index_in_rational_span']),'orbit_count':o['orbit_count'],'orbit_zero_codimension':o['anti_fixed_rational_codimension_inside_orbit_zero_space'],'within_orbit_difference_rank':o['within_orbit_difference_rank'],'canonical_sha256':cert['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
