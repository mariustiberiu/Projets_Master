#!/usr/bin/env python3
"""
===========================================================
export.py — Export CSV / JSON / SQLite
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
🟨 LINK → diagram_export.drawio
"""

# ===================== IMPORTS =====================
try:
    from utils import safe_input, color_text, export_csv, export_json, connect_sqlite
except Exception:
    print(color_text("[ERREUR] utils.py manquant pour export.py", "red"))
    # Pas d'exit pour permettre développement


# ===================== MENU EXPORT =====================
def menu():
    """
    🟢 OVALE → Début menu export
    🟥 RECTANGLE → Affiche menu export et gère choix
    🟨 LINK → diagram_export.drawio
    """
    while True:
        print("\n" + "=" * 40)
        print(color_text("EXPORT / SAUVEGARDE", "cyan"))
        print("=" * 40)
        print("1. Export CSV")
        print("2. Sauvegarde JSON")
        print("3. Sauvegarde SQLite")
        print("Q. Retour au menu principal")
        print("=" * 40)

        choix = safe_input("Votre choix")

        # 🔷 LOSANGE → Sortie
        if choix is None or choix.upper() == "Q":
            break
        elif choix == "1":
            export_csv_action()
        elif choix == "2":
            sauvegarder_json_action()
        elif choix == "3":
            sauvegarder_sqlite_action()
        else:
            print(color_text("[ERREUR] Choix invalide", "red"))

    # 🟢 OVALE → Fin menu
    print("Retour au menu principal...")


# ===================== FONCTIONS TODO =====================
def export_csv_action():
    """
    🟥 RECTANGLE → Export CSV
    🟪 CLOUD → Utilise utils.export_csv
    """
    # TODO : Implémenter export CSV réel
    print(color_text("[TODO] Export CSV à implémenter", "yellow"))


def sauvegarder_json_action():
    """
    🟥 RECTANGLE → Sauvegarde JSON
    🟪 CLOUD → Utilise utils.export_json
    """
    # TODO : Implémenter sauvegarde JSON réelle
    print(color_text("[TODO] Sauvegarde JSON à implémenter", "yellow"))


def sauvegarder_sqlite_action():
    """
    🟥 RECTANGLE → Sauvegarde SQLite
    🟪 CLOUD → Utilise utils.connect_sqlite et logique stockage
    """
    # TODO : Implémenter sauvegarde SQLite réelle
    print(color_text("[TODO] Sauvegarde SQLite à implémenter", "yellow"))
