import time
import sys

class Turing:
    """
    A simple Turing machine simulator. Data is 1D, expansible in both directions.

    You can use max_cntr argument of Reset method if you want to limit number of
    cycles (prevent against hanging). max_cntr = -1 means no limit.

    You can use delay argument of Run method in order to slow execution down.
    delay = -1 means waiting for ENTER from the keyboard (works ony on Unix).

    You can use printing arument of constructor to switch printing off and speed
    execution up.

    Program format:
        <state><data><new_state><new_data><direction><any_comments><\n>

    state - current state of the machine
    data - input symbols
    new_state - new state of the machine
    new_data - new symbol
    direction - directin of the head
    any_comments - user comments (optional)
    
    data, new_data - consists of any characters, but '_' means blank symbol
    state, new_state - can be any character, but 'x' means halt
    direction - it can be either '>' (means right), or '<' (means left)
    any_comments - any characters by the end of the line
    
    Program can contain empty lines. These are ignored.
    """

    def __init__(self, program, data, printing=True):
        self.prog = {}
        self.data = data        
        self.Reset()
        
        if not printing: self.Disp = lambda: None # Do nothing when Disp called

        # Convert program to a dictionary of the format:
        # "<state><data>": "<new_state><new_data><direction>"
        for instruction in program.strip().splitlines():
            self.prog[instruction[0:2]] = instruction[2:5]

    def Reset(self, init_state='0', init_head=0, max_cntr=-1):
        self.stat = init_state   # State of the machine
        self.head = init_head    # Position of the head
        self.cntr = 0            # Current number of cycles
        self.max_cntr = max_cntr # Max number of cycles
        

    def Step(self):
        # Take a single element from input data
        data = self.data[self.head:self.head+1]
        
        # If it is blank symbol, replace it by '_'
        if len(data) == 0: data = '_'
        
        try:
            # Read and decode a single instruction
            new_stat, new_data, direction = self.prog[self.stat + data]
        except KeyError:
            print('ERROR: No instruction at ' + str(self.stat + data))
            return True

        #if new_data != '_': # Skip if user attempts to write a blank symbol
        if self.head >= 0:
            # Overwrite a single element of data or expand data to the right
            self.data = self.data[0:self.head] + new_data + self.data[self.head+1:]
        else:
            # Expand data to the left
            self.data = new_data + self.data

        # Change state of the machine
        self.stat = new_stat
        
        # Move the head in appropriate direction
        self.head += [-1,1][direction == '>']
        
        # Return True if it's the last step of the program
        return new_stat == 'x' or self.cntr == self.max_cntr

    def Run(self, delay=0):
        while(True):
            self.Disp()
            self.cntr += 1

            if delay < 0:
                sys.stdin.read(1) # Wait for ENTER
            elif delay > 0:
                time.sleep(delay) # Wait given amount of time
                
            if self.Step(): break # Execute a single step of the program

        return self.data # Return output data
        
    def Disp(self):
        # This method may be disabled in __init__()
        print(' ' * (25 + self.head) + 'V')
        print('cntr/stat/data: %4i  %c  %s' % (self.cntr, self.stat, self.data))
        print()



