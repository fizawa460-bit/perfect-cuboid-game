import math
from fractions import Fraction
REQUIRED={'schema','row_id','terminal_identity','d','m','picard64_coordinates','selected64_pairings','C2','negative_hperp_square_N','witness_source_locks'}
def validate(record):
 missing=sorted(REQUIRED-set(record))
 if missing: raise ValueError('missing producer fields: '+','.join(missing))
 if record['schema']!='STAGE32_32_02_SCALAR_PRODUCER_V1': raise ValueError('schema mismatch')
 for key in ('d','m','C2','negative_hperp_square_N'):
  if type(record[key]) is not int: raise ValueError('exact integer required: '+key)
 if record['d']<=0 or record['negative_hperp_square_N']<0: raise ValueError('invalid degree/norm')
 if record['m']!=16//math.gcd(record['d'],16): raise ValueError('m/d mismatch')
 for key in ('row_id','terminal_identity'):
  if not isinstance(record[key],str) or not record[key]: raise ValueError('missing identity')
 for key in ('picard64_coordinates','selected64_pairings'):
  v=record[key]
  if not isinstance(v,list) or len(v)!=64 or any(type(x) is not int for x in v): raise ValueError('exact 64-vector required: '+key)
 if not isinstance(record['witness_source_locks'],dict) or not record['witness_source_locks']: raise ValueError('source locks required')
 n=record['m']**2*(Fraction(record['d']**2,16)-record['C2'])
 if n!=record['negative_hperp_square_N']: raise ValueError('C2/N mismatch')
 return True

def replay(record, Psel, gram, expected_source_locks):
 """Validate the common record against independently supplied trusted matrices."""
 from sympy import Matrix
 from picard_pairing_scalar_producer import digest
 validate(record)
 if record['witness_source_locks']!=expected_source_locks: raise ValueError('source-lock mismatch')
 P,G=Matrix(Psel),Matrix(gram)
 if P.shape!=(64,64) or G.shape!=(64,64) or P.det()==0 or G!=G.T: raise ValueError('invalid matrices')
 for field,value in [('selected_pairing_matrix_sha256',Psel),('gram64_sha256',gram),('picard64_coordinates_sha256',record['picard64_coordinates'])]:
  if record.get(field)!=digest(value): raise ValueError('commitment mismatch: '+field)
 c=Matrix(record['picard64_coordinates'])
 if P*c!=Matrix(record['selected64_pairings']): raise ValueError('pairing mismatch')
 if (c.T*G*c)[0]!=record['C2']: raise ValueError('C2 mismatch')
 return True
