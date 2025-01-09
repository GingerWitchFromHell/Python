
# Adressendatei
# Teil 2 siehe unten !!!

# Folgende Adressendatei (Adressendatei.txt) ist gegeben:
"""
Frank;Meyer;Radolfzell;07732/43452
Peter;Rabe;Konstanz;07531/70021
Ottmar;Huber;Rosenheim;08031/7877-0
Anna;Rabe;Radolfzell;07732/2343
Oskar;Lindner;Konstanz;07531/890
Anna;List;München;089/3434544
Franziska;Huber;Rosenheim;08031/787878
Sarah;Rabe;Konstanz;07531/343454
"""
# Schreibe ein Python-Programm,
# das diese Adressen zeilenweise in der Form
# „Vorname Nachname, Ort, Telefonnummer” ausgibt.


# Teil 2
# Schreibe ein Python-Programm,
# das aus der Adressendatei eine Liste mit Zweiertupels erstellt,
# die jeweils aus dem ersten und letzten Element einer Adresse,
# also dem Vornamen und der Telefonnummer, bestehen:
"""
[('Frank', '07732/43452'), ('Peter', '07531/70021'), ('Ottmar',
'08031/7877-0'), ('Anna', '07732/2343'), ('Oskar', '07531/890'), ('
Anna', '089/3434544'), ('Anna', '089/3434544'), ('Franziska',
'08031/787878'), ('Sarah', '07531/343454')]
"""

def format_addresses(input_file):
    with open (input_file, "r") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) >= 4:
                first_name = parts[0]
                last_name = parts[1]
                city = parts[2]
                phone_number = parts[3]
                print(f"{first_name} {last_name}, {city}, {phone_number}")

format_addresses("C:/Users/Student/Desktop/python/Übungen/240_Adressendatei/Adressendatei.txt")

def create_tuples(input_file):
    result = []
    with open(input_file, "r") as file:
        for line in file:
            print("Zeile aus Datei: ", repr(line))
            parts = line.strip().split(";")
            print("Geteilte Zeile: ", parts)
            if len(parts) >= 4:
                first_name = parts[0]
                phone_number = parts[3]
                result.append((first_name, phone_number))
    return result

input_file = "C:/Users/Student/Desktop/python/Übungen/240_Adressendatei/Adressendatei.txt"
tuples = create_tuples(input_file)
print("Ergebnis der Zweiertupel-Liste: ")
print(tuples)


