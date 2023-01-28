import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_01(self):
        inp = ''''''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 201))

    def test_02(self):
        inp = '''
            main: function void() {}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 202))
        
    def test_03(self):
        inp = '''
            a : boolean;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 203))
        
    def test_04(self):
        inp = '''
            b : integer;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 204))
        
    def test_05(self):
        inp = '''
            c : float;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 205))
        
    def test_06(self):
        inp = '''
            d : string;    
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 206))
        
    def test_07(self):
        inp = '''
            a : boolean
        '''
        expect = 'Error on line 3 col 8: <EOF>'
        self.assertTrue(TestParser.test(inp, expect, 207))
        
    def test_08(self):
        inp = '''
            : integer
        '''
        expect = 'Error on line 2 col 12: :'
        self.assertTrue(TestParser.test(inp, expect, 208))
        
    def test_09(self):
        inp = '''
            a,b,c : array [0] of float;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 209))
        
    def test_10(self):
        inp = '''
            a : array [0,1,2] of integer;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 210))
        
    def test_11(self):
        inp = '''
            a : array [] of integer;
        '''
        expect = 'Error on line 2 col 23: ]'
        self.assertTrue(TestParser.test(inp, expect, 211))
        
    def test_12(self):
        inp = '''
            a : void;
        '''
        expect = 'Error on line 2 col 16: void'
        self.assertTrue(TestParser.test(inp, expect, 212))
        
    def test_13(self):
        inp = '''
            a : auto;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 213))
        
    def test_14(self):
        inp = '''
            a : integer = 12/2;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 214))
        
    def test_15(self):
        inp = '''
            b : boolean = ;
        '''
        expect = 'Error on line 2 col 26: ;'
        self.assertTrue(TestParser.test(inp, expect, 215))
        
    def test_16(self):
        inp = '''
            : boolean = ;
        '''
        expect = 'Error on line 2 col 12: :'
        self.assertTrue(TestParser.test(inp, expect, 216))
        
    def test_17(self):
        inp = '''
            a,b : float = 1.2, 2.3%7;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 217))
        
    def test_18(self):
        inp = '''
            a : float = 1.2, 2.3*2+3;
        '''
        expect = 'Error on line 2 col 27: ,'
        self.assertTrue(TestParser.test(inp, expect, 218))
        
    def test_19(self):
        inp = '''
            a,b : float = 1.2+4;
        '''
        expect = 'Error on line 2 col 31: ;'
        self.assertTrue(TestParser.test(inp, expect, 219))
        
    def test_20(self):
        inp = '''
            a, b : array[2] of boolean = {false, true}, {{true}, !true};
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 220))
        
    def test_21(self):
        inp = '''
            foo : function void (out x : integer, arr : array [3] of integer) {

            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 221))
        
    def test_22(self):
        inp = '''
            child : function float (inherit out a : integer) inherit parent  {
                a = b + c;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 222))
        
    def test_23(self):
        inp = '''
            child : function void (inherit out a : integer) inherit parent
        '''
        expect = 'Error on line 3 col 8: <EOF>'
        self.assertTrue(TestParser.test(inp, expect, 223))
        
    def test_24(self):
        inp = '''
            foo : function array [1,2] of float () {}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 224))
        
    def test_25(self):
        inp = '''
            foo : function auto (inherit x : boolean) {}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 225))
        
    def test_26(self):
        inp = '''
            main : function void () {
                a = 12+6*3;
            }   
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 226))
        
    def test_27(self):
        inp = '''
            main : function void () {
                a[1,2,3] = 12+6*3;
                a[1] = "hi" :: "there";
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 227))
        
    def test_28(self):
        inp = '''
            main : function void () {
                a[] = true;
            }
        '''
        expect = 'Error on line 3 col 18: ]'
        self.assertTrue(TestParser.test(inp, expect, 228))
        
    def test_29(self):
        inp = '''
            main : function void () {
                a[foo(1,2)] = true;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 229))
        
    def test_30(self):
        inp = '''
            main : function void () {
                a = foo() / 2;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 230))
        
    def test_31(self):
        inp = '''
            main : function void () {
                a[-1] = --1;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 231))
        
    def test_32(self):
        inp = '''
            main : function void () {
                c = -a+-b[1,2];
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 232))
        
    def test_33(self):
        inp = '''
            main : function void () {
                c : auto = !!!!false;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 233))
        
    def test_34(self):
        inp = '''
            main : function void () {
                if (is_happy)
                    energy = energy*10000;
                    print("Yeah");
                else
                    print("Uh oh");
            }
        '''
        expect = 'Error on line 6 col 16: else'
        self.assertTrue(TestParser.test(inp, expect, 234))
        
    def test_35(self):
        inp = '''
            main : function void () {
                if (is_happy) {}
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 235))
        
    def test_36(self):
        inp = '''
            main : function void () {
                if (is_happy)
                else
            }
        '''
        expect = 'Error on line 4 col 16: else'
        self.assertTrue(TestParser.test(inp, expect, 236))
        
    def test_37(self):
        inp = '''
            main : function void () {
                if (hour >= 7 && hour <= 23) {
                    getup();
                    do_homework();
                }
                else {
                    sleep();
                }
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 237))
        
    def test_38(self):
        inp = '''
            main : function void() 
                print("Hello");
        '''
        expect = 'Error on line 3 col 16: print'
        self.assertTrue(TestParser.test(inp, expect, 238))
        
    def test_39(self):
        inp = '''
            main : function void() {
                for ( i = 2 , i <= 10 , -i)
                    print(i);
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 239))
        
    def test_40(self):
        inp = '''
            main : function void() {
                for ( i = {1,2,3} , i <= 10 , -i)
                    print(i);
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 240))
        
    def test_41(self):
        inp = '''
            main : function void() {
                for ( i = 1.2e3 , is_primary(i) , i+1) {}
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 241))
        
    def test_42(self):
        inp = '''
            main : function void() {
                for ( i = 0 , i + 5 < X , ) {
                    a = 4 + 5;
                }
            }
        '''
        expect = 'Error on line 3 col 42: )'
        self.assertTrue(TestParser.test(inp, expect, 242))
        
    def test_43(self):
        inp = '''
            main : function void() {
                delta:integer = fact(3);
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 243))
        
    def test_44(self):
        inp = '''
            main : function void()
                delta:integer = fact(3);
        '''
        expect = 'Error on line 3 col 16: delta'
        self.assertTrue(TestParser.test(inp, expect, 244))
        
    def test_45(self):
        inp = '''
            main : function void() {
                for ( i = 0 , i + 5 < X , 5) {
                    a : integer = 7;
                    a = a + 5;
                }
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 245))
        
    def test_46(self):
        inp = '''
            main : function void() {
                for ( i = 0 , i + 5 < X , 5)
                    a : integer = 7;
            }
        '''
        expect = 'Error on line 4 col 22: :'
        self.assertTrue(TestParser.test(inp, expect, 246))
        
    def test_47(self):
        inp = '''
            main : function void() {
                for ( i = 0 , {1,2,3} , {1,2,3}) {}
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 247))
        
    def test_48(self):
        inp = '''
            main : function void() {
                for ( i = 0 , "Hello" , "Hello") {}
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 248))
        
    def test_49(self):
        inp = '''
            main : function void() {
                for ( i[0] = 0 , i[0] < 1 , -1) {}
            }
        
        '''
        expect = 'Error on line 3 col 23: ['
        self.assertTrue(TestParser.test(inp, expect, 249))
        
    def test_50(self):
        inp = '''
            a : float = 7; b : boolean;
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 250))
        
    def test_51(self):
        inp = '''
            main : function void () {
                while(true) say("hi");
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 251))
        
    def test_52(self):
        inp = '''
            main : function void () {
                while(true) 
                    x : boolean = False;
            }
        '''
        expect = 'Error on line 4 col 22: :'
        self.assertTrue(TestParser.test(inp, expect, 252))
        
    def test_53(self):
        inp = '''
            main : function void () {
                while(true) {
                    x : boolean = False;
                }
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 253))
        
    def test_54(self):
        inp = '''
            main : function void () {
                while(a[1][1]) 
                    x = x + 1;
            }
        '''
        expect = 'Error on line 3 col 26: ['
        self.assertTrue(TestParser.test(inp, expect, 254))
        
    def test_55(self):
        inp = '''
            main : function void () {
                while(x != 3) x = x + 1;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 255))
        
    def test_56(self):
        inp = '''
            main : function void () {
                do x = x + 1
                while (true);
            }
        '''
        expect = 'Error on line 3 col 19: x'
        self.assertTrue(TestParser.test(inp, expect, 256))
        
    def test_57(self):
        inp = '''
            main : function void () {
                do {
                    x = x + 1;
                    y = y - 1;
                }
                while (true);
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 257))
        
    def test_58(self):
        inp = '''
            main : function void () {
                do while (true);
            }
        '''
        expect = 'Error on line 3 col 19: while'
        self.assertTrue(TestParser.test(inp, expect, 258))
        
    def test_59(self):
        inp = '''
            break;
        '''
        expect = 'Error on line 2 col 12: break'
        self.assertTrue(TestParser.test(inp, expect, 259))
        
    def test_60(self):
        inp = '''
            main : function void () {
                break;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 260))
        
    def test_61(self):
        inp = '''
            main : function void () {
                while(true)
                    if(today == "Sunday")
                        break;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 261))
        
    def test_62(self):
        inp = '''
            continue;
        '''
        expect = 'Error on line 2 col 12: continue'
        self.assertTrue(TestParser.test(inp, expect, 262))
        
    def test_63(self):
        inp = '''
            main : function void () {
                continue;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 263))
        
    def test_64(self):
        inp = '''
            return;
        '''
        expect = 'Error on line 2 col 12: return'
        self.assertTrue(TestParser.test(inp, expect, 264))
        
    def test_65(self):
        inp = '''
            main : function void () {
                return;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 265))
        
    def test_66(self):
        inp = '''
            return abc;
        '''
        expect = 'Error on line 2 col 12: return'
        self.assertTrue(TestParser.test(inp, expect, 266))
        
    def test_67(self):
        inp = '''
            foo : function auto () {
                return 123 + {1,2,3} / another_foo();
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 267))
        
    def test_68(self):
        inp = '''
            foo(x%3 , 4.0 - y);
        '''
        expect = 'Error on line 2 col 15: ('
        self.assertTrue(TestParser.test(inp, expect, 268))
        
    def test_69(self):
        inp = '''
            main : function void() {
                foo(x%3 , 4.0 - y);
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 269))
        
    def test_70(self):
        inp = '''
            main : function void() {
                {{{{{}}}}}
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 270))
        
    def test_71(self):
        inp = '''
            {}
        '''
        expect = 'Error on line 2 col 12: {'
        self.assertTrue(TestParser.test(inp, expect, 271))
        
    def test_72(self):
        inp = '''
            x,y : integer, float;
        '''
        expect = 'Error on line 2 col 25: ,'
        self.assertTrue(TestParser.test(inp, expect, 272))
        
    def test_73(self):
        inp = '''
            out x : string;
        '''
        expect = 'Error on line 2 col 12: out'
        self.assertTrue(TestParser.test(inp, expect, 273))
        
    def test_74(self):
        inp = '''
            foo : function auto (x : integer = 3) {}
        '''
        expect = 'Error on line 2 col 45: ='
        self.assertTrue(TestParser.test(inp, expect, 274))
        
    def test_75(self):
        inp = '''
            main : function void() {
                inherit x : auto = 7;
            }
        '''
        expect = 'Error on line 3 col 16: inherit'
        self.assertTrue(TestParser.test(inp, expect, 275))
        
    def test_76(self):
        inp = '''
            main : function void();
        '''
        expect = 'Error on line 2 col 34: ;'
        self.assertTrue(TestParser.test(inp, expect, 276))
        
    def test_77(self):
        inp = '''
            main : function void() {};
        '''
        expect = 'Error on line 2 col 37: ;'
        self.assertTrue(TestParser.test(inp, expect, 277))
        
    def test_78(self):
        inp = '''
            x: float = .e1 * 012;
        '''
        expect = 'Error on line 2 col 30: 12'
        self.assertTrue(TestParser.test(inp, expect, 278))
        
    def test_79(self):
        inp = '''
            arr : array [x,y] of integer;
        '''
        expect = 'Error on line 2 col 25: x'
        self.assertTrue(TestParser.test(inp, expect, 279))
        
    def test_80(self):
        inp = '''
            arr : array [1*2] of float;
        '''
        expect = 'Error on line 2 col 26: *'
        self.assertTrue(TestParser.test(inp, expect, 280))
        
    def test_81(self):
        inp = '''
            main : function void () {
                arr[a*2] = 3;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 281))
        
    def test_82(self):
        inp = '''
            main : function void () {
                if (a < 3 && a > 1)
                    if (is_int)
                        print("a is 2");
                    else
                        print("I don\\' know");
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 282))
        
    def test_83(self):
        inp = '''
            main : function void () {
                while () {}
            }
        '''
        expect = 'Error on line 3 col 23: )'
        self.assertTrue(TestParser.test(inp, expect, 283))
        
    def test_84(self):
        inp = '''
            main : function void() {
                x : integer = 7;
                if(x%2!=0){writeInt(i)};
            }
        '''
        expect = 'Error on line 4 col 38: }'
        self.assertTrue(TestParser.test(inp, expect, 284))
        
    def test_85(self):
        inp = '''
            main : function void (out foo: function auto ()) {}
        '''
        expect = 'Error on line 2 col 43: function'
        self.assertTrue(TestParser.test(inp, expect, 285))
        
    def test_86(self):
        inp = '''
            main : function void () {
                false : integer = 7;
            }
        '''
        expect = 'Error on line 3 col 16: false'
        self.assertTrue(TestParser.test(inp, expect, 286))
        
    def test_87(self):
        inp = '''
            main : function void () {
                false1 : integer = 7;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 287))
        
    def test_88(self):
        inp = '''
            main: function void () {
                i: integer = 45;
                while (i > 0)
                    i--;
            }
        '''
        expect = 'Error on line 5 col 21: -'
        self.assertTrue(TestParser.test(inp, expect, 288))
        
    def test_89(self):
        inp = '''
            main : function () {}
        '''
        expect = 'Error on line 2 col 28: ('
        self.assertTrue(TestParser.test(inp, expect, 289))
        
    def test_90(self):
        inp = '''
            main : function void () {
                x = a == b == c;
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 290))
        
    def test_91(self):
        inp = '''
            arr : array [2] of array [2] of float;
        '''
        expect = 'Error on line 2 col 31: array'
        self.assertTrue(TestParser.test(inp, expect, 291))
        
    def test_92(self):
        inp = '''
            arr : array [2] of auto;
        '''
        expect = 'Error on line 2 col 31: auto'
        self.assertTrue(TestParser.test(inp, expect, 292))
        
    def test_93(self):
        inp = '''
            arr : array [2] of void;
        '''
        expect = 'Error on line 2 col 31: void'
        self.assertTrue(TestParser.test(inp, expect, 293))
        
    def test_94(self):
        inp = '''
            arr : array [3,3] of integer = {
                {1,2,3}, {4,5,6} , {7,8,9}
            };
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 294))
        
    def test_95(self):
        inp = '''
            arr : array [1] of float = {};
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 295))
        
    def test_96(self):
        inp = '''
            a : string = x(y(z()));
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 296))
        
    def test_97(self):
        inp = '''
            x : integer = a + integer;
        '''
        expect = 'Error on line 2 col 30: integer'
        self.assertTrue(TestParser.test(inp, expect, 297))
        
    def test_98(self):
        inp = '''
            a : array [/*1,2*/] of float;
        '''
        expect = 'Error on line 2 col 30: ]'
        self.assertTrue(TestParser.test(inp, expect, 298))
        
    def test_99(self):
        inp = '''
            main : function void () {
                do 
                    /* do-nothing */
                while (true);
            }
        '''
        expect = 'Error on line 5 col 16: while'
        self.assertTrue(TestParser.test(inp, expect, 299))
        
    def test_100(self):
        inp = '''
            foo : function void () {
                // bai bai
            }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(inp, expect, 300))

