#!/usr/bin/env python3
"""
===========================================================
events.py — Gestion des événements
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
🟨 LINK → diagram_events.drawio
"""

# ===================== IMPORTS =====================
from utils import (
    safe_input,
    color_text,
    valid_date_format,
    valid_time_format,
    is_time_slot_free,
)

# Stockage temporaire en mémoire
EVENTS = []


# ===================== MENU =====================
def menu():
    """
    🟢 OVALE → Début du menu événements
    🟥 RECTANGLE → Affiche le menu et gère la sélection
    🟨 LINK → diagram_events.drawio
    """
    while True:
        print("\n" + "=" * 40)
        print(color_text("GESTION DES ÉVÉNEMENTS", "cyan"))
        print("=" * 40)
        print("1. Créer un événement")
        print("2. Supprimer un événement")
        print("3. Lister les événements")
        print("Q. Retour au menu principal")
        print("=" * 40)

        choix = safe_input("Votre choix")

        # 🔷 LOSANGE → Sortie
        if choix is None or choix.upper() == "Q":
            break
        elif choix == "1":
            creer_evenement()
        elif choix == "2":
            supprimer_evenement()
        elif choix == "3":
            lister_evenements()
        else:
            print(color_text("[ERREUR] Choix invalide", "red"))

    # 🟢 OVALE → Fin
    print("Retour au menu principal...")


# ===================== FONCTIONS =====================
def creer_evenement():
    """
    🟥 RECTANGLE → Créer un événement
    🔷 LOSANGE → Validation date/heure
    🟪 CLOUD → Sauvegarde éventuelle via export.py
    """
    print("\n--- CREER UN EVENEMENT ---")
    titre = safe_input("Titre")
    date = safe_input("Date (AAAA-MM-JJ)")
    heure_debut = safe_input("Heure début (HH:MM)")
    heure_fin = safe_input("Heure fin (HH:MM)")
    salle = safe_input("Salle (optionnelle)")

    # Validation
    if not valid_date_format(date):
        print(color_text("[ERREUR] Format date invalide", "red"))
        return
    if not valid_time_format(heure_debut) or not valid_time_format(heure_fin):
        print(color_text("[ERREUR] Format heure invalide", "red"))
        return
    if not is_time_slot_free(date, heure_debut, heure_fin, salle, EVENTS):
        return

    evt_id = len(EVENTS) + 1
    EVENTS.append(
        {
            "id": evt_id,
            "title": titre,
            "date": date,
            "start": heure_debut,
            "end": heure_fin,
            "room": salle,
            "participants": [],
        }
    )
    print(color_text(f"✅ Événement '{titre}' ajouté avec ID {evt_id}", "green"))


def supprimer_evenement():
    """
    🟥 RECTANGLE → Supprimer un événement
    🟦 PARAL → Entrée ID événement
    """
    lister_evenements()
    evt_id = safe_input("ID de l'événement à supprimer")
    if not evt_id:
        return
    try:
        evt_id = int(evt_id)
    except ValueError:
        print(color_text("[ERREUR] ID invalide", "red"))
        return

    for e in EVENTS:
        if e["id"] == evt_id:
            EVENTS.remove(e)
            print(color_text(f"✅ Événement {evt_id} supprimé", "green"))
            return
    print(color_text("[ERREUR] Événement non trouvé", "red"))


def lister_evenements():
    """
    🟥 RECTANGLE → Lister tous les événements
    🟦 PARAL → Option filtre date
    """
    date_filtre = safe_input("Date (AAAA-MM-JJ) ou vide pour tous")
    print("\n--- LISTE DES EVENEMENTS ---")
    for e in EVENTS:
        if date_filtre and e["date"] != date_filtre:
            continue
        print(
            f"[{e['id']}] {e['title']} - {e['date']} {e['start']}-{e['end']} (Salle: {e['room']})"
        )
    print("-" * 40)
