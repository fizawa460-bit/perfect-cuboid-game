#!/usr/bin/env python3
"""Lift all mixed-order first-residue functions on the 48 exceptional curves
from frozen P1 coordinates to explicit ambient tangent/blowup rational functions.

At each ordinary double point the frozen exceptional-coordinate producer builds
an affine tangent basis B=[p|T], the nonsingular tangent-cone Gram matrix G, and
a deterministic projection from the first physical tangent point to P1.  This
leaf reconstructs that model exactly, then chooses a deterministic left inverse
L of B.  If F is the 2x3 matrix of projection forms and Y is the last three rows
of L, then R=F*Y is a pair of ambient linear forms vanishing at the node.  On the
exceptional tangent conic [R0:R1] is exactly the frozen rational P1 projection
(up to the removable base point used by projection-from-a-point).

Thus every boundary factor (b*u-a*v)/v lifts in the blowup function field to
(b*R0-a*R1)/R1.  The common base-point factor cancels between numerator and
denominator with the frozen total divisor degree.

This still is not a global Gersten/Brauer lift: off-boundary codimension-one
residues and global compatibility across all 72 boundary components remain
firewalled.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
FIRST = HERE / "order2-first-residue-function-liftability.json"
ORDER4 = HERE / "order2-quotient-raw-order4-bockstein.json"
EXC = HERE / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "mixed-order-exceptional-ambient-tangent-function-lifts.json"
EXPECTED = {
    FIRST.name: "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312",
    ORDER4.name: "085ad52c1eb1cf8069fcac9a0814250428288cc5d517a036670ae529c36eb88a",
    EXC.name: "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636",
}
I = sp.I
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]
UVS = [(0, 1), (1, 0), (1, 1), (-1, 1), (I, 1), (-I, 1)]
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path):
    x = json.loads(path.read_text(encoding="utf-8"))
    claimed = x["canonical_sha256"]
    body = dict(x); body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if claimed != EXPECTED[path.name] or actual != EXPECTED[path.name]:
        raise SystemExit(f"source lock moved for {path.name}: {claimed} {actual}")
    return x


def clean(x): return sp.cancel(sp.expand(x))
def is_zero(x): return clean(x) == 0


def projective_normalize(v):
    values = [clean(x) for x in list(v)]
    pivot = next((x for x in values if not is_zero(x)), None)
    if pivot is None: raise SystemExit("zero projective vector")
    return tuple(clean(x / pivot) for x in values)


def independent_columns(columns):
    out=[]; rank=0
    for column in columns:
        candidate=sp.Matrix.hstack(*(out+[sp.Matrix(column)]))
        new_rank=candidate.rank()
        if new_rank>rank:
            out.append(sp.Matrix(column)); rank=new_rank
    return out


def perpendicular_candidates(v):
    x,y,z=list(v)
    return [sp.Matrix([y,-x,0]),sp.Matrix([z,0,-x]),sp.Matrix([0,z,-y])]


def rational_pair(q):
    q=clean(q)
    if q.is_Rational is not True: raise SystemExit(f"expected rational coefficient, got {q}")
    return [int(sp.numer(q)),int(sp.denom(q))]


def encode_element(x):
    x=clean(x); xc=clean(sp.conjugate(x))
    a=clean((x+xc)/2); b=clean((x-xc)/(2*I))
    if clean(x-a-b*I)!=0: raise SystemExit(f"element escaped Q(i): {x}")
    ar,br=rational_pair(a),rational_pair(b)
    return [ar[0],ar[1],br[0],br[1]]


def decode_element(z):
    return sp.Rational(int(z[0]),int(z[1])) + I*sp.Rational(int(z[2]),int(z[3]))


def encode_vector(v): return [encode_element(x) for x in list(v)]
def encode_matrix(m): return [[encode_element(m[r,c]) for c in range(m.cols)] for r in range(m.rows)]


def side_metadata(side_index):
    j=side_index-1; family=j//8; r=j%8
    e1=[1,-1][r//4]; e2=[1,-1][(r//2)%2]; e3=[1,-1][r%2]
    return family,e1,e2,e3


def side_param_and_tangent(side_index, parameter_index):
    family,e1,e2,e3=side_metadata(side_index)
    u,v=UVS[parameter_index-1]
    X,Y,Z=u*u-v*v,2*u*v,u*u+v*v
    du,dv=(1,0) if v!=0 else (0,1)
    dX=2*u*du-2*v*dv; dY=2*(du*v+u*dv); dZ=2*u*du+2*v*dv
    if family==0:
        q=[0,-e1*X,-e2*Y,-e3*Z,Y,X,Z]; d=[0,-e1*dX,-e2*dY,-e3*dZ,dY,dX,dZ]
    elif family==1:
        q=[-e2*Y,0,-e1*X,X,-e3*Z,Y,Z]; d=[-e2*dY,0,-e1*dX,dX,-e3*dZ,dY,dZ]
    else:
        q=[-e1*X,-e2*Y,0,Y,X,-e3*Z,Z]; d=[-e1*dX,-e2*dY,0,dY,dX,-e3*dZ,dZ]
    return sp.Matrix([clean(x) for x in q]),sp.Matrix([clean(x) for x in d])


def quadrics(v):
    a1,a2,a3,b1,b2,b3,c=list(v)
    return sp.Matrix([a1*a1+a2*a2-b3*b3,a2*a2+a3*a3-b1*b1,a1*a1+a3*a3-b2*b2,a1*a1+a2*a2+a3*a3-c*c])


def jacobian(v):
    a1,a2,a3,b1,b2,b3,c=list(v)
    return sp.Matrix([
        [2*a1,2*a2,0,0,0,-2*b3,0],
        [0,2*a2,2*a3,-2*b1,0,0,0],
        [2*a1,0,2*a3,0,-2*b2,0,0],
        [2*a1,2*a2,2*a3,0,0,0,-2*c],
    ])


def deterministic_left_inverse(B):
    # Pivot columns of B^T are pivot rows of B.
    rows=list(B.T.rref()[1])
    if len(rows)!=4: raise SystemExit("tangent basis did not expose four pivot rows")
    M=B.extract(rows,range(4))
    if is_zero(M.det()): raise SystemExit("pivot-row tangent minor singular")
    Minv=M.inv(); L=sp.zeros(4,7)
    for j,row in enumerate(rows):
        for i in range(4): L[i,row]=clean(Minv[i,j])
    if L*B != sp.eye(4): raise SystemExit("deterministic tangent left inverse failed")
    return L,rows


def same_projective_pair(encoded, pair):
    frozen=sp.Matrix([decode_element(x) for x in encoded])
    return projective_normalize(frozen)==projective_normalize(pair)


first=load_locked(FIRST); order4=load_locked(ORDER4); exc=load_locked(EXC)

# Reconstruct every exceptional tangent model and ambient projection pair R0,R1.
ambient_models={}; edge_rows=[]
for er in exc["exceptional_models"]:
    eid=er["exceptional_id"]; eidx=int(eid[4:])
    p=sp.Matrix([decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
    if any(not is_zero(x) for x in quadrics(p)): raise SystemExit(f"node escaped surface {eid}")
    J=jacobian(p)
    if J.rank()!=3: raise SystemExit(f"node Jacobian rank regression {eid}")
    W=J.nullspace(); Bcols=independent_columns([p]+W)
    if len(Bcols)!=4 or Bcols[0]!=p: raise SystemExit(f"tangent basis regression {eid}")
    B=sp.Matrix.hstack(*Bcols)
    alpha_space=J.T.nullspace()
    if len(alpha_space)!=1: raise SystemExit(f"quadratic relation regression {eid}")
    alpha=alpha_space[0]
    def qeval(v): return clean((alpha.T*quadrics(v))[0])
    U=B[:,1:4]; G=sp.zeros(3,3)
    for r in range(3):
        for c in range(3):
            G[r,c]=clean((qeval(U[:,r]+U[:,c])-qeval(U[:,r])-qeval(U[:,c]))/2)
    if G!=G.T or is_zero(G.det()): raise SystemExit(f"tangent conic degenerate {eid}")

    tangent_rows=[]; ys=[]
    for cr in er["physical_crossing_tangent_coordinates"]:
        side=int(cr["side_index_1based"]); z=int(cr["side_parameter_index_1based"])
        q,d=side_param_and_tangent(side,z)
        if projective_normalize(q)!=projective_normalize(p): raise SystemExit(f"node/side incidence moved {eid} side={side}")
        solution,parameters=B.gauss_jordan_solve(d)
        if parameters.rows or B*solution!=d: raise SystemExit(f"tangent solve failed {eid}")
        y=solution[1:4,0]
        if y==sp.zeros(3,1) or not is_zero((y.T*G*y)[0]): raise SystemExit(f"side tangent missed conic {eid}")
        ys.append(y); tangent_rows.append((cr,d,y))
    p0=ys[0]
    forms=independent_columns([v for v in perpendicular_candidates(p0) if v!=sp.zeros(3,1)])
    if len(forms)!=2 or any(not is_zero(f.dot(p0)) for f in forms): raise SystemExit(f"projection forms failed {eid}")
    grad=G*p0
    tangent_kernel=independent_columns([v for v in perpendicular_candidates(grad) if v!=sp.zeros(3,1)])
    w=next((v for v in tangent_kernel if sp.Matrix.hstack(p0,v).rank()==2),None)
    if w is None or not is_zero(grad.dot(w)): raise SystemExit(f"projection base tangent failed {eid}")

    full_crossings=[]
    for k,(cr,d,y) in enumerate(tangent_rows):
        source=w if k==0 else y
        pair=sp.Matrix([clean(forms[0].dot(source)),clean(forms[1].dot(source))])
        if pair==sp.zeros(2,1): raise SystemExit(f"zero frozen P1 coordinate reconstruction {eid}")
        pair=sp.Matrix(projective_normalize(pair))
        if not same_projective_pair(cr["exceptional_P1_homogeneous_coordinate_L_basis"],pair):
            raise SystemExit(f"frozen exceptional P1 coordinate moved {eid} side={cr['side_index_1based']}")
        full_crossings.append({
            "side_index_1based":int(cr["side_index_1based"]),
            "side_parameter":cr["side_parameter"],
            "side_parameter_index_1based":int(cr["side_parameter_index_1based"]),
            "ambient_tangent_vector_L_basis":encode_vector(d),
            "exceptional_conic_point_L_basis":encode_vector(y),
            "exceptional_P1_homogeneous_coordinate_L_basis":encode_vector(pair),
        })
        edge_rows.append({
            "side":int(cr["side_index_1based"]),"exceptional":24+(eidx-1),
            "exceptional_id":eid,
            "point":cr["exceptional_P1_homogeneous_coordinate_L_basis"],
        })
    commitment={
        "node":encode_vector(p),
        "affine_tangent_basis_radial_first":encode_matrix(B),
        "exceptional_conic_gram":encode_matrix(G),
        "projection_forms":encode_matrix(sp.Matrix.hstack(*forms).T),
        "projection_base_tangent":encode_vector(w),
        "full_crossings":sorted(full_crossings,key=lambda x:(x["side_index_1based"],x["side_parameter_index_1based"])),
    }
    if canonical_sha256(commitment)!=er["full_tangent_conic_coordinate_model_sha256"]:
        raise SystemExit(f"full frozen tangent model commitment moved {eid}")

    L,pivot_rows=deterministic_left_inverse(B); Y=L[1:4,:]
    F=sp.Matrix.hstack(*forms).T; R=(F*Y).applyfunc(clean)
    if R.shape!=(2,7) or R*p!=sp.zeros(2,1): raise SystemExit(f"ambient exceptional projection forms do not vanish at node {eid}")
    # Away from the projection base point, R*d must equal the frozen P1 pair.
    for k,(cr,d,y) in enumerate(tangent_rows):
        if k==0:
            if R*d!=sp.zeros(2,1): raise SystemExit(f"projection base point should be common zero {eid}")
        elif not same_projective_pair(cr["exceptional_P1_homogeneous_coordinate_L_basis"],R*d):
            raise SystemExit(f"ambient projection ratio mismatch {eid} side={cr['side_index_1based']}")
    ambient_models[eid]={
        "exceptional_id":eid,
        "node_point_ambient_P6_L_basis":encode_vector(p),
        "tangent_basis_left_inverse_pivot_rows_0based":pivot_rows,
        "ambient_projection_R0_R1_coefficients_L_basis":encode_matrix(R),
        "projection_base_crossing":{
            "side_index_1based":int(tangent_rows[0][0]["side_index_1based"]),
            "side_parameter":tangent_rows[0][0]["side_parameter"],
            "removable_common_base_factor":True,
        },
        "frozen_tangent_model_sha256":er["full_tangent_conic_coordinate_model_sha256"],
    }

edge_rows.sort(key=lambda x:(x["side"],x["exceptional"]))
if len(edge_rows)!=144 or len({(x["side"],x["exceptional"]) for x in edge_rows})!=144:
    raise SystemExit("stable 144 crossing inventory regression")
edge_by_id={f"X_{i+1:04d}":row for i,row in enumerate(edge_rows)}


def factor_coeffs(point,R):
    a,b=[decode_element(x) for x in point]
    return [clean(b*R[0,j]-a*R[1,j]) for j in range(7)]

source_rows=[]; raw2=0; raw4=0; function_count=0; selected_factor_count=0
for src in first["source_basis"]:
    if not src["raw_order2_first_residue_function_liftable"]: continue
    raw2+=1; packages=[]
    for comp in src["component_first_residue_functions"]:
        if not comp["component_id"].startswith("EXC_"): continue
        eid=comp["component_id"]; model=ambient_models[eid]
        R=sp.Matrix([[decode_element(z) for z in row] for row in model["ambient_projection_R0_R1_coefficients_L_basis"]])
        factors=[]
        for edge_id in comp["selected_edge_ids"]:
            row=edge_by_id[edge_id]
            if row["exceptional_id"]!=eid: raise SystemExit(f"raw2 exceptional edge mismatch {edge_id}")
            point=row["point"]
            factors.append({
                "edge_id":edge_id,"exponent":1,"point_P1_L_basis":point,
                "ambient_tangent_linear_factor_coefficients_L_basis":encode_vector(factor_coeffs(point,R)),
            })
        d=len(factors)
        if d!=int(comp["even_degree"]) or d%2: raise SystemExit(f"raw2 exceptional degree regression {eid}")
        package={
            "component_id":eid,"ambient_coordinate_order":COORDS,
            "ambient_projection_R0_R1_coefficients_L_basis":model["ambient_projection_R0_R1_coefficients_L_basis"],
            "numerator_factors":factors,"denominator":{"ambient_linear_form":"R1","exponent":d},
            "restriction_identity":"after removing the common projection-base factor, (b*R0-a*R1)/R1=(b*u-a*v)/v in L(E)",
            "source_boundary_function_model_sha256":comp["function_model_sha256"],
            "frozen_tangent_model_sha256":model["frozen_tangent_model_sha256"],
        }
        package["ambient_tangent_lift_model_sha256"]=canonical_sha256(package)
        packages.append(package); function_count+=1; selected_factor_count+=d
    source_rows.append({"source_basis_name":src["source_basis_name"],"raw_order":2,"exceptional_ambient_tangent_function_lifts":packages})

for src in order4["quotient_to_raw_bockstein"]["nine_source_records"]:
    raw4+=1; packages=[]
    for comp in src["component_order4_first_residue_functions"]:
        if not comp["component_id"].startswith("EXC_"): continue
        eid=comp["component_id"]; model=ambient_models[eid]
        R=sp.Matrix([[decode_element(z) for z in row] for row in model["ambient_projection_R0_R1_coefficients_L_basis"]])
        factors=[]; d=0
        for factor in comp["selected_crossing_factors"]:
            edge_id=factor["edge_id"]; row=edge_by_id[edge_id]
            if row["exceptional_id"]!=eid: raise SystemExit(f"order4 exceptional edge mismatch {edge_id}")
            point=factor["point_P1_L_basis"]
            if not same_projective_pair(row["point"],sp.Matrix([decode_element(x) for x in point])):
                raise SystemExit(f"order4 exceptional P1 point regression {edge_id}")
            exponent=int(factor["z4_divisor_coefficient"])
            if exponent not in (1,2,3): raise SystemExit("unexpected z4 exponent")
            d+=exponent
            factors.append({
                "edge_id":edge_id,"exponent":exponent,"point_P1_L_basis":point,
                "ambient_tangent_linear_factor_coefficients_L_basis":encode_vector(factor_coeffs(point,R)),
            })
        if d!=int(comp["denominator_exponent_d"]) or d%4:
            raise SystemExit(f"order4 exceptional degree regression {src['source_basis_name']} {eid} {d}")
        package={
            "component_id":eid,"ambient_coordinate_order":COORDS,
            "ambient_projection_R0_R1_coefficients_L_basis":model["ambient_projection_R0_R1_coefficients_L_basis"],
            "numerator_factors":factors,"denominator":{"ambient_linear_form":"R1","exponent":d},
            "restriction_identity":"after removing the common projection-base factor, (b*R0-a*R1)/R1=(b*u-a*v)/v in L(E), exponents in Z/4",
            "source_boundary_function_model_sha256":comp["function_model_sha256"],
            "frozen_tangent_model_sha256":model["frozen_tangent_model_sha256"],
        }
        package["ambient_tangent_lift_model_sha256"]=canonical_sha256(package)
        packages.append(package); function_count+=1; selected_factor_count+=len(factors)
    source_rows.append({"source_basis_name":src["source_basis_name"],"raw_order":4,"exceptional_ambient_tangent_function_lifts":packages})

source_rows.sort(key=lambda x:int(x["source_basis_name"].split("_")[1]))
if len(source_rows)!=26 or raw2!=17 or raw4!=9: raise SystemExit("17+9 source partition regression")
if [x["source_basis_name"] for x in source_rows] != [f"A2_{i:02d}" for i in range(1,27)]: raise SystemExit("source basis order regression")
if len(ambient_models)!=48 or function_count==0: raise SystemExit("exceptional ambient tangent atlas incomplete")

cert={
    "schema":"STAGE33_07_MIXED_ORDER_EXCEPTIONAL_AMBIENT_TANGENT_FUNCTION_LIFTS_V1",
    "source_locks":{
        "first_residue_liftability_sha256":first["canonical_sha256"],
        "raw_order4_bockstein_full_sha256":order4["canonical_sha256"],
        "exceptional_p1_tangent_coordinates_sha256":exc["canonical_sha256"],
    },
    "field":"L=Q(i,sqrt(2)); reconstructed tangent data lie in Q(i)",
    "ambient_coordinate_order":COORDS,
    "mixed_order_partition":{"raw_order2":17,"raw_order4":9},
    "exceptional_ambient_projection_models":[ambient_models[f"EXC_{i:03d}"] for i in range(1,49)],
    "source_ambient_exceptional_lifts":source_rows,
    "counts":{
        "source_count":26,"exceptional_component_count":48,
        "nontrivial_source_exceptional_function_count":function_count,
        "selected_exceptional_crossing_factor_count_without_exponent_multiplicity":selected_factor_count,
    },
    "exact_checks":{
        "all_48_frozen_tangent_model_commitments_reproduced":True,
        "all_48_deterministic_ambient_projection_pairs_vanish_at_their_nodes":True,
        "all_nonbase_physical_tangent_projection_ratios_match_frozen_P1_coordinates":True,
        "projection_base_point_is_recorded_as_removable_common_factor":True,
        "stable_144_crossing_edge_dictionary_reconstructed":True,
        "all_26_sources_processed_in_frozen_order":True,
        "mixed_order_partition_is_17_plus_9":True,
        "all_raw2_exceptional_denominator_degrees_even":True,
        "all_raw4_exceptional_denominator_degrees_divisible_by_4":True,
        "all_exceptional_P1_factors_have_explicit_ambient_tangent_linear_lifts":True,
    },
    "constructive_progress":{
        "all_26_boundary_first_residue_packages_materialized_mixed_order":True,
        "physical_side_component_functions_have_ambient_surface_rational_lifts":True,
        "exceptional_component_functions_have_ambient_blowup_rational_lifts":True,
        "all_72_boundary_component_function_packages_have_explicit_ambient_or_blowup_rational_lifts":True,
        "global_geometric_Gersten_lifts_materialized_count":0,
        "global_geometric_Gersten_lifts_required_count":26,
        "off_boundary_codimension1_residue_certificates_materialized_count":0,
        "project_14x26_L_squareclass_tensor_materialized":False,
        "absolute_delta_loc_computed":False,"arithmetic_HS_closed":False,
    },
    "new_smallest_exact_kernel":"R33-BR2A-26-AMBIENT-BOUNDARY-FUNCTION-PACKAGES-GLOBAL-GERSTEN-OFF-BOUNDARY-RESIDUES",
    "next_exact_leaf":"L33-07-ASSEMBLE-26-AMBIENT-BOUNDARY-PACKAGES-AND-CERTIFY-OFF-BOUNDARY-CODIM1-RESIDUES",
    "stage33_progress":"6/11","stage33_08_released":False,
    "theorem_credit":False,"endpoint_credit":False,
    "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,
}
cert["canonical_sha256"]=canonical_sha256(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,"sources":"26/26","exceptional_models":"48/48",
    "nontrivial_exceptional_function_lifts":function_count,
    "selected_exceptional_factors":selected_factor_count,
    "all_72_boundary_component_packages_have_ambient_or_blowup_lifts":True,
    "global_Gersten_lifts":"0/26","certificate_sha256":cert["canonical_sha256"],
    "next_exact_leaf":cert["next_exact_leaf"],
},indent=2,sort_keys=True))
