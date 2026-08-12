import sys
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bo_hybrid_gate import balance
t,lo,hi=balance(); assert t==Fraction(1,4) and lo==hi==Fraction(3,4)
print('Stage15-6bo PASS')
