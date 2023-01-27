import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_01(self):
        inp = ''' /* A C-style comment */ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 101))

    def test_02(self):
        inp = ''' /*\n A C-style comment \n*/ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 102))

    def test_03(self):
        inp = ''' /*\n // inline comment in block comment \n*/ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 103))

    def test_04(self):
        inp = ''' /* check non-greedy */*/ '''
        expect = '''*,/,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 104))

    def test_05(self):
        inp = '''a=5// A C++ style comment'''
        expect = '''a,=,5,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 105))

    def test_06(self):
        inp = '''/* comment */ abc // another comment'''
        expect = '''abc,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 106))

    def test_07(self):
        inp = '''_Le_Hung_45 hungle45'''
        expect = '''_Le_Hung_45,hungle45,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 107))

    def test_08(self):
        inp = '''4hung5le'''
        expect = '''4,hung5le,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 108))

    def test_09(self):
        inp = '''auto break boolean do'''
        expect = '''auto,break,boolean,do,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 109))

    def test_10(self):
        inp = '''else false float for'''
        expect = '''else,false,float,for,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 110))

    def test_11(self):
        inp = '''function if integer return'''
        expect = '''function,if,integer,return,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 111))

    def test_12(self):
        inp = '''string true while void out'''
        expect = '''string,true,while,void,out,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 112))

    def test_13(self):
        inp = '''continue of inherit array'''
        expect = '''continue,of,inherit,array,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 113))

    def test_14(self):
        inp = ''' a+b-12/c%d!false '''
        expect = '''a,+,b,-,12,/,c,%,d,!,false,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 114))

    def test_15(self):
        inp = ''' 500 >> 6 < 10 '''
        expect = '''500,>,>,6,<,10,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 115))

    def test_16(self):
        inp = ''' &&&&||||!===>=>=<=<=:::: '''
        expect = '''&&,&&,||,||,!=,==,>=,>=,<=,<=,::,::,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 116))

    def test_17(self):
        inp = ''' a&b '''
        expect = '''a,Error Token &'''
        self.assertTrue(TestLexer.test(inp, expect, 117))

    def test_18(self):
        inp = ''' a|b '''
        expect = '''a,Error Token |'''
        self.assertTrue(TestLexer.test(inp, expect, 118))

    def test_19(self):
        inp = ''' a:b '''
        expect = '''a,:,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 119))

    def test_20(self):
        inp = '''1234 123'''
        expect = '''1234,123,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 120))

    def test_21(self):
        inp = '''01'''
        expect = '''0,1,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 121))    

    def test_22(self):
        inp = '''1_72 1_234_567'''
        expect = '''172,1234567,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 122))

    def test_23(self):
        inp = '''0_123 0_0'''
        expect = '''0,_123,0,_0,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 123))

    def test_24(self):
        inp = '''123_'''
        expect = '''123,_,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 124))

    def test_25(self):
        inp = '''_123'''
        expect = '''_123,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 125))

    def test_26(self):
        inp = '''1.234E+5 0.123e-6'''
        expect = '''1.234E+5,0.123e-6,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 126))

    def test_27(self):
        inp = '''1.E+2'''
        expect = '''1.E+2,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 127))

    def test_28(self):
        inp = '''0.0E0 0.0e0'''
        expect = '''0.0E0,0.0e0,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 128))

    def test_29(self):
        inp = '''.012e34 .123E-3'''
        expect = '''.012e34,.123E-3,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 129))

    def test_30(self):
        inp = '''1E-2 0e0'''
        expect = '''1E-2,0e0,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 130))

    def test_31(self):
        inp = '''1.23 0.0 1.'''
        expect = '''1.23,0.0,1.,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 131))

    def test_32(self):
        inp = '''1_234.567 1_2.03e4 1_2.'''
        expect = '''1234.567,12.03e4,12.,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 132))

    def test_33(self):
        inp = '''1_234_.567e1'''
        expect = '''1234,_,.567e1,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 133))

    def test_34(self):
        inp = '''123.4_5'''
        expect = '''123.4,_5,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 134))

    def test_35(self):
        inp = '''123e6_2'''
        expect = '''123e6,_2,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 135))

    def test_36(self):
        inp = ''' "This is normal string" '''
        expect = '''This is normal string,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 136))

    def test_37(self):
        inp = ''' "This is a string containing tab \\t" '''
        expect = '''This is a string containing tab \\t,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 137))

    def test_38(self):
        inp = ''' "He asked me: \\"What\\' your name?\\"" '''
        expect = '''He asked me: \\"What\\' your name?\\",<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 138))

    def test_39(self):
        inp = ''' "This string contains all supported escape sequence \\b\\f\\r\\n\\t\\\'\\\\\\". The end" '''
        expect = '''This string contains all supported escape sequence \\b\\f\\r\\n\\t\\\'\\\\\\". The end,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 139))

    def test_40(self):
        inp = ''' "Normal string '''
        expect = '''Unclosed String: Normal string '''
        self.assertTrue(TestLexer.test(inp, expect, 140))

    def test_41(self):
        inp = ''' "Hello world\\ . Goodbye" '''
        expect = '''Illegal Escape In String: Hello world\\ '''
        self.assertTrue(TestLexer.test(inp, expect, 141))

    def test_42(self):
        inp = ''' "Hung \\abc Hung" '''
        expect = '''Illegal Escape In String: Hung \\a'''
        self.assertTrue(TestLexer.test(inp, expect, 142))

    def test_43(self):
        inp = ''' " '''
        expect = '''Unclosed String:  '''
        self.assertTrue(TestLexer.test(inp, expect, 143))

    def test_44(self):
        inp = ''' "Hung's code" '''
        expect = '''Hung's code,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 144))

    def test_45(self):
        inp = ''' \\b '''
        expect = '''Error Token \\'''
        self.assertTrue(TestLexer.test(inp, expect, 145))

    def test_46(self):
        inp = ''' a?b '''
        expect = '''a,Error Token ?'''
        self.assertTrue(TestLexer.test(inp, expect, 146))

    def test_47(self):
        inp = ''' $'hi' '''
        expect = '''Error Token $'''
        self.assertTrue(TestLexer.test(inp, expect, 147))

    def test_48(self):
        inp = ''' ~true '''
        expect = '''Error Token ~'''
        self.assertTrue(TestLexer.test(inp, expect, 148))

    def test_49(self):
        inp = ''' a^b'''
        expect = '''a,Error Token ^'''
        self.assertTrue(TestLexer.test(inp, expect, 149))

    def test_50(self):
        inp = ''' {1, 2, 3, 4} '''
        expect = '''{,1,,,2,,,3,,,4,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 150))

    def test_51(self):
        inp = ''' {"a", "b", "c"} '''
        expect = '''{,a,,,b,,,c,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 151))

    def test_52(self):
        inp = ''' 1 + (-2) = -1'''
        expect = '''1,+,(,-,2,),=,-,1,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 152))

    def test_53(self):
        inp = ''' "b"" '''
        expect = '''b,Unclosed String:  '''
        self.assertTrue(TestLexer.test(inp, expect, 153))

    def test_54(self):
        inp = ''' "line\nline" '''
        expect = '''Unclosed String: line'''
        self.assertTrue(TestLexer.test(inp, expect, 154))

    def test_55(self):
        inp = ''' { 1, "a\\tb", 2} '''
        expect = '''{,1,,,a\\tb,,,2,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 155))

    def test_56(self):
        inp = ''' "" '''
        expect = ''',<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 156))

    def test_57(self):
        inp = ''' {} '''
        expect = '''{,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 157))

    def test_58(self):
        inp = ''' { "", ""} '''
        expect = '''{,,,,,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 158))

    def test_59(self):
        inp = ''' "/* comment in string */" '''
        expect = '''/* comment in string */,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 159))

    def test_60(self):
        inp = ''' "/* comment in string */ '''
        expect = '''Unclosed String: /* comment in string */ '''
        self.assertTrue(TestLexer.test(inp, expect, 160))

    def test_61(self):
        inp = ''' /* \\a */ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 161))

    def test_62(self):
        inp = ''' // \\nabc '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 162))

    def test_63(self):
        inp = ''' {/* comment */ 4, 5} '''
        expect = '''{,4,,,5,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 163))

    def test_64(self):
        inp = ''' /* comment "*/"'''
        expect = '''Unclosed String: '''
        self.assertTrue(TestLexer.test(inp, expect, 164))

    def test_65(self):
        inp = ''' .00e00 '''
        expect = '''.00e00,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 165))

    def test_66(self):
        inp = '''00e00 '''
        expect = '''0,0e00,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 166))

    def test_67(self):
        inp = ''' "//abc" '''
        expect = '''//abc,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 167))

    def test_68(self):
        inp = ''' "//abc '''
        expect = '''Unclosed String: //abc '''
        self.assertTrue(TestLexer.test(inp, expect, 168))

    def test_69(self):
        inp = ''' "@!#" '''
        expect = '''@!#,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 169))

    def test_70(self):
        inp = ''' #abc '''
        expect = '''Error Token #'''
        self.assertTrue(TestLexer.test(inp, expect, 170))

    def test_71(self):
        inp = ''''''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 171))

    def test_72(self):
        inp = ''' /*/* comment */ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 172))

    def test_73(self):
        inp = ''' a = i++ '''
        expect = '''a,=,i,+,+,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 173))

    def test_74(self):
        inp = '''
        {
            r, s: int;
            r = 2.0;
            a, b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
        }
        '''
        expect = '''{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 174))

    def test_75(self):
        inp = '''
        for (i = 1, i < 10, i + 1) {
            writeInt(i);
        }
        '''
        expect = '''for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 175))

    def test_76(self):
        inp = ''' "1+1=3" '''
        expect = '''1+1=3,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 176))

    def test_77(self):
        inp = ''' ____ '''
        expect = '''____,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 177))

    def test_78(self):
        inp = ''' _" '''
        expect = '''_,Unclosed String:  '''
        self.assertTrue(TestLexer.test(inp, expect, 178))

    def test_79(self):
        inp = ''' a += 1 '''
        expect = '''a,+,=,1,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 179))

    def test_80(self):
        inp = ''' !== '''
        expect = '''!=,=,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 180))

    def test_81(self):
        inp = ''' \\"" '''
        expect = '''Error Token \\'''
        self.assertTrue(TestLexer.test(inp, expect, 181))

    def test_82(self):
        inp = ''' __init__ '''
        expect = '''__init__,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 182))

    def test_83(self):
        inp = ''' /* \n a \n a \n */ '''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 183))

    def test_84(self):
        inp = ''' "\r" '''
        expect = '''Unclosed String: '''
        self.assertTrue(TestLexer.test(inp, expect, 184))

    def test_85(self):
        inp = ''' -1 '''
        expect = '''-,1,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 185))

    def test_86(self):
        inp = ''' a[0, 0] '''
        expect = '''a,[,0,,,0,],<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 186))

    def test_87(self):
        inp = ''' a: interger = 12'''
        expect = '''a,:,interger,=,12,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 187))

    def test_88(self):
        inp = ''' out n : float '''
        expect = '''out,n,:,float,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 188))

    def test_89(self):
        inp = '''
        main : function void () {
            delta : integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        '''
        expect = '''main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 189))

    def test_90(self):
        inp = '''
        if (true)
            if (false)
                a = b
            else
                a = c
        '''
        expect = '''if,(,true,),if,(,false,),a,=,b,else,a,=,c,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 190))

    def test_91(self):
        inp = '''foo(x,y);'''
        expect = '''foo,(,x,,,y,),;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 191))

    def test_92(self):
        inp = ''' /* ???? */'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 192))

    def test_93(self):
        inp = ''' // ????'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 193))

    def test_94(self):
        inp = ''' "hungle\\4 " '''
        expect = '''Illegal Escape In String: hungle\\4'''
        self.assertTrue(TestLexer.test(inp, expect, 194))

    def test_95(self):
        inp = ''' // comment /* another comment */ abc'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 195))

    def test_96(self):
        inp = ''' _@bc '''
        expect = '''_,Error Token @'''
        self.assertTrue(TestLexer.test(inp, expect, 196))

    def test_97(self):
        inp = ''' 1.2.3 '''
        expect = '''1.2,.,3,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 197))

    def test_98(self):
        inp = ''' """ '''
        expect = ''',Unclosed String:  '''
        self.assertTrue(TestLexer.test(inp, expect, 198))

    def test_99(self):
        inp = '''\n\n\n'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 199))

    def test_100(self):
        inp = '''_true'''
        expect = '''_true,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 200))