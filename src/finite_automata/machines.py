from src.Models.state import MealyState, MooreState
from src.base.finiteAutomata import BaseFiniteStateMachine
from src.finite_automata.fa import FiniteAutomata

class Mealy(FiniteAutomata, BaseFiniteStateMachine):

    def __init__(self, num_of_states: int, input_alpha: list[str], 
                 output_alpha: list[str]) -> None:
        """
        Initialize a Mealy machine.

        @params:
            - num_of_states (int): Number of states in the machine.
            - input_alpha (list[str]): List of input alphabets.
            - output_alpha (list[str]): List of output alphabets.
        """
        super().__init__(num_of_states, input_alpha, list("0"))
        self.__output_alpha: list[str] = output_alpha
    

    # Implement abstract method
    def get_output(self, input_str: str) -> str:
        """
        Get the Mealy Machine output for a given input string.

        @params:
            input_str (str): The input string.

        @return:
            str: The output string.
        """
        machine_output: str = str()
        curr_state: MealyState = self._transition_table[0]
        for char in input_str:
            machine_output += curr_state.get_curr_output(char)
            curr_state = curr_state.get_next_trans(char)

        return machine_output
    
    #Override
    def _create_states(self) -> None:   
        for i in range(self._num_of_states):
            curr_stateName: str = f"q{i}"
            is_init: bool = self._check_if_fin_or_init_state(self._init_states, curr_stateName)
            new_state: MealyState = MealyState(curr_stateName, is_init)

            self._transition_table.append(new_state)

    #Override
    def fill_table(self) -> None:
        """
        Fill the transition table for the Mealy machine.
        """
        self._create_states()

        print("Enter state and output (sep by comma) (e.g, Transition (state, input): Next State, Output)")
        for state in self._transition_table:
            for inp in self._input_alpha:
                curr_state, output = input(f"Transition ({state.get_stateName()},{inp}): ").split(",")
                curr_stateName: str = f"q{curr_state}" 
                next_state: MealyState = self._find_next_state(curr_stateName)
                state.add_transition(next_state, inp, output)
    

    #Override
    def display_transition_table(self) -> None:
        """
        Display the transition table for the Mealy machine.
        """
        print("states ", end="")

        for inp in self._input_alpha:
            print(f"   {inp}      ", end="")
        
        print()

        for state in self._transition_table:
            state.display_transition()
            print()


class Moore(FiniteAutomata, BaseFiniteStateMachine):

    def __init__(self, num_of_states: int, input_alpha: list[str], 
                 output_alpha: list[str]) -> None:
        """
        Initialize a Moore machine.

        @params:
            - num_of_states (int): Number of states in the machine.
            - input_alpha (list[str]): List of input alphabets.
            - output_alpha (list[str]): List of output alphabets.
        """
        super().__init__(num_of_states, input_alpha, list("0"))
        self.__output_alpha: list[str] = output_alpha

    #implement abstract method
    def get_output(self, input_str: str) -> str:
        """
        Get the Moore Machine output for a given input string.

        @params:
            input_str (str): The input string.

        @return:
            str: The output string.
        """
        curr_state: MooreState = self._transition_table[0]
        machine_output: str = curr_state.get_state_output()

        for char in input_str:
            print(curr_state.get_stateName())
            curr_state = curr_state.get_next_trans(char)
            machine_output += curr_state.get_state_output()
            
        return machine_output

    #Override
    def _create_states(self) -> None:   
        for i in range(self._num_of_states):
            curr_stateName: str = f"q{i}"
            is_init: bool = self._check_if_fin_or_init_state(self._init_states, curr_stateName)
            curr_state_output: str = input(f"Enter output of state {curr_stateName}: ")
            new_state: MooreState = MooreState(curr_stateName, is_init, curr_state_output)

            self._transition_table.append(new_state)

    #Override
    def fill_table(self) -> None:
        """
        Fill the transition table for the Moore machine.
        """
        self._create_states()

        for state in self._transition_table:

            for inp in self._input_alpha:
                curr_stateName: str = "q" + input(f"Transition ({state.get_stateName()},{inp}): ")

                next_state: MooreState = self._find_next_state(curr_stateName)
                state.add_transition(next_state, inp)
    
    #Override
    def display_transition_table(self) -> None:
        """
        Display the transition table for the Moore machine.
        """
        print(" states ", end="")

        for inp in self._input_alpha:
            print(f" {inp}   ", end="")
        
        print()

        for state in self._transition_table:
            state.display_transition()
            print()



