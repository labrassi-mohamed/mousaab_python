class Utudiant :
    def __unit__(self,name,myAge,myNote):
        self.nom =name
        self.age =myAge
        self.note = myNote
    def ajouterNote (self , points):
        print(self.note + points)

etd1 = Utudiant("hesan" , 16 ,14)
print(etd1.age)
etd1.ajouterNote(2)