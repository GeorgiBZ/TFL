from Lexical_analyzers.finite_stat_machine_lexical_analyzer import *
from Lexical_analyzers.lexical_analyzer_with_regex import scaner
from Syntax_analyzers.recursive_descent_parser import parser
from Programs_in_model_language.Path import *

file_path = list_of_path[5]

def f(a, b):
    token_a = a[0]
    table_a = a[1]
    token_b = b[0]
    table_b = b[1]

    print(f'{len(token_a)}---{token_a}')
    print(f'{len(token_b)}---{token_b}\n\n')

    for i in range(len(token_a)):
        print(f'{table_a[token_a[i][0]][token_a[i][1]] == table_b[token_b[i][0]][token_b[i][1]]}\t'
              f'{token_a[i]} --- {table_a[token_a[i][0]][token_a[i][1]]}\t'
              f'{token_b[i]} --- {table_b[token_b[i][0]][token_b[i][1]]}')


    print('\n\n')
    print(f'token_a == token_b --- {token_a == token_b}')

lex = lexer(file_path)

#f(lex, scaner(file_path))

parser(lex[0], lex[1])
