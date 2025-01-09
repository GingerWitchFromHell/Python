""" 1.Schreibe ein Programm, das testet und ausgibt,
welche von zwei Zahlen (User Eingabe) größer ist oder ob beide Zahlen gleich groß sind"""

""" 2.Schreibe ein Programm, das testet und ausgibt,
welche von drei Zahlen (User Eingabe) kleiner ist."""
 
"""3. Schreiben Sie ein Python-Programm, das testet und ausgibt, ob eine Zahl(User Eingabe)
 gerade ist"""

"""4. Schreiben Sie ein Python-Programm, das testet und ausgibt, ob eine Zahl(User Eingabe)
 durch 7 und 5 teilbar ist"""
"""
# 1. 

# Eingabe von zwei Zahlen durch den Benutzer
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Vergleich der beiden Zahlen
if zahl1 > zahl2:
    print("Die erste Zahl ist größer als die zweite Zahl.")
elif zahl1 < zahl2:
    print("Die zweite Zahl ist größer als die erste Zahl.")
else:
    print("Beide Zahlen sind gleich groß.")
"""

"""
# 2.     

# Eingabe von drei Zahlen durch den Benutzer
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))

# Bestimmung der kleinsten Zahl
if zahl1 <= zahl2 and zahl1 <= zahl3:
    print("Die kleinste Zahl ist:", zahl1)
elif zahl2 <= zahl1 and zahl2 <= zahl3:
    print("Die kleinste Zahl ist:", zahl2)
else:
    print("Die kleinste Zahl ist:", zahl3)
"""

"""
# Eingabe der Zahl durch den Benutzer
zahl = int(input("Gib eine Zahl ein: "))

# Überprüfung, ob die Zahl gerade ist
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
"""

"""
# Eingabe der Zahl durch den Benutzer
zahl = int(input("Gib eine Zahl ein: "))

# Überprüfung, ob die Zahl durch 7 und 5 teilbar ist
if zahl % 7 == 0 and zahl % 5 == 0:
    print("Die Zahl ist durch 7 und 5 teilbar.")
else:
    print("Die Zahl ist nicht durch 7 und 5 teilbar.")
"""


"""
# Eingabe von drei Zahlen durch den Benutzer
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))

# Bestimmung der größten Zahl
if zahl1 >= zahl2 and zahl1 >= zahl3:
    groesste_zahl = zahl1
elif zahl2 >= zahl1 and zahl2 >= zahl3:
    groesste_zahl = zahl2
else:
    groesste_zahl = zahl3

print("Die größte Zahl ist:", groesste_zahl)

# Bestimmung der kleinsten Zahl
if zahl1 <= zahl2 and zahl1 <= zahl3:
    kleinste_zahl = zahl1
elif zahl2 <= zahl1 and zahl2 <= zahl3:
    kleinste_zahl = zahl2
else:
    kleinste_zahl = zahl3

print("Die kleinste Zahl ist:", kleinste_zahl)

# Überprüfung, ob jede Zahl gerade oder ungerade ist
def gerade_oder_ungerade(zahl):
    if zahl % 2 == 0:
        return "gerade"
    else:
        return "ungerade"

print(f"Die erste Zahl ({zahl1}) ist {gerade_oder_ungerade(zahl1)}.")
print(f"Die zweite Zahl ({zahl2}) ist {gerade_oder_ungerade(zahl2)}.")
print(f"Die dritte Zahl ({zahl3}) ist {gerade_oder_ungerade(zahl3)}.")

# Überprüfung, ob jede Zahl durch 7 und 5 teilbar ist
def teilbar_durch_7_und_5(zahl):
    if zahl % 7 == 0 and zahl % 5 == 0:
        return "durch 7 und 5 teilbar"
    else:
        return "nicht durch 7 und 5 teilbar"

print(f"Die erste Zahl ({zahl1}) ist {teilbar_durch_7_und_5(zahl1)}.")
print(f"Die zweite Zahl ({zahl2}) ist {teilbar_durch_7_und_5(zahl2)}.")
print(f"Die dritte Zahl ({zahl3}) ist {teilbar_durch_7_und_5(zahl3)}.")
"""
"""
from random import randint

wochentag = randint(1,7)

print(wochentag)

if wochentag == 1:
    print("montag")
elif wochentag == 2:
    print("dienstag")
elif wochentag == 3:
    print("mittwoch")
elif wochentag == 4:
    print("donnerstag")
elif wochentag == 5:
    print("friiidaaaaayyy")
elif wochentag == 6:
    print("samstag")
elif wochentag == 7:
    print("sonntag")
"""

"""
Addition von 2 zufällige Zahlen (bereich 1-100)
Die Eingabe wird in eine Zahl umgewandelt.
Entspricht diese Zahl dem Ergebnis der Rechnug,
wird ist Richtig ausgegeben
Anderenfalls wird ist falsch ausgegeben,
und das korrekte Ergebnis wird genannt.
Eine mögliche Ausgabe des Programms:
Die Aufgabe: 2+ 8
19
19 ist falsch.Viel Glück beim nächsten Mal!
Ergebnis: 10
Die Aufgabe: 2+ 8
11
11 ist ganz nahe dran
Ergebnis: 10
"""

import random

# Zufällige Zahlen generieren
zahl1 = random.randint(1, 100)
zahl2 = random.randint(1, 100)
korrektes_ergebnis = zahl1 + zahl2

# Aufgabe anzeigen
print(f"Die Aufgabe: {zahl1} + {zahl2}")

# Benutzereingabe
try:
    benutzer_ergebnis = int(input("Gib dein Ergebnis ein: "))

    # Überprüfung der Benutzereingabe
    if benutzer_ergebnis == korrektes_ergebnis:
        print(f"{benutzer_ergebnis} ist richtig! Gut gemacht!")
    elif abs(benutzer_ergebnis - korrektes_ergebnis) <= 2:
        print(f"{benutzer_ergebnis} ist ganz nahe dran!")
        print(f"Ergebnis: {korrektes_ergebnis}")
    else:
        print(f"{benutzer_ergebnis} ist falsch. Viel Glück beim nächsten Mal!")
        print(f"Ergebnis: {korrektes_ergebnis}")

except ValueError:
    print("Bitte gib eine gültige Zahl ein.")

    
    
          
          










