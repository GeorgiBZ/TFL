import re
from enum import Enum

class State(Enum):

    I = 1
    N2 = 2
    N8 = 3
    N10 = 4
    N16 = 5
    C1 = 6
    C2 = 7
    C3 = 8
    M1 = 9
    M2 = 10
    P1 = 11
    P2 = 12
    B = 13
    O = 14
    D = 15
    HX = 16
    E11 = 17
    E12 = 18
    E13 = 19
    E22 = 20
    ZN = 21
    E21 = 22
    ОG = 23
    V = 24
    ER = 25
    H = 26

ch = ''
s = ''
b = 0
cs = State.H
z = 0
tw = ['read', 'write', 'if', 'then', 'else', 'for', 'to', 'while',
      'do', 'true', 'false', 'or', 'and', 'not', 'as']

tl = ['{', '}', '%', '!', '$', ',', ';', '[', ']', ':', '(', ')',
      '+', '-', '*', '/', '=', '<>', '>', '<', '<=', '>=', '/*', '/*']

tn = []

ti = []

fi = open('')
fo = open('', 'w')

def gc():
    global fi, ch
    ch = fi.read(1)


def let():
    global ch
    return ch.isalpha()


def digit():
    global ch
    return ch.isdigit()


def nill():
    global s
    s = ''


def add():
    global s, ch
    s += ch


def look(t):
    global s, z
    if (s in t):
        z = t.index(s) + 1
    else:
        return 0


def put(t):
    global s, z
    if (s not in t):
        t.append(s)
        z = t.index(s)


def out(n, k):
    global fo
    fo.write(f'({n}, {k})')


def check_hex():
    global ch
    return ((ch.isdigit()) or (ch in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']))


def AFH():
    return (ch in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'H', 'h'])


def translate(base):
    global s
    if ((base == 2) and ((s[-1] == 'B') or (s[-1] == 'b'))):
        return int(s[:-1], base)
    elif ((base == 8) and ((s[-1] == 'O') or (s[-1] == 'o'))):
        return int(s[:-1], base)
    elif ((base == 10) and ((s[-1] == 'D') or (s[-1] == 'd'))):
        return int(s[:-1], base)
    elif ((base == 16) and ((s[-1] == 'H') or (s[-1] == 'h'))):
        return int(s[:-1], base)
    else:
        return int(s, base)


def convert():
    global s
    r = r"(?:([-+]?)(\d+)(?:E|e)([-+]?)(\d+)|([-+]?)(\d*)\.(\d+)(?:E|e)([-+]?)(\d+))"
    n = re.findall(r, s)[0]
    if (n[1] != '' and n[3] != ''):
        return (float(n[0] + n[1]) * pow(10, int(n[2] + n[3])))
    elif (n[5] != ''):
        return (float(f"{n[4]}{n[5]}.{n[6]}") * pow(10, int(n[7] + n[8])))
    else:
        return (float(f"0.{n[6]}") * pow(10, int(n[7] + n[8])))







def scanner():
    global ch, s, b, cs, z
    global tw, tl, ti, tn
    global fi, fo

    gc()
    while ((cs is not State.V) and (cs is not State.ER)):
        print(f"cs-{cs}\ts-{s}\tch-{ch}")
        match cs:
            case State.H:
                while (((ch == ' ') or (ch == '\n')) and (ch != '')):
                    gc()
                if (ch == ''):
                    cs = State.ER



                elif (let()):
                    nill()
                    add()
                    gc()
                    cs = State.I
                elif ((ch == '0') or (ch == '1')):
                    nill()
                    add()
                    gc()
                    cs = State.N2
                elif ((ch >= '2') and (ch <= '7')):
                    nill()
                    add()
                    gc()
                    cs = State.N8
                elif ((ch == '8') and (ch == '9')):
                    nill()
                    add()
                    gc()
                    cs = State.N10
                elif (ch == '.'):
                    nill()
                    add()
                    gc()
                    cs = State.P1
                elif (ch == '/'):
                    gc()
                    cs = State.C1
                elif (ch == '<'):
                    gc()
                    cs = State.M1
                elif (ch == '>'):
                    gc()
                    cs = 'M2'
                elif (ch == '}'):
                    out(2, 2)
                    cs = State.V
                else:
                    cs = State.ОG



            case State.I:
                while(let() or digit()):
                    add()
                    gc()
                look(tw)
                if (z != 0):
                    out(1, z)
                    cs = State.H
                else:
                    put(ti)
                    out(4, z)
                    cs = State.Н



            case State.N2:
                while((ch == '0') or (ch == '1')):
                    add()
                    gc()
                if ((ch >= '2') and (ch <= '7')):
                    add()
                    gc()
                    cs = State.N8
                elif ((ch == '8') or (ch == '9')):
                    add()
                    gc()
                    cs = State.N10
                elif ((ch == 'A') or (ch == 'a')
                      or (ch == 'C') or (ch == 'c')
                      or (ch == 'F') or (ch == 'F')):
                    add()
                    gc()
                    cs = State.N16
                elif (ch == 'E') or (ch == 'e'):
                    add()
                    gc()
                    cs = State.E11
                elif ((ch == 'D') or (ch == 'd')):
                    add()
                    gc()
                    cs = State.D
                elif ((ch == 'O') or (ch == 'o')):
                    add()
                    gc()
                    cs = State.O
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (ch == '.'):
                    add()
                    gc()
                    cs = State.P1
                elif ((ch == 'B') or (ch == 'b')):
                    add()
                    gc()
                    cs = State.B
                elif (ch == '}'):
                    out(2, 2)
                    cs = State.H
                elif(let()):
                    cs = State.ER
                else:
                    cs = State.ER



            case State.N8:
                while ((ch >= '0') or (ch <= '7')):
                    add()
                    gc()
                if ((ch >= '8') and (ch <= '9')):
                    add()
                    gc()
                    cs = State.N10
                elif ((ch == 'A') or (ch == 'a')
                      or (ch == 'B') or (ch == 'b')
                      or (ch == 'C') or (ch == 'c')
                      or (ch == 'F') or (ch == 'f')):
                    add()
                    gc()
                    cs = State.N16
                elif ((ch == 'E') or (ch == 'e')):
                    add()
                    gc()
                    cs = State.E11
                elif ((ch == 'D') or (ch == 'd')):
                    add()
                    gc()
                    cs = State.D
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (ch == '.'):
                    add()
                    gc()
                    cs = State.P1
                elif ((ch == 'O') or (ch == 'o')):
                    add()
                    gc()
                    cs = State.O
                elif (let()):
                    cs = State.ER
                else:
                    cs = State.ER



            case State.N10:
                while ((ch >= '0') or (ch <= '9')):
                    add()
                    gc()
                if ((ch == 'A') or (ch == 'a')
                        or (ch == 'B') or (ch == 'b')
                        or (ch == 'C') or (ch == 'c')
                        or (ch == 'F') or (ch == 'f')):
                    add()
                    gc()
                    cs = State.N16
                elif ((ch == 'E') or (ch == 'e')):
                    add()
                    gc()
                    cs = State.E11
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (ch == '.'):
                    add()
                    gc()
                    cs = State.P1
                elif ((ch == 'D') or (ch == 'd')):
                    add()
                    gc()
                    cs = State.D
                elif (let()):
                    cs = State.ER
                else:
                    cs = State.ER



            case State.N16:
                while (check_hex()):
                    add()
                    gc()
                if ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                else:
                    cs = State.ER



            case State.B:
                if (check_hex()):
                    add()
                    gc()
                    cs = State.N16
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (let()):
                    cs = State.ER
                else:
                    translate(2)
                    put(tn)
                    out(3, z)
                    cs = State.H



            case State.O:
                if (let() or digit()):
                    cs = State.ER
                else:
                    translate(8)
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.D:
                if (check_hex()):
                    add()
                    gc()
                    cs = State.N16
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (let()):
                    cs = State.ER
                else:
                    translate(10)
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.HX:
                if (let() or digit()):
                    cs = State.ER
                else:
                    translate(16)
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.E11:
                if (digit()):
                    add()
                    gc()
                    cs = State.E12
                elif ((ch == '+') or (ch == '-')):
                    add()
                    gc()
                    cs = State.ZN
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (check_hex()):
                    add()
                    gc()
                    cs = State.N16
                else:
                    cs = State.ER


            case State.ZN:
                if (digit()):
                    add()
                    gc()
                    cs = State.E13
                else:
                    cs = State.ER


            case State.E12:
                if (digit()):
                    add()
                    gc()
                    cs = State.E12
                elif ((ch == 'H') or (ch == 'h')):
                    add()
                    gc()
                    cs = State.HX
                elif (check_hex()):
                    add()
                    gc()
                    cs = State.N16
                elif (let()):
                    cs = State.ER
                else:
                    convert()
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.E13:
                while(digit()):
                    add()
                    gc()
                if (len() or (ch == '.')):
                    cs = State.ER
                else:
                    convert()
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.P1:
                if (digit()):
                    add()
                    gc()
                    cs = State.P2
                else:
                    cs = State.ER


            case State.P2:
                while(digit()):
                    add()
                    gc()
                if ((ch == 'E') or (ch == 'e')):
                    add()
                    gc()
                    cs = State.E21
                elif (len() or (ch == '.')):
                    cs = 'ER'
                else:
                    convert()
                    put(tn)
                    out(3, z)
                    cs = State.H


            case State.E21:
                if ((ch == '+') or (ch == '-')):
                    add()
                    gc()
                    cs = State.ZN
                elif (digit()):
                    add()
                    gc()
                    cs = State.E22
                else:
                    cs = State.ER



            case State.E22:
                while(digit()):
                    add()
                    gc()
                if ((let()) or (ch == '.')):
                    cs = State.ER
                else:
                    convert()
                    put(tn)
                    out(3, z)
                    cs = State.H



            case State.C1:
                if (ch == '*'):
                    gc()
                    cs = State.C2
                else:
                    out(2, 16)
                    cs = State.H



            case State.C2:
                while((ch != '*') or (ch != '}')):
                    gc()
                if (ch == '*'):
                    cs = State.C3
                elif (ch == '}'):
                    cs = State.ER



            case State.C3:
                if (ch == '/'):
                    gc()
                    cs = State.H
                else:
                    gc()
                    cs = State.C2



            case State.M1:
                if (ch == '>'):
                    gc()
                    out(2, 18)
                    cs = State.H
                elif (ch == '='):
                    gc()
                    out(2, 21)
                    cs = State.H
                else:
                    out(2, 20)
                    cs = State.H



            case State.M2:
                if (ch == '='):
                    gc()
                    out(2, 22)
                    cs = State.H
                else:
                    out(2, 19)
                    cs = State.H



            case State.ОG:
                nill()
                add()
                look(tl)
                if (z != 0):
                    gc()
                    out(2, z)
                    cs = State.H
                else:
                    cs = State.ER
    return cs

#print(scanner())

















fi.close()
fo.close()



