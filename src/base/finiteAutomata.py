from abc import ABC, abstractmethod

class BaseFiniteAutomata(ABC):

    @abstractmethod
    def validate_input_str(self, input_str: str) -> bool:
        pass


class BaseFiniteStateMachine(ABC):

    @abstractmethod
    def get_output(self, input_str: str) -> str:
        pass