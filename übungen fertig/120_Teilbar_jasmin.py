
# Teilbar
#
#  Schreibe ein Skript, das alle Zahlen von 1 bis 100 ausgibt,
#  die durch drei teilbar sind.
#  Hilfsmittel: Schleife, if, Modulo
#
#  Zusatz 1: Gib die Anzahl der Zahlen aus
#
#  Zusatz 2: Das Programm soll nun alle Zahlen ausgeben,
#            die durch 3 ODER 7 teilbar sind.
#            Gib auch hiervon die Anzahl aus.


zahlen_durch_3 = []
for zahl in range(1, 101):  
    if zahl % 3 == 0:
        zahlen_durch_3.append(zahl)


print("Zahlen von 1 bis 100, die durch 3 teilbar sind:")
print(zahlen_durch_3)
print("Anzahl:", len(zahlen_durch_3))

print("\n") 


zahlen_durch_3_oder_7 = []
for zahl in range(1, 101):
    if zahl % 3 == 0 or zahl % 7 == 0:
        zahlen_durch_3_oder_7.append(zahl)


print("Zahlen von 1 bis 100, die durch 3 ODER 7 teilbar sind:")
print(zahlen_durch_3_oder_7)
print("Anzahl:", len(zahlen_durch_3_oder_7))

