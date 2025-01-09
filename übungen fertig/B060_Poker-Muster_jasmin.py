
# Poker-Muster

# Das Würfelspiel Yahtzee verwendet ähnliche Muster wie das Kartenspiel Poker,
# verzichtet aber auf die verschiedenen Farben.
# Bei Yahtzee werden fünf Spielwürfel (Augenzahlen 1 bis 6) geworfen.
# Verwende dazu Zufallszahlen.

# Schreibe ein Programm, das die fünf Zahlen in einer Liste speichert
# und mittels einer Funktion in der Standardausgabe anzeigt.
#
# Entscheide dann, ob alle Zahlen gleich sind (5-Poker).

# Zusatz:
# Entscheide, ob es sich um ein anderes Poker-Muster handelt:
# Vierling
# Strasse
# Full House
# Drilling
# Zwei Paare
# Paar

import random

# Funktion: Würfeln simulieren
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# Funktion: Poker-Muster analysieren
def analyze_pattern(dice):
    counts = {number: dice.count(number) for number in set(dice)}  # Häufigkeiten zählen
    values = sorted(counts.values(), reverse=True)  # Häufigkeiten sortieren

    if values == [5]:  # 5 gleiche Zahlen
        return "5-Poker"
    elif values == [4, 1]:  # 4 gleiche Zahlen und 1 unterschiedliche
        return "Vierling"
    elif values == [3, 2]:  # 3 gleiche Zahlen und 2 gleiche Zahlen
        return "Full House"
    elif sorted(dice) == list(range(min(dice), min(dice) + 5)):  # Aufeinanderfolgende Zahlen
        return "Straße"
    elif values == [3, 1, 1]:  # 3 gleiche Zahlen und 2 unterschiedliche
        return "Drilling"
    elif values == [2, 2, 1]:  # 2 Paare und 1 unterschiedliche Zahl
        return "Zwei Paare"
    elif values == [2, 1, 1, 1]:  # 1 Paar und 3 unterschiedliche Zahlen
        return "Paar"
    else:  # Kein Muster
        return "Kein spezielles Muster"

# Funktion: Mehrere Würfelwürfe ausführen und Ergebnisse speichern
def roll_dice_multiple_times(times):
    results = []
    for _ in range(times):
        dice = roll_dice()
        pattern = analyze_pattern(dice)
        results.append((dice, pattern))  # Speichere das Ergebnis und das Muster
    return results

# Funktion: Statistik erstellen
def generate_statistics(results):
    statistics = {}
    for _, pattern in results:
        if pattern in statistics:
            statistics[pattern] += 1
        else:
            statistics[pattern] = 1
    return statistics

# Hauptprogramm
def main():
    # Eingabe der Anzahl der Würfe
    try:
        times = int(input("Wie oft soll gewürfelt werden? "))
        if times <= 0:
            print("Die Anzahl der Würfe muss eine positive Zahl sein.")
            return
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")
        return
    
    # Würfe durchführen
    results = roll_dice_multiple_times(times)
    
    # Würfelergebnisse ausgeben
    print("\nErgebnisse der Würfe:")
    for idx, (dice, pattern) in enumerate(results, start=1):
        print(f"Wurf {idx}: {dice} -> {pattern}")
    
    # Statistik generieren und ausgeben
    statistics = generate_statistics(results)
    print("\nStatistik:")
    for pattern, count in statistics.items():
        print(f"{pattern}: {count} Mal")

# Programm ausführen
if __name__ == "__main__":
    main()
