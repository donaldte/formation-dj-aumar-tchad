"""
# Polymorphisme
- Polymorphisme signifie que les classes dérivées d'une même classe de base peuvent avoir des méthodes différentes.
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
        
    def show(self):
        return 'Employe'  
    
    def calculer_salaire(self, **kwargs):
        salaire = self.salaire
        for key, value in kwargs.items():
            print(f"{key}: {value}")
            salaire += value
        return salaire
    
    
            