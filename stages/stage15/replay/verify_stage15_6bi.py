from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bi_complementary_products import check_norm_identity
assert check_norm_identity(3,4,5,12)==25*169
print('Stage15-6bi PASS')
