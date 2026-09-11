import math
REQUIRED={'row_id','terminal_identity','d','m','integral_picard_witness','negative_hperp_square_N','witness_source_locks'}
def validate(record):
 missing=sorted(REQUIRED-set(record))
 if missing: raise ValueError('missing producer fields: '+','.join(missing))
 if record['m']!=16//math.gcd(int(record['d']),16): raise ValueError('m/d mismatch')
 return True
