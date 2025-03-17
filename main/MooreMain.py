from src.finite_automata.machines import Moore

def main() -> None:

    num_of_states: int
    input_alpha: list[str]
    output_alpha: list[str]
    input_str: str

    num_of_states = int(input("Enter the number of states: "))
    input_alpha = input("Enter the input alphabet (seb by comma): ").split(",")
    output_alpha = input("Enter the output alphabet (seb by comma): ").split(",")

    mealy: Moore = Moore(num_of_states, input_alpha, output_alpha)

    mealy.fill_table()

    mealy.display_transition_table()

    loop_state: bool = True

    while(loop_state):
        input_str = input("Enter the input string: ")

        print(f"Output: {mealy.get_output(input_str)}")
        
        is_retry: str = input("Do you want to try another string? <any key>/N: ")

        if (is_retry.lower() == "n"):
            break
    
    print("Program finished!")


if __name__ == "__main__":
    main()