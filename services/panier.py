PANIER = {
    "P04": 1,
    "P12": 1,
    "P14": 2,
    "P15": 1,
    "P28": 1
}


def calculer_panier(index_prix):

    resultats = {}

    enseignes = [
        "Marche Lagune",
        "Baobab Shop",
        "Comptoir Ivoire"
    ]

    for enseigne in enseignes:

        total = 0

        for produit, quantite in PANIER.items():

            if produit in index_prix:

                if enseigne in index_prix[produit]:

                    total += (
                        index_prix[produit][enseigne]
                        * quantite
                    )

        resultats[enseigne] = total

    return resultats


def panier_optimise(index_prix):

    total = 0

    for produit, quantite in PANIER.items():

        if produit in index_prix:

            prix_min = min(
                index_prix[produit].values()
            )

            total += prix_min * quantite

    return total