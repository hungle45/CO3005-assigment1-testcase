import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/mt22/parser/' in sys.path:
    sys.path.append('./main/mt22/parser/')
if os.path.isdir('../target/main/mt22/parser') and not '../target/main/mt22/parser/' in sys.path:
    sys.path.append('../target/main/mt22/parser/')
from MT22Lexer import MT22Lexer
from MT22Parser import MT22Parser
from lexererr import *
import subprocess

JASMIN_JAR = "./external/jasmin.jar"
LEXER_TEST_DIR = "../CO3005-assigment1-testcase/lexer/testcases/"
LEXER_SOL_DIR = "../CO3005-assigment1-testcase/lexer/solutions/"
LEXER_DETAIL_DIR = "../CO3005-assigment1-testcase/lexer/details/"
PARSER_TEST_DIR = "../CO3005-assigment1-testcase/parser/testcases/"
PARSER_SOL_DIR = "../CO3005-assigment1-testcase/parser/solutions"
Lexer = MT22Lexer
Parser = MT22Parser

token_names = {}
for name, value in MT22Lexer.__dict__.items():
    if isinstance(value, int) and name == name.upper():
        token_names[value] = name

class TestUtil:
    @staticmethod
    def makeSource(testdir, inputStr, num):
        filename = testdir + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input, expect, num):
        num = str(num)
        inputfile = TestUtil.makeSource(LEXER_TEST_DIR,input, num)
        TestLexer.check(LEXER_DETAIL_DIR, LEXER_SOL_DIR, inputfile, num)
        dest = open(LEXER_SOL_DIR + num + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(detaildir, soldir, inputfile, num):
        num = str(num)
        sol_dest = open(os.path.join(soldir, num + ".txt"), "w")
        detail_dest = open(os.path.join(detaildir, num + ".txt"), "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(detail_dest, sol_dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            sol_dest.write(err.message)
        finally:
            sol_dest.close()
            detail_dest.close()

    @staticmethod
    def printLexeme(detail_dest, sol_dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            detail_dest.write(f'{tok.text} --> TOKEN_{token_names[tok.type]}\n')
            sol_dest.write(tok.text+",")
            TestLexer.printLexeme(detail_dest, sol_dest, lexer)
        else:
            detail_dest.write("<EOF>")
            sol_dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        num = str(num)
        inputfile = TestUtil.makeSource(PARSER_TEST_DIR,input, num)
        TestParser.check(PARSER_SOL_DIR, inputfile, num)
        dest = open(PARSER_SOL_DIR + num + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        num = str(num)
        dest = open(os.path.join(soldir, num + ".txt"), "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()