class Etudiant:
    def __init__(self,nm,ag,nt):
        self.__name=nm
        self.age =ag
        self.note =nt
    def getName (self):
        return self.__name
etd1 = Etudiant("aymen",29 , 18)
print(etd1.getName())
        