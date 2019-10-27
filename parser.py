#!/usr/bin/env python2
# import pprint as pp
import ply.yacc as yacc
import ply.lex as lex
import sys

#
# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     # else:
#     #     pip._internal.main(['install', package])
#
#
# install("pprint")
# install("ply")


# test = input("numero de test > ")
# print(sys.argv)
# test = "test" + str(test) + ".ex"
test = "test" + str(sys.argv[1]) + ".ex"

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
    t.lineno += t.value.count('\n')
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
    print("Invalid character '{0}' at {1}", t.value[0], t.lineno)
    t.lexer.skip(1)


""" Aqui se construye el lexer"""
lexer = lex.lex()

""" Lee cada uno de los archivos de prueba y tokeniza su contenido imprimiendo
    cada token conforme lo lee"""

with open("tests/" + test, 'r') as file:
    data = file.read()
    res = lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        # print(tok)


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
i = 0
# Tabla de simbolos para guardar variables
scopes = [{}]
# Arbol para imprimir todo
tree = {}

# Caso base de donde todo se va construido
# NOTA: todos los scopes son llamados cuando se ve un scope[-1]
def p_expr(t):
    '''statements : statements statement
        | statement
        | expression'''
    if(len(t) == 3):
        # t[0] = (p-expression', t[1], t[2])
        t[0] = (t[1], t[2])
    else:
        # t[0] = ('p-expression', t[1])
        t[0] = (t[1])

# Si lee un nombre o una constante espera una expresion despues


def p_assign_cons(t):
    '''statement : CONSTANT expression
                 '''
    t[0] = ('assign', t[1][1:])
    scopes[-1][t[0]] = t[2]
    tree[t[0]] = t[0]


def p_assign_var(t):
    '''statement : NAME EQUALS expression
                 | NAME EQUALS expression PARENL expression PARENR
                 '''
    t[0] = ('assign', t[1])
    tree[t[0]] = t[0]
    scopes[-1][t[0]] = t[3]

# Define una funcion y agrega su nombre a la tabla de simbolos
def p_func(t):
    '''statement : DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END
                 | DEF NAME PARENL empty PARENR DO new_scope statements end_scope END
                 | DEF NAME DO new_scope statements end_scope END'''
    if(len(t) == 11):
        t[0] = ('func-statement', t[2], t[8])
    else:
        t[0] = ('func-statement', t[2], t[5])
    tree[t[0]] = t[0]
    scopes[-1][('assign', t[2])] = t[2]
# Para definir un if y sus dos posibilidades

# Esto hace psoible hacer un nuevo scope para los ifs
def p_if_scope(t):
    'statement : new_scope if_statement end_scope'


def p_if(t):
    '''if_statement : IF expression DO statements END
                 | IF expression DO statements ELSE statements END
                 '''
    if(len(t) == 6):
        t[0] = ('if-statement', t[2], t[4])
    else:
        t[0] = ('if-statement', t[2], t[4], t[5])

    tree[t[0]] = t[0]
# Para definir la estructira de un if


def p_for(t):
    'statement : FOR NAME FOREXPR NAME DO new_scope statements end_scope END'
    # name_scope[t[2]] = get_scope()
    t[0] = ('for-expression', t[2], t[7])
    tree[t[0]] = t[0]

# Los while no existen en elixir ya que en esencia es funcional
# def p_while(t):
#     'statement : WHILE expression DO statements END'

# Para definir las operaciones binarias


def p_binary(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATEQ expression
                  | expression LESSEQ expression
                  | expression AND expression
                  | expression OR expression
                  '''
    t[0] = ('binary-expression', t[2], t[1], t[3])
    flag = True
    while(True):
        if(t[1][0] == 'name'):
            if(scopes[-1].has_key(('assign', t[1][1]))):
                t[1] = scopes[-1][('assign', t[1][1])]
            else:
                # print("Var out of scope")
                flag = not flag
                break
        else:
            break
    while(True):
        if(t[3][0] == 'name'):
            if(scopes[-1].has_key(('assign', t[1][1]))):
                t[3] = scopes[-1][('assign', t[3][1])]
            else:
                # print("Var out of scope")
                flag = not flag
                break
        else:
            break

    if(t[1][0] != t[3][0] and flag):
        if(not((t[1][0] == "double" and t[3][0] == "int") or (t[3][0] == "double" and t[1][0] == "int"))):
            print("Can't do " + t[0][1] + " with " +
                  t[1][0] + " and " + t[3][0])
    tree[t[0]] = t[0]

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


def p_name(t):
    'expression : NAME'
    t[0] = ('name', t[1])
    if not scopes[-1].has_key(('assign', t[0][1])):
        print("Var " + t[1] + " doesn't exist")

# Funciones para definir la creacion y destruccion de scopes

def p_empty(p):
    'empty :'
    pass

def p_new_scope(t):
    "new_scope : empty"
    scopes.append(scopes[-1].copy())

def p_end_scope(t):
    " end_scope : empty"
    scopes.pop()


# Aqui se imprime el error si existe alguno

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Evita que pare y siga leyendo token a pesar de encontrar un error
        parser.errok()
    # else:
    #     print("Syntax error at EOF")


# Se construye el parser
parser = yacc.yacc()


""" Lee cada uno de los archivos de prueba y parsea su contenido imprimiendo
    en caso de un error el error o en caso de que se ejecuto correctamente nada"""

print("Code to test:")
print("-----------------------------------")
with open("tests/" + test, 'r') as file:
    data = file.read()
    print(data)
print("-----------------------------------")
print("Errors (if any):")
print("-----------------------------------")
res = parser.parse(data)
print("-----------------------------------")
print("TREE")
print("-----------------------------------")
flag = False

# Imprime el arbol de manera bonita
for leaf in tree:
    for data in leaf:
        if not data == None:
            if isinstance(data, tuple):
                for a in range(i):
                    print("| "),
                print(data)
                i=i-1
            elif data == "assign":
                for a in range(i):
                    print("| "),
                print(data),
                flag = True
                i=i-1
            elif data == "+" or data == "-" or data == ">" or data == "<":
                for a in range(i):
                    print("| "),
                i=i-1
                print(data)
            else:
                if not flag:
                    for a in range(i):
                        print("| "),
                flag = False
                print(data)
        i = i+1
    i=i-1
parser.restart()
print("-----------------------------------")
