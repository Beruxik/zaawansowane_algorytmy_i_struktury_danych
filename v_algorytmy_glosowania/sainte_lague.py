def sainte_lague(vote_list, num_of_mandates):
    mandates_for_votes = [0 for _ in vote_list]
        
    while num_of_mandates:
        max_index = vote_list.index(max(vote_list))
        mandates_for_votes[max_index] += 1
        vote_list[max_index] /= 2 * mandates_for_votes[max_index] + 1
        num_of_mandates -= 1
    
    return mandates_for_votes

vote_list = [1228, 1012, 850, 543, 352]
print(sainte_lague(vote_list, 7))
