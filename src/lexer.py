from typing import Optional

from .errors import Error, InvalidIdentifier, LexicalError, TokenError, InvalidComment
from .tokens import Token, TokenType
from .states import machines

"""
----------------
LEXICAL ANALYZER
----------------
"""


class Lexer:
    def __init__(self, code: str):
        self._machines = machines
        self._code = code
        self._tokens = []
        self._identifiers = {}
        self._errors = []

    def tokenize(self, verbose=True) -> tuple[list[Token], list[Error]]:
        def advance(val, row, col, cursor):
            if val == "\n":
                row += 1
                col = 1
            else:
                col += len(val)
            cursor += len(val)

            return row, col, cursor

        self._tokens = []
        self._errors = []

        # Preprocess
        preprocessed_code = self._preprocessed_code()

        # Tokenize code
        tmp_code = preprocessed_code
        cursor = 0
        row = 1
        col = 1

        while cursor < len(preprocessed_code):
            tmp_code = preprocessed_code[cursor:]
            cur_char = tmp_code[0]
            token = None
            val = ""

            machine = self._machines.get_machine(cur_char)

            if machine is None:
                self._errors.append(LexicalError(self._code, row, col, cur_char))
                row, col, cursor = advance(cur_char, row, col, cursor)
                continue

            if verbose:
                print(f"Current character to tokenize: {repr(cur_char)}")

            while token is None and machine is not None:
                token, val = machine.tokenize_first(tmp_code, verbose=verbose)
                machine = machine.fallback

                if verbose and (machine is not None and token is None):
                    print("Going to fallback machine")

            if token is None:
                self._errors.append(LexicalError(self._code, row, col, val))
                row, col, cursor = advance(val, row, col, cursor)
                continue

            token.set_position(row, col)
            row, col, cursor = advance(val, row, col, cursor)

            # Verify token according to rules
            token_error = self._verify_token(token)

            if token_error:
                if verbose:
                    print("Invalid token")
                self._errors.append(token_error)
                continue

            if verbose:
                print(f"Token of val {repr(token.val)} verified\n")

            self._append_token(token)

        return self._tokens, self._errors

    def _preprocessed_code(self) -> str:
        # Remove the excess spaces after each line before the newline
        preprocessed_code = "\n".join(
            [line.rstrip() for line in self._code.split("\n")]
        )

        return preprocessed_code

    def _verify_token(self, token: Token) -> Optional[Error]:
        MAX_ID_LEN = 20
        MAX_S_COMM_LEN = 79

        if (
            token.type == TokenType.IDENTIFIER
            and token.val in TokenType.reserved_words.value
        ):
            return TokenError(
                self._code, token, "Invalid use of reserved word."
            )

        if token.type == TokenType.IDENTIFIER and len(token.val) > MAX_ID_LEN:
            return InvalidIdentifier(
                self._code, token, f"Identifier length must be <= {MAX_ID_LEN}."
            )
        
        if token.type == TokenType.S_COMMENT and len(token.val) - 1 > MAX_S_COMM_LEN:
            return InvalidComment(
                self._code, token, f"Inline comment length must be <= {MAX_S_COMM_LEN}."
            )


        return None

    def _append_token(self, token: Token) -> None:
        if token.type == TokenType.IDENTIFIER:
            if token.val in self._identifiers:
                token.id = self._identifiers[token.val]
            else:
                token.id = len(self._identifiers) + 1
                self._identifiers[token.val] = token.id

        self._tokens.append(token)
