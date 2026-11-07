import json
S=json.load(open('../m2/scan16.json'))
for i,(h,r) in S.items():
    for k,hh in r:
        if hh==1 and h==2:
            print(f'm_{i}_{k}'); raise SystemExit
