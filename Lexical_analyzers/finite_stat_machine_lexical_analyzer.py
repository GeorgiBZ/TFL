import sys
from enum import Enum










class TheLexemeDoesNotExist(Exception):
    pass

class CommentSyntaxIsIncorrect(Exception):
    pass

class State(Enum):

    H = 1
    ID_OR_KEYWORDS = 2


    N2_N8_N10_N16_E10_E10P = 3
    N8_N10_N16_E10_E10P = 4
    N10_N16_E10_E10P = 5
    E10P = 6
    N16 = 7
    B_N16 = 8
    D_N16 = 9
    N16_E10 = 10
    N16_unsE10 = 11
    O = 12
    HX = 13
    E = 14
    SIGN = 15
    DEGREE = 16
    FRACTION = 17



    M1 = 18
    M11 = 19
    M12 = 20
    M13 = 21
    M2 = 22
    M21 = 23
    OG = 24


    C1 = 25
    C2 = 26
    C3 = 27
    C4 = 28


    ER = 29

ch = ''

s = ''

cs = State.H

z = 0

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
         'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']




table_of_keywords = ['', 'or', 'and', 'not', 'true', 'false', 'program', 'var',
                     'begin', 'end.', 'int', 'float', 'bool', 'as', 'if',
                     'then', 'else', 'for', 'to', 'do', 'while', 'read', 'write']

table_of_separators = ['','<>', '=', '<', '<=', '>', '>=', '+', '-', '*', '/', '(',
                       ')', ';', ',', '[', ']', ':', '{', '}']

table_of_identifier = ['', ]

table_of_number = ['', ]

table_of_table = [[], table_of_keywords, table_of_separators,
                  table_of_identifier, table_of_number]

token_sequence = []









def lexer(file_path):
    try:
        global ch, s, cs, z
        global alpha, digits
        global table_of_keywords, table_of_separators
        global table_of_identifier, table_of_number
        global table_of_table
        global token_sequence
        f = open(file_path, 'r')









        def gc(file = f):
            global ch
            ch = file.read(1)

        def let():
            global ch, alpha
            return (ch in alpha)

        def digit():
            global ch, digits
            return (ch in digits)

        def nill():
            global s
            s = ''

        def add():
            global s, ch
            s = s + ch

        def look(t):
            global s, z

            if (s in t):
                z =  t.index(s)
            else:
                z = 0

        def put(t):
            global s

            if (s not in t):
                t.append(s)
            return t.index(s)

        def out(n, k):
            token_sequence.append((n, k))

        def isseparator():
            global s, z
            if ((s in table_of_separators) and (s != '')):
                z = table_of_separators.index(s)
            else:
                z = 0









        gc()
        #print(f'ch == {ch}\ts == {s}\tcs == {cs}\ttoken_sequence == {token_sequence[-1::-1]}')
        while ((ch != '') and (cs != State.ER)):
            #print(f'ch == {ch}\ts == {s}\tcs == {cs}\ttoken_sequence == {token_sequence[-1::-1]}')

            match cs:


                case State.H:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        gc()
                        cs = State.H
                    elif (let()):
                        nill(); add(); gc()
                        cs = State.ID_OR_KEYWORDS
                    elif ((ch == '0') or (ch == '1')):
                        nill(); add(); gc()
                        cs = State.N2_N8_N10_N16_E10_E10P
                    elif ((ch == '2') or (ch == '3')
                          or (ch == '4') or (ch == '5')
                          or (ch == '6') or (ch == '7')):
                        nill(); add(); gc()
                        cs = State.N8_N10_N16_E10_E10P
                    elif ((ch == '8') or (ch == '9')):
                        nill(); add(); gc()
                        cs = State.N10_N16_E10_E10P
                    elif (ch == '.'):
                        nill(); add(); gc()
                        cs = State.E10P
                    elif (ch == '}'):
                        cs = State.ER
                        raise CommentSyntaxIsIncorrect(f'Лексическая ошибка: Ошибка в комментарии')
                    elif (ch == '{'):
                        nill(); gc()
                        cs = State.C1
                    elif (ch == '<'):
                        nill(); add(); gc()
                        cs = State.M1
                    elif (ch == '>'):
                        nill(); add(); gc()
                        cs = State.M2
                    else:
                        nill(); add(); gc()
                        cs = State.OG


                case State.ID_OR_KEYWORDS:
                    if (let() or digit() or ((ch == '.') and (s == "end"))):
                        add(); gc()
                        cs = State.ID_OR_KEYWORDS
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        look(table_of_keywords)
                        if (z != 0 ):
                            out(1, z)
                        else:
                            out(3, put(table_of_identifier))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N2_N8_N10_N16_E10_E10P:
                    if ((ch == '0') or (ch == '1')):
                        add(); gc()
                        cs = State.N2_N8_N10_N16_E10_E10P
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    elif ((ch == '2') or (ch == '3')
                          or (ch == '4') or (ch == '5')
                          or (ch == '6') or (ch == '7')):
                        add(); gc()
                        cs = State.N8_N10_N16_E10_E10P
                    elif ((ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.N10_N16_E10_E10P
                    elif ((ch == 'A') or (ch == 'a')
                          or (ch == 'C') or (ch == 'c')
                          or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'B') or (ch == 'b')):
                        add(); gc()
                        cs = State.B_N16
                    elif ((ch == 'D') or (ch == 'd')):
                        add(); gc()
                        cs = State.D_N16
                    elif ((ch == 'E') or (ch == 'e')):
                        add(); gc()
                        cs = State.N16_E10
                    elif ((ch == 'O') or (ch == 'o')):
                        add(); gc()
                        cs = State.O
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif ((ch == '.')):
                        add(); gc()
                        cs = State.E10P
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N8_N10_N16_E10_E10P:
                    if ((ch == '0') or (ch == '1')
                            or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5')
                            or (ch == '6') or (ch == '7')):
                        add(); gc()
                        cs = State.N8_N10_N16_E10_E10P
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    elif ((ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.N10_N16_E10_E10P
                    elif ((ch == 'A') or (ch == 'a')
                          or (ch == 'B') or (ch == 'b')
                          or (ch == 'C') or (ch == 'c')
                          or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'D') or (ch == 'd')):
                        add(); gc()
                        cs = State.D_N16
                    elif ((ch == 'E') or (ch == 'e')):
                        add(); gc()
                        cs = State.N16_E10
                    elif ((ch == 'O') or (ch == 'o')):
                        add(); gc()
                        cs = State.O
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif (ch == '.'):
                        add(); gc()
                        cs = State.E10P
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N10_N16_E10_E10P:
                    if ((ch == '0') or (ch == '1')
                            or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5')
                            or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.N10_N16_E10_E10P
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    elif ((ch == 'A') or (ch == 'a')
                          or (ch == 'B') or (ch == 'b')
                          or (ch == 'C') or (ch == 'c')
                          or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'D') or (ch == 'd')):
                        add(); gc()
                        cs = State.D_N16
                    elif ((ch == 'E') or (ch == 'e')):
                        add(); gc()
                        cs = State.N16_E10
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif (ch == '.'):
                        add(); gc()
                        cs = State.E10P
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N16:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                    or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                    or (ch == '8') or (ch == '9') or (ch == 'A') or (ch == 'a')
                    or (ch == 'B') or (ch == 'b') or (ch == 'C') or (ch == 'c')
                    or (ch == 'D') or (ch == 'd') or (ch == 'E') or (ch == 'e')
                            or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.B_N16:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9') or (ch == 'A') or (ch == 'a')
                            or (ch == 'B') or (ch == 'b') or (ch == 'C') or (ch == 'c')
                            or (ch == 'D') or (ch == 'd') or (ch == 'E') or (ch == 'e')
                            or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.D_N16:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9') or (ch == 'A') or (ch == 'a')
                            or (ch == 'B') or (ch == 'b') or (ch == 'C') or (ch == 'c')
                            or (ch == 'D') or (ch == 'd') or (ch == 'E') or (ch == 'e')
                            or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N16_E10:
                    if ((ch == 'A') or (ch == 'a') or (ch == 'B') or (ch == 'b')
                            or (ch == 'C') or (ch == 'c') or (ch == 'D') or (ch == 'd')
                            or (ch == 'E') or (ch == 'e') or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                          or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                          or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.N16_unsE10
                    elif (ch == '+') or (ch == '-'):
                        add(); gc()
                        cs = State.SIGN
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.N16_unsE10:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                          or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                          or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.N16_unsE10
                    elif ((ch == 'A') or (ch == 'a') or (ch == 'B') or (ch == 'b')
                            or (ch == 'C') or (ch == 'c') or (ch == 'D') or (ch == 'd')
                            or (ch == 'E') or (ch == 'e') or (ch == 'F') or (ch == 'f')):
                        add(); gc()
                        cs = State.N16
                    elif ((ch == 'H') or (ch == 'h')):
                        add(); gc()
                        cs = State.HX
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.SIGN:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                          or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                          or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.DEGREE
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.DEGREE:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.DEGREE
                    elif ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.O:
                    if ((ch == ' ') or (ch == '\t')
                          or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.HX:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.E10P:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.FRACTION
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.FRACTION:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.FRACTION
                    elif ((ch == 'E') or (ch == 'e')):
                        add(); gc()
                        cs = State.E
                    elif ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        out(4, put(table_of_number))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.E:
                    if ((ch == '0') or (ch == '1') or (ch == '2') or (ch == '3')
                            or (ch == '4') or (ch == '5') or (ch == '6') or (ch == '7')
                            or (ch == '8') or (ch == '9')):
                        add(); gc()
                        cs = State.DEGREE
                    elif ((ch == '+') or (ch == '-')):
                        add(); gc()
                        cs = State.SIGN
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.C1:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        gc()
                        cs = State.C2
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')



                case State.C2:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        gc()
                        cs = State.C3
                    else:
                        while ((ch != ' ') and (ch != '\t')
                            and (ch != '\r') and (ch != '\n')):
                            if (ch != ''):
                                gc()
                                cs = State.C2
                            else:
                                cs = State.ER
                                raise CommentSyntaxIsIncorrect(f'Лексическая ошибка: Ошибка в комментарии')


                case State.C3:
                    if (ch == '}'):
                        gc()
                        cs = State.C4
                    else:
                        gc()
                        cs = State.C2


                case State.C4:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        gc()
                        cs = State.H
                    else:
                        gc()
                        cs = State.C2


                case State.M1:
                    if (ch == ' '):
                        out(2, put(table_of_separators))
                        cs = State.H
                    elif (ch == '>'):
                        add();gc()
                        cs = State.M11
                    elif (ch == '='):
                        add(); gc()
                        cs = State.M12
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.M11:
                    if (ch == ' '):
                        out(2, put(table_of_separators))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.M12:
                    if (ch == ' '):
                        out(2, put(table_of_separators))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.M2:
                    if (ch == ' '):
                        out(2, put(table_of_separators))
                        cs = State.H
                    elif (ch == '='):
                        add(); gc()
                        cs = State.M21
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.M21:
                    if (ch == ' '):
                        out(2, put(table_of_separators))
                        cs = State.H
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


                case State.OG:
                    if ((ch == ' ') or (ch == '\t')
                            or (ch == '\r') or (ch == '\n')):
                        isseparator()
                        if (z != 0):
                            out(2, z)
                            cs = State.H
                        else:
                            cs = State.ER
                            raise TheLexemeDoesNotExist(
                                f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s + ch}')
                    else:
                        cs = State.ER
                        raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


    except FileNotFoundError:
        print(f'Не существует файла по такому пути: {file_path}')
        sys.exit(1)

    except (TheLexemeDoesNotExist or CommentSyntaxIsIncorrect) as e:
        print(e)
        sys.exit(1)


    f.close()
    return [token_sequence, table_of_table]
