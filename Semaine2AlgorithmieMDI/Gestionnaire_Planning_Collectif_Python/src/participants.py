#!/usr/bin/env python3
"""
===========================================================
participants.py — Gestion des participants et agenda
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
🟨 LINK → diagram_participants.drawio
"""

# ===================== IMPORTS =====================
from utils import safe_input, color_text

# Stockage temporaire en mémoire
PARTICIPANTS = []


# ===================== MENU =====================
def menu():
    """
    🟢 OVALE → Début menu participants
    🟥 RECTANGLE → Affiche menu et gère choix
    🟨 LINK → diagram_participants.drawio
    """
    while True:
        print("\n" + "=" * 40)
        print(color_text("GESTION DES PARTICIPANTS", "cyan"))
        print("=" * 40)
        print("1. Ajouter participant")
        print("2. Retirer participant")
        print("3. Afficher agenda participant")
        print("Q. Retour au menu principal")
        print("=" * 40)

        choix = safe_input("Votre choix")

        # 🔷 LOSANGE → Sortie
        if choix is None or choix.upper() == "Q":
            break
        elif choix == "1":
            ajouter_participant()
        elif choix == "2":
            retirer_participant()
        elif choix == "3":
            afficher_agenda()
        else:
            print(color_text("[ERREUR] Choix invalide", "red"))

    # 🟢 OVALE → Fin menu
    print("Retour au menu principal...")


# ===================== FONCTIONS =====================
def ajouter_participant():
    """
    🟥 RECTANGLE → Ajouter un participant
    🟦 PARAL → Entrée nom
    """
    nom = safe_input("Nom du participant")
    if nom:
        PARTICIPANTS.append({"name": nom, "agenda": []})
        print(color_text(f"✅ Participant {nom} ajouté", "green"))


def retirer_participant():
    """
    🟥 RECTANGLE → Retirer un participant
    🟦 PARAL → Entrée nom
    """
    nom = safe_input("Nom du participant à retirer")
    if not nom:
        return
    for p in PARTICIPANTS:
        if p["name"] == nom:
            PARTICIPANTS.remove(p)
            print(color_text(f"✅ Participant {nom} retiré", "green"))
            return
    print(color_text("[ERREUR] Participant non trouvé", "red"))


def afficher_agenda():
    """
    🟥 RECTANGLE → Afficher l'agenda d'un participant
    🟦 PARAL → Entrée nom
    """
    nom = safe_input("Nom du participant")
    for p in PARTICIPANTS:
        if p["name"] == nom:
            print(f"\n--- Agenda de {nom} ---")
            if not p["agenda"]:
                print("(Vide)")
            else:
                for evt in p["agenda"]:
                    print(f"{evt}")
            print("-" * 40)
            return
    print(color_text("[ERREUR] Participant non trouvé", "red"))
