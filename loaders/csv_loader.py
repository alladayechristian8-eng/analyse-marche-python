import csv

def charger_catalogue(fichier):
   produits = {}
   with open(fichier, encoding="utf-8") as f:
       reader = csv.DictReader(f)
       for ligne in reader:
           produits[ligne["produit_id"]] = {
               "nom": ligne["nom"],
               "categorie": ligne["categorie"],
               "marque": ligne["marque"]
           }
   return produits