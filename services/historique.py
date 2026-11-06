import pandas as pd


def analyser_black_friday(fichier):

    df = pd.read_csv(fichier)

    df["date"] = pd.to_datetime(df["date"])

    black_friday = df[

        (df["date"] >= "2025-11-24")
&

        (df["date"] <= "2025-11-30")

    ]

    print("\nBLACK FRIDAY\n")

    for source in df["source"].unique():

        moyenne_annuelle = (

            df[df["source"] == source]

            ["prix_fcfa"]

            .mean()

        )

        moyenne_black = (

            black_friday[

                black_friday["source"] == source

            ]["prix_fcfa"]

            .mean()

        )

        print(

            source,

            "\nMoyenne annuelle :",

            round(moyenne_annuelle, 2),

            "\nMoyenne Black Friday :",

            round(moyenne_black, 2),

            "\n"

        )
 