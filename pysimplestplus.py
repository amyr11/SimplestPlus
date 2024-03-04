#######################################
# CONSTANTS
#######################################


TAB_COUNT = 4
S_COMMENT_LIMIT = 79
ID_LIMIT = 20
NUM_LIMIT = 999999999
DECI_LIMIT = 999999999.999999
DECI_PRECISION_LIMIT = 6
WORD_ESCAPE_CHARS = {
            'n': '\n',
            't': '\t',
            '"': '\"',
            '\\': '\\',
        }
LETTER_ESCAPE_CHARS = {
            'n': '\n',
            't': '\t',
            "'": '\'',
            '\\': '\\',
        }

def without(list, chars):
    return [char for char in list if char not in chars]


DEFINITIONS = {}

# Sets
DEFINITIONS["digits"] = list("123456789")
DEFINITIONS["all_digits"] = [*DEFINITIONS["digits"], "0"]
DEFINITIONS["all_alpha"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
DEFINITIONS["alpha_num"] = [*DEFINITIONS["all_alpha"], *DEFINITIONS["all_digits"]]
DEFINITIONS["arith_op"] = ["+", "-", "*", "/", "%"]
DEFINITIONS["rel_op"] = ["=", "!", ">", "<"]
DEFINITIONS["special_char"] = [
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    '"',
    "#",
    "$",
    "&",
    "'",
    "(",
    ")",
    ",",
    ".",
    ":",
    ";",
    "?",
    "@",
    "[",
    "\\",
    "\t",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    "±",
    "§",
]
DEFINITIONS["special_char_wo_t"] = without(DEFINITIONS["special_char"], ["\t"])
DEFINITIONS["special_char_wo_t_sq"] = without(DEFINITIONS["special_char_wo_t"], ["'"])
DEFINITIONS["special_char_wo_dq"] = without(DEFINITIONS["special_char"], ['"'])
DEFINITIONS["special_char_wo_bs"] = without(DEFINITIONS["special_char"], ["\\"])
DEFINITIONS["special_char_wo_sq"] = without(DEFINITIONS["special_char"], ["'"])
DEFINITIONS["all_id"] = [*DEFINITIONS["alpha_num"], "_"]
DEFINITIONS["all_word"] = [
    *DEFINITIONS["alpha_num"],
    *DEFINITIONS["special_char_wo_dq"],
    " ",
]
DEFINITIONS["all_letter"] = [
    *DEFINITIONS["alpha_num"],
    *without(DEFINITIONS["special_char_wo_bs"], ["'"]),
    " ",
]
DEFINITIONS["all_s_com"] = [
    *DEFINITIONS["all_word"],
    '"',
]
DEFINITIONS["all_word_wo_bs"] = without(DEFINITIONS["all_word"], ["\\"])
DEFINITIONS["all_mul_com"] = [
    *DEFINITIONS["alpha_num"],
    *DEFINITIONS["special_char_wo_sq"],
    " ",
    "\n",
]
DEFINITIONS["all_mul_com_wo_t"] = without(DEFINITIONS["all_mul_com"], ["\t"])

# Delims
DEFINITIONS["delim_word"] = [" ", "\n", ",", "]", ")", "}", "+", ":", "#", "!", "=", ".", "["]
DEFINITIONS["delim_dtype"] = [" ", "(", "[", "]", ","]
DEFINITIONS["delim_break"] = [" ", "\n"]
DEFINITIONS["delim_value"] = [" ", "\n", ")", "]", "}", ",", ":", "."]
DEFINITIONS["delim_indent"] = [
    *DEFINITIONS["all_alpha"],
    " ",
    "#",
    "'",
    '"',
    "}",
    "]",
    "{",
    ")",
]
DEFINITIONS["delim_arith"] = [*DEFINITIONS["alpha_num"], " ", "(", "-"]
DEFINITIONS["delim_plus"] = [*DEFINITIONS["alpha_num"], " ", "(", "-", '"', "'", "["]
DEFINITIONS["delim_minus"] = DEFINITIONS["delim_arith"]
DEFINITIONS["delim_assign"] = [*DEFINITIONS["alpha_num"], " ", "(", "-", '"', "{", "[", "'"]
DEFINITIONS["delim_opar"] = [
    *DEFINITIONS["alpha_num"],
    " ",
    "(",
    "-",
    '"',
    "'",
    "[",
    "{",
    "(",
    ")",
    "\n",
]
DEFINITIONS["delim_cpar"] = [
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    " ",
    "\n",
    ":",
    ")",
    "(",
    ",",
    "]",
    "[",
    "}",
    "#",
    ".",
]
DEFINITIONS["delim_obrace"] = [*DEFINITIONS["alpha_num"], " ", "\n", '"', "'", "}"]
DEFINITIONS["delim_cbrace"] = [" ", "\n", ",", "}", ")", "]", "."]
DEFINITIONS["delim_obrack"] = [
    *DEFINITIONS["alpha_num"],
    " ",
    "\n",
    "-",
    "(",
    "{",
    "[",
    "]",
    '"',
    "'",
]
DEFINITIONS["delim_cbrack"] = [" ", "\n", ",", "[", "]", ")", "}", ".", "(", "+", ":"]
DEFINITIONS["delim_comma"] = [
    *DEFINITIONS["alpha_num"],
    " ",
    "(",
    "-",
    '"',
    "'",
    "[",
    "{",
    "(",
    ")",
    "#",
    "\n",
]
DEFINITIONS["delim_period"] = DEFINITIONS["all_alpha"]
DEFINITIONS["delim_id"] = [
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    " ",
    "\n",
    "(",
    "[",
    ")",
    "]",
    "}",
    ",",
    ".",
    ":",
    "#",
]
DEFINITIONS["delim_num_deci"] = [
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    " ",
    ",",
    "}",
    ")",
    "]",
    ":",
    "#",
    '"',
    "\n",
]
DEFINITIONS["delim_reserve"] = [" "]
DEFINITIONS["delim_colon"] = [":"]
DEFINITIONS["delim_func"] = ["("]
DEFINITIONS["delim_comment"] = ["\n"]
DEFINITIONS["delim_access"] = ["."]


DEFINITIONS["delim_tab"] = [
    "\t",
    "\n",
    *DEFINITIONS["alpha_num"],
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    *DEFINITIONS["special_char"],
]

DEFINITIONS["delim_space"] = [
    *DEFINITIONS["alpha_num"],
    *DEFINITIONS["arith_op"],
    *DEFINITIONS["rel_op"],
    *DEFINITIONS["special_char_wo_t"],
    " ",
    "\n",
]


#######################################
# POSITION
#######################################


class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        if current_char == "\n":
            self.idx += 1
            self.ln += 1
            self.col = 0
        elif current_char == "\t":
            self.idx += 1
            self.col += TAB_COUNT
        else:
            self.idx += 1
            self.col += 1

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


#######################################
# TOKENS
#######################################

TT_EOF = "\\0"
TT_AND = "and"
TT_BACK = "back"
TT_BLANK = "blank"
TT_CHOICE = "choice"
TT_COLLECTION = "collection"
TT_DECI = "deci"
TT_DEFAULT = "default"
TT_DEL = "del"
TT_DURING = "during"
TT_EMPTY = "empty"
TT_EVENT = "event"
TT_EVERY = "every"
TT_FROZEN = "frozen"
TT_GIVEN = "given"
TT_GLOBAL = "global"
TT_GO = "go"
TT_GROUP = "group"
TT_HIDDEN = "hidden"
TT_HOME = "home"
TT_IN = "in"
TT_INCASE = "incase"
TT_INHERITS = "inherits"
TT_INSTEAD = "instead"
TT_NEW = "new"
TT_NO = "no"
TT_NOT = "not"
TT_NUM = "num"
TT_OR = "or"
TT_RESTRICTED = "restricted"
TT_SKIP = "skip"
TT_STOP = "stop"
TT_UNLESS = "unless"
TT_VISIBLE = "visible"
TT_WIKI = "wiki"
TT_WORD = "word"
TT_YES = "yes"
TT_IDENTIFIER = "id"
TT_SPACE = "space"
TT_TAB = "\\t"
TT_NEWLINE = "\\n"
TT_MULTIPLY = "*"
TT_MULTIPLY_ASSIGN = "*="
TT_POWER = "**"
TT_POWER_ASSIGN = "**="
TT_PLUS = "+"
TT_PLUS_ASSIGN = "+="
TT_MINUS = "-"
TT_MINUS_ASSIGN = "-="
TT_DIVIDE = "/"
TT_DIVIDE_ASSIGN = "/="
TT_FLOOR = "//"
TT_FLOOR_ASSIGN = "//="
TT_MODULO = "%"
TT_MODULO_ASSIGN = "%="
TT_ASSIGN = "="
TT_EQUAL_TO = "=="
TT_NOT_EQUAL = "!="
TT_GREATER_THAN = ">"
TT_GREATER_THAN_EQUAL = ">="
TT_LESS_THAN = "<"
TT_LESS_THAN_EQUAL = "<="
TT_LETTER = "letter"
TT_OPAR = "("
TT_CPAR = ")"
TT_OBRACE = "{"
TT_CBRACE = "}"
TT_OBRACK = "["
TT_CBRACK = "]"
TT_COMMA = ","
TT_PERIOD = "."
TT_COLON = ":"
TT_WORD_LITERAL = "word_lit"
TT_LETTER_LITERAL = "letter_lit"
TT_NUM_LITERAL = "num_lit"
TT_DECI_LITERAL = "deci_lit"
TT_S_COMMENT = "s_comment"
TT_M_COMMENT = "m_comment"

KEYWORDS = [
    TT_AND,
    TT_BACK,
    TT_BLANK,
    TT_CHOICE,
    TT_COLLECTION,
    TT_DECI,
    TT_DEFAULT,
    TT_DEL,
    TT_DURING,
    TT_EMPTY,
    TT_EVENT,
    TT_EVERY,
    TT_FROZEN,
    TT_GIVEN,
    TT_GLOBAL,
    TT_GO,
    TT_GROUP,
    TT_HIDDEN,
    TT_HOME,
    TT_IN,
    TT_INCASE,
    TT_INHERITS,
    TT_INSTEAD,
    TT_LETTER,
    TT_NEW,
    TT_NO,
    TT_NOT,
    TT_NUM,
    TT_OR,
    TT_RESTRICTED,
    TT_SKIP,
    TT_STOP,
    TT_UNLESS,
    TT_VISIBLE,
    TT_WIKI,
    TT_WORD,
    TT_YES,
]

DELIM_MAP = {
    TT_IDENTIFIER: DEFINITIONS["delim_id"],
    TT_SPACE: DEFINITIONS["delim_space"],
    TT_TAB: DEFINITIONS["delim_tab"],
    TT_NEWLINE: None,
    TT_MULTIPLY: DEFINITIONS["delim_arith"],
    TT_MULTIPLY_ASSIGN: DEFINITIONS["delim_arith"],
    TT_POWER: DEFINITIONS["delim_arith"],
    TT_POWER_ASSIGN: DEFINITIONS["delim_arith"],
    TT_PLUS: DEFINITIONS["delim_plus"],
    TT_PLUS_ASSIGN: DEFINITIONS["delim_plus"],
    TT_MINUS: DEFINITIONS["delim_minus"],
    TT_MINUS_ASSIGN: DEFINITIONS["delim_arith"],
    TT_DIVIDE: DEFINITIONS["delim_arith"],
    TT_DIVIDE_ASSIGN: DEFINITIONS["delim_arith"],
    TT_FLOOR: DEFINITIONS["delim_arith"],
    TT_FLOOR_ASSIGN: DEFINITIONS["delim_arith"],
    TT_MODULO: DEFINITIONS["delim_arith"],
    TT_MODULO_ASSIGN: DEFINITIONS["delim_arith"],
    TT_ASSIGN: DEFINITIONS["delim_assign"],
    TT_EQUAL_TO: DEFINITIONS["delim_plus"],
    TT_NOT_EQUAL: DEFINITIONS["delim_plus"],
    TT_GREATER_THAN: DEFINITIONS["delim_arith"],
    TT_GREATER_THAN_EQUAL: DEFINITIONS["delim_arith"],
    TT_LESS_THAN: DEFINITIONS["delim_arith"],
    TT_LESS_THAN_EQUAL: DEFINITIONS["delim_arith"],
    TT_LETTER: DEFINITIONS["delim_dtype"],
    TT_LETTER_LITERAL: DEFINITIONS["delim_word"],
    TT_OPAR: DEFINITIONS["delim_opar"],
    TT_CPAR: DEFINITIONS["delim_cpar"],
    TT_OBRACE: DEFINITIONS["delim_obrace"],
    TT_CBRACE: DEFINITIONS["delim_cbrace"],
    TT_OBRACK: DEFINITIONS["delim_obrack"],
    TT_CBRACK: DEFINITIONS["delim_cbrack"],
    TT_COMMA: DEFINITIONS["delim_comma"],
    TT_PERIOD: DEFINITIONS["delim_period"],
    TT_COLON: DEFINITIONS["delim_comma"],
    TT_WORD_LITERAL: DEFINITIONS["delim_word"],
    TT_NUM_LITERAL: DEFINITIONS["delim_num_deci"],
    TT_DECI_LITERAL: DEFINITIONS["delim_num_deci"],
    TT_S_COMMENT: DEFINITIONS["delim_comment"],
    TT_M_COMMENT: DEFINITIONS["delim_comment"],
    TT_AND: DEFINITIONS["delim_reserve"],
    TT_BACK: DEFINITIONS["delim_reserve"],
    TT_BLANK: DEFINITIONS["delim_value"],
    TT_CHOICE: DEFINITIONS["delim_dtype"],
    TT_COLLECTION: DEFINITIONS["delim_dtype"],
    TT_DECI: DEFINITIONS["delim_dtype"],
    TT_DEFAULT: DEFINITIONS["delim_colon"],
    TT_DEL: DEFINITIONS["delim_reserve"],
    TT_DURING: DEFINITIONS["delim_reserve"],
    TT_EMPTY: DEFINITIONS["delim_reserve"],
    TT_EVENT: DEFINITIONS["delim_reserve"],
    TT_EVERY: DEFINITIONS["delim_reserve"],
    TT_FROZEN: DEFINITIONS["delim_reserve"],
    TT_GIVEN: DEFINITIONS["delim_reserve"],
    TT_GLOBAL: DEFINITIONS["delim_reserve"],
    TT_GO: DEFINITIONS["delim_colon"],
    TT_GROUP: DEFINITIONS["delim_reserve"],
    TT_HIDDEN: DEFINITIONS["delim_reserve"],
    TT_HOME: DEFINITIONS["delim_func"],
    TT_IN: DEFINITIONS["delim_reserve"],
    TT_INCASE: DEFINITIONS["delim_reserve"],
    TT_INHERITS: DEFINITIONS["delim_reserve"],
    TT_INSTEAD: DEFINITIONS["delim_colon"],
    TT_NEW: DEFINITIONS["delim_reserve"],
    TT_NO: DEFINITIONS["delim_value"],
    TT_NOT: DEFINITIONS["delim_reserve"],
    TT_NUM: DEFINITIONS["delim_dtype"],
    TT_OR: DEFINITIONS["delim_reserve"],
    TT_RESTRICTED: DEFINITIONS["delim_reserve"],
    TT_SKIP: DEFINITIONS["delim_break"],
    TT_STOP: DEFINITIONS["delim_break"],
    TT_UNLESS: DEFINITIONS["delim_reserve"],
    TT_VISIBLE: DEFINITIONS["delim_reserve"],
    TT_WIKI: DEFINITIONS["delim_dtype"],
    TT_WORD: DEFINITIONS["delim_dtype"],
    TT_YES: DEFINITIONS["delim_value"],
}

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def lexeme_str(self):
        if self.value:
            return f"{repr(self.value)}"
        else:
            return f"{self.type}"

    def token_type_str(self):
        return f"{self.type}"

    def __repr__(self):
        if self.value:
            return f"{self.type}:{repr(self.value)}"
        return f"{self.type}"


#######################################
# ERRORS
#######################################


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        lineno = self.pos_start.ln + 1
        result = f'File "{self.pos_start.fn}", line {lineno}, col {self.pos_start.col + 1}\n'
        result += "\n" + self.string_with_arrows(
            self.pos_start.ftxt, self.pos_start, self.pos_end
        )
        result += f"\n\n{self.error_name}: {self.details}"
        return result

    def string_with_arrows(self, text, pos_start, pos_end):
        result = ""

        # Calculate indices
        idx_start = max(text.rfind("\n", 0, pos_start.idx), 0)
        idx_end = text.find("\n", idx_start + 1)
        if idx_end < 0:
            idx_end = len(text)

        # Generate each line
        line_count = pos_end.ln - pos_start.ln + 1
        for i in range(line_count):
            # Calculate line columns
            line = text[idx_start:idx_end]

            # Replace \t with spaces
            line = line.replace("\t", " "*TAB_COUNT)

            col_start = pos_start.col if i == 0 else 0
            col_end = pos_end.col if i == line_count - 1 else len(line) - 1

            # Append to result
            result += line + "\n"
            result += " " * col_start + "~" * (col_end - col_start)

            # Re-calculate indices
            idx_start = idx_end
            idx_end = text.find("\n", idx_start + 1)
            if idx_end < 0:
                idx_end = len(text)

        return result.replace("\t", "")


class LexicalError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "LexicalError", details)


class SyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=None):
        super().__init__(pos_start, pos_end, "SyntaxError", details)

class IndentationError(Error):
    def __init__(self, pos_start, pos_end, details=None):
        super().__init__(pos_start, pos_end, "IndentationError", details)


#######################################
# LEXER
#######################################


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.tokens = []
        self.errors = []
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = (
            self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
        )

    def check_delim(self, delim_of):
        delimiters = DELIM_MAP[delim_of]

        if delimiters is None:
            return None

        if self.current_char not in delimiters and self.current_char is not None:
            pos_start = self.pos.copy()
            pos_end = pos_start.copy().advance()
            return LexicalError(
                pos_start,
                pos_end,
                f"Unexpected delim {repr(self.current_char)} after {delim_of}",
            )

        return None

    def make_tokens(self):

        while self.current_char is not None:
            token = None

            if self.current_char == " ":
                token = Token(TT_SPACE, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "\t":
                token = Token(TT_TAB, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "\n":
                token = Token(TT_NEWLINE, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "*":
                token = self.make_asterisk()
            elif self.current_char == "+":
                token = self.make_plus()
            elif self.current_char == "-":
                token, error = self.make_minus()
                if error:
                    self.errors.append(error)
            elif self.current_char == "/":
                token = self.make_slash()
            elif self.current_char == "%":
                token = self.make_modulo()
            elif self.current_char == "=":
                token = self.make_equal()
            elif self.current_char == "!":
                token, error = self.make_not_equal()
                if error:
                    self.errors.append(error)
            elif self.current_char == ">":
                token = self.make_greater_than()
            elif self.current_char == "<":
                token = self.make_less_than()
            elif self.current_char == "(":
                token = Token(TT_OPAR, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == ")":
                token = Token(TT_CPAR, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "{":
                token = Token(TT_OBRACE, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "}":
                token = Token(TT_CBRACE, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "[":
                token = Token(TT_OBRACK, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "]":
                token = Token(TT_CBRACK, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == ",":
                token = Token(TT_COMMA, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == ".":
                token = Token(TT_PERIOD, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == ":":
                token = Token(TT_COLON, pos_start=self.pos.copy())
                self.advance()
            elif self.current_char == "#":
                token, error = self.make_s_comment()
                if error:
                    self.errors.append(error)
            elif self.current_char == "'":
                token, error = self.make_single_quote()
                if error:
                    self.errors.append(error)
            elif self.current_char in DEFINITIONS["all_alpha"]:
                token, error = self.make_keyword_or_id()
                if error:
                    self.errors.append(error)
            elif self.current_char == '"':
                token, error = self.make_word()
                if error:
                    self.errors.append(error)
            elif self.current_char in DEFINITIONS["all_digits"]:
                token, error = self.make_num_deci()
                if error:
                    self.errors.append(error)
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                self.errors.append(
                    LexicalError(
                        pos_start, self.pos.copy(), f"Illegal character {repr(char)}"
                    )
                )

            if token:
                error = self.check_delim(token.type)

                if error:
                    self.errors.append(error)
                else:
                    self.tokens.append(token)

        self.tokens.append(Token(TT_EOF, pos_start=self.pos))
        return self.tokens, self.errors

    def make_asterisk(self):
        tok_type = TT_MULTIPLY
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_MULTIPLY_ASSIGN
            self.advance()
        elif self.current_char == "*":
            tok_type = TT_POWER
            self.advance()
            if self.current_char == "=":
                tok_type = TT_POWER_ASSIGN
                self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_plus(self):
        tok_type = TT_PLUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_PLUS_ASSIGN
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_minus(self):
        tok_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char in DEFINITIONS["all_digits"] and not (self.tokens and self.tokens[-1].type in [TT_IDENTIFIER, TT_NUM_LITERAL, TT_DECI_LITERAL]):
            token, error = self.make_num_deci(neg=True)
            if error:
                return None, error

            if token and token.value == 0:
                return None, LexicalError(pos_start, self.pos.copy(), "Negative zero is not allowed")

            return token, None

        if self.current_char == "=":
            tok_type = TT_MINUS_ASSIGN
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos), None

    def make_slash(self):
        tok_type = TT_DIVIDE
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_DIVIDE_ASSIGN
            self.advance()
        elif self.current_char == "/":
            tok_type = TT_FLOOR
            self.advance()
            if self.current_char == "=":
                tok_type = TT_FLOOR_ASSIGN
                self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_modulo(self):
        tok_type = TT_MODULO
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_MODULO_ASSIGN
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_equal(self):
        tok_type = TT_ASSIGN
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_EQUAL_TO
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_not_equal(self):
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            return Token(TT_NOT_EQUAL, pos_start=pos_start, pos_end=self.pos), None

        return None, LexicalError(pos_start, self.pos.copy(), "Expected '=' after '!'")

    def make_greater_than(self):
        tok_type = TT_GREATER_THAN
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_GREATER_THAN_EQUAL
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_less_than(self):
        tok_type = TT_LESS_THAN
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == "=":
            tok_type = TT_LESS_THAN_EQUAL
            self.advance()

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_s_comment(self):
        pos_start = self.pos.copy()
        value = ""
        self.advance()

        while self.current_char is not None and self.current_char in DEFINITIONS["all_s_com"]:
            value += self.current_char
            self.advance()

        if len(value) == 0:
            return None, LexicalError(pos_start, self.pos.copy(), "Comments must have at least 1 character")
        elif len(value) > S_COMMENT_LIMIT:
            return None, LexicalError(pos_start, self.pos.copy(), f"Single-line comments can only have {S_COMMENT_LIMIT} characters")

        return Token(TT_S_COMMENT, value=value, pos_start=pos_start, pos_end=self.pos), None

    def make_single_quote(self):
        pos_start = self.pos.copy()
        value = ""

        s_quote_count = 0

        while self.current_char == "'" and s_quote_count < 3:
            s_quote_count += 1
            self.advance()

        if s_quote_count == 3:
            # Multi-line comment
            while True:
                while self.current_char is not None and self.current_char in DEFINITIONS["all_mul_com"]:
                    value += self.current_char
                    self.advance()

                s_quote_count = 0
                while self.current_char is not None and self.current_char == "'" and s_quote_count < 3:
                    s_quote_count += 1
                    self.advance()

                if s_quote_count == 3:
                    break
                elif s_quote_count < 3 and self.current_char in DEFINITIONS["all_mul_com"]:
                    value += "'" * s_quote_count
                    continue
                else:
                    return None, LexicalError(
                        pos_start,
                        self.pos.copy(),
                        "Unterminated comment",
                    )

            if len(value) == 0:
                return None, LexicalError(pos_start, self.pos.copy(), "Comments must have at least 1 character")

            return (
                Token(
                    TT_M_COMMENT, value=value, pos_start=pos_start, pos_end=self.pos
                ),
                None,
            )
        elif s_quote_count == 2:
            return (
                    Token(
                        TT_LETTER_LITERAL,
                        value=value,
                        pos_start=pos_start,
                        pos_end=self.pos,
                    ),
                    None,
                )
        else:
            # Letter literal
            if self.current_char is not None and self.current_char in DEFINITIONS["all_letter"]:
                value += self.current_char
                self.advance()

            if self.current_char == "\\":
                self.advance()
                if self.current_char in LETTER_ESCAPE_CHARS:
                    value += LETTER_ESCAPE_CHARS[self.current_char]
                    self.advance()

            if self.current_char == "'":
                self.advance()

                return (
                    Token(
                        TT_LETTER_LITERAL,
                        value=value,
                        pos_start=pos_start,
                        pos_end=self.pos,
                    ),
                    None,
                )
            else:
                return None, LexicalError(
                    pos_start, self.pos.copy(), "Unterminated letter literal"
                )

    def make_keyword_or_id(self):
        tok_type = TT_IDENTIFIER
        value = self.current_char or ""
        pos_start = self.pos.copy()
        self.advance()

        while self.current_char is not None and self.current_char in DEFINITIONS["all_id"]:
            value += self.current_char
            self.advance()

        for keyword in DELIM_MAP.keys():
            if value == keyword:
                tok_type = keyword
                return Token(tok_type, pos_start=pos_start, pos_end=self.pos), None

        if len(value) > ID_LIMIT:
            return None, LexicalError(pos_start, self.pos.copy(), f"Identifiers can only have {ID_LIMIT} characters")

        return Token(tok_type, value=value, pos_start=pos_start, pos_end=self.pos), None

    def make_word(self):
        pos_start = self.pos.copy()
        value = ''
        self.advance()

        while True:
            while self.current_char is not None and self.current_char in DEFINITIONS["all_word_wo_bs"]:
                value += self.current_char
                self.advance()

            if self.current_char == "\\":
                self.advance()
                if self.current_char in WORD_ESCAPE_CHARS:
                    value += WORD_ESCAPE_CHARS[self.current_char]
                    self.advance()
                    continue

            if self.current_char == '"':
                self.advance()
                break
            else:
                return None, LexicalError(
                    pos_start, self.pos.copy(), "Unterminated word literal"
                )

        return Token(TT_WORD_LITERAL, value=value, pos_start=pos_start, pos_end=self.pos), None

    def make_num_deci(self, neg=False):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in DEFINITIONS["all_digits"] + ['.']:
            if self.current_char == '.':
                dot_count += 1
            num_str += self.current_char
            self.advance()

        negative_val = -1 if neg else 1

        if dot_count == 0:
            num_val = int(num_str) * negative_val
            if num_val > NUM_LIMIT:
                return None, LexicalError(pos_start, self.pos.copy(), f"Num value cannot be greater than {NUM_LIMIT}")
            return Token(TT_NUM_LITERAL, num_val, pos_start, self.pos), None
        elif dot_count > 1:
            return None, LexicalError(pos_start, self.pos.copy(), "Too many decimal points")
        else:
            deci_val = float(num_str) * negative_val
            if deci_val > DECI_LIMIT:
                return None, LexicalError(pos_start, self.pos.copy(), f"Deci value cannot be greater than {DECI_LIMIT}")
            if len(num_str.split('.')[1]) > DECI_PRECISION_LIMIT:
                return None, LexicalError(pos_start, self.pos.copy(), f"Deci value cannot have more than {DECI_PRECISION_LIMIT} decimal places")
            return Token(TT_DECI_LITERAL, deci_val, pos_start, self.pos), None


#######################################
# PARSE RESULT
#######################################


class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if res.error:
            self.error = res.error
        return res.node

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


#######################################
# PARSER
#######################################


class Parser:
    def __init__(self, tokens):
        self.tokens = [token for token in tokens if token.type not in (TT_SPACE, TT_S_COMMENT, TT_M_COMMENT)]
        self.tok_idx = -1
        self.force_newline = False
        self.advance()

    def advance(self):
        self.tok_idx += 1

        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

        return self.current_tok

    def mark(self):
        return self.tok_idx

    def reset(self, idx):
        self.tok_idx = idx - 1
        self.advance()

    def get_tok_at(self, idx):
        return self.tokens[idx]

    def expect(self, token_types, advance=True):
        tok = self.current_tok

        if tok.type in token_types:
            if advance:
                self.advance()
            return tok

        return None

    def throw_error(self, details, error_type=None, pos_start=None, pos_end=None,):
        pos_start = pos_start or self.current_tok.pos_start
        pos_end = pos_end or self.current_tok.pos_end

        if not error_type:
            error_type = SyntaxError

        return error_type(pos_start, pos_end, details)

    def throw_expected_error(self, expected):
        expected_txt = ""
        comma_sep = ", ".join([f"'{i}'" for i in expected])

        if len(expected) > 1:
            expected_txt += f"one of ({comma_sep})"
        else:
            expected_txt += f"{comma_sep}"

        message = f"Unexpected end of file, expected {expected_txt}" if self.current_tok.type == TT_EOF else f"Expected {expected_txt}, got '{self.current_tok.type}'"

        return self.throw_error(message)

    def throw_indentation_error(self, pos, tab_count, level):
        return self.throw_error(f"Required indent is {level}, got {tab_count}", error_type=IndentationError, pos_start=self.get_tok_at(pos).pos_start, pos_end=self.get_tok_at(self.tok_idx).pos_start)

    def parse(self):
        res = self.program()

        if not res.error and self.current_tok.type != TT_EOF:
            return res.failure(self.throw_error("Unexpected token"))

        return res

    #######################################

    def program(self):
        res = ParseResult()
        global_nodes = []

        if self.expect({TT_HOME}):
            if not self.expect({TT_OPAR}):
                return res.failure(self.throw_expected_error([TT_OPAR]))

            if not self.expect({TT_CPAR}):
                return res.failure(self.throw_expected_error([TT_CPAR]))

            if not self.expect({TT_COLON}):
                return res.failure(self.throw_expected_error([TT_COLON]))

            res.register(self._req_newline())
            if res.error:
                return res

            self.force_newline = False

            home_body = res.register(self.statements(level=1))
            if res.error:
                return res

            home_node = FuncDefNode(DataTypeNode(TT_EMPTY), TT_HOME, [], home_body)

            return res.success(ProgramNode(global_nodes, home_node))

        return res.failure(self.throw_expected_error([TT_HOME, TT_FROZEN, TT_NUM, TT_DECI, TT_WORD, TT_LETTER, TT_CHOICE, TT_WIKI, TT_IDENTIFIER]))

    def extras(self):
        pass

    def global_(self):
        pass

    def group_def(self):
        pass

    def group_body(self):
        pass

    def group_global(self):
        pass

    def access_spec(self):
        pass

    def group_constr(self):
        pass

    def func_def(self):
        pass

    def ret_type(self):
        """
        First set: {EMPTY, COLLECTION, WIKI, NUM, DECI, WORD, LETTER, CHOICE, ID}
        """
        res = ParseResult()

        # -> EMPTY|type
        if self.expect({TT_EMPTY}):
            return res.success(DataTypeNode(TT_EMPTY))

        return res.register(self.type())

    def type(self):
        """
        First set: {COLLECTION, WIKI, NUM, DECI, WORD, LETTER, CHOICE, ID}
        """
        res = ParseResult()

        # -> data-struct|data-type
        if self.expect({TT_COLLECTION, TT_WIKI}, False):
            return res.register(self.data_struct())

        return res.success(self.data_type())

    def data_struct(self):
        """
        First set: {COLLECTION, WIKI}
        """
        res = ParseResult()

        # -> COLLECTION OBRACK type CBRACK
        if self.expect({TT_COLLECTION}):
            if not self.expect({TT_OBRACK}):
                return res.failure(self.throw_expected_error([TT_OBRACK]))

            type_ = res.register(self.type())
            if res.error:
                return res

            if not self.expect({TT_CBRACK}):
                return res.failure(self.throw_expected_error([TT_CBRACK]))

            return res.success(CollectionTypeNode(type_))
        # -> WIKI OBRACK data-type COMMA type CBRACK
        elif self.expect({TT_WIKI}):
            if not self.expect({TT_OBRACK}):
                return res.failure(self.throw_expected_error([TT_OBRACK]))

            data_type = res.register(self.data_type())
            if res.error:
                return res

            if not self.expect({TT_COMMA}):
                return res.failure(self.throw_expected_error([TT_COMMA]))

            type_ = res.register(self.type())
            if res.error:
                return res

            if not self.expect({TT_CBRACK}):
                return res.failure(self.throw_expected_error([TT_CBRACK]))

            return res.success(WikiTypeNode(data_type, type_))

        return res.failure(self.throw_expected_error([TT_COLLECTION, TT_WIKI]))

    def data_type(self):
        """
        First set: {NUM, DECI, WORD, LETTER, CHOICE, ID}
        """
        res = ParseResult()

        # -> NUM|DECI|WORD|LETTER|CHOICE|ID
        if type_ := self.expect({TT_NUM, TT_DECI, TT_WORD, TT_LETTER, TT_CHOICE, TT_IDENTIFIER}):
            return res.success(DataTypeNode(type_))

        return res.failure(self.throw_expected_error([TT_NUM, TT_DECI, TT_WORD, TT_LETTER, TT_CHOICE, TT_IDENTIFIER]))

    def params(self):
        pass

    def statements(self, level):
        """
        First set: {TAB}
        """
        res = ParseResult()
        nodes = []

        while True:
            pos = self.mark()
            tab_count = 0
            while self.expect({TT_TAB}):
                tab_count += 1

            if self.expect({TT_NEWLINE}):
                continue

            if tab_count > level:
                return res.failure(self.throw_indentation_error(pos, tab_count, level))
            elif tab_count < level:
                if len(nodes) == 0:
                    return res.failure(self.throw_indentation_error(pos, tab_count, level))
                self.reset(pos)
                break

            nodes.append(res.register(self.statement(level)))
            if res.error:
                return res

        return res.success(BodyNode(nodes))

    def statement(self, level):
        """
        First set: {BACK, SKIP, STOP, GLOBAL, DEL, ID, INCASE, GIVEN, EVERY, DURING, GO, NEW, NOT, MINUS, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT, BLANK}
        """
        res = ParseResult()

        # -> BACK expr NEWLINE+
        if self.expect({TT_BACK}):
            expr = res.register(self.expr())
            if res.error:
                return res
            res.register(self._req_newline())
            if res.error:
                return res
            return res.success(BackNode(expr))
        # -> SKIP NEWLINE+
        if self.expect({TT_SKIP}):
            res.register(self._req_newline())
            return res.success(SkipNode())
        # -> STOP NEWLINE+
        if self.expect({TT_STOP}):
            res.register(self._req_newline())
            return res.success(StopNode())
        # -> GLOBAL ID NEWLINE+
        if self.expect({TT_GLOBAL}):
            if not (id := self.expect({TT_IDENTIFIER})):
                return res.failure(self.throw_error([TT_IDENTIFIER]))
            res.register(self._req_newline())
            if res.error:
                return res
            return res.success(GlobalAccessNode(id))
        # -> DEL ID NEWLINE+
        if self.expect({TT_DEL}):
            if not (id := self.expect({TT_IDENTIFIER})):
                return res.failure(self.throw_error([TT_IDENTIFIER]))
            res.register(self._req_newline())
            if res.error:
                return res
            return res.success(DelNode(id))
        # -> dec-stmt
        # -> assign-stmt
        # if self.expect({TT_IDENTIFIER}, False):
        #     # TODO
        #     return self.assign_stmt()
        # -> incase-stmt
        if self.expect({TT_INCASE}, False):
            return self.incase_stmt(level)
        # -> given-stmt
        if self.expect({TT_GIVEN}, False):
            return self.given_stmt(level)
        # -> every-stmt
        if self.expect({TT_EVERY}, False):
            return self.every_stmt(level)
        # -> during-stmt
        if self.expect({TT_DURING}, False):
            return self.during_stmt(level)
        # -> go-during-stmt
        if self.expect({TT_GO}, False):
            return self.go_during_stmt(level)

        # -> expr NEWLINE+
        expr = res.register(self.expr())
        if res.error:
            return res
        res.register(self._req_newline())
        if res.error:
            return res
        return res.success(expr)

    def dec_stmt(self):
        pass

    def assign_stmt(self):
        pass

    def incase_stmt(self, level):
        """
        First set: {INCASE}
        """
        res = ParseResult()
        conditions = []
        instead_stmt = None

        # -> INCASE expr COLON NEWLINE+ statements unless* instead?
        if self.expect({TT_INCASE}):
            condition = res.register(self.expr())
            if res.error:
                return res

            if not self.expect({TT_COLON}):
                res.failure(self.throw_expected_error([TT_COLON]))

            self.force_newline = True
            res.register(self._req_newline())
            if res.error:
                return res
            self.force_newline = False

            statements = res.register(self.statements(level+1))
            if res.error:
                return res

            conditions.append((condition, statements))

            # Lookahead for unless/instead
            pos = self.mark()
            tab_count = res.register(self._req_tab(level))
            if res.error:
                if tab_count < level:
                    res.error = None
                    self.reset(pos)
                    return res.success(IncaseNode(conditions, instead_stmt))
                return res

            if self.expect({TT_UNLESS}, False):
                while True:
                    self.reset(pos)
                    conditions.append(res.register(self.unless(level)))
                    if res.error:
                        return res

                    
                    # Lookahead for unless/instead
                    pos = self.mark()
                    tab_count = res.register(self._req_tab(level))
                    if res.error:
                        if tab_count < level:
                            res.error = None
                            self.reset(pos)
                            return res.success(IncaseNode(conditions, instead_stmt))
                        return res

                    if not self.expect({TT_UNLESS}, False):
                        break

            if self.expect({TT_INSTEAD}, False):
                self.reset(pos)
                instead_stmt = res.register(self.instead(level))
                if res.error:
                    return res
            else:
                self.reset(pos)

            return res.success(IncaseNode(conditions, instead_stmt))

        return res.failure(self.throw_expected_error([TT_INCASE]))

    def unless(self, level):
        """
        First set: {TAB}
        """
        res = ParseResult()

        res.register(self._req_tab(level))
        if res.error:
            return res

        if not self.expect({TT_UNLESS}):
            return res.failure(self.throw_expected_error([TT_UNLESS]))

        condition = res.register(self.expr())
        if res.error:
            return res

        if not self.expect({TT_COLON}):
            return res.failure(self.throw_expected_error([TT_COLON]))

        self.force_newline = True
        res.register(self._req_newline())
        if res.error:
            return res
        self.force_newline = False

        statements = res.register(self.statements(level+1))
        if res.error:
            return res

        return res.success((condition, statements))

    def instead(self, level):
        """
        First set: {TAB}
        """
        res = ParseResult()

        res.register(self._req_tab(level))
        if res.error:
            return res

        if not self.expect({TT_INSTEAD}):
            return res.failure(self.throw_expected_error([TT_INSTEAD]))

        if not self.expect({TT_COLON}):
            return res.failure(self.throw_expected_error([TT_COLON]))

        self.force_newline = True
        res.register(self._req_newline())
        if res.error:
            return res
        self.force_newline = False

        statements = res.register(self.statements(level+1))
        if res.error:
            return res

        return res.success((statements))

    def given_stmt(self, level):
        """
        First set: {GIVEN}
        """
        res = ParseResult()

        # -> GIVEN expr COLON NEWLINE+ event-default
        if self.expect({TT_GIVEN}):
            expr = res.register(self.expr())
            if res.error:
                return res

            if not self.expect({TT_COLON}):
                return res.failure(self.throw_expected_error([TT_COLON]))

            self.force_newline = True
            res.register(self._req_newline())
            if res.error:
                return res
            self.force_newline = False

            event_default = res.register(self.event_default(level+1))
            if res.error:
                return res

            if event_default:
                event_nodes, default_stmt = event_default

            return res.success(GivenNode(expr, event_nodes, default_stmt))

        return res.failure(self.throw_expected_error([TT_GIVEN]))

    def event_default(self, level):
        """
        First set: {TAB}
        """
        res = ParseResult()
        event_nodes = []
        default_stmt = None

        pos = self.mark()
        res.register(self._req_tab(level))
        if res.error:
            return res

        # -> event+ (default event*)?
        if self.expect({TT_EVENT}, False):
            # event+
            while True:
                self.reset(pos)
                event_nodes.append(res.register(self.event(level)))
                if res.error:
                    return res

                # Lookahead for next event
                pos = self.mark()
                tab_count = res.register(self._req_tab(level))
                if res.error:
                    if tab_count < level:
                        res.error = None
                        self.reset(pos)
                        return res.success((event_nodes, default_stmt))
                    return res

                # Possible "default" block
                if not self.expect({TT_EVENT}, False):
                    break

            # (default event*)?
            if self.expect({TT_DEFAULT}, False):
                self.reset(pos)
                default_stmt = res.register(self.default(level))
                if res.error:
                    return res

                # Lookahead for next event
                pos = self.mark()
                tab_count = res.register(self._req_tab(level))
                if res.error:
                    if tab_count < level:
                        res.error = None
                        self.reset(pos)
                        return res.success((event_nodes, default_stmt))
                    return res

                if self.expect({TT_DEFAULT}, False):
                    return res.failure(self.throw_error("Only one default block is allowed in given statement"))

                if self.expect({TT_EVENT}, False):
                    while True:
                        self.reset(pos)
                        event_nodes.append(res.register(self.event(level)))
                        if res.error:
                            return res

                        # Lookahead for next event
                        pos = self.mark()
                        tab_count = res.register(self._req_tab(level))
                        if res.error:
                            if tab_count < level:
                                res.error = None
                                break
                            return res

                        # End of given statement
                        if not self.expect({TT_EVENT}, False):
                            break

            self.reset(pos)
            return res.success((event_nodes, default_stmt))
        # -> default event*
        elif self.expect({TT_DEFAULT}, False):
            self.reset(pos)
            default_stmt = res.register(self.default(level))
            if res.error:
                return res

            # Lookahead for next event
            pos = self.mark()
            tab_count = res.register(self._req_tab(level))
            if res.error:
                if tab_count < level:
                    res.error = None
                    self.reset(pos)
                    return res.success((event_nodes, default_stmt))
                return res

            print("mcl")

            if self.expect({TT_DEFAULT}, False):
                return res.failure(
                    self.throw_error(
                        "Only one default block is allowed in given statement"
                    )
                )

            if self.expect({TT_EVENT}, False):
                while True:
                    self.reset(pos)
                    event = res.register(self.event(level))
                    if res.error:
                        return res
                    event_nodes.append(event)

                    # Lookahead for next event
                    pos = self.mark()
                    tab_count = res.register(self._req_tab(level))
                    if res.error:
                        if tab_count < level:
                            res.error = None
                            break
                        return res

                    # End of given statement
                    if not self.expect({TT_EVENT}, False):
                        break

            self.reset(pos)
            return res.success((event_nodes, default_stmt))

        return res.failure(self.throw_expected_error([TT_EVENT, TT_DEFAULT]))

    def default(self, level):
        """
        First set: {TAB}
        """
        res = ParseResult()

        # -> TAB+ DEFAULT COLON NEWLINE+ statements
        res.register(self._req_tab(level))
        if res.error:
            return res

        if not self.expect({TT_DEFAULT}):
            return res.failure(self.throw_expected_error([TT_DEFAULT]))

        if not self.expect({TT_COLON}):
            return res.failure(self.throw_expected_error([TT_COLON]))

        self.force_newline = True

        res.register(self._req_newline())
        if res.error:
            return res

        self.force_newline = False

        default_statements = res.register(self.statements(level+1))
        if default_statements.items[0].node_to_call.var_name_tok.value == "how":
            print("aaaa")
        if res.error:
            return res

        return res.success(default_statements)

    def event(self, level):
        """
        First set: {}
        """
        res = ParseResult()

        # -> TAB+ EVENT literals COLON NEWLINE+ statements
        res.register(self._req_tab(level))
        if res.error:
            return res

        if not self.expect({TT_EVENT}):
            return res.failure(self.throw_expected_error([TT_EVENT]))

        event = res.register(self.literals())
        if res.error:
            return res

        if not self.expect({TT_COLON}):
            return res.failure(self.throw_expected_error([TT_COLON]))

        self.force_newline = True

        res.register(self._req_newline())
        if res.error:
            return res

        self.force_newline = False

        statements = res.register(self.statements(level+1))
        if res.error:
            return res

        return res.success((event, statements))

    def literals(self):
        """
        First set: {NUM_LIT, DECI_LIT, WORD_LIT, LETTER_LIT, YES, NO, BLANK}
        """
        res = ParseResult()

        # -> NUM_LIT|DECI_LIT|WORD_LIT|LETTER_LIT|YES|NO|BLANK
        if number := self.expect({TT_NUM_LITERAL, TT_DECI_LITERAL}):
            return res.success(NumberNode(number))
        elif word := self.expect({TT_WORD_LITERAL}):
            return res.success(WordNode(word))
        elif letter := self.expect({TT_LETTER_LITERAL}):
            return res.success(LetterNode(letter))
        elif choice := self.expect({TT_YES, TT_NO}):
            return res.success(ChoiceNode(choice))
        elif blank := self.expect({TT_BLANK}):
            return res.success(BlankNode(blank))

        return res.failure(self.throw_expected_error([TT_NUM_LITERAL, TT_DECI_LITERAL, TT_WORD_LITERAL, TT_LETTER_LITERAL,TT_YES, TT_NO, TT_BLANK]))

    def every_stmt(self, level):
        """
        First set: {EVERY}
        """
        res = ParseResult()

        # -> EVERY type ID (COMMA type ID)? IN expr COLON NEWLINE+ statements
        if self.expect({TT_EVERY}):
            type_ = res.register(self.type())
            if res.error:
                return res

            if not (id := self.expect({TT_IDENTIFIER})):
                return res.failure(self.throw_expected_error([TT_IDENTIFIER]))

            if self.expect({TT_COMMA}):
                type2 = res.register(self.type())
                if res.error:
                    return res

                if not (id2 := self.expect({TT_IDENTIFIER})):
                    return res.failure(self.throw_expected_error([TT_IDENTIFIER]))
            else:
                type2 = None
                id2 = None

            if not self.expect({TT_IN}):
                return res.failure(self.throw_expected_error([TT_IN]))

            iterable = res.register(self.expr())
            if res.error:
                return res

            if not self.expect({TT_COLON}):
                return res.failure(self.throw_expected_error([TT_COLON]))

            res.register(self._req_newline())
            if res.error:
                return res

            statements = res.register(self.statements(level + 1))
            if res.error:
                return res

            return res.success(EveryNode((type_, id), (type2, id2), iterable, statements))

    def during_stmt(self, level):
        """
        First set: {DURING}
        """
        res = ParseResult()

        # -> DURING expr COLON NEWLINE+ statements
        if self.expect({TT_DURING}):
            condition = res.register(self.expr())
            if res.error:
                return res

            if not self.expect({TT_COLON}):
                return res.failure(self.throw_expected_error([TT_COLON]))

            self.force_newline = True

            res.register(self._req_newline())
            if res.error:
                return res

            self.force_newline = False

            statements = res.register(self.statements(level + 1))
            if res.error:
                return res

            return res.success(DuringNode(condition, statements))

        return res.failure(self.throw_expected_error([TT_DURING]))

    def go_during_stmt(self, level):
        """
        First set: {GO}
        """
        res = ParseResult()

        # -> GO COLON NEWLINE+ statements TAB+ DURING expr NEWLINE+
        if self.expect({TT_GO}):
            if not self.expect({TT_COLON}):
                return res.failure(self.throw_expected_error([TT_COLON]))

            self.force_newline = True

            res.register(self._req_newline())
            if res.error:
                return res

            statements = res.register(self.statements(level + 1))
            if res.error:
                return res

            self.force_newline = False

            res.register(self._req_tab(level))
            if res.error:
                return res

            if not self.expect({TT_DURING}):
                return res.failure(self.throw_expected_error([TT_DURING]))

            condition = res.register(self.expr())
            if res.error:
                return res

            res.register(self._req_newline())
            if res.error:
                return res

            return res.success(GoDuringNode(statements, condition))

        return res.failure(self.throw_expected_error([TT_GO]))

    def _req_newline(self):
        res = ParseResult()

        if self.force_newline or not self.expect({TT_EOF}, False):
            if not self.expect({TT_NEWLINE}):
                return res.failure(self.throw_expected_error([TT_NEWLINE]))

        while self.expect({TT_NEWLINE}):
            pass

        return res

    def _req_tab(self, level):
        pos = self.mark()
        res = ParseResult()

        if self.expect({TT_EOF}, False):
            res.node = 0
            return res

        tab_count = 0
        while self.expect({TT_TAB}):
            tab_count += 1

        if tab_count != level:
            res.node = tab_count
            return res.failure(self.throw_indentation_error(pos, tab_count, level))

        return res.success(tab_count)

    def expr(self):
        """
        First set: {NEW, NOT, MINUS, ID, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT, BLANK}
        """
        res = ParseResult()

        # -> NEW ID args
        if self.expect({TT_NEW}):
            if not (id := self.expect({TT_IDENTIFIER})):
                return res.failure(self.throw_error([TT_IDENTIFIER]))
            new_object = res.register(self.args(VarAccessNode(id)))
            return res.success(new_object)
        # -> and-expr (OR and-expr)*
        return self._binary_op(self.and_expr, (TT_OR,))

    def and_expr(self):
        """
        First set: {NOT, MINUS, ID, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT, BLANK}
        """
        # -> comp-expr (AND comp-expr)*
        return self._binary_op(self.comp_expr, (TT_AND,))

    def comp_expr(self):
        """
        First set: {NOT, MINUS, ID, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT, BLANK}
        """
        res = ParseResult()

        # -> NOT comp-expr
        if not_ := self.expect({TT_NOT}):
            comp_expr = res.register(self.comp_expr())
            if res.error:
                return res
            return res.success(UnaryOpNode(not_, comp_expr))
        # -> BLANK
        elif blank := self.expect({TT_BLANK}):
            return res.success(BlankNode(blank))
        # -> arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*
        return self._binary_op(self.arith_expr, (TT_EQUAL_TO, TT_NOT_EQUAL, TT_LESS_THAN, TT_GREATER_THAN, TT_LESS_THAN_EQUAL, TT_GREATER_THAN_EQUAL))

    def arith_expr(self):
        """
        First set: {MINUS, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT}
        """
        # -> term ((PLUS|MINUS) term)*
        return self._binary_op(self.term, (TT_PLUS, TT_MINUS))

    def term(self):
        """
        First set: {MINUS, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT}
        """
        # -> factor ((MUL|DIV|FLOOR|MOD) factor)*
        return self._binary_op(self.factor, (TT_MULTIPLY, TT_DIVIDE, TT_FLOOR, TT_MODULO))

    def factor(self):
        """
        First set: {MINUS, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT}
        """
        res = ParseResult()

        # -> MINUS factor
        if neg := self.expect({TT_MINUS}):
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(neg, factor))

        # -> power
        return self.power()

    def power(self):
        """
        First set: {ID, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT}
        """
        # -> atom (POW factor)*
        return self._binary_op(self.atom, (TT_POWER,), self.factor)

    def _binary_op(self, func_a, ops, func_b=None):
        """
        Returns a BinaryOpNode with the left and right operand along with its operator
        """
        res = ParseResult()

        if not func_b:
            func_b = func_a

        left = res.register(func_a())
        if res.error:
            return res

        while op_tok := self.expect(ops):
            right = res.register(func_b())
            if res.error:
                return res
            left = BinaryOpNode(left, op_tok, right)

        return res.success(left)

    def atom(self):
        """
        First set: {ID, WORD_LIT, OBRACK, OBRACE, OPAR, YES, NO, LETTER_LIT, NUM_LIT, DECI_LIT}
        """
        res = ParseResult()
        # -> ID dot_slice_arg*
        if id := self.expect({TT_IDENTIFIER}):
            var_node = VarAccessNode(id)
            while self.expect({TT_PERIOD, TT_OBRACK, TT_OPAR}, False):
                var_node = res.register(self.dot_slice_arg(var_node))
                if res.error:
                    return res
            return res.success(var_node)
        # -> WORD_LIT dot_slice* dot_slice_arg*
        elif word_lit := self.expect({TT_WORD_LITERAL}):
            word_node = res.register(self._dot_slice_first(WordNode(word_lit)))
            if res.error:
                return res
            return res.success(word_node)
        # -> collection-expr dot_slice* dot_slice_arg*
        elif self.expect({TT_OBRACK}, False):
            collection_node = res.register(self.collection_expr())
            if res.error:
                return res
            collection_node = res.register(self._dot_slice_first(collection_node))
            if res.error:
                return res
            return res.success(collection_node)
        # -> wiki-expr dot_slice* dot_slice_arg*
        elif self.expect({TT_OBRACE}, False):
            wiki_node = res.register(self.wiki_expr())
            if res.error:
                return res
            wiki_node = res.register(self._dot_slice_first(wiki_node))
            if res.error:
                return res
            return res.success(wiki_node)
        # -> OPAR expr CPAR dot_slice* dot_slice_arg*
        elif self.expect({TT_OPAR}):
            expr = res.register(self.expr())
            if res.error:
                return res
            if not self.expect({TT_CPAR}):
                return res.failure(self.throw_error([TT_CPAR]))
            expr = res.register(self._dot_slice_first(expr))
            if res.error:
                return res
            return res.success(expr)
        # -> YES dot* dot_slice_arg*
        # -> NO dot* dot_slice_arg*
        elif choice_node := self.expect({TT_YES, TT_NO}):
            choice_node = res.register(self._dot_first(ChoiceNode(choice_node)))
            if res.error:
                return res
            return res.success(choice_node)
        # -> LETTER_LIT dot* dot_slice_arg*
        elif letter := self.expect({TT_LETTER_LITERAL}):
            letter_node = res.register(self._dot_first(LetterNode(letter)))
            if res.error:
                return res
            return res.success(letter_node)
        # -> NUM_LIT
        # -> DECI_LIT
        elif num := self.expect({TT_NUM_LITERAL, TT_DECI_LITERAL}):
            return res.success(NumberNode(num))

        return res.failure(self.throw_expected_error([TT_NEW, TT_NOT, TT_BLANK, TT_MINUS, TT_IDENTIFIER, TT_WORD_LITERAL, TT_OBRACK, TT_OBRACE, TT_OPAR, TT_YES, TT_NO, TT_LETTER_LITERAL, TT_NUM_LITERAL, TT_DECI_LITERAL]))

    def _dot_slice_first(self, node):
        """
        Allow dot or slicing first then args
        """
        res = ParseResult()

        # -> (dot_slice args*)*
        while self.expect({TT_PERIOD, TT_OBRACK}, False):
            node = res.register(self.dot_slice(node))
            if res.error:
                return res
            while self.expect({TT_OPAR}, False):
                node = res.register(self.args(node))
                if res.error:
                    return res
        return res.success(node)

    def _dot_first(self, node):
        """
        Allow dot first then slicing and args
        """
        res = ParseResult()

        # -> (dot slice_args*)*
        while self.expect({TT_PERIOD}, False):
            node = res.register(self.dot(node))
            if res.error:
                return res
            while self.expect({TT_OBRACK, TT_OPAR}, False):
                node = res.register(self.slice_arg(node))
                if res.error:
                    return res
        return res.success(node)

    def dot_slice_arg(self, node):
        """
        First set: {PERIOD, OBRACK, OPAR}
        """
        res = ParseResult()

        # -> dot_slice
        if self.expect({TT_PERIOD, TT_OBRACK}, False):
            node = res.register(self.dot_slice(node))
            if res.error:
                return res
            return res.success(node)
        elif self.expect({TT_OPAR}, False):
            call_node = res.register(self.args(node))
            if res.error:
                return res
            return res.success(call_node)

        return res.failure(self.throw_expected_error([TT_PERIOD, TT_OBRACK, TT_OPAR]))

    def dot_slice(self, node):
        """
        First set: {PERIOD, OBRACK}
        """
        res = ParseResult()

        # -> dot
        if self.expect({TT_PERIOD}, False):
            dot_node = res.register(self.dot(node))
            if res.error:
                return res
            return res.success(dot_node)
        # -> slice
        elif self.expect({TT_OBRACK}, False):
            slice_node = res.register(self.slice(node))
            if res.error:
                return res
            return res.success(slice_node)

        return res.failure(self.throw_expected_error([TT_PERIOD, TT_OBRACK]))

    def slice_arg(self, node):
        """
        First set: {OBRACK, OPAR}
        """
        res = ParseResult()

        # -> slice
        if self.expect({TT_OBRACK}, False):
            slice_node = res.register(self.slice(node))
            if res.error:
                return res
            return res.success(slice_node)
        # -> args
        elif self.expect({TT_OPAR}, False):
            call_node = res.register(self.args(node))
            if res.error:
                return res
            return res.success(call_node)

        return res.failure(self.throw_expected_error([TT_OBRACK, TT_OPAR]))

    def dot(self, node):
        """
        First set: {PERIOD}
        """
        res = ParseResult()

        # -> PERIOD ID
        if self.expect({TT_PERIOD}):
            if id := self.expect({TT_IDENTIFIER}):
                return res.success(DotOpNode(node, VarAccessNode(id)))

            return res.failure(self.throw_expected_error([TT_IDENTIFIER]))

        return res.failure(self.throw_expected_error([TT_PERIOD]))

    def slice(self, node):
        """
        First set: {OBRACK}
        """
        res = ParseResult()
        start = None
        end = None

        # -> OBRACK expr (COLON expr)? CBRACK
        if self.expect({TT_OBRACK}):
            start = res.register(self.expr())
            if res.error:
                return res

            if not self.expect({TT_CBRACK}):
                if self.expect({TT_COLON}):
                    end = res.register(self.expr())
                    if res.error:
                        return res

                    if self.expect({TT_CBRACK}):
                        return res.failure(self.throw_expected_error([TT_CBRACK]))

                return res.failure(self.throw_error("Expected an expression"))

            return res.success(BracketAccessNode(node, start, end))

        return res.failure(self.throw_expected_error([TT_OBRACK]))

    def args(self, node):
        """
        First set: {OPAR}
        """
        res = ParseResult()
        arg_nodes = []

        # -> OPAR (expr (COMMA expr)*)? CPAR
        if self.expect({TT_OPAR}):
            if not self.expect({TT_CPAR}):
                while True:
                    arg_nodes.append(res.register(self.expr()))
                    if res.error:
                        return res

                    if not self.expect({TT_COMMA}):
                        break

                if not self.expect({TT_CPAR}):
                    return res.failure(self.throw_expected_error([TT_CPAR]))

            return res.success(CallNode(node, arg_nodes))

        return res.failure(self.throw_expected_error([TT_OPAR]))

    def collection_expr(self):
        """
        First set: {OBRACK}
        """
        res = ParseResult()
        items = []

        # -> OBRACK (expr (COMMA expr)*)? CBRACK
        if self.expect({TT_OBRACK}):
            if not self.expect({TT_CBRACK}):
                while True:
                    items.append(res.register(self.expr()))
                    if res.error:
                        return res
                    if not self.expect({TT_COMMA}):
                        break
                if not self.expect({TT_CBRACK}):
                    return res.failure(self.throw_expected_error([TT_CBRACK]))
            return res.success(CollectionNode(items))

        return res.failure(self.throw_expected_error([TT_OBRACK]))

    def wiki_expr(self):
        """
        First set: {OBRACE}
        """
        res = ParseResult()
        key_value_pairs = []

        # -> OBRACE (keys COLON expr (COMMA keys COLON expr)*)? CBRACE
        if self.expect({TT_OBRACE}):
            if not self.expect({TT_CBRACE}):
                while True:
                    key = res.register(self.keys())
                    if res.error:
                        return res
                    if not self.expect({TT_COLON}):
                        return res.failure(self.throw_expected_error([TT_COLON]))
                    value = res.register(self.expr())
                    if res.error:
                        return res
                    key_value_pairs.append((key, value))
                    if not self.expect({TT_COMMA}):
                        break
                if not self.expect({TT_CBRACE}):
                    return res.failure(self.throw_expected_error([TT_CBRACE]))
            return res.success(WikiNode(key_value_pairs))

        return res.failure(self.throw_expected_error([TT_OBRACE]))

    def keys(self):
        """
        First set: {NUM_LIT, DECI_LIT, WORD_LIT, LETTER_LIT, YES, NO}
        """
        res = ParseResult()

        # -> NUM_LIT|DECI_LIT|WORD_LIT|LETTER_LIT|YES|NO|BLANK
        if number := self.expect({TT_NUM_LITERAL, TT_DECI_LITERAL}):
            return res.success(NumberNode(number))
        elif word := self.expect({TT_WORD_LITERAL}):
            return res.success(WordNode(word))
        elif letter := self.expect({TT_LETTER_LITERAL}):
            return res.success(LetterNode(letter))
        elif choice := self.expect({TT_YES, TT_NO}):
            return res.success(ChoiceNode(choice))

        return res.failure(self.throw_expected_error([TT_NUM_LITERAL, TT_DECI_LITERAL, TT_WORD_LITERAL, TT_LETTER_LITERAL,TT_YES, TT_NO]))


#######################################
# NODES
#######################################


class NumberNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f"num({self.tok.value})"

class WordNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f"word({repr(self.tok.value)})"

class LetterNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f"letter({repr(self.tok.value)})"

class ChoiceNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f"choice({self.tok})"

class BlankNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f"{self.tok}"

class UnaryOpNode:
    def __init__(self, op_tok, right_node):
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f"('{self.op_tok}', {self.right_node})"

class BinaryOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f"({self.left_node}, '{self.op_tok}', {self.right_node})"

class DotOpNode:
    def __init__(self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f"({self.left_node}, '.', {self.right_node})"

class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok
    
    def __repr__(self):
        return f"var_access({self.var_name_tok})"

class BracketAccessNode:
    def __init__(self, var_access_node, left_slice, right_slice):
        self.var_access_node = var_access_node
        self.left_slice = left_slice
        self.right_slice = right_slice
    
    def __repr__(self):
        return f"bracket_access({self.var_access_node}, from:{self.left_slice}, to:{self.right_slice})"

class VarDecNode:
    def __init__(self, is_frozen, data_type_node, var_name_tok, value_node):
        self.is_frozen = is_frozen
        self.data_type_node = data_type_node
        self.var_name_tok = var_name_tok
        self.value_node = value_node

    def __repr__(self):
        return f"var_init({self.var_name_tok}, frozen:{self.is_frozen}, type:{self.data_type_node}, val:{self.value_node})"

class BodyNode:
    def __init__(self, items):
        self.items = items or []

    def __repr__(self):
        return f"{self.items}"

class ProgramNode:
    def __init__(self, global_nodes, home_node):
        self.global_nodes = global_nodes
        self.home_node = home_node

    def __repr__(self):
        return f"program({self.global_nodes}, {self.home_node})"

class CollectionNode:
    def __init__(self, coll_value_nodes):
        self.coll_value_nodes = coll_value_nodes
    
    def __repr__(self):
        return f"collection({self.coll_value_nodes})"

class WikiNode:
    def __init__(self, key_value_pairs):
        self.key_value_pairs = key_value_pairs

    def __repr__(self):
        return f"wiki({self.key_value_pairs})"

class FuncDefNode:
    def __init__(self, return_type, id, params, body):
        self.return_type = return_type
        self.id = id
        self.params = params
        self.body = body
    
    def __repr__(self):
        return f"func_def({self.id}, type:{self.return_type}, params:{self.params}, body:{self.body})"

class CallNode:
    def __init__(self, node_to_call, args):
        self.node_to_call = node_to_call
        self.args = args

    def __repr__(self):
        return f"call({self.node_to_call}, args:{self.args})"

class NewObjectNode:
    def __init__(self, node_to_call, args):
        self.node_to_call = node_to_call
        self.args = args

    def __repr__(self):
        return f"new_object({self.node_to_call}, args:{self.args})"


class DataTypeNode:
    def __init__(self, type_tok):
        self.type_tok = type_tok

    def __repr__(self):
        return f"datatype({self.type_tok})"

class CollectionTypeNode:
    def __init__(self, type_node):
        self.type_node = type_node

    def __repr__(self):
        return f"collectiontype({self.type_node})"

class WikiTypeNode:
    def __init__(self, key_type_node, value_type_node):
        self.key_type_node = key_type_node
        self.value_type_node = value_type_node
    
    def __repr__(self):
        return f"wikitype({self.key_type_node}, {self.value_type_node})"

class DuringNode:
    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def __repr__(self):
        return f"during({self.condition}, {self.statements})"

class GoDuringNode:
    def __init__(self, statements, condition):
        self.statements = statements
        self.condition = condition

    def __repr__(self):
        return f"go_during({self.statements}, {self.condition})"

class DelNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok

    def __repr__(self):
        return f"del({self.var_name_tok})"

class GlobalAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok

    def __repr__(self):
        return f"global_access({self.var_name_tok})"

class StopNode:
    def __repr__(self):
        return "stop()"

class SkipNode:
    def __repr__(self):
        return "skip()"

class BackNode:
    def __init__(self, value_node):
        self.value_node = value_node

    def __repr__(self):
        return f"back({self.value_node})"

class EveryNode:
    def __init__(self, var1, var2, iterable, statements):
        self.var1 = var1
        self.var2 = var2
        self.iterable = iterable
        self.statements = statements

    def __repr__(self):
        return f"every({self.var1}, {self.var2}, {self.iterable}, {self.statements})"


class GivenNode:
    def __init__(self, given_expr, event_nodes, default_stmt):
        self.given_expr = given_expr
        self.event_nodes = event_nodes
        self.default_stmt = default_stmt
    
    def __repr__(self):
        return f"given({self.given_expr}, {self.event_nodes}, {self.default_stmt})"

class IncaseNode:
    def __init__(self, conditions, instead_stmt):
        self.conditions = conditions
        self.instead_stmt = instead_stmt
    
    def __repr__(self):
        return f"incase({self.conditions}, {self.instead_stmt})"


#######################################
# RUN
#######################################


def run_syntax(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, errors = lexer.make_tokens()
    if errors:
        return tokens[:-1], None, errors

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    res = parser.parse()

    return tokens[:-1], res.node, [res.error] if res.error else None


def run_lexical(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, errors = lexer.make_tokens()
    # tokens.pop()

    return tokens[:-1], errors
