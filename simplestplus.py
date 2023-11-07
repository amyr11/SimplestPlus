from enum import Enum
from optparse import Option
from typing import Optional


"""
-------------------
REGULAR DEFINITIONS
-------------------
"""

definitions = {}

definitions['all_alpha'] = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
definitions['digits'] = list('123456789')
definitions['all_digits'] = definitions['digits'] + ['0']
definitions['all_id'] = definitions['all_alpha'] + definitions['all_digits'] + ['_']

definitions['delim_space'] = definitions['all_alpha'] + ['"', '>', '+', ' ', '\n']
definitions['delim_indent'] = definitions['all_alpha'] + ['\n']
definitions['delim_newline'] = definitions['all_alpha'] + ['\n', ' ']
definitions['delim_res_words'] = [' ', '\n']
definitions['delim_word'] = definitions['delim_res_words']
definitions['delim_id'] = [' ', '\n', '+']
definitions['delim_gt'] = [' ', '\n']
definitions['delim_gte'] = [' ', '\n']
definitions['delim_plus'] = definitions['all_alpha'] + [' ', '\n']

class DefTranslator:
    def __init__(self, definitions: dict[str, list[str]] = definitions):
        self.definitions = definitions

    def translate(self, inp) -> set[str]:
        ids = {inp}
        for id, symbols in definitions.items():
            if inp in symbols:
                ids.add(id)
        return ids


"""
------
TOKENS
------
"""

class TokenType(Enum):
    GT = 'GREATER_THAN'
    GTE = 'GREATER_THAN_OR_EQUAL'
    IDENTIFIER = 'IDENTIFIER'
    WORD_LITERAL = 'WORD_LITERAL'
    SPACE = 'SPACE'
    NEWLINE = 'NEWLINE'
    AND = 'AND'
    PLUS = 'PLUS'


class Token:
    def __init__(self, t_type: TokenType, t_val: str):
        self.type = t_type
        self.val = t_val
        self._row = None
        self._col = None

    def __repr__(self) -> str:
        return f'Lexeme: {repr(self.val)}\nToken: {self.type}'

    def set_position(self, row, col):
        self._row = row
        self._col = col

    def get_position(self) -> tuple[int, int]:
        if self._row is None or self._col is None:
            raise ValueError('Token position not defined')
        
        return self._row, self._col

"""
------
ERRORS
------
"""
    
class Error:
    def __init__(self, code: str, row: int, col: int, message:str):
        self.code = code
        self.row = row
        self.col = col
        self.message = message

    def _code_error_string(self) -> str:
        split = self.code.split('\n')
        out = ''
        top = self.row > 3
        start = self.row - 3 if top else 0
        len_last_row_no = len(str(self.row)) if self.row > 100 else 3
        if top:
            out += ' '*3 + '...\n'
        for i in range(start, self.row):
            line = split[i]
            cur_row = i+1
            len_cur_row_no = len(str(cur_row))
            len_space = len_last_row_no - len_cur_row_no
            if cur_row == self.row:
                tmp_out = '-> ' + ' '*len_space + str(cur_row) + ' '*2
                out += tmp_out
                out += line + '\n'
                out += ' '*(len(tmp_out)+self.col-1) + '^' + '\n'
            else:
                out += '   ' + ' '*len_space + str(cur_row) + ' '*2
                out += line + '\n'
        return out
    
    def as_string(self) -> str:
        out = self._code_error_string()
        out += '-'*len(self.message) + '\n' + self.message + '\n'
        return out


class LexicalError(Error):
    def __init__(self, code: str, row: int, col: int):
        super().__init__(code, row, col, f'LexicalError: Unexpected character at ln {row}, col {col}')


class TokenError(Error):
    def __init__(self, code: str, row: int, col: int, token: Token):
        super().__init__(code, row, col, f'TokenError: Invalid {token.type.value} token `{token.val}` at ln {row}, col {col}')


"""
-------------
STATE MACHINE
-------------
"""

class StateMachine:
    def __init__(self, initial: int, transitions: dict, final: dict, fallback: Optional['StateMachine'] = None):
        self.initial = initial
        self.final = final
        self.transitions = transitions
        self.fallback = fallback
    
    def tokenize_first(self, code, translator = DefTranslator()) -> tuple[Optional[Token], str]:
        machine = self
        state = machine.initial
        tmp_code = code + '\n'
        token = None
        val = ''
        cur_char = ''

        while tmp_code != '' and code != '':
            cur_char = tmp_code[0]
            
            assert translator is not None, "Translator can't be None"
            ids = translator.translate(cur_char)
            new_state = machine._next(state, ids)

            if new_state is None:
                break

            if isinstance(new_state, tuple):
                machine = new_state[0]
                new_state = new_state[1]
            
            state = new_state
            tmp_code = tmp_code[1:]
            val += cur_char
        
        if state in self.final.keys():
            final_state = self.final[state]
            if final_state.retract:
                val = val[:-1]
            token = Token(final_state.token_type, val)
        else:
            val += cur_char


        return token, val
    
    def _next(self, state, ids) -> Optional[int]:
        for id in ids:
            try:
                next_state = self.transitions[(state, id)]
                if next_state is not None:
                    return next_state
            except:
                continue
        
        return None

    def is_accepting_char(self, char) -> bool:
        translator = DefTranslator()
        ids = translator.translate(char)

        for id in ids:
            try:
                self.transitions[(self.initial, id)]
                if self.transitions[(self.initial, id)] is not None:
                    return True
            except:
                continue
        
        return False


class MachineGroup:
    def __init__(self, machines: list[StateMachine]):
        self.machines = machines
    
    def get_machine(self, char) -> Optional[StateMachine]:
        for machine in self.machines:
            if machine.is_accepting_char(char):
                return machine
        
        return None
    
    def tokenize_first(self, code) -> tuple[Optional[Token], str]:
        token = None
        val = ''
        machine = self.get_machine(code)
        
        if machine is not None:
            token, val = machine.tokenize_first(code)

        return token, val


class FinalState:
    def __init__(self, token_type: TokenType, retract: bool = True):
        self.token_type = token_type
        self.retract = retract

"""
----------------
LEXICAL ANALYZER
----------------
"""

class Lexer:
    def __init__(self):
        self._identifiers_machine = StateMachine(
            initial = 0,
            final = {
                2: FinalState(TokenType.IDENTIFIER)
            },
            transitions = {
                (0, 'all_alpha'): 1,
                (1, 'all_id'): 1,
                (1, 'delim_id'): 2,
            }
        )

        self._reserved_words_machine = StateMachine(
            initial = 0,
            final = {
                4: FinalState(TokenType.AND)
            },
            transitions = {
                (0, 'a'): 1,
                (1, 'n'): 2,
                (2, 'd'): 3,
                (3, 'delim_res_words'): 4
            },
            fallback = self._identifiers_machine
        )

        self._reserved_symbols_machine = StateMachine(
            initial = 0,
            final = {
                2: FinalState(TokenType.GT),
                4: FinalState(TokenType.GTE),
                6: FinalState(TokenType.SPACE),
                8: FinalState(TokenType.PLUS),
                10: FinalState(TokenType.NEWLINE),
            },
            transitions = {
                (0, '>'): 1,
                (1, 'delim_gt'): 2,
                (1, '='): 3,
                (3, 'delim_gte'): 4,

                (0, ' '): 5,
                (5, 'delim_space'): 6,

                (0, '+'): 7,
                (7, 'delim_plus'): 8,

                (0, '\n'): 9,
                (9, 'delim_newline'): 10
            },
        )

        self._machines = MachineGroup([
            self._reserved_words_machine,
            self._identifiers_machine,
            self._reserved_symbols_machine
        ])

    def tokenize(self, code) -> tuple[list[Token], Optional[Error]]:
        def advance(val, row, col, cursor):
            for char in val:
                if char == '\n':
                    row += 1
                    col = 1
                else:
                    col += 1
                cursor += 1
            return row, col, cursor

        tokens = []

        # Preprocess
        preprocessed_code = self._preprocess(code)

        # Tokenize code
        tmp_code = preprocessed_code
        cursor = 0
        row = 1
        col = 1

        while cursor < len(code):
            tmp_code = code[cursor:]
            cur_char = tmp_code[0]
            token = None
            val = ''
            
            machine = self._machines.get_machine(cur_char)

            if machine is None:
                    return tokens, LexicalError(code, row, col)
            
            while token is None and machine is not None:
                token, val = machine.tokenize_first(tmp_code)
                machine = machine.fallback

            if token is None:
                row, col, cursor = advance(val, row, col, cursor)
                col -= 1
                
                return tokens, LexicalError(code, row, col)
            
            row, col, cursor = advance(val, row, col, cursor)

            token.set_position(row, col - len(token.val))

            # Verify token according to rules
            token_valid = self._verify_token(token)

            if not token_valid:
                t_row, t_col = token.get_position()
                return tokens, TokenError(code, t_row, t_col, token)
            
            tokens.append(token)

        return tokens, None

    def _preprocess(self, code) -> str:
        # TODO: Lexer's _preprocess
        preprocessed_code = code

        # Remove trailing whitespace per line

        return preprocessed_code
    
    def _verify_token(self, token) -> bool:
        # TODO: Lexer's _is_token_valid
        reserved_words = ['and']

        if token.type == TokenType.IDENTIFIER and token.val in reserved_words:
            return False
        
        return True