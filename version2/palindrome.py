from turing_machine import TuringMachine

initial_state = "q0"
transition_function = {("q0","0"):("q4", "_", "R"),
                       ("q0","1"):("q1", "0", "R"),
                       ("q0","_"):("accept","_", None),
                       ("q1","1"):("q1","1","R"),
                       ("q1","0"):("q1","0","R"),
                       ("q1","_"):("q2","_","L"),
                       ("q2","1"):("q3","_","L"),
                       ("q2","_"):("accept","_", None),
                       ("q3","1"):("q3","1","L"),
                       ("q3","0"):("q3","0","L"),
                       ("q3","_"):("q0","_","R"),
                       ("q4","0"):("q4","0","R"),
                       ("q4","1"):("q4","1","R"),
                       ("q4","_"):("q5","_","L"),
                       ("q5","0"):("q3","_","L"),
                       ("q5","_"):("accept","_", None),
                       }
final_states = {"accept"}

t = TuringMachine("010011", 
                  initial_state = initial_state,
                  final_states = final_states,
                  blank_symbol = "_",
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")    
print(t.get_tape())
