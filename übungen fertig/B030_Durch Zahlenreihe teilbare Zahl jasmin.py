
# Durch Zahlenreihe teilbare Zahl

"""
Die kleinste positive Zahl,
die durch alle Zahlen von 1 bis 10 ohne Rest teilbar ist, ist die 2520.
Schreibe ein Programm mit der die kleinste positive Zahl ermittelt werden kann,
die durch alle Zahlen von 1 bis 40 ohne Rest teilbar ist.

Hinweis: Die gesuchte Zahl ist 5342931457063200

Tipp:
Erst einmal mit einer kleineren Zahl anfangen
und dann eine immer größere Zahl nehmen.
Hier alle möglichen Zahlen mit ihrem Ergebnis:

    1: 1
    2: 2
    3: 6
    4: 12
    5: 60
    6: 60
    7: 420
    8: 840
    9: 2520
    10: 2520
    11: 27720
    12: 27720
    13: 360360
    14: 360360
    15: 360360
    16: 720720
    17: 12252240
    18: 12252240
    19: 232792560
    20: 232792560
    21: 232792560
    22: 232792560
    23: 5354228880
    24: 5354228880
    25: 26771144400
    26: 26771144400
    27: 80313433200
    28: 80313433200
    29: 2329089562800
    30: 2329089562800
    31: 72201776446800
    32: 144403552893600
    33: 144403552893600
    34: 144403552893600
    35: 144403552893600
    36: 144403552893600
    37: 5342931457063200
    38: 5342931457063200
    39: 5342931457063200
    40: 5342931457063200
"""

import math

def lcm(a, b):
    """Berechnet das kleinste gemeinsame Vielfache (LCM) von a und b."""
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    """Findet die kleinste Zahl, die durch alle Zahlen von 1 bis n teilbar ist."""
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)  # Schrittweise Berechnung des LCM
    return result

# Für Zahlen von 1 bis 40
n = 40
result = smallest_multiple(n)
print(f"Die kleinste Zahl, die durch alle Zahlen von 1 bis {n} teilbar ist, ist: {result}")





