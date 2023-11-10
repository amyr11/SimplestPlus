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
    INP = "inp"
    INSTEAD = "instead"
    NO = "no"
    NOT = "not"
    NUM = "num"
    OR = "or"
    OUT = "out"
    RANGE = "range"
    RESTRICTED = "restricted"
    SKIP = "skip"
    STOP = "stop"
    UNLESS = "unless"
    VISIBLE = "visible"
    WIKI = "wiki"
    WORD = "word"
    YES = "yes"

    IDENTIFIER = "ID"

    SPACE = "SPACE"
    INDENT = "INDENT"
    NEWLINE = "NEWLINE"
    MULTIPLY = "MULTIPLY"
    MULTIPLY_EQUAL = "MULTIPLY_EQUAL"
    POWER = "POWER"
    POWER_EQUAL = "POWER_EQUAL"
    ADD = "ADD"
    ADD_EQUAL = "ADD_EQUAL"
    SUBTRACT = "SUBTRACT"
    SUBTRACT_EQUAL = "SUBTRACT_EQUAL"
    DIVIDE = "DIVIDE"
    DIVIDE_EQUAL = "DIVIDE_EQUAL"
    FLOOR = "FLOOR"
    FLOOR_EQUAL = "FLOOR_EQUAL"
    MODULO = "MODULO"
    MODULO_EQUAL = "MODULO_EQUAL"
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
        INP,
        INSTEAD,
        NO,
        NOT,
        NUM,
        OR,
        OUT,
        RANGE,
        RESTRICTED,
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

    def __str__(self):
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
