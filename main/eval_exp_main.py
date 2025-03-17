from src.finite_automata.fa import PushDown
from typing import Tuple, List


def _init_trans_table() -> List[List[Tuple[str, str, str, str]]] :

    init_transition_table: List[List[Tuple[str, str, str, str]]] = [
        
        # state q0
        [
            ("0", "q3", "e", "e"), ("1", "q3", "e", "e"), ("2", "q3", "e", "e"), ("3", "q3", "e", "e"),   # integer
            ("4", "q3", "e", "e"), ("5", "q3", "e", "e"), ("6", "q3", "e", "e"), ("7", "q3", "e", "e"),  # integer
            ("8", "q3", "e", "e"), ("9", "q3"), # integer
            ("+", "q2", "e", "e"), ("-", "q2", "e", "e"), ("*", "q2", "e", "e"), ("/", "q2", "e", "e"), # operator
            ("(", "q1", "e", "("), (")", "q2", "e", "e") # parentheiss
        ],

        # state q1
        [
            ("0", "q3"), ("1", "q3"), ("2", "q3"), ("3", "q3"), ("4", "q3"), ("5", "q3"), # integer
            ("6", "q3"), ("7", "q3"), ("8", "q3"), ("9", "q3"), # integer
            ("+", "q4"), ("-", "q4"), ("*", "q4"), ("/", "q4"), # operator
            ("(", "q1"), (")", "q2") # parentheissq
        ],
        [],
        [],
        []
    ]


def main() -> None:
    


    input_alpha: List[str] = [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "+", "-", "/" ,"*", "^",
                "(", ")"
    ]

    stack_symbol: List[str] = ["(", ")"]


    pda: PushDown = PushDown()

    pda.init_automaton()
    
    
    pass
