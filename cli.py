import pysimplestplus as simp

while True:
    text = input("simplest+ > ")
    tokens, errors = simp.run("<stdin>", text)

    if errors:
        print("Tokens:", tokens)
        print()
        for error in errors:
            print(error.as_string())
    elif tokens:
        print("Tokens:", tokens)
    print()
