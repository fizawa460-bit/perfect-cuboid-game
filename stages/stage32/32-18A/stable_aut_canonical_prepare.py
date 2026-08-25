#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

HPERP_MAGIC='S32_D16_AUT_CANON_HPERP_V1'
BUNDLE_MAGIC='S32_D16_AUT_CANONICAL_BUNDLE_V1'
AUT_SCHEMA='STAGE32_AUT_PERM_SOURCELOCK_V1'
EXPECTED_SOURCE_BLOB='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
EXPECTED_STABLE_AUT_SHA='7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3'
EXPECTED_GROUP_ORDER=1536
SEED='stage32-d16-aut-a'
N=63; M=140; BREAKER_COUNT=64

def csha(v:object)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()

def stable_aut_payload(payload:dict)->dict:
    return {k:v for k,v in payload.items() if k not in {'magma_elapsed_seconds','canonical_sha256_without_this_field'}}

def sha_weights(seed:str)->list[int]:
    out=[]
    for i in range(M):
        d=hashlib.sha256(f'{seed}:{i}'.encode()).digest()
        out.append(int.from_bytes(d[:4],'big')%2000003-1000001)
    return out

def compose(p:tuple[int,...],q:tuple[int,...])->tuple[int,...]:
    return tuple(q[p[i]] for i in range(M))

def full_group(gens:list[tuple[int,...]])->list[tuple[int,...]]:
    ident=tuple(range(M)); seen={ident}; frontier=[ident]
    while frontier:
        nxt=[]
        for cur in frontier:
            for gen in gens:
                z=compose(cur,gen)
                if z not in seen: seen.add(z); nxt.append(z)
        frontier=nxt
    if len(seen)!=EXPECTED_GROUP_ORDER: raise RuntimeError(f'Aut closure order mismatch {len(seen)}')
    return sorted(seen)

def perm_hash(p:tuple[int,...])->bytes:
    return hashlib.sha256(SEED.encode()+b';spread;'+bytes(p)).digest()

def load_hperp(path:pathlib.Path):
    with path.open() as f:
        if f.readline().rstrip('\n')!=HPERP_MAGIC: raise RuntimeError('bad Hperp magic')
        _core=f.readline().strip(); source=f.readline().strip(); input_sha=f.readline().strip()
        n,m=map(int,f.readline().split())
        if (n,m)!=(N,M): raise RuntimeError('unexpected Hperp dimensions')
        for _ in range(N):
            if len(f.readline().split())!=N: raise RuntimeError('truncated Gram')
        p0=[]; lin=[]
        for _ in range(M):
            row=list(map(int,f.readline().split()))
            if len(row)!=N+2: raise RuntimeError('truncated pairing row')
            p0.append(row[0]); lin.append(row[2:])
    if source!=EXPECTED_SOURCE_BLOB: raise RuntimeError('Hperp source blob mismatch')
    return input_sha,p0,lin

def load_aut(path:pathlib.Path):
    payload=json.loads(path.read_text())
    if payload.get('schema')!=AUT_SCHEMA: raise RuntimeError('bad Aut schema')
    if payload.get('source',{}).get('git_blob_sha1')!=EXPECTED_SOURCE_BLOB: raise RuntimeError('Aut source blob mismatch')
    stable_sha=csha(stable_aut_payload(payload))
    if stable_sha!=EXPECTED_STABLE_AUT_SHA: raise RuntimeError(f'stable Aut hash mismatch {stable_sha}')
    raw=payload.get('permutations_1based')
    if not isinstance(raw,list) or len(raw)!=9: raise RuntimeError('expected nine generators')
    gens=[]
    for row in raw:
        if sorted(row)!=list(range(1,M+1)): raise RuntimeError('bad permutation')
        p=tuple(int(x)-1 for x in row)
        if any((i<92)!=(p[i]<92) for i in range(M)): raise RuntimeError('Aut mixes cap types')
        gens.append(p)
    return stable_sha,gens,payload.get('canonical_sha256_without_this_field'),payload.get('magma_elapsed_seconds')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',type=pathlib.Path,required=True); ap.add_argument('--aut',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True); ap.add_argument('--summary',type=pathlib.Path,required=True); a=ap.parse_args()
    input_sha,p0,lin=load_hperp(a.input); stable_sha,gens,legacy_sha,elapsed=load_aut(a.aut)
    group=full_group(gens); ident=tuple(range(M)); selected=sorted((p for p in group if p!=ident),key=lambda p:(perm_hash(p),p))[:BREAKER_COUNT]
    weights=sha_weights(SEED); rows=[]
    for p in selected:
        dw=[weights[p[i]]-weights[i] for i in range(M)]
        c0=sum(dw[i]*p0[i] for i in range(M))
        coeff=tuple(sum(dw[i]*lin[i][j] for i in range(M)) for j in range(N))
        if c0==0 and not any(coeff): raise RuntimeError('trivial breaker restriction')
        rows.append((c0,coeff))
    if len(set(rows))!=BREAKER_COUNT: raise RuntimeError('duplicate breaker rows')
    bundle_payload={'input_sha':input_sha,'aut_sha':stable_sha,'seed':SEED,'weights':weights,'breakers':[[c0,list(c)] for c0,c in rows],'group':[list(p) for p in group]}
    bundle_sha=csha(bundle_payload)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('w') as f:
        f.write(BUNDLE_MAGIC+'\n'+input_sha+'\n'+stable_sha+'\n'+bundle_sha+'\n'+SEED+'\n')
        f.write(f'{N} {M} {BREAKER_COUNT} {len(group)}\n'); f.write(' '.join(map(str,weights))+'\n')
        for c0,c in rows: f.write(str(c0)+' '+' '.join(map(str,c))+'\n')
        for p in group: f.write(' '.join(map(str,p))+'\n')
    out={'schema':'STAGE32_18A_STABLE_AUT_PROVENANCE_V1','stable_aut_content_sha256':stable_sha,'expected_stable_aut_content_sha256':EXPECTED_STABLE_AUT_SHA,'legacy_runtime_dependent_canonical_sha256':legacy_sha,'observed_magma_elapsed_seconds':elapsed,'runtime_fields_excluded_from_stable_content_hash':['magma_elapsed_seconds','canonical_sha256_without_this_field'],'stable_hash_matches_hostile_audit_lock':True,'prepared_input_sha256':input_sha,'full_group_order':len(group),'selected_breakers':BREAKER_COUNT,'canonical_bundle_sha256':bundle_sha,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'FULL_D16_G0_ROW_COMPLETE':False}
    a.summary.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
