
# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist,
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

max_limit = 1_000_000_000

n = 1
while factorial(n) <= max_limit:
    n += 1

print(f"The largest number whose factorial is below {max_limit} is {n - 1}")
