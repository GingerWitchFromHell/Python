
# Doppelte Zahl

"""
Schreibe eine Funktion, die überprüft,
ob in einer Liste mit Zahlen zwei Zahlen gleich sind.
Der Funktion wird die Liste übergeben
und sie soll True zurückgeben, wenn es Doppelte gibt
und ansonsten soll die Funktion False zurückgeben.
"""

def has_duplicates(numbers):
    seen = set()  
    for number in numbers:
        print(f"Überprüfe Zahl: {number}, bereits gesehen: {seen}")  
        if number in seen:  
            print(f"Doppelte Zahl gefunden: {number}")  
            return True  
        seen.add(number)  
    print("Keine doppelten Zahlen gefunden.") 
    return False  

# Testfälle
print(has_duplicates([1, 2, 3, 4]))  
print(has_duplicates([1, 2, 3, 4, 2])) 

