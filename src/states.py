from .tokens import TokenType
from .machine import FinalState, MachineGroup, StateMachine

identifiers_machine = StateMachine(
    name="identifiers",
    initial=0,
    final={272: FinalState(TokenType.IDENTIFIER)},
    transitions={
        (0, "all_alpha"): 271,
        (271, "all_id"): 271,
        (271, "delim_id"): 272,
    },
)

reserved_words_machine = StateMachine(
    name="reserved_words",
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
        106: FinalState(TokenType.INHERITS),
        115: FinalState(TokenType.INITIALIZE),
        117: FinalState(TokenType.INP),
        123: FinalState(TokenType.INSTEAD),
        127: FinalState(TokenType.NEW),
        129: FinalState(TokenType.NO),
        131: FinalState(TokenType.NOT),
        134: FinalState(TokenType.NUM),
        137: FinalState(TokenType.OR),
        140: FinalState(TokenType.OUT),
        147: FinalState(TokenType.PARENT),
        153: FinalState(TokenType.RANGE),
        163: FinalState(TokenType.RESTRICTED),
        168: FinalState(TokenType.SELF),
        172: FinalState(TokenType.SKIP),
        176: FinalState(TokenType.STOP),
        183: FinalState(TokenType.UNLESS),
        191: FinalState(TokenType.VISIBLE),
        196: FinalState(TokenType.WIKI),
        200: FinalState(TokenType.WORD),
        204: FinalState(TokenType.YES),
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
        (93, "h"): 100,
        (100, "e"): 101,
        (101, "r"): 102,
        (102, "i"): 103,
        (103, "t"): 104,
        (104, "s"): 105,
        (105, "delim_reserve"): 106,
        (93, "i"): 107,
        (107, "t"): 108,
        (108, "i"): 109,
        (109, "a"): 110,
        (110, "l"): 111,
        (111, "i"): 112,
        (112, "z"): 113,
        (113, "e"): 114,
        (114, "delim_func"): 115,
        (93, "p"): 116,
        (116, "delim_func"): 117,
        (93, "s"): 118,
        (118, "t"): 119,
        (119, "e"): 120,
        (120, "a"): 121,
        (121, "d"): 122,
        (122, "delim_colon"): 123,
        (0, "n"): 124,
        (124, "e"): 125,
        (125, "w"): 126,
        (126, "delim_reserve"): 127,
        (124, "o"): 128,
        (128, "delim_value"): 129,
        (128, "t"): 130,
        (130, "delim_reserve"): 131,
        (124, "u"): 132,
        (132, "m"): 133,
        (133, "delim_dtype"): 134,
        (0, "o"): 135,
        (135, "r"): 136,
        (136, "delim_reserve"): 137,
        (135, "u"): 138,
        (138, "t"): 139,
        (139, "delim_func"): 140,
        (0, "p"): 141,
        (141, "a"): 142,
        (142, "r"): 143,
        (143, "e"): 144,
        (144, "n"): 145,
        (145, "t"): 146,
        (146, "delim_access"): 147,
        (0, "r"): 148,
        (148, "a"): 149,
        (149, "n"): 150,
        (150, "g"): 151,
        (151, "e"): 152,
        (152, "delim_func"): 153,
        (148, "e"): 154,
        (154, "s"): 155,
        (155, "t"): 156,
        (156, "r"): 157,
        (157, "i"): 158,
        (158, "c"): 159,
        (159, "t"): 160,
        (160, "e"): 161,
        (161, "d"): 162,
        (162, "delim_reserve"): 163,
        (0, "s"): 164,
        (164, "e"): 165,
        (165, "l"): 166,
        (166, "f"): 167,
        (167, "delim_access"): 168,
        (164, "k"): 169,
        (169, "i"): 170,
        (170, "p"): 171,
        (171, "delim_break"): 172,
        (164, "t"): 173,
        (173, "o"): 174,
        (174, "p"): 175,
        (175, "delim_break"): 176,
        (0, "u"): 177,
        (177, "n"): 178,
        (178, "l"): 179,
        (179, "e"): 180,
        (180, "s"): 181,
        (181, "s"): 182,
        (182, "delim_reserve"): 183,
        (0, "v"): 184,
        (184, "i"): 185,
        (185, "s"): 186,
        (186, "i"): 187,
        (187, "b"): 188,
        (188, "l"): 189,
        (189, "e"): 190,
        (190, "delim_reserve"): 191,
        (0, "w"): 192,
        (192, "i"): 193,
        (193, "k"): 194,
        (194, "i"): 195,
        (195, "delim_reserve"): 196,
        (192, "o"): 197,
        (197, "r"): 198,
        (198, "d"): 199,
        (199, "delim_dtype"): 200,
        (0, "y"): 201,
        (201, "e"): 202,
        (202, "s"): 203,
        (203, "delim_value"): 204,
    },
    fallback=identifiers_machine,
)

reserved_symbols_machine = StateMachine(
    name="reserved_symbols",
    initial=0,
    final={
        206: FinalState(TokenType.SPACE),
        208: FinalState(TokenType.TAB),
        209: FinalState(TokenType.NEWLINE, retract=False),
        211: FinalState(TokenType.MULTIPLY),
        213: FinalState(TokenType.MULTIPLY_ASSIGN),
        215: FinalState(TokenType.POWER),
        217: FinalState(TokenType.POWER_ASSIGN),
        219: FinalState(TokenType.PLUS),
        221: FinalState(TokenType.PLUS_ASSIGN),
        223: FinalState(TokenType.MINUS),
        225: FinalState(TokenType.MINUS_ASSIGN),
        227: FinalState(TokenType.DIVIDE),
        229: FinalState(TokenType.DIVIDE_ASSIGN),
        231: FinalState(TokenType.FLOOR),
        233: FinalState(TokenType.FLOOR_ASSIGN),
        235: FinalState(TokenType.MODULO),
        237: FinalState(TokenType.MODULO_ASSIGN),
        239: FinalState(TokenType.ASSIGN),
        241: FinalState(TokenType.EQUAL_TO),
        244: FinalState(TokenType.NOT_EQUAL),
        246: FinalState(TokenType.GREATER_THAN),
        248: FinalState(TokenType.GREATER_THAN_EQUAL),
        250: FinalState(TokenType.LESS_THAN),
        252: FinalState(TokenType.LESS_THAN_EQUAL),
        254: FinalState(TokenType.OPAR),
        256: FinalState(TokenType.CPAR),
        258: FinalState(TokenType.OBRACE),
        260: FinalState(TokenType.CBRACE),
        262: FinalState(TokenType.OBRACK),
        264: FinalState(TokenType.CBRACK),
        266: FinalState(TokenType.COMMA),
        268: FinalState(TokenType.PERIOD),
        270: FinalState(TokenType.COLON),
    },
    transitions={
        (0, " "): 205,
        (205, "delim_space"): 206,
        (0, "\t"): 207,
        (207, "delim_tab"): 208,
        (0, "\n"): 209,
        (0, "*"): 210,
        (210, "delim_arith"): 211,
        (210, "="): 212,
        (212, "delim_arith"): 213,
        (210, "*"): 214,
        (214, "delim_arith"): 215,
        (214, "="): 216,
        (216, "delim_arith"): 217,
        (0, "+"): 218,
        (218, "delim_plus"): 219,
        (218, "="): 220,
        (220, "delim_plus"): 221,
        (0, "-"): 222,
        (222, "delim_arith"): 223,
        (222, "="): 224,
        (224, "delim_arith"): 225,
        (0, "/"): 226,
        (226, "delim_arith"): 227,
        (226, "="): 228,
        (228, "delim_arith"): 229,
        (226, "/"): 230,
        (230, "delim_arith"): 231,
        (230, "="): 232,
        (232, "delim_arith"): 233,
        (0, "%"): 234,
        (234, "delim_arith"): 235,
        (234, "="): 236,
        (236, "delim_arith"): 237,
        (0, "="): 238,
        (238, "delim_assign"): 239,
        (238, "="): 240,
        (240, "delim_plus"): 241,
        (0, "!"): 242,
        (242, "="): 243,
        (243, "delim_plus"): 244,
        (0, ">"): 245,
        (245, "delim_arith"): 246,
        (245, "="): 247,
        (247, "delim_arith"): 248,
        (0, "<"): 249,
        (249, "delim_arith"): 250,
        (249, "="): 251,
        (251, "delim_arith"): 252,
        (0, "("): 253,
        (253, "delim_opar"): 254,
        (0, ")"): 255,
        (255, "delim_cpar"): 256,
        (0, "{"): 257,
        (257, "delim_obrace"): 258,
        (0, "}"): 259,
        (259, "delim_cbrace"): 260,
        (0, "["): 261,
        (261, "delim_obrack"): 262,
        (0, "]"): 263,
        (263, "delim_cbrack"): 264,
        (0, ","): 265,
        (265, "delim_comma"): 266,
        (0, "."): 267,
        (267, "delim_period"): 268,
        (0, ":"): 269,
        (269, "delim_comma"): 270,
    },
)

word_literal_machine = StateMachine(
    name="word_literal",
    initial=0,
    final={313: FinalState(TokenType.WORD_LITERAL)},
    transitions={
        (0, '"'): 311,
        (311, '"'): 312,
        (311, "all_word_wo_bs"): 311,
        (311, "\\"): 314,
        (312, "delim_word"): 313,
        (314, "all_word"): 311,
        (314, '"'): 315,
        (315, '"'): 312,
        (315, "all_word"): 311,
    },
)

deci_literal_machine = StateMachine(
    name="deci_literal",
    initial=337,
    final={
        340: FinalState(TokenType.DECI_LITERAL),
        342: FinalState(TokenType.DECI_LITERAL),
        344: FinalState(TokenType.DECI_LITERAL),
        346: FinalState(TokenType.DECI_LITERAL),
        348: FinalState(TokenType.DECI_LITERAL),
        350: FinalState(TokenType.DECI_LITERAL),
    },
    transitions={
        (337, "."): 338,
        (338, "all_digits"): 339,
        (339, "delim_num_deci"): 340,
        (339, "all_digits"): 341,
        (341, "delim_num_deci"): 342,
        (341, "all_digits"): 343,
        (343, "delim_num_deci"): 344,
        (343, "all_digits"): 345,
        (345, "delim_num_deci"): 346,
        (345, "all_digits"): 347,
        (347, "delim_num_deci"): 348,
        (347, "all_digits"): 349,
        (349, "delim_num_deci"): 350,
    },
)

num_literal_machine = StateMachine(
    name="num_literal",
    initial=0,
    final={
        317: FinalState(TokenType.NUM_LITERAL),
        320: FinalState(TokenType.NUM_LITERAL),
        322: FinalState(TokenType.NUM_LITERAL),
        324: FinalState(TokenType.NUM_LITERAL),
        326: FinalState(TokenType.NUM_LITERAL),
        328: FinalState(TokenType.NUM_LITERAL),
        330: FinalState(TokenType.NUM_LITERAL),
        332: FinalState(TokenType.NUM_LITERAL),
        334: FinalState(TokenType.NUM_LITERAL),
        336: FinalState(TokenType.NUM_LITERAL),
    },
    transitions={
        (0, "0"): 316,
        (316, "delim_num_deci"): 317,
        (316, "."): (deci_literal_machine, 338),
        (0, "-"): 318,
        (0, "digits"): 319,
        (318, "digits"): 319,
        (319, "delim_num_deci"): 320,
        (319, "all_digits"): 321,
        (319, "."): (deci_literal_machine, 338),
        (321, "delim_num_deci"): 322,
        (321, "all_digits"): 323,
        (321, "."): (deci_literal_machine, 338),
        (323, "delim_num_deci"): 324,
        (323, "all_digits"): 325,
        (323, "."): (deci_literal_machine, 338),
        (325, "delim_num_deci"): 326,
        (325, "all_digits"): 327,
        (325, "."): (deci_literal_machine, 338),
        (327, "delim_num_deci"): 328,
        (327, "all_digits"): 329,
        (327, "."): (deci_literal_machine, 338),
        (329, "delim_num_deci"): 330,
        (329, "all_digits"): 331,
        (329, "."): (deci_literal_machine, 338),
        (331, "delim_num_deci"): 332,
        (331, "all_digits"): 333,
        (331, "."): (deci_literal_machine, 338),
        (333, "delim_num_deci"): 334,
        (333, "all_digits"): 335,
        (333, "."): (deci_literal_machine, 338),
        (335, "delim_num_deci"): 336,
        (335, "."): (deci_literal_machine, 338),
    },
)

s_comment_machine = StateMachine(
    name="s_comment",
    initial=0,
    final={353: FinalState(TokenType.S_COMMENT)},
    transitions={
        (0, "#"): 351,
        (351, "all_word"): 352,
        (352, "all_word"): 352,
        (352, "delim_comment"): 353,
    },
)

m_comment_machine = StateMachine(
    name="m_comment",
    initial=0,
    final={363: FinalState(TokenType.M_COMMENT)},
    transitions={
        (0, "'"): 354,
        (354, "'"): 355,
        (355, "'"): 356,
        (356, "\n"): 357,
        (357, "\n"): 357,
        (357, "all_mul_com"): 358,
        (358, "all_mul_com"): 358,
        (358, "\n"): 359,
        (359, "\n"): 359,
        (359, " "): 359,
        (359, "all_mul_com_wo_sq_s"): 358,
        (359, "'"): 360,
        (360, "'"): 361,
        (360, "all_mul_com_wo_sq"): 358,
        (361, "'"): 362,
        (361, "all_mul_com_wo_sq"): 358,
        (362, "delim_comment"): 363,
        (362, "all_mul_com"): 358,
    },
)

machines = MachineGroup(
    [
        reserved_words_machine,
        identifiers_machine,
        reserved_symbols_machine,
        word_literal_machine,
        num_literal_machine,
        deci_literal_machine,
        s_comment_machine,
        m_comment_machine,
    ]
)
