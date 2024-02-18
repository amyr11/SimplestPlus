from pysimplestplus.compiler import SimplestPlusCompiler
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
    
    compiler = SimplestPlusCompiler(code)
    compiler.run()

    if compiler.errors:
        for error in compiler.errors:
            print(error.as_string())
    else:
        print(f"{file_path} Compiled successfully.")

test_compile()