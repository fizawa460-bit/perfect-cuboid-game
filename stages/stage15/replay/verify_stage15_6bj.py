from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bj_equal_hypotenuse_audit import rank_one_from_endpoints,equal_norm_defect
x,y,p,q=3,4,5,12
e1=x*p-y*q; e2=x*q+y*p; e3=x*p+y*q; e4=y*p-x*q
assert equal_norm_defect(e1,e2,e3,e4)==0
assert rank_one_from_endpoints(e1,e2,e3,e4)==0
print('Stage15-6bj PASS')
