from regex_lex_tokens import *
from if_stmt import *

class Parser(object):
    def __init__(self):
        tokens = list()
        pos = 0
        tree = None

    def parse(self, tokens):
        if tokens[0].seq == "func":
            self.parse_func(tokens)


        if tokens[0].seq == "if":
            if_stmt = self.parse_if(tokens)
            print(if_stmt)
            return if_stmt

    def parse_func(self, tokens):
        level = 0

    def parse_if(self, tokens):
        # Assuming starting on if-token
        if_test = list()
        true_body = list()
        false_body = list()

        # Collect if_test
        if tokens[1].seq == "(":
            tokens = tokens[2:]
            while len(tokens) > 0:
                token = tokens[0]
                if token.seq == ")":
                    tokens = tokens[1:]
                    break
                if_test.append(token)
                # Convert tokens into statement
                if_test = self.parse(if_test)
                tokens = tokens[1:]

            # Collect true-body
            if tokens[0].seq == "{":
                tokens = tokens[1:]
                curr_stmt = list()
                while len(tokens) > 0:
                    token = tokens[0]
                    if token.seq == "}":
                        tokens = tokens[1:]
                        break
                    if token.seq == ";":
                        # Convert tokens to statement
                        curr_stmt = self.parse(curr_stmt)
                        true_body.append(curr_stmt)
                        curr_stmt = list()
                    curr_stmt.append(token)
                    tokens = tokens[1:]

            # Collect false-body
            if len(tokens) > 0 and tokens[0].seq == "else":
                tokens = tokens[1:]
                if tokens[0].seq == "{":
                    tokens = tokens[1:]
                    curr_stmt = list()
                    while len(tokens) > 0:
                        token = tokens[0]
                        if token.seq == "}":
                            tokens = tokens[1:]
                            break
                        if token.seq == ";":
                            # Convert tokens to statement
                            curr_stmt = self.parse(curr_stmt)
                            false_body.append(curr_stmt)
                            curr_stmt = list()
                        curr_stmt.append(token)
                        tokens = tokens[1:]

            return tokens, IfStmt(if_test, true_body, false_body)




