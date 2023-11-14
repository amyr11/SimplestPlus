"""
-------------------
REGULAR DEFINITIONS
-------------------
"""


def without(l: list, chars: list[str]):
    return [char for char in l if char not in chars]


definitions = {}

# Sets
definitions["digits"] = list("123456789")
definitions["all_digits"] = [*definitions["digits"], "0"]
definitions["all_alpha"] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
definitions["alpha_num"] = [*definitions["all_alpha"], *definitions["all_digits"]]
definitions["arith_op"] = ["+", "-", "*", "/", "%"]
definitions["rel_op"] = ["=", "!", ">", "<"]
definitions["special_char"] = [
    *definitions["arith_op"],
    *definitions["rel_op"],
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
definitions["special_char_wo_dq"] = without(definitions["special_char"], ['"'])
definitions["special_char_wo_bs"] = without(definitions["special_char"], ["\\"])
definitions["special_char_wo_sq"] = without(definitions["special_char"], ["'"])
definitions["all_id"] = [*definitions["alpha_num"], "_"]
definitions["delim_word"] = [" ", "\n", ",", "]", ")", "}", "+", ":", "#", "!", "="]
definitions["all_word"] = [
    *definitions["alpha_num"],
    *definitions["special_char_wo_dq"],
    " ",
]
definitions["all_word_wo_bs"] = without(definitions["all_word"], ["\\"])
definitions["all_mul_com"] = [
    *definitions["alpha_num"],
    *definitions["special_char"],
    " ",
]
definitions["all_mul_com_wo_sq"] = [
    *definitions["alpha_num"],
    *definitions["special_char_wo_sq"],
    " ",
]

# Delims
definitions["delim_dtype"] = [" ", "("]
definitions["delim_break"] = [" ", "\n"]
definitions["delim_value"] = [" ", "\n", ")", "]", "}", ",", ":"]
definitions["delim_indent"] = [
    *definitions["all_alpha"],
    " ",
    "#",
    "'",
    '"',
    "}",
    "]",
    "{",
    ")",
]
definitions["delim_arith"] = [*definitions["alpha_num"], " ", "(", "-"]
definitions["delim_plus"] = [*definitions["alpha_num"], " ", "(", "-", '"']
definitions["delim_assign"] = [*definitions["alpha_num"], " ", "(", "-", '"', "{", "["]
definitions["delim_opar"] = [
    *definitions["alpha_num"],
    " ",
    "(",
    "-",
    '"',
    "[",
    "{",
    "(",
    ")",
    "\n",
]
definitions["delim_cpar"] = [
    *definitions["arith_op"],
    *definitions["rel_op"],
    " ",
    "\n",
    ":",
    ")",
    ",",
    "]",
    "}",
]
definitions["delim_obrace"] = [*definitions["all_alpha"], " ", "\n", '"']
definitions["delim_cbrace"] = [" ", "\n", ","]
definitions["delim_obrack"] = [
    *definitions["alpha_num"],
    " ",
    "\n",
    "-",
    "{",
    "[",
    "]",
    '"',
]
definitions["delim_cbrack"] = [" ", "\n", ",", "[", "]", ")", "}"]
definitions["delim_comma"] = [
    *definitions["alpha_num"],
    " ",
    "(",
    "-",
    '"',
    "[",
    "{",
    "(",
    ")",
    "\n",
]
definitions["delim_period"] = definitions["all_alpha"]
definitions["delim_id"] = [
    *definitions["arith_op"],
    *definitions["rel_op"],
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
definitions["delim_num_deci"] = [
    *definitions["arith_op"],
    *definitions["rel_op"],
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
definitions["delim_reserve"] = [" "]
definitions["delim_colon"] = [":"]
definitions["delim_func"] = ["("]
definitions["delim_comment"] = ["\n"]


# definitions['delim_space'] = definitions['alpha_num'] + definitions['arith_op'] + definitions['rel_op'] + ['\n', '(', '{', '[', ')', '}', ']', ',', ':', '"', '#']
# definitions['delim_newln'] = definitions['delim_indent'] + ['\n']


def getDefinitions():
    for key, val in definitions.items():
        if "delim" in key:
            val += ["\0"]

    return definitions


class DefTranslator:
    def __init__(self, definitions: dict[str, list[str]] | None = None):
        if definitions is None:
            definitions = getDefinitions()
        self.definitions = definitions

    def translate(self, inp) -> list[str]:
        ids = [inp]
        for id, symbols in self.definitions.items():
            if inp in symbols:
                ids.append(id)
        return ids
