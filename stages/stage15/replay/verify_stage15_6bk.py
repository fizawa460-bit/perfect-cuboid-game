from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bk_joint_core_endpoint import endpoint_cells
r=endpoint_cells(1,1,1,1,2,1,3,1)
assert r['E1']==35 and r['E3']==37
assert r['E2']==13 and r['E4']==5
print('Stage15-6bk PASS')
