from __future__ import division

def list_of_all_games_outcomes(n):
    if n == 0:
        return []
    elif n == 1:
        return ['L', 'W']
    else:
        ret = []
        n_minus_one_list_outcomes = list_of_all_games_outcomes(n-1)
        for outcome in n_minus_one_list_outcomes:
            ret.append('L' + outcome)
            ret.append('W' + outcome)
        return ret


def non_LL_outcomes_given_x_Ws_and_y_Ls(x, y, n):
    list_of_outcomes = list_of_all_games_outcomes(n)
    returned_sublist = []
    for outcome in list_of_outcomes:
        count_W = 0
        count_L = 0
        for letter in outcome:
            if letter == 'L':
                count_L += 1
            else:
                count_W += 1
        if count_W == x and count_L == y and "LL" not in outcome:
            returned_sublist.append(outcome)
    return returned_sublist
    

def probability_of_two_consecutive_losses_in_n_games(n):
    list_of_outcomes = list_of_all_games_outcomes(n)
    list_of_outcomes_with_two_consecutive_losses = []
    
    for outcome in list_of_outcomes:
        if 'LL' in outcome:
            list_of_outcomes_with_two_consecutive_losses.append(outcome)
    
    # Now calculate the probability
    total_probability = 0.0
    outcome_probability = 1.0
    for outcome in list_of_outcomes_with_two_consecutive_losses:
        for letter in outcome:
            if letter == 'L':
                outcome_probability *= 0.2
            else:
                outcome_probability *= 0.8
            
        total_probability += outcome_probability
        outcome_probability = 1.0

    return total_probability
    

if __name__ == "__main__":
    #print(list_of_all_games_outcomes(1))
    #print(list_of_all_games_outcomes(2))
    print(list_of_all_games_outcomes(4))
    print(probability_of_two_consecutive_losses_in_n_games(4))
    print(non_LL_outcomes_given_x_Ws_and_y_Ls(3, 3, 6))
    print(non_LL_outcomes_given_x_Ws_and_y_Ls(4, 2, 6))
            