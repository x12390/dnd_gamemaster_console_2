class armor:
    def __init__(self):
        self.rk = 0
        self.category = ""
        self.type = type
        self.rk = 0
        self.max = 0

    def add_type(self, name):
        if name == "Leder":
            self.rk = 11
            self.category = 1 #leicht
        elif name == "Beschlagenes Leder":
            self.rk = 12
            self.category = 1 #leicht
        elif name =="Fell":
            self.rk = 12
            self.category = 2 #mittelschwer
        elif name =="Kettenhemd":
            self.rk = 13
            self.category = 2 #mittelschwer
        elif name =="Schuppenpanzer":
            self.rk = 14
            self.category = 2 #mittelschwer
        elif name =="Brustplatte":
            self.rk = 14
            self.category = 2 #mittelschwer
        elif name =="Plattenpanzer":
            self.rk = 15
            self.category = 2 #mittelschwer
        elif name =="Ringpanzer":
            self.rk = 14
            self.category = 3 #schwer
        elif name =="Kettenpanzer":
            self.rk = 16
            self.category = 3 #schwer
        elif name =="Schienenpanzer":
            self.rk = 17
            self.category = 3 #schwer
        elif name =="Ritterrüstung":
            self.rk = 18
            self.category = 3 #schwer
        elif name == "Schild":
            self.rk = 2 #additional rk +2
            self.category = 4 #Schild

