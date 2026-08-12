def gate():
    return {
        'petit_whole_family_route_blocked': True,
        'ar012_route_blocked': True,
        'fixed_cell_pointwise_bound': True,
        'weighted_same_twist_second_moment': False,
    }

if __name__=='__main__':
    print(gate())
