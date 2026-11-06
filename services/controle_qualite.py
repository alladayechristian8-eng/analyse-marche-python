
from services.journal import enregistrer_anomalie


def verifier_marche_lagune(produits):

    references = set()

    for produit in produits:

        ref = produit.get("reference", "")

        designation = produit.get(
            "designation",
            "Produit inconnu"
        )

        prix = produit.get("prix", "")

        disponibilite = produit.get(
            "disponibilite",
            ""
        )

        if ref:

            if ref in references:

                enregistrer_anomalie(
                    f"Doublon détecté : {ref}"
                )

            references.add(ref)

        if prix == "" or prix is None:

            enregistrer_anomalie(
                f"Prix manquant : {designation}"
            )

        if disponibilite == "Rupture":

            enregistrer_anomalie(
                f"Produit en rupture : {designation}"
            )


def verifier_baobab(produits):

    for produit in produits:

        if produit.get("prix") is None:

            enregistrer_anomalie(
                f"Prix absent : {produit.get('nom')}"
            )

        if produit.get("stock", 0) == 0:

            enregistrer_anomalie(
                f"Stock nul : {produit.get('nom')}"
            )


def verifier_comptoir(produits):

    for produit in produits:

        if produit.get("stock", 0) == 0:

            enregistrer_anomalie(
                f"Stock nul : {produit.get('nom')}"
            )
