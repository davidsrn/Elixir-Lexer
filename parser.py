import ply.lex as lex
import ply.yacc as yacc

# Numero de tests
test_num = 15 + 1
# Palabras reservadas del lenguaje
reserved = {
    'def': 'DEF',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'for': 'FOR',
    'if': 'IF',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE'
    # 'gets': 'GETS',
    # 'puts': 'PUTS',
    # 'io': 'IO'
}

# Lista de token que acepta el parser unida con las palabras reservadas
tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'CONSTANT',
    'GREATEQ', 'LESSEQ', 'AND',
    'PARENL', 'PARENR', 'CHAR', 'OR', 'FOREXPR',
    'NAME', 'INT', 'DOUBLE', 'GREATER', 'LESS',
    'STRING'
    # 'COMMA'
] + list(reserved.values())

# print(tokens)

# Expresiones regulares que identifican a cada token

# t_COMMA = r','
# t_COMMENT = r'\#.*'
# t_ignore_COMMENT = r'\#.*'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_AND = r'&'
t_CHAR = r'\'[a-zA-Z0-9_+\*\- :,\s]*\''
t_CONSTANT = r'\@[a-zA-Z_][a-zA-Z0-9_]*'
t_DEF = r'def'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_FALSE = r'false'
t_FOREXPR = r'<-'
# t_GETS = r'gets'
t_GREATEQ = r'>='
t_GREATER = r'>'
t_IF = r'if'
t_ignore = " \t"
# t_IO = r'IO\.'
t_LESS = r'<'
t_MINUS = r'-'
t_OR = r'\|'
t_PARENL = r'\('
t_PARENR = r'\)'
t_PLUS = r'\+'
# t_PUTS = r'puts'
t_STRING = r'\"[a-zA-Z0-9_\ ][a-zA-Z0-9_\ ]*\"'
t_TIMES = r'\*'
t_TRUE = r'true'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if reserved.has_key(t.value):
        t.type = reserved[t.value]
    return t


# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t


def t_COMMENT(t):
    r'(\"\"\"(.|\n)*?\"\"\")|(\#.*)|(\r)'
    pass


def t_DOUBLE(t):
    r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Value too long %d", t.value)
        t.value = 0
    return t


def t_INT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Value too long %d", t.value)
        t.value = 0
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Invalid character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

print("TOKEN TEST WITH " + str(test_num) + " FILES")
for num in range(test_num):
    print("Lexer test number " + str(num))
    with open("tests/test" + str(num) + ".ex", 'r') as file:
        data = file.read()
    res = lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
    print("-----------------------------------")


# Definicion de presedencia de operadores
precedence = (
    ('left', 'DO', 'END', 'AND', 'OR', 'IF', 'ELSE', 'FOR', 'WHILE', 'TRUE',
     'FALSE', 'FOREXPR', 'NAME'),
    ('left', 'EQUALS', 'CONSTANT', 'CHAR', 'INT',
     'STRING', 'DOUBLE'),
    ('left', 'GREATER', 'LESS', 'GREATEQ', 'LESSEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PARENL', 'PARENR'),
    ('right', 'UMINUS'),
)

# Tabla de simbolos para guardar variables
names = {}

# def p_comment(t):
#     '''statement : COMMENT'''


def p_expr(t):
    '''statements : statements statement
        | statement
        | expression'''


def p_assign(t):
    '''statement : NAME EQUALS expression
                 | CONSTANT expression
                 '''


def p_func(t):
    '''statement : DEF NAME PARENL NAME PARENR DO statements END'''


def p_if(t):
    '''statement : IF expression DO statements END
                 | IF expression DO statements ELSE statements END
                 '''


def p_for(t):
    'statement : FOR NAME FOREXPR NAME DO statements END'


def p_while(t):
    'statement : WHILE expression DO statements END'

# def p_puts(t):
#     '''statement : IO PUTS PARENL statement PARENR
#                  | IO PUTS statement
#                  '''
#
# def p_gets(t):
#     '''statement : IO GETS NUMBER
#     | IO GETS STRING
#     '''

# def p_number(t):
#     'expression : NUMBER'


def p_binary(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  '''


def p_comparison(t):
    '''expression : expression GREATER expression
                  | expression LESS expression
                  | expression GREATEQ expression
                  | expression LESSEQ expression
                  | expression AND expression
                  | expression OR expression'''


def p_minus(t):
    'expression : MINUS expression %prec UMINUS'


def p_group(t):
    'expression : PARENL expression PARENR'


def p_int(t):
    'expression : INT'


def p_double(t):
    'expression : DOUBLE'


def p_char(t):
    'expression : CHAR'


def p_true(t):
    'expression : TRUE'


def p_false(t):
    'expression : FALSE'


def p_string(t):
    'expression : STRING'


def p_name(t):
    'expression : NAME'


def p_error(t):
    if t != None:
        print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

print("\n\nPARSE TEST WITH " + str(test_num) + " FILES")
for num in range(test_num):
    print("Test number " + str(num))
    with open("tests/test" + str(num) + ".ex", 'r') as file:
        data = file.read()
    res = parser.parse(data)
    print("-----------------------------------")
