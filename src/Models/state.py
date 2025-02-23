from __future__ import annotations

class State():

    __state_name: str
    __isFinalState: bool | None
    __isInitState: bool
    __transitions: list[dict[str, State]]
    # __state_output: str | None

    def __init__(self, state_name: str, isInitState: bool, 
                 isFinalState: bool | None = None):
        self.__state_name = state_name
        self.__isInitState = isInitState
        self.__isFinalState = isFinalState
        self.__transitions = list(dict())
        # self.__state_output = state_output

    def __str__(self) -> str:
        return self.__state_name

    def get_stateName(self) -> str:
        return self.__state_name
    
    def isFinalState(self) -> bool:
        return self.__isFinalState
    
    def isInitState(self) -> bool:
        return self.__isInitState

    def add_transition(self, state: State, input: str) -> None:
        state_dict: dict[str, State] = {input : state}
        self.__transitions.append(state_dict)

    
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

                