####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DNME-MAS' # Only 10 chars displayed.
strategy_name = 'Every1 is the NME!'
strategy_description = 'Always c except when the other team b then I b except 1/7 of the time I can change my mind and c'
import random
    
def move(my_history, their_history, my_score, their_score):
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    '''    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
        return 'c'
    else:
        if their_history[-1]=='b':
            if random.randint(1,7)==3:
                return 'c'
            else:
                return 'b'
        else:
            return 'c'    
