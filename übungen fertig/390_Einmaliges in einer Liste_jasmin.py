
# Einmaliges in einer Liste

"""
Schreibe eine Funktion,
die eine Liste mit neun zufälligen Zahlen befüllt und zurückgibt.
Dabei sollen vier Zahlen doppelt vorkommen und eine Zahl nur einmal.

Dann mische die Liste per random.shuffle() und schreibe eine zweite Funktion,
die aus dieser Liste die Zahl findet, die nur einmal vorkommt.
"""

import random


def generate_list():
    
    total_numbers = int(input("Wie viele Zahlen sollen generiert werden? "))
    if total_numbers < 2:
        raise ValueError("Die Anzahl der Zahlen muss mindestens 2 betragen.")
    
    
    n_unique = random.randint(1, total_numbers // 2)  
    n_duplicates = total_numbers - n_unique  
    
    unique_numbers = random.sample(range(1, 100), n_unique)  
    duplicates = random.choices(unique_numbers, k=n_duplicates)  
    
    numbers = unique_numbers + duplicates  
    random.shuffle(numbers)  
    return numbers

def find_unique(numbers):
    unique = [num for num in numbers if numbers.count(num) == 1]  
    return unique

numbers = generate_list()
print("Generierte Liste: ", numbers)
unique_numbers = find_unique(numbers)
print("Einzigartige Zahlen sind: ", unique_numbers)
