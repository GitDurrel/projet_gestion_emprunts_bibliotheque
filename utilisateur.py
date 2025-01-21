class Utilisateur:
    def __init__(self, nom, prenom, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.emprunts = []  # Liste pour stocker les emprunts de l'utilisateur

    def emprunter(self, livre):
        """Ajoute un livre à la liste des emprunts de l'utilisateur."""
        if livre not in self.emprunts:
            self.emprunts.append(livre)
            print(f"{self.prenom} {self.nom} a emprunté le livre: {livre}")
        else:
            print(f"{self.prenom} {self.nom} a déjà emprunté ce livre.")

    def rendre(self, livre):
        """Retire un livre de la liste des emprunts de l'utilisateur."""
        if livre in self.emprunts:
            self.emprunts.remove(livre)
            print(f"{self.prenom} {self.nom} a rendu le livre: {livre}")
        else:
            print(f"{self.prenom} {self.nom} n'a pas emprunté ce livre.")

    def afficher_emprunts(self):
        """Affiche tous les emprunts de l'utilisateur."""
        if self.emprunts:
            print(f"Emprunts de {self.prenom} {self.nom}: {', '.join(self.emprunts)}")
        else:
            print(f"{self.prenom} {self.nom} n'a pas d'emprunts.")

# Exemple d'utilisation
if __name__ == "__main__":
    utilisateur1 = Utilisateur("roland", "lonts", "001")
    utilisateur1.emprunter("Le Petit Prince")
    utilisateur1.afficher_emprunts()
    utilisateur1.rendre("Le Petit Prince")
    utilisateur1.afficher_emprunts()