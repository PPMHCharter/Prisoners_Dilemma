####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'KTJA' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
import random

    

def move(my_history, their_history, my_score, their_score):

    '''Make my move based on the history with this player.

    

    history: a string with one letter (c or b) per round that has been played with this opponent.

    their_history: a string of the same length as history, possibly empty. 

    The first round between these two players is my_history[0] and their_history[0]

    The most recent round is my_history[-1] and their_history[-1]

    

    Returns 'c' or 'b' for collude or betray.

    '''

    # If the other player has betrayed or this is the last half of the game, 

    if 'b' in their_history or len(their_history)>0: 
        return 'b'               # Betray.
    else:
        if 'c' in their_history and len(my_score)<0
            return 'c'         # but 90% of the time collude
        else:
            return 'b'
