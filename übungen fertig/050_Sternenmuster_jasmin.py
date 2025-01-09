
# Sternenmuster

# Schreibe ein Python-Programm,
# das folgende Sternchen-Muster auf den Bildschirm schreibt:

"""
* * * *
* * * *
* * * *

*
* *
* * *
* * * *
* * * * *

      *
    * * *
  * * * * *
* * * * * * *
"""


for i in range(4):
    print("***")

print()  


for i in range(1, 5):
    print("*" * i)

print()  


for i in range(4, 0, -1):
    print("*" * i)

print()  


for i in range(1, 5):
    print(" " * (4 - i) + "*" * i)
