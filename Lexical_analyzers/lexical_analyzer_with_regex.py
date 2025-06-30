import sys
import re





class TheLexemeDoesNotExist(Exception):
    pass

class CommentSyntaxIsIncorrect(Exception):
    pass





keywords = (r'^or$|'
            r'^and$|'
            r'^not$|'
            r'^true$|'
            r'^false$|'
            r'^program$|'
            r'^var$|'
            r'^begin$|'
            r'^end.$|'
            r'^int$|'
            r'^float$|'
            r'^bool$|'
            r'^as$|'
            r'^if$|'
            r'^then$|'
            r'^else$|'
            r'^for$|'
            r'^to$|'
            r'^do$|'
            r'^while$|'
            r'^read$|'
            r'^write$')

separators = (r'^<>$|'
              r'^=$|'
              r'^<$|'
              r'^<=$|'
              r'^>$|'
              r'^>=$|'
              r'^\+$|'
              r'^-$|'
              r'^\*$|'
              r'^/$|'
              r'^\($|'
              r'^\)$|'
              r'^;$|'
              r'^,$|'
              r'^\[$|'
              r'^\]$|'
              r'^\:$|'
              r'^\{$|'
              r'^\}$')

identifier = (r'^[a-zA-Z][a-zA-Z0-9]*$')

number = (r'^[0-1]+(B|b)$|'
          r'^[0-7]+(O|o)$|'
          r'^[0-9]+(D|d)?$|'
          r'^\d[0-9A-Fa-f]*(H|h)$|'
          r'^\d+(E|e)(\+|-)?\d+$|^(?:\d+)?\.\d+(E|e)(\+|-)?\d+$')







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






def scaner(file_path):
    try:


        with open(file_path, 'r') as f:
            s = f.read()
            #print(f'Код программы:\n\n{s}\n\n')
            s = s.replace('\n', ' ').split()
            #s = [i for i in s if i != '']
            #print(f'Код программы поделённый на лексемы:\n\n{s}\n\n')

        i = 0
        while (i < len(s)):
            lex = s[i]

            if (lex == '{'):
                #print(f'i - {i}\nlen(s) - {len(s)}\n')
                while ((i < len(s)) and (s[i] != '}')):
                    i = i + 1
                #print(f'i - {i}\nlen(s) - {len(s)}\n')
                if (i == len(s)):
                    raise CommentSyntaxIsIncorrect(f'Лексическая ошибка: Ошибка в комментарии')

            elif (lex == '}'):
                raise CommentSyntaxIsIncorrect(f'Лексическая ошибка: Ошибка в комментарии')

            elif (re.match(keywords, lex)):
                token_sequence.append((1, table_of_table[1].index(lex)))
                #print(f'keyword - {lex}')

            elif (re.match(separators, lex)):
                token_sequence.append((2, table_of_table[2].index(lex)))
                #print(f'separator - {lex}')

            elif (re.match(identifier, lex)):
                if (lex not in table_of_table[3]):
                    table_of_table[3].append(lex)
                token_sequence.append((3, table_of_table[3].index(lex)))
                #print(f'identifier - {lex}')

            elif (re.match(number, lex)):
                if (lex not in table_of_table[4]):
                    table_of_table[4].append(lex)
                token_sequence.append((4, table_of_table[4].index(lex)))
                #print(f'number - {lex}')

            else:
                raise TheLexemeDoesNotExist(f'Лексическая ошибка:\nНе существует в модельной языке такой лексемы: {s+ch}')


            i += 1

    except FileNotFoundError:
        print(f'Не существует файла по такому пути: {file_path}')
        sys.exit(1)

    except (TheLexemeDoesNotExist or CommentSyntaxIsIncorrect) as  e:
        print(e)
        sys.exit(1)

    return [token_sequence, table_of_table]