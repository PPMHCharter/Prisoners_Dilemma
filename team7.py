####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ACAM'
strategy_name = 'History with the player'
strategy_description = 'The strategy looks at the previous history with the player'
    
def move(my_history, their_history, my_score, their_score):

    if len(my_history)==0:
        return 'c'
    else:
        
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' 
        else:
            return 'c'
