import re


# Tokens: IF ELSE WHILE INT RETURN LE LT GT GE EQ NE VOID
class TokenInfo(object):
    def __init__(self, pattern, token, t_type):
        self.pattern = pattern
        self.token = token
        self.tok_type = t_type

class Token(object):
    def __init__(self, token, sequence, t_type):
        self.token = token
        self.seq = sequence
        self.t_type = t_type

class Lexer(object):
    def __init__(self):
        self.tokenInfos = list()
        self.tokens = list()

    def add(self, regex, token, t):
        self.tokenInfos.append(TokenInfo(re.compile("^("+regex+")"), token, t))

    def lex(self, string):
        col = 0
        lineno = 0

        s = string.strip()
        del self.tokens[:]
        while s != "":
            match = False
            for info in self.tokenInfos:
                m = re.search(info.pattern, s)
                if m is not None:
                    match = True
                    tok = m.group(0).strip()
                    s = s.replace(m.group(0), "", 1).strip()
                    self.tokens.append(Token(info.token, tok, info.tok_type))
                    break
            if not match:
                print("Unexpected Character!\n", s[0], "at col: ", col, " and line: ", lineno)
                exit(-1)
        return self.tokens
