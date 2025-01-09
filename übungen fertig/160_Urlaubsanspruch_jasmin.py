
#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruchs der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruchs
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.


def calculate_vacation_days(age, disability_percent, years_of_service):
    # Base vacation days
    vacation_days = 26

    # Rules for additional vacation days
    if age < 18:
        vacation_days = 30
    elif age > 55:
        vacation_days = 28

    if disability_percent >= 50:
        vacation_days += 5

    if years_of_service > 10:
        vacation_days += 2

    return vacation_days

# input
try:
    age = int(input("Geben Sie das Alter des Mitarbeiters ein: "))
    disability_percent = int(input("Geben Sie den Behinderungsgrad in Prozent ein (0, wenn keiner vorliegt): "))
    years_of_service = int(input("Geben Sie die Betriebszugehörigkeit in Jahren ein: "))

    # calculate and display vacation days
    vacation_days = calculate_vacation_days(age, disability_percent, years_of_service)
    print(f"Der Mitarbeiter hat Anspruch auf {vacation_days} Urlaubstage.")
except ValueError:
    print("Bitte geben Sie gültige Zahlen für Alter, Behinderungsgrad und Betriebszugehörigkeit ein.")
