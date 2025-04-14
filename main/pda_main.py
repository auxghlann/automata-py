from typing import List, Tuple
from src.finite_automata.fa import PushDown

def main() -> None:
    # Step 1: Create the PDA
    num_states = 2
    input_alphabet = ['(', ')']
    stack_alphabet = ['(', '$']
    final_states = ['1']
    start_state = 'q0'
    init_states = ['0']

    pda = PushDown(num_states, input_alphabet, stack_alphabet, final_states, start_state, init_states)

    # Step 2: Define transition table
    # Format: List for each state, where each tuple is (input, next_state_name, to_pop, to_push)
    transitions: List[List[Tuple[str, str, str, str]]] = [
        [   # Transitions for q0
            ('(', 'q0', 'e', '('),   # push '(' on '('
            (')', 'q1', '(', 'e'),   # pop '(' on ')'
            ('e', 'q1', '$', 'e')    # epsilon transition to final if stack has only $
        ],

        [
            # Transitions for q1
            ('(', 'q0', 'e', '('),   # push '(' on '('
            (')', 'q1', '(', 'e'),   # pop '(' on ')'
            ('e', 'q1', '$', 'e')    # epsilon transition to final if stack has only $
        ]
    ]

    # Step 3: Initialize PDA
    pda.init_automaton(transitions)

    pda.display_transition_table()


    # Step 4: Test some strings
    test_cases = [
        "()",           # valid
        "(())",         # valid
        "(()())",       # valid
        "(",            # invalid
        "())",          # invalid
        "(()",          # invalid
        "",             # valid (empty string is balanced)
    ]

    # Step 5: Run tests
    for string in test_cases:
        try:
            result = pda.validate_input_str(string)
            print(f"'{string}' -> {'ACCEPTED' if result else 'REJECTED'}")
        except Exception as e:
            print(f"'{string}' -> ERROR: {e}")

if __name__ == "__main__":
    main()