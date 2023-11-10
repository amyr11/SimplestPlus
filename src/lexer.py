from typing import Optional

from .errors import Error, InvalidIdentifier, LexicalError
from .machine import FinalState, MachineGroup, StateMachine
from .tokens import Token, TokenType

"""
----------------
LEXICAL ANALYZER
----------------
"""


class Lexer:
    def __init__(self, code: str):
        self._identifiers_machine = StateMachine(
            initial=0,
            final={2: FinalState(TokenType.IDENTIFIER)},
            transitions={
                (0, "all_alpha"): 1,
                (1, "all_id"): 1,
                (1, "delim_id"): 2,
            },
        )

        self._reserved_words_machine = StateMachine(
            initial=0,
            final={
                4: FinalState(TokenType.AND),
                9: FinalState(TokenType.BACK),
                14: FinalState(TokenType.BLANK),
                21: FinalState(TokenType.CHOICE),
                26: FinalState(TokenType.DECI),
                38: FinalState(TokenType.DURING),
                32: FinalState(TokenType.DEFAULT),
                44: FinalState(TokenType.EMPTY),
                49: FinalState(TokenType.EVENT),
                52: FinalState(TokenType.EVERY),
                59: FinalState(TokenType.FROZEN),
                65: FinalState(TokenType.GIVEN),
                71: FinalState(TokenType.GLOBAL),
                73: FinalState(TokenType.GO),
                78: FinalState(TokenType.GROUP),
                85: FinalState(TokenType.HIDDEN),
                91: FinalState(TokenType.HOME),
                94: FinalState(TokenType.IN),
                99: FinalState(TokenType.INCASE),
                101: FinalState(TokenType.INP),
                107: FinalState(TokenType.INSTEAD),
                110: FinalState(TokenType.NO),
                112: FinalState(TokenType.NOT),
                115: FinalState(TokenType.NUM),
                118: FinalState(TokenType.OR),
                121: FinalState(TokenType.OUT),
                127: FinalState(TokenType.RANGE),
                137: FinalState(TokenType.RESTRICTED),
                142: FinalState(TokenType.SKIP),
                146: FinalState(TokenType.STOP),
                153: FinalState(TokenType.UNLESS),
                161: FinalState(TokenType.VISIBLE),
                166: FinalState(TokenType.WIKI),
                170: FinalState(TokenType.WORD),
                174: FinalState(TokenType.YES),
            },
            transitions={
                (0, "a"): 1,
                (1, "n"): 2,
                (2, "d"): 3,
                (3, "delim_reserve"): 4,
                (0, "b"): 5,
                (5, "a"): 6,
                (6, "c"): 7,
                (7, "k"): 8,
                (8, "delim_reserve"): 9,
                (5, "l"): 10,
                (10, "a"): 11,
                (11, "n"): 12,
                (12, "k"): 13,
                (13, "delim_value"): 14,
                (0, "c"): 15,
                (15, "h"): 16,
                (16, "o"): 17,
                (17, "i"): 18,
                (18, "c"): 19,
                (19, "e"): 20,
                (20, "delim_reserve"): 21,
                (0, "d"): 22,
                (22, "e"): 23,
                (23, "c"): 24,
                (24, "i"): 25,
                (25, "delim_dtype"): 26,
                (23, "f"): 27,
                (27, "a"): 28,
                (28, "u"): 29,
                (29, "l"): 30,
                (30, "t"): 31,
                (31, "delim_colon"): 32,
                (22, "u"): 33,
                (33, "r"): 34,
                (34, "i"): 35,
                (35, "n"): 36,
                (36, "g"): 37,
                (37, "delim_reserve"): 38,
                (0, "e"): 39,
                (39, "m"): 40,
                (40, "p"): 41,
                (41, "t"): 42,
                (42, "y"): 43,
                (43, "delim_reserve"): 44,
                (39, "v"): 45,
                (45, "e"): 46,
                (46, "n"): 47,
                (47, "t"): 48,
                (48, "delim_reserve"): 49,
                (46, "r"): 50,
                (50, "y"): 51,
                (51, "delim_reserve"): 52,
                (0, "f"): 53,
                (53, "r"): 54,
                (54, "o"): 55,
                (55, "z"): 56,
                (56, "e"): 57,
                (57, "n"): 58,
                (58, "delim_reserve"): 59,
                (0, "g"): 60,
                (60, "i"): 61,
                (61, "v"): 62,
                (62, "e"): 63,
                (63, "n"): 64,
                (64, "delim_reserve"): 65,
                (60, "l"): 66,
                (66, "o"): 67,
                (67, "b"): 68,
                (68, "a"): 69,
                (69, "l"): 70,
                (70, "delim_reserve"): 71,
                (60, "o"): 72,
                (72, "delim_colon"): 73,
                (60, "r"): 74,
                (74, "o"): 75,
                (75, "u"): 76,
                (76, "p"): 77,
                (77, "delim_reserve"): 78,
                (0, "h"): 79,
                (79, "i"): 80,
                (80, "d"): 81,
                (81, "d"): 82,
                (82, "e"): 83,
                (83, "n"): 84,
                (84, "delim_reserve"): 85,
                (79, "o"): 86,
                (86, "m"): 87,
                (87, "e"): 88,
                (88, "("): 89,
                (89, ")"): 90,
                (90, "delim_colon"): 91,
                (0, "i"): 92,
                (92, "n"): 93,
                (93, "delim_reserve"): 94,
                (93, "c"): 95,
                (95, "a"): 96,
                (96, "s"): 97,
                (97, "e"): 98,
                (98, "delim_reserve"): 99,
                (93, "p"): 100,
                (100, "delim_func"): 101,
                (93, "s"): 102,
                (102, "t"): 103,
                (103, "e"): 104,
                (104, "a"): 105,
                (105, "d"): 106,
                (106, "delim_colon"): 107,
                (0, "n"): 108,
                (108, "o"): 109,
                (109, "delim_value"): 110,
                (109, "t"): 111,
                (111, "delim_reserve"): 112,
                (108, "u"): 113,
                (113, "m"): 114,
                (114, "delim_dtype"): 115,
                (0, "o"): 116,
                (116, "r"): 117,
                (117, "delim_reserve"): 118,
                (116, "u"): 119,
                (119, "t"): 120,
                (120, "delim_func"): 121,
                (0, "r"): 122,
                (122, "a"): 123,
                (123, "n"): 124,
                (124, "g"): 125,
                (125, "e"): 126,
                (126, "delim_func"): 127,
                (122, "e"): 128,
                (128, "s"): 129,
                (129, "t"): 130,
                (130, "r"): 131,
                (131, "i"): 132,
                (132, "c"): 133,
                (133, "t"): 134,
                (134, "e"): 135,
                (135, "d"): 136,
                (136, "delim_reserve"): 137,
                (0, "s"): 138,
                (138, "k"): 139,
                (139, "i"): 140,
                (140, "p"): 141,
                (141, "delim_break"): 142,
                (138, "t"): 143,
                (143, "o"): 144,
                (144, "p"): 145,
                (145, "delim_break"): 146,
                (0, "u"): 147,
                (147, "n"): 148,
                (148, "l"): 149,
                (149, "e"): 150,
                (150, "s"): 151,
                (151, "s"): 152,
                (152, "delim_reserve"): 153,
                (0, "v"): 154,
                (154, "i"): 155,
                (155, "s"): 156,
                (156, "i"): 157,
                (157, "b"): 158,
                (158, "l"): 159,
                (159, "e"): 160,
                (160, "delim_reserve"): 161,
                (0, "w"): 162,
                (162, "i"): 163,
                (163, "k"): 164,
                (164, "i"): 165,
                (165, "delim_reserve"): 166,
                (162, "o"): 167,
                (167, "r"): 168,
                (168, "d"): 169,
                (169, "delim_dtype"): 170,
                (0, "y"): 171,
                (171, "e"): 172,
                (172, "s"): 173,
                (173, "delim_value"): 174,
            },
            fallback=self._identifiers_machine,
        )

        self._reserved_symbols_machine = StateMachine(
            initial=0,
            final={
                175: FinalState(TokenType.SPACE, retract=False),
                176: FinalState(TokenType.SPACE, retract=False),
                177: FinalState(TokenType.SPACE, retract=False),
                178: FinalState(TokenType.INDENT, retract=False),
                181: FinalState(TokenType.NEWLINE, retract=False),
                184: FinalState(TokenType.MULTIPLY),
                186: FinalState(TokenType.MULTIPLY_EQUAL),
                188: FinalState(TokenType.POWER),
                190: FinalState(TokenType.POWER_EQUAL),
                192: FinalState(TokenType.ADD),
                194: FinalState(TokenType.ADD_EQUAL),
                196: FinalState(TokenType.SUBTRACT),
                198: FinalState(TokenType.SUBTRACT_EQUAL),
                200: FinalState(TokenType.DIVIDE),
                202: FinalState(TokenType.DIVIDE_EQUAL),
                204: FinalState(TokenType.FLOOR),
                206: FinalState(TokenType.FLOOR_EQUAL),
                208: FinalState(TokenType.MODULO),
                210: FinalState(TokenType.MODULO_EQUAL),
                212: FinalState(TokenType.ASSIGN),
                214: FinalState(TokenType.EQUAL_TO),
                217: FinalState(TokenType.NOT_EQUAL),
                219: FinalState(TokenType.GREATER_THAN),
                221: FinalState(TokenType.GREATER_THAN_EQUAL),
                223: FinalState(TokenType.LESS_THAN),
                225: FinalState(TokenType.LESS_THAN_EQUAL),
                227: FinalState(TokenType.OPAR),
                229: FinalState(TokenType.CPAR),
                231: FinalState(TokenType.OBRACE),
                233: FinalState(TokenType.CBRACE),
                235: FinalState(TokenType.OBRACK),
                237: FinalState(TokenType.CBRACK),
                239: FinalState(TokenType.COMMA),
                241: FinalState(TokenType.PERIOD),
                243: FinalState(TokenType.COLON),
            },
            transitions={
                (0, " "): 175,
                (175, " "): 176,
                (176, " "): 177,
                (177, " "): 178,
                (0, "\n"): 181,
                (0, "*"): 183,
                (183, "delim_arith"): 184,
                (183, "="): 185,
                (185, "delim_arith"): 186,
                (183, "*"): 187,
                (187, "delim_arith"): 188,
                (187, "="): 189,
                (189, "delim_arith"): 190,
                (0, "+"): 191,
                (191, "delim_plus"): 192,
                (191, "="): 193,
                (193, "delim_plus"): 194,
                (0, "-"): 195,
                (195, "delim_minus"): 196,
                (195, "="): 197,
                (197, "delim_arith"): 198,
                (0, "/"): 199,
                (199, "delim_arith"): 200,
                (199, "="): 201,
                (201, "delim_arith"): 202,
                (199, "/"): 203,
                (203, "delim_arith"): 204,
                (203, "="): 205,
                (205, "delim_arith"): 206,
                (0, "%"): 207,
                (207, "delim_arith"): 208,
                (207, "="): 209,
                (209, "delim_arith"): 210,
                (0, "="): 211,
                (211, "delim_plus"): 212,
                (211, "="): 213,
                (213, "delim_plus"): 214,
                (0, "!"): 215,
                (215, "="): 216,
                (216, "delim_plus"): 217,
                (0, ">"): 218,
                (218, "delim_arith"): 219,
                (218, "="): 220,
                (220, "delim_arith"): 221,
                (0, "<"): 222,
                (222, "delim_arith"): 223,
                (222, "="): 224,
                (224, "delim_arith"): 225,
                (0, "("): 226,
                (226, "delim_opar"): 227,
                (0, ")"): 228,
                (228, "delim_cpar"): 229,
                (0, "{"): 230,
                (230, "delim_obrace"): 231,
                (0, "}"): 232,
                (232, "delim_cbrace"): 233,
                (0, "["): 234,
                (234, "delim_obrack"): 235,
                (0, "]"): 236,
                (236, "delim_cbrack"): 237,
                (0, ","): 238,
                (238, "delim_comma"): 239,
                (0, "."): 240,
                (240, "delim_period"): 241,
                (0, ":"): 242,
                (242, "delim_comma"): 243,
            },
        )

        self._word_literal_machine = StateMachine(
            initial=0,
            final={286: FinalState(TokenType.WORD_LITERAL)},
            transitions={
                (0, '"'): 284,
                (284, '"'): 285,
                (284, "all_word_wo_bs"): 284,
                (284, "\\"): 287,
                (285, "delim_word"): 286,
                (287, "all_word"): 284,
                (287, '"'): 288,
                (288, '"'): 285,
            },
        )

        self._deci_literal_machine = StateMachine(
            initial=321,
            final={
                324: FinalState(TokenType.DECI_LITERAL),
                326: FinalState(TokenType.DECI_LITERAL),
                328: FinalState(TokenType.DECI_LITERAL),
                330: FinalState(TokenType.DECI_LITERAL),
                332: FinalState(TokenType.DECI_LITERAL),
                334: FinalState(TokenType.DECI_LITERAL),
            },
            transitions={
                (321, "."): 322,
                (322, "all_digits"): 323,
                (323, "delim_num_deci"): 324,
                (323, "all_digits"): 325,
                (325, "delim_num_deci"): 326,
                (325, "all_digits"): 327,
                (327, "delim_num_deci"): 328,
                (327, "all_digits"): 329,
                (329, "delim_num_deci"): 330,
                (329, "all_digits"): 331,
                (331, "delim_num_deci"): 332,
                (331, "all_digits"): 333,
                (333, "delim_num_deci"): 334,
            },
        )

        # TODO: Distinguish negative from subtract
        self._num_literal_machine = StateMachine(
            initial=0,
            final={
                301: FinalState(TokenType.NUM_LITERAL),
                304: FinalState(TokenType.NUM_LITERAL),
                306: FinalState(TokenType.NUM_LITERAL),
                308: FinalState(TokenType.NUM_LITERAL),
                310: FinalState(TokenType.NUM_LITERAL),
                312: FinalState(TokenType.NUM_LITERAL),
                314: FinalState(TokenType.NUM_LITERAL),
                316: FinalState(TokenType.NUM_LITERAL),
                318: FinalState(TokenType.NUM_LITERAL),
                320: FinalState(TokenType.NUM_LITERAL),
            },
            transitions={
                (0, "0"): 300,
                (300, "delim_num_deci"): 301,
                (0, "-"): 302,
                (0, "digits"): 303,
                (302, "digit"): 303,
                (303, "delim_num_deci"): 304,
                (303, "all_digits"): 305,
                (303, "."): (self._deci_literal_machine, 322),
                (305, "delim_num_deci"): 306,
                (305, "all_digits"): 307,
                (305, "."): (self._deci_literal_machine, 322),
                (307, "delim_num_deci"): 308,
                (307, "all_digits"): 309,
                (307, "."): (self._deci_literal_machine, 322),
                (309, "delim_num_deci"): 310,
                (309, "all_digits"): 311,
                (309, "."): (self._deci_literal_machine, 322),
                (311, "delim_num_deci"): 312,
                (311, "all_digits"): 313,
                (311, "."): (self._deci_literal_machine, 322),
                (313, "delim_num_deci"): 314,
                (313, "all_digits"): 315,
                (313, "."): (self._deci_literal_machine, 322),
                (315, "delim_num_dec"): 316,
                (315, "all_digiits"): 317,
                (315, "."): (self._deci_literal_machine, 322),
                (317, "delim_num_deci"): 318,
                (317, "all_digits"): 319,
                (317, "."): (self._deci_literal_machine, 322),
                (319, "delim_num_deci"): 320,
                (319, "."): (self._deci_literal_machine, 322),
            },
        )

        self._s_comment_machine = StateMachine(
            initial=0,
            final={291: FinalState(TokenType.S_COMMENT)},
            transitions={
                (0, "#"): 289,
                (289, "all_word"): 290,
                (290, "all_word"): 290,
                (290, "delim_comment"): 291,
            },
        )

        self._m_comment_machine = StateMachine(
            initial=0,
            final={299: FinalState(TokenType.M_COMMENT)},
            transitions={
                (0, "'"): 292,
                (292, "'"): 293,
                (293, "'"): 294,
                (294, "all_mul_com"): 295,
                (295, "all_mul_com"): 295,
                (295, "'"): 296,
                (296, "'"): 297,
                (297, "'"): 298,
                (298, "delim_comment"): 299,
            },
        )

        self._machines = MachineGroup(
            [
                self._reserved_words_machine,
                self._identifiers_machine,
                self._reserved_symbols_machine,
                self._word_literal_machine,
                self._num_literal_machine,
                self._deci_literal_machine,
                self._s_comment_machine,
                self._m_comment_machine,
            ]
        )

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