#! /usr/bin/env python3

from sys import argv

from parser import *
from lexer import *
from regex_lex_tokens import *

def main():
    f_data = open(argv[1]).read()
    print(f_data)

    l = Lexer()
    for r in regexes:
        l.add(r[0], r[1], r[2])

    tokens = l.lex(f_data)
    
    for i in tokens:
        print(i.token, " ", i.seq, " ", i.t_type)

    p = Parser()
    p.parse(tokens)

main()
