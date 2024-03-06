import datetime
import pysimplestplus.compiler as sp
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

    now = datetime.datetime.now()
    date = now.strftime("%a %b %d %Y %H:%M:%S")
    python_version = os.popen("python --version").read()
    os_ = os.popen("uname").read()
    print(f"Simplest+ 2.2.0 {date} [{python_version[:-1]}] on {os_[:-1].lower()}")

    if mode == MODES[0]:
        run_lexical()
    elif mode == MODES[1]:
        run_syntax()
    else:
        pass


def run_lexical():
    while True:
        text = get_input()
        if text:
            tokens, errors = sp.run_lexical("<stdin>", text)

            if errors:
                for error in errors:
                    print(error.as_string())
            print("Tokens:", tokens)
            print()


def run_syntax():
    while True:
        text = get_input()
        if text:
            tokens, ast, errors = sp.run_syntax("<stdin>", text)

            if errors:
                for error in errors:
                    print(error.as_string())
            elif ast:
                print("AST:", ast)
            print()


def get_input():
    text = ""
    tmp_text = ""
    while True:
        try:
            prompt = ">>> " if not text or text[-2] != ":" else "... "
            tmp_text = input(prompt)
            if tmp_text.strip() in ["", "\n"]:
                break
            text += tmp_text + "\n"
            if tmp_text.strip() in ["exit"]:
                exit()
            if tmp_text.strip()[0] == "\t":
                continue
        except KeyboardInterrupt:
            # clear the ^C character
            print()
            print("Type 'exit' or ctrl + D to exit")
            text = ""
            break
    return text

cli()
