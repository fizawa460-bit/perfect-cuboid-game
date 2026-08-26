#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, subprocess, urllib.request, zipfile

EXCLUDED={0,15,63,64,173}
BULK_IDS=[i for i in range(256) if i not in EXCLUDED]
PILOT_IDS=[63,64,173]
HOT_IDS=[26,748]
SNAPSHOT_NAME='stage32-18t-b14-source-snapshot-g1'
RESUME_SUMMARY_NAME='stage32-18t-b14-resume-summary-g1'
PREPARED_NAME='stage32-18p-b14-bulk251-prepared-g1'

def api_json(url:str, token:str):
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18r'})
    with urllib.request.urlopen(req) as r: return json.loads(r.read())

def list_run_artifacts(repo:str,run:int,token:str):
    out=[]; page=1
    while True:
        d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        xs=d.get('artifacts',[]); out.extend(xs)
        if len(xs)<100: break
        page+=1
    table={}
    for a in out:
        table.setdefault(a['name'],[]).append(a)
    return table

def require_unique(table,name):
    xs=table.get(name,[])
    if len(xs)!=1: raise RuntimeError(f'expected exactly one artifact {name}, got {len(xs)}')
    a=xs[0]
    if a.get('expired'): raise RuntimeError(f'expired artifact {name}')
    return a

def artifact_by_id(repo:str,aid:int,token:str):
    a=api_json(f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}',token)
    if a.get('expired'): raise RuntimeError(f'expired artifact id {aid}')
    return a

def download(repo:str,a:dict,token:str,dest:pathlib.Path,zips:pathlib.Path,inventory:list,expected_zip_sha:str|None=None,expected_run:int|None=None):
    aid=int(a['id'])
    if expected_run is not None and int(a.get('workflow_run',{}).get('id',-1))!=expected_run:
        raise RuntimeError(f'artifact {aid} run mismatch')
    z=zips/f'{aid}.zip'; zips.mkdir(parents=True,exist_ok=True); dest.mkdir(parents=True,exist_ok=True)
    subprocess.run(['curl','-L','--fail','--silent','--show-error','-H',f'Authorization: Bearer {token}','-H','X-GitHub-Api-Version: 2022-11-28','-o',str(z),f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}/zip'],check=True)
    got=hashlib.sha256(z.read_bytes()).hexdigest(); digest=a.get('digest')
    if digest and got!=digest.removeprefix('sha256:'): raise RuntimeError(f'artifact ZIP digest mismatch {a["name"]}')
    if expected_zip_sha is not None and got!=expected_zip_sha: raise RuntimeError(f'locked ZIP SHA mismatch {a["name"]}: {got}')
    with zipfile.ZipFile(z) as f: f.extractall(dest)
    inventory.append({'id':aid,'name':a['name'],'zip_sha256':got,'api_digest':digest,'size_in_bytes':a.get('size_in_bytes'),'expired':a.get('expired'),'workflow_run_id':a.get('workflow_run',{}).get('id')})
    return got

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True)
    ap.add_argument('--legacy-run-id',type=int,required=True)
    ap.add_argument('--resume-run-id',type=int,required=True)
    ap.add_argument('--snapshot-artifact-id',type=int,required=True)
    ap.add_argument('--snapshot-artifact-zip-sha256',required=True)
    ap.add_argument('--prepared-artifact-id',type=int,required=True)
    ap.add_argument('--prepared-artifact-zip-sha256',required=True)
    ap.add_argument('--pilot-run-id',type=int,required=True)
    ap.add_argument('--hot-run-id',type=int,required=True)
    ap.add_argument('--b12-artifact-id',type=int,required=True)
    ap.add_argument('--b12-artifact-zip-sha256',required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    a=ap.parse_args(); token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    root=a.output; root.mkdir(parents=True,exist_ok=True); zips=root/'zips'; inventory=[]

    resume_table=list_run_artifacts(a.repo,a.resume_run_id,token)
    pilot_table=list_run_artifacts(a.repo,a.pilot_run_id,token)
    hot_table=list_run_artifacts(a.repo,a.hot_run_id,token)

    snap_art=artifact_by_id(a.repo,a.snapshot_artifact_id,token)
    if snap_art['name']!=SNAPSHOT_NAME: raise RuntimeError('snapshot artifact name mismatch')
    download(a.repo,snap_art,token,root/'control'/'snapshot',zips,inventory,a.snapshot_artifact_zip_sha256,a.resume_run_id)
    summary_art=require_unique(resume_table,RESUME_SUMMARY_NAME)
    download(a.repo,summary_art,token,root/'control'/'resume',zips,inventory,expected_run=a.resume_run_id)

    snap=json.loads((root/'control'/'snapshot'/'source-completion.json').read_text())
    summary=json.loads((root/'control'/'resume'/'resume-summary.json').read_text())
    if snap.get('schema')!='STAGE32_18T_B14_SOURCE_COMPLETION_SNAPSHOT_V1': raise RuntimeError('bad source snapshot schema')
    if summary.get('schema')!='STAGE32_18T_B14_OPTIMIZED_RESUME_SUMMARY_V1': raise RuntimeError('bad resume summary schema')
    if int(snap.get('source_run_id',-1))!=a.legacy_run_id or int(summary.get('source_run_id',-1))!=a.legacy_run_id: raise RuntimeError('legacy source run mismatch')
    source_ids=[int(x) for x in snap['source_complete_ids']]; missing_ids=[int(x) for x in snap['missing_bulk_ids']]
    if len(source_ids)!=41 or len(missing_ids)!=210: raise RuntimeError(f'frozen handoff counts changed: {len(source_ids)} + {len(missing_ids)}')
    if sorted(source_ids+missing_ids)!=BULK_IDS or set(source_ids)&set(missing_ids): raise RuntimeError('frozen handoff is not exact BULK_IDS partition')
    if [int(x) for x in summary.get('source_complete_ids',[])]!=source_ids: raise RuntimeError('summary source set differs from snapshot')
    if [int(x) for x in summary.get('resume_expected_ids',[])]!=missing_ids: raise RuntimeError('summary expected complement differs from snapshot')
    if [int(x) for x in summary.get('resume_complete_ids',[])]!=missing_ids: raise RuntimeError('18T complement is not complete')
    if summary.get('resume_missing_ids')!=[] or summary.get('resume_extra_ids')!=[] or summary.get('ready_for_18r') is not True: raise RuntimeError('18T not ready for 18R')

    prepared=artifact_by_id(a.repo,a.prepared_artifact_id,token)
    if prepared['name']!=PREPARED_NAME: raise RuntimeError('prepared artifact name mismatch')
    download(a.repo,prepared,token,root/'prepared',zips,inventory,a.prepared_artifact_zip_sha256,a.legacy_run_id)

    complete_meta={int(x['packet_id']):x for x in snap.get('complete_artifacts',[])}
    if set(complete_meta)!=set(source_ids): raise RuntimeError('snapshot complete artifact ledger mismatch')
    bulk_sources={}
    for pid in source_ids:
        meta=complete_meta[pid]; art=artifact_by_id(a.repo,int(meta['artifact_id']),token)
        if art['name']!=meta['artifact_name']: raise RuntimeError(f'legacy artifact name mismatch packet {pid}')
        if art.get('digest')!=meta.get('artifact_digest'): raise RuntimeError(f'legacy artifact digest metadata changed packet {pid}')
        download(a.repo,art,token,root/'bulk'/str(pid),zips,inventory,expected_run=a.legacy_run_id)
        bulk_sources[str(pid)]='18P_frozen_snapshot'
    for pid in missing_ids:
        art=require_unique(resume_table,f'stage32-18t-b14-packet-{pid}-g1')
        download(a.repo,art,token,root/'bulk'/str(pid),zips,inventory,expected_run=a.resume_run_id)
        bulk_sources[str(pid)]='18T_resume_complement'

    for pid in PILOT_IDS:
        download(a.repo,require_unique(pilot_table,f'stage32-18o-b14-pilot-packet-{pid}-g1'),token,root/'pilot'/str(pid),zips,inventory,expected_run=a.pilot_run_id)
    for primary in HOT_IDS:
        download(a.repo,require_unique(hot_table,f'stage32-18s-b14-logical-primary-{primary}-of1024-g1'),token,root/'hot'/str(primary),zips,inventory,expected_run=a.hot_run_id)
    b12=artifact_by_id(a.repo,a.b12_artifact_id,token)
    download(a.repo,b12,token,root/'b12',zips,inventory,a.b12_artifact_zip_sha256)

    out={
      'schema':'STAGE32_18R_B14_INPUT_ARTIFACT_INVENTORY_V3','repo':a.repo,
      'legacy_run_id':a.legacy_run_id,'resume_run_id':a.resume_run_id,'snapshot_artifact_id':a.snapshot_artifact_id,
      'resume_summary_artifact_id':int(summary_art['id']),'prepared_artifact_id':a.prepared_artifact_id,
      'pilot_run_id':a.pilot_run_id,'hot_run_id':a.hot_run_id,'hot_source':'Stage32-18S hostile-audited repaired logical parents',
      'b12_artifact_id':a.b12_artifact_id,'legacy_source_complete_ids':source_ids,'resume_packet_ids':missing_ids,
      'bulk_packet_sources':bulk_sources,'artifacts':inventory,
      'handoff_exact':True,'legacy_packet_count':41,'resume_packet_count':210,
      'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING'
    }
    (root/'artifact-inventory.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'legacy_packets':41,'resume_packets':210,'pilot_packets':PILOT_IDS,'hot_primaries':HOT_IDS,'artifact_count':len(inventory),'handoff_exact':True},sort_keys=True))
if __name__=='__main__': main()
