class Savasci:
    def __init__(self, kaynak, can, hasar, yataym, dikeym, caprazm):
        self.kaynak = kaynak
        self.can = can
        self.hasar = hasar
        self.yataym = yataym
        self.dikeym = dikeym
        self.caprazm = caprazm

class Okcu(Savasci):
    def __init__(self):
        super().__init__(20, 30, 0.6, 2, 2, 2)
        self.isim = "Okçu"

class Topcu(Savasci):
    def __init__(self):
        super().__init__(50, 30, -1, 2, 2, 0)
        self.isim = "Topçu"

class Atli(Savasci):
    def __init__(self):
        super().__init__(30, 40, 30, 0, 0, 3)
        self.isim = "Atlı"

class Muhafiz(Savasci):
    def __init__(self):
        super().__init__(10, 80, 20, 1, 1, 1)
        self.isim = "Muhafız"

class Saglikci(Savasci):
    def __init__(self):
        super().__init__(10, 100, 0.5, 2, 2, 2)
  
        self.isim = "Sağlıkçı"