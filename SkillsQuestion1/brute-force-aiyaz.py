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

def probability_of_two_consecutive_losses_in_n_games(n):
    list_of_outcomes = list_of_all_games_outcomes(n)
    number_of_possible_outcomes = len(list_of_outcomes)
    list_of_outcomes_with_two_consecutive_losses = []
    
    for outcome in list_of_outcomes:
        if 'LL' in outcome:
            list_of_outcomes_with_two_consecutive_losses.append(outcome)
            
    number_of_outcomes_with_two_consecutive_losses = len(list_of_outcomes_with_two_consecutive_losses)

    return (number_of_outcomes_with_two_consecutive_losses/number_of_possible_outcomes)
    

if __name__ == "__main__":
    #print(list_of_all_games_outcomes(1))
    #print(list_of_all_games_outcomes(2))
    print(list_of_all_games_outcomes(15))
    print(probability_of_two_consecutive_losses_in_n_games(15))
    # Not finished yet, didn't incorporate probability values of 80% win rate
            