
# Eigene Klasse

# Suche dir ein Objekt aus deiner Umgebung/Fantasie.
# Schreibe eine eigene Klasse dazu mit
# Konstruktor
# Objekt-Attributen
# Objekt-Methoden
# Statischem Attribut
# ToString-Methode - __str__()
# Entsprechende Getter & Setter

# Erzeuge dann einige Objekte, verändere sie und lasse sie wieder anzeigen.

class Character:
    world = "Middle Earth"
    def __init__(self, name, folk, clan, age, weapon):
        self.__name = name
        self.__folk = folk
        self.__clan = clan
        self.__age = age
        self.__weapon = weapon

    def __str__(self):
        return f"{self.__name}, a {self.__folk}, from {self.__clan}, {self.__age} years old, wields {self.__weapon}."
    def get_name(self):
        return self.__name
    def get_folk(self):
        return self.__folk
    def get_clan(self):
        return self.__clan
    def get_age(self):
        return self.__age
    def get_weapon(self):
        return self.__weapon

    def set_name(self, name):
        self.__name = name
    def set_folk(self, folk):
        self.__folk = folk
    def set_clan(self, clan):
        self.__clan = clan
    def set_age(self, age):
        self.__age = age
    def set_weapon(self, weapon):
        self.__weapon = weapon


character1 = Character("Gimli, Son of Gloin", "Dwarf", "The Lonely Mountain", 139, "Axe")
character2 = Character("Galadriel", "Elf", "the House of Finwe", 3000, "Sword")
character3 = Character("Aragorn", "Human", "The Dúnedain", 87, "Sword")

# ergebnis
print(character1, character2, character3, sep='\n')
# testing setter and getter
print("Name: ", character3.get_name())
character3.set_weapon("Andúril")
print(character3)
