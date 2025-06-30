from enum import Enum
from Table_of_lexem_token_sequence.table_lexem_and_token_sequence import *

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
    M11 = 30
    M12 = 19
    M13 = 20
    M2 = 21
    M21 = 22
    OG = 23


    C1 = 24
    C2 = 25
    C3 = 26
    C4 = 27


    ER = 28


ch = ''

s = ''

b = 0

cs = State.H

z = 0

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
         'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']