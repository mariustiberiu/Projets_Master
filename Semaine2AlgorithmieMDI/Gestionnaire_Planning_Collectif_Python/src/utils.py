#!/usr/bin/env python3
"""
===========================================================
utils.py — Fonctions utilitaires pour Projet_Planning
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
🟨 LINK → diagram_principal.drawio (menu général)
🟨 LINK → diagram_events.drawio (gestion événements)
🟨 LINK → diagram_participants.drawio (participants / agenda)
🟨 LINK → diagram_rooms.drawio (salles / occupation)
🟨 LINK → diagram_export.drawio (export CSV/JSON/SQLite)
"""

# ================== IMPORTS ==================
import csv
import json
import sqlite3
from datetime import datetime


# ================== INPUT SÉCURISÉ ==================
def safe_input(prompt):
    """
    🟦 PARAL → Entrée utilisateur
    🟢 OVALE → Début fonction input sécurisé
    🟥 RECTANGLE → Lecture input
    🔷 LOSANGE → Quitter si Q/q
    """
    try:
        s = input(f"{prompt} : ").strip()
        if s.lower() == "q":
            return None
        if s == "Q":
            print("Fermeture du programme...")
            exit(0)
        return s
    except KeyboardInterrupt:
        print("\n[Fermeture]")
        exit(0)


# ================== COULEURS CLI ==================
def color_text(text, color):
    """
    🟥 RECTANGLE → Applique couleur ANSI au texte
    """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m",
    }
    return f"{colors.get(color,'')}{text}{colors['reset']}"


# ================== VALIDATION DATE / HEURE ==================
def valid_date_format(date_str):
    """
    🔷 LOSANGE → Vérifie format AAAA-MM-JJ
    🟥 RECTANGLE → Retourne True/False
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def valid_time_format(time_str):
    """
    🔷 LOSANGE → Vérifie format HH:MM
    🟥 RECTANGLE → Retourne True/False
    """
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def is_future_date(date_str):
    """
    🔷 LOSANGE → Vérifie que date >= aujourd'hui
    """
    d = datetime.strptime(date_str, "%Y-%m-%d").date()
    return d >= datetime.today().date()


def is_valid_time_range(start_str, end_str):
    """
    🔷 LOSANGE → Vérifie que fin > début
    """
    start = datetime.strptime(start_str, "%H:%M")
    end = datetime.strptime(end_str, "%H:%M")
    return end > start


def is_in_allowed_hours(start_str, end_str, start_limit="08:00", end_limit="20:00"):
    """
    🔷 LOSANGE → Vérifie horaires autorisés
    """
    start = datetime.strptime(start_str, "%H:%M")
    end = datetime.strptime(end_str, "%H:%M")
    s_lim = datetime.strptime(start_limit, "%H:%M")
    e_lim = datetime.strptime(end_limit, "%H:%M")
    if start < s_lim or end > e_lim:
        print(
            color_text(
                f"[ERREUR] Horaire autorisé : {start_limit} - {end_limit}", "red"
            )
        )
        return False
    return True


# ================== CONVERSION / CHEVAUCHEMENTS ==================
def time_to_dt(date_s, time_s):
    """
    🟥 RECTANGLE → Convertit date+heure en datetime
    🟪 CLOUD → Utilisé pour overlaps / planning
    """
    return datetime.strptime(f"{date_s} {time_s}", "%Y-%m-%d %H:%M")


def overlaps_dt(s1, e1, s2, e2):
    """
    🔷 LOSANGE → Vérifie si deux intervalles se chevauchent
    🟥 RECTANGLE → Retourne True/False
    """
    return max(s1, s2) < min(e1, e2)


# ================== CRÉNEAU / SALLE ==================
def is_time_slot_free(date_s, start_s, end_s, salle="", events=None, ignore_id=None):
    """
    🔷 LOSANGE → Vérifie disponibilité créneau pour tous événements
    🟪 CLOUD → peut ignorer un événement (ignore_id)
    🟢 OVALE → Début fonction
    """
    if events is None:
        return True
    start_dt = time_to_dt(date_s, start_s)
    end_dt = time_to_dt(date_s, end_s)
    for e in events:
        if ignore_id and e.get("id") == ignore_id:
            continue
        if e["date"] != date_s:
            continue
        ev_start = time_to_dt(e["date"], e["start"])
        ev_end = time_to_dt(e["date"], e["end"])
        if overlaps_dt(start_dt, end_dt, ev_start, ev_end):
            if salle and e.get("room") != salle:
                continue
            print(
                color_text(
                    f"[ERREUR] Conflit avec événement [{e['id']}] {e['title']} ({e['start']}-{e['end']})",
                    "red",
                )
            )
            return False
    return True


def is_room_available(date_s, start_s, end_s, salle, events=None, ignore_id=None):
    """
    🔷 LOSANGE → Vérifie si salle disponible
    🟥 RECTANGLE → Appelle is_time_slot_free
    """
    return is_time_slot_free(date_s, start_s, end_s, salle, events, ignore_id)


# ================== EXPORT / LOGS ==================
# 🟡 OVALE : Fonction -> charger JSON
def load_json(file_path):
    """
    Charge un fichier JSON et retourne les données.
    OVALE dans diagram_export : 'Load JSON'
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERREUR] Impossible de charger {file_path} : {e}")
        return []


# 🟡 OVALE : Fonction -> sauvegarder JSON
def save_json(file_path, data):
    """
    Sauvegarde des données dans un fichier JSON.
    OVALE dans diagram_export : 'Save JSON'
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERREUR] Impossible de sauvegarder {file_path} : {e}")


# 🟡 OVALE : Fonction -> export CSV
def export_csv(file_path, data, fieldnames):
    """
    Exporte une liste de dictionnaires dans un CSV.
    OVALE : 'Export CSV'
    """
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"[ERREUR] Export CSV échoué : {e}")


# 🟡 OVALE : Fonction -> export JSON
def export_json(file_path, data):
    """
    Exporte des données dans un JSON.
    OVALE : 'Export JSON'
    """
    save_json(file_path, data)


# 🟡 OVALE : Fonction -> connexion SQLite
def connect_sqlite(db_name="database.db"):
    """
    Crée ou ouvre une base SQLite.
    Rectangle dans diagram_export : 'SQLite Database'
    """
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"[ERREUR] Connexion SQLite : {e}")
        return None


# 🟡 OVALE : Fonction -> logs
def log_event(message):
    """
    Écrit un message de log horodaté.
    OVALE : 'Logger'
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
