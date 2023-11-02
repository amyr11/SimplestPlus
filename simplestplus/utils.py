from simplestplus.regdef import definitions as default_defs


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

    def run(self, inp, translator = DefTranslator()):
        machine = self
        state = machine.initial
        tmp_inp = inp + '\n'
        val = ''

        if tmp_inp[0] in ['\n', ' ']:
            return tmp_inp[0], tmp_inp[0]

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

class Lexer:
    def __init__(self, state_machines: list, translator: DefTranslator = DefTranslator()):
        self.state_machines = state_machines
        self.translator = translator

    def analyze(self, inp):
        tokens = []
        row = col = 1
        cursor = 0

        while cursor < len(inp):
            token = None
            val = ''
            tmp_inp = inp[cursor:]

            tmp_vals = []
            for machine in self.state_machines:
                token, val = machine.run(tmp_inp, self.translator)
                if token is not None:
                    break
                else:
                    tmp_vals.append(val)

            if token is None:
                val = max(tmp_vals, key=len)
                return tokens, Lexer.display_code_error(f'LexicalError: Invalid lexeme near line {row}, col {col}', inp, row, col, len(val))
            
            if val == '\n':
                row += 1
                col = 1
            else:
                col += len(val)

            cursor += len(val)
            tokens.append(token)

        return tokens, None

    @staticmethod
    def display_code_error(message, inp, row, col, lex_len):
        split = inp.split('\n')
        out = ''
        top = row > 3
        start = row - 3 if top else 0
        len_last_row_no = len(str(row)) if row > 100 else 3
        if top:
            out += ' '*3 + '...\n'
        for i in range(start, row):
            line = split[i]
            cur_row = i+1
            len_cur_row_no = len(str(cur_row))
            len_space = len_last_row_no - len_cur_row_no
            if cur_row == row:
                tmp_out = '-> ' + ' '*len_space + str(cur_row) + ' '*2
                out += tmp_out
                out += line + '\n'
                out += ' '*(len(tmp_out)+col-1) + '~'*lex_len + '\n'
            else:
                out += '   ' + ' '*len_space + str(cur_row) + ' '*2
                out += line + '\n'
        out += '-'*len(message) + '\n' + message + '\n'
        return out
