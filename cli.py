import pysimplestplus as simp
import os
import sys

MODES = ["lexical", "syntax", "compile"]


def print_no_file_found(path):
    print(f"{path} doesn't exist.")
    print()


def print_invalid_mode():
    print(f"Invalid mode. ({MODES})")
    print()


def cli():
    mode = sys.argv[1]

    if mode not in MODES:
        print_invalid_mode()
        return

    if mode == MODES[0]:
        run_lexical()
    elif mode == MODES[1]:
        run_syntax()
    else:
        pass


def run_lexical():
    while True:
        text = input("simplest+ > ")
        tokens, errors = simp.run_lexical("<stdin>", text)

        if errors:
            for error in errors:
                print(error.as_string())
        elif tokens:
            print("Tokens:", tokens)
        print()


def run_syntax():
    while True:
        text = input("simplest+ > ")
        tokens, ast, errors = simp.run_syntax("<stdin>", text)

        if errors:
            for error in errors:
                print(error.as_string())
        elif ast:
            print("AST:", ast)
        print()


cli()
