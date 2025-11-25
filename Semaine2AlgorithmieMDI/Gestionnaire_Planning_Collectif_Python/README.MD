# Projet_Master

Ce dépôt contient deux parties principales :  
1. La matière de la semaine 2 d’**Algorithmie MDI**  
2. Le projet final **Gestionnaire_Planning_Collectif_Python**

---

## 📂 Structure du dépôt

Projets_Master/
└─ Semaine2AlgorithmieMDI/
└─ Gestionnaire_Planning_Collectif_Python/
├─ README.md
├─ diagrams/ # Diagrammes du projet (Draw.io, PNG, SVG)
├─ screenshots/ # Captures d’écran de l’application
├─ src/ # Code source Python
│ ├─ main.py
│ ├─ events.py
│ ├─ participants.py
│ ├─ rooms.py
│ ├─ export.py
│ ├─ utils.py
│ └─ storage/
│ └─ events.db
├─ storage/ # Données du projet
│ ├─ events.csv
│ ├─ events.json
│ ├─ events.db
│ ├─ participants.json
│ ├─ salles.json
│ └─ init_db.py
└─ requirements.txt # Librairies Python nécessaires

yaml
Copier le code

---

## Description du projet

**Gestionnaire de planning collectif en Python**  
Permet à une équipe de créer, gérer et optimiser un emploi du temps partagé.

### Fonctionnalités principales
- Gestion des événements (création, suppression, listing)
- Gestion des participants (ajout, retrait, agenda)
- Détection des conflits horaires
- Recherche de créneau commun pour plusieurs participants
- Gestion des salles avec capacité maximale
- Export CSV, JSON, SQLite
- Interface console simple avec validations et affichage coloré

---

## Installation

1. Cloner le dépôt :

### Option 1 : Cloner le dépôt principal (tous les projets)


git clone https://github.com/mariustiberiu/Projets_Master.git
cd Semaine2AlgorithmieMDI/Gestionnaire_Planning_Collectif_Python
Créer un environnement virtuel et l’activer :

Option 2 : Télécharger seulement ce projet depuis GitHub

Gestionnaire_Planning_Collectif_Python
Installer les dépendances
pip install -r requirements.txt

Copier le code
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Utilisation
Lancer le programme :

bash
Copier le code
python src/main.py
Suivre le menu principal :

yaml
Copier le code
1 : Gestion des événements
2 : Gestion des participants
3 : Gestion des salles
4 : Export / Sauvegarde
Q : Quitter
Chaque sous-menu contient des options pour ajouter, supprimer, lister ou effectuer des recherches avancées.
Le menu principal et les sous-menus affichent des validations et des messages clairs pour l’utilisateur.





Structure du projet
Gestionnaire_Planning_Collectif_Python/
├─ README.md
├─ diagrams/
│  ├─ diagram_events.drawio
│  ├─ diagram_events.drawio.png
│  ├─ diagram_export.drawio
│  ├─ diagram_export.drawio.png
│  ├─ diagram_participants.drawio
│  ├─ diagram_participants.drawio.png
│  ├─ diagram_principal.drawio
│  ├─ diagram_principal.drawio.png
│  ├─ diagram_principal.svg
│  ├─ diagram_rooms.drawio
│  ├─ diagram_rooms.drawio.png
│  └─ planning_flow.png
├─ requirements.txt
├─ screenshots/
├─ src/
│  ├─ main.py
│  ├─ events.py
│  ├─ participants.py
│  ├─ rooms.py
│  ├─ export.py
│  ├─ utils.py
│  └─ storage/events.db
├─ storage/
│  ├─ events.csv
│  ├─ events.db
│  ├─ events.json
│  ├─ init_db.py
│  ├─ participants.json
│  └─ salles.json
└─ .gitignore

Utilisation

Lancer le programme :

python src/main.py


Suivre le menu principal :

1 : Gestion des événements
2 : Gestion des participants
3 : Gestion des salles
4 : Export / Sauvegarde
Q : Quitter


Dans Gestion des participants :

1 : Ajouter participant
2 : Retirer participant
3 : Afficher agenda d’un participant
Q : Retour au menu principal

Auteur
Niculae Marius-Tiberiu Groupe 2

Collaborateurs / Groupe
Collègue 1
Collègue 2


Notes
Le projet utilise un fichier .gitignore pour exclure le dossier .venv et les fichiers temporaires.

Tous les fichiers de données et captures sont inclus pour permettre une réutilisation ou une présentation complète