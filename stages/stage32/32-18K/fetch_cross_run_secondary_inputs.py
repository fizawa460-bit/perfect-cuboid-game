#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, urllib.request, zipfile

API='https://api.github.com'
ORDINARY_RUN=32903188011
RESCUE_RUN=32904153727
PREPARED_ARTIFACT_ID=9583859427
REPAIR_IDS={8,15}


def request_json(url:str, token:str):
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18k-fetcher'})
    with urllib.request.urlopen(req,timeout=60) as r: return json.load(r)


def request_bytes(url:str, token:str)->bytes:
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18k-fetcher'})
    with urllib.request.urlopen(req,timeout=120) as r: return r.read()


def artifacts(repo:str,run:int,token:str):
    out=[]; page=1
    while True:
        p=request_json(f'{API}/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        batch=p.get('artifacts',[]); out.extend(batch)
        if len(batch)<100: break
        page+=1
    return out


def extract_artifact(a:dict,dst:pathlib.Path,token:str,inventory:list):
    if a.get('expired'): raise RuntimeError(f"expired artifact {a['name']}")
    raw=request_bytes(a['archive_download_url'],token)
    got=hashlib.sha256(raw).hexdigest(); declared=a.get('digest')
    if declared and got!=declared.removeprefix('sha256:'):
        raise RuntimeError(f"artifact digest mismatch {a['name']}: {got} != {declared}")
    zpath=dst.parent/f"artifact-{a['id']}.zip"; zpath.parent.mkdir(parents=True,exist_ok=True); zpath.write_bytes(raw)
    tmp=dst.parent/f"extract-{a['id']}"; tmp.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(zpath) as z: z.extractall(tmp)
    dst.mkdir(parents=True,exist_ok=True)
    for p in tmp.iterdir():
        if p.is_file():
            q=dst/p.name
            if q.exists(): raise RuntimeError(f'filename collision {q}')
            p.replace(q)
    inventory.append({'id':a['id'],'name':a['name'],'zip_sha256':got,'declared_digest':declared,'size_in_bytes':a.get('size_in_bytes')})


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True); ap.add_argument('--output',type=pathlib.Path,required=True); args=ap.parse_args()
    token=os.environ.get('GH_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    args.output.mkdir(parents=True,exist_ok=True); inv=[]

    ordinary=artifacts(args.repo,ORDINARY_RUN,token)
    pa=next((a for a in ordinary if int(a['id'])==PREPARED_ARTIFACT_ID),None)
    if pa is None or pa.get('name')!='stage32-18i-two-stage-prepared-g1': raise RuntimeError('immutable 18I prepared artifact missing')
    extract_artifact(pa,args.output/'prepared',token,inv)
    pzip=inv[-1]['zip_sha256']
    if pzip!='7644f66b977419549a75aeee8c230a9a97330b712bbb35dd801ad4412e21a6ef': raise RuntimeError(f'prepared ZIP lock mismatch {pzip}')

    pat=re.compile(r'^stage32-18i-b12-secondary-(\d+)-of32-g1$')
    selected={}
    for a in ordinary:
        m=pat.match(str(a.get('name','')))
        if m:
            sid=int(m.group(1))
            if sid not in REPAIR_IDS: selected[sid]=a
    expected=set(range(32))-REPAIR_IDS
    if set(selected)!=expected:
        raise RuntimeError(f'ordinary secondary artifact set incomplete: missing={sorted(expected-set(selected))}, extra={sorted(set(selected)-expected)}')
    for sid in sorted(selected): extract_artifact(selected[sid],args.output/'secondaries',token,inv)

    # Stage32-18J was launched before the original slow secondary5 finished.  The
    # original subsequently completed, so use it as the logical parent input and
    # require the nested-rescue construction to reproduce its canonical BIN
    # byte-for-byte as a strong independent cross-check.
    rescue=artifacts(args.repo,RESCUE_RUN,token)
    ra=next((x for x in rescue if x.get('name')=='stage32-18j-b12-logical-secondary5-g1'),None)
    if ra is None: raise RuntimeError('Stage32-18J logical secondary5 artifact not available')
    cross=args.output/'secondary5-crosscheck'
    extract_artifact(ra,cross/'rescue',token,inv)
    orig_json=args.output/'secondaries'/'d16-b12-exact-secondary-5-of32.json'
    orig_bin=args.output/'secondaries'/'d16-b12-exact-secondary-5-of32.bin'
    rescue_json=cross/'rescue'/'d16-b12-exact-secondary-5-of32.json'
    rescue_bin=cross/'rescue'/'d16-b12-exact-secondary-5-of32.bin'
    if not all(p.exists() for p in [orig_json,orig_bin,rescue_json,rescue_bin]):
        raise RuntimeError('secondary5 cross-check files missing')
    ob=orig_bin.read_bytes(); rb=rescue_bin.read_bytes()
    if ob!=rb: raise RuntimeError('original secondary5 and nested-rescue secondary5 canonical BIN differ')
    o=json.loads(orig_json.read_text()); r=json.loads(rescue_json.read_text())
    keys=['bound','aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count','primary_split_coordinate','primary_shard_count','primary_shard_id','secondary_split_coordinate','secondary_shard_count','secondary_shard_id','canonical_survivors_including_zero','canonical_nonzero_survivors','canonical_norm_histogram','canonical_dump_sha256']
    for k in keys:
        if o.get(k)!=r.get(k): raise RuntimeError(f'secondary5 cross-check metadata mismatch {k}: {o.get(k)} != {r.get(k)}')
    if o.get('status')!='COMPLETE' or r.get('status')!='COMPLETE': raise RuntimeError('secondary5 cross-check non-COMPLETE input')
    if r.get('tertiary_rescue_partition_certificate') is not True: raise RuntimeError('secondary5 rescue partition certificate missing')
    bin_sha=hashlib.sha256(ob).hexdigest()
    if bin_sha!=o.get('canonical_dump_sha256'): raise RuntimeError('secondary5 BIN SHA does not match logical metadata')

    js=sorted((args.output/'secondaries').glob('d16-b12-exact-secondary-*-of32.json'))
    ids=[]
    for p in js:
        d=json.loads(p.read_text()); ids.append(int(d['secondary_shard_id']))
    if set(ids)!=(set(range(32))-REPAIR_IDS): raise RuntimeError(f'logical ids before repair mismatch: {sorted(ids)}')
    original5_artifact=selected[5]
    out={
      'schema':'STAGE32_18K_CROSS_RUN_INPUT_INVENTORY_V1',
      'ordinary_run_id':ORDINARY_RUN,'rescue_run_id':RESCUE_RUN,'prepared_artifact_id':PREPARED_ARTIFACT_ID,
      'inherited_secondary_ids':sorted(expected),'repair_secondary_ids':sorted(REPAIR_IDS),
      'secondary5_original_artifact_id':original5_artifact['id'],'secondary5_rescue_artifact_id':ra['id'],
      'secondary5_original_vs_nested_rescue_byte_identical':True,
      'secondary5_canonical_dump_sha256':bin_sha,
      'secondary5_canonical_survivors_including_zero':o['canonical_survivors_including_zero'],
      'secondary5_canonical_norm_histogram':o['canonical_norm_histogram'],
      'artifact_count':len(inv),'artifacts':inv,
      'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING'
    }
    (args.output/'cross-run-inventory.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'inherited_count':len(expected),'logical_ids_before_repair':sorted(ids),'secondary5_byte_identical':True,'secondary5_dump_sha256':bin_sha,'artifact_count':len(inv)},sort_keys=True))

if __name__=='__main__': main()
