#!/usr/bin/env python3
"""
===========================================================
main.py — Point d’entrée du Gestionnaire de Planning
===========================================================

🔗 LIENS UML (liaison avec tes diagrams drawio)
-------------------------------------
🟥 RECTANGLE  = Action
🟦 PARAL      = Entrée / sortie
🔷 LOSANGE    = Condition
🟢 OVALE      = Début / fin
🟪 CLOUD      = Appel vers module externe
🟨 LINK       = Référence à un diagramme drawio
-------------------------------------

🟨 LINK → diagram_principal.drawio (MENU général)
🟨 LINK → diagram_events.drawio (événements)
🟨 LINK → diagram_participants.drawio
🟨 LINK → diagram_rooms.drawio
🟨 LINK → diagram_export.drawio
"""

# ===================== IMPORTS SÉCURISÉS =====================
try:
    # 🟪 CLOUD → utils
    from utils import safe_input, color_text
except Exception:
    print("Erreur import utils — vérifiez l’arborescence.")
    exit(1)

# 🟪 CLOUD → modules externes (créés après)
try:
    import events
    import participants
    import rooms
    import export
except Exception:
    print("⚠️ Modules incomplets — en cours de construction UML")
    # Pas de exit pour permettre développement


# ============================================================
# 🟥 RECTANGLE → AFFICHAGE MENU PRINCIPAL
# ============================================================
def afficher_menu():
    print("\n" + "=" * 50)
    print(color_text("GESTIONNAIRE DE PLANNING COLLECTIF", "cyan"))
    print("=" * 50)
    print("1. Gestion des événements")
    print("2. Gestion des participants")
    print("3. Gestion des salles")
    print("4. Export / Sauvegarde")
    print("Q. Quitter")
    print("=" * 50)


# ============================================================
# 🟥 RECTANGLE → BOUCLE PRINCIPALE
# 🟨 LINK → diagram_principal.drawio
# ============================================================
def main():
    # 🟢 OVALE → Début
    while True:

        afficher_menu()

        # 🟦 PARAL → Lecture choix
        choix = safe_input("Votre choix")

        # 🔷 LOSANGE → Test sortie
        if choix is None or choix.upper() == "Q":
            print("Fermeture du programme…")
            break

        # ====================================================
        # 🔷 LOSANGE → Menu événements
        # 🟪 CLOUD → events.menu()
        # 🟨 LINK → diagram_events.drawio
        # ====================================================
        if choix == "1":
            if hasattr(events, "menu"):
                events.menu()
            else:
                print(color_text("[ERREUR] Module events incomplet", "red"))

        # ====================================================
        # 🔷 LOSANGE → Menu participants
        # 🟪 CLOUD → participants.menu()
        # 🟨 LINK → diagram_participants.drawio
        # ====================================================
        elif choix == "2":
            if hasattr(participants, "menu"):
                participants.menu()
            else:
                print(color_text("[ERREUR] Module participants incomplet", "red"))

        # ====================================================
        # 🔷 LOSANGE → Menu salles
        # 🟪 CLOUD → rooms.menu()
        # 🟨 LINK → diagram_rooms.drawio
        # ====================================================
        elif choix == "3":
            if hasattr(rooms, "menu"):
                rooms.menu()
            else:
                print(color_text("[ERREUR] Module rooms incomplet", "red"))

        # ====================================================
        # 🔷 LOSANGE → Menu export
        # 🟪 CLOUD → export.menu()
        # 🟨 LINK → diagram_export.drawio
        # ====================================================
        elif choix == "4":
            if hasattr(export, "menu"):
                export.menu()
            else:
                print(color_text("[ERREUR] Module export incomplet", "red"))

        # ====================================================
        # 🔷 LOSANGE → Choix invalide
        # ====================================================
        else:
            print(color_text("[ERREUR] Choix invalide.", "red"))

    # 🟢 OVALE → Fin
    print("À bientôt !")


# ============================================================
# 🟥 RECTANGLE → Exécution directe
# ============================================================
if __name__ == "__main__":
    main()
