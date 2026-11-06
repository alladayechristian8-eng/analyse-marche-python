import pandas as pd


def charger_comptoir(fichier):

    df = pd.read_excel(

        fichier,

        header=2

    )

    produits = []

    for _, ligne in df.iterrows():

        try:

            prix = str(

                ligne["Prix catalogue (FCFA)"]

            ).replace(" ", "").replace("\u202f", "")

            prix = float(prix)

            remise = float(

                ligne["Remise (%)"]

            )

            prix_final = prix - (

                prix * remise / 100

            )

            produits.append({

                "nom": str(

                    ligne["Article"]

                ).strip(),

                "prix": round(

                    prix_final

                ),

                "stock": int(

                    ligne["Quantité en rayon"]

                ),

                "source": "Comptoir Ivoire"

            })

        except Exception as erreur:

            print(

                "Erreur :",

                ligne,

                erreur

            )

    return produits
 