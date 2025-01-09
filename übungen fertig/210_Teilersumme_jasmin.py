
# Teilersumme

"""
Schreibe eine Funktion, die überprüft, ob bei einer Zahl
die Summe aller Teiler kleiner als die Zahl ist.
Die Zahl selber soll hierbei nicht zu den Teilern zählen.

Bei 81 würde True zurückgegeben werden, da
1 + 3 + 9 + 27 = 40
und 40 < 81

Bei 80 würde False zurückgegeben werden, da
1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
und 106 > 80
"""

def is_proper_divisor_sum(number):
    divisors = []
    for i in range(1, number // 2 +1):
        if number % i == 0:
            divisors.append(i)
    divisor_sum = sum(divisors)
    result = divisor_sum < number
    print(
        f"Die Zahl {number} hat die Teiler {divisors}. Ihre Summe beträgt {divisor_sum}. "
        f"Daher ist das Ergebnis: {result}."
    )

    return result

# Testfälle
is_proper_divisor_sum(81)  
is_proper_divisor_sum(80)  
is_proper_divisor_sum(12)  
