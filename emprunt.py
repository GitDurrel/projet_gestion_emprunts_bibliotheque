from utilisateur import Utilisateur
from livres import Livre
# THIERRY

class Emprunt():
    def __init__(self,livre,utilisateur,date_emprunt,date_retour):
        # code d'instanciation des atrabuts de l'objet emprunt
        # livre ici rclass Emprunt():
    #  def __init__(self, livre, utilisateur, date_emprunt, date_retour):
        # Initialisation des attributs de l'objet emprunt
        self.livre = livre            # Objet de la classe Livre
        self.utilisateur = utilisateur # Objet de la classe Utilisateur
        self.date_emprunt = date_emprunt  # Date d'emprunt (sous forme de chaîne ou d'objet date)
        self.date_retour = date_retour  # Date de retour (sous forme de chaîne ou d'objet date)
    
    @staticmethod
    def charger_emprunts():
        # Ouvre et lit le fichier "livres.txt", enregistre chaque ligne dans une liste
        # et retourne la liste des emprunts. Chaque ligne est séparée par une virgule.
        
        emprunts = []
        
        try:
            with open('livres.txt', 'r') as fichier:
                for ligne in fichier:
                    # Supposons que chaque ligne a le format : 
                    # livre, utilisateur, date_emprunt, date_retour
                    donnees = ligne.strip().split(',')
                    
                    if len(donnees) == 4:
                        # Pour créer un emprunt, il faut des objets Livre et Utilisateur.
                        # Ici, on suppose que nous avons des classes Livre et Utilisateur
                        # qui peuvent être instanciées avec les informations de la ligne.
                        
                        livre = Livre(donnees[0])  # Exemple d'instanciation d'un objet Livre
                        utilisateur = Utilisateur(donnees[1])  # Exemple d'instanciation d'un objet Utilisateur
                        date_emprunt = donnees[2]  # Vous pouvez aussi convertir cette valeur en un objet date si nécessaire
                        date_retour = donnees[3]  # Idem pour la date de retour
                        
                        emprunt = Emprunt(livre, utilisateur, date_emprunt, date_retour)
                        emprunts.append(emprunt)
        except FileNotFoundError:
            print("Le fichier 'livres.txt' n'a pas été trouvé.")
        
        return emprunts


        
    


