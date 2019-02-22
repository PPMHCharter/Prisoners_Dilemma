####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Goldfish.' # Only 10 chars displayed.
strategy_name = 'The snack that smiles back.'
strategy_description = 'We start with collude but adapt to our opponents moves.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    else:
        if their_score == 0:
            return 'c'
        else:
            if 'b' in their_history:
                return 'b'
            else:
                return 'c'
