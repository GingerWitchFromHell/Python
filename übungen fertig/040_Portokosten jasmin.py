
# Portokosten

"""
Die Portokosten (Versandkosten) sind wie folgt festgelegt:
 0 - 39.99 € Bestellwert kosten 3.99 € Porto
40 - 69.99 € Bestellwert kosten 2.99 € Porto
70 - 99.99 € Bestellwert kosten 1.99 € Porto
ab 100 € ist portofrei

Es soll eine Zufallszahl (bestellwert)
von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)

Dann soll ermittelt werden,
wie hoch die entsprechenden Portokosten sind.
Am Ende sollen der Bestellwert, die Portokosten
und der Gesamtbetrag ausgegeben werden.
"""

import random


bestellwert = round(random.uniform(1.00, 130.00), 2)  # Fließkommazahl mit 2 Dezimalstellen
versandkosten = 0.00

if bestellwert <= 39.99:
    versandkosten = 3.99
    print(f"Der Bestellwert liegt unter 40 €, das Porto beträgt 3,99 €.")
elif 40.00 <= bestellwert <= 69.99:
    versandkosten = 2.99
    print(f"Der Bestellwert liegt zwischen 40 € und 70 €, das Porto beträgt 2,99 €.")
elif 70.00 <= bestellwert <= 99.99:
    versandkosten = 1.99
    print(f"Der Bestellwert liegt zwischen 70 € und 100 €, das Porto beträgt 1,99 €.")
elif bestellwert >= 100.00:
    versandkosten = 0.00
    print(f"Der Bestellwert liegt über 100 €, der Versand ist kostenfrei!")

gesamtbetrag = bestellwert + versandkosten
print(f"Bestellwert: {bestellwert} €")
print(f"Versandkosten: {versandkosten} €")
print(f"Gesamtbetrag: {gesamtbetrag} €")
