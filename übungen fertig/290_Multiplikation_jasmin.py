
# Multiplikation
#
# Schreibe ein Programm, das ermittelt,
# wie viele ganzzahlige Multiplikator-Multiplikand-Kombinationen
# vom Produkt 8.420.000 es gibt,
# bei denen sowohl Multiplikator als auch Multiplikand
# kleiner als 10.000 sind.
#
# 1000 * 8420 und 8420 * 1000 zählt nur einmal.

# Gib die Zahlenpaare aus:
# 1000 * 8420
# 1250 * 6736
# ...

produkt = 8420000

paare = []
for x in range(1, 10000):
    if produkt % x == 0:
        y = produkt // x
        if y < 10000 and x <= y:
            paare.append((x, y))

print(f"Es gibt {len(paare)} gültige Zahlenpaare: ")
for x, y in paare:
    print(f"{x} * {y}")

           