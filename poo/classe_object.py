"""
Les type de programmation 
1. La programmation procédurale: 
    definition: La programmation procédurale est un paradigme de programmation 
    qui consiste à diviser un programme en une suite de procédures ou fonctions.
2. La programmation orientée objet:
    definition: La programmation orientée objet (POO) est un paradigme de programmation 
    qui consiste à organiser un programme autour d'objets qui représentent des instances de classes.
3. La programmation fonctionnelle:
    definition: La programmation fonctionnelle est un paradigme de programmation 
    qui consiste à traiter les fonctions comme des objets de première classe.
4. La programmation impérative:
    definition: La programmation impérative est un paradigme de programmation 
    qui consiste à décrire les étapes d'un programme en termes d'instructions.
5. La programmation logique:
    definition: La programmation logique est un paradigme de programmation 
    qui consiste à décrire les relations entre les données d'un programme.
6. La programmation événementielle:
    definition: La programmation événementielle est un paradigme de programmation 
    qui consiste à traiter les événements comme des objets de première classe.
"""

## La programmation orientée objet


# Les classes en python

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
        
        
personne_1 = Personne("Doe", "John", 30)
personne_1.afficher()
personne_1.changer_nom("Smith")
personne_1.afficher()        