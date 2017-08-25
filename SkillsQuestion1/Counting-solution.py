from __future__ import division
import math

# Counting solution: 1 - Prob(No two consecutive Ls in 82 games)

# ALL cases of seasons with 42 losses or above results in two consecutive losses
# somewhere in the season. SOME cases of seasons with 41 losses or fewer results
# in two consecutive losses somewhere in the season. So, consider 41 losses or
# fewer. Or equivalently 41-wins-or-more seasons. Count all the ways for each case
# (41 wins, 42 wins, ... 82 wins) that no two Ls will be next to each other in the season.
# This gives Prob(No two consecutive Ls in 82 games). Do 1 - Prob(No two consecutive Ls in 82 games)
# to get Prob(two consecutive Ls in 82 games), noting that Prob(winning any one game) = 0.8.

def C(n, k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    

def probability_of_two_consecutive_losses_in_n_games(n):
    
    if(n%2 == 0):
        
        # Basically looks like: 2 * [ C(41, 0) * (0.8)^41 * (0.2)^41 ] +
        #                       2 * [ C(41, 1) * (0.8)^42 * (0.2)^40 ] +
        #                       2 * [ C(41, 2) * (0.8)^43 * (0.2)^39 ] +
        #                       ... +
        #                       2 * [ C(41, 40) * (0.8)^81 * (0.2)^1 ] +
        #                       C(41, 41) * (0.8)^82 * (0.2)^0    
        
        Prob_no_two_consecutive_losses = 0.0
        
        number_of_wins = int(n/2)
        for i in range(int(n/2)):
            number_of_losses = n - number_of_wins
            Prob_no_two_consecutive_losses += 2*(C(n/2,i)*math.pow(0.8, number_of_wins))*(math.pow(0.2, number_of_losses))
            print("i = " + str(i),"num_wins = " + str(number_of_wins), "num_losses = " + str(number_of_losses), "Prob_no_two_consecutive_losses = " + str(Prob_no_two_consecutive_losses), "C(n/2,i) = " + str(C(n/2,i)), "0.8^num_wins = " + str(math.pow(0.8, number_of_wins)), "0.2^num_losses = " + str(math.pow(0.2, number_of_losses)))
            number_of_wins += 1
        
        Prob_no_two_consecutive_losses += C(n/2, n/2)*math.pow(0.8, n)*math.pow(0.2, n-number_of_wins)
    
    return (1 - Prob_no_two_consecutive_losses)


if __name__ == "__main__":
    print(probability_of_two_consecutive_losses_in_n_games(4))
    