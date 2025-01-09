
# Begrüßung

# Es soll eine Begrüßung in Abhängigkeit zur Uhrzeit ausgegeben werden.

# Zwischen 22Uhr und 5Uhr: Gute Nacht
# Vor 11Uhr: Guten Morgen
# Vor 15Uhr: Mahlzeit
# Vor 18Uhr: Guten Nachmittag
# Vor 22Uhr: Guten Abend

# Benutze zum Testen randint(0, 23),
# um eine Zahl von 0 bis 23 zu erzeugen.

import random
from random import randint

# Zufällige Uhrzeit generieren
Uhrzeit = randint(0, 23)

# Überprüfen der Uhrzeit und passende Begrüßung
if Uhrzeit in (22, 23, 0, 1, 2, 3, 4, 5):
    print("Es ist", Uhrzeit, "Uhr. Gute Nacht.")
elif Uhrzeit in (6, 7, 8, 9, 10):
    print("Es ist", Uhrzeit, "Uhr. Guten Morgen.")
elif Uhrzeit in (11, 12, 13, 14):
    print("Es ist", Uhrzeit, "Uhr. Mahlzeit!")
elif Uhrzeit in (15, 16, 17):
    print("Es ist", Uhrzeit, "Uhr. Guten Nachmittag.")
elif Uhrzeit in (18, 19, 20, 21):
    print("Es ist", Uhrzeit, "Uhr. Guten Abend.")
else:
    print("Es ist", Uhrzeit, "Uhr. Das passt nicht.")
