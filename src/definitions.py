"""
-------------------
REGULAR DEFINITIONS
-------------------
"""
# TODO: Refactor reg def
definitions = {}

definitions["all_alpha"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
definitions["digits"] = list("123456789")
definitions["all_digits"] = definitions["digits"] + ["0"]
definitions["alpha_num"] = definitions["all_alpha"] + definitions["all_digits"]
definitions["arith_op"] = ["+", "-", "*", "/", "%"]
definitions["rel_op"] = ["=", "!", ">", "<"]
definitions["special_char"] = (
    definitions["arith_op"]
    + definitions["rel_op"]
    + [
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
)
definitions["special_char_wo_sq"] = [
    char for char in definitions["special_char"] if char != "'"
]
definitions["special_char_wo_bs"] = [
    char for char in definitions["special_char"] if char != "\\"
]
definitions["special_char_wo_dq"] = [
    char for char in definitions["special_char"] if char != '"'
]
definitions["delim_reserve"] = [" "]
definitions["delim_colon"] = [":"]
definitions["delim_func"] = ["("]
definitions["delim_dtype"] = [" ", "("]
definitions["delim_break"] = [" ", "\n"]
definitions["delim_value"] = definitions["delim_break"] + [")", "]", "}", ",", ":"]
definitions["delim_indent"] = definitions["all_alpha"] + [
    " ",
    "#",
    "'",
    '"',
    "}",
    "]",
    "{",
    ")",
]
definitions["delim_arith"] = (
    definitions["alpha_num"] + definitions["delim_dtype"] + ["-"]
)
definitions["delim_plus"] = definitions["delim_arith"] + ['"']
definitions["delim_minus"] = (
    definitions["digits"] + definitions["all_alpha"] + definitions["delim_dtype"]
)
definitions["delim_opar"] = definitions["delim_plus"] + ["[", "{", "(", ")", "\n"]
definitions["delim_cpar"] = (
    definitions["arith_op"]
    + definitions["rel_op"]
    + definitions["delim_break"]
    + [":", ")", ",", "]", "}"]
)
definitions["delim_obrace"] = (
    definitions["delim_break"] + definitions["all_alpha"] + ['"']
)
definitions["delim_cbrace"] = definitions["delim_break"] + [","]
definitions["delim_obrack"] = (
    definitions["delim_break"] + definitions["alpha_num"] + ["-", "{", "[", "]", '"']
)
definitions["delim_cbrack"] = definitions["delim_break"] + [",", "[", ")", "}"]
definitions["delim_comma"] = definitions["delim_opar"] + ["\n"]
definitions["delim_period"] = definitions["all_alpha"]
definitions["delim_id"] = (
    definitions["arith_op"]
    + definitions["rel_op"]
    + definitions["delim_break"]
    + ["(", "[", ")", ",", ".", ":", "#"]
)
definitions["all_id"] = definitions["alpha_num"] + ["_"]
definitions["delim_word"] = definitions["delim_break"] + [",", "]", ")", "+", ":", "#"]
definitions["all_word"] = (
    definitions["alpha_num"] + definitions["special_char_wo_dq"] + [" "]
)
definitions["all_word_wo_bs"] = (
    definitions["alpha_num"] + definitions["special_char_wo_bs"] + [" "]
)
definitions["all_mul_com"] = (
    definitions["alpha_num"] + definitions["special_char"] + [" "]
)
definitions["all_mul_com_wo_sq"] = (
    definitions["alpha_num"] + definitions["special_char_wo_sq"] + [" "]
)
definitions["delim_comment"] = ["\n"]
definitions["delim_num_deci"] = definitions["arith_op"] + [
    ",",
    "}",
    ")",
    "]",
    ":",
    "#",
    '"',
    " ",
    "\n",
]
# definitions['delim_space'] = definitions['alpha_num'] + definitions['arith_op'] + definitions['rel_op'] + ['\n', '(', '{', '[', ')', '}', ']', ',', ':', '"', '#']
# definitions['delim_newln'] = definitions['delim_indent'] + ['\n']


def getDefinitions():
    for key, val in definitions.items():
        if "delim" in key:
            val += ["\0"]

    return definitions


class DefTranslator:
    def __init__(self, definitions: dict[str, list[str]] = getDefinitions()):
        self.definitions = definitions

    def translate(self, inp) -> set[str]:
        ids = {inp}
        for id, symbols in definitions.items():
            if inp in symbols:
                ids.add(id)
        return ids
