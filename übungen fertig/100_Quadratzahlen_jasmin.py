
# Quadratzahlen

"""
Schreibe ein Skript, welches alle Quadratzahlen von natürlichen
Zahlen (1, 2, 3, ...) ausgibt, die kleiner als 100 sind.
(Die Quadratzahlen sollen kleiner 100 sein!)

Zusatz: Gib auch die Anzahl der gefundenen Quadratzahlen aus
"""


quadratzahlen = []  


zahl = 1
while zahl ** 2 < 100:
    quadratzahlen.append(zahl ** 2)
    zahl += 1


print("Quadratzahlen kleiner als 100:", quadratzahlen)


print("Anzahl der Quadratzahlen:", len(quadratzahlen))
