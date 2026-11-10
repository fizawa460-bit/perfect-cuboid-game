# M3-T11-187 — Short primitive product-phase leg sector and integer numerator receiver

## Authority / status

Stage37 mainbatch continuation, 2026-10-02 UTC. Current authority read in priority order: MAIN, CARD-INDEX (latest186, next row blank), short RESULT-LEDGER, active ROUTE section17 as needed, newest186; targeted dependency183. No full history reread. This card is the detailed proof authority for187; MAIN and short LEDGER carry only status and pointers. active ROUTE's historical header does not override MAIN CURRENT STATE.

PROVED_SCOPED_SHORT_PHASE_LEG_SECTOR / EXACT_INTEGER_NUMERATOR_RECEIVER. Gate OPEN; GLOBAL_COUNTING_CREDIT=0. TI parked;120 retracted;147–149 frozen. The separate-chat hostile audit remains scoped to162–185;186 and187 have not received independent hostile audit.

## Domain and inherited hypotheses

Use the same primitive positive physical endpoints with intrinsic integer R<=B as183–186. Retain canonical orientation, cyclic/content masks, the134 four-square lift and intrinsic-R condition. No ambient phase label is counted as a physical endpoint without these constraints. R is odd. Write h_i=gcd(e_i,R), H=h_1h_2h_3, tau=R/H; the h_i are pairwise coprime. Signed f_i satisfy e_i²+f_i²=R² and sum e_i²=R². Set w_i=(e_i+i f_i)/R and Z=prod w_i=X+iY. We restrict to corrected finite nonzero common-u, hence X,Y≠0.

184 identifies u=±Y/X. Let Z=(b_phi+i a_phi)/c, where c=c_u>0, gcd(|a_phi|,|b_phi|)=1 and a_phi²+b_phi²=c². Signed swaps are bounded conventions, not new families. Define ell=min(|a_phi|,|b_phi|)>0 and beta=max(|a_phi|,|b_phi|). Since the coordinate denominator of Z divides R³, c<=B³. The183 global fixed-c physical fiber is B^{o(1)}, uniformly over the full content range: no outer content cost C is inserted here.

## 1. Fixed short leg and its summed sector

For a fixed positive integer ell=L, the primitive phase triangle obeys

(c-beta)(c+beta)=L².

Put d=c-beta>0 and t=c+beta>d. Then d t=L², d and t have the same parity, c=(d+t)/2, beta=(t-d)/2. Thus positive divisor pairs of L² determine all possible (beta,c). The restrictions beta>=L and primitivity only discard candidates. There are at most d(L²)=B^{o(1)} such pairs for L<=B³. For every resulting c, the183 global fixed-c fiber contributes B^{o(1)} physical endpoints. Bounded signs and swaps change only constants. Consequently

#E(ell=L) <= B^{o(1)},
#E(ell<=A) <= A B^{o(1)}  (1<=A<=B³).

This sums over every admitted family/content packet; it is not a fixed-content statement. For A=B^(1/3-epsilon), epsilon>0 fixed, it gives a scoped negligible sector on the existing B^(1/3) comparison scale. This is a composition of elementary conic divisor counting with183, not a new global fixed-fiber theorem.

A useful deterministic cap on this sector is

2c=d+L²/d <= L²+1,
so c<=(ell²+1)/2<=(A²+1)/2.

Indeed d is an integer in [1,L], and (d-1)(d-L²)<=0. The sector includes the already controlled small-c sector because ell<=c. It need not force c<=A: primitive conic labels (2m,m²-1,m²+1), m even and m>=4, have ell=2m and c=m²+1. These are examples of labels only; no positive physical endpoint realization is asserted.

Intersecting this sector with186 gives the valid combined bound

#E(ell<=A,c<=Z,q_phase>=D) <= min(A,Z/D) B^{o(1)}.

This takes the minimum of two bounds on the same set. It does not multiply two independent densities or assert that the conic candidates are independently occupied.

## 2. Exact integer numerator / gcd receiver

Define original integer numerators

N_T=e_1 f_1+e_2 f_2+e_3 f_3,
U=e_1e_2e_3-e_1f_2f_3-e_2f_1f_3-e_3f_1f_2,
V=f_1e_2e_3+f_2e_1e_3+f_3e_1e_2-f_1f_2f_3.

Then T=N_T/R², Z=(U+iV)/R³ and U²+V²=R^6. The184 sphere identity TY=2e_1e_2e_3/R³ becomes

N_T V = 2e_1e_2e_3 R².

Use186: Den(S)=D_S² with D_S|R, q_phase=R/D_S, c=tau*q_phase² and H*c*D_S²=R³. Because R is odd, reducing S=2N_T/R² gives the same denominator as T=N_T/R². Hence

gcd(|N_T|,R²)=q_phase².

Let s=N_T/q_phase². It is an integer with gcd(|s|,D_S)=1, and T=s/D_S², S=2s/D_S². Also, if g=gcd(|U|,|V|), then

g=R³/c=H D_S²,
a_phi=V/(H D_S²), b_phi=U/(H D_S²).

For completeness: the primitive integer legs U/g,V/g have integer hypotenuse R³/g. Its integrality follows because its square is an integer and it is rational. Their reduced coordinate denominator is therefore c, so g=R³/c. This identifies g as the actual gcd, not just a known common divisor.

Substitution in N_T V=2e_1e_2e_3 R², using q_phase² D_S²=R², yields

H s a_phi=2e_1e_2e_3,
s a_phi=2 prod_i(e_i/h_i).

Thus s and a_phi have the same sign, since e_i>0. This interface retains the original sphere and content constraints and exposes a coupled multiplicative condition. It does NOT prove a B^{o(1)} fixed-s fiber, a numerator density saving, or a moving occupancy bound. Fixed S, fixed s and fixed Den(S) are distinct. q_phase is not the old q_min or Euclid q.

## 3. Residual and next gate188

After removing ell<=A, both |a_phi| and |b_phi| exceed A and c>sqrt(2) A. The all-content bounds above do not count this residual. In K=1 retain tau=D_min>B^(1/3-delta_D), c=tau*q_phase², four-square/intrinsic R and181 face-space gcd-lcm filters. Do not discard the gcd conditions on N_T and U,V or s*a_phi=2prod(e_i/h_i).

NEXT188: exploit these original integer numerator/gcd constraints jointly with134/181 to prove an actual moving physical occupancy estimate or a useful upper cap on c for the both-phase-legs-large residual. A fixed-leg conic divisor count alone is now recorded in187 and earns no new global credit. Generic independent-density products, fixed-denominator/fixed-S confusion and reopening fresh amplified C_u/interior without withdrawing134 remain forbidden. Large-c threshold tail and K>1 low-median averaging remain separate OPEN tasks.

## 4. Verification and limits

verify_m3_t11_187.py / M3-T11-187-verification.json: PASS. Checked3186 primitive positive phase triangles with c<=20000, across2538 distinct short-leg classes; divisor reconstruction exactly reproduces all3186, and 2c<=ell²+1 holds. Checked9472 nonzero finite-field sphere/face-root assignments over p=41,73,89; U²+V²=1 and N_T V=2e_1e_2e_3 hold at R=1. These finite-field points verify polynomial algebra only, not characteristic-zero positive endpoints. Physical endpoints enumerated=0.

The asymptotic short-leg bound and integer gcd extraction are deductive consequences of183/184/186, not conclusions of finite tests. Within-session review checks the divisor cost is uniform because L<=B³; no outer C; original masks restrict, rather than enlarge, fixed-c fibers; and the conjunction uses min rather than a product. Independent hostile audit NOT RUN. No claim of complete count, balanced-energy improvement or main-gate closure.

## Durable references

MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
Short LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
186: https://drive.google.com/file/d/18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94/view
183: https://docs.google.com/document/d/156OI672uaTABWO1UaogndaieH8kYIUL7LFizZATcqGg/edit
Active ROUTE: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
Audit162–185: https://docs.google.com/document/d/1FmDo8C_NK3RauxLoqh6Z5ZaRD9rtYUGw5RF2cCRa4Q8/edit
SCRIPT_DRIVE_ID: 1XIW6MIHtPB_tEhslywUOSMqEuY9UCFgM
JSON_DRIVE_ID: 1y9C2YjkkQerkc1ynwUo8McWgRZEb8DXL
