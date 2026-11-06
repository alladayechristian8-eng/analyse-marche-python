import csv

from services.rapprochement import trouver_produit


def construire_index_prix(

    marche,

    baobab,

    comptoir,

    index_catalogue

):

    index_prix = {}

    # ============================

    # MARCHE LAGUNE

    # ============================

    for produit in marche:

        produit_id, score = trouver_produit(

            produit["designation"],

            index_catalogue

        )

        if produit_id:

            prix_txt = str(

                produit["prix"]

            )

            chiffres = "".join(

                c for c in prix_txt

                if c.isdigit()

            )

            if chiffres:

                prix = int(chiffres)

                if produit_id not in index_prix:

                    index_prix[produit_id] = {}

                index_prix[produit_id][

                    "Marche Lagune"

                ] = prix

    # ============================

    # BAOBAB SHOP

    # ============================

    for produit in baobab:

        produit_id, score = trouver_produit(

            produit["nom"],

            index_catalogue

        )

        if produit_id and produit["prix"]:

            if produit_id not in index_prix:

                index_prix[produit_id] = {}

            index_prix[produit_id][

                "Baobab Shop"

            ] = produit["prix"]

    # ============================

    # COMPTOIR IVOIRE

    # ============================

    for produit in comptoir:

        produit_id, score = trouver_produit(

            produit["nom"],

            index_catalogue

        )

        if produit_id:

            if produit_id not in index_prix:

                index_prix[produit_id] = {}

            index_prix[produit_id][

                "Comptoir Ivoire"

            ] = produit["prix"]

    return index_prix


def calculer_comparatif(index_prix):

    rapport = []

    for produit_id, prixs in index_prix.items():

        if len(prixs) < 2:

            continue

        prix_min = min(prixs.values())

        prix_max = max(prixs.values())

        moins_cher = min(

            prixs,

            key=prixs.get

        )

        ecart_fcfa = prix_max - prix_min

        ecart_pct = (

            ecart_fcfa / prix_min

        ) * 100

        rapport.append({

            "produit_id": produit_id,

            "moins_cher": moins_cher,

            "prix_min": prix_min,

            "prix_max": prix_max,

            "ecart_fcfa": ecart_fcfa,

            "ecart_pct": round(ecart_pct, 2)

        })

    return rapport


def top_3_ecarts(rapport):

    return sorted(

        rapport,

        key=lambda x: x["ecart_pct"],

        reverse=True

    )[:3]


def exporter_csv(

    rapport,

    fichier="exports/comparatif.csv"

):

    with open(

        fichier,

        "w",

        newline="",

        encoding="utf-8"

    ) as f:

        writer = csv.DictWriter(

            f,

            fieldnames=rapport[0].keys()

        )

        writer.writeheader()

        writer.writerows(

            rapport

        )
 