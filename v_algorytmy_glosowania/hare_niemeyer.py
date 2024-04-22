from math import floor

def hare_niemeyer(vote_list, num_of_mandates):
    sum_of_votes = sum(vote_list)
    
    vote_factors = [votes * num_of_mandates / sum_of_votes for votes in vote_list]

    mandates_for_votes = [floor(mandates) for mandates in vote_factors]
    
    rest_of_vote_factors = [a - b for a, b in zip(vote_factors, mandates_for_votes)]

    num_of_mandates -= sum(mandates_for_votes)
    
    while num_of_mandates:
        max_index = rest_of_vote_factors.index(max(rest_of_vote_factors))
        mandates_for_votes[max_index] += 1
        rest_of_vote_factors[max_index] = 0
        num_of_mandates -= 1
    
    return mandates_for_votes

vote_list = [1228, 1012, 850, 543, 352]
print(hare_niemeyer(vote_list, 7))