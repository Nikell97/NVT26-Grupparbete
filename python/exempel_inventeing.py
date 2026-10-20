# Inventerings- och statusrapport
# Grupparbete Nätverskteknik

import csv

with open("enheter.csv", "r") as fil:
    lasare = csv.DictReader(fil)
    for enhet in lasare:
        print(enhet["namn"], enhet["modell"], enhet["version"])

with open("status.csv", "r") as fil:
        status_lasare = csv.DictReader(fil)

        for rad in status_lasare:
            print(rad["namn"])