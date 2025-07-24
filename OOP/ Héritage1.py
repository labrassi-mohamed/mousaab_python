class Person ():
    def __init__(self , nm , ag):
        self.name = nm
        self.age = ag

class Etudiant (Person):
    def __init__(self , nm,ag,nt):
        Person.__init__(self , name,age )
        setf.note = nt
class Professeur (Person):
    def __init__(self , nm,ag,sal):
        Person.__init__(self , name,age )
        setf.salaire = sal

etd1 = Etudiant("Asmae",17 ,14)
print(etd1.name)
prof1 = Professeur("Mohemed" , 25 , 50000)
print(prof1.name)



        