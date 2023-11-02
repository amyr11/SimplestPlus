from simplestplus.utils import StateMachine
from simplestplus.utils import Lexer

class SimplestplusLexer(Lexer):
    def __init__(self):
        num_deci_literal = StateMachine(
            'num_deci_literal',
            transitions={
                (0, 'digits'): 1,
                (1, 'delim_1'): 2,
                (1, 'all_digits'): 3,
                (1, '.'): 6,
                (3, 'delim_1'): 4,
                (3, '.'): 6,
                (6, 'all_digits'): 7,
                (7, 'delim_1'): 8,
                (0, '0'): 11,
                (11, 'delim_1'): 12,
            },
            initial=0,
            final={2, 4, 8, 12}
        )

        reserved_symbols = StateMachine(
            'reserved_symbols',
            transitions={
                (0, 'delim_1'): 9,
                (9, 'delim_2'): 10,
            },
            initial=0,
            final={10}
        )

        reserved_words = StateMachine(
            'reserved_words',
            transitions={
                (0, 'a'): 1,
                (1, 'n'): 2,
                (2, 'd'): 3,
                (3, 'delim_1'): 4,
            },
            initial=0,
            final={4}
        )

        word_literal = StateMachine(
            'word_literal',
            transitions={
                (0, '"'): 1,
                (1, 'all_alpha'): 1,
                (1, ' '): 1,
                (1, '"'): 2,
                (1, '\\'): 4,
                (4, '"'): 5,
                (5, 'all_alpha'): 1,
                (5, ' '): 1,
                (5, '"'): 2,
                (2, 'delim_1'): 3,
            },
            initial=0,
            final={3}
        )
        super().__init__([num_deci_literal, reserved_symbols, reserved_words, word_literal])
