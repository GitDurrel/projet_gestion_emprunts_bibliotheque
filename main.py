from utilisateur import Utilisateur
from livres import Livre
from emprunt import Emprunt

def afficher_menu():
    print("\n=== Menu ===")
    print("1. Se connecter")
    print("2. S'inscrire")
    print("3. Quitter")

def afficher_menu_admin():
    print("\n=== Menu Administrateur ===")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Modifier un livre")
    print("4. Gérer les emprunts")
    print("5. Retour au menu principal")

def afficher_menu_utilisateur():
    print("\n=== Menu Utilisateur ===")
    print("1. Rechercher un livre")
    print("2. Emprunter un livre")
    print("3. Retourner un livre")
    print("4. Retour au menu principal")

def rechercher_livre(livres):
    try:
        titre = input("Entrez le titre du livre à rechercher : ")
        livres_trouves = [livre for livre in livres if titre.lower() in livre.titre.lower()]
        if livres_trouves:
            print("Livres trouvés :")
            for livre in livres_trouves:
                print(f"Titre : {livre.titre}, Auteur : {livre.auteur}, Genre : {livre.genre}")
        else:
            print("Aucun livre trouvé.")
    except Exception as e:
        print(f"Erreur lors de la recherche du livre : {e}")

def main():
    # Charger les utilisateurs depuis un fichier
    utilisateurs = Utilisateur.charger_utilisateurs("utilisateurs.txt")
    
    # Charger les livres depuis un fichier
    livres = Livre.charger_livres("livres.txt")
    
    # Charger les emprunts depuis un fichier
    emprunts = Emprunt.charger_emprunts()

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        try:
            if choix == "1":  # Se connecter
                nom = input("Entrez votre nom : ")
                mot_de_passe = input("Entrez votre mot de passe : ")

                utilisateur = Utilisateur.get_utilisateur(utilisateurs, nom, mot_de_passe)
                if utilisateur:
                    if utilisateur.role == "administrateur":
                        while True:
                            afficher_menu_admin()
                            choix_admin = input("Entrez votre choix : ")
                            if choix_admin == "1":
                                # Ajouter un livre
                                titre = input("Entrez le titre du livre : ")
                                auteur = input("Entrez l'auteur du livre : ")
                                genre = input("Entrez le genre du livre : ")
                                livre = Livre(titre, auteur, genre)
                                livres.append(livre)
                                print(f"Livre '{titre}' ajouté avec succès.")
                            elif choix_admin == "2":
                                # Supprimer un livre
                                titre = input("Entrez le titre du livre à supprimer : ")
                                livres = [livre for livre in livres if livre.titre != titre]
                                print(f"Livre '{titre}' supprimé (si existant).")
                            elif choix_admin == "3":
                                # Modifier un livre
                                titre = input("Entrez le titre du livre à modifier : ")
                                for livre in livres:
                                    if livre.titre == titre:
                                        livre.auteur = input(f"Entrez le nouvel auteur pour '{titre}' : ")
                                        livre.genre = input(f"Entrez le nouveau genre pour '{titre}' : ")
                                        print(f"Livre '{titre}' modifié avec succès.")
                                        break
                                else:
                                    print("Livre non trouvé.")
                            elif choix_admin == "4":
                                # Gérer les emprunts
                                print("Liste des emprunts :")
                                for emprunt in emprunts:
                                    print(f"Emprunt: Livre '{emprunt.livre.titre}' par {emprunt.utilisateur.nom}, Date emprunt: {emprunt.date_emprunt}, Date retour: {emprunt.date_retour}")
                            elif choix_admin == "5":
                                break
                            else:
                                print("Choix invalide.")
                    else:
                        while True:
                            afficher_menu_utilisateur()
                            choix_utilisateur = input("Entrez votre choix : ")
                            if choix_utilisateur == "1":
                                # Rechercher un livre
                                rechercher_livre(livres)
                            elif choix_utilisateur == "2":
                                # Emprunter un livre (ajouter un emprunt)
                                titre = input("Entrez le titre du livre à emprunter : ")
                                livre = next((livre for livre in livres if livre.titre == titre), None)
                                if livre and livre.disponible:
                                    livre.emprunter()  # Emprunter le livre
                                    date_emprunt = input("Entrez la date d'emprunt (jj/mm/aaaa) : ")
                                    date_retour = input("Entrez la date de retour (jj/mm/aaaa) : ")
                                    emprunt = Emprunt(livre, utilisateur, date_emprunt, date_retour)
                                    emprunts.append(emprunt)
                                else:
                                    print("Livre non disponible.")
                            elif choix_utilisateur == "3":
                                # Retourner un livre
                                titre = input("Entrez le titre du livre à retourner : ")
                                for emprunt in emprunts:
                                    if emprunt.livre.titre == titre:
                                        emprunt.livre.disponible = True
                                        emprunts.remove(emprunt)
                                        print(f"Livre '{titre}' retourné avec succès.")
                                        break
                                else:
                                    print(f"Aucun emprunt trouvé pour le livre '{titre}'.")
                            elif choix_utilisateur == "4":
                                break
                            else:
                                print("Choix invalide.")
                else:
                    print("Nom ou mot de passe incorrect.")
            elif choix == "2":  # Inscription
                nom = input("Entrez votre nom : ")
                mot_de_passe = input("Entrez votre mot de passe : ")
                utilisateur = Utilisateur(nom, mot_de_passe)
                utilisateurs.append(utilisateur)
                print("Inscription réussie.")
            elif choix == "3":  # Quitter
                print("Au revoir.")
                break
            else:
                print("Choix invalide.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()