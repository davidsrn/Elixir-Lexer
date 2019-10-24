import ply.lex as lex
import ply.yacc as yacc
import pprint as pp


class Scope(object):
    def __init__(self):
        self.i = 1


scope = Scope()

test = input("numero de test > ")

test = "test" + str(test) + ".ex"

# Numero de tests
test_num = 16 + 1

""" Palabras reservadas del lenguaje
 Cada una de ellas es definida y agregada a la lista de tokens"""

reserved = {
    'def': 'DEF',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'for': 'FOR',
    'if': 'IF',
    'true': 'TRUE',
    'false': 'FALSE'
    # 'while': 'WHILE',
    # 'gets': 'GETS',
    # 'puts': 'PUTS',
    # 'io': 'IO'
}

""" Lista de token que acepta el parser unida con las palabras reservadas """

tokens = [
    'FOREXPR',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'CONSTANT',
    'GREATEQ', 'LESSEQ', 'AND',
    'PARENL', 'PARENR', 'CHAR', 'OR',
    'NAME', 'INT', 'DOUBLE', 'GREATER', 'LESS',
    'STRING'
    # 'COMMA'
] + list(reserved.values())

""" Expresiones regulares que identifican a cada token
 Dependiendo del la expresion regular se asigna el valor del token al
 lo leido """

# t_COMMA = r','
# t_COMMENT = r'\#.*'
# t_ignore_COMMENT = r'\#.*'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_FOREXPR = r'[a-zA-Z_][a-zA-Z0-9_]*[ ]*<-'
t_FOREXPR = r'<-'
t_AND = r'&'
t_CHAR = r'\'[a-zA-Z0-9_+\*\- :,\s]*\''
t_CONSTANT = r'\@[a-zA-Z_][a-zA-Z0-9_]*'
t_DEF = r'def'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_FALSE = r'false'
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
# t_FORNAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
# Expresion para definir que se leyo un nombre de variable


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if reserved.has_key(t.value):
        # if t.value in reserved:
        t.type = reserved[t.value]
    # t.value = (t.value, symbol_lookup(t.value))
    return t

# Si la linea comienza con un # o el texto esta entre tres comillas
# """texto"""" se ignora y no se tokeniza


def t_COMMENT(t):
    r'(\"\"\"(.|\n)*?\"\"\")|(\#.*)|(\r)'
    pass

# Expresion para leer e identificar un doble


def t_DOUBLE(t):
    r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Value too long %d", t.value)
        t.value = 0
    return t

# Expresion para leer e identificar un int


def t_INT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Value too long %d", t.value)
        t.value = 0
    return t

# Lee saltos de linea y los agrega al lexer para saber el numero de linea


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Imprime un error si un caracter no es identificado


def t_error(t):
    print("Invalid character '%s'" % t.value[0])
    t.lexer.skip(1)


""" Aqui se construye el lexer"""
lexer = lex.lex()

""" Lee cada uno de los archivos de prueba y tokeniza su contenido imprimiendo
    cada token conforme lo lee"""

# print("TOKEN TEST WITH " + str(test_num) + " FILES")
# for num in range(test_num):
#     print("Lexer test number " + str(num))
#     with open("tests/test" + str(num) + ".ex", 'r') as file:
#         data = file.read()
#     res = lexer.input(data)
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break      # No more input
#         print(tok)
#     print("-----------------------------------")

with open("tests/" + test, 'r') as file:
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
    ('left', 'DO', 'END', 'AND', 'OR', 'IF', 'ELSE', 'FOR', 'TRUE',
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
i = 0
names = {}
names_type = {}
name_scope = {}
# scopes=[{}]
# def p_comment(t):
#     '''statement : COMMENT'''

# Caso base de donde todo se va construido
#
# def p_new_scope(t):
#      "new_scope : statement"
#      # Create a new scope for local variables
#      # names = {}
#      print("NEW SCOPE")
#      scopes.append({})
# def p_end_scope(t):
#     " end_scope : "
#     print("ENDSCOPE")
#     scopes.pop()


def p_expr(t):
    '''statements : statements statement
        | statement
        | expression'''
    t[0] = ('p-expression', t[1])
# Si lee un nombre o una constante espera una expresion despues


def p_assign_cons(t):
    '''statement : CONSTANT expression
                 '''
    name_scope[t[1][1:]] = get_scope()
    t[0] = ('assign', t[1][1:])
    names[t[0]] = t[2]


def p_assign_var(t):
    '''statement : NAME EQUALS expression
                 '''
    name_scope[t[1]] = get_scope()
    t[0] = ('assign', t[1])
    names[t[0]] = t[3]


def p_func(t):
    '''statement : DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END
                 | DEF NAME PARENL empty PARENR DO new_scope statements end_scope END '''
    t[0] = ('func-statement', t[7])
# Para definir un if y sus dos posibilidades


def p_if(t):
    '''statement : IF new_scope expression end_scope DO new_scope statements end_scope END
                 | IF new_scope expression end_scope DO new_scope statements ELSE new_scope statements end_scope END
                 '''
    t[0] = ('if-expression-statement', t[1], t[3])
# Para definir la estructira de un if


def p_for(t):
    'statement : FOR NAME FOREXPR NAME DO new_scope statements end_scope END'
    name_scope[t[2]] = get_scope()
    t[0] = ('for-expression', t[6])
# Los while no existen en elixir ya que en esencia es funcional
# def p_while(t):
#     'statement : WHILE expression DO statements END'

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

# Para definir las operaciones binarias


def p_binary(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  '''
    t[0] = ('binary-expression', t[2], t[1], t[3])
    while(True):
        if(t[1][0] == 'name'):
            # print(names)
            t[1] = names[('assign', t[1][1])]
            # t[1][1] = names[('assign-expression', t[1][1])][1]
            # t[1][0] = names[('assign-expression', t[1][1])][0]
            # print(t[1])
        else:
            break;
    while(True):
        if(t[3][0] == 'name'):
            t[3] = names[('assign', t[3][1])]
            # t[3][1] = names[('assign-expression', t[3][1])][1]
            # t[3][0] = names[('assign-expression', t[3][1])][0]
            # print(t[3])
        else:
            break;

    if(t[1][0] != t[3][0]):
        if(not((t[1][0] == "double" and t[3][0] == "int") or (t[3][0] == "double" and t[1][0] == "int"))):
            print("Can't do "+t[0][1]+" with " + t[1][0] +" and " + t[3][0] )
# Para definir las operaciones de comparacion (aun no el


def p_comparison(t):
    '''expression : expression GREATER expression
                  | expression LESS expression
                  | expression GREATEQ expression
                  | expression LESSEQ expression
                  | expression AND expression
                  | expression OR expression'''
    t[0] = ('binary-expression', t[2], t[1], t[3])
    while(True):
        if(t[1][0] == 'name'):
            # print(names)
            t[1] = names[('assign', t[1][1])]
            # t[1][1] = names[('assign-expression', t[1][1])][1]
            # t[1][0] = names[('assign-expression', t[1][1])][0]
            # print(t[1])
        else:
            break;
    while(True):
        if(t[3][0] == 'name'):
            t[3] = names[('assign', t[3][1])]
            # t[3][1] = names[('assign-expression', t[3][1])][1]
            # t[3][0] = names[('assign-expression', t[3][1])][0]
            # print(t[3])
        else:
            break;

    if(t[1][0] != t[3][0]):
        if((t[1][0] == "double" and t[3][0] == "int") or (t[3][0] == "double" and t[1][0] == "int")):
            print("")
        else:
            print("Can't do "+t[0][1]+" with " + t[1][0] +" and " + t[3][0] )
# Para definir que se esta definiendo un numero negativo


def p_minus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = ('min-expression', t[2])
# Para definir que un grupo es algo dentro de parentesis


def p_group(t):
    'expression : PARENL new_scope expression end_scope PARENR'
    t[0] = ('group-expression', t[2])
# Definir que un expr puede ser un int


def p_int(t):
    'expression : INT'
    t[0] = ('int', t[1])
# O doble


def p_double(t):
    'expression : DOUBLE'
    t[0] = ('double', t[1])
# O char


def p_char(t):
    'expression : CHAR'
    t[0] = ('char', t[1])
# O un true


def p_true(t):
    'expression : TRUE'
    t[0] = ('true', t[1])
# O un false


def p_false(t):
    'expression : FALSE'
    t[0] = ('false', t[1])
# O una cadena de caracters


def p_string(t):
    'expression : STRING'
    t[0] = ('string', t[1])
# o el nombre de una variable

# def p_forname(t):
#     'expression : FORNAME'
#     name_scope[t[1]] = t[1]
#     t[0] = ('forname-expresion', t[1])


def p_name(t):
    'expression : NAME'
        # print(name_scope)/
    t[0] = ('name', t[1])
    if name_scope.has_key(t[0][1]):
        if(get_scope() < name_scope[t[1]]):
            print("Var " + t[1] + " not accesible in this scope")
            # print(name_scope)
    else:
        print("Var " + t[1] + " doesn't exist")
        name_scope[t[0][1]] = t[1]
        names[('assign', t[0][1])] = ('int', t[0][1])
        # print(names)


def p_empty(p):
    'empty :'
    pass


def del_scope():
    scope.i = scope.i - 1


def add_scope():
    scope.i = scope.i + 1


def get_scope():
    return scope.i


def p_new_scope(t):
    "new_scope : empty"
    # Create a new scope for local variables
    # names = {}
    # print("NEW SCOPE")
    # scopes.append({})
    add_scope()
    # print(get_scope())


def p_end_scope(t):
    " end_scope : empty"
    # print("ENDSCOPE")
    del_scope()
    # print(get_scope())
    # scopes.pop()

# Aqui se imprime el error si existe alguno


# def p_error(t):
#     if t != None:
#         print("Syntax error at '%s'" % t.value)
#
# def p_error(t):
#      print("Whoa. No sabes escribir en elixir you n00b.")
#      if not t:
#          print("End of File!")
#          return
#
#      # Read ahead looking for a closing '}'
#      while True:
#          tok = parser.token()             # Get the next token
#          if not tok or tok.type == 'RBRACE':
#              break
#      parser.restart()

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    # else:
        # print("Syntax error at EOF")


# Se construye el parser
parser = yacc.yacc()


""" Lee cada uno de los archivos de prueba y parsea su contenido imprimiendo
    en caso de un error el error o en caso de que se ejecuto correctamente nada"""

# print("\n\nPARSE TEST WITH " + str(test_num) + " FILES")
# for num in range(test_num):
#     print("Test number " + str(num))
#     with open("tests/test" + str(num) + ".ex", 'r') as file:
#         data = file.read()
#     res = parser.parse(data)
#     pp.pprint(names)
#     print("-----------------------------------")
#     pp.pprint(name_scope)
#     parser.restart()
#     print("-----------------------------------")
with open("tests/" + test, 'r') as file:
    data = file.read()
res = parser.parse(data)
print("-----------------------------------")
print("TREE")
print("-----------------------------------")
pp.pprint(names)
# pp.pprint(name_scope)
parser.restart()
print("-----------------------------------")
