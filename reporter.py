import csv

# cursistnamen -> gevolgde cursussen iclusief prijs
cursisten = {}
# voor so
cursisten_stats = []

#importeer regels uit cursisten.csv naar cursisten{}
with open("cursisten.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for regel in csv_reader:
        cursist = cursisten.setdefault(regel["naam"], {})
        cursist[regel["cursus"]] = regel["betaald"]  # zet naam en prijs van cursus bij cursist

for naam, cursus in cursisten.items():
    # maak statistieken gereed om in lijst te stoppen
    cursist_stats = []
    totaalbedrag = 0
    cursussen = ""
    # tel het totaalbedrag van trainingen op 
    for key in cursus.items():
        totaalbedrag += int(key[1])
    for key in cursus.items():
        if cursussen == "":
            cursussen = key[0]
        # voeg komma toe bij tweede woord
        else:
            cursussen += ", " + key[0]
    cursist_stats.append(naam)
    cursist_stats.append(totaalbedrag)
    cursist_stats.append(cursussen)
    cursisten_stats.append(cursist_stats)

# functie die statistieken weergeeft in leesbare tekst
def toon_cursist_info():
    for cursist in cursisten_stats:
        print("{0} - €{1} \n- {2}".format(cursist[0], cursist[1], cursist[2]))

# sorteer display lijst op alfabetische volgorde en geef weer
cursisten_stats.sort()
toon_cursist_info()

print("------------------------------")

# sorteer display lijst van klein naar groot 
cursisten_stats.sort(key = lambda x: x[1], reverse=True) # op dalend totaalbedrag
toon_cursist_info()