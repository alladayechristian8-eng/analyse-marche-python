import csv

def charger_marche_lagune(fichier):
   produits = []
   with open(
       fichier,
       encoding="utf-8"
   ) as f:
       reader = csv.DictReader(
           f,
           delimiter=";"
       )
       for ligne in reader:
           produits.append(ligne)
   return produits