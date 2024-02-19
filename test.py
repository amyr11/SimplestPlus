import pysimplestplus
import os
import sys

def print_no_file_found(path):
    print(f"{path} doesn't exist.")
    print()

def test_compile():
    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print_no_file_found(file_path)
        return

    with open(file_path, "r") as file:
        code = file.read()

    tokens, errors = pysimplestplus.run(file_path, code)

    if errors:
        print("Tokens:", tokens)
        print()
        for error in errors:
            print(error.as_string())
    else:
        print("Tokens:", tokens)
        print()
        print(f"{file_path} compiled successfully.")


test_compile()
