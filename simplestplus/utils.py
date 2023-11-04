from simplestplus.regdef import definitions as default_defs


class Token:
    pass

class DefTranslator:
    def __init__(self, definitions: dict = default_defs):
        self.definitions = definitions

    def translate(self, inp):
        ids = {inp}
        for id, symbols in default_defs.items():
            if inp in symbols:
                ids.add(id)
        return ids

class StateMachine:
    def __init__(
            self,
            name: str = None,
            transitions: dict = None,
            initial: int = None,
            final: int = None
    ):
        self.name = name
        self.transitions = transitions
        self.initial = initial
        self.final = final

    def tokenize(self, inp, translator = DefTranslator()):
        machine = self
        state = machine.initial
        tmp_inp = inp + '\n'
        val = ''

        while tmp_inp != '':
            cur_char = tmp_inp[0]
            val += cur_char
            
            assert translator is not None, 'Translator can\'t be None'
            ids = translator.translate(cur_char)
            new_state = machine._next(state, ids)

            if new_state is None:
                break
            else:
                if isinstance(new_state, tuple):
                    machine = new_state[0]
                    new_state = new_state[1]

                if new_state in machine.final:
                    val = val[:-1]
                    token = val
                    return token, val

            state = new_state
            tmp_inp = tmp_inp[1:]
        
        # if val[-1] == '\n':
        #     val = val[:-1]
        # elif val[0] == '\n':
        #     val = val[1:]

        return None, val

    def _next(self, state, ids):
        new_state = None

        for id in ids:
            try:
                new_state = self.transitions[(state, id)]
            except:
                continue

            if new_state is not None:
                break

        return new_state
    
class Error:
    def __init__(self, code, val, row, col, message):
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
    def __init__(self, code, val, row, col):
        super().__init__(code, val, row, col, f'LexicalError: Invalid lexeme {repr(val)} at ln {row}, col {col}')

class Lexer:
    def __init__(self, state_machines: list, translator: DefTranslator = DefTranslator()):
        self.state_machines = state_machines
        self.translator = translator

    def tokenize(self, inp):
        tokens = []
        row = col = 1
        cursor = 0

        while cursor < len(inp):
            token = None
            val = ''
            tmp_inp = inp[cursor:]

            tmp_vals = []
            for machine in self.state_machines:
                token, val = machine.tokenize(tmp_inp, self.translator)
                if token is not None:
                    break
                else:
                    tmp_vals.append(val)

            if token is None:
                val = max(tmp_vals, key=len)
                if val[-1] == '\n':
                    val = val[-1]
                elif val[0] == '\n':
                    row += 1
                    col = 1
                    val = val[1:]
                return None, LexicalError(inp, val, row, col)
            
            if val == '\n':
                row += 1
                col = 1
            else:
                col += len(val)

            cursor += len(val)
            tokens.append(token)

        return tokens, None
