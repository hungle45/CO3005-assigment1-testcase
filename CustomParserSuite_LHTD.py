import unittest
from CustomTestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_parser0(self):
        """Simple program: integermain() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_parser1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_parser2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_parser3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_parser4(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i = i - 1;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_parser5(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i = i + 2;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test_parser6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_parser7(self):
        input = '''
            main: function void () {
                delta: string = "dat";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_parser8(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_parser9(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_parser10(self):
        input = '''
            main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printInt(b[4]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_parser11(self):
        input = '''
            main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_parser12(self):
        input = '''
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_parser13(self):
        input = '''
            main: function void () {
                i: integer = -10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_parser14(self):
        input = '''
            main: function void () {
                delta: float = 130.34e2;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_parser15(self):
        input = '''
            main: function void () {
                delta: string = "true";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_parser16(self):
        input = '''
            voidA: function integer(n: integer) inherit voidB{
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_parser17(self):
        input = '''
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer){
                n = n + 24;
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInt(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_parser18(self):
        input = '''
            main: function void () {
                delta: boolean = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_parser19(self):
        input = '''
            main: function void () {
                delta: string;
                delta = "abcd"::"298";
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_parser20(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                temp: boolean = !delta||false||!false;
                printBoolean(temp);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test_parser21(self):
        input = '''
            main: function void () {
                a,c: boolean = true,!false;
                printBoolean(a);
                printBoolean(c);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
        
    def test_parser22(self):
        input = '''
            main: function void () {
                a,c: string = "true","!false";
                printString(a);
                printString(c);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_parser23(self):
        input = '''
            main: function void () {
                a,c: string = "true","!false";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test_parser24(self):
        input = '''
            main: function void () {
                a,c: string = "true","det/tsef";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test_parser25(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
    def test_parser26(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)+24);
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        
    def test_parser27(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)%2);
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        
    def test_parser28(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34+voidA(3)));
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test_parser29(self):
        input = '''
            voidA: function string (s: string){
                i: integer = 4;
                while (i>0){
                    s = s::"qua";
                }
                return s;
            }
            main: function void () {
                delta: string = "av";
                delta = voidA(delta);
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        
    def test_parser30(self):
        input = '''
            voidAB: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(23);
                delta = delta/2 + delta/2/3;
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_parser31(self):
        input = '''
            main: function void () {
                delta: integer = 34+-4--5;
                delta = delta*2;
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_parser32(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        continue;
                    }
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_parser33(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_parser34(self):
        input = '''
            main: function void () {
                for (i = 10, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        break;
                    }
                }
                return;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_parser35(self):
        input = '''
            s: string = "daylastring";
            main: function void () {
                printString(s);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test_parser36(self):
        input = '''
            voidAB: function integer(n: integer){
                for (i = n, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        return;
                    }
                }
            }
            main: function void () {
                voidAB(10);
                printInt("/ndone");
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test_parser37(self):
        input = '''
            voidAB: function integer(){
                return 4+2;
            }
            main: function void () {
                delta: integer = voidAB();
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_parser38(self):
        input = '''
            s: string = "daylastring";
            main: function void () {
                printString(s+"uk");
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test_parser39(self):
        input = '''
            s: boolean = true;
            main: function void () {
                s = false;
                printBoolean(s);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_parser40(self):
        input = '''
            s: float = 5.5;
            main: function void () {
                s = s/7;
                printFloat(s);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_parser41(self):
        input = '''
            main: function void () {
                s: integer;
                readInt(s);
                printInt(s);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        
    def test_parser42(self):
        input = '''
            main: function void () {
                s: string;
                readString(s);
                printString(s::"acd");
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
        
    def test_parser43(self):
        input = '''
            main: function void () {
                s: boolean;
                readBoolean(s);
                printBoolean(s && true || false);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
    def test_parser44(self):
        input = '''
            main: function void () {
                s: float;
                readFloat(s);
                printFloat(s + 40.9);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        
    def test_parser45(self):
        input = '''
            r, s: integer;
            main: function void () {
                a, b: array [5] of integer;
                r = 2.0;
                s = r * r * myPI;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        
    def test_parser46(self):
        input = '''
            r, s: integer = 5,10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        
    def test_parser47(self):
        input = '''
            main: function void () {
                a, b: array [5] of integer;
                a[0] = 12;
                b[1] = a[0];
                printInt(b[1]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_parser48(self):
        input = '''
            main: function void () {
                a, b: array [5] of integer;
                a[0] = 2;
                a[3] = 4;
                b[1] = a[1 + a[0]];
                printInt(b[1]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_parser49(self):
        input = '''
            main: function void () {
                a: array [5,2] of integer;
                a[0,1] = 2;
                printInt(a[0,1] + 2);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_parser50(self):
        input = '''
            main: function void () {
                a: array [5,2] of integer;
                a[0,1] = 2;
                a[0,2] = 5;
                printInt(a[0,1] + a[0,2]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    def test_parser51(self):
        input = '''
            x integer = 65;
            mess: function integer(n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInt(delta);
            }
        '''
        expect = "Error on line 2 col 14: integer"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_parser52(self):
        input = '''
            add: function integer(n: integer){
                integer = 0;
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
        expect = "Error on line 3 col 16: integer"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_parser53(self):
        input = '''
            x: integer65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta := fact(3);
                inc(x,delta);
                printInt(x);
            }
        '''
        expect = "Error on line 2 col 15: integer65"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_parser54(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i=0){
                    i--;
                }
                return  i;
            }
        '''
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_parser55(self):
        input = '''
            function void () {
                i: integer = 10;
                while (i>20){
                    i+=2;
                }
                return  i;
            }
        '''
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_parser56(self):
        input = '''
            voidA: function integer(n: integer){
                return n%/10;
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
        expect = "Error on line 3 col 25: /"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_parser57(self):
        input = '''
            main: function () {
                delta: string = "dat";
                printString(delta);
            }
        '''
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_parser58(self):
        input = '''
            main: function void () {
                delta: float == 3.45;
                printFloat(delta);
            }
        '''
        expect = "Error on line 3 col 29: =="
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_parser59(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta++);
            }
        '''
        expect = "Error on line 4 col 35: +"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_parser60(self):
        input = '''
            main: function void () {
                b: array [5] integer = [1,2,3,4,6];
                printInt(b[4]);
            }
        '''
        expect = "Error on line 3 col 29: integer"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_parser61(self):
        input = '''
            main: function void () {
                delta: integer = 3+/2;
                printInt(delta);
            }
        '''
        expect = "Error on line 3 col 35: /"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_parser62(self):
        input = '''
            main: function void () {
                i: integer = 10;
                {
                    i = i - 1;
                }
                while (i!=0)
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_parser63(self):
        input = '''
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0)
                return  i;
            }
        '''
        expect = "Error on line 8 col 16: return"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_parser64(self):
        input = '''
            main: function void () {
                i: integer = -10;
                do{
                    i = i++;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "Error on line 5 col 26: +"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_parser65(self):
        input = '''
            main: function void () {
                delta:= 34e2
                printFloat(delta);
            }
        '''
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_parser66(self):
        input = '''
            main: function void () {
                delta: string = "true";
                4 = 5;
                printString(delta);
            }
        '''
        expect = "Error on line 4 col 16: 4"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_parser67(self):
        input = '''
            voidA: integer(n: integer) inherit voidB{
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
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_parser68(self):
        input = '''
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(de,);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInt(x);
            }
        '''
        expect = "Error on line 6 col 33: )"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_parser69(self):
        input = '''
            voidA: function integer(n: integer) inheri voidB{
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
        expect = "Error on line 2 col 48: inheri"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_parser70(self):
        input = '''
            main: function void () {
                delta: bool = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        '''
        expect = "Error on line 3 col 23: bool"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_parser71(self):
        input = '''
            main: function void () {
                delta: string;
                delta = "abcd":"298";
                printBoolean(delta);
            }
        '''
        expect = "Error on line 4 col 30: :"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_parser72(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                temp: boolean = !delta false||!false;
                printBoolean(temp);
            }
        '''
        expect = "Error on line 4 col 39: false"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_parser73(self):
        input = '''
            main: function void () {
                a,c: boolean = true,!false;
                printBoolean;
                printBoolean(c);
            }
        '''
        expect = "Error on line 4 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_parser74(self):
        input = '''
            main: function void () {
                a,b: string = "!false";
                printString(a);
                printString(c);
            }
        '''
        expect = "Error on line 3 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_parser75(self):
        input = '''
            main: function void () {
                a,c: string : "true","!false";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        '''
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_parser76(self):
        input = '''
            main: function void () {
                a,c: string = "true","det\tsef";
                v: string = a::c;
                printString(a)
            }
        '''
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_parser77(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInt(delta);
            }
        '''
        expect = "Error on line 3 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_parser78(self):
        input = '''
            voidA: function int{
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)+24);
                printInt(delta);
            }
        '''
        expect = "Error on line 2 col 28: int"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_parser79(self):
        input = '''
            voidA: function integer(n: integer){
                n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)%2);
                printInt(delta);
            }
        '''
        expect = "Error on line 3 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_parser80(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA34+voidA(3)));
                printInt(delta);
            }
        '''
        expect = "Error on line 6 col 56: )"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_parser81(self):
        input = '''
            main: function void () {
                delta string = "av";
                delta = voidA(delta);
                printString(delta);
            }
        '''
        expect = "Error on line 3 col 22: string"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_parser82(self):
        input = '''
            voidAB: function integer(n integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(23);
                delta = delta/2 + delta/2/3;
                printInt(delta);
            }
        '''
        expect = "Error on line 2 col 39: integer"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_parser83(self):
        input = '''
            main: void () {
                delta: integer = 34+-4--5;
                delta = delta*2;
                printInt(delta);
            }
        '''
        expect = "Error on line 2 col 18: void"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_parser84(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 >> i){
                        writeInt(i);
                        continue;
                    }
                }
            }
            //m cmt
        '''
        expect = "Error on line 4 col 29: >"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_parser85(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10; i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
        '''
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_parser86(self):
        input = '''
            main: function void () {
                for (i = 10, i >= 0, i = i- 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        break;
                    }
                }
                return;
            }
        '''
        expect = "Error on line 3 col 39: ="
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_parser87(self):
        input = '''
            s: string = "daylastring";
            main: function void () {
                (s);
            }
        '''
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_parser88(self):
        input = '''
            voidAB: function integer(n: integer,){
                for (i = n, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        return;
                    }
                }
            }
            main: function void () {
                voidAB(10);
                printInt("/ndone");
            }
        '''
        expect = "Error on line 2 col 48: )"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_parser89(self):
        input = '''
            voidAB: function integer(){
                return 4+2;
            }
            main: function void () {
                delta: integer = ();
                printInt(delta);
            }
        '''
        expect = "Error on line 6 col 33: ("
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_parser90(self):
        input = '''
            s: string = "daylastring";
            main: function void () {
                printString(s::);
            }
        '''
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_parser91(self):
        input = '''
            s: boolean = true;
            main: function void () {
                s = false;
                printBoolean(s);
                return
            }
        '''
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_parser92(self):
        input = '''
            s: floa = 5.5;
            main: function void () {
                s = s/7;
                printFloat(s);
            }
        '''
        expect = "Error on line 2 col 15: floa"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_parser93(self):
        input = '''
            main: function void () 
                s: integer;
                readInt(s);
                printInt(s);
            }
        '''
        expect = "Error on line 3 col 16: s"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_parser94(self):
        input = '''
            main: function void () {
                s: string;
                readString(s);
                printString(s:io:"acd");
            }
        '''
        expect = "Error on line 5 col 29: :"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_parser95(self):
        input = '''
            main: function void () {
                s: boolean;
                readBoolean(s);
                printBoolean(s && && true || false);
            }
        '''
        expect = "Error on line 5 col 34: &&"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_parser96(self):
        input = '''
            main: function void () {
                s float;
                readFloat(s);
                printFloat(s + 40.9);
            }
        '''
        expect = "Error on line 3 col 18: float"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_parser97(self):
        input = '''
            r, s: integer;
            main: function void () {
                a, b: array [5] of integer;
                r = 2.0;
                s = r * r * ;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = "Error on line 6 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_parser98(self):
        input = '''
            r, s = 5,10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = "Error on line 2 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_parser99(self):
        input = '''
            r, s: integer = 5;10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 299))
    
    def test_parser100(self):
        input = '''
            main: function void () {
                a, b: array [5] of integer;
                a[0,] = 12;
                b[1] = a[0];
                printInt(b[1]);
            }
        '''
        expect = "Error on line 4 col 20: ]"
        self.assertTrue(TestParser.test(input, expect, 300))
     