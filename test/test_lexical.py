from prettytable import PrettyTable

from src.lexer import Lexer

with open("samples/sample.simp", "r") as f:
    sample_code = f.read()

lexer = Lexer(sample_code)

tokens, errors = lexer.tokenize(verbose=True)


table = PrettyTable()
table.field_names = ["Lexeme", "Token"]
table.align = "l"

for token in tokens:
    table.add_row([token.val_string(), token.token_string()])

print(table)

print()

for error in errors:
    print(error.as_string())