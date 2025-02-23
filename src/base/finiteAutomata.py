from abc import ABC, abstractmethod

class BaseFiniteAutomata(ABC):

    @abstractmethod
    def validate_input_str(self, input: str) -> bool:
        pass


class BaseFiniteStateMachine(ABC):

    @abstractmethod
    def get_output(self, input: str) -> str:
        pass