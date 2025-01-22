class Utilisateur:
    def __init__(self, nom, mot_de_passe, role="utilisateur"):
        self.nom = nom
        self.mot_de_passe = mot_de_passe
        self.role = role  # Rôle de l'utilisateur, par défaut "utilisateur"
    
    @staticmethod
    def get_utilisateur(utilisateurs, nom, mot_de_passe):
        """Retourne un utilisateur correspondant à l'identifiant et mot de passe."""
        for utilisateur in utilisateurs:
            if utilisateur.nom == nom and utilisateur.mot_de_passe == mot_de_passe:
                return utilisateur
        return None  

    @staticmethod
    def charger_utilisateurs(fichier):
        """Charge les utilisateurs depuis un fichier texte."""
        utilisateurs = []
        try:
            with open(fichier, 'r') as f:
                for ligne in f:

                    ligne = ligne.strip()

                    if ligne:
                        nom, mot_de_passe, role = ligne.split(',')
                        utilisateur = Utilisateur(nom, mot_de_passe, role)
                        utilisateurs.append(utilisateur)
        except FileNotFoundError:
            print(f"Le fichier {fichier} est introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement des utilisateurs: {e}")
        return utilisateurs