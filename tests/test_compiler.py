import unittest
import sys
import os
sys.path.append("./")
import pysimplestplus.compiler as sp


class TestSyntax(unittest.TestCase):

    def _tokenize(self, code):
        lexer = sp.Lexer("<test>", code)
        tokens, errors = lexer.make_tokens()

        self.assertIsNone(errors)
        self.assertIsNotNone(tokens)

        return tokens

    def _read(self, file_path):
        with open(file_path, "r") as file:
            code = file.read()
            return code

    def _get_test_codes(self, folder):
        test_codes = []

        for file in os.listdir(folder):
            if file.endswith(".simp"):
                test_codes.append(folder + file)

        return test_codes

    def _run_syntax(self, file, func):
        code = self._read(file)
        tokens = self._tokenize(code)
        parser = sp.Parser(tokens)
        res = parser.parse(func)

        return res.node, res.error

    def _test_positive_node(self, path, func, expected_node):
        test_codes = self._get_test_codes(path)

        for file in test_codes:
            node, error = self._run_syntax(file, func)

            self.assertIsNone(error, file)
            self.assertIsNotNone(node, file)
            self.assertIsInstance(node, expected_node, file)

    def _test_negative(self, path, func):
        test_codes = self._get_test_codes(path)

        for file in test_codes:
            node, error = self._run_syntax(file, func)

            self.assertIsNotNone(error, file)

    def test_program(self):
        self._test_positive_node("tests/syntax/program/positive/", "program", sp.ProgramNode)
        self._test_negative("tests/syntax/program/negative/", "program")

    def test_global(self):
        self._test_positive_node("tests/syntax/global/positive/dec_stmt/", "global_", sp.DeclarationsNode)
        self._test_positive_node("tests/syntax/global/positive/func_def/", "global_", sp.FuncDefNode)
        self._test_negative("tests/syntax/global/negative/", "global_")


if __name__ == '__main__':
    unittest.main()
