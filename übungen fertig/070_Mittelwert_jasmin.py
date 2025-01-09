
# Mittelwert

"""
Schreibe eine Funktion, die drei Zahlen entgegennimmt,
den Mittelwert (Durchschnitt) berechnet und diesen zurückgibt.
"""


def berechne_mittelwert(a, b, c):
    """Berechnet den Mittelwert von drei Zahlen."""
    mittelwert = (a + b + c) / 3
    return mittelwert


zahl1 = 4
zahl2 = 8
zahl3 = 15
ergebnis = berechne_mittelwert(zahl1, zahl2, zahl3)
print(f"Der Mittelwert von {zahl1}, {zahl2} und {zahl3} ist: {ergebnis}")
