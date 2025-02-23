from src.finite_automata.fa import DFA

def main():
    
    states: int = int()
    input_alpha: list[str] = list()
    init_states: list[str] = list()
    fin_states: list[str] = list()
    input_str: str = str()

    states = int(input("Enter the number of states: "))
    input_alpha = input("Enter the input alphabet (seb by comma): ").split(",")

    init_states = input("Enter the initial state/s (seb by comma): ").split(",")
    fin_states = input("Enter the final state/s (seb by comma): ").split(",")

    dfa: DFA = DFA(states, input_alpha, init_states, fin_states)

    dfa.fill_table()

    dfa.display_transition_table()

    loop_state: bool = True

    while(loop_state):
        input_str = input("Enter the input string: ")

        if dfa.validate_input_str(input_str):
            print("Remarks: Accepted")
        else:
            print("Remarks: Rejected")
        
        is_retry: str = input("Do you want to try another string? <any key>/N: ")

        if (is_retry.lower() == "n"):
            break
    
    print("Program finished!")


if __name__ == "__main__":
    main()