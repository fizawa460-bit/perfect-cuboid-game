#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, urllib.error, urllib.request, zipfile

API='https://api.github.com'
ORDINARY_RUN=32903188011
RESCUE_RUN=32904153727
REPAIR_RUN=32906177710
PREPARED_ARTIFACT_ID=9583859427
REPAIR_IDS={8,15}
MAGIC=b'S32D16C1'
RECORD_SIZE=141


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request_json(url:str, token:str):
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18k-fetcher'})
    with urllib.request.urlopen(req,timeout=60) as r: return json.load(r)


def request_bytes(url:str, token:str)->bytes:
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18k-fetcher'})
    opener=urllib.request.build_opener(_NoRedirect())
    try:
        with opener.open(req,timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code not in (301,302,303,307,308):
            raise
        location=e.headers.get('Location')
        if not location:
            raise RuntimeError(f'artifact redirect {e.code} missing Location')
    blob_req=urllib.request.Request(location,headers={'User-Agent':'stage32-18k-fetcher'})
    with urllib.request.urlopen(blob_req,timeout=120) as r:
        return r.read()


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


def read_records(raw:bytes):
    if raw[:8]!=MAGIC: raise RuntimeError('bad canonical BIN magic')
    body=raw[8:]
    if len(body)%RECORD_SIZE: raise RuntimeError('truncated canonical BIN')
    return [body[i:i+RECORD_SIZE] for i in range(0,len(body),RECORD_SIZE)]


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

    # Independently deep-rescued secondary5 must reproduce exactly the same
    # canonical RECORD SET. Raw BIN ordering is not semantically significant:
    # the original single traversal emits DFS order, while the 16-way rescue
    # synthesizer emits sorted record order.
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
    ors=read_records(ob); rrs=read_records(rb)
    if len(ors)!=len(set(ors)) or len(rrs)!=len(set(rrs)):
        raise RuntimeError('secondary5 duplicate canonical record in one path')
    if sorted(ors)!=sorted(rrs):
        raise RuntimeError('original secondary5 and nested-rescue secondary5 canonical record SETS differ')
    o=json.loads(orig_json.read_text()); r=json.loads(rescue_json.read_text())
    keys=['bound','aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count','primary_split_coordinate','primary_shard_count','primary_shard_id','secondary_split_coordinate','secondary_shard_count','secondary_shard_id','canonical_survivors_including_zero','canonical_nonzero_survivors','canonical_norm_histogram','TRAVERSAL_COMPLETENESS_CERTIFICATE','all_symmetry_branch_rejections_exact_rational_cauchy_schwarz']
    for k in keys:
        if o.get(k)!=r.get(k): raise RuntimeError(f'secondary5 cross-check metadata mismatch {k}: {o.get(k)} != {r.get(k)}')
    if o.get('status')!='COMPLETE' or r.get('status')!='COMPLETE': raise RuntimeError('secondary5 cross-check non-COMPLETE input')
    if r.get('tertiary_rescue_partition_certificate') is not True: raise RuntimeError('secondary5 rescue partition certificate missing')
    orig_raw_sha=hashlib.sha256(ob).hexdigest(); rescue_raw_sha=hashlib.sha256(rb).hexdigest()
    normalized= MAGIC + b''.join(sorted(ors))
    normalized_sha=hashlib.sha256(normalized).hexdigest()
    if rescue_raw_sha!=r.get('canonical_dump_sha256'):
        raise RuntimeError('secondary5 rescue BIN SHA does not match rescue metadata')

    # Reuse the already-completed exact repair artifacts from the prior 18K run;
    # do not spend Actions time re-enumerating 8 and 15.
    repairs=artifacts(args.repo,REPAIR_RUN,token)
    repair_selected={}
    rpat=re.compile(r'^stage32-18k-b12-repair-secondary-(8|15)-g1$')
    for a in repairs:
        m=rpat.match(str(a.get('name','')))
        if m: repair_selected[int(m.group(1))]=a
    if set(repair_selected)!=REPAIR_IDS:
        raise RuntimeError(f'repair artifact set incomplete: {sorted(repair_selected)}')
    for sid in sorted(repair_selected):
        extract_artifact(repair_selected[sid],args.output/'secondaries',token,inv)

    js=sorted((args.output/'secondaries').glob('d16-b12-exact-secondary-*-of32.json'))
    bs=sorted((args.output/'secondaries').glob('d16-b12-exact-secondary-*-of32.bin'))
    ids=[]
    for p in js:
        d=json.loads(p.read_text()); ids.append(int(d['secondary_shard_id']))
    if len(js)!=32 or len(bs)!=32 or sorted(ids)!=list(range(32)):
        raise RuntimeError(f'logical ids after repair mismatch: json={len(js)} bin={len(bs)} ids={sorted(ids)}')
    original5_artifact=selected[5]
    out={
      'schema':'STAGE32_18K_CROSS_RUN_INPUT_INVENTORY_V2',
      'ordinary_run_id':ORDINARY_RUN,'rescue_run_id':RESCUE_RUN,'repair_source_run_id':REPAIR_RUN,
      'prepared_artifact_id':PREPARED_ARTIFACT_ID,
      'inherited_secondary_ids':sorted(expected),'repair_secondary_ids':sorted(REPAIR_IDS),
      'secondary5_original_artifact_id':original5_artifact['id'],'secondary5_rescue_artifact_id':ra['id'],
      'secondary5_original_vs_nested_rescue_set_identical':True,
      'secondary5_record_order_identical':ob==rb,
      'secondary5_original_raw_dump_sha256':orig_raw_sha,
      'secondary5_rescue_raw_dump_sha256':rescue_raw_sha,
      'secondary5_normalized_record_set_sha256':normalized_sha,
      'secondary5_canonical_survivors_including_zero':o['canonical_survivors_including_zero'],
      'secondary5_canonical_norm_histogram':o['canonical_norm_histogram'],
      'artifact_count':len(inv),'artifacts':inv,
      'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING'
    }
    (args.output/'cross-run-inventory.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'logical_secondary_count':32,'secondary5_set_identical':True,'secondary5_record_order_identical':ob==rb,'secondary5_original_raw_sha256':orig_raw_sha,'secondary5_rescue_raw_sha256':rescue_raw_sha,'secondary5_normalized_record_set_sha256':normalized_sha,'artifact_count':len(inv)},sort_keys=True))

if __name__=='__main__': main()
