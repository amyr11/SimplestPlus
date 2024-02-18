from prettytable import PrettyTable
from pysimplestplus.lexical_analyzer import Lexer
import os
import sys


def test_lexical(file_path, verbose):
    with open(file_path, "r") as f:
        test_file = f.read()
    lexer = Lexer(test_file)
    tokens, errors = lexer.tokenize(verbose)
    table = PrettyTable(["Lexeme", "Token", "Line", "Column"])
    table.align = "l"
    for token in tokens:
        row, col = token.get_position()
        table.add_row([token.val_string().replace("\t", "\\t"), token.token_string(), row, col])
    if len(errors) > 0:
        print(f"(Failed) {file_path.split('/')[-1]}")
    else:
        print(f"(Passed) {file_path.split('/')[-1]}")
    print(f"\n{table}\n")
    print()

    return errors


def test_syntax(file_path, verbose):
    return []


def test_dir(mode_func, folder_path=""):
    all_passed = True
    error_files = {}  # Initialize a dictionary to store file paths and error objects
    test_files = os.listdir(folder_path)
    for file in test_files:
        file_path = os.path.join(folder_path, file)
        errors = mode_func(file_path, False)
        if errors:
            all_passed = False
        error_files[file] = errors

    file_errors_count = 0

    for file in error_files:
        if len(error_files[file]) > 0:
            print(f"(Failed) {file}")
            file_errors_count += 1
        else:
            print(f"(Passed) {file}")

    print()

    if all_passed:
        print("All files passed")
    else:
        print(f"{file_errors_count} file/s produced errors:\n")
        for file_path in error_files:
            if len(error_files[file_path]) == 0:
                continue
            print("*" * 50)
            print(file_path)
            print("*" * 50 + "\n")
            for error in error_files[file_path]:
                print(error.as_string())


def print_usage():
    print("Usage: python test.py <mode> [<file_path>] [-v]")
    print("\n<mode>:\n    'lexical'\n    'syntax'")
    print("\n<file_path>:\n    File name inside tests/lexical or tests/syntax only.")
    print("\n-v:\n    Verbose flag.")


def print_no_file_found(path):
    print(f"{path} doesn't exist.")
    print()
    print()
    print_usage()


def test():
    if len(sys.argv) == 1:
        print_usage()
        return

    mode = sys.argv[1]
    mode_func = test_lexical if mode == "lexical" else test_syntax

    if mode not in ["lexical", "syntax"]:
        print_usage()
        return

    file_path = None if len(sys.argv) < 3 else sys.argv[2]
    test_folder = "tests/lexical" if mode == "lexical" else "tests/syntax"

    verbose = False
    if len(sys.argv) == 4:
        verbose_arg = sys.argv[3]
        if verbose_arg != "-v":
            print_usage()
            return
        else:
            verbose = True

    if file_path:
        full_path = os.path.join(test_folder, file_path)
        if not os.path.exists(full_path):
            print_no_file_found(full_path)
            return

        errors = mode_func(full_path, verbose)
        for error in errors:
            print(error.as_string())
    else:
        test_dir(mode_func, test_folder)


test()
