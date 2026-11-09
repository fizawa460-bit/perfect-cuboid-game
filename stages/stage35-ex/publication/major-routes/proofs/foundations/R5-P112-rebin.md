# R5-P112｜Stage35EX 原著研究記録（歴史的テキスト）

> 出典：R5-P112-P113-EXACT-REBINATION-P109-AUDIT-NO-NEW-SUBMIT  
> URL：https://docs.google.com/document/d/1G98BNpe8-rGfe5y0FUoK_KXPCfDm0-VpCqapVo9s5Rg/edit  
> 更新：2026-10-25T14:04:33.358Z  
> 取得：Google Docs paragraph text（改行連結）。原文の数式表示/表レイアウトのバイト同一性は未認証。  
> 原文中の当時のPROVISIONAL・条件付き・誤記は歴史資料として保存する。特にR5-C220の曲線式の誤記はR5-C224とR0-C183の訂正文を優先し、R5-C220単独を正本とみなさない。R5-P112の歴史的マスク残数を2026-11時点のLOW生存数とみなさない。

---

STAGE35EX-E R5 P112/P113 INTERNAL DEPENDENT PROJECTION AND HISTORICAL P109 REPLAY
DATE 2026-10-25 JST
R0 CURRENT C35-189 COMPLETE
NO NEW INDEPENDENT MATHEMATICS, NO R0 SUBMIT, NO PHYSICAL D_i, NO R0/OWNER STATUS UPDATE
PRIMARY OLD R0 C181 https://docs.google.com/document/d/1gBT0cVA2pfJogF928voazcyvzQIh4Fr7NLBr-pPzqe8/edit
PRIMARY OLD R5 C212 https://docs.google.com/document/d/1dQv5-eZwiCWjS27JBAQPVEQGohanIWrZra_d6EyXZs8/edit
OLD S264 as cited by C212.
R0 C189 https://docs.google.com/document/d/10MNKZS2aWJ6rZVi1YxgIliuX9kxIJAPlY3EWwhf5d48/edit
P109 OLD RECORDED SHA VALUES NOT REPRODUCED AS ARTIFACTS: new P113 hashes pertain to standalone replay ONLY.
P112 basis: even n abs ranges [12,154] and [156,196]; C181 all-labelled mask; C212 all-labelled; Aeven C181 support k=j/3 squarefree kernel primes 5 or2/3 mod5 plus OLD S264 n not divisible8. Union LOW36 (12 extra relative old two-mask24), MID12 (2 extra relative old two-mask10); not-covered under three masks LOW36 MID9.
P112 universal out-of-C181/C212 display family j=3*23^(2r+1), signed n=±(j−1),±(j+1), r>=0. This family is not new vs whole history, and no claim about physical survivors.
===== rebin_p112.py START =====
#!/usr/bin/env python3
"""R5 P112 exact bounded index-set audit. No physical-source verifier.
Inputs: R0 C181 Aeven Ward 3*s*t^2 and all-labelled support family;
OLD S264 opposite labelled even 8-nonmultiple; R5 C212 signed family.
All arithmetic standard library, finite range exact.
"""
from itertools import product
from hashlib import sha256
from json import dumps
from pathlib import Path
def factor(n):
    assert n>=1
    out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1; n//=p
        p=3 if p==2 else p+2
    if n>1: out[n]=out.get(n,0)+1
    return out
def kernel(n):
    return set(p for p,k in factor(n).items() if k&1)
def c181_ae(n):
    # C181 R2 Aeven GOOD rank3 support (not by itself all-labelled)
    return any(j>0 and j%3==0 and all(p==5 or p%5 in (2,3) for p in kernel(j//3)) for j in (n-1,n+1))
def c181_all(n):
    # C181 R2 all-labelled stronger p1mod4 support limitation
    return any(j>0 and j%3==0 and all(p==5 or p%20 in (13,17) for p in kernel(j//3)) for j in (n-1,n+1))
def c212_all(n):
    if n%8==0:return False
    for j in (n-1,n+1):
        fs=factor(j)
        if not fs.get(3): continue
        outsiders=[p for p in fs if p not in (3,5,7)]
        if len(outsiders)==1 and outsiders[0]>=11 and outsiders[0]%8 in (3,5):return True
    return False
def c181_ae_s264_all(n):
    return n%8!=0 and c181_ae(n)
def band(a,b):
    ns=list(range(a,b+1,2))
    f1={n for n in ns if c181_all(n)}
    f2={n for n in ns if c212_all(n)}
    f3={n for n in ns if c181_ae_s264_all(n)}
    old=f1|f2
    new=old|f3
    return dict(count=len(ns), c181=sorted(f1),c212=sorted(f2), aeS264=sorted(f3),
                previous_union=sorted(old),new_projection=sorted(new-old),
                new_union=sorted(new),two_mask_not_covered=sorted(set(ns)-old),
                three_mask_not_covered=sorted(set(ns)-new),
                intersections=dict(c181_c212=sorted(f1&f2),old_aeS264=sorted(old&f3)))
v_old=band(12,582)
assert len(v_old['c212'])==61
# Correct regression counts original j<=583 with d>=1 and one extra prime modulo8
js=set()
for n in range(12,583,2):
  if c212_all(n):
    for j in (n-1,n+1):
      fs=factor(j); outsiders=[p for p in fs if p not in (3,5,7)]
      if fs.get(3) and len(outsiders)==1 and outsiders[0]>=11 and outsiders[0]%8 in(3,5):js.add(j)
assert len(js)==45
low=band(12,154);mid=band(156,196)
assert list(map(len,(low['previous_union'],mid['previous_union'],low['new_projection'],mid['new_projection'],low['new_union'],mid['new_union'])))==[24,10,12,2,36,12]
assert low['new_projection']==[20,22,44,46,62,68,70,82,106,140,142,154]
assert mid['new_projection']==[188,190]
# Strong infinite new projection relative to only C181 ALL and C212 families:
for e in [1,3,5]:
 j=3*23**e
 for n in (j-1,j+1):
  assert n%8!=0 and c181_ae_s264_all(n)
  assert not c181_all(n) and not c212_all(n)
result={
    "run_id":"R5-P112-20261025-C181-AEVEN-S264-ALLLABEL-THREE-MASK-REBIN",
    "base_head":"C35-189 COMPLETE",
    "classes":"EXACT_DEPENDENT_OLD_C181_AND_S264_COROLLARY_NOT_NEW_MATH_NOT_ALL_HISTORY",
    "regression":{"old_C212_12_582_index_count":len(v_old['c212']),"old_C212_ward_j_count":len(js)},
    "low":low,"mid":mid,
    "strict_infinite_family":{"j":"3*23**(2r+1), r>=0", "n":"signed ±(j−1), ±(j+1)","uncovered_by_named_C181_C212":True,"genuine_packet":False},
    "new_independent_theorem":False,"new_physical_exclusions":0,"all_history_net_increment":"UNVERIFIED_POSSIBLY_ZERO", "r0_submit":False,
    "signed_and_parity":"original indexed signed± each absolute even, BOTH labelled A-even/B-odd and A-odd/B-even; Bwide outside Iidx unresolved",
}
p=Path(__file__).with_name('evidence_p112.json')
p.write_text(dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(dumps({"replay":"PASS","low_old":len(low['previous_union']),"low_add":len(low['new_projection']),"low_union":len(low['new_union']),"low_remaining_two_or_three":[len(low['two_mask_not_covered']),len(low['three_mask_not_covered'])],"mid_old":len(mid['previous_union']),"mid_add":len(mid['new_projection']),"mid_union":len(mid['new_union']),"mid_remaining_two_or_three":[len(mid['two_mask_not_covered']),len(mid['three_mask_not_covered'])],"code_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),"evidence_sha256":sha256(p.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
===== rebin_p112.py END =====
===== evidence_p112.json START =====
{
  "run_id": "R5-P112-20261025-C181-AEVEN-S264-ALLLABEL-THREE-MASK-REBIN",
  "base_head": "C35-189 COMPLETE",
  "classes": "EXACT_DEPENDENT_OLD_C181_AND_S264_COROLLARY_NOT_NEW_MATH_NOT_ALL_HISTORY",
  "regression": {
    "old_C212_12_582_index_count": 61,
    "old_C212_ward_j_count": 45
  },
  "low": {
    "count": 72,
    "c181": [
      14,
      16,
      26,
      28,
      38,
      40,
      50,
      52,
      74,
      76,
      110,
      112,
      134,
      136,
      146,
      148
    ],
    "c212": [
      34,
      38,
      58,
      86,
      98,
      100,
      110,
      116,
      118,
      130
    ],
    "aeS264": [
      14,
      20,
      22,
      26,
      28,
      38,
      44,
      46,
      50,
      52,
      62,
      68,
      70,
      74,
      76,
      82,
      106,
      110,
      116,
      118,
      130,
      134,
      140,
      142,
      146,
      148,
      154
    ],
    "previous_union": [
      14,
      16,
      26,
      28,
      34,
      38,
      40,
      50,
      52,
      58,
      74,
      76,
      86,
      98,
      100,
      110,
      112,
      116,
      118,
      130,
      134,
      136,
      146,
      148
    ],
    "new_projection": [
      20,
      22,
      44,
      46,
      62,
      68,
      70,
      82,
      106,
      140,
      142,
      154
    ],
    "new_union": [
      14,
      16,
      20,
      22,
      26,
      28,
      34,
      38,
      40,
      44,
      46,
      50,
      52,
      58,
      62,
      68,
      70,
      74,
      76,
      82,
      86,
      98,
      100,
      106,
      110,
      112,
      116,
      118,
      130,
      134,
      136,
      140,
      142,
      146,
      148,
      154
    ],
    "two_mask_not_covered": [
      12,
      18,
      20,
      22,
      24,
      30,
      32,
      36,
      42,
      44,
      46,
      48,
      54,
      56,
      60,
      62,
      64,
      66,
      68,
      70,
      72,
      78,
      80,
      82,
      84,
      88,
      90,
      92,
      94,
      96,
      102,
      104,
      106,
      108,
      114,
      120,
      122,
      124,
      126,
      128,
      132,
      138,
      140,
      142,
      144,
      150,
      152,
      154
    ],
    "three_mask_not_covered": [
      12,
      18,
      24,
      30,
      32,
      36,
      42,
      48,
      54,
      56,
      60,
      64,
      66,
      72,
      78,
      80,
      84,
      88,
      90,
      92,
      94,
      96,
      102,
      104,
      108,
      114,
      120,
      122,
      124,
      126,
      128,
      132,
      138,
      144,
      150,
      152
    ],
    "intersections": {
      "c181_c212": [
        38,
        110
      ],
      "old_aeS264": [
        14,
        26,
        28,
        38,
        50,
        52,
        74,
        76,
        110,
        116,
        118,
        130,
        134,
        146,
        148
      ]
    }
  },
  "mid": {
    "count": 21,
    "c181": [
      158,
      160,
      194,
      196
    ],
    "c212": [
      158,
      164,
      166,
      170,
      172,
      178,
      182,
      194,
      196
    ],
    "aeS264": [
      158,
      188,
      190,
      194,
      196
    ],
    "previous_union": [
      158,
      160,
      164,
      166,
      170,
      172,
      178,
      182,
      194,
      196
    ],
    "new_projection": [
      188,
      190
    ],
    "new_union": [
      158,
      160,
      164,
      166,
      170,
      172,
      178,
      182,
      188,
      190,
      194,
      196
    ],
    "two_mask_not_covered": [
      156,
      162,
      168,
      174,
      176,
      180,
      184,
      186,
      188,
      190,
      192
    ],
    "three_mask_not_covered": [
      156,
      162,
      168,
      174,
      176,
      180,
      184,
      186,
      192
    ],
    "intersections": {
      "c181_c212": [
        158,
        194,
        196
      ],
      "old_aeS264": [
        158,
        194,
        196
      ]
    }
  },
  "strict_infinite_family": {
    "j": "3*23**(2r+1), r>=0",
    "n": "signed ±(j−1), ±(j+1)",
    "uncovered_by_named_C181_C212": true,
    "genuine_packet": false
  },
  "new_independent_theorem": false,
  "new_physical_exclusions": 0,
  "all_history_net_increment": "UNVERIFIED_POSSIBLY_ZERO",
  "r0_submit": false,
  "signed_and_parity": "original indexed signed± each absolute even, BOTH labelled A-even/B-odd and A-odd/B-even; Bwide outside Iidx unresolved"
}
===== evidence_p112.json END =====
===== p109_badprime_replay.py START =====
#!/usr/bin/env python3
"""New independent original C135 J1 bad-prime local-square control.
P109's previously recorded checksum provenance is NOT asserted reproducible here.
Checks primitive Euclid bases and all p dividing the actual 2ABC product.
Finite controls DO NOT prove the universal lemma or a physical full source.
"""
from json import dumps
from math import gcd
from pathlib import Path
from hashlib import sha256
CO=[1,3,9,31,5,135,-115,307,-189,345,155,237,119,-35,15,1]
def factor(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d=3 if d==2 else d+2
 if n>1:out[n]=out.get(n,0)+1
 return out
results=[]
for u,v in [(65,48),(61,48),(89,48),(153,80)]:
 assert gcd(u,v)==1 and u>v and u%2==1 and v%2==0
 A,B,C=2*u*v,u*u-v*v,u*u+v*v
 assert A*A+B*B==C*C and A%8==0
 X,Y=B*B,A*C
 J=sum(c*X**(15-i)*Y**i for i,c in enumerate(CO))
 pB=factor(B)
 assert all(p%4==1 for p in pB)
 prime_set=sorted(set(factor(2*A*B*C)))
 test={str(p): (J%8==1 if p==2 else J%p!=0 and pow(J%p,(p-1)//2,p)==1) for p in prime_set}
 assert all(test.values())
 results.append(dict(u=u,v=v,primitive=True,all_B_prime_1mod4=True,
                     pB={str(p):e for p,e in pB.items()},J1_mod8=J%8,
                     tested_primes=prime_set,all_Qp_unit_square=True))
evidence={"run_id":"R5-P113-20261025-P109-EXACT-BADPRIME-CONTROL-REPLAY",
 "old_p109_sha256_status":"UNVERIFIED_NEVER_REUSE_AS_CURRENT_SCRIPT_PROVENANCE",
 "math_statement":"For p|2ABC and OLD C131 imposed p|B=>p=1mod4, original J1 is a Qp unit square; universal proof algebraic, these are samples.",
 "cases":results,"pass_count":4,"new_independent_method":False,"new_physical_source_exclusions":0,"R0_submission":False}
p=Path(__file__).with_name('evidence_p113.json')
p.write_text(dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(dumps({"replay":"PASS","cases":len(results),"prime_totals":[len(x['tested_primes']) for x in results],"new_script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),"new_evidence_sha256":sha256(p.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
===== p109_badprime_replay.py END =====
===== evidence_p113.json START =====
{
  "run_id": "R5-P113-20261025-P109-EXACT-BADPRIME-CONTROL-REPLAY",
  "old_p109_sha256_status": "UNVERIFIED_NEVER_REUSE_AS_CURRENT_SCRIPT_PROVENANCE",
  "math_statement": "For p|2ABC and OLD C131 imposed p|B=>p=1mod4, original J1 is a Qp unit square; universal proof algebraic, these are samples.",
  "cases": [
    {
      "u": 65,
      "v": 48,
      "primitive": true,
      "all_B_prime_1mod4": true,
      "pB": {
        "17": 1,
        "113": 1
      },
      "J1_mod8": 1,
      "tested_primes": [
        2,
        3,
        5,
        13,
        17,
        113,
        6529
      ],
      "all_Qp_unit_square": true
    },
    {
      "u": 61,
      "v": 48,
      "primitive": true,
      "all_B_prime_1mod4": true,
      "pB": {
        "13": 1,
        "109": 1
      },
      "J1_mod8": 1,
      "tested_primes": [
        2,
        3,
        5,
        13,
        61,
        109,
        241
      ],
      "all_Qp_unit_square": true
    },
    {
      "u": 89,
      "v": 48,
      "primitive": true,
      "all_B_prime_1mod4": true,
      "pB": {
        "41": 1,
        "137": 1
      },
      "J1_mod8": 1,
      "tested_primes": [
        2,
        3,
        5,
        41,
        89,
        137,
        409
      ],
      "all_Qp_unit_square": true
    },
    {
      "u": 153,
      "v": 80,
      "primitive": true,
      "all_B_prime_1mod4": true,
      "pB": {
        "73": 1,
        "233": 1
      },
      "J1_mod8": 1,
      "tested_primes": [
        2,
        3,
        5,
        13,
        17,
        73,
        233,
        2293
      ],
      "all_Qp_unit_square": true
    }
  ],
  "pass_count": 4,
  "new_independent_method": false,
  "new_physical_source_exclusions": 0,
  "R0_submission": false
}
===== evidence_p113.json END =====
