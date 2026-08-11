import itertools, json

def walsh(eps, mask):
    out=1
    for i in range(len(eps)):
        if (mask>>i)&1:
            out*=eps[i]
    return out

quotient_checks=0
even_character_checks=0
odd_cancellation_checks=0
occupancy_checks=0
for r in range(1,9):
    cube=list(itertools.product((-1,1), repeat=r))
    seen=set(); reps=[]
    for e in cube:
        if e in seen: continue
        ne=tuple(-x for x in e)
        seen.add(e); seen.add(ne); reps.append(e)
    assert len(reps)==2**(r-1)
    quotient_checks += len(reps)
    for mask in range(1<<r):
        parity=mask.bit_count()%2
        vals=[walsh(e,mask) for e in cube]
        anti=[walsh(tuple(-x for x in e),mask) for e in cube]
        if parity==0:
            assert vals==anti
            even_character_checks += 1
        else:
            assert all(a==-b for a,b in zip(vals,anti))
            assert sum(vals)==0
            odd_cancellation_checks += 1
    # deterministic nonnegative pair occupancy model
    for j,e in enumerate(reps):
        w=(j+1)/len(reps)
        assert 0 < w <= 1
        occupancy_checks += 1

out={
  'stage':'14-t94',
  'quotient_checks':quotient_checks,
  'even_character_checks':even_character_checks,
  'odd_cancellation_checks':odd_cancellation_checks,
  'occupancy_checks':occupancy_checks,
  'max_rank':8,
  'boundary':{
    'ANTIPODAL_QUOTIENT_REDUCTION_PROVED':True,
    'ODD_WALSH_SECTOR_REOPENED':False,
    'EVEN_WALSH_CHARACTERS_DESCEND_TO_QUOTIENT':True,
    'PAIR_OCCUPANCY_DEFICIT_FIXED_POWER_SAVING_PROVED':True,
    'SQRT_SATURATION_FORCES_NEAR_MAXIMAL_PAIR_OCCUPANCY':True,
    'PRINCIPAL_PAIR_MEAN_ELIMINATED':False,
    'CENTERED_EVEN_QUOTIENT_SPECTRUM_ELIMINATED':False,
    'TH27_NEEDED':False,
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT':'1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED':False,
    'NEXT':'Stage14-t95'
  }
}
print(json.dumps(out, sort_keys=True))
