from rapidfuzz import process
from services.nettoyage import normaliser_nom

def creer_index_catalogue(catalogue):
   index = {}
   for produit_id, infos in catalogue.items():
       nom = normaliser_nom(
           infos["nom"]
       )
       index[nom] = produit_id
   return index

def trouver_produit(nom_produit, index_catalogue):
   nom = normaliser_nom(nom_produit)
   resultat = process.extractOne(
       nom,
       index_catalogue.keys()
   )
   if resultat:
       meilleur_nom = resultat[0]
       score = resultat[1]
       if score >= 60:
           return (
               index_catalogue[meilleur_nom],
               score
           )
   return (None, 0)