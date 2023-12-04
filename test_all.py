from prettytable import PrettyTable
from src.lexer import Lexer
import os

test_folder = "test_files"
test_sub_folders = ["lexical"]
all_passed = True  # Initialize all_passed as True
error_files = {}  # Initialize a dictionary to store file paths and error objects

for folder in test_sub_folders:
    test_folder_path = test_folder + "/" + folder
    test_files = os.listdir(test_folder_path)
    for file in test_files:
        file_path = test_folder_path + "/" + file
        with open(file_path, "r") as f:
            test_file = f.read()
        lexer = Lexer(test_file)
        tokens, errors = lexer.tokenize(verbose=False)
        table = PrettyTable(["Lexeme", "Token", "Line", "Column"])
        for token in tokens:
            row, col = token.get_position()
            table.add_row([token.val_string(), token.token_string(), row, col])
        if len(errors) > 0:
            all_passed = False  # Set all_passed to False if there are errors
            error_files[f"{folder}/{file}"] = errors  # Add the error file to the list
            print(f"(Failed) {folder}/{file}")
        else:
            print(f"(Passed) {folder}/{file}")
        print(f"\n{table}\n")
        print()

if all_passed:
    print("All files passed")
else:
    print(f"{len(error_files)} file/s produced errors:\n")
    for file_path in error_files:
        print("*" * 50)
        print(file_path)
        print("*" * 50 + "\n")
        for error in error_files[file_path]:
            print(error.as_string())
