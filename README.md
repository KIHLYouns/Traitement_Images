# Projet de Traitement d'Images en Python

## Introduction

Ce projet de travaux pratiques (TP) a pour objectif de vous familiariser avec le traitement d'images en utilisant le langage de programmation Python. Vous apprendrez à manipuler des images binaires et en niveaux de gris, à appliquer des filtres, à générer des histogrammes et à transformer des images couleur.

## Prérequis

- **Python 3.12** installé.
- **Pip** pour gérer les paquets Python.

## Installation

### 1. Cloner le Répertoire

Si vous utilisez Git, vous pouvez cloner le répertoire avec la commande suivante :

```zsh
git clone https://github.com/KIHLYouns/Traitement_Images.git
cd Traitement_Images
```

## Structure du Projet

```
Traitement_image/
├── images_initiales/
│   ├── I1.pbm
│   ├── I2.pbm
│   ├── I_g.pgm
│   ├── image_gris.png
│   ├── portrait_youns.jpeg
│   └── thousand-yard_stare.jpeg
├── programmes/
│   ├── q1.py
│   ├── q2.py
│   ├── q3.py
│   ├── q4.py
│   └── q5.py
└── résultats/
```

## Utiliser un Environnement Virtuel

Il est recommandé d'utiliser un environnement virtuel pour gérer les dépendances du projet.

### 1. Vérifier la version de Python

```sh
python3 --version
```

Assurez-vous que la sortie est Python 3.12.x

### 2. Créer un environnement virtuel nommé 'venv'

```sh
python3 -m venv venv
```

### 3. Activer l'environnement virtuel

```sh
source venv/bin/activate
```

### 4. Mettre à jour pip dans l'environnement virtuel

```sh
pip install --upgrade pip
```

### 5. Installer les modules requis

```sh
pip install numpy matplotlib Pillow tqdm
```

### 6. Exécuter votre script Python

```sh
python3 programmes/q1.py
```

## Utilisation des Scripts Python

### q1.py : Manipulation d'Images Binaires

Ce script permet de créer, lire et afficher des images au format PBM (Portable Bitmap). Il effectue également des opérations arithmétiques sur des images binaires.

#### Exécution

```sh
python3 programmes/q1.py
```

### q2.py : Génération d'Histogrammes

Ce script génère et affiche l'histogramme des canaux de couleur d'une image.

#### Exécution

```sh
python3 programmes/q2.py
```

### q3.py : Transformation d'Images Couleur

Ce script transforme une image couleur en une image en niveaux de gris ou binaire, en fonction du choix de l'utilisateur.

#### Exécution

```sh
python3 programmes/q3.py
```

### q5.py : Application du Filtre de Nagao

Ce script applique le filtre de Nagao à une image en niveaux de gris, avec une barre de progression pour suivre le traitement.

#### Exécution

```sh
python3 programmes/q5.py
```
