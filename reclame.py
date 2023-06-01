def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    smaak = "aardbei"
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {nieuwe_prijs}."

def inkomsten_totaal(inkomsten):
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal_bedrag = inkomsten_totaal(inkomsten) 

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is <totaal> euro, waarover <bedrag> euro btw betaald dient te worden."
btw = 0.09

def laag_en_hoog(mijn_lijst):
    inkomsten_laagste = (90)
    inkomsten_hoogste = (430)
    inkomsten = (inkomsten_laagste, inkomsten_hoogste)

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
def gemiddelde(mijn_lijst):
    totaal_bedrag = sum(mijn_lijst)
    aantal_dagen = len(mijn_lijst)
    gemiddelde_bedrag = totaal_bedrag / aantal_dagen
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."
print()
