def calculer_synthese(comparatif):

    compteur = {}

    for ligne in comparatif:

        enseigne = ligne["moins_cher"]

        compteur[enseigne] = (

            compteur.get(enseigne, 0)

            + 1

        )

    return compteur

def calculer_synthese(rapport):
   resultat = {}
   for ligne in rapport:
       enseigne = ligne["moins_cher"]
       resultat[enseigne] = (
           resultat.get(
               enseigne,
               0
           ) + 1
       )
   return resultat