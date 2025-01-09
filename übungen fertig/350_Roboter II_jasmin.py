
# Roboter II

# In dieser Aufgabe geht wieder um eine Roboterklasse.
# Uns interessiert nicht das Aussehen und die Beschaffenheit eines Roboters,
# sondern nur seine Position in einer imaginären „Landschaft”,
# die zweidimensional sein soll
# und durch ein Koordinatensystem beschrieben werden kann.
# Ein Roboter hat also zwei Attribute für die x- und die y-Koordinate.
# Es empfiehlt sich, diese Informationen in einer 2er-Liste zusammenzufassen,
# also beispielsweise position = [3, 4],
# wobei dann 3 der x-Position und 4 der y-Position entspricht.
# Der Roboter ist in eine der vier Richtungen „west”, „south”, „east”
# oder „north” orientiert, was wir in einem Attribut speichern wollen.
# Außerdem sollten unsere Roboter auch Namen haben.
# Allerdings dürfen die Namen nicht länger als 10 Zeichen sein.
# Sollte jemand versuchen,
# dem Roboter einen längeren Namen zuzuweisen,
# soll der Name auf 10 Zeichen abgeschnitten werden.
# Um die Roboter im Koordinatensystem bewegen zu können,
# benötigen wir eine move()-Methode.
# Die Methode erwartet einen Parameter „distance”,
# der angibt, um welchem Betrag sich der Roboter in Richtung
# der eingestellten Orientierung bewegen soll.
# Wird ein Roboter x beispielsweise mit x.move(10) aufgerufen
# und ist dieser Roboter östlich orientiert,
# also x.orientation == "east", und ist [3, 7] die aktuelle Position des
# Roboters, dann bewegt er sich 10 Felder östlich
# und befindet sich anschließend in Position [13, 7].


class Robot:
    def __init__(self, name, position, orientation):
        # Name: Maximal 10 Zeichen
        if len(name) > 10:
            name = name[:10]
        self.name = name
        
        # Position und Orientierung
        self.position = position 
        self.orientation = orientation  # "north", "south", "east", "west"
    
    def move(self, distance):
        
        if self.orientation == "north":
            self.position[1] += distance  # y erhöhen
        elif self.orientation == "south":
            self.position[1] -= distance  # y verringern
        elif self.orientation == "east":
            self.position[0] += distance  # x erhöhen
        elif self.orientation == "west":
            self.position[0] -= distance  # x verringern
    
    def __str__(self):
        
        return f"Robot {self.name}: Position {self.position}, Facing {self.orientation}"

# Roboter erstellen
robot1 = Robot("C3PO", [3, 4], "east")
robot2 = Robot("R2D2", [0, 0], "north")

# Roboter anzeigen
print(robot1)
print(robot2)

# Roboter bewegen
robot1.move(10)  
robot2.move(5)   

# Positionen nach Bewegung
print("After movement:")
print(robot1)
print(robot2)
