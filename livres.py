
# GLORY

class Livre:
    def __init__(self, titre, auteur, genre, disponible=True):
        # code d'instanciation des attributs de l'objet livre
        self.titre = titre 
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible
    

    def emprunter(self):
        # Vérifie la disponibilite d'un livre . si il est disponible message pour confirmr l'emprunt sinon message pour dire que c'est pas dispo
        if self.disponible:
            self.disponible = False
            print(f"Le livre {self.titre} de {self.auteur} du genre {self.genre} a  ete emprunte avec succes.")
        else:
            print(f"L livre {self.titre} de {self.auteur}n'est pas dsiponible pour l'emprunt")
    
    def charger_livres(fichier="livres.txt"):
        # ouvre et lie le fichier livres.txt ligne par ligne et enregistre maintenant les informations dans une liste et retourne cette liste(prendre pour separateur la virgule)
        livres = []
        try:
            with open(fichier, 'r', encoding='utf-8')as file:
                for line in file:
                    titre,auteur,genre = line.strip().split(',')
                    livre = Livre(titre, auteur, genre)
                    livres.append(livre)
         
        except FileNotFoundError:
                print(f"le fichier {fichier} n'a pas ete trouve.")
        except Exception as e:
            print(f"une erreur {e} s'est produite")