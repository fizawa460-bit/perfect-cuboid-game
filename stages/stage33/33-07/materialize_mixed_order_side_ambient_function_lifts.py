#!/usr/bin/env python3
"""Lift all mixed-order first-residue functions on the 24 physical side conics
from abstract P1 coordinates to explicit rational functions in ambient cuboid
surface coordinates.

For the three side families the frozen parametrizations give

  A1: t=u/v = b2/(c-b3)
  A2: t=u/v = b3/(c-b1)
  A3: t=u/v = b1/(c-b2)

in the function field of the conic.  Thus a P1 factor (b*u-a*v)/v becomes
(b*N-a*D)/D, where t=N/D.  This leaf applies that identity to every nontrivial
side component in all 17 raw-order2 and 9 raw-order4 source packages.

This is a boundary-function ambient lift, not yet a global Gersten/Brauer lift:
off-boundary codimension-one residues and exceptional-divisor ambient lifts are
still firewalled.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST = HERE / "order2-first-residue-function-liftability.json"
ORDER4 = HERE / "order2-quotient-raw-order4-bockstein.json"
EXC = HERE / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "mixed-order-side-ambient-function-lifts.json"
EXPECTED = {
    FIRST.name: "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312",
    ORDER4.name: "085ad52c1eb1cf8069fcac9a0814250428288cc5d517a036670ae529c36eb88a",
    EXC.name: "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636",
}
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
PARAM_POINT = {
    "0": [[0,1,0,1],[1,1,0,1]],
    "infinity": [[1,1,0,1],[0,1,0,1]],
    "1": [[1,1,0,1],[1,1,0,1]],
    "-1": [[-1,1,0,1],[1,1,0,1]],
    "i": [[0,1,1,1],[1,1,0,1]],
    "-i": [[0,1,-1,1],[1,1,0,1]],
}


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def load_locked(path):
    x=json.loads(path.read_text(encoding="utf-8")); claimed=x["canonical_sha256"]
    body=dict(x); body.pop("canonical_sha256")
    actual=canonical_sha256(body)
    if claimed!=EXPECTED[path.name] or actual!=EXPECTED[path.name]:
        raise SystemExit(f"source lock moved for {path.name}: {claimed} {actual}")
    return x


def dec(z):
    return (Fraction(int(z[0]),int(z[1])), Fraction(int(z[2]),int(z[3])))


def enc(z):
    a,b=z
    return [a.numerator,a.denominator,b.numerator,b.denominator]


def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def scale(q,x): return (q*x[0],q*x[1])
ZERO=(Fraction(0),Fraction(0)); ONE=(Fraction(1),Fraction(0))


def linear_basis(term):
    """Return 7 coefficients in Q(i) for a sparse rational linear form."""
    v=[ZERO for _ in COORDS]
    for name,q in term.items(): v[COORDS.index(name)]=scale(Fraction(q),ONE)
    return v


def family_forms(side):
    if 1 <= side <= 8:
        family="A1"; N=linear_basis({"b2":1}); D=linear_basis({"c":1,"b3":-1})
        identity="N=b2=2uv; D=c-b3=2v^2"
    elif 9 <= side <= 16:
        family="A2"; N=linear_basis({"b3":1}); D=linear_basis({"c":1,"b1":-1})
        identity="N=b3=2uv; D=c-b1=2v^2"
    elif 17 <= side <= 24:
        family="A3"; N=linear_basis({"b1":1}); D=linear_basis({"c":1,"b2":-1})
        identity="N=b1=2uv; D=c-b2=2v^2"
    else: raise SystemExit(f"side index out of range {side}")
    return family,N,D,identity


def ambient_factor(point,N,D):
    a,b=map(dec,point)
    return [add(scale(b[0],n), ZERO) if b[1]==0 else None for n in []]  # unreachable sentinel


def mul_gaussian(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c)


def factor_coeffs(point,N,D):
    a,b=map(dec,point)
    return [add(mul_gaussian(b,n), neg(mul_gaussian(a,d))) for n,d in zip(N,D)]


first=load_locked(FIRST); order4=load_locked(ORDER4); exc=load_locked(EXC)

# Rebuild the stable X_#### edge dictionary exactly as the #1414 producer did.
edges=[]
for er in exc["exceptional_models"]:
    e=int(er["exceptional_id"][4:])-1
    for crossing in er["physical_crossing_tangent_coordinates"]:
        edges.append({
            "side":int(crossing["side_index_1based"]),
            "exceptional":24+e,
            "parameter":crossing["side_parameter"],
        })
edges.sort(key=lambda x:(x["side"],x["exceptional"]))
if len(edges)!=144 or len({(x['side'],x['exceptional']) for x in edges})!=144:
    raise SystemExit("stable crossing inventory regression")
edge_by_id={f"X_{i+1:04d}":row for i,row in enumerate(edges)}

source_rows=[]; raw2_count=0; raw4_count=0; side_function_count=0; factor_count=0

# 17 raw-order2 sources: selected edge IDs recover the exact P1 crossing point.
for src in first["source_basis"]:
    if not src["raw_order2_first_residue_function_liftable"]: continue
    raw2_count+=1; packages=[]
    for comp in src["component_first_residue_functions"]:
        if not comp["component_id"].startswith("SIDE_"): continue
        side=int(comp["component_id"].split("_")[1])
        family,N,D,identity=family_forms(side)
        factors=[]
        for edge_id in comp["selected_edge_ids"]:
            row=edge_by_id[edge_id]
            if row["side"]!=side: raise SystemExit(f"edge/component mismatch {edge_id}")
            point=PARAM_POINT[row["parameter"]]
            factors.append({
                "edge_id":edge_id,
                "exponent":1,
                "parameter":row["parameter"],
                "point_P1_L_basis":point,
                "ambient_linear_factor_coefficients_L_basis":[enc(z) for z in factor_coeffs(point,N,D)],
            })
        d=len(factors)
        if d!=int(comp["even_degree"]) or d%2: raise SystemExit("raw2 side degree regression")
        package={
            "component_id":comp["component_id"],"side_index_1based":side,"family":family,
            "ambient_coordinate_order":COORDS,
            "P1_function_field_inverse":f"t=N/D; {identity}",
            "N_coefficients_L_basis":[enc(z) for z in N],
            "D_coefficients_L_basis":[enc(z) for z in D],
            "numerator_factors":factors,
            "denominator":{"ambient_linear_form":"D","exponent":d},
            "restriction_identity":"(b*N-a*D)/D=(b*u-a*v)/v in L(C)",
            "source_boundary_function_model_sha256":comp["function_model_sha256"],
        }
        package["ambient_lift_model_sha256"]=canonical_sha256(package)
        packages.append(package); side_function_count+=1; factor_count+=d
    source_rows.append({"source_basis_name":src["source_basis_name"],"raw_order":2,"side_ambient_function_lifts":packages})

# 9 raw-order4 sources: the full transient Bockstein certificate carries signed exponents.
for src in order4["quotient_to_raw_bockstein"]["nine_source_records"]:
    raw4_count+=1; packages=[]
    for comp in src["component_order4_first_residue_functions"]:
        if not comp["component_id"].startswith("SIDE_"): continue
        side=int(comp["component_id"].split("_")[1])
        family,N,D,identity=family_forms(side)
        factors=[]; d=0
        for factor in comp["selected_crossing_factors"]:
            edge_id=factor["edge_id"]; row=edge_by_id[edge_id]
            if row["side"]!=side: raise SystemExit(f"order4 edge/component mismatch {edge_id}")
            point=factor["point_P1_L_basis"]
            if point!=PARAM_POINT[row["parameter"]]: raise SystemExit(f"order4 P1 point regression {edge_id}")
            exponent=int(factor["z4_divisor_coefficient"])
            if exponent not in (1,2,3): raise SystemExit("unexpected z4 exponent")
            d+=exponent
            factors.append({
                "edge_id":edge_id,"exponent":exponent,"parameter":row["parameter"],
                "point_P1_L_basis":point,
                "ambient_linear_factor_coefficients_L_basis":[enc(z) for z in factor_coeffs(point,N,D)],
            })
        if d!=int(comp["denominator_exponent_d"]) or d%4:
            raise SystemExit(f"order4 side degree regression {src['source_basis_name']} {comp['component_id']} {d}")
        package={
            "component_id":comp["component_id"],"side_index_1based":side,"family":family,
            "ambient_coordinate_order":COORDS,
            "P1_function_field_inverse":f"t=N/D; {identity}",
            "N_coefficients_L_basis":[enc(z) for z in N],
            "D_coefficients_L_basis":[enc(z) for z in D],
            "numerator_factors":factors,
            "denominator":{"ambient_linear_form":"D","exponent":d},
            "restriction_identity":"(b*N-a*D)/D=(b*u-a*v)/v in L(C), with exponents read in Z/4",
            "source_boundary_function_model_sha256":comp["function_model_sha256"],
        }
        package["ambient_lift_model_sha256"]=canonical_sha256(package)
        packages.append(package); side_function_count+=1; factor_count+=len(factors)
    source_rows.append({"source_basis_name":src["source_basis_name"],"raw_order":4,"side_ambient_function_lifts":packages})

source_rows.sort(key=lambda x:int(x["source_basis_name"].split("_")[1]))
if len(source_rows)!=26 or raw2_count!=17 or raw4_count!=9: raise SystemExit("17+9 source partition regression")
if [x["source_basis_name"] for x in source_rows] != [f"A2_{i:02d}" for i in range(1,27)]:
    raise SystemExit("source basis order regression")
if side_function_count==0 or factor_count==0: raise SystemExit("empty side ambient lift atlas")

cert={
    "schema":"STAGE33_07_MIXED_ORDER_SIDE_AMBIENT_FUNCTION_LIFTS_V1",
    "source_locks":{
        "first_residue_liftability_sha256":first["canonical_sha256"],
        "raw_order4_bockstein_full_sha256":order4["canonical_sha256"],
        "exceptional_p1_tangent_coordinates_sha256":exc["canonical_sha256"],
        "testa_stoll_surface_model":"a1^2+a2^2=b3^2; a2^2+a3^2=b1^2; a1^2+a3^2=b2^2; a1^2+a2^2+a3^2=c^2",
    },
    "field":"L=Q(i,sqrt(2)); side inverse forms lie over Q",
    "ambient_coordinate_order":COORDS,
    "mixed_order_partition":{"raw_order2":17,"raw_order4":9},
    "side_inverse_chart":{
        "A1":"t=b2/(c-b3)","A2":"t=b3/(c-b1)","A3":"t=b1/(c-b2)",
        "generic_restriction_check":"N=2uv and D=2v^2, hence (bN-aD)/D=(bu-av)/v",
    },
    "source_ambient_side_lifts":source_rows,
    "counts":{
        "source_count":26,"physical_side_component_count":24,
        "nontrivial_source_side_function_count":side_function_count,
        "selected_side_crossing_factor_count_without_exponent_multiplicity":factor_count,
    },
    "exact_checks":{
        "all_26_sources_processed_in_frozen_order":True,
        "mixed_order_partition_is_17_plus_9":True,
        "stable_144_crossing_edge_dictionary_reconstructed":True,
        "every_selected_side_edge_matches_its_component":True,
        "every_order4_side_point_matches_frozen_crossing_parameter":True,
        "all_raw2_side_denominator_degrees_even":True,
        "all_raw4_side_denominator_degrees_divisible_by_4":True,
        "all_side_P1_factors_have_explicit_ambient_linear_lifts":True,
    },
    "constructive_progress":{
        "all_26_boundary_first_residue_packages_materialized_mixed_order":True,
        "physical_side_component_functions_have_ambient_surface_rational_lifts":True,
        "exceptional_component_functions_have_ambient_blowup_rational_lifts":False,
        "global_geometric_Gersten_lifts_materialized_count":0,
        "global_geometric_Gersten_lifts_required_count":26,
        "project_14x26_L_squareclass_tensor_materialized":False,
        "absolute_delta_loc_computed":False,
        "arithmetic_HS_closed":False,
    },
    "new_smallest_exact_kernel":"R33-BR2A-48-EXCEPTIONAL-AMBIENT-TANGENT-FUNCTION-LIFTS-THEN-26-GLOBAL-GERSTEN",
    "next_exact_leaf":"L33-07-MATERIALIZE-48-EXCEPTIONAL-P1-AMBIENT-TANGENT-RATIONAL-FUNCTION-LIFTS",
    "stage33_progress":"6/11","stage33_08_released":False,
    "theorem_credit":False,"endpoint_credit":False,
    "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,
}
cert["canonical_sha256"]=canonical_sha256(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,"sources":"26/26","raw_order_partition":"17+9",
    "nontrivial_side_function_lifts":side_function_count,
    "selected_side_factors":factor_count,
    "global_Gersten_lifts":"0/26",
    "certificate_sha256":cert["canonical_sha256"],
    "next_exact_leaf":cert["next_exact_leaf"],
},indent=2,sort_keys=True))
