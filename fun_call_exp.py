
class FunCallExp(object):
    def __init__(self, name, args):
        self.fun_name = name
        self.args = args

    def __str__(self):
        s = "CALLING:  " + self.fun_name + "\n"
        for i in self.args:
            s += "  " + i.seq + "\n"
        return s

    def __repr__(self):
        return self.__str__()
