from __future__ import division
import math

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


def recursive_function_solution(n):
    if(n <= 1):
        return 0
    else:
        # Formula: F(n) = P_W*F(n-1) + (1-P_W)^2 + (1-P_W)*P_W*F(n-2)
        return P_W*(recursive_function_solution(n-1)) + math.pow(1-P_W, 2) + (1-P_W)*P_W*(recursive_function_solution(n-2))


def return_list_of_probabilities(n):
    probabilites_list = [0, 0]
    for i in range (n-1):
        probability = P_W*(probabilites_list[-1]) + math.pow(1-P_W, 2) + (1-P_W)*P_W*(probabilites_list[-2])
        probabilites_list.append(round(probability, 4))
    
    return probabilites_list


def probability_of_two_consecutive_losses_SOLUTION(n):
    F_n_minus_1, F_n_minus_2 = 0.0, 0.0 
    for i in range (n-1):
        probability = P_W*(F_n_minus_1) + math.pow(1-P_W, 2) + (1-P_W)*P_W*(F_n_minus_2)
        #probability = round(probability, 4)
        F_n_minus_2 = F_n_minus_1
        F_n_minus_1 = probability
    
    return probability
    

if __name__ == "__main__":
    #print(list_of_all_games_outcomes(1))
    #print(list_of_all_games_outcomes(2))
    #print(list_of_all_games_outcomes(4))
    #print(probability_of_two_consecutive_losses_in_n_games(4))
    #print(non_LL_outcomes_given_x_Ws_and_y_Ls(3, 3, 6))
    #print(non_LL_outcomes_given_x_Ws_and_y_Ls(4, 2, 6))
    n = 82
    P_W = 0.9037
    #print(probability_of_two_consecutive_losses_in_n_games(n))
    #print(recursive_function_solution(n))
    #print(return_list_of_probabilities(n))
    print(probability_of_two_consecutive_losses_SOLUTION(n))
    