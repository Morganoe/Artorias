R_BUILT_IN = "out|in"
R_L_PAREN = "\\("
R_R_PAREN = "\\)"
R_ADDOP = "[+-]"
R_MULOP = "[*/]"
R_POWOP = "\\^"
R_RELOP = "<|>|=>|=<|==|!="
R_NUMBER = "[0-9]+"
R_VAR = "[a-zA-Z][a-zA-Z0-9_]*"
R_L_CURL = "\\{"
R_R_CURL = "\\}"
R_DELIM = ";"
R_FUNC_RET = "->"

regexes = \
    [
        (R_BUILT_IN, 0, "built-ins"),
        (R_FUNC_RET, 12, "func_ret"),
        (R_L_PAREN, 1, "l_paren"),
        (R_R_PAREN, 2, "r_paren"),
        (R_ADDOP, 3, "addop"),
        (R_MULOP, 4, "mulop"),
        (R_POWOP, 5, "powop"),
        (R_RELOP, 6, "relop"),
        (R_NUMBER, 7, "number"),
        (R_VAR, 8, "var"),
        (R_L_CURL, 9, "l_curl"),
        (R_R_CURL, 10, "r_curl"),
        (R_DELIM, 11, "delim")
    ]
