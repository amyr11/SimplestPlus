from .lexical_analyzer import Lexer

class SimplestPlusCompiler:
    def __init__(self, code):
        self.code = code
        self.lexer = Lexer(self.code)
        self.tokens = []
        self.errors = []
    
    def run(self):
        self.lexical_analysis()

    def lexical_analysis(self):
        tokens, errors = self.lexer.tokenize()

        self.tokens = tokens
        self.errors = self.errors + errors

    def syntax_analysis(self):
        pass