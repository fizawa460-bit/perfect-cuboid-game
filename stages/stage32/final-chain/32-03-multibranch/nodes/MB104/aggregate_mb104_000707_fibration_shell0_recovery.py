#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_recovery_singleton as recovery
import verify_mb104_000707_fibration_shell0_recovery_singleton as workverify
import verify_mb104_000707_gen13_shard0_carry as carry

def aggregate_source_locks()->dict:
    sl=json.loads(recovery.RUNKEY.read_text())["source_locks"]
    fields=[
        "local_exact_engine_git_blob","recovery_runner_git_blob","recovery_verifier_git_blob",
        "recovery_aggregate_git_blob","carry_verifier_git_blob","carry_manifest_git_blob",
        "gen15_carry_bundle_git_blob","rehydrate_gen15_carry_git_blob","workflow_git_blob",
        "runner_git_blob","stage33_stoll_helper_blob","stage33_picard_marking_blob",
        "stage33_picard_base_rows_blob","hperp_integral_adapter_blob","pairing_prefix_engine_blob",
    ]
    return {field:sl[field] for field in fields}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",type=Path,required=True)
    ap.add_argument("--carry-certificate",type=Path,required=True)
    ap.add_argument("--carry-manifest",type=Path,required=True)
    ap.add_argument("--gen15-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    manifest=json.loads(a.carry_manifest.read_text())
    gen13,gen15=carry.validate_all(a.carry_certificate,a.carry_manifest,a.gen15_dir)
    k=json.loads(recovery.RUNKEY.read_text())
    expected={(p,r) for p in recovery.PRIMARY_VALUES for r in range(8)}
    observed={}
    for path in sorted(a.input_dir.glob("*.json")):
        try:d=json.loads(path.read_text())
        except Exception:continue
        if d.get("schema")!=recovery.SCHEMA:continue
        p=int(d["partition"]["primary_value"]); r=int(d["partition"]["secondary_residue"])
        assert (p,r) in expected and (p,r) not in observed
        observed[(p,r)]=workverify.validate_certificate(path,p,r)

    missing=sorted(expected-set(observed))
    incomplete=sorted(k2 for k2,d in observed.items() if not d["result"]["complete"])
    sec=recovery.secondary_contract()
    for p in recovery.PRIMARY_VALUES:
        rows=[observed.get((p,r)) for r in range(8)]
        if all(rows):
            assert [d["partition"]["secondary_interval"] for d in rows]==sec["secondary_intervals"]

    candidates=[]; sx=set(); sf=set()
    for d in observed.values():
        for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); candidates.append(rec)
    candidates.sort(key=lambda rec:tuple(rec["picard_basis_coordinates"]))

    assert sorted(gen15)==recovery.GEN15_COMPLETE_VALUES
    assert sorted(recovery.GEN15_COMPLETE_VALUES+recovery.PRIMARY_VALUES)==list(range(-15,21))
    complete=not missing and not incomplete and len(observed)==56

    gen15_inputs=[
        {
            "value":v,
            "certificate_file_sha256":gen15[v]["_rehydrated_certificate_file_sha256"],
            "canonical_sha256":gen15[v]["canonical_sha256_without_this_field"],
        }
        for v in sorted(gen15)
    ]
    residual_inputs={
        f"{p}:{r}":d["canonical_sha256_without_this_field"]
        for (p,r),d in sorted(observed.items())
    }
    total_models=None
    if complete:
        total_models=(
            int(gen13["result"]["integral_known140_nonnegative_solution_count"])
            +sum(int(d["result"]["integral_known140_nonnegative_solution_count"]) for d in gen15.values())
            +sum(int(d["result"]["integral_known140_nonnegative_solution_count"]) for d in observed.values())
        )

    out={
        "schema":"STAGE32_MB104_000707_FIBRATION_SHELL0_SECONDARY_RECOVERY_AGGREGATE_V2",
        "status":"COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" if complete else "PARTIAL_SECONDARY_RECOVERY_NO_CREDIT",
        "complete":complete,
        "provenance":{
            "aggregate_generation":int(k["generation"]),
            "aggregate_mode":k["mode"],
            "gen13_producing_generation":13,
            "gen15_producing_generation":int(manifest["generation15_singleton_carry"]["producing_generation"]),
            "gen15_producing_execution_head":manifest["generation15_singleton_carry"]["producing_execution_head"],
            "gen15_producing_workflow_run_id":manifest["generation15_singleton_carry"]["producing_workflow_run_id"],
        },
        "semantic_source_locks":aggregate_source_locks(),
        "coverage":{
            "gen13_carried_interval":[-20,-16],
            "gen13_canonical":gen13["canonical_sha256_without_this_field"],
            "gen15_complete_values":sorted(gen15),
            "residual_primary_values":recovery.PRIMARY_VALUES,
            "secondary_contract":sec,
            "expected_residual_workunits":56,
            "observed_residual_workunits":len(observed),
            "missing_workunits":[list(x) for x in missing],
            "incomplete_workunits":[list(x) for x in incomplete],
            "full_primary_union":[-20,20],
        },
        "gen15_input_identities":gen15_inputs,
        "residual_input_canonical_sha256":residual_inputs,
        "result":{
            "integral_known140_nonnegative_solution_count":total_models,
            "primitive_candidate_count":len(candidates) if complete else None,
            "primitive_candidates":candidates if complete else [],
        },
        "credit_firewall":{
            "numerical_fibration_shell_credit":False,
            "effectivity_credit":False,
            "semiampleness_credit":False,
            "global_fibration_optimum_credit":False,
            "MB104_complete":False,
            "receiver_credit":False,
            "theorem_credit":False,
            "endpoint_credit":False,
            "merge_authorized":False,
        },
    }
    out["canonical_sha256_without_this_field"]=parent.csha(out)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "complete":complete,
        "observed":len(observed),
        "missing":len(missing),
        "incomplete":len(incomplete),
        "gen15_bound_inputs":len(gen15_inputs),
        "primitive_candidates":out["result"]["primitive_candidate_count"],
        "canonical":out["canonical_sha256_without_this_field"],
    },sort_keys=True))
    raise SystemExit(0 if complete else 2)

if __name__=="__main__": main()
