from src.finite_automata.fa import FinteAuPushDowntomata
from typing import Tuple, List


def _init_trans_table() -> List[List[Tuple[str, str, str, str]]] :

    init_transition_table: List[List[Tuple[str, str, str, str]]] = [
        
        # state q0
        [
            ("0", "q3"), ("1", "q3"), ("2", "q3"), ("3", "q3"), ("4", "q3"), ("5", "q3"), # integer
            ("6", "q3"), ("7", "q3"), ("8", "q3"), ("9", "q3"), # integer
            ("+", "q2"), ("-", "q2"), ("*", "q2"), ("/", "q2"), # operator
            ("(", "q1"), (")", "q2") # parentheiss
        ],

        # state q1
        [
            ("0", "q3"), ("1", "q3"), ("2", "q3"), ("3", "q3"), ("4", "q3"), ("5", "q3"), # integer
            ("6", "q3"), ("7", "q3"), ("8", "q3"), ("9", "q3"), # integer
            ("+", "q4"), ("-", "q4"), ("*", "q4"), ("/", "q4"), # operator
            ("(", "q1"), (")", "q2") # parentheiss
        ],
        [],
        [],
        []
    ]


def main() -> None:
    pass
