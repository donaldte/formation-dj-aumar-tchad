"""
# Heritage
type d'heritage
1. Heritage simple
2. Heritage multiple
3. Heritage multilevel
"""

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Age: {self.age}")
        
    def changer_nom(self, nom):
        self.nom = nom
        
    def changer_prenom(self, prenom):
        self.prenom = prenom
        
        
    def show(self):
        return 'Personne'


class Employe(Personne):
    def __init__(self, nom, prenom, age, salaire):
        super().__init__(nom, prenom, age)
        self.salaire = salaire
        
    def afficher(self):
        super().afficher()
        print(f"Salaire: {self.salaire}")
        
    def changer_salaire(self, salaire):
        self.salaire = salaire
        
        
    def show_1(self):
        print(self.show())
        return 'Employe'
        

class Chef(Employe):
    def __init__(self, nom, prenom, age, salaire, service):
        super().__init__(nom, prenom, age, salaire)
        self.service = service
        
    def afficher(self):
        super().afficher()
        print(f"Service: {self.service}")
        
    def changer_service(self, service):
        self.service = service

chef = Chef("Doe", "John", 30, 3000, "Informatique")
print(chef.show_1() )       
        
class Directeur(Chef):
    def __init__(self, nom, prenom, age, salaire, service, societe):
        super().__init__(nom, prenom, age, salaire, service)
        self.societe = societe
        
    def afficher(self):
        super().afficher()
        print(f"Société: {self.societe}")
        
    def changer_societe(self, societe):
        self.societe = societe
        
        
# multiple inheritance
class A:
    def __init__(self):
        print("A")
        
class B:
    def __init__(self):
        print("B")
        
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C")
        
c = C()                        
