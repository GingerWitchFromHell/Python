
# Ferienwohnungen

# Schreibe ein Programm für einen Anbieter für Ferienwohnungen.
# Die Klasse soll "Wohnung" heissen.
# Diese soll den Namen der Wohnung, den Standort, die Anzahl der Betten,
# und den Preis pro Übernachtung enthalten.

# Bitte Attribute mit doppeltem Unterstrich und dazugehörige Getter & Setter erstellen.

# Teste danach die Klasse,
# indem du einige Wohnung-Objekte erzeugst und anschließend ihre Werte ausgibst.

class Wohnung:
    def __init__(self, name, standort, betten, preis):
        self.__name = name
        self.__standort = standort
        self.__betten = betten
        self.__preis = preis
    
    def get_name(self):
        return self.__name
    def get_standort(self):
        return self.__standort
    def get_betten(self):
        return self.__betten
    def get_preis(self):
        return self.__preis

    def set_name(self, name):
        self.__name = name
    def set_standort(self, standort):
        self.__standort = standort
    def set_betten(self, betten):
        self.__betten = betten
    def set_preis(self, preis):
        self.__preis = preis
    def __str__(self):
        return (f"Wohnung: {self.__name}, Standort: {self.__standort}, Betten: {self.__betten}, Preis: {self.__preis}")

wohnung1 = Wohnung("Casa Nera", "Berlin", 2, 50)
wohnung2 = Wohnung("Casa Blanca", "Hamburg", 3, 120)

print(wohnung1)
print(wohnung2)

wohnung1.set_preis(30)
wohnung2.set_betten(8)

print(wohnung1)
print(wohnung2)
