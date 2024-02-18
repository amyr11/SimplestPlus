from .tokens import Token

"""
------
ERRORS
------
"""


class Error:
    def __init__(self, code: str, row: int, col: int, val: str, message: str):
        self.code = code
        self.row = row
        self.col = col
        self.val = val
        self.message = message

    def _code_error_string(self) -> str:
        # TODO: Fix multiple line errors formatting
        split = self.code.split("\n")
        out = ""
        top = self.row > 3
        start = self.row - 3 if top else 0
        len_last_row_no = len(str(self.row)) if self.row > 100 else 3
        if top:
            out += " " * 3 + "...\n"
        for i in range(start, self.row):
            line = split[i]
            line = line.replace("\t", " "*4)
            cur_row = i + 1
            len_cur_row_no = len(str(cur_row))
            len_space = len_last_row_no - len_cur_row_no
            if cur_row == self.row:
                tmp_out = "-> " + " " * len_space + str(cur_row) + " " * 2
                out += tmp_out
                out += line + "\n"
                out += (
                    " " * (len(tmp_out) + self.col - 1) + "~" * (len(self.val)) + "\n"
                )
            else:
                out += "   " + " " * len_space + str(cur_row) + " " * 2
                out += line + "\n"
        return out

    def as_string(self) -> str:
        out = self._code_error_string()
        out += "-" * len(self.message) + "\n" + self.message + "\n"
        return out


class LexicalError(Error):
    def __init__(self, code: str, row: int, col: int, val: str):
        super().__init__(
            code,
            row,
            col,
            val,
            f"LexicalError: Invalid lexeme {repr(val)} at ln {row}, col {col}",
        )


class TokenError(Error):
    def __init__(self, code: str, token: Token, message: str):
        t_row, t_col = token.get_position()
        super().__init__(
            code,
            t_row,
            t_col,
            token.val,
            f"TokenError: `{token.val}` at ln {t_row}, col {t_col}. {message}",
        )


class InvalidIdentifier(Error):
    def __init__(self, code: str, token: Token, message: str):
        t_row, t_col = token.get_position()
        super().__init__(
            code,
            t_row,
            t_col,
            token.val,
            f"InvalidIdentifier: `{token.val}` at ln {t_row}, col {t_col}. {message}",
        )

class InvalidComment(Error):
    def __init__(self, code: str, token: Token, message: str):
        t_row, t_col = token.get_position()
        super().__init__(
            code,
            t_row,
            t_col,
            token.val,
            f"InvalidComment: `{token.val}` at ln {t_row}, col {t_col}. {message}",
        )
