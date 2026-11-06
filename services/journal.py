def enregistrer_anomalie(message):

    with open(

        "logs/journal.txt",

        "a",

        encoding="utf-8"

    ) as fichier:

        fichier.write(message + "\n")
 