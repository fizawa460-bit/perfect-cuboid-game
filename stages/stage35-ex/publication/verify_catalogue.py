#!/usr/bin/env python3
"""Verify the owner-index publication, not its underlying mathematics.
Default: frozen publication payload only. --check-live-boundary additionally
checks the unchanged formal state and exact navigation edits for this PR.
All checks use explicit exceptions and remain enabled under Python -O.
"""
from pathlib import Path
from collections import Counter
import argparse,csv,hashlib,json,re,sys
from html import escape

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parent.parent
EXPECTED_COUNTS={'R1':9,'R2':8,'R3':10,'R4':52,'R5':20}

def require(ok,message):
    if not ok:raise ValueError(message)
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def blob(path):
    b=path.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def quoted(value):return '\n'.join('> '+t if t else '>' for t in escape(str(value),quote=False).splitlines())
def expected_ids():
    return {f'{g}-{i:02}' for g,n in [('R1',9),('R2',8),('R3',10)] for i in range(1,n+1)}|{f'R4-ROUTE-{i:02}' for i in range(1,53)}|{f'R5-K{i:02}' for i in range(20)}

def verify(check_live_boundary=False):
    c=read(HERE/'catalogue.json');cfg=read(HERE/'VERIFICATION-CONFIG.json');status=read(HERE/'STATUS.json')
    entries=c['entries'];ids=[r['id'] for r in entries];idset=set(ids)
    require(len(ids)==len(idset)==99,'Expected 99 unique management IDs')
    require(idset==expected_ids(),'Management ID coverage mismatch')
    require(dict(Counter(r['group'] for r in entries))==EXPECTED_COUNTS,'Group counts mismatch')
    require(c['counts']==cfg['expected_counts']==status['index_counts']==EXPECTED_COUNTS,'Published counts disagree')
    require(c['independent_mathematical_route_count']=='NOT_ASSERTED','Do not equate IDs with independent routes')
    require(status['research_status']=='USER_PAUSED_AFTER_R3_ROW393','Research pause missing')
    require(status['authorized_activity']=='PUBLICATION_INVENTORY_AND_MIGRATION_ONLY','Publication-only boundary missing')
    require(status['new_mathematical_research_performed'] is False and status['new_research_rows_added']==0,'New mathematics is outside this import')
    require(status['new_math_credit'] is False and status['formal_state_changed'] is False,'Publication must not promote authority')
    require(status['row393_audit']['verdict']=='PASS_SCOPED_DEPENDENT_20261108_SOURCE_THEOREM_VERIFICATION_PENDING','row393 audit qualifier missing')
    require(status['proof_payload_migration']=='NOT_PERFORMED_BY_THIS_INDEX_IMPORT','Do not imply all proof payloads migrated')
    sources={}
    for g in EXPECTED_COUNTS:
        path=HERE/'sources'/f'{g}.json'
        require(sha(path)==cfg['source_snapshot_sha256'][g],g+' source snapshot hash mismatch')
        x=read(path);require(len(x['rows'])==EXPECTED_COUNTS[g],g+' source count mismatch')
        sources[g]={r['sheet_row']:r['values'] for r in x['rows']}
        require({v[0] for v in sources[g].values()}=={e['id'] for e in entries if e['group']==g},g+' source/entry ID mismatch')
    cards=set()
    for e in entries:
        ident=e['id'];path=HERE/e['card']
        require(e['card']=='routes/'+ident+'.md',ident+' card path mismatch')
        require(path.is_file(),ident+' card missing');cards.add(path.resolve())
        require(e['new_math_credit'] is False,ident+' changed credit')
        require(e['publication_scope']=='OWNER_INDEX_SUMMARY_AND_SOURCE_LINKS',ident+' changed import scope')
        require(e['full_proof_or_certificate_payload_migration']=='NOT_PERFORMED_IN_THIS_IMPORT',ident+' hides unimported materials')
        require(all(a in idset and a!=ident for a in e['canonical_ids']),ident+' invalid redirect')
        v=sources[e['group']][e['source_row']]
        require(v[0]==ident and len(v)==e['source_field_count'],ident+' source row mismatch')
        text=path.read_text(encoding='utf-8')
        require(text.startswith('# '+ident+' — '),ident+' title mismatch')
        require(e['owner_index_url'] in text,ident+' source link missing')
        for value in v[1:]:
            if str(value).strip():require(quoted(value) in text,ident+' source field omitted/changed')
        require('今回の公開での研究再開・新規採用の判定ではありません' in text,ident+' status interpretation missing')
    require(cards=={p.resolve() for p in (HERE/'routes').glob('*.md')},'Unexpected/missing card files')
    with (HERE/'catalogue.csv').open(encoding='utf-8',newline='') as f:csvrows=list(csv.DictReader(f))
    require([r['id'] for r in csvrows]==ids,'CSV ID order/coverage mismatch')
    for row,e in zip(csvrows,entries):
        require(row['card']==e['card'] and row['owner_index_url']==e['owner_index_url'],'CSV source mismatch')
    rpath=HERE/'research-records/R3-330-393.json'
    require(sha(rpath)==cfg['research_records_sha256'],'Research metadata hash mismatch')
    records=read(rpath)['records'];require([r['row'] for r in records]==list(range(330,394)),'R3 research record coverage mismatch')
    require('SOURCE_THEOREM_VERIFICATION_PENDING' in records[-1]['latest_status_field_D'],'Latest source audit qualifier missing')
    for key in ['R3-07','R5-K04']:
        require('SOURCE_THEOREM_VERIFICATION_PENDING' in (HERE/'routes'/f'{key}.md').read_text(),key+' curated audit note missing')
    # Check only authored navigation, not source-quoted historical links.
    link_count=0
    for p in HERE.rglob('*.md'):
        authored='\n'.join(l for l in p.read_text(encoding='utf-8').splitlines() if not l.startswith('>'))
        for dest in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',authored):
            if dest.startswith(('http:','https:','mailto:','#')):continue
            target=(p.parent/dest.split('#',1)[0]).resolve()
            require(target==ROOT.resolve() or ROOT.resolve() in target.parents,'Link escapes repository: '+dest)
            require(target.exists(),'Broken local link '+str(p.relative_to(HERE))+' -> '+dest);link_count+=1
    manifest=read(HERE/'MANIFEST.json')
    listed=manifest['publication_payload_sha256']
    for relative,h in listed.items():require(sha(ROOT/relative)==h,'Payload hash mismatch '+relative)
    found={p.relative_to(ROOT).as_posix() for p in HERE.rglob('*') if p.is_file() and p.name not in ['MANIFEST.json','LOCAL-REPLAY.json'] and '__pycache__' not in p.parts}
    require(set(listed)==found,'Publication manifest coverage mismatch')
    if check_live_boundary:
        for relative,h in manifest['boundary_files_sha256'].items():require(sha(ROOT/relative)==h,'Navigation boundary mismatch '+relative)
        for relative,h in cfg['protected_git_blobs'].items():
            if relative.endswith('MAIN-START-HERE.md'):
                data=(ROOT/relative).read_text();prefix=cfg['startup_banner'];require(data.startswith(prefix),'Startup pause notice missing');b=data[len(prefix):].encode()
                require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==h,'Old startup content changed')
            elif relative.endswith('MAIN-BATCH-HANDOFF.md'):
                data=(ROOT/relative).read_text();prefix=cfg['handoff_banner'];require(data.startswith(prefix),'Handoff pause notice missing');b=data[len(prefix):].encode()
                require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==h,'Old handoff history changed')
            else:require(blob(ROOT/relative)==h,'Protected formal/policy source changed '+relative)
    return {'result':'PASS','management_ids':99,'counts':EXPECTED_COUNTS,'entry_kinds':dict(Counter(e['entry_kind'] for e in entries)),'source_rows_preserved':99,'research_record_metadata_rows':64,'local_navigation_links_checked':link_count,'manifest_payload_files':len(listed),'research_paused_at_row':393,'new_math_credit':False,'full_proof_payload_migration':False,'row393_source_theorem_verification_pending':True,'live_boundary_checked':bool(check_live_boundary)}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--summary',action='store_true');ap.add_argument('--id');ap.add_argument('--check-live-boundary',action='store_true');args=ap.parse_args()
    try:
        out=verify(args.check_live_boundary)
        if args.id:
            c=read(HERE/'catalogue.json');e=next((x for x in c['entries'] if x['id']==args.id),None);require(e is not None,'Unknown ID '+args.id)
            out['selected_entry']={k:e[k] for k in ['id','group','title','entry_kind','canonical_ids','card','owner_index_url','publication_scope']}
        print(json.dumps(out,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
