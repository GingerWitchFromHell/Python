
# Korrektes Datum

"""
Die Meyer GmbH benötigt ein Modul,
das ein beliebiges Datum auf Korrektheit prüft.
Ist das zu prüfende Datum korrekt,
so ist die Variable datok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02.1999 - datok: 0
29.02.2000 - datok: 1
13.05.2000 - datok: 1
32.05.2000 - datok: 0
24.13.2000 - datok: 0

Für die Jahre gilt: jahr > 1900 UND jahr < 2100
"""

def is_valid_date(day, month, year):
    # Check year range
    if not (1900 < year < 2100):
        return 0
    # Check month range
    if not (1 <= month <= 12):
        return 0
    # Days in each month (default, without leap year adjustment)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Adjust for leap year
    if is_leap_year(year):
        days_in_month[1] = 29  # February in leap year
    # Check day range
    if not (1 <= day <= days_in_month[month - 1]):
        return 0
    # If all checks pass, the date is valid
    return 1

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to get input from the user and validate the date
def get_user_date():
    try:
        day = int(input("Enter the day: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        # Validate the entered date
        datok = is_valid_date(day, month, year)
        if datok:
            print(f"The date {day:02}.{month:02}.{year} is valid!")
        else:
            print(f"The date {day:02}.{month:02}.{year} is NOT valid!")
    except ValueError:
        print("Invalid input! Please enter integers for day, month, and year.")

# Test cases
test_dates = [(29, 2, 1999), (29, 2, 2000), (13, 5, 2000), (32, 5, 2000), (24, 13, 2000)]
print("Testing predefined dates:")
for day, month, year in test_dates:
    datok = is_valid_date(day, month, year)
    print(f"Date: {day:02}.{month:02}.{year}, datok: {datok}")

# Allow user input
print("\nNow you can enter your own date to validate:")
get_user_date()
