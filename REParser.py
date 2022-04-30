import ply.yacc as yacc
from RELexer import tokens
from RENode import RENode
from Counter import *

#records position
c = Counter() #so for some reason, counter is always 1?
#this list allows us to traverse later for followpos
nodes = []
alphabet = []

#start functions
def p_begin_1(p):
    'begin : re SEMI'
    p[0] = p[1]

#re functions
def p_re_1(p):
    're : term'
    p[0] = p[1]

def p_re_2(p): # + node
    're : re PLUS term'
    global nodes
    n = RENode()
    n._operator = '+'
    n._lchild = p[1]
    n._rchild = p[3]
    p[0] = n
    n._nullable = n._lchild._nullable or n._rchild._nullable
    n._firstpos = n._lchild._firstpos.union(n._rchild._firstpos)
    n._lastpos = n._lchild._lastpos.union(n._rchild._lastpos)
    nodes.append(n)


#term functions
def p_term_1(p):
    'term : factor'
    p[0] = p[1]

def p_term_2(p): #concat node
    'term : term factor'
    global nodes
    n = RENode()
    n._operator = '.'
    n._lchild = p[1]
    n._rchild = p[2]
    p[0] = n
    n._nullable = n._lchild._nullable and n._rchild._nullable
    if(n._lchild._nullable == True):
        n._firstpos = n._lchild._firstpos.union(n._rchild._firstpos)
    else:
        n._firstpos = n._lchild._firstpos
    if(n._rchild._nullable == True):
        n._lastpos = n._lchild._lastpos.union(n._rchild._lastpos)
    else:
        n._lastpos = n._rchild._lastpos
    nodes.append(n)

#factor functions
def p_factor_1(p):
    'factor : niggle'
    p[0] = p[1]

def p_factor_2(p): # * node
    'factor : factor STAR'
    global nodes
    n = RENode()
    n._operator = '*'
    n._lchild = p[1]
    p[0] = n
    n._nullable = True
    n._firstpos = n._lchild._firstpos
    n._lastpos = n._lchild._lastpos
    nodes.append(n)


#niggle functions
def p_niggle_1(p): #leaf node
    'niggle : LETTER'
    global alphabet,nodes,c
    n = RENode()
    n._operator = 'leaf'
    n._position = c.get_value()
    c.set_value(c.get_value()+1)
    n._symbol = p[1]
    p[0] = n
    n._nullable = False
    n._firstpos.add(n._position)
    n._lastpos.add(n._position)
    nodes.append(n)
    #adds the letter to the alphabet
    if(p[1] not in alphabet):
        alphabet.append(p[1])

def p_niggle_2(p): #leaf node
    'niggle : EPSILON'
    global nodes
    n = RENode()
    n._operator = 'leaf'
    n._symbol = p[1]
    p[0] = n
    n._nullable = True
    nodes.append(n)

def p_niggle_3(p): 
    'niggle : LPAR re RPAR'
    p[0] = p[2]

def p_niggle_4(p):
    'niggle : END'
    global nodes
    n= RENode()
    n._operator = 'leaf'
    n._position = c.get_value()
    n._symbol = p[1]
    p[0] = n
    n._nullable = False
    n._firstpos.add(n._position)
    n._lastpos.add(n._position)
    nodes.append(n)

def p_error(p):
    print("Syntax error in input!")

def set_values():
    c.set_value(1)
    nodes = []
    alphabet = []

parser = yacc.yacc()