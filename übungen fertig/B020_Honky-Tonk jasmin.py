
# Honky-Tonk

# Simuliere das Spiel Honky-Tonk.
# Bei diesem Spiel bezahlt der Spieler pro Runde einen Euro als Einsatz.
# Er darf nun drei Würfel werfen.
# Zeigt mindestens ein Würfel eine sechs,
# so erhält er zunächst den Einsatz zurück.
# Zudem erhält er für jede geworfene Sechs
# einen Euro als Gewinn ausbezahlt.
# Liegt keine Sechs, so verliert er den Einsatz.
# Starte mit einem Kapital von 1000 Euro und simuliere 1000 Runden.

import random
from random import randint

kapital = 1000
runden = 1000

for runde in range(1, runden+1):
    kapital -= 1
    würfel1 = random.randint(1,7)
    würfel2 = random.randint(1,7)
    würfel3 = random.randint(1,7)
    sechsen = [würfel1, würfel2, würfel3].count(6)
    if sechsen > 0:
        kapital += 1 + sechsen
        print(f"Runde {runde}: Du hast {sechsen} Sechsen geworfen! Kapital: {kapital} €")
    else:
        print(f"Runde {runde}: Keine Sechs geworfen. Kapital: {kapital} €")
print(f"Nach {runden} Runden beträgt dein Kapital: {kapital} €")


