
# Sekunden seit Mitternacht

# Ermittel, wie viele Sekunden genau jetzt (zur Ausführung des Programms)
# seit der letzten Mitternacht vergangen sind.

from datetime import datetime

jetzt = datetime.now()

mitternacht = datetime(jetzt.year, jetzt.month, jetzt.day, 0, 0, 0)
differenz = jetzt - mitternacht

sekunden_seit_mitternacht = int(differenz.total_seconds())

print(f"Seit Mitternacht sind {sekunden_seit_mitternacht} Sekunden vergangen. ")


