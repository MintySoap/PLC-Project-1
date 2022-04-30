import ply.lex as lex

reserved = {}

tokens = ['SEMI','PLUS','STAR','LETTER','EPSILON','LPAR','RPAR','END'] + \
    list(reserved.values())

t_SEMI = r';'
t_LPAR = r'\('
t_RPAR = r'\)'
t_PLUS = r'\+'
t_STAR = r'\*'
t_EPSILON = r'\^'
t_END = r'\#'

#establishes the token for letter lexemes
def t_LETTER(t):
    r'[a-zA-Z0-9]'
    t.type = reserved.get(t.value.lower(),'LETTER')
    t.value = t.value
    return t

# Ignored characters
t_ignore = " \r\n\t"#

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    #t.lexer.skip(1)
    raise Exception('LEXER ERROR')

lexer = lex.lex()