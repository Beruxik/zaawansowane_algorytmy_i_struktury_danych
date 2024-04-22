def hondt(vote_list, num_of_mandates):
    mandates_for_votes = [0 for _ in vote_list]
    vote_factors = vote_list.copy()

    while num_of_mandates:
        max_index = vote_factors.index(max(vote_factors))
        mandates_for_votes[max_index] += 1
        vote_factors[max_index] = vote_list[max_index] / (mandates_for_votes[max_index] + 1)
        num_of_mandates -= 1
        
    return mandates_for_votes

vote_list = [1228, 1012, 850, 543, 352]
print(hondt(vote_list, 7))
