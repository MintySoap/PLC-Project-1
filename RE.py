import traceback
from REParser import *
from collections import deque
from Counter import *
from States import *

states = deque()
#test cases that don't work:
#a(a+b)*b + b(a+b)*a;
#todo:
#1. figure out how to make it work with multiple inputs status: unsolved

#for first input
def read_input():
    result = ''
    while True:
        data = input('Regex: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i+1]
            break
        else:
            result += data + ' '
    return result

#for second input
def read_string():
    result = ''
    while True:
        data = input('INPUT STRING: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i+1]
            break
        else:
            result += data + ' '
    return result

def main():
    global states
    #outer loop to get first input, the regex expression
    while True:
        #sets the values for each regex iteration
        data = read_input().strip()
        formatted_data = data[:-1] + "#" + data[-1:]
        if data == 'exit;':
            break
        try:
            parser.parse(formatted_data)
        except Exception as err:
            print(err.args[0])
            traceback.print_tb(err.__traceback__)
            print("BAD STRING")

        #calls the necessary functions
        fp = followpos()
        dfa_table = dfa(fp)

        #prints the modified dfa table
        for s in states:
            if(s.get_category() == "start_state"): #prints start state
                print(str(s.get_category())+"("+str(s.get_state())+")")
            #prints all the deltas
            keys = alphabet
            for alph in alphabet:
                print("delta("+str(s.get_state())+","+alph+","+str(dfa_table[str(s.get_state())][alph])+")")
        for st in states:
            if(st.get_category() == "final_state"):
                print(str(st.get_category())+"("+str(st.get_state())+")")

        #inner loop to get the second input, the strings that we check to see if they match the dfa
        while True:
            input_string = read_string().strip()
            keys = list(dfa_table.keys()) #gets a list of the keys (sets) of the dfa table
            current_state = keys[0] #sets the current state to dictionary of first key
            match = False
            not_in_alphabet = False
            last_letter_index = 0;
            for char in range(len(input_string)): #gets the index of the last character which we will see if it is valid
                if(input_string[char] in alphabet):
                    last_letter_index = char
            if input_string == 'exit;':
                break
            for letter in range (len(input_string)):
                if(input_string[letter] == ';'):
                    break
                elif(input_string[letter] not in alphabet):
                    not_in_alphabet = True
                    break
                current_letter_set = dfa_table[str(current_state)][str(input_string[letter])] #this is the corresponding set that the letter is pointing to
                for s in states:#cycles through states
                    if(s.get_category() == "final_state"): #checks to see if the current letter state is equal to the final state
                        if(current_letter_set == s.get_state() and letter == last_letter_index):
                            match = True;
                            break
                current_state = str(dfa_table[str(current_state)][input_string[letter]])
                if(current_state == 'set()'):
                    break

            if(match == True):
                print("MATCH")
            elif(not_in_alphabet == True):
                print("NO MATCH: Invalid input character")
            else:
                print("NO MATCH")

def followpos(): #question: how does this work with each individual tree?
    global nodes,alphabet,c
    #sets up the blank table/dictionary for followpos
    followpos = {}
    for i in range(c.get_value()):
        followpos[i+1] = set()

    #assigns followpos values
    for n in nodes:
        if(n._operator == '.'):
            for i in n._lchild._lastpos:
                followpos[i] = followpos[i].union(n._rchild._firstpos)
        elif (n._operator == '*'):
            for i in n._lastpos:
                followpos[i] = followpos[i].union(n._firstpos) 
    return followpos

def dfa(followpos_set):
    global nodes,alphabet,states

    final_state_pos = 0
    for n in nodes: #establishes final state position for later
        if(n._symbol == "#"):
            final_state_pos = n._position

    #DFA stuff
    dfa = {}
    s0 = States(nodes[-1]._firstpos)
    s0.set_category("start_state")
    states.append(s0)
    unmarked_in_states = True
    T = states[-1]
    while (unmarked_in_states):
        for uwu in states:
            if(uwu.get_marked() == False):
                uwu.set_marked(True)
                T = uwu
                break
        dfa[str(T.get_state())] = {} #sets dfa table
        for a in alphabet:
            u = set()
            insert_u=True
            for p in T.get_state(): #goes through elements of T to get leaf numbers
                for n in nodes: #goes through nodes to find node that has the correct symbol and position
                    if (n._symbol == a and n._position == p):
                        u = u.union(followpos_set[p])
            for i in states:
                if(i.get_state() == u or len(u) == 0): #this should eliminate duplicate states in states
                    insert_u = False
            if(insert_u):
                states.append(States(u))
            dfa[str(T.get_state())][a] = u
        #breaks out of the loop if we there's no unmarked states
        unmarked_in_states = False #termination condition
        for s in states:
            if(s.get_marked() == False):
                unmarked_in_states = True

    for s in states: #cycles through the states
        for pos in s.get_state(): #cycles through the individual 
            if(pos == final_state_pos):
                s.set_category("final_state")
                break #breaks out of inner loop
    return dfa

def test(): #random testing thing so I can test out my stuff
    global nodes, alphabet,c
    data = "a*bb*a#;"
    #counter = 1;
    #nodes = []
    #alphabet = []
    parser.parse(data)
    fp=followpos()
    print(dfa(fp))

#test()

main()