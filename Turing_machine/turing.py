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

def run_machine(turing_machine, tape, blank_symbol='_', verbose=False, limit=107):
    if verbose:
        print("\nInput on tape: "+tape+"\n") # Print input initially
    head = 0 # initialize head
    state = 0
    shifts = 0
    while (state != -1 and shifts<=limit): # While not in the halt state or exceeded interation limit
        #---------------------- Visualation
        if verbose: 
            print(tape)
            print(" "*head + "^")
        #----------------------
        sym = tape[head] if (head<len(tape) and head>=0) else blank_symbol # Take the symbol under the r/w head, gives the blank symbol given in parameter
        new_sym, new_state, mov = turing_machine[state][sym]
        tape = (tape[:head] if head!=-1 else '') + new_sym + tape[head+1:]
        head = 0 if head==-1 else head
        head += 1 if mov == 'R' else -1 # Position the head accordingly
        state = new_state # Change state
        shifts += 1

    if verbose:
        print("Result on tape :\n"+tape)
    return tape,state==-1,tape.count('1')

# To see the result of the programme, open in idle and type :

run_machine(turing_machine, "aabaa", verbose=True) # You can save this to a variable if you wish, but the function prints the result so no need here

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
print("===========\nTesting palindrome\n==========")
print("\nTest 1001")
run_machine(palindrome, "1001") # Should result in an empty tape
print("\nTest 101")
run_machine(palindrome, "101") # should result in an empty tape
print("\nTest 1101")
run_machine(palindrome, "1101") # should result in a non-empty tape


# Unary addition
# We will now program the unary addition
# It is quite simple as our program will take a sequence of 1s followed by a
# blank symbol (here 0) then another sequence of 1s.
# So for an input tape "111011" we should recieve "11111".

unary_addition = {
    0: {
        '1': ('1',0,'R'),
        '0': ('1',1,'R')
        },
    1: {
        '1': ('1',1,'R'),
        '0': ('0',2,'L')
        },
    2: {
        '1': ('0',-1,None), # The only transition that makes sense
        '0': ('0',-1,None)
        }
    }

# Testing it out:
print("="*10 + "\nTesting Unary Addition\n" + "="*10)
run_machine(unary_addition,"101",'0',True) # Should result in "11"
run_machine(unary_addition,"110111",'0',True) # Should result in "11111"

# Binary increment
# Here he will be constructing a TM that will increment a binary number
# So the input tape would be a binary number
# So for example if the machine recieves "1101" the result should be "1110"
# Here are some example :
# 0010++ = 0011, 00++ = 01, 011++ = 100
# So we notice that increment is reading the number from right to left changing
# all the 1s into 0s and the first 0 into a 1.
# So we recieve the machine:
# (Lets suppose that an this interaction exists machine("") -> ""

binary_increment = {
    0: {
        '0': ('0',0,'R'),
        '1': ('1',0,'R'),
        '_': ('_',1,'L')
        },
    1: {
        '0': ('1',-1,None),
        '1': ('0',1,'L'),
        '_': ('_',-1,None)
        }
    }

# Lets test it out
print("="*10 + "\nTesting binary increment\n" + "="*10)
run_machine(binary_increment,"0") # Should result in "1"
run_machine(binary_increment,"1100") # Should result in "1101"
run_machine(binary_increment,"011") # Should result in "100"

# Binary decrement
# So using the same logic if we think about it we got the mirror
# operation, that this time changes all the 0s into 1s before changing the
# first 1 into a 0 from right to left again.

binary_decrement = {
    0: {
        '0': ('0',0,'R'),
        '1': ('1',0,'R'),
        '_': ('_',1,'L')
        },
    1: {
        '0': ('1',1,'L'),
        '1': ('0',-1,None),
        '_': ('_',-1,None)
        }
    }


# Lets test it out
print("="*10 + "\nTesting binary decrement\n" + "="*10)
run_machine(binary_decrement,"1") # Should result in "0"
run_machine(binary_decrement,"1100") # Should result in "1011"
run_machine(binary_decrement,"011") # Should result in "010"

# Binary addition
# Now knowing how to increment and decrement, we should be able to program
# addition simply by incrementing and decrementing successively

binary_addition = {
    0: {
        '0': ('0',0,'R'),
        '1': ('1',0,'R'),
        '_': ('_',1,'R')
        },
    1: {
        '0': ('0',1,'R'),
        '1': ('1',2,'R'),
        '_': ('_',-1,None)
        },
    2: {
        '0': ('0',2,'R'),
        '1': ('1',2,'R'),
        '_': ('_',3,'L')
        },
    3: {
        '0': ('1',3,'L'),
        '1': ('0',4,'L'),
        '_': ('_',-1,None) #This will never happen as we check if the number if zero beforehand
        },
    4: {
        '0': ('0',4,'L'),
        '1': ('1',4,'L'),
        '_': ('_',5,'L')
        },
    5: {
        '0': ('1',0,'R'),
        '1': ('0',5,'L'),
        '_': ('_',0,'R')
        }
    }


# Lets test it out
print("="*10 + "\nTesting binary addition\n" + "="*10)
run_machine(binary_addition,"01_10") # Should result in "11" (1 + 2)
run_machine(binary_addition,"001_011") # Should result in "100" (1 + 3)
run_machine(binary_addition,"0110_0011") # Should result in "1001" (6 + 3)

# Others ... ?

### Creating a random turing machine
# Now that we have become a bit more conformtable with the idea of turing machines
# and how they work, we will attempt to create a random turing machine!
# As we now know what defines a turing machines is it's transitions, so in order to
# create a random turing machine all we need to do is give a  certain number of
# states that the machine will have, give a certain alphabet on which we will be working
# and then simply fill the squares of our transition table, with random symbols

# To start simple, let's say we will attempt to create a random 1-state turing machine, with the alphabet 0,1 and _ (blank symbol)
alphabet = ('0','1','_')

# A N-state turing machine, means that the machine has N non-halting state, meaning that there can be always be a halting state.

# We use tuples as python's random module natively uses tuples
# So now all that is left is to do is assign random transitions into a dictionary

import random # we need this for the choice function

def create_random_machine(n_states,alphabet):
    random_machine = dict()# empty transition table
    states = tuple(range(-1,n_states)) #This way we always include the -1 halting state
    mov = ('L','R') # Left or Right
    for state in range(n_states):
        random_machine[state] = dict() # Necessary to initialize it
        for alpha in alphabet:
            random_machine[state][alpha] = (random.choice(alphabet), # choosing random letter to write
                                            random.choice(states), # choosing a random state to transition to
                                            random.choice(mov) # choosing a random movement
                                            )
    return random_machine

# Running this simple algorithm now will generate a random N-state machine 
random_machine = create_random_machine(1,alphabet) # This will now generate a random 1-state turing machine

# You can now try this out and see that we have indeed created a random 1-state turing machine by
# print the variable random_machine

### Trying to find one of our own machines

# Now... at the start of this file we created a 1-state turing machine using the alphabet 'a','b' and '_' to create a 1-state
# turing machine that changed all a's to b's, we could maybe try to see if creating random 1 state turing machines will at some point
# give us the machine we created earlier.

random_machine = dict()
while (random_machine != turing_machine): # We named it turing machine earlier
    random_machine = create_random_machine(1, ('a','b','_'))
    print("Looking...looking...")
print("Found it!")

# Amazing isn't it, so we just created a program, that created random programs, until it ended up by finding the program we had
# created earlier.

# We can make sure that it is the same program by running it and making sure it does it's job correctly!

run_machine(random_machine,'aabba') # Should result in 'bbbbb'

### Enumerating all possible turing machines

# So instead of enumerating all of the turing machines, lets try enumerating
# only all 1-state turing machines.

# First of all we will generate all possible transitions for a square of our
# transition table
# We have 3 symbols in our alphabet ('a','b','_'), 2 possible states (-1,0) and 2
# possible movements ('R','L').
# So for a single square we have 3x2x2 = 12 options.

# After that we have to get all the possible combinations of 3 tuples.
# As a turing machine is simply a transition table, if we have 1 state, our
# table will resemble something like this :
#
#       a     b    _
#  0   X1    X2   X3

# So to create all of them we need to enumerate all of the possibilities
# for X1,X2,X3 where each one individually will be chosen from the possibilities
# for one square of the matrix. So what we obtain is 12**3 = 1728 possibilities
# for 1-state turing machines (using ('a','b','_') for alphabet)

# So in order to program it, we need to generate our tuples.
# Then simply put them in a dictionary

import itertools # we use itertools' optimized function of the cartesian product
one_square = tuple(itertools.product(('a','b','_'),(-1,0),('R','L'))) # all possibilities for one square of the matrix
three_squares = tuple(itertools.product(one_square,repeat=3)) # all possibilities for three squares
all_machines_1 = []
for t1,t2,t3 in three_squares:
    machine_t,machine_t[0] = dict(), dict()
    machine_t[0]['a'], machine_t[0]['b'], machine_t[0]['_'] = t1,t2,t3
    all_machines_1.append(machine_t)

# lets now try to find our machine again
print("It is the "+str(all_machines_1.index(turing_machine))+" machine") # This will give the index of our machine in the list of all machines

# Now that we have seen the principle for a 3 letter alphabet and 1 state, we can
# generalize for n states and a m letter alphabet.

def enumerate_turing_machines(n_states, alphabet):
    # We will not store them, as the number of turing machines grows insanely fast and we will easily saturate the computer's memory
    # To grasp the idea, there are 1 728 1-state turing machines, there are 2 985 984 2-state turing machines...
    n_symboles = len(alphabet) # The number of letters in the alphabet
    one_square = tuple(itertools.product(alphabet,tuple(range(-1,n_states)),('R','L')))
    # So now 1 entry of the all_squares tuple, is 1 turing machine, so all thats left is to transform it into a dictionary
    nb_machines = 0
    for machine_transitions in itertools.product(one_square,repeat=n_symboles*n_states):
        i, nb_machines = 0, nb_machines+1
        nth_machine = dict()
        for state in range(n_states):
            nth_machine[state] = dict()
            for sym in alphabet:
                nth_machine[state][sym],i = machine_transitions[i],i+1
        yield nth_machine # More efficient as we are generating insane amount of machines
    print("Generated "+str(nb_machines)+" machines")

### Busy beaver

# A busy beaver is for a given number of states (using binary alphabet ('0','1')), the turing machine that produces the most number of 1s on the tape starting
# with a blank tape (only 0s) and halts (very important).
# So now that we are able to enumerate all turing machines, in order to find the busy beaver for a given state, we would need to test the machines, problem is not
# all of them stop... Even worse it has been proven mathematically that there is no sure way to know if a turing machine stops...
# So what we need is to find a stop test that is reliable enough but not too hard so that we can test the output of our turing machines.

import math # for the log function
import time

def quick_halt_test(machine):
    for state in machine:
        for sym in machine[state]:
            if -1 in machine[state][sym]:
                return True
    return False

def nth_busy_beaver(n,shifts=107): # The value 107 is the value for Tibor Rado's S(n) function for all beavers up to 4 states
    """
    This function finds the busy beaver for a certain n using a 
    very naive method by simply limiting the number of shifts a busy beaver can do.
    """
    ts = time.time()
    max_ones,winner,nb_of_winners  = 0, None, 0
    cpt, total = 0 ,(4*(n+1))**(2*n)
    for m in enumerate_turing_machines(n,('0','1')):
        if not quick_halt_test(m):
            pass
        else:
            _,stops,ones = run_machine(m,'','0',limit=shifts)
            if stops and ones > max_ones:
                max_ones = ones
                winner = m
                nb_of_winners = 1
            elif ones==max_ones:
                nb_of_winners += 1
        if (cpt==0 or math.log10(cpt).is_integer()):
            print('*')
        cpt+=1
    print(time.time()-ts)
    return max_ones,winner,nb_of_winners

# With this simple naive test, we can find the first 3 busy beavears relatively
# quickly, but for n's bigger than 3, it becomes insanely laborious because of
# the amount of machines to test

# For test purposes these are commented out but you can test them out if you wish
# (nb: the values for shifts are the exact s(n) values from the wikipedia page for optimization purposes)

# nb_ones_1, busy_beaver1, nb_win1 = nth_busy_beaver(1,shifts=2)

# nb_ones_2, busy_beaver2, nb_win2 = nth_busy_beaver(2,shifts=6)

# This already takes a bit of time due to the [4(n+1)]^(2n) = 16^6 machines
nb_ones_3, busy_beaver3, nb_win3 = nth_busy_beaver(3,shifts=21)

# This one would take an all nighter most likely, but it would find it.
# nb_ones_4, busy_beaver4, nb_win4 = nth_busy_beaver(4)

# For the next busy beaver, considering the current lower bound for s(n) ~= 47 million, 
# running our function would probably take a couple of human lifetimes on any computer.

#### Universal turing machine

# As we know a universal turing machine executes the turing machine that is encoded on it's tape
# so we would need to start by being able to encode a turing machine as Alan Turing described it
# in his 1936 paper "On computable numbers" (https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)

def encode_machine(machine):
    """
    Each cell of our transition table will be encoded in the following way:

    [state][scanned symbol][printing symbol][movement][new state]

    where:
    - the states be encoded with the following code {DA, DAA, DAAA, ...} where qi = D(A^i)
    - the scanned symbol will be encoded with the following code {D, DC, DCC, ...} where si = D(A^i) given that D = blank_symbol always
    - the printing symbol will be encoded in the same way as the scanned one
    - the movemenet will simply represent either R or L.
    - the new state will be encoded in the same way as the originating state

    So for example, the line (considering a binary alphabet and 0 as the blank symbol):

    {0: {0: ('1',1,'L'), ...}, ...  ==>  q0 blank 1 L q1  ==> DADDCLDAA
    
    The different cells being interlaced with semicolons (';')
    
    And all of this on alternating squares meaning the sequence DADDCLDAA will actually be D.A.D.D.C.L.D.A.A where '.' will be a special character

    """
    pass
