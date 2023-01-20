import unittest
from CustomTestUtils import TestLexer


class LexerSuite(unittest.TestCase):

#----------------- [TEST IDENTIFIER] -----------------#
    def test_1(self):
        self.assertTrue(TestLexer.test(""" k """,
        "k,<EOF>", 101))
    
    def test_2(self):
        self.assertTrue(TestLexer.test(""" kien """,
        "kien,<EOF>",102))

    def test_3(self):
        self.assertTrue(TestLexer.test(""" _kien """,
        "_kien,<EOF>",103))

    def test_4(self):
        self.assertTrue(TestLexer.test(""" _kien_ """,
        "_kien_,<EOF>",104))

    def test_5(self):
        self.assertTrue(TestLexer.test(""" _1k_ """,
        "_1k_,<EOF>",105))

    def test_6(self):
        self.assertTrue(TestLexer.test(""" 1k_ """,
        "1,k_,<EOF>",106))

    def test_7(self):
        self.assertTrue(TestLexer.test(""" k1 """,
        "k1,<EOF>",107))

    def test_8(self):
        self.assertTrue(TestLexer.test(""" k_1 """,
        "k_1,<EOF>",108))

#----------------- [TEST INTERGER AND FLOAT] -----------------#
    def test_9(self):
        self.assertTrue(TestLexer.test(""" -7.6 -5 ""","-,7.6,-,5,<EOF>",115))
    def test_10(self):
        self.assertTrue(TestLexer.test(""" 0 123456789 """,
        "0,123456789,<EOF>",110))

    def test_11(self):
        self.assertTrue(TestLexer.test(""" 0 1_2_3_4_5_6_7_8_9 """,
        "0,123456789,<EOF>",111))

    def test_12(self): # note
        self.assertTrue(TestLexer.test(""" 0_00 02_3_4 """,
        "0,_00,0,234,<EOF>",112))

    def test_13(self):
        self.assertTrue(TestLexer.test(""" 123.123e123 123.e-123 """,
        "123.123e123,123.e-123,<EOF>",113))

    def test_14(self):
        self.assertTrue(TestLexer.test(""" 1_2_3.123e123 1_2_3.e-1_2_3 """,
        "123.123e123,123.e-1,_2_3,<EOF>",114))

    def test_15(self):
        self.assertTrue(TestLexer.test(""" 123.123e123 123.123 123e123 .123e123 .e123 """,
        "123.123e123,123.123,123e123,.123e123,.e123,<EOF>",115))

    def test_16(self):
        self.assertTrue(TestLexer.test(""" 0_0_0.000e000 """,
        "0,_0_0,.000e000,<EOF>",116))

    def test_17(self):
        self.assertTrue(TestLexer.test(""" 123. 1_2_3. """,
        "123.,123.,<EOF>",117))

    def test_18(self):
        self.assertTrue(TestLexer.test(""" 123.12_3 123.12e4_5 """,
        "123.12,_3,123.12e4,_5,<EOF>",118))

    def test_19(self): # note
        self.assertTrue(TestLexer.test(""" 0123.E-123 """,
        "0,123.E-123,<EOF>",119))
    
#----------------- [TEST STRINGLIT] -----------------#
    def test_20(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
        """He asked me: \\"Where is John?\\",<EOF>""",120))

    def test_21(self):
        self.assertTrue(TestLexer.test(""" "HA TRUNG KIEN  " """,
        "HA TRUNG KIEN  ,<EOF>",121))

    def test_22(self):
        self.assertTrue(TestLexer.test(""" "Ha '" Trung '" Kien" """,
        "Ha ',Trung,Error Token '",122))

    def test_23(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\b \\f \\r \\n \\t \\' \\\\" """,
        "Ha Trung Kien \\b \\f \\r \\n \\t \\' \\\\,<EOF>",123))

    def test_24(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung \\Kien" """,
        "Illegal Escape In String: Ha Trung \K",124))

    def test_25(self):
        self.assertTrue(TestLexer.test(""" "Ha
        Trung Kien" """,
        "Unclosed String: Ha",125))

    def test_26(self):
        self.assertTrue(TestLexer.test(""" "" """,
        ",<EOF>",126))

    def test_27(self):
        self.assertTrue(TestLexer.test(""" "## Ha Trung Kien ##" """,
        "## Ha Trung Kien ##,<EOF>",127))
    
    def test_28(self):
        self.assertTrue(TestLexer.test(""" "// Ha Trung Kien" """,
        "// Ha Trung Kien,<EOF>",128))
    
    def test_29(self):
        self.assertTrue(TestLexer.test(""" "/* Ha Trung Kien */" """,
        "/* Ha Trung Kien */,<EOF>",129))

    def test_30(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien """,
        "Unclosed String: Ha Trung Kien ",130))

    def test_31(self):
        self.assertTrue(TestLexer.test(""" "Ha'Trung'Kien" """,
        "Ha'Trung'Kien,<EOF>",131))

    def test_32(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien\ """,
        "Illegal Escape In String: Ha Trung Kien\\ ",132))

    def test_33(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung'Kien" """,
        "Ha Trung'Kien,<EOF>",133))

    def test_34(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\t" """,
        "Ha Trung Kien \\t,<EOF>",134))

    def test_35(self):
        self.assertTrue(TestLexer.test(""" "Ha Trung Kien \\\\ """,
        "Unclosed String: Ha Trung Kien \\\\ ",135))

    def test_36(self):
        self.assertTrue(TestLexer.test(""" "Kien dep trai" """,
        "Kien dep trai,<EOF>",136))

    def test_37(self): # cái dấu \" là python nó sẽ chuyển thành "
        self.assertTrue(TestLexer.test(""" "Anh'\" """,
        "Anh',<EOF>",137))

    def test_38(self):
        self.assertTrue(TestLexer.test(""" "Anh' """,
        "Unclosed String: Anh' ",138))
    
    def test_39(self):
        self.assertTrue(TestLexer.test(""" "Ha \\n Trung \\n Kien" """,
        "Ha \\n Trung \\n Kien,<EOF>",139))

    def test_40(self):
        self.assertTrue(TestLexer.test(""" "Ha \\n """,
        "Unclosed String: Ha \\n ",140))

    def test_41(self):
        self.assertTrue(TestLexer.test(""" "_@x#" """,
        "_@x#,<EOF>",141))
#----------------- [TEST BOOLEAN] -----------------#
    def test_42(self):
        self.assertTrue(TestLexer.test(""" true """,
        "true,<EOF>",142))
    def test_43(self):
        self.assertTrue(TestLexer.test(""" false """,
        "false,<EOF>",143))
    def test_44(self):
        self.assertTrue(TestLexer.test(""" truetrue """,
        "truetrue,<EOF>",144))

#----------------- [TEST COMMENT] -----------------#
    def test_45(self):
        self.assertTrue(TestLexer.test("""//An inline cmt \n/* before a block cmt*/ """,
        "<EOF>",145))

    def test_46(self):
        self.assertTrue(TestLexer.test("""/*This is a block cmt*/ """,
        """<EOF>""",146))
    def test_47(self):
        self.assertTrue(TestLexer.test(""" /* inside this block cmt is a smtblk{int a;}*/ """,
        "<EOF>",147))

    def test_48(self):
        self.assertTrue(TestLexer.test(""" /* unclosed block cmt""",
        "/,*,unclosed,block,cmt,<EOF>",148))

    def test_49(self):
        self.assertTrue(TestLexer.test(""" /* escape in block cmt \t*/""" ,
        "<EOF>",149))

    def test_50(self):
        self.assertTrue(TestLexer.test("/*block cmt1*/ /*block cmt2*/",
        "<EOF>",150))

    def test_51(self):
        self.assertTrue(TestLexer.test("""//A line cmt #contains a line cmt/n """,
        "<EOF>",151))

    def test_52(self):
        self.assertTrue(TestLexer.test(""" /* a block cmt /*cover a block cmt*/ */""",
        "*,/,<EOF>",152))

    def test_53(self):
        self.assertTrue(TestLexer.test(""" /* A block cmt // includes a line cmt*/ """,
        "<EOF>",153))

    def test_54(self):
        self.assertTrue(TestLexer.test(""" /* This block cmt is followed by*/ //An inline cmt """,
        "<EOF>",154))

    def test_55(self):
        self.assertTrue(TestLexer.test(""" /*Big block cmt //with small inline cmt\n */ """,
        "<EOF>",155))    
#----------------- [TEST KEYWORD] -----------------#
    def test_56(self):
        self.assertTrue(TestLexer.test(""" auto break of """,
        "auto,break,of,<EOF>",156))

    def test_57(self):
        self.assertTrue(TestLexer.test(""" if else """,
        "if,else,<EOF>",157))

    def test_58(self):  
        self.assertTrue(TestLexer.test(" break continue",
        "break,continue,<EOF>",160))

    def test_59(self):
        self.assertTrue(TestLexer.test(" void return",
        "void,return,<EOF>",161))

    def test_60(self):
        self.assertTrue(TestLexer.test(" int void float",
        "int,void,float,<EOF>",162))

#----------------- [TEST TOKEN] -----------------#
    def test_61(self):
        self.assertTrue(TestLexer.test(""" Ha Trung Kien #---# """,
        "Ha,Trung,Kien,Error Token #",161))

    def test_62(self):
        self.assertTrue(TestLexer.test(""" Ha ' Trung ' Kien """,
        "Ha,Error Token '",162))

    def test_63(self):
        self.assertTrue(TestLexer.test(""" Ha & Trung & Kien """,
        "Ha,Error Token &",163))

    def test_64(self):
        self.assertTrue(TestLexer.test(""" Ha # Trung # Kien """,
        "Ha,Error Token #",164))

    def test_65(self):
        self.assertTrue(TestLexer.test(""" + - * / { } [ ] ( ) """,
        "+,-,*,/,{,},[,],(,),<EOF>",165))

    def test_66(self):
        self.assertTrue(TestLexer.test(""" Ha | Trung | Kien """,
        "Ha,Error Token |",166))

    def test_67(self):
        self.assertTrue(TestLexer.test(""" Ha || Trung || Kien """,
        "Ha,||,Trung,||,Kien,<EOF>",167))

    def test_68(self):
        self.assertTrue(TestLexer.test(""" Ha && Trung && Kien """,
        "Ha,&&,Trung,&&,Kien,<EOF>",168))


    def test_69(self):
        self.assertTrue(TestLexer.test(""" Ha||Trung||Kien """,
        "Ha,||,Trung,||,Kien,<EOF>",169))

    def test_70(self):
        self.assertTrue(TestLexer.test(""" Ha&&Trung&&Kien """,
        "Ha,&&,Trung,&&,Kien,<EOF>",170))

    def test_71(self):
        self.assertTrue(TestLexer.test(""" HaNewTrung(Kien)+Anh """,
        "HaNewTrung,(,Kien,),+,Anh,<EOF>",171))

    ##################################################
    ##################################################

    def test_75(self): 
        self.assertTrue(TestLexer.test(""" 
        main: function void () {
            delta: int = fact (3);
            inc(x, delta);
            printint(x);
        """,
        "main,:,function,void,(,),{,delta,:,int,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,<EOF>",175))

    def test_76(self): 
        self.assertTrue(TestLexer.test(""" 
        inc: function void (out n: int, delta: int) 
        """,
        "inc,:,function,void,(,out,n,:,int,,,delta,:,int,),<EOF>",176))

    def test_77(self): 
        self.assertTrue(TestLexer.test(""" out n : int   """,
        "out,n,:,int,<EOF>",177))

    def test_78(self):
        self.assertTrue(TestLexer.test(""" Ha(Trung+Kien[Anh])  """,
        "Ha,(,Trung,+,Kien,[,Anh,],),<EOF>",178))

    def test_79(self):
        self.assertTrue(TestLexer.test(""" array [2, 3] of string """,
        "array,[,2,,,3,],of,string,<EOF>",179))

    def test_80(self): 
        self.assertTrue(TestLexer.test("""  array [2, 3] of integer """,
        "array,[,2,,,3,],of,integer,<EOF>",180))
 
    def test_81(self): 
        self.assertTrue(TestLexer.test(""" x,y,z: int = 1,2,3; """,
        "x,,,y,,,z,:,int,=,1,,,2,,,3,;,<EOF>",181))

    def test_82(self): 
        self.assertTrue(TestLexer.test(""" x: int = 65; """,
        "x,:,int,=,65,;,<EOF>",182))

    def test_83(self): 
        self.assertTrue(TestLexer.test(""" 
         for (i = 1, i < 10, i + 1) {
            writeInt(i);
        }  
        """,
        "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>",183))

    def test_84(self): 
        self.assertTrue(TestLexer.test(""" 1_2_3+86-10*1_2_3.00e22%48 """,
        "123,+,86,-,10,*,123.00e22,%,48,<EOF>",184))

    def test_85(self):
        self.assertTrue(TestLexer.test(""" true+false - 0001_2_3_4 """,
        "true,+,false,-,0,0,0,1234,<EOF>",185))

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
        "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>",186))

    def test_87(self):
        self.assertTrue(TestLexer.test(""" !!====.||+.... """,
        "!,!=,==,=,.,||,+,.,.,.,.,<EOF>",187))
    
    def test_88(self): 
        self.assertTrue(TestLexer.test(""" goo() """,
        "goo,(,),<EOF>",188))

    def test_89(self): 
        self.assertTrue(TestLexer.test(""" foo( 2 + x, 4.0 / y) """,
        "foo,(,2,+,x,,,4.0,/,y,),<EOF>",189))

#----------------- [TEST ADDITIONAL] -----------------#
    def test_72(self):
        self.assertTrue(TestLexer.test("$no idea","Error Token $",172))

    def test_73(self):
        self.assertTrue(TestLexer.test(""" \"Open the string \h \"""",
        """Illegal Escape In String: Open the string \h""",173))

    def test_74(self):
        self.assertTrue(TestLexer.test(""" \"Open the string \n\"""",
        """Unclosed String: Open the string """,174))
    
    def test_90(self):
        self.assertTrue(TestLexer.test(""" 0123.E-123 """,
        "0,123.E-123,<EOF>",190))

    def test_91(self):
        self.assertTrue(TestLexer.test(""" "1+1-2,true" """,
        "1+1-2,true,<EOF>",191))

    def test_92(self): 
        self.assertTrue(TestLexer.test("""
        a [2, 3] of integer;
        x: int = a[0,0];
        """,
        "a,[,2,,,3,],of,integer,;,x,:,int,=,a,[,0,,,0,],;,<EOF>",192))
 
    def test_93(self):
        self.assertTrue(TestLexer.test(""" a1b2c3 ___ _ """,
        "a1b2c3,___,_,<EOF>",93))
 
    def test_94(self): 
        self.assertTrue(TestLexer.test(""" (1+2+3).abc::789;; """,
        "(,1,+,2,+,3,),.,abc,::,789,;,;,<EOF>",194))

    def test_95(self): 
        self.assertTrue(TestLexer.test(""" "Ha::"Trung"||"Kien"&&Yeu+Em """,
        "Ha::,Trung,||,Kien,Unclosed String: &&Yeu+Em ",195))

    def test_96(self):
        self.assertTrue(TestLexer.test(""" 123.12_3 123.12e4_5 """,
        "123.12,_3,123.12e4,_5,<EOF>",96))


    def test_97(self):
        self.assertTrue(TestLexer.test(""" false&&//array(1,2,3)+4-5||true##""",
        "false,&&,<EOF>",197))
 
    def test_98(self):
        self.assertTrue(TestLexer.test(""" String out comment //"String in comment""",
        "String,out,comment,<EOF>",198))

    def test_99(self):
        self.assertTrue(TestLexer.test(""" x = 4 + 5; """,
        "x,=,4,+,5,;,<EOF>",199))

    def test_100(self): #note check again
        self.assertTrue(TestLexer.test(""" 
        x: int; 
        y: int = 5;
        if(x==5) y = 5
        else y = 4
        """,
        "x,:,int,;,y,:,int,=,5,;,if,(,x,==,5,),y,=,5,else,y,=,4,<EOF>",200))

