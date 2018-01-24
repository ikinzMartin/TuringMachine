
class UnknownStateException(Exception):
    pass

class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.tape = tape
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        if transition_function == None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function
        if final_states == None:
            self.final_states = set()
        else:
            self.final_states = final_states
        
    def get_tape(self): 
        return self.tape
    
    def step(self):
        char_under_head = self.get_head_symbol()
        state = (self.current_state, char_under_head)
        if state in self.transition_function:
            new_state, new_symbol, direction = self.transition_function[state]
            self.write_to_tape(new_symbol)
            if direction == "R":
                self.head_position += 1
            elif direction == "L":
                self.head_position -= 1
            self.current_state = new_state
        else:
            raise UnknownStateException();

    def write_to_tape(self, symbol):
        index = self.head_position
        self.tape = self.tape[:index] + symbol + self.tape[index+1:]

    def get_head_symbol(self):
        try:
            return self.tape[self.head_position]
        except:
            self.write_to_tape(self.blank_symbol)
            return self.blank_symbol
        
    def final(self):
        return self.current_state in self.final_states
