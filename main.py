from Lexical_analyzers.finite_stat_machine_lexical_analyzer import lexer
from Lexical_analyzers.lexical_analyzer_with_regex import scaner
from Syntax_analyzers.recursive_descent_parser import parser
from Programs_in_model_language.Path import list_of_path

file_path = list_of_path[2][1]


tokens = lexer(file_path)
print(f'Лексический анализ успешно прошёл!')
parser(tokens[0], tokens[1])
print(f'Синтаксический анализ успешно прошёл!')