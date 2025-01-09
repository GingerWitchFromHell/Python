
# Römische Zahlen

# Schreibe ein Python-Programm,
# das eine beliebige römische Zahl in eine „gewöhnliche” Dezimalzahl umrechnet.

# Römische zu Dezimal
def roman_to_decimal(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    decimal = 0
    prev_value = 0
    
    for char in reversed(roman): 
        current_value = roman_values[char]
        if current_value < prev_value:  
            decimal -= current_value
        else:  
            decimal += current_value
        prev_value = current_value
    
    return decimal

# Dezimal zu Römische
def decimal_to_roman(number):
    roman_pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ""
    for value, symbol in roman_pairs:
        while number >= value:
            roman += symbol
            number -= value
    return roman

# Hauptprogramm mit Eingabemöglichkeit
def main():
    print("Willkommen zum Römische-Dezimal-Konverter!")
    print("1: Römische Zahl in Dezimalzahl umrechnen")
    print("2: Dezimalzahl in Römische Zahl umrechnen")
    choice = input("Wähle eine Option (1 oder 2): ")

    if choice == "1":
        roman = input("Gib eine römische Zahl ein: ").upper()
        try:
            decimal = roman_to_decimal(roman)
            print(f"Die römische Zahl {roman} entspricht der Dezimalzahl {decimal}.")
        except KeyError:
            print("Ungültige römische Zahl!")
    elif choice == "2":
        try:
            number = int(input("Gib eine Dezimalzahl ein: "))
            if number <= 0 or number >= 4000:
                print("Die Zahl muss zwischen 1 und 3999 liegen.")
            else:
                roman = decimal_to_roman(number)
                print(f"Die Dezimalzahl {number} entspricht der römischen Zahl {roman}.")
        except ValueError:
            print("Bitte eine gültige Dezimalzahl eingeben!")
    else:
        print("Ungültige Auswahl!")


if __name__ == "__main__":
    main()
