####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DNME-MAS' # Only 10 chars displayed.
strategy_name = 'Every1 is the NME!'
strategy_description = 'b first, collude 10 times, check last 5 moves, if b 1 time, then b, else c.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    if len(my_history)>0 
        if len(my_history)<11:
            return 'c'
    if len(my_history):
        if my_history[-10]=='c' and their_history[-5]=='b':
            return 'b' # Betray if they were severely punished last time,
        else:
            return 'c' # otherwise collude.
    
 

    
