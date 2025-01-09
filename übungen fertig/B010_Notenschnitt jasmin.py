
# Notenschnitt

"""
Schreibe ein Programm, das 20 Zeugnisnoten (1.0 bis 6.0) in Zehntel-Noten
(z.B. 4.3) zufällig erzeugt.

Verwende diese 20 Noten, um damit den relevanten Durchschnitt
nach folgendem Verfahren zu berechnen:
- streiche die beste und die schlechteste Note (statistische Ausreißer),
- ermittel den Durchschnitt der verbleibenden Noten
- runde zur nächsten halben Note (1, 1.5, 2, ..., 4.5, 5, 5.5, 6).
"""

import random

def generate_grades():
    # 20 Zufallsnoten zwischen 1.0 und 6.0 in Zehntelschritten
    grades = [round(random.uniform(1.0, 6.0), 1) for _ in range(20)]
    return grades

def calculate_average(grades):
    # Sortiere die Noten
    sorted_grades = sorted(grades)

    # Entferne die beste und schlechteste Note
    trimmed_grades = sorted_grades[1:-1]

    # Berechne den Durchschnitt der verbleibenden Noten
    average = sum(trimmed_grades) / len(trimmed_grades)

    # Runde zur nächsten halben Note
    rounded_average = round(average * 2) / 2

    return rounded_average

# Zufallsnoten generieren
grades = generate_grades()
print("Zufällig erzeugte Noten:", grades)

# Durchschnitt berechnen
average_grade = calculate_average(grades)
print("Gerundeter Durchschnitt nach Entfernung der Ausreißer:", average_grade)



