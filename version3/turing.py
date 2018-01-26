### Creating a turing machine
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

# Lets try and encode a simple turing machine in this manner:
# We will create the turing machine that replaces all 'a's with 'b's 

# We need to store where the r/w head is pointing
head = 0 # initially to the first symbol

#We need to store the tape
tape = "" # initially empty

# Now what is left is the transitions
# We can code a matrix comfortably
turing_machine = \
{
    0: {
        'a' : ('b',0,'R'),
        'b' : ('b',0,'R'),
        '_' : ('_',-1,'L')
       }
}
    
# Note that here the state -1 is the halt state (meaning that the turing machine stops
# So if we were to transcribe this to a table
#
#    a   b   _ 
# 0  b0R b0R _xL
#
# x is the halt state here (-1)

# So now in order to run this we can use the following algorithm

def run_machine(turing_machine, tape, state, verbose=False):
    head = 0 # initialize head
    print("Input on tape: "+tape+"\n") # Print input initially

    while (state != -1): # While not in the halt state
        #---------------------- Visualation
        if verbose: 
            print(tape)
            print(" "*head + "^")
        #----------------------
        sym = tape[head] if head<len(tape) else '_' # Take the symbol under the r/w head, if no symbol gives '_' (blank symbol by my arbitrary convention)
        new_sym, new_state, mov = turing_machine[state][sym] # Take what our transition table gives us
        tape = tape[:head] + new_sym + tape[head+1:] # Writing the symbol
        head += 1 if mov == 'R' else -1 # Position the head accordingly
        state = new_state # Change state
        
    print("Result on tape :\n"+tape)
    return tape

# To see the result of the programme, open in idle and type :

run_machine(turing_machine, "aabaa", 0, verbose=True) # You can save this to a variable if you wish, but the function prints the result so no need here

#  - The first argument is the transition matrix encoded with a dictionary
#  - The second argument is the input on the tape
#  - The last is the initial state of the machine

### Testing out our machine

# So now we have a very minimalistic version of a turing maching
# We can use it to try out some programs

# Palindrome
palindrome = {
                 0 : {
                     '0' : ('_',4,'R'),
                     '1' : ('_',1,'R'),
                     '_' : ('_',-1,None) # The word is a palindrome
                     },
                 1 : {
                     '0' : ('0',1,'R'),
                     '1' : ('1',1,'R'),
                     '_' : ('_',2,'L')
                     },
                 2 : {
                     '0' : ('0',-1,None), # The word is NOT a palindrome
                     '1' : ('_',3,'L'),
                     '_' : ('_',-1,None) # The word is a palindrome
                     },
                 3 : {
                     '0' : ('0',3,'L'),
                     '1' : ('1',3,'L'),
                     '_' : ('_',0,'R')
                     },
                 4 : {
                     '0' : ('0',4,'R'),
                     '1' : ('1',4,'R'),
                     '_' : ('_',5,'L')
                     },
                 5 : {
                     '0' : ('_',3,'L'),
                     '1' : ('1',-1,None), # The word is NOT a palindrome
                     '_' : ('_',-1,None) # The word is a palindrome
                     }
                 }

# In order to test it out :
print("===========\nTesting palindrome\n==========");
print("\nTest 1001")
run_machine(palindrome, "1001", 0) # Should result in an empty tape
print("\nTest 101")
run_machine(palindrome, "101", 0) # should result in an empty tape
print("\nTest 1101")
run_machine(palindrome, "1101", 0) # should result in a non-empty tape


# Addition

# Reversing a tape

# Others ... ?

### Creating a random turing machine

### Enumerating all possible turing machines

### Trying to find one of our own machines

### Busy beaver
