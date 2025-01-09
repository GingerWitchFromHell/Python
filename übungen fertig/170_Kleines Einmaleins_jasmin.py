
# Kleines Einmaleins

"""
Schreibe ein Programm,
welches das kleine Einmaleins formatiert ausgibt:

001 002 003 004 005 006 007 008 009 010
002 004 006 008 010 012 014 016 018 020
003 006 009 012 015 018 021 024 027 030
004 008 012 016 020 024 028 032 036 040
005 010 015 020 025 030 035 040 045 050
006 012 018 024 030 036 042 048 054 060
007 014 021 028 035 042 049 056 063 070
008 016 024 032 040 048 056 064 072 080
009 018 027 036 045 054 063 072 081 090
010 020 030 040 050 060 070 080 090 100
"""
# Small Multiplication Table without Leading Zeros

# Function to generate and display the small multiplication table
def print_multiplication_table():
    # Loop through rows (1 to 10)
    for row in range(1, 11):
        # Initialize an empty list for the current row
        current_row = []
        # Loop through columns (1 to 10)
        for col in range(1, 11):
            # Calculate the product
            product = row * col
            # Format the product with consistent spacing
            formatted_product = f"{product:>3}"  # Right-aligned, 3-character width
            # Append formatted product to the current row
            current_row.append(formatted_product)
        # Print the row, joining values with a space
        print(" ".join(current_row))

# Run the function
print_multiplication_table()
