import sys
from enum import Enum









class SyntaxError(Exception):
    pass

class Lex_Type(Enum):

    NULL = 0
    OR = 1
    AND = 2
    NOT = 3
    TRUE = 4
    FALSE = 5
    PROGRAM = 6
    VAR = 7
    BEGIN = 8
    END = 9
    INT = 10
    FLOAT = 11
    BOOL = 12
    AS = 13
    IF = 14
    THEN = 15
    ELSE = 16
    FOR = 17
    TO = 18
    DO = 19
    WHILE = 20
    READ = 21
    WRITE = 22

    NEQ = 23 # <>
    EQ = 24 # =
    LSS = 25 # <
    LEQ = 26 # <=
    GRT = 27  # >
    GEQ = 28  # >=
    PLUS = 29  # +
    MINUS = 30  # -
    MUL = 31  # *
    DIV = 32  # /
    LRB = 33  # (
    PRB = 34  # )
    SEMICOLON = 35  # ;
    COMMA = 36  # ,
    LSB = 37  # [
    PSB = 38  # ]
    COLON = 39  # :
    LCB = 40  # {
    PCB = 41  # }

    ID = 42

    NUM = 43









def add_type(token_sequence, table_of_table):

    for i in range(len(token_sequence)):
        lex = table_of_table[token_sequence[i][0]][token_sequence[i][1]]

        #print(token_sequence[i])
        match lex:
            case "or":
                token_sequence[i] = (Lex_Type.OR, token_sequence[i][0], token_sequence[i][1])
            case "and":
                token_sequence[i] = (Lex_Type.AND, token_sequence[i][0], token_sequence[i][1])
            case "not":
                token_sequence[i] = (Lex_Type.NOT, token_sequence[i][0], token_sequence[i][1])
            case "true":
                token_sequence[i] = (Lex_Type.TRUE, token_sequence[i][0], token_sequence[i][1])
            case "false":
                token_sequence[i] = (Lex_Type.FALSE, token_sequence[i][0], token_sequence[i][1])
            case "program":
                token_sequence[i] = (Lex_Type.PROGRAM, token_sequence[i][0], token_sequence[i][1])
            case "var":
                token_sequence[i] = (Lex_Type.VAR, token_sequence[i][0], token_sequence[i][1])
            case "begin":
                token_sequence[i] = (Lex_Type.BEGIN, token_sequence[i][0], token_sequence[i][1])
            case "end.":
                token_sequence[i] = (Lex_Type.END, token_sequence[i][0], token_sequence[i][1])
            case "int":
                token_sequence[i] = (Lex_Type.INT, token_sequence[i][0], token_sequence[i][1])
            case "float":
                token_sequence[i] = (Lex_Type.FLOAT, token_sequence[i][0], token_sequence[i][1])
            case "bool":
                token_sequence[i] = (Lex_Type.BOOL, token_sequence[i][0], token_sequence[i][1])
            case "as":
                token_sequence[i] = (Lex_Type.AS, token_sequence[i][0], token_sequence[i][1])
            case "if":
                token_sequence[i] = (Lex_Type.IF, token_sequence[i][0], token_sequence[i][1])
            case "then":
                token_sequence[i] = (Lex_Type.THEN, token_sequence[i][0], token_sequence[i][1])
            case "else":
                token_sequence[i] = (Lex_Type.ELSE, token_sequence[i][0], token_sequence[i][1])
            case "for":
                token_sequence[i] = (Lex_Type.FOR, token_sequence[i][0], token_sequence[i][1])
            case "to":
                token_sequence[i] = (Lex_Type.TO, token_sequence[i][0], token_sequence[i][1])
            case "do":
                token_sequence[i] = (Lex_Type.DO, token_sequence[i][0], token_sequence[i][1])
            case "while":
                token_sequence[i] = (Lex_Type.WHILE, token_sequence[i][0], token_sequence[i][1])
            case "read":
                token_sequence[i] = (Lex_Type.READ, token_sequence[i][0], token_sequence[i][1])
            case "write":
                token_sequence[i] = (Lex_Type.WRITE, token_sequence[i][0], token_sequence[i][1])
            case "<>":
                token_sequence[i] = (Lex_Type.EQ, token_sequence[i][0], token_sequence[i][1])
            case "=":
                token_sequence[i] = (Lex_Type.EQ, token_sequence[i][0], token_sequence[i][1])
            case "<":
                token_sequence[i] = (Lex_Type.LSS, token_sequence[i][0], token_sequence[i][1])
            case "<=":
                token_sequence[i] = (Lex_Type.LEQ, token_sequence[i][0], token_sequence[i][1])
            case ">":
                token_sequence[i] = (Lex_Type.GRT, token_sequence[i][0], token_sequence[i][1])
            case ">=":
                token_sequence[i] = (Lex_Type.GEQ, token_sequence[i][0], token_sequence[i][1])
            case "+":
                token_sequence[i] = (Lex_Type.PLUS, token_sequence[i][0], token_sequence[i][1])
            case "-":
                token_sequence[i] = (Lex_Type.MINUS, token_sequence[i][0], token_sequence[i][1])
            case "*":
                token_sequence[i] = (Lex_Type.MUL, token_sequence[i][0], token_sequence[i][1])
            case "/":
                token_sequence[i] = (Lex_Type.DIV, token_sequence[i][0], token_sequence[i][1])
            case "(":
                token_sequence[i] = (Lex_Type.LRB, token_sequence[i][0], token_sequence[i][1])
            case ")":
                token_sequence[i] = (Lex_Type.PRB, token_sequence[i][0], token_sequence[i][1])
            case ";":
                token_sequence[i] = (Lex_Type.SEMICOLON, token_sequence[i][0], token_sequence[i][1])
            case ",":
                token_sequence[i] = (Lex_Type.COMMA, token_sequence[i][0], token_sequence[i][1])
            case "[":
                token_sequence[i] = (Lex_Type.LSB, token_sequence[i][0], token_sequence[i][1])
            case "]":
                token_sequence[i] = (Lex_Type.PSB, token_sequence[i][0], token_sequence[i][1])
            case ":":
                token_sequence[i] = (Lex_Type.COLON, token_sequence[i][0], token_sequence[i][1])
            case "{":
                token_sequence[i] = (Lex_Type.LCB, token_sequence[i][0], token_sequence[i][1])
            case "}":
                token_sequence[i] = (Lex_Type.PCB, token_sequence[i][0], token_sequence[i][1])
            case _:
                if (token_sequence[i][0] == 3):
                    token_sequence[i] = (Lex_Type.ID, token_sequence[i][0], token_sequence[i][1])
                elif  (token_sequence[i][0] == 4):
                    token_sequence[i] = (Lex_Type.NUM, token_sequence[i][0], token_sequence[i][1])
        #print(token_sequence[i])

    #print(token_sequence)



















current_token = Lex_Type.NULL
index_token = 0


def parser(token_sequence, table_of_table):
    add_type(token_sequence, table_of_table)
    global current_token, index_token


    try:




        def get_token():
            global current_token, index_token
            current_token = token_sequence[index_token][0]
            #print(f'token = {current_token}\tlex = {table_of_table[token_sequence[index_token][1]][token_sequence[index_token][2]]}')
            index_token += 1

        def next_token():
            global index_token
            return token_sequence[index_token][0]









        def P():
            #P --> program D1 B
            #print('P')

            get_token()
            if (current_token != Lex_Type.PROGRAM): raise SyntaxError(f'Синтаксическая ошибка: P')
            D1()
            B()

        def D1():
            #D1 --> var D D11
            #print('D1')

            get_token()
            if (current_token != Lex_Type.VAR): raise SyntaxError(f'Синтаксическая ошибка:  D1')
            D()
            D11()

        def D():
            #D --> int ID1 | float ID1 | bool ID1
            #print('D')

            get_token()
            if ((current_token != Lex_Type.INT) and (current_token != Lex_Type.FLOAT)
                    and (current_token != Lex_Type.BOOL)): raise SyntaxError(f'Синтаксическая ошибка: D')
            ID1()

        def ID1():
            #ID1 --> ID ID11
            #print('ID1')

            get_token()
            if (current_token != Lex_Type.ID): raise SyntaxError(f'Синтаксическая ошибка: ID1')
            ID11()

        def ID11():
            #ID11 --> , ID ID11 | 𝜀
            #print('ID11')

            if (next_token() == Lex_Type.COMMA):
                get_token()
                get_token()
                if (current_token != Lex_Type.ID): raise SyntaxError(f'Синтаксическая ошибка: ID11')
                ID11()
            else:
                pass

        def D11():
            #D11 --> ; D D11 | 𝜀
            #print('D11')

            if (next_token() == Lex_Type.SEMICOLON):
                get_token()
                D()
                D11()
            else:
                pass

        def B():
            #B --> begin S1 end.
            #print('B')

            get_token()
            if (current_token != Lex_Type.BEGIN): raise SyntaxError(f'Синтаксическая ошибка: B')
            S1()
            get_token()
            if (current_token != Lex_Type.END): raise SyntaxError(f'Синтаксическая ошибка: B')

        def S1():
            #S1 --> S S11
            #print('S1')

            S()
            S11()

        def S():
            '''S --> ID as E|
                    if E then S [ else S]
                    for ID as E to E do S
                    while E do S
                    read «(» ID1 «)»
                    write «(» EW «)»
                    «[» SC «]»'''
            #print('S')

            get_token()
            if (current_token == Lex_Type.ID):
                get_token()
                if (current_token != Lex_Type.AS): raise SyntaxError(f'Синтаксическая ошибка: S-ID-AS')
                E()
            elif (current_token == Lex_Type.IF):
                E()
                get_token()
                if (current_token != Lex_Type.THEN): raise SyntaxError(f'Синтаксическая ошибка: S-IF-THEN')
                S()
                if (next_token() == Lex_Type.ELSE):
                    get_token()
                    S()
                else:
                    pass
            elif (current_token == Lex_Type.FOR):
                get_token()
                if (current_token != Lex_Type.ID): raise SyntaxError(f'Синтаксическая ошибка: S-FOR-ID')
                get_token()
                if (current_token != Lex_Type.AS): raise SyntaxError(f'Синтаксическая ошибка: S-FOR-AS')
                E()
                get_token()
                if (current_token != Lex_Type.TO): raise SyntaxError(f'Синтаксическая ошибка: S-FOR-TO')
                E()
                get_token()
                if (current_token != Lex_Type.DO): raise SyntaxError(f'Синтаксическая ошибка: S-FOR-DO')
                S()
            elif (current_token == Lex_Type.WHILE):
                E()
                get_token()
                if (current_token != Lex_Type.DO): raise SyntaxError(f'Синтаксическая ошибка: S-WHILE-DO')
                S()
            elif (current_token == Lex_Type.READ):
                get_token()
                if (current_token != Lex_Type.LRB): raise SyntaxError(f'Синтаксическая ошибка: S-READ-LRB')
                ID1()
                get_token()
                if (current_token != Lex_Type.PRB): raise SyntaxError(f'Синтаксическая ошибка: S-READ-PRB')
            elif (current_token == Lex_Type.WRITE):
                get_token()
                if (current_token != Lex_Type.LRB): raise SyntaxError(f'Синтаксическая ошибка: S-WRITE-LRB')
                EW()
                get_token()
                if (current_token != Lex_Type.PRB): raise SyntaxError(f'Синтаксическая ошибка: S-WRITE-PRB')
            elif (current_token == Lex_Type.LSB):
                SC()
                get_token()
                if (current_token != Lex_Type.PSB): raise SyntaxError(f'Синтаксическая ошибка: S-LSB-PSB')
            else:
                raise SyntaxError(f'Синтаксическая ошибка: S-else')

        def S11():
            #S11 --> ; S S11 | 𝜀
            #print('S11')

            if (next_token() == Lex_Type.SEMICOLON):
                get_token()
                S()
                S11()
            else:
                pass

        def E():
            #E --> E1 E11
            #print('E')

            E1()
            E11()

        def EW():
            #EW --> E EW1
            #print('EW')

            E()
            EW1()



        def SC():
            #SC --> S SC1
            #print('SC')

            S()
            SC1()

        def EW1():
            #EW1 --> , E EW1 | 𝜀
            #print('EW1')

            if (next_token() == Lex_Type.COMMA):
                get_token()
                E()
                EW1()
            else:
                pass

        def SC1():
            #SC1 --> : S SC1 | S SC1 | 𝜀
            #print('SC1')


            if (next_token() == Lex_Type.COLON):
                get_token()
                S()
                SC1()
            elif ((next_token() == Lex_Type.IF)
                  or (next_token() == Lex_Type.FOR)
                  or (next_token() == Lex_Type.WHILE)
                  or (next_token() == Lex_Type.READ)
                  or (next_token() == Lex_Type.WRITE)
                  or (next_token() == Lex_Type.LSB)
                  or (next_token() == Lex_Type.ID)):
                S()
                SC1()
            else:
                pass

        def E1():
            #E1 --> T T1
            #print('E1')

            T()
            T1()

        def E11():
            #E11 --> <> E1 E11| = E1 E11| < E1 E11| <= E1 E11| > E1 E11| >= E1 E11 | 𝜀
            #print('E11')

            if ((next_token() == Lex_Type.NEQ) or (next_token() == Lex_Type.EQ)
                    or (next_token() == Lex_Type.LSS) or (next_token() == Lex_Type.LEQ)
                    or (next_token() == Lex_Type.GRT) or (next_token() == Lex_Type.GEQ)):
                get_token()
                E1()
                E11()
            else:
                pass

        def T():
            #T --> F F1
            #print('T')

            F()
            F1()

        def T1():
            #T1 --> + T T1| - T T1| or T T1 | 𝜀
            #print('T1')

            if ((next_token() == Lex_Type.PLUS) or  (next_token() == Lex_Type.MINUS)
                    or (next_token() == Lex_Type.OR)):
                get_token()
                T()
                T1()
            else:
                pass

        def F():
            #F --> ID | NUMBER | true | false | not F | «(» E «)»
            #print('F')

            get_token()
            if ((current_token == Lex_Type.ID) or (current_token == Lex_Type.NUM)
                    or (current_token == Lex_Type.TRUE) or (current_token == Lex_Type.FALSE)):
                pass
            elif (current_token == Lex_Type.NOT):
                F()
            elif (current_token == Lex_Type.LRB):
                E()
                get_token()
                if (current_token != Lex_Type.PRB): raise SyntaxError(f'Синтаксическая ошибка: F')
            else:
                raise SyntaxError(f'Синтаксическая ошибка: F')


        def F1():
            #F1 --> * F F1| / F F1| and F F1| 𝜀
            #print('F1')

            if ((next_token() == Lex_Type.MUL) or (next_token() == Lex_Type.DIV)
                    or (next_token() == Lex_Type.AND)):
                get_token()
                F()
                F1()
            else:
                pass







        P()
        return True
    except SyntaxError as e:
        print(e)
        sys.exit(1)
    except IndexError as e:
        print(f'Синтаксическая ошибка: IndexError')
        sys.exit(1)




