from enum import Enum

"""
------
TOKENS
------
"""


class TokenType(Enum):
    EOF = "\\0"

    AND = "and"
    BACK = "back"
    BLANK = "blank"
    CHOICE = "choice"
    DECI = "deci"
    DEFAULT = "default"
    DURING = "during"
    EMPTY = "empty"
    EVENT = "event"
    EVERY = "every"
    FROZEN = "frozen"
    GIVEN = "given"
    GLOBAL = "global"
    GO = "go"
    GROUP = "group"
    HIDDEN = "hidden"
    HOME = "home"
    IN = "in"
    INCASE = "incase"
    INHERITS = "inherits"
    INITIALIZE = "initialize"
    INP = "inp"
    INSTEAD = "instead"
    NEW = "new"
    NO = "no"
    NOT = "not"
    NUM = "num"
    OR = "or"
    OUT = "out"
    PARENT = "parent"
    RANGE = "range"
    RESTRICTED = "restricted"
    SELF = "self"
    SKIP = "skip"
    STOP = "stop"
    UNLESS = "unless"
    VISIBLE = "visible"
    WIKI = "wiki"
    WORD = "word"
    YES = "yes"

    IDENTIFIER = "id"

    SPACE = "space"
    TAB = "\\t"
    NEWLINE = "\\n"
    MULTIPLY = "*"
    MULTIPLY_ASSIGN = "*="
    POWER = "**"
    POWER_ASSIGN = "**="
    PLUS = "+"
    PLUS_ASSIGN = "+="
    MINUS = "-"
    MINUS_ASSIGN = "-="
    DIVIDE = "/"
    DIVIDE_ASSIGN = "/="
    FLOOR = "//"
    FLOOR_ASSIGN = "//="
    MODULO = "%"
    MODULO_ASSIGN = "%="
    ASSIGN = "="
    EQUAL_TO = "=="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    GREATER_THAN_EQUAL = ">="
    LESS_THAN = "<"
    LESS_THAN_EQUAL = "<="
    OPAR = "("
    CPAR = ")"
    OBRACE = "{"
    CBRACE = "}"
    OBRACK = "["
    CBRACK = "]"
    COMMA = ","
    PERIOD = "."
    COLON = ":"

    WORD_LITERAL = "word_lit"
    NUM_LITERAL = "num_lit"
    DECI_LITERAL = "deci_lit"

    S_COMMENT = "s_comment"
    M_COMMENT = "m_comment"

    reserved_words = [
        AND,
        BACK,
        BLANK,
        CHOICE,
        DECI,
        DEFAULT,
        DURING,
        EMPTY,
        EVENT,
        EVERY,
        FROZEN,
        GIVEN,
        GLOBAL,
        GO,
        GROUP,
        HIDDEN,
        HOME,
        IN,
        INCASE,
        INHERITS,
        INITIALIZE,
        INP,
        INSTEAD,
        NEW,
        NO,
        NOT,
        NUM,
        OR,
        OUT,
        PARENT,
        RANGE,
        RESTRICTED,
        SELF,
        SKIP,
        STOP,
        UNLESS,
        VISIBLE,
        WIKI,
        WORD,
        YES,
    ]


class Token:
    def __init__(self, t_type: TokenType, t_val: str):
        self.type = t_type
        self.val = t_val
        self.id = 1
        self._row = None
        self._col = None

    def val_string(self):
        if self.val == "\n":
            return "\\n"
        elif self.val == "\t":
            return "\\t"
        return self.val

    def token_string(self):
        if self.type == TokenType.IDENTIFIER:
            return f"{self.type.value}_{self.id}"
        return self.type.value

    def set_position(self, row, col):
        self._row = row
        self._col = col

    def get_position(self) -> tuple[int, int]:
        if self._row is None or self._col is None:
            raise ValueError("Token position not defined")

        return self._row, self._col
