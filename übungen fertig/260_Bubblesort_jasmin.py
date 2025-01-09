
# Bubblesort

"""
Schreibe eine Funktion,
der man eine Liste mit beliebig vielen Zahlen als Werten übergeben kann
und die diese Liste sortiert und zurückgibt.

Benutze hierzu den Bubblesort-Algorithmus.
Bei diesem wird die Liste durchlaufen
und jede Zahl mit der jeweils nachfolgenden Zahl verglichen.
Wenn die nachfolgende Zahl kleiner ist,
werden die Zahlen getauscht.
Die Liste wird so lange durchlaufen,
bis bei einem Durchlauf keine Zahlen getauscht werden müssen.
"""

def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

unsorted_list = [34, 25, 15, 11, 78, 54, 978, 13, 1, 7, 34, 7785]
sorted_list = bubblesort(unsorted_list)
print("Sortierte Liste: ", sorted_list)
