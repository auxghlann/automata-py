from __future__ import annotations
from typing import Tuple
class State():

    def __init__(self, state_name: str, isInitState: bool, 
                 isFinalState: bool | None = None):
        self.__state_name: str = state_name
        self.__isInitState: bool | None = isInitState
        self.__isFinalState: bool = isFinalState
        self.__transitions: list[dict[str, State]] = list(dict())
        # self.__state_output = state_output

    def __str__(self) -> str:
        return self.__state_name

    def get_stateName(self) -> str:
        return self.__state_name
    
    def isFinalState(self) -> bool:
        return self.__isFinalState
    
    def isInitState(self) -> bool:
        return self.__isInitState

    def add_transition(self, state: State, input_char: str) -> None:
        state_trans: dict[str, State] = {input_char : state}
        self.__transitions.append(state_trans)

    def get_transitions(self):
        return self.__transitions
    
    def get_next_trans(self, input_char: str) -> State:
        for trans in self.__transitions:
            if input_char in trans:
                return trans[input_char]

        raise ValueError(f"Did not find next transition for input {input_char}")

    def display_transition(self) -> None:
        if self.isInitState():
            print(f" -{self.get_stateName()} | ", end="")
        elif self.isFinalState():
            print(f" +{self.get_stateName()} | ", end="")
        else:
            print(f"  {self.get_stateName()} | ", end="")

        for trans in self.__transitions:

            for _, value in trans.items():
                print(f"{value} | ", end="")



class MealyState(State):

    def __init__(self, state_name: str, isInitState: bool) -> None:
        super().__init__(state_name, isInitState)
        self.__outputs_list: list[dict[str, str]] = list(dict())
    
    # override and overload
    def add_transition(self, state: State, input_char: str, output_char: str) -> None:
        super().add_transition(state, input_char)
        state_trans: dict[str, str] = {input_char : output_char}
        self.__outputs_list.append(state_trans)
    
    #override
    def get_next_trans(self, input_char: str) -> MealyState:
        return super().get_next_trans(input_char)

    def get_curr_output(self, input_char: str) -> str:
        for outputs in self.__outputs_list:
            if input_char in outputs:
                return outputs[input_char]
        
        raise ValueError(f"Did not find output for input {input_char}")

    #override
    def display_transition(self) -> None:
        if super().isInitState():
            print(f" -{super().get_stateName()} | ", end="")
        else:
            print(f"  {super().get_stateName()} | ", end="")

        ctr: int = 0
        for trans in super().get_transitions():

            for key, value in trans.items():
                print(f" {value},{self.__outputs_list[ctr].get(key)}  | ", end="")

            ctr += 1


class MooreState(State):

    def __init__(self, state_name: str, isInitState: bool, state_output:str) -> None:
        super().__init__(state_name, isInitState)
        self.__state_output: str = state_output
    
    # reuse add_transition method of state class
    def add_transition(self, state: State, input_char: str) -> None:
        super().add_transition(state, input_char)

    #override
    def get_next_trans(self, input_char: str) -> MooreState:
        return super().get_next_trans(input_char)
    
    def get_state_output(self) -> str:
        return self.__state_output

    def display_transition(self) -> None:
        if super().isInitState():
            print(f" -{super().get_stateName()},{self.get_state_output()} | ", end="")
        else:
            print(f"  {super().get_stateName()},{self.get_state_output()} | ", end="")

        for trans in super().get_transitions():

            for _, value in trans.items():
                print(f"{value} | ", end="")
    
class PushdownState(State):
    

    def __init__(self, state_name: str, isInitState: bool, isFinalState: bool):
        super().__init__(state_name, isInitState, isFinalState)
        self.__transitions: list[dict[str, Tuple[State, str, str]]] = list()
        
    # override
    def get_transitions(self) -> list[dict[str, Tuple[State, str, str]]]:
        return self.__transitions
    
    # override and overload
    def add_transition(self, nxt_state: State, input_char: str, to_pop: str | None = None, 
                       to_push: str | None = None) -> None:
        state_trans: dict[str, Tuple[State, str, str]] = {input_char: (nxt_state, to_pop, to_push)}
        self.__transitions.append(state_trans)

    # override
    def get_next_trans(self, input_char: str, stack: list[str]) -> PushdownState:
        # print(f"Current State: {self.get_stateName()}, Input: {input_char}, Stack Before: {stack}")
        for trans in self.__transitions:
            if input_char in trans:
                nxt_state, to_pop, to_push = trans[input_char]
                # print(f"Transition Found: {input_char} -> {nxt_state.get_stateName()}, Pop: {to_pop}, Push: {to_push}")

                # Handle stack operations
                if to_pop and (not stack or stack[-1] != to_pop):
                    raise ValueError(f"Invalid transition: Stack top {stack[-1] if stack else None} != {to_pop}")

                if to_pop:
                    stack.pop()
                
                if to_push:
                    stack.append(to_push)
                
                print(f"Stack After: {stack}")
                return nxt_state
    
        raise ValueError(f"Did not find next transition for input {input_char}")

    def display_transition(self) -> None:
        if super().isInitState():
            print(f" -{super().get_stateName()} | ", end="")
        elif super().isFinalState():
            print(f" +{super().get_stateName()} | ", end="")
        else:
            print(f"  {super().get_stateName()} | ", end="")

        for trans in self.__transitions:
            for key, value in trans.items():
                nxt_state, to_pop, to_push = value
                print(f" {key} -> {nxt_state.get_stateName()} [pop: {to_pop}, push: {to_push}] | ", end="")
    
