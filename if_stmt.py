
class IfStmt(object):
    def __init__(self, test, true, false):
        self.test = test
        self.true = true
        self.false = false

    def __str__(self):
        s = "IF\n   "
        for i in self.test:
            s += i.seq
            s += " "
        s += "\nTHEN\n  "
        for i in self.true:
            for j in i:
                s += j.seq
                s += " "
            s += "\n    "
        s = s.strip()
        s += "\nELSE\n  "
        if self.false:
            for i in self.false:
                for j in i:
                    s += j.seq
                    s += " "
                s += "\n    "
            s = s.strip()
        return s

    def __repr__(self):
        return self.__str__()


