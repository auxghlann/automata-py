from src.Models.state import State, PushdownState
from src.base.finiteAutomata import BaseFiniteAutomata
from typing import Tuple, List

class FiniteAutomata(BaseFiniteAutomata):

    def __init__(self, num_of_states: int,  input_alpha: list[str], init_states: list[str],
                    final_states: list[str] | None = None) -> None:
        """
        Initialize a FA.

        @params
            num_of_states (int): Number of states in the FA.
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
        Validate the input string against the FA.

        @params
            input_str (str): The input string to validate.

        @return:
            True if the input string is accepted by the FA, False otherwise.
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


    def init_automaton(self, init_transition_table: list[list[Tuple[str, str]]]) -> None:
        # input, next state
        for i in range(len(init_transition_table)):

            curr_state: State = self._transition_table[i]

            for init_trans in init_transition_table:
                inp, next_state = init_trans
                next_state: State = self._find_next_state(next_state)
                curr_state.add_transition(next_state, inp)



    def fill_table(self) -> None:
        """
        Fill the transition table for the FA.
        """

        self._initialize_states()

        for state in self._transition_table:

            for inp in self._input_alpha:
                curr_stateName: str = "q" + input(f"Transition ({state.get_stateName()},{inp}): ")

                next_state: State = self._find_next_state(curr_stateName)
                state.add_transition(next_state, inp)

    def display_transition_table(self) -> None:
        """
        Display the transition table for the FA.
        """

        print("states ", end="")

        for inp in self._input_alpha:
            print(f" {inp}  ", end="")
        
        print()

        for state in self._transition_table:
            state.display_transition()
            print()

    def _check_if_fin_or_init_state(self, states: list[str], curr_stateName: str) -> bool:
         
        for state in states:
            build_state_name: str = f"q{state}"
            return build_state_name == curr_stateName
        

    def _initialize_states(self) -> None:
        
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
    
    

class PushDown(FiniteAutomata):
    
    def __init__(self, num_of_states: int, input_alpha: List[str], stack_symbol: List[str], 
                 final_states: List[str], start_state: str, start_stk_symbol: str = "$", 
                 init_states: List[str] | None = None,) -> None:
        super().__init__(num_of_states, input_alpha, init_states, final_states)
        self.stack_symbol = stack_symbol
        self.start_state = start_state
        self.stack: List[str] = [start_stk_symbol]

    #overwrite
    def validate_input_str(self, input_str: str) -> bool:
        init_state: PushdownState = None
        
        # find initial state
        for state in self._transition_table:
            if state.isInitState():
                init_state = state
                break
        
        # raise error if initial is not found
        if init_state is None:
            raise ValueError("Initial state not found")
        
        curr_state: PushdownState = init_state
        for char in input_str:
            curr_state = curr_state.get_next_trans(char, self.stack)
        
        return curr_state.isFinalState() and self.stack.pop == self.stack_symbol

    def init_automaton(self, init_transition_table: list[list[Tuple[str, str, str, str]]]) -> None:
        
        """
        Initialize the PDA with the given transition table.

        @params
            init_transition_table (list[list[Tuple[str, str, str, str]]]): 
                List of transitions where each transition is a tuple of 
                (input_char, next_state, to_pop, to_push).
        """

        self._initialize_states()

        for i in range(len(init_transition_table)):
            curr_state: PushdownState = self._transition_table[i]

            for init_trans in init_transition_table[i]:
                inp, next_state_name, to_pop, to_push = init_trans
                next_state: PushdownState = self._find_next_state(next_state_name)

                if (to_pop == "e" and to_push == "e"):
                    curr_state.add_transition(next_state, inp)
                
                elif (to_pop == "e" and to_push != "e"):
                    curr_state.add_transition(next_state, inp, to_pop=to_pop)
                
                elif (to_pop != "e" and to_push == "e"):
                    curr_state.add_transition(next_state, inp, to_push=to_push)
                else:
                    curr_state.add_transition(next_state, inp, to_pop, to_push)


    def _initialize_states(self) -> None:
        for i in range(self._num_of_states):
            curr_stateName: str = f"q{i}"
            is_init: bool = self._check_if_fin_or_init_state(self._init_states, curr_stateName)
            is_fin: bool = self._check_if_fin_or_init_state(self._final_states, curr_stateName)
            new_state: PushdownState = PushdownState(curr_stateName, is_init, is_fin)
            self._transition_table.append(new_state)
    

    

    
    