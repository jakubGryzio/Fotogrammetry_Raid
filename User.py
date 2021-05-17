class User:

    def __init__(self, *args):
        if len(args) > 0:
            self.GSD = args[0]
            self.p = args[1]
            self.q = args[2]
            self.Dx = args[3]
            self.Dy = args[4]
        else:
            self.GSD = 0.25
            self.p = 60
            self.q = 30
            self.Dx = 19090
            self.Dy = 17219
