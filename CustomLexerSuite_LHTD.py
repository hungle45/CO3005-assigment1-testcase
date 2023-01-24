import unittest
from CustomTestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lexer0(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 0))
        
    def test_lexer1(self):
        input = """{"}"""
        expect = """{,Unclosed String: }"""
        self.assertTrue(TestLexer.test(input, expect, 1))

    def test_lexer2(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))

    def test_lexer3(self):
        input = "// abcd"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 3))

    def test_lexer4(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 4))

    def test_lexer5(self):
        input = "// this is a line comment /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 5))
    
    def test_lexer6(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 6))

    def test_lexer7(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """\\"aadadddldld\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 7))

    def test_lexer8(self):
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 8))

    def test_lexer9(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 9))

    def test_lexer10(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 10))

    def test_lexer11(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 11))

    def test_lexer12(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: \\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 12))

    def test_lexer13(self):
        input = """ "        " """
        expect = """        ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 13))

    def test_lexer14(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))

    def test_lexer15(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))

    def test_lexer16(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 16))

    def test_lexer17(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 17))

    def test_lexer18(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 18))
    
    def test_lexer19(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 19))
    
    def test_lexer20(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
    
    def test_lexer21(self):
        self.assertTrue(TestLexer.test(""" abvccd """, """abvccd,<EOF>""", 21))
        
        
    def test_lexer22(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 22))

    def test_lexer23(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 23))
        
    def test_lexer24(self):
        input = '""'
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
        
    def test_lexer25(self):
        input = '''
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
                }
            '''
        expect = "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
        
    def test_lexer26(self):
        input = '''
            foo(2 + x, 4.0 / y);
            goo();
            '''
        expect = "foo,(,2,+,x,,,4.0,/,y,),;,goo,(,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 26))
        
    def test_lexer27(self):
        input = '''
            {
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
                s = r * r * myPI;
                a[0] = s;
            }
            '''
        expect = "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 27))
        
    def test_lexer28(self):
        input = '''
            "
            "
            '''
        expect = "Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 28))
        
    def test_lexer29(self):
        input = '''
            "103_5940"
            '''
        expect = "103_5940,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 29))
        
    def test_lexer30(self):
        input = '''
            1039_390_9024_
            '''
        expect = "10393909024,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 30))
        
    def test_lexer31(self):
        self.assertTrue(TestLexer.test("!a%5&&b||c+*", "!,a,%,5,&&,b,||,c,+,*,<EOF>", 31))

    def test_lexer32(self):
        self.assertTrue(TestLexer.test("a==b==01234!=43210<3>4", "a,==,b,==,0,1234,!=,43210,<,3,>,4,<EOF>", 32))

    def test_lexer33(self):
        self.assertTrue(TestLexer.test("*and<=>mod<\\<=", "*,and,<=,>,mod,<,Error Token \\", 33))

    def test_lexer34(self):
        self.assertTrue(TestLexer.test("/*this is a cmt*/", "<EOF>", 34))

    def test_lexer35(self):
        self.assertTrue(TestLexer.test("//hjhjhuhu/*youare live */", "<EOF>", 35))

    def test_lexer36(self):
        self.assertTrue(TestLexer.test("//hello my friend \n asda", "asda,<EOF>", 36))

    def test_lexer37(self):
        self.assertTrue(TestLexer.test("/*hello my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 37))

    def test_lexer38(self):
        self.assertTrue(TestLexer.test("asf aso Dowoad ", "asf,aso,Dowoad,<EOF>", 38))

    def test_lexer39(self):
        self.assertTrue(TestLexer.test("hello tat ca moi nguoi", "hello,tat,ca,moi,nguoi,<EOF>", 39))

    def test_lexer40(self):
        self.assertTrue(TestLexer.test("thu thu abc () ", "thu,thu,abc,(,),<EOF>", 40))

    def test_lexer41(self):
        self.assertTrue(TestLexer.test("01 10 001 100", "0,1,10,0,0,1,100,<EOF>", 41))

    def test_lexer42(self):
        self.assertTrue(TestLexer.test("0.1 0399 20_39 true false 0.3e55","0.1,0,399,2039,true,false,0.3e55,<EOF>", 42))

    def test_lexer43(self):
        self.assertTrue(TestLexer.test("5.e5 6. 5.e-8","5.e5,6.,5.e-8,<EOF>", 43))

    def test_lexer44(self):
        self.assertTrue(TestLexer.test("anD then false", "anD,then,false,<EOF>", 44))

    def test_lexer45(self):
        self.assertTrue(TestLexer.test("sTRIng False", "sTRIng,False,<EOF>", 45))

    def test_lexer46(self):
        self.assertTrue(TestLexer.test(""" ",dls\\F12" """, """Illegal Escape In String: ,dls\\F""", 46))

    def test_lexer47(self):
        input = "a88jdjij + a2x - 40 > 12"
        expect = "a88jdjij,+,a2x,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 47))

    def test_lexer48(self):
        input = "as<.>iooi"
        expect = "as,<,.,>,iooi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_lexer49(self):
        input = "[;]12kkkasijiasdijANXNMXMM\t"
        expect = "[,;,],12,kkkasijiasdijANXNMXMM,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 49))

    def test_lexer50(self):
        input = ":a:sxassa:,irejgioj0990hiju."
        expect = ":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 50))
        
    def test_lexer51(self):
        input = '''
            x: integer = 65;
            mess: function integer(n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInt(delta);
            }
        '''
        expect = "x,:,integer,=,65,;,mess,:,function,integer,(,n,:,integer,),{,return,n,/,50,*,2,;,},main,:,function,void,(,),{,delta,:,integer,=,mess,(,7,),;,printInt,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 51))

    def test_lexer52(self):
        input = '''
            add: function integer(n: integer){
                sum: integer = 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                }
                return sum;
            }
            main: function void () {
                delta: integer = add(10);
                printInt(delta);
            }
        '''
        expect = "add,:,function,integer,(,n,:,integer,),{,sum,:,integer,=,0,;,for,(,i,=,0,,,i,<=,n,,,i,+,1,),{,sum,=,sum,+,i,;,},return,sum,;,},main,:,function,void,(,),{,delta,:,integer,=,add,(,10,),;,printInt,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 52))

    def test_lexer53(self):
        input = '''
            x: integer = 65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInt(x);
            }
        '''
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInt,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 53))

    def test_lexer54(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i--;
                }
                return  i;
            }
        '''
        expect = "main,:,function,void,(,),{,i,:,integer,=,10,;,while,(,i,!=,0,),{,i,-,-,;,},return,i,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 54))

    def test_lexer55(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i+=2;
                }
                return  i;
            }
        '''
        expect = "main,:,function,void,(,),{,i,:,integer,=,10,;,while,(,i,>,20,),{,i,+,=,2,;,},return,i,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 55))

    def test_lexer56(self):
        input = '''
            voidA: function integer(n: integer){
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInt(x);
            }
        '''
        expect = "voidA,:,function,integer,(,n,:,integer,),{,return,n,%,10,;,},voidB,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,voidA,(,delta,),;,},main,:,function,void,(,),{,delta,:,integer,=,5,;,voidB,(,x,,,delta,),;,printInt,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 56))

    def test_lexer57(self):
        input = '''
            main: function void () {
                delta: string = "dat";
                printString(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,string,=,dat,;,printString,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 57))

    def test_lexer58(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,float,=,3.45,;,printFloat,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 58))

    def test_lexer59(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,boolean,=,true,;,printBoolean,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 59))

    def test_lexer60(self):
        input = '''
            main: function void () {
                b: array [5] of integer = [1,2,3,4,6];
                printInt(b[4]);
            }
        '''
        expect = "main,:,function,void,(,),{,b,:,array,[,5,],of,integer,=,[,1,,,2,,,3,,,4,,,6,],;,printInt,(,b,[,4,],),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 60))

    def test_lexer61(self):
        input = "a = true, b = false"
        expect = "a,=,true,,,b,=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_lexer62(self):
        input = """ "abc\\e def" """
        expect = """Illegal Escape In String: abc\\e"""
        self.assertTrue(TestLexer.test(input, expect, 62))
    
    def test_lexer63(self):
        input = """ "ab'c\\n def" """
        expect = """ab'c\\n def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_lexer64(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 64))

    def test_lexer65(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 65))

    def test_lexer66(self):
        input = """a= "He said: " Im Super'Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,He said: ,Im,Super,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 66))

    def test_lexer67(self):
        input = """a= "He said: " Hello " \n ";"""
        expect = """a,=,He said: ,Hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 67))

    def test_lexer68(self):
        input = """a = "Hello \n world !";"""
        expect = """a,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(input, expect, 68))

    def test_lexer69(self):
        input = '{1,"an\\t",3}'
        expect = "{,1,,,an\\t,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 69))

    def test_lexer70(self):
        input = "{2.3, 4.2, 102e3}"
        expect = "{,2.3,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 70))

    def test_lexer71(self):
        input = "a[4] = {1, 2,  3, 4}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 71))

    def test_lexer72(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 72))

    def test_lexer73(self):
        input = "v[5] a;"
        expect = "v,[,5,],a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 73))

    def test_lexer74(self):
        input = "a[3 + x.foo(2)] = a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 74))

    def test_lexer75(self):
        input = "s=r*r*myPI;"
        expect = "s,=,r,*,r,*,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 75))

    def test_lexer76(self):
        input = "1/2"
        expect = "1,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 76))

    def test_lexer77(self):
        input = """ " \\h " """
        expect = """Illegal Escape In String:  \h"""
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_lexer78(self):
        input = """ " \\naaa\\t" """
        expect = """ \\naaa\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 78))

    def test_lexer79(self):
        input = "{}"
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 79))

    def test_lexer80(self):
        input = """{"}"""
        expect = """{,Unclosed String: }"""
        self.assertTrue(TestLexer.test(input, expect, 80))

    def test_lexer81(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 81))

    def test_lexer82(self):
        input = "//{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_lexer83(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 83))

    def test_lexer84(self):
        input = '''
                // this is a line comment"
                kakf
        '''
        expect = "kakf,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 84))
    
    def test_lexer85(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 85))

    def test_lexer86(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """\\"aadadddldld\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 86))

    def test_lexer87(self):
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 87))

    def test_lexer88(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 88))

    def test_lexer89(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_lexer90(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 90))

    def test_lexer91(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: \\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 91))

    def test_lexer92(self):
        input = """ "        " """
        expect = """        ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 92))

    def test_lexer93(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 93))

    def test_lexer94(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 94))

    def test_lexer95(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_lexer96(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 96))

    def test_lexer97(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 97))
    
    def test_lexer98(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 98))
    
    def test_lexer99(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 99))
    
    def test_lexer100(self):
        self.assertTrue(TestLexer.test(""" abvccd """, """abvccd,<EOF>""", 100))
        
        
