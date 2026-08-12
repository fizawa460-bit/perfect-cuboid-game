from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bb_rational_reciprocal import reciprocal_parts
p,m=reciprocal_parts(1,3,2,5,1)
assert p*m==12
print('Stage15-6bb PASS')
