import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_block_comment_v1(self):
        inp = '''/* A C-style comment */'''
        self.assertTrue(TestLexer.test(inp,'<EOF>','LNH_001'))
    
    def test_block_comment_v2(self):
        inp = '''/* 
        A C-style comment */'''
        self.assertTrue(TestLexer.test(inp,'<EOF>','LNH_002'))

    def test_block_comment_v3(self):
        inp = '''/* 
        //A C-style comment */'''
        self.assertTrue(TestLexer.test(inp,'<EOF>','LNH_003'))

    def test_block_comment_v4(self):
        # check non-greedy
        inp = '''/* 
        //A C-style comment do*/*/'''
        self.assertTrue(TestLexer.test(inp,'*,/,<EOF>','LNH_004'))

    def test_inline_comment_v1(self):
        inp = '''// A C++ style comment'''
        self.assertTrue(TestLexer.test(inp,'<EOF>','LNH_005'))

    def test_inline_comment_v2(self):
        inp = '''a=5// A C++ style comment'''
        self.assertTrue(TestLexer.test(inp,'a,=,5,<EOF>','LNH_006'))

    def test_lowercase_identifier(self):
        '''test identifiers'''
        self.assertTrue(TestLexer.test('abc', 'abc,<EOF>','LNH_007'))

    def test_interger_literal(self):
        self.assertTrue(TestLexer.test('01', '0,1,<EOF>','LNH_008'))

    def test_interger_remove_underscore(self):
        self.assertTrue(TestLexer.test('1_01', '101,<EOF>','LNH_009'))

    def test_float_literal(self):
        self.assertTrue(TestLexer.test('1.234 1.2e3 7E-10 1_234.567 .2e+2', 
            '1.234,1.2e3,7E-10,1234.567,.2e+2,<EOF>','LNH_010'))

    def test_bool_literal(self):
        self.assertTrue(TestLexer.test('false true', 'false,true,<EOF>','LNH_011'))

    def test_string_literal_v1(self):
        inp = '''"This is a string containing escape sequences \\t \\b \\f \\r \\n \\t \\\\ \\' \\""'''
        out = '''"This is a string containing escape sequences \\t \\b \\f \\r \\n \\t \\\\ \\' \\"",<EOF>'''
        self.assertTrue(TestLexer.test(inp, out,'LNH_012'))

    def test_string_literal_v2(self):
        inp = '''"This is a string containing non-ASCII char \\""'''
        out = '''"This is a string containing non-ASCII char \\"",<EOF>'''
        self.assertTrue(TestLexer.test(inp, out,'LNH_013'))

    def test_array_literal(self):
        self.assertTrue(TestLexer.test('{1, 5, 7, 12}', '{,1,,,5,,,7,,,12,},<EOF>', 'LNH_014'))

    def test_unclosed_string(self):
        inp = '''a = b + c"This is a string containing escape sequences \\t \\b \\f \\r \\n \\t \\\\ \\' \\"'''
        out = '''a,=,b,+,c,Unclosed String: This is a string containing escape sequences \\t \\b \\f \\r \\n \\t \\\\ \\' \\"'''
        self.assertTrue(TestLexer.test(inp, out,'LNH_015'))
    
    def test_unclosed_string_v2(self):
        inp = '''a = b + c"This is a string containing escape sequences'''
        out = '''a,=,b,+,c,Unclosed String: This is a string containing escape sequences'''
        self.assertTrue(TestLexer.test(inp, out,'LNH_016'))

    def test_illegal_excapse_v1(self):
        inp = '''"This is a string containing non-ASCII char \\ "'''
        out = '''Illegal Escape In String: This is a string containing non-ASCII char \ '''
        self.assertTrue(TestLexer.test(inp, out,'LNH_017'))

    def test_token_err(self):
        inp = '''abcâabc'''
        out = '''abc,Error Token â'''
        self.assertTrue(TestLexer.test(inp, out,'LNH_018'))