
# Erste Zeile: 1 2 3 4 5
for i in range(1, 6):
    print(i, end=' ')
print()  # Zeilenumbruch

# Zweite Zeile: 100 90 80 70 60 50 40 30 20 10
for i in range(100, 0, -10):
    print(i, end=' ')
print()  # Zeilenumbruch

# Dritte Zeile: 2000 3000 4000 5000 6000
for i in range(2000, 7000, 1000):
    print(i, end=' ')
print()  # Zeilenumbruch

# Vierte Zeile: 13 17 21 25 29
for i in range(13, 30, 4):
    print(i, end=' ')
print()  # Zeilenumbruch

# Fünfte Zeile: 1 2 3 4 5 6 8 9 10
for i in range(1, 11):
    if i != 7:  # 7 auslassen
        print(i, end=' ')
print()  # Zeilenumbruch

# Sechste Zeile: 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0
for i in range(20, -11, -5):  # Werte von 2.0 bis -1.0
    print(i / 10, end=' ')
print()  # Zeilenumbruch

for i in range(5,14,2):
    print(f"Z{i}",end=" ")


