from src.Models.state import State
from src.base.finiteAutomata import BaseFiniteAutomata


class DFA(BaseFiniteAutomata):

    def __init__(self, num_of_states: int,  input_alpha: list[str], init_states: list[str],
                    final_states: list[str] | None = None) -> None:
        """
        Initialize a DFA.

        @params
            num_of_states (int): Number of states in the DFA.
            input_alpha (list[str]): List of input alphabets.
            init_states (list[str]): List of initial states.
            final_states (list[str] | None): List of final states, optional.
        """
        self._num_of_states: int = num_of_states
        self._input_alpha: list[str] = input_alpha
        self._init_states: list[str]  = init_states
        self._final_states: list[str] | None = final_states
        self._transition_table: list[State] = list()
    

    # implement abstract method from base class
    def validate_input_str(self, input_str: str ) -> bool:
        """
        Validate the input string against the DFA.

        @params
            input_str (str): The input string to validate.

        @return:
            True if the input string is accepted by the DFA, False otherwise.
        """
        init_state: State
        
        for state in self._transition_table:
            if state.isInitState():
                init_state = state
                break
        
        if (init_state == None):
            raise ValueError("Initial state not found")
        
        curr_state: State = init_state
        for char in input_str:
            curr_state = curr_state.get_next_trans(char)
        
        return curr_state.isFinalState()

    def _check_if_fin_or_init_state(self, states: list[str], curr_stateName: str) -> bool:
         
        for state in states:
            build_state_name: str = f"q{state}"
            return build_state_name == curr_stateName
        

    def _create_states(self) -> None:
        
        for i in range(self._states):
            curr_stateName: str = f"q{i}"
            is_init: bool = self._check_if_fin_or_init_state(self._init_states, curr_stateName)
            is_fin: bool = self._check_if_fin_or_init_state(self._final_states, curr_stateName)
            new_state: State = State(curr_stateName, is_init, is_fin)

            self._transition_table.append(new_state)

    def _find_next_state(self, state_name: str) -> State:

        for state in self._transition_table:
            if state.get_stateName() == state_name:
                return state
        
        # raise ValueError("State does not exist")
    
    def fill_table(self) -> None:
        """
        Fill the transition table for the DFA.
        """

        self._create_states()

        for state in self._transition_table:

            for inp in self._input_alpha:
                curr_stateName: str = "q" + input(f"Transition ({state.get_stateName()},{inp}): ")

                next_state: State = self._find_next_state(curr_stateName)
                state.add_transition(next_state, inp)

    def display_transition_table(self) -> None:
        """
        Display the transition table for the DFA.
        """

        print("states ", end="")

        for inp in self._input_alpha:
            print(f" {inp}  ", end="")
        
        print()

        for state in self._transition_table:
            state.display_transition()
            print()
        
            




    

    

    
    