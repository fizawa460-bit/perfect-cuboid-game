"""32R-69d: Singular base-locus script with the CORRECT component ideals (v2): curves of multiplicity c are
sat(S + I^c) by the 48 node points and the irrelevant ideal; node powers sat(S + m_p^c) by the irrelevant ideal.
Prints h0, residual (base locus outside D's curves), known-curve containment of the residual, and (optional)
the char-p geometric genus via P3 projection."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ST = os.path.dirname(HERE)
_g = {}
_cwd = os.getcwd(); os.chdir(ST); sys.argv = ["x"]
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], _g)
os.chdir(_cwd)
CURVES, POINTS, NOL = _g["CURVES"], _g["POINTS"], _g["node_of_label"]
TESTS = open(os.path.join(ST, "fg12_1215b.sing")).read(); TESTS = TESTS[TESTS.index("int hit = 0;"):]
GENUS = open(os.path.join(ST, "f14", "genus_tail3.sing")).read()   # 32R-69e: 3 projections, smooth image => g = p_a
def script(D, m, genus=False):
    """D: {label: mult} over 1..140"""
    s = 'LIB "primdec.lib"; LIB "elim.lib"; LIB "normal.lib";\nring R = 10009,(a1,a2,a3,b1,b2,b3,c),dp; number z = 792;\n'
    s += "ideal S = a1^2+a2^2-b3^2, a2^2+a3^2-b1^2, a1^2+a3^2-b2^2, a1^2+a2^2+a3^2-c^2;\n"
    s += 'proc satur(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }\n'
    s += 'ideal MX = maxideal(1);\n'
    pts = sorted(set(NOL.values()))
    need_np = any(int(k) <= 92 and c > 1 for k, c in D.items())
    if need_np:
        s += "ideal NP = intersect(" + ",".join(f"std(S + ideal({POINTS[p]}))" for p in pts) + "); NP = std(NP);\n"
    parts, curve_ids = [], []
    for k, c in sorted(D.items()):
        k = int(k)
        if k <= 92:
            s += f"ideal G{k} = satur(std(S + ideal({','.join(CURVES[k-1])})), MX);\n"
            if c == 1: parts.append(f"G{k}")
            else:
                s += f"ideal G{k}p = satur(satur(std(S + G{k}^{c}), NP), MX);\n"; parts.append(f"G{k}p")
            curve_ids.append(k)
        else:
            s += f"ideal N{k} = satur(std(S + ideal({POINTS[NOL[k]]})^{c}), MX);\n"; parts.append(f"N{k}")
    s += "ideal Iall = " + (parts[0] if len(parts) == 1 else "intersect(" + ",".join(parts) + ")") + "; Iall = std(Iall);\n"
    s += f"int mm = {m}; int q; int r; int t;\n"
    s += "ideal Lsys; t = 0;\n"
    s += "for (q = 1; q <= ncols(Iall); q++) { if (Iall[q] != 0) { if (deg(Iall[q]) <= mm) { if (deg(Iall[q]) == mm) { t++; Lsys[t] = Iall[q]; } else { ideal U = maxideal(mm - deg(Iall[q])); for (r = 1; r <= ncols(U); r++) { t++; Lsys[t] = U[r] * Iall[q]; } kill U; } } } }\n"
    s += "ideal SS = std(S); \"H0 (h0):\", size(kbase(SS, mm)) - size(kbase(Iall, mm));\n"
    s += "ideal B = std(S + Lsys);\n\"base locus: dim\", dim(B), \" degree\", mult(B);\n"
    rem = " , ".join(f"G{i}" for i in curve_ids)
    s += f"ideal Dc = {('intersect(' + rem + ')') if len(curve_ids) > 1 else (rem if rem else 'ideal(1)')}; Dc = std(Dc);\n"
    s += 'def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;\n'
    s += "\"base locus outside D's curves: dim\", dim(Bp), \" degree\", mult(Bp);\n"
    s += 'if (dim(Bp) != 2) { "residual not a curve"; quit; }\n'
    s += '"residual: dim", dim(Bp), " hilbPoly", hilbPoly(Bp);\n'
    t = TESTS
    if genus:
        t = t.replace('if (hit == 0) { "no known curve inside"; }\nquit;', 'if (hit == 0) { "no known curve inside";\n' + GENUS.replace("quit;", "") + ' }\nquit;')
    return s + t
