# We want to create a turing machine
# A turing machine can be defined as a matrix :
#  - The lines being the states that the turing machine has
#  - The rows being the alphabet we are working on

# For example:
# ------------
# Transition :
#    a     b
# 0  a1R   b0L
# 1  b1R   a0R
# ------------
# This is a 2-state turing machine, working on the alphabet {'a','b'}.
# The triplets define the transitions between the states
# For example, here : 'a', 1, 'R' in the Transition[0][a] square corresponds
# to : "write an 'a' ('a') where the  r/w head points, switch to state 1 (1) and move right ('R')

# For our definition of a turing machine to be complete we would also need a variable indicating where
# the r/w head is currently pointing and a variable that holds the infinite tape, on which the machine operates.

# Note : we could use numpy instead of the classic python arrays for optimization

# Lets try and encode a simple turing machine in this manner:
# We will create the turing machine that replaces all 'a's with 'b's 

# We need to store where the r/w head is pointing
# head = 0 # initially to the first symbol

#We need to store the tape
#tape = "" # initially empty

# Now what is left is the transitions
#turing_machine = \
#{
#    0: {
#        'a' : ('b',0,'R'),
#        'b' : ('b',0,'R'),
#        '_' : ('_',-1,'L')
#       }
# }
    
# Note that here the state -1 is the halt state (meaning that the turing machine stops
# So if we were to transcribe this to a table
#
#    a   b   _ 
# 0  b0R b0R _xL
#
# x is the halt state here (-1)

# So now in order to run this we can use the following algorithm

def run_machine(turing_machine, tape, state):
    print("Input on tape:\n"+tape) # Print input initially

    while (state != -1): # While not in the halt state
        sym = tape[head] if head<len(tape) else '_' # Take the symbol under the r/w head, if no symbol gives '_' (blank symbol by my arbitrary convention)
        new_sym, new_state, mov = turing_machine[state][sym] # Take what our transition table gives us
        tape = tape[:head] + new_sym + tape[head+1:] # Writing the symbol
        head += 1 if mov == 'R' else -1 # Position the head accordingly
        state = new_state # Change state

    return tape

