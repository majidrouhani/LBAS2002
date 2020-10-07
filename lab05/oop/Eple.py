
class Eple:
    def __init__(self,farge,vekt,importert):
        self.farge = farge
        self.vekt = vekt
        self.importert = importert

    def get_farge(self):
        return self.farge

    def get_vekt(self):
        return self.vekt

    def get_importert(self):
        return self.importert


    def to_string(self):
        return self.farge+", "+str(self.vekt)+", "+ self.importert
