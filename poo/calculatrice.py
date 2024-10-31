from abc import ABC, abstractmethod
import math
import time
from colorama import Fore, Style, init

# Initialiser colorama pour Windows
init(autoreset=True)

# Classe abstraite pour les opérations
class Operation(ABC):
    @abstractmethod
    def execute(self, x, y=None):
        pass

# Classe pour les opérations basiques
class BasicOperation(Operation):
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol

class Addition(BasicOperation):
    def __init__(self):
        super().__init__("Addition", "➕")

    def execute(self, x, y):
        return x + y

class Soustraction(BasicOperation):
    def __init__(self):
        super().__init__("Soustraction", "➖")

    def execute(self, x, y):
        return x - y

class Multiplication(BasicOperation):
    def __init__(self):
        super().__init__("Multiplication", "✖️")

    def execute(self, x, y):
        return x * y

class Division(BasicOperation):
    def __init__(self):
        super().__init__("Division", "➗")

    def execute(self, x, y):
        if y == 0:
            raise ValueError("Division par zéro non permise.")
        return x / y

# Classe pour les opérations avancées
class AdvancedOperation(Operation):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class Sinus(AdvancedOperation):
    def __init__(self):
        super().__init__("Sinus")

    def execute(self, x, y=None):
        return math.sin(math.radians(x))

class Cosinus(AdvancedOperation):
    def __init__(self):
        super().__init__("Cosinus")

    def execute(self, x, y=None):
        return math.cos(math.radians(x))

class Tangente(AdvancedOperation):
    def __init__(self):
        super().__init__("Tangente")

    def execute(self, x, y=None):
        return math.tan(math.radians(x))

class Logarithme(AdvancedOperation):
    def __init__(self):
        super().__init__("Logarithme")

    def execute(self, x, y=None):
        if x <= 0:
            raise ValueError("Logarithme indéfini pour x <= 0.")
        return math.log(x)

# Fonction utilitaire pour obtenir un nombre de l'utilisateur avec validation
def obtenir_nombre(message):
    while True:
        try:
            return float(input(Fore.LIGHTBLUE_EX + message))
        except ValueError:
            print(Fore.RED + "🚫 Entrée invalide ! Veuillez entrer un nombre. 🚫")

# Classe principale pour gérer la calculatrice
class Calculatrice:
    def __init__(self):
        self.operations = {
            "1": Addition(),
            "2": Soustraction(),
            "3": Multiplication(),
            "4": Division(),
            "5": Sinus(),
            "6": Cosinus(),
            "7": Tangente(),
            "8": Logarithme()
        }

    def afficher_menu(self):
        print(Fore.CYAN + "====== Calculatrice POO de 💻 DONALD PROGRAMMEUR 💻 ======")
        print(Fore.MAGENTA + """
    ██████╗░░█████╗░███╗░░██╗░█████╗░██╗░░░░░██████╗░  ██████╗░██████╗░░█████╗░███╗░░░███╗██╗███████╗██╗░░░░░
    ██╔══██╗██╔══██╗████╗░██║██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗████╗░████║██║██╔════╝██║░░░░░
    ██████╔╝██║░░██║██╔██╗██║██║░░██║██║░░░░░██║░░██║  ██████╔╝██████╔╝██║░░██║██╔████╔██║██║█████╗░░██║░░░░░
    ██╔═══╝░██║░░██║██║╚████║██║░░██║██║░░░░░██║░░██║  ██╔═══╝░██╔══██╗██║░░██║██║╚██╔╝██║██║██╔══╝░░██║░░░░░
    ██║░░░░░╚█████╔╝██║░╚███║╚█████╔╝███████╗██████╔╝  ██║░░░░░██║░░██║╚█████╔╝██║░╚═╝░██║██║███████╗███████╗
    ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░╚════╝░╚══════╝╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝╚══════╝╚══════╝

        """)
        for key, operation in self.operations.items():
            symbol = operation.get_symbol() if isinstance(operation, BasicOperation) else operation.get_name()
            print(Fore.YELLOW + f"{key}. {operation.get_name()} ({symbol})")
        print(Fore.CYAN + "========================================================")

    def choisir_operation(self):
        self.afficher_menu()
        choix = input(Fore.GREEN + "⚡ Choisissez une opération (1-8) ⚡: ")
        return self.operations.get(choix, None)

    def obtenir_valeurs(self, op):
        x = obtenir_nombre("🔢 Entrez le premier nombre : ")
        y = None
        if isinstance(op, BasicOperation):
            y = obtenir_nombre("🔢 Entrez le deuxième nombre : ")
        return x, y

    def calculer(self):
        operation = self.choisir_operation()
        if operation:
            x, y = self.obtenir_valeurs(operation)
            print(Fore.MAGENTA + "🔮 Calcul en cours...✨✨✨")
            time.sleep(1)  # Petit effet de "loading"
            try:
                resultat = operation.execute(x, y)
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"🎉 Résultat : {resultat} 🎉")
            except Exception as e:
                print(Fore.RED + f"💥 Erreur : {e} 💥")
        else:
            print(Fore.RED + "🚫 Opération invalide ! Veuillez choisir une option correcte. 🚫")

if __name__ == "__main__":
    calc = Calculatrice()
    continuer = "o"
    while continuer.lower() == "o":
        calc.calculer()
        continuer = input(Fore.LIGHTYELLOW_EX + "🔥 Voulez-vous effectuer un autre calcul ? (o/n) 🔥: ")
