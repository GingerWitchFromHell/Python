
# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurückgeben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.

Teste die Funktion:
print(berechne_kosten(2))  # 200 €
print(berechne_kosten(2, 2))  # 4 €
print(berechne_kosten(2, 2, '$'))  # 4 $
print(berechne_kosten(2, waehrung='$'))  # 200 $
"""

def berechne_kosten(preis, anzahl=100, waehrung='€'):
    """
    Berechnet die Gesamtkosten basierend auf Preis, Anzahl und Währung.
    :param preis: Einzelpreis des Artikels
    :param anzahl: Anzahl der Artikel (Standardwert: 100)
    :param waehrung: Währung der Kosten (Standardwert: €)
    :return: String mit Gesamtkosten und Währung
    """
    kosten = preis * anzahl
    return f"{kosten} {waehrung}"


print(berechne_kosten(2))               
print(berechne_kosten(2, 2))            
print(berechne_kosten(2, 2, '$'))       
print(berechne_kosten(2, waehrung='$')) 
