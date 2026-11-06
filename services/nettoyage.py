import re

def normaliser_nom(nom):
   """
   Met le texte en minuscules,
   supprime les espaces inutiles,
   supprime certains caractères.
   """
   nom = str(nom).lower()
   nom = nom.replace("-", " ")
   nom = nom.replace("(", " ")
   nom = nom.replace(")", " ")
   nom = nom.replace("/", " ")
   nom = " ".join(nom.split())
   return nom

def nettoyer_prix(prix):
   """
   Convertit :
   102 900 FCFA
   en
   102900
   """
   if prix is None:
       return None
   prix = str(prix)
   if "prix sur demande" in prix.lower():
       return None
   chiffres = re.sub(r"[^0-9]", "", prix)
   if chiffres == "":
       return None
   return int(chiffres)