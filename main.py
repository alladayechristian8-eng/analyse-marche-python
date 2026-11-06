
import time
debut = time.perf_counter()
import os

os.makedirs(

    "logs",

    exist_ok=True

)

open(

    "logs/journal.txt",

    "w",

    encoding="utf-8"

).close()
 

# ==================================================
# IMPORTATION DES MODULES
# ==================================================
from loaders.marche_loader import charger_marche_lagune
from loaders.csv_loader import charger_catalogue
from loaders.json_loader import charger_baobab
from loaders.excel_loader import charger_comptoir
from services.rapprochement import creer_index_catalogue
from services.comparatif import (
    construire_index_prix,
    calculer_comparatif,
    top_3_ecarts,
    exporter_csv
)
from services.synthese import calculer_synthese
from services.panier import (
    calculer_panier,
    panier_optimise
)
from services.historique import analyser_black_friday
from services.controle_qualite import (
    verifier_marche_lagune,
    verifier_baobab,
    verifier_comptoir
)

# ==================================================
# CHARGEMENT DES DONNEES
# ==================================================
print("\nChargement des données...\n")

marche = charger_marche_lagune(
    "data/marche_lagune.csv"
)

 

catalogue = charger_catalogue(
    "data/catalogue_reference.csv"
)

baobab = charger_baobab(
    "data/baobab_shop.json"
)

comptoir = charger_comptoir(
    "data/comptoir_ivoire.xlsx"
)

# ==================================================
# CONTROLE QUALITE ET JOURNAL
# ==================================================
open(
    "logs/journal.txt",
    "w",
    encoding="utf-8"
).close()

verifier_marche_lagune(marche)
verifier_baobab(baobab)
verifier_comptoir(comptoir)

# ==================================================
# CREATION DE L'INDEX CATALOGUE
# ==================================================
index_catalogue = creer_index_catalogue(
    catalogue
)

# ==================================================
# CONSTRUCTION AUTOMATIQUE DE L'INDEX DES PRIX
# ==================================================
index_prix = construire_index_prix(
    marche,
    baobab,
    comptoir,
    index_catalogue
)

# ==================================================
# COMPARATIF
# ==================================================
rapport = calculer_comparatif(
    index_prix
)

# ==================================================
# SYNTHESE
# ==================================================
synthese = calculer_synthese(
    rapport
)

# ==================================================
# PANIER
# ==================================================
panier = calculer_panier(
    index_prix
)

# ==================================================
# TEMPS INITIAL
# ==================================================
temps_initialisation = round(
    time.perf_counter() - debut,
    4
)

print("Application prête.\n")

# ==================================================
# MENU INTERACTIF
# ==================================================
while True:

    print("\n" + "=" * 55)
    print("ANALYSE COMPARATIVE DE MARCHE")
    print("=" * 55)
    print("1 - Voir le catalogue")
    print("2 - Rechercher un produit")
    print("3 - Voir le comparatif")
    print("4 - Top 3 des écarts")
    print("5 - Synthèse")
    print("6 - Panier")
    print("7 - Analyse Black Friday")
    print("8 - Exporter le comparatif")
    print("9 - Temps d'exécution")
    print("10 - Informations du projet")
    print("11 - Journal des anomalies")
    print("0 - Quitter")
    print("=" * 55)

    choix = input("\nVotre choix : ").strip()

    # ==================================================
    # CATALOGUE
    # ==================================================
    if choix == "1":

        print("\nCATALOGUE DES PRODUITS\n")

        for pid, info in catalogue.items():
            print(
                pid,
                "-",
                info["nom"]
            )

    # ==================================================
    # RECHERCHE PRODUIT
    # ==================================================
    elif choix == "2":

        produit = input(
            "\nEntrez un code produit (P04 par exemple) : "
        ).strip().upper()

        if produit in catalogue:

            print(
                "\nProduit :",
                catalogue[produit]["nom"]
            )

            if produit in index_prix:

                print("\nPrix disponibles :\n")

                for enseigne, prix in index_prix[produit].items():
                    print(
                        enseigne,
                        ":",
                        prix,
                        "FCFA"
                    )

                moins_cher = min(
                    index_prix[produit],
                    key=index_prix[produit].get
                )

                print(
                    "\nMeilleure offre :",
                    moins_cher
                )

            else:
                print("\nAucun prix disponible.")

        else:
            print("\nCode produit inexistant.")

    # ==================================================
    # COMPARATIF
    # ==================================================
    elif choix == "3":

        print("\nCOMPARATIF DES PRIX\n")

        for ligne in rapport:
            print(ligne)

    # ==================================================
    # TOP 3
    # ==================================================
    elif choix == "4":

        print("\nTOP 3 DES ECARTS\n")

        for item in top_3_ecarts(rapport):
            print(item)

    # ==================================================
    # SYNTHESE
    # ==================================================
    elif choix == "5":

        print("\nSYNTHESE\n")

        for enseigne, nb in synthese.items():
            print(
                enseigne,
                "est moins chère",
                nb,
                "fois"
            )

    # ==================================================
    # PANIER
    # ==================================================
    elif choix == "6":

        print("\nPANIER\n")

        for enseigne, total in panier.items():
            print(
                enseigne,
                ":",
                total,
                "FCFA"
            )

        print(
            "\nPanier optimisé :",
            panier_optimise(index_prix),
            "FCFA"
        )

    # ==================================================
    # BLACK FRIDAY
    # ==================================================
    elif choix == "7":

        print("\nANALYSE BLACK FRIDAY\n")

        analyser_black_friday(
            "data/historique_prix.csv"
        )

    # ==================================================
    # EXPORT CSV
    # ==================================================
    elif choix == "8":

        exporter_csv(rapport)

        print("\nComparatif exporté avec succès.")

    # ==================================================
    # TEMPS D'EXECUTION
    # ==================================================
    elif choix == "9":

        temps_actuel = round(
            time.perf_counter() - debut,
            4
        )

        print(
            "\nTemps écoulé :",
            temps_actuel,
            "secondes"
        )

    # ==================================================
    # INFORMATIONS DU PROJET
    # ==================================================
    elif choix == "10":

        print("\nINFORMATIONS DU PROJET\n")

        print(f"Catalogue : {len(catalogue)} produits")
        print(f"Marché Lagune : {len(marche)} produits")
        print(f"Baobab Shop : {len(baobab)} produits")
        print(f"Comptoir Ivoire : {len(comptoir)} produits")
        print(f"Produits comparables : {len(index_prix)}")
        print(f"Produits comparés : {len(rapport)}")

    # ==================================================
    # JOURNAL DES ANOMALIES
    # ==================================================
    elif choix == "11":

        print("\nJOURNAL DES ANOMALIES\n")

        try:

            with open(
                "logs/journal.txt",
                "r",
                encoding="utf-8"
            ) as fichier:

                contenu = fichier.read()

                if contenu.strip():
                    print(contenu)

                else:
                    print("Aucune anomalie détectée.")

        except FileNotFoundError:

            print("Journal introuvable.")

    # ==================================================
    # QUITTER
    # ==================================================
    elif choix == "0":

        print("\nMerci d'avoir utilisé l'application.")
        break

    # ==================================================
    # ERREUR
    # ==================================================
    else:

        print("\nChoix invalide. Veuillez réessayer.")
