from src.finite_automata.fa import PushDown
from typing import List, Tuple

def main() -> None:
    # Step 1: Define PDA parameters
    num_states: int = 3
    input_alphabet: List[str] = [
        '(', ')', 
        '+', '-', '*', '/', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    stack_alphabet: List[str] = ['(', '$']
    final_states: List[str] = ['2']  # q2 is the final state
    start_state: str = 'q0'
    init_states: List[str] = ['0']  # q0 is the initial state

    # Step 2: Create the PDA
    pda = PushDown(num_states, input_alphabet, stack_alphabet, final_states, start_state, init_states)

    # Step 3: Define the transition table
    # Format: List for each state, where each tuple is (input, next_state_name, to_pop, to_push)

    transitions: List[List[Tuple[str, str, str, str]]] = [
    [   # q0: Start or after '('
        ('(', 'q0', 'e', '('),     # Push '('              
        ('0', 'q1', 'e', 'e'),     # Pop '(' 
        ('1', 'q1', 'e', 'e'),     # Start of number
        ('2', 'q1', 'e', 'e'),
        ('3', 'q1', 'e', 'e'),
        ('4', 'q1', 'e', 'e'),
        ('5', 'q1', 'e', 'e'),
        ('6', 'q1', 'e', 'e'),
        ('7', 'q1', 'e', 'e'),
        ('8', 'q1', 'e', 'e'),
        ('9', 'q1', 'e', 'e')
    ],
    [   # q1: In number (possibly multi-digit)
        ('0', 'q1', 'e', 'e'),     # Continue number
        ('1', 'q1', 'e', 'e'),
        ('2', 'q1', 'e', 'e'),
        ('3', 'q1', 'e', 'e'),
        ('4', 'q1', 'e', 'e'),
        ('5', 'q1', 'e', 'e'),
        ('6', 'q1', 'e', 'e'),
        ('7', 'q1', 'e', 'e'),
        ('8', 'q1', 'e', 'e'),
        ('9', 'q1', 'e', 'e'),
        ('+', 'q0', 'e', 'e'),     # Operator after number → go to q0 to handle next number or '('
        ('-', 'q0', 'e', 'e'),
        ('*', 'q0', 'e', 'e'),
        ('/', 'q0', 'e', 'e'),
        (')', 'q1', '(', 'e'),     # Pop '(' on ')'
        ('e', 'q2', '$', 'e')      # Accept if only '$' left in stack
    ],
    [   # q2: Final accepting state (optional)
        ('e', 'q2', '$', 'e')      # Stay in accept if stack has only '$'
    ]
]

    # Step 4: Initialize the PDA with the transition table
    pda.init_automaton(transitions)

    # Step 5: Display the transition table (for debugging purposes)
    # pda.display_transition_table()

    # Step 6: Test the PDA with various input strings
    test_cases = [
        "1+2",         # valid
        "(1+2)",       # valid
        "((1+2)*3)",   # valid
        "1+(2*3)-4",   # valid
        "(5*3+(4+2))", # valid
        "1+",          # invalid (ends with operator)
        "(1+2",        # invalid (unbalanced parentheses)
        "1+2)",        # invalid (unbalanced parentheses)
        "1++2",        # invalid (consecutive operators)
        "1+*2",        # invalid (operator misuse)
        "",            # invalid (empty string)
    ]

    # Step 7: Validate each test case
    for string in test_cases:
        try:
            result = pda.validate_input_str(string)
            print(f"'{string}' -> {'ACCEPTED' if result else 'REJECTED'}")
        except Exception as e:
            print(f"'{string}' -> ERROR: {e}")

if __name__ == "__main__":
    main()