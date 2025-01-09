
# Nettopreis

"""
Schreibe eine Funktion zum Berechnen des Nettopreises.
Dieser Funktion soll der Bruttopreis übergeben werden
und sie soll den Nettopreis zurückgeben.
Der Mehrwertsteuersatz soll als zweiter Parameter
übergeben werden können.
Der Standardwert des Mehrwertsteuersatzes soll 19 sein.

Teste die Funktion:
print(berechne_netto(119))     # 100.0
print(berechne_netto(107, 7))  # 100.0
"""


def berechne_netto(bruttopreis, mwst=19):
    """
    Berechnet den Nettopreis aus dem Bruttobetrag und dem Mehrwertsteuersatz.
    :param bruttopreis: Der Bruttobetrag (Preis inkl. MwSt.)
    :param mwst: Der Mehrwertsteuersatz in Prozent (Standardwert: 19%)
    :return: Der Nettobetrag
    """
    nettobetrag = bruttopreis / (1 + mwst / 100)
    return round(nettobetrag, 2)


print(berechne_netto(119))        
print(berechne_netto(107, 7))    
