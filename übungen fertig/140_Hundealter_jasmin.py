
# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.


# Hundealter in Menschenjahre umrechnen

hundealter = int(input("Gib das Alter des Hundes in Jahren ein: "))

if hundealter == 1:
    menschenjahre = 14
elif hundealter == 2:
    menschenjahre = 22
elif hundealter >= 17:
    menschenjahre = 22 + (hundealter - 2) * 5  # Definiere menschenjahre auch hier
    print("Dein Hund ist älter als Gandalf!")
else:
    menschenjahre = 22 + (hundealter - 2) * 5

print(f"Das Alter von {hundealter} Hundejahr(en) entspricht etwa {menschenjahre} Menschenjahren.")

