import csv
from presentatie import presenteer

inkomsten = {
    'Aarbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750
}

totaal_inkomsten = 5250

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])

