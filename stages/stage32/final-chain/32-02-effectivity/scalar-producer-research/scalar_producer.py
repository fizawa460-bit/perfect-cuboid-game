#!/usr/bin/env python3
import json, math

def scalar_record(row_id,d,negative_hperp_square_N):
 d=int(d); N=int(negative_hperp_square_N); m=16//math.gcd(d,16)
 return {"row_id":row_id,"d":d,"negative_hperp_square_N":N,"m":m,"rr_gate_lhs":16*N,"rr_gate_rhs":m*m*(d*d-16*d+224),"rr_effective_sufficient":d>16 and 16*N<=m*m*(d*d-16*d+224),"credit":{"authority":False,"pruning":False,"irreducible_member":False}}
if __name__=="__main__": print(json.dumps(scalar_record("example",18,0),sort_keys=True))
