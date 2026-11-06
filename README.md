# Analyse Comparative de Marché

## Présentation

Ce projet a été réalisé dans le cadre du cours de Développement d'Applications Python.

L'objectif est d'aider un client à comparer les prix de plusieurs enseignes afin d'identifier les meilleures offres du marché.

L'application collecte des données provenant de plusieurs sources, les nettoie, les rapproche d'un catalogue commun, puis génère des comparaisons et des analyses décisionnelles.

---

## Sources de données

- Marché Lagune (CSV)
- Baobab Shop (JSON)
- Comptoir Ivoire (Excel)
- Catalogue de référence
- Historique des prix

---

## Fonctionnalités

### Chargement des données

- Lecture de fichiers CSV
- Lecture de fichiers JSON
- Lecture de fichiers Excel

### Nettoyage et contrôle qualité

- Détection des produits en rupture
- Détection des prix manquants
- Détection des stocks nuls
- Journalisation des anomalies

### Normalisation

- Uniformisation des noms de produits
- Suppression des différences de casse et d'espaces

### Rapprochement

- Association automatique des produits avec le catalogue de référence

### Comparatif

- Identification de l'enseigne la moins chère
- Calcul des écarts en FCFA
- Calcul des écarts en pourcentage

### Synthèse

- Comptage du nombre de fois où chaque enseigne est la moins chère
- Classement des meilleures offres

### Panier

- Calcul du coût du panier dans chaque enseigne
- Calcul du panier optimisé

### Historique

- Analyse des prix pendant la période du Black Friday
- Comparaison avec la moyenne annuelle

### Exportation

- Génération automatique du fichier comparatif.csv

---

## Architecture du projet

```text
analyse_marche
│
├── data
│   ├── catalogue_reference.csv
│   ├── marche_lagune.csv
│   ├── baobab_shop.json
│   ├── comptoir_ivoire.xlsx
│   └── historique_prix.csv
│
├── exports
│   └── comparatif.csv
│
├── logs
│   └── journal.txt
│
├── loaders
│   ├── csv_loader.py
│   ├── marche_loader.py
│   ├── json_loader.py
│   └── excel_loader.py
│
├── services
│   ├── nettoyage.py
│   ├── rapprochement.py
│   ├── comparatif.py
│   ├── synthese.py
│   ├── panier.py
│   ├── historique.py
│   ├── controle_qualite.py
│   └── journal.py
│
└── main.py
```

---

## Structures de données utilisées

- Listes (list)
- Dictionnaires (dict)
- Ensembles (set)

---

## Complexité

### Approche naïve

Boucles imbriquées :

```
O(n²)
```

### Approche optimisée

Utilisation de dictionnaires :

```
O(n)
```

### Recherche par clé

```
O(1)
```

---

## Lancement du projet

Installation :

```bash
pip install pandas openpyxl rapidfuzz
```

Exécution :

```bash
py main.py
```

---

## Menu de l'application

```text
1 - Voir le catalogue
2 - Rechercher un produit
3 - Voir le comparatif
4 - Top 3 des écarts
5 - Synthèse
6 - Panier
7 - Analyse Black Friday
8 - Exporter le comparatif
9 - Temps d'exécution
10 - Informations du projet
11 - Journal des anomalies
0 - Quitter
```

---

## Résultats

Le projet permet :

- de comparer automatiquement les prix ;
- de détecter les anomalies ;
- de proposer un panier optimisé ;
- d'analyser les périodes promotionnelles ;
- d'aider à la prise de décision.

---

## Auteur

Christian Tolidji Uriel Alladaye

Licence 2 Réseaux et Télécommunications

Projet Python : Analyse Comparative de Marché
