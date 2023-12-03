from enum import Enum

"""
------
TOKENS
------
"""


class TokenType(Enum):
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

    IDENTIFIER = "ID"

    SPACE = "SPACE"
    TAB = "\\t"
    NEWLINE = "\\n"
    MULTIPLY = "MULTIPLY"
    MULTIPLY_ASSIGN = "MULTIPLY_ASSIGN"
    POWER = "POWER"
    POWER_ASSIGN = "POWER_ASSIGN"
    PLUS = "PLUS"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS = "MINUS"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    DIVIDE = "DIVIDE"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    FLOOR = "FLOOR"
    FLOOR_ASSIGN = "FLOOR_ASSIGN"
    MODULO = "MODULO"
    MODULO_ASSIGN = "MODULO_ASSIGN"
    ASSIGN = "ASSIGN"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL = "NOT_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_EQUAL = "LESS_THAN_EQUAL"
    OPAR = "OPAR"
    CPAR = "CPAR"
    OBRACE = "OBRACE"
    CBRACE = "CBRACE"
    OBRACK = "OBRACK"
    CBRACK = "CBRACK"
    COMMA = "COMMA"
    PERIOD = "PERIOD"
    COLON = "COLON"

    WORD_LITERAL = "WORD_LITERAL"
    NUM_LITERAL = "NUM_LITERAL"
    DECI_LITERAL = "DECI_LITERAL"

    S_COMMENT = "S_COMMENT"
    M_COMMENT = "M_COMMENT"

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
