from simplestplus.utils import StateMachine
from simplestplus.utils import Lexer

class SimplestplusLexer(Lexer):
    def __init__(self):
        reserved_symbols = StateMachine(
            'reserved_symbols',
            transitions={
                (0, ' '): 1,
                (1, 'delim_space'): 2,
                (0, '\n'): 3,
                (3, 'delim_newline'): 4,
            },
            initial=0,
            final={2, 4}
        )

        reserved_words = StateMachine(
            'reserved_words',
            transitions={
                (0, 'a'): 1,
                (1, 'n'): 2,
                (2, 'd'): 3,
                (3, 'delim_res_words'): 4,
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
                (2, 'delim_word'): 3,
            },
            initial=0,
            final={3}
        )
        super().__init__([reserved_symbols, reserved_words, word_literal])
