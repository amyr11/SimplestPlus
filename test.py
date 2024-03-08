import pysimplestplus.compiler as sp
import os
import sys

MODES = ['lexical', 'syntax', 'compile']

def print_no_file_found(path):
    print(f"{path} doesn't exist.")
    print()

def print_invalid_mode():
    print(f"Invalid mode. ({MODES})")
    print()

def test_compile():
    mode = sys.argv[1]
    file_path = sys.argv[2]

    if mode not in MODES:
        print_invalid_mode()
        return

    if not os.path.exists(file_path):
        print_no_file_found(file_path)
        return

    with open(file_path, "r") as file:
        code = file.read()

    if mode == MODES[0]:
        run_lexical(file_path, code)
    elif mode == MODES[1]:
        run_syntax(file_path, code)
    else:
        pass

def run_lexical(file_path, code):
    tokens, errors = sp.run_lexical(file_path, code)

    if errors:
        print("Tokens:", tokens)
        print()
        if errors:
            for error in errors:
                print(error.as_string())
    else:
        print("Tokens:", tokens)
        print()
        print(f"{file_path} compiled successfully.")


def run_syntax(file_path, code):
    tokens, ast, errors = sp.run_syntax(file_path, code)

    if errors:
        for error in errors:
            print(error.as_string())
    else:
        # print("AST:", ast)
        # print()
        print(f"{file_path} compiled successfully.")


test_compile()
