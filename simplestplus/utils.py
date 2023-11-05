from ctypes import Union
from simplestplus.regdef import definitions as default_defs


class Token:
    def __init__(self, kind, token, val):
        self.kind = kind
        self.token = token
        self.val = val

    def __repr__(self):
        return f'{self.token}: {repr(self.val)}'

class DefTranslator:
    def __init__(self, definitions: dict = default_defs):
        self.definitions = definitions

    def translate(self, inp):
        ids = {inp}
        for id, symbols in default_defs.items():
            if inp in symbols:
                ids.add(id)
        return ids

# class StateMachine:
#     def __init__(
#             self,
#             transitions: dict,
#             initial: int,
#             final: set[int],
#             name: str = '',
#     ):
#         self.name = name
#         self.transitions = transitions
#         self.initial = initial
#         self.final = final

#     def tokenize(self, inp, translator = DefTranslator()):
#         machine = self
#         state = machine.initial
#         tmp_inp = inp + '\n'
#         val = ''

#         while tmp_inp != '':
#             cur_char = tmp_inp[0]
#             val += cur_char
            
#             assert translator is not None, 'Translator can\'t be None'
#             ids = translator.translate(cur_char)
#             new_state = machine._next(state, ids)

#             if new_state is None:
#                 break
#             else:
#                 if isinstance(new_state, tuple):
#                     machine = new_state[0]
#                     new_state = new_state[1]

#                 if new_state in machine.final:
#                     val = val[:-1]
#                     token = val
#                     return token, val

#             state = new_state
#             tmp_inp = tmp_inp[1:]

#         return None, val

#     def _next(self, state, ids):
#         new_state = None

#         for id in ids:
#             try:
#                 new_state = self.transitions[(state, id)]
#             except:
#                 continue

#             if new_state is not None:
#                 break

#         return new_state

class StateMachine:
    def __init__(
            self,
            transitions: dict,
            initial: int,
            name: str = '',
    ):
        self.name = name
        self.transitions = transitions
        self.initial = initial

    def tokenize(self, code, translator = DefTranslator()):
        tmp_inp = code + '\n'
        machine = self
        state = machine.initial
        token = None
        val = ''

        while tmp_inp != '':
            cur_char = tmp_inp[0]
            val += cur_char
            
            assert translator is not None, 'Translator can\'t be None'

            ids = translator.translate(cur_char)
            new_state, new_token = machine._next(state, ids)

            if new_state is None:
                break
            elif isinstance(new_state, tuple):
                machine = new_state[0]
                state = new_state[1]
            else:
                state = new_state
            
            token = new_token
            tmp_inp = tmp_inp[1:]
        
        if token:
            val = val[:-2]
            return Token(machine.name, token, val), val, machine

        return None, val, machine

    def _next(self, state, ids):
        if state in self.transitions:
            state_dict = self.transitions[state]
            for id in ids:
                if id in state_dict:
                    next_state, token = state_dict[id]
                    return next_state, token
        return None, None
    
class Error:
    def __init__(self, code: str, val: str, row: int, col: int, message:str):
        self.code = code
        self.val = val
        self.row = row
        self.col = col
        self.message = message

    def _code_error_string(self):
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
                out += ' '*(len(tmp_out)+self.col-1) + '~'*(len(self.val)) + '\n'
            else:
                out += '   ' + ' '*len_space + str(cur_row) + ' '*2
                out += line + '\n'
        return out
    
    def as_string(self):
        out = self._code_error_string()
        out += '-'*len(self.message) + '\n' + self.message + '\n'
        return out

class LexicalError(Error):
    def __init__(self, code: str, val: str, row: int, col: int, machine_name: str):
        super().__init__(code, val, row, col, f'LexicalError: Invalid {machine_name} `{val}` at ln {row}, col {col}')

class Lexer:
    def __init__(self, state_machine: StateMachine, translator: DefTranslator = DefTranslator()):
        self.state_machine = state_machine
        self.translator = translator

    def tokenize(self, inp):
        tokens = []
        row = col = 1
        cursor = 0

        while cursor < len(inp):
            token = None
            val = ''
            tmp_inp = inp[cursor:]

            token, val, machine = self.state_machine.tokenize(tmp_inp, self.translator)

            if token is None:
                if val[-1] == '\n':
                    val = val[:-1]
                elif val[0] == '\n':
                    row += 1
                    col = 1
                    val = val[1:]
                return tokens, LexicalError(inp, val, row, col, machine.name)
            
            if val == '\n':
                row += 1
                col = 1
            else:
                col += len(val)

            cursor += len(val)
            tokens.append(token)

        return tokens, None
