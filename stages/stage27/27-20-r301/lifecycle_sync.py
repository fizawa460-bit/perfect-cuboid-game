#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/'stages/stage27/27-controller.json'
ctl=json.loads(cp.read_text())
ctl['derived_routes']['Stage27-20-r301']={
  'status':'PARALLEL_PREFLIGHT_SUBMITTED_PENDING_FRESH_AUDIT',
  'trigger_checkpoint':30,
  'route_serial':'20-r301',
  'route_kind':'UPPER_REENTRY_PREFLIGHT',
  'source_stage':'Stage20',
  'purpose':'test which Stage20 Euler-brick upper mechanisms legally transfer to the Stage27 N2 space-diagonal completion problem on the common two-face host',
  'population_noncontainment_proved':True,
  'common_two_face_host_identified':True,
  'e8_raw_transplant_dominated':True,
  'stage20_local_factors_direct_transfer_forbidden':True,
  'space_diagonal_thin_cover_fixed_power_theorem_proved':False,
  'strict_sub_sqrt_upper_proved':False,
  'new_mu_lt_half_proved':False,
  'true_N2_exponent_identified':False,
  'audit_status':'PENDING',
  'parallel_route':True,
  'advance_allowed':False,
  'merge_allowed':False,
  'next_derived_route':'27-20-r301a'
}
ctl['safety']['stage20_M3_upper_promoted_to_N2_upper']=False
ctl['safety']['stage20_third_face_local_factors_copied_to_space_diagonal']=False
cp.write_text(json.dumps(ctl,indent=2)+'\n')
