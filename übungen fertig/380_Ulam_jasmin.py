
# Ulam

# Berühmt ist die (3a + 1)-Folge des amerikanischen Mathematikers Ulam.
# Sie ist durch folgenden Algorithmus definiert:
#
# 1. Beginne mit einem Startwert a.
# 2. Wenn a == 1 ist, stoppe.
# 3. Ist a gerade, setze a = a/2,
#    sonst setze a = 3*a + 1 und fahre mit 2. fort.
#
# Bis heute weiß man nicht,
# ob die Ulam-Folge bei jedem Startwert a zum Stoppen kommt.
#
# Entwickle zu dem Algorithmus eine Funktion
# und teste sie mit verschiedensten Startwerten für a.

def ulam_sequence_with_steps(start):
    if start <= 0:
        raise ValueError("Der Startwert muss eine positive ganze Zahl sein.")
    
    sequence = [start]
    steps = 0
    while start != 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
        sequence.append(start)
        steps += 1
    return sequence, steps
# Testfälle
folge, schritte = ulam_sequence_with_steps(6)
folge, schritte = ulam_sequence_with_steps(12)
folge, schritte = ulam_sequence_with_steps(27)
print(f"Folge: {folge}, Schritte: {schritte}")


