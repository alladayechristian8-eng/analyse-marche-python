import json

def charger_baobab(fichier):
   with open(fichier, encoding="utf-8") as f:
       data = json.load(f)
   produits = []
   for item in data["items"]:
       prix_final = None
       if item["pricing"]["amount"] is not None:
           prix_final = (
               item["pricing"]["amount"]
               + item["pricing"]["delivery_fee"]
           )
       produits.append({
           "nom": item["title"],
           "prix": prix_final,
           "stock": item["stock"],
           "source": "Baobab Shop"
       })
   return produits