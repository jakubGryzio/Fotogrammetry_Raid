class User:

    def __init__(self, *args):
        if len(args) > 0:
            self.GSD = args[0]
            self.p = args[1]
            self.q = args[2]
            self.Dx = args[3]
            self.Dy = args[4]
        else:
            self.GSD = 0
            self.p = 0
            self.q = 0
            self.Dx = 0
            self.Dy = 0
