
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.

import random
from random import randint
x = randint(1, 10000)
y = randint(1, 10000)
print(x)
print(y)
if x >= y:
    print(x, "ist größer als ", y, ". ")
elif x <= y:
    print(x, "ist kleiner als ", y, ". ")
else:
    print("Die Zahlen sind gleich groß. ")
