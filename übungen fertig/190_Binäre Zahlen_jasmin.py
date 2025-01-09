
# Binäre Zahlen

# Schreibe ein Skript, das alle Zahlen von 0 bis 255 binär schreibt:
# Beachte die Leerzeichen zwischen den Ziffern!

"""
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 1 0 0
...
...
...
1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1
"""

for number in range(256):
    pass
    binary = bin(number)
    binary = binary[2:].zfill(8)
    formatted_binary = " ".join(binary)
    print(formatted_binary)
