####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DNME-MAS' # Only 10 chars displayed.
strategy_name = 'Every1 is the NME!'
strategy_description = 'Playing The Percentages'
    
def move(my_history, their_history, my_score, their_score):
    opp_b = 0
    opp_c = 0
    
    if len(my_history) < 10:
        return 'c'
    elif len(my_history) < 20:
        return 'b'
    else:
        for choice in their_history:
            if choice == 'b':
                opp_b += 1
            else:
                opp_c += 1
                
        if opp_c != 0:
            percentage = float(opp_b)/opp_c
        else:
            return 'b'
            
        if percentage >= 1:
            return 'b'
        else:
            return 'c'
    
 

    
