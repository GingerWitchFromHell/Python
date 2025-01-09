"""
u_steuer.py
Das Programm zur Berechnung des monatlich zu zahlenden Steuerbetrags soll verändert werden.
Schreiben Sie ein Programm zur Berechnung des monatliches zu zahlenden Steuerbetrags.
Der Anwender wird dazu aufgefordert, sein monatliches Bruttogehalt und sein Familienstandeinzugeben.
Anschließend wird sein Steuerbetrag nach der folgenden Steuertabelle berechnet:
Gehalt      Familienstand   Steuersatz
>4000 €     ledig           26%
>4000 €     verheiratet     22%
<= 4000 €   ledig          22%
<= 4000 €   verheiratet     18%
Die Ausgabe kann z.B. wie folgt aussehen:
Geben Sie Ihr Bruttogehalt in Euro ein:3000
Geben Sie Ihren Familienstand ein(1 = ledig; 2 = verheiratet) 2
Es ergibt sich ein Steuerbetrag von 540. 0Euro
Oder sie kann so aussehen:
Geben Sie Ihr Bruttogehalt in Euro ein:5000
Geben Sie Ihren Familienstand ein(1 = ledig; 2 = verheiratet)1
Es ergibt sich ein Steuerbetrag von 1300.0 Euro
"""

def berechnen_steuer(gehalt, familienstand):
    """Berechnet den monatlichen Steuerbetrag basierend auf Gehalt und Familienstand.

    Args:
        gehalt (float): Das monatliche Bruttogehalt in Euro.
        familienstand (int): 1 für ledig, 2 für verheiratet.

    Returns:
        float: Der monatliche Steuerbetrag in Euro.
    """

def berechnen_steuer(gehalt, familienstand):
    """Berechnet den monatlichen Steuerbetrag basierend auf Gehalt und Familienstand.

    Args:
        gehalt (float): Das monatliche Bruttogehalt in Euro.
        familienstand (int): 1 für ledig, 2 für verheiratet.

    Returns:
        float: Der monatliche Steuerbetrag in Euro.
    """

    if gehalt > 4000:
        if familienstand == 1:
            steuersatz = 0.26
        else:
            steuersatz = 0.22
    else:
        if familienstand == 1:
            steuersatz = 0.22
        else:
            steuersatz = 0.18

    steuerbetrag = gehalt * steuersatz
    return steuerbetrag

if __name__ == "__main__":
    gehalt = float(input("Geben Sie Ihr Bruttogehalt in Euro ein: "))
    familienstand = int(input("Geben Sie Ihren Familienstand ein (1 = ledig; 2 = verheiratet): "))

    steuer = berechnen_steuer(gehalt, familienstand)
    print(f"Es ergibt sich ein Steuerbetrag von {steuer:.2f} Euro.")




