class ani():
    def __init__(self,eye,feet):
        self.eye = eye
        self.feet = feet

    def goster(self):
        print("""
        
        Eye : {} 

        Feet   : {}

        """.format(self.eye,self.feet))

class kucu(ani):
    def __init__(self,eye,feet,bark):
        super().__init__(eye,feet)
        self.bark = bark

        print("""
        
        Eye : {} 

        Feet   : {}

        Bark : {}

        """.format(self.eye,self.feet,self.bark))


class birb(ani):
    def __init__(self,eye,feet,wing):
        super().__init__(eye,feet)
        self.wing = wing

class hrs(ani):
    def __init__(self,eye,feet,size):
        super().__init__(eye,feet)
        self.size = size

animal = ani(2,2)

animal.goster()

kopek = kucu(2,4, "Gürültülü")

bird = birb(2,2,2)

horse = hrs(2,2,"Small")