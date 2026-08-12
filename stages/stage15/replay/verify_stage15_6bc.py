from stages.stage15.scripts.stage15_6bc_weighted_twist_gate import gate
f=gate()
assert f['petit_whole_family_route_blocked'] is True
assert f['ar012_route_blocked'] is True
assert f['fixed_cell_pointwise_bound'] is True
assert f['weighted_same_twist_second_moment'] is False
print('Stage15-6bc PASS')
