class Etudiant :
    def __init__(self,nm,ag,nt):
        self.__name=nm
        self.__note=nt
        self.__age=ag
    
    def getNote (self):
        return self.__note
    def setNote (self , note):
        self.__note= note
    def getName (self):
        return self.__name
    def setName (self , note):
        self.__name = name
    def getAge(self):
        return self.__age
    def setAge (self , note):
        self.__age= age


etd1 = Etudiant("asmae",16 ,14)
etd1.setAge(17)
print(etd1.getAge())


        
       