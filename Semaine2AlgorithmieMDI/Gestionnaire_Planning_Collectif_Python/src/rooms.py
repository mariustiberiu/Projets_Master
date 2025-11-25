#!/usr/bin/env python3
"""
===========================================================
rooms.py — Gestion des salles et occupation
===========================================================

🔗 LIENS UML
-------------------------------------
🟥 RECTANGLE  = Action / Processus
🟦 PARAL      = Entrée / sortie
🔷 LOSANGE    = Condition
🟢 OVALE      = Début / fin
🟪 CLOUD      = Appel vers module externe
🟨 LINK       = Référence diagram drawio
-------------------------------------
🟨 LINK → diagram_rooms.drawio
"""

# ===================== IMPORTS =====================
try:
    from utils import safe_input, color_text, is_room_available
except Exception:
    print(color_text("[ERREUR] utils.py manquant pour rooms.py", "red"))
    # Pas d'exit pour permettre développement


# ===================== MENU SALLES =====================
def menu():
    """
    🟢 OVALE → Début menu salles
    🟥 RECTANGLE → Affiche menu salles et gère choix
    🟨 LINK → diagram_rooms.drawio
    """
    while True:
        print("\n" + "=" * 40)
        print(color_text("GESTION DES SALLES", "cyan"))
        print("=" * 40)
        print("1. Ajouter une salle")
        print("2. Supprimer une salle")
        print("3. Lister les salles")
        print("4. Vérifier disponibilité")
        print("Q. Retour au menu principal")
        print("=" * 40)

        choix = safe_input("Votre choix")

        # 🔷 LOSANGE → Sortie
        if choix is None or choix.upper() == "Q":
            break
        elif choix == "1":
            ajouter_salle()
        elif choix == "2":
            supprimer_salle()
        elif choix == "3":
            lister_salles()
        elif choix == "4":
            verifier_disponibilite()
        else:
            print(color_text("[ERREUR] Choix invalide", "red"))

    # 🟢 OVALE → Fin menu
    print("Retour au menu principal...")


# ===================== FONCTIONS TODO =====================
def ajouter_salle():
    """
    🟥 RECTANGLE → Ajouter une salle
    🟦 PARAL → Entrée nom / capacité
    🟪 CLOUD → Mise à jour stockage (JSON/SQLite)
    """
    # TODO : Implémenter ajout de salle
    print(color_text("[TODO] ajouter_salle à implémenter", "yellow"))


def supprimer_salle():
    """
    🟥 RECTANGLE → Supprimer une salle
    🟦 PARAL → Entrée ID salle
    🟪 CLOUD → Suppression du stockage
    """
    # TODO : Implémenter suppression de salle
    print(color_text("[TODO] supprimer_salle à implémenter", "yellow"))


def lister_salles():
    """
    🟥 RECTANGLE → Lister toutes les salles
    🟪 CLOUD → Lecture stockage (JSON/SQLite)
    """
    # TODO : Implémenter affichage des salles
    print(color_text("[TODO] lister_salles à implémenter", "yellow"))


def verifier_disponibilite():
    """
    🟥 RECTANGLE → Vérifier si salle disponible
    🔷 LOSANGE → Validation créneau
    🟪 CLOUD → Appel à utils.is_room_available
    """
    # TODO : Implémenter vérification de disponibilité
    print(color_text("[TODO] verifier_disponibilite à implémenter", "yellow"))
