import unittest
from CustomTestUtils import TestLexer


class LexerSuite(unittest.TestCase):

#----------------- [TEST IDENTIFIER] -----------------#
    def test_1(self):
        self.assertTrue(TestLexer.test(""" k """,
        "k,<EOF>", "HTK_101"))
    
    def test_2(self):
        self.assertTrue(TestLexer.test(""" kien """,
        "kien,<EOF>","HTK_102"))

    def test_3(self):
        self.assertTrue(TestLexer.test(""" _kien """,
        "_kien,<EOF>","HTK_103"))

    def test_4(self):
        self.assertTrue(TestLexer.test(""" _kien_ """,
        "_kien_,<EOF>","HTK_104"))

    def test_5(self):
        self.assertTrue(TestLexer.test(""" _1k_ """,
        "_1k_,<EOF>","HTK_105"))

    def test_6(self):
        self.assertTrue(TestLexer.test(""" 1k_ """,
        "1,k_,<EOF>","HTK_106"))

    def test_7(self):
        self.assertTrue(TestLexer.test(""" k1 """,
        "k1,<EOF>","HTK_107"))

    def test_8(self):
        self.assertTrue(TestLexer.test(""" k_1 """,
        "k_1,<EOF>","HTK_108"))

#----------------- [TEST INTERGER AND FLOAT] -----------------#
    def test_9(self):
        self.assertTrue(TestLexer.test(""" -7.6 -5 ""","-,7.6,-,5,<EOF>","HTK_115"))
    def test_10(self):
        self.assertTrue(TestLexer.test(""" 0 123456789 """,
        "0,123456789,<EOF>","HTK_110"))

    def test_11(self):
        self.assertTrue(TestLexer.test(""" 0 1_2_3_4_5_6_7_8_9 """,
        "0,123456789,<EOF>","HTK_111"))

    def test_12(self): # note
        self.assertTrue(TestLexer.test(""" 0_00 02_3_4 """,
        "0,_00,0,234,<EOF>","HTK_112"))

    def test_13(self):
        self.assertTrue(TestLexer.test(""" 123.123e123 123.e-123 """,
        "123.123e123,123.e-123,<EOF>","HTK_113"))

    def test_14(self):
        self.assertTrue(TestLexer.test(""" 1_2_3.123e123 1_2_3.e-1_2_3 """,
        "123.123e123,123.e-1,_2_3,<EOF>","HTK_114"))

    def test_15(self):
        self.assertTrue(TestLexer.test(""" 123.123e123 123.123 123e123 .123e123 .e123 """,
        "123.123e123,123.123,123e123,.123e123,.e123,<EOF>","HTK_115"))

    def test_16(self):
        self.assertTrue(TestLexer.test(""" 0_0_0.000e000 """,
        "0,_0_0,.000e000,<EOF>","HTK_116"))

    def test_17(self):
        self.assertTrue(TestLexer.test(""" 123. 1_2_3. """,
        "123.,123.,<EOF>","HTK_117"))

    def test_18(self):
        self.assertTrue(TestLexer.test(""" 123.12_3 123.12e4_5 """,
        "123.12,_3,123.12e4,_5,<EOF>","HTK_118"))

    def test_19(self): # note
        self.assertTrue(TestLexer.test(""" 0123.E-123 """,
        "0,123.E-123,<EOF>","HTK_119"))
    
#----------------- [TEST STRINGLIT] -----------------#
    def test_20(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
        """He asked me: \\"Where is John?\\",<EOF>""","HTK_120"))

    def test_21(self):
        self.assertTrue(TestLexer.test(""" "HA TRUNG KIEN  " """,
        "HA TRUNG KIEN  ,<EOF>","HTK_121"))

    def test_22(self):
        self.assertTrue(TestLexer.test(""" "Ha '" Trung '" Kien" """,
        "Ha ',Trung,Error Token '","HTK_122"))

    def test_23(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\b \\f \\r \\n \\t \\' \\\\" """,
        "Ha Trung Kien \\b \\f \\r \\n \\t \\' \\\\,<EOF>","HTK_123"))

    def test_24(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung \\Kien" """,
        "Illegal Escape In String: Ha Trung \K","HTK_124"))

    def test_25(self):
        self.assertTrue(TestLexer.test(""" "Ha
        Trung Kien" """,
        "Unclosed String: Ha","HTK_125"))

    def test_26(self):
        self.assertTrue(TestLexer.test(""" "" """,
        ",<EOF>","HTK_126"))

    def test_27(self):
        self.assertTrue(TestLexer.test(""" "## Ha Trung Kien ##" """,
        "## Ha Trung Kien ##,<EOF>","HTK_127"))
    
    def test_28(self):
        self.assertTrue(TestLexer.test(""" "// Ha Trung Kien" """,
        "// Ha Trung Kien,<EOF>","HTK_128"))
    
    def test_29(self):
        self.assertTrue(TestLexer.test(""" "/* Ha Trung Kien */" """,
        "/* Ha Trung Kien */,<EOF>","HTK_129"))

    def test_30(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien """,
        "Unclosed String: Ha Trung Kien ","HTK_130"))

    def test_31(self):
        self.assertTrue(TestLexer.test(""" "Ha'Trung'Kien" """,
        "Ha'Trung'Kien,<EOF>","HTK_131"))

    def test_32(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien\ """,
        "Illegal Escape In String: Ha Trung Kien\\ ","HTK_132"))

    def test_33(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung'Kien" """,
        "Ha Trung'Kien,<EOF>","HTK_133"))

    def test_34(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\t" """,
        "Ha Trung Kien \\t,<EOF>","HTK_134"))

    def test_35(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\\\ """,
        "Unclosed String: Ha Trung Kien \\\\ ","HTK_135"))

    def test_36(self):
        self.assertTrue(TestLexer.test(""" "Kien dep trai" """,
        "Kien dep trai,<EOF>","HTK_136"))

    def test_37(self): # cái dấu \" là python nó sẽ chuyển thành "
        self.assertTrue(TestLexer.test(""" "Anh'\" """,
        "Anh',<EOF>","HTK_137"))

    def test_38(self):
        self.assertTrue(TestLexer.test(""" "Anh' """,
        "Unclosed String: Anh' ","HTK_138"))
    
    def test_39(self):
        self.assertTrue(TestLexer.test(""" "Ha \\n Trung \\n Kien" """,
        "Ha \\n Trung \\n Kien,<EOF>","HTK_139"))

    def test_40(self):
        self.assertTrue(TestLexer.test(""" "Ha \\n """,
        "Unclosed String: Ha \\n ","HTK_140"))

    def test_41(self):
        self.assertTrue(TestLexer.test(""" "_@x#" """,
        "_@x#,<EOF>","HTK_141"))
#----------------- [TEST BOOLEAN] -----------------#
    def test_42(self):
        self.assertTrue(TestLexer.test(""" true """,
        "true,<EOF>","HTK_142"))
    def test_43(self):
        self.assertTrue(TestLexer.test(""" false """,
        "false,<EOF>","HTK_143"))
    def test_44(self):
        self.assertTrue(TestLexer.test(""" truetrue """,
        "truetrue,<EOF>","HTK_144"))

#----------------- [TEST COMMENT] -----------------#
    def test_45(self):
        self.assertTrue(TestLexer.test("""//An inline cmt \n/* before a block cmt*/ """,
        "<EOF>","HTK_145"))

    def test_46(self):
        self.assertTrue(TestLexer.test("""/*This is a block cmt*/ """,
        """<EOF>""","HTK_146"))
    def test_47(self):
        self.assertTrue(TestLexer.test(""" /* inside this block cmt is a smtblk{int a;}*/ """,
        "<EOF>","HTK_147"))

    def test_48(self):
        self.assertTrue(TestLexer.test(""" /* unclosed block cmt""",
        "/,*,unclosed,block,cmt,<EOF>","HTK_148"))

    def test_49(self):
        self.assertTrue(TestLexer.test(""" /* escape in block cmt \t*/""" ,
        "<EOF>","HTK_149"))

    def test_50(self):
        self.assertTrue(TestLexer.test("/*block cmt1*/ /*block cmt2*/",
        "<EOF>","HTK_150"))

    def test_51(self):
        self.assertTrue(TestLexer.test("""//A line cmt #contains a line cmt/n """,
        "<EOF>","HTK_151"))

    def test_52(self):
        self.assertTrue(TestLexer.test(""" /* a block cmt /*cover a block cmt*/ */""",
        "*,/,<EOF>","HTK_152"))

    def test_53(self):
        self.assertTrue(TestLexer.test(""" /* A block cmt // includes a line cmt*/ """,
        "<EOF>","HTK_153"))

    def test_54(self):
        self.assertTrue(TestLexer.test(""" /* This block cmt is followed by*/ //An inline cmt """,
        "<EOF>","HTK_154"))

    def test_55(self):
        self.assertTrue(TestLexer.test(""" /*Big block cmt //with small inline cmt\n */ """,
        "<EOF>","HTK_155"))    
#----------------- [TEST KEYWORD] -----------------#
    def test_56(self):
        self.assertTrue(TestLexer.test(""" auto break of """,
        "auto,break,of,<EOF>","HTK_156"))

    def test_57(self):
        self.assertTrue(TestLexer.test(""" if else """,
        "if,else,<EOF>","HTK_157"))

    def test_58(self):  
        self.assertTrue(TestLexer.test(" break continue",
        "break,continue,<EOF>","HTK_160"))

    def test_59(self):
        self.assertTrue(TestLexer.test(" void return",
        "void,return,<EOF>","HTK_161"))

    def test_60(self):
        self.assertTrue(TestLexer.test(" int void float",
        "int,void,float,<EOF>","HTK_162"))

#----------------- [TEST TOKEN] -----------------#
    def test_61(self):
        self.assertTrue(TestLexer.test(""" Ha Trung Kien #---# """,
        "Ha,Trung,Kien,Error Token #","HTK_161"))

    def test_62(self):
        self.assertTrue(TestLexer.test(""" Ha ' Trung ' Kien """,
        "Ha,Error Token '","HTK_162"))

    def test_63(self):
        self.assertTrue(TestLexer.test(""" Ha & Trung & Kien """,
        "Ha,Error Token &","HTK_163"))

    def test_64(self):
        self.assertTrue(TestLexer.test(""" Ha # Trung # Kien """,
        "Ha,Error Token #","HTK_164"))

    def test_65(self):
        self.assertTrue(TestLexer.test(""" + - * / { } [ ] ( ) """,
        "+,-,*,/,{,},[,],(,),<EOF>","HTK_165"))

    def test_66(self):
        self.assertTrue(TestLexer.test(""" Ha | Trung | Kien """,
        "Ha,Error Token |","HTK_166"))

    def test_67(self):
        self.assertTrue(TestLexer.test(""" Ha || Trung || Kien """,
        "Ha,||,Trung,||,Kien,<EOF>","HTK_167"))

    def test_68(self):
        self.assertTrue(TestLexer.test(""" Ha && Trung && Kien """,
        "Ha,&&,Trung,&&,Kien,<EOF>","HTK_168"))


    def test_69(self):
        self.assertTrue(TestLexer.test(""" Ha||Trung||Kien """,
        "Ha,||,Trung,||,Kien,<EOF>","HTK_169"))

    def test_70(self):
        self.assertTrue(TestLexer.test(""" Ha&&Trung&&Kien """,
        "Ha,&&,Trung,&&,Kien,<EOF>","HTK_170"))

    def test_71(self):
        self.assertTrue(TestLexer.test(""" HaNewTrung(Kien)+Anh """,
        "HaNewTrung,(,Kien,),+,Anh,<EOF>","HTK_171"))

    ##################################################
    ##################################################

    def test_75(self): 
        self.assertTrue(TestLexer.test(""" 
        main: function void () {
            delta: int = fact (3);
            inc(x, delta);
            printint(x);
        """,
        "main,:,function,void,(,),{,delta,:,int,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,<EOF>","HTK_175"))

    def test_76(self): 
        self.assertTrue(TestLexer.test(""" 
        inc: function void (out n: int, delta: int) 
        """,
        "inc,:,function,void,(,out,n,:,int,,,delta,:,int,),<EOF>","HTK_176"))

    def test_77(self): 
        self.assertTrue(TestLexer.test(""" out n : int   """,
        "out,n,:,int,<EOF>","HTK_177"))

    def test_78(self):
        self.assertTrue(TestLexer.test(""" Ha(Trung+Kien[Anh])  """,
        "Ha,(,Trung,+,Kien,[,Anh,],),<EOF>","HTK_178"))

    def test_79(self):
        self.assertTrue(TestLexer.test(""" array [2, 3] of string """,
        "array,[,2,,,3,],of,string,<EOF>","HTK_179"))

    def test_80(self): 
        self.assertTrue(TestLexer.test("""  array [2, 3] of integer """,
        "array,[,2,,,3,],of,integer,<EOF>","HTK_180"))
 
    def test_81(self): 
        self.assertTrue(TestLexer.test(""" x,y,z: int = 1,2,3; """,
        "x,,,y,,,z,:,int,=,1,,,2,,,3,;,<EOF>","HTK_181"))

    def test_82(self): 
        self.assertTrue(TestLexer.test(""" x: int = 65; """,
        "x,:,int,=,65,;,<EOF>","HTK_182"))

    def test_83(self): 
        self.assertTrue(TestLexer.test(""" 
         for (i = 1, i < 10, i + 1) {
            writeInt(i);
        }  
        """,
        "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>","HTK_183"))

    def test_84(self): 
        self.assertTrue(TestLexer.test(""" 1_2_3+86-10*1_2_3.00e22%48 """,
        "123,+,86,-,10,*,123.00e22,%,48,<EOF>","HTK_184"))

    def test_85(self):
        self.assertTrue(TestLexer.test(""" true+false - 0001_2_3_4 """,
        "true,+,false,-,0,0,0,1234,<EOF>","HTK_185"))

    def test_86(self): 
        self.assertTrue(TestLexer.test(""" 
        {
            r, s: int;
            r = 2.0;
            a,b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
        } 
        """,
        "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>","HTK_186"))

    def test_87(self):
        self.assertTrue(TestLexer.test(""" !!====.||+.... """,
        "!,!=,==,=,.,||,+,.,.,.,.,<EOF>","HTK_187"))
    
    def test_88(self): 
        self.assertTrue(TestLexer.test(""" goo() """,
        "goo,(,),<EOF>","HTK_188"))

    def test_89(self): 
        self.assertTrue(TestLexer.test(""" foo( 2 + x, 4.0 / y) """,
        "foo,(,2,+,x,,,4.0,/,y,),<EOF>","HTK_189"))

#----------------- [TEST ADDITIONAL] -----------------#
    def test_72(self):
        self.assertTrue(TestLexer.test("$no idea","Error Token $","HTK_172"))

    def test_73(self):
        self.assertTrue(TestLexer.test(""" \"Open the string \h \"""",
        """Illegal Escape In String: Open the string \h""","HTK_173"))

    def test_74(self):
        self.assertTrue(TestLexer.test(""" \"Open the string \n\"""",
        """Unclosed String: Open the string ""","HTK_174"))
    
    def test_90(self):
        self.assertTrue(TestLexer.test(""" 0123.E-123 """,
        "0,123.E-123,<EOF>","HTK_190"))

    def test_91(self):
        self.assertTrue(TestLexer.test(""" "1+1-2,true" """,
        "1+1-2,true,<EOF>","HTK_191"))

    def test_92(self): 
        self.assertTrue(TestLexer.test("""
        a [2, 3] of integer;
        x: int = a[0,0];
        """,
        "a,[,2,,,3,],of,integer,;,x,:,int,=,a,[,0,,,0,],;,<EOF>","HTK_192"))
 
    def test_93(self):
        self.assertTrue(TestLexer.test(""" a1b2c3 ___ _ """,
        "a1b2c3,___,_,<EOF>""HTK_,93"))
 
    def test_94(self): 
        self.assertTrue(TestLexer.test(""" (1+2+3).abc::789;; """,
        "(,1,+,2,+,3,),.,abc,::,789,;,;,<EOF>","HTK_194"))

    def test_95(self): 
        self.assertTrue(TestLexer.test(""" "Ha::"Trung"||"Kien"&&Yeu+Em """,
        "Ha::,Trung,||,Kien,Unclosed String: &&Yeu+Em ","HTK_195"))

    def test_96(self):
        self.assertTrue(TestLexer.test(""" 123.12_3 123.12e4_5 """,
        "123.12,_3,123.12e4,_5,<EOF>""HTK_,96"))


    def test_97(self):
        self.assertTrue(TestLexer.test(""" false&&//array(1,2,3)+4-5||true##""",
        "false,&&,<EOF>","HTK_197"))
 
    def test_98(self):
        self.assertTrue(TestLexer.test(""" String out comment //"String in comment""",
        "String,out,comment,<EOF>","HTK_198"))

    def test_99(self):
        self.assertTrue(TestLexer.test(""" x = 4 + 5; """,
        "x,=,4,+,5,;,<EOF>","HTK_199"))

    def test_100(self): #note check again
        self.assertTrue(TestLexer.test(""" 
        x: int; 
        y: int = 5;
        if(x==5) y = 5
        else y = 4
        """,
        "x,:,int,;,y,:,int,=,5,;,if,(,x,==,5,),y,=,5,else,y,=,4,<EOF>","HTK_200"))

