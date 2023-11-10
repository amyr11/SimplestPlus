from typing import Optional

from .errors import Error, InvalidIdentifier, LexicalError
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
        self.code = code

    def tokenize(self, verbose=True) -> tuple[list[Token], list[Error]]:
        def preprocess(code) -> str:
            # Remove the excess spaces after each line before the newline
            preprocessed_code = "\n".join([line.rstrip() for line in code.split("\n")])

            return preprocessed_code

        def verify_token(token) -> Optional[Error]:
            # TODO: Other rules
            if (
                token.type == TokenType.IDENTIFIER
                and token.val in TokenType.reserved_words.value
            ):
                return InvalidIdentifier(self.code, token)

            return None

        def advance(val, row, col, cursor):
            if val == "\n":
                row += 1
                col = 1
            else:
                col += len(val)
            cursor += len(val)

            return row, col, cursor

        errors = []
        tokens = []

        # Preprocess
        preprocessed_code = preprocess(self.code)

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
                errors.append(LexicalError(self.code, row, col, cur_char))
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
                errors.append(LexicalError(self.code, row, col, val))
                row, col, cursor = advance(val, row, col, cursor)
                continue

            row, col, cursor = advance(val, row, col, cursor)
            token.set_position(row, col)

            # Verify token according to rules
            token_error = verify_token(token)

            if token_error:
                if verbose:
                    print("Invalid token")
                errors.append(token_error)
                continue

            if verbose:
                print(f"Token of val {repr(token.val)} verified\n")

            tokens.append(token)

        return tokens, errors
