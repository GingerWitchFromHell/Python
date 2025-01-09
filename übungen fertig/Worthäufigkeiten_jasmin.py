
# Worthäufigkeiten

# Von den Textdokumenten sollen jeweils die Worthäufigkeiten ermittelt werden.
# Die Ergebnisse sollen sortierte Listen (absteigend nach Häufigkeit)
# von Tupeln der Form (wort, häufigkeit) sein.
# Dabei ist wort ein Wort, das im Text vorkommt
# und häufigkeit die Anzahl der Vorkommen dieses Wortes im Text.

"""
print(ermittleWorthaeufigkeitenAusDatei('Lorem Ipsum.txt'))
print(ermittleWorthaeufigkeitenAusDatei('Kafka.txt'))
print(ermittleWorthaeufigkeitenAusDatei('Werther.txt'))
"""

import string

# Function to determine word frequencies from a file
def get_word_frequencies_from_file(filename):
    try:
        # 1. Read
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # 2. Clean text
        text = text.lower()  # Convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

        # 3. Count words
        words = text.split()  # Split into words
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        # 4. Sort
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_word_counts

    except FileNotFoundError:
        return f"The file '{filename}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"


# display
def display_word_frequencies_per_file(file_names, top_n=None):
    for file_name in file_names:
        print(f"Word Frequencies for '{file_name}':")
        try:
            word_counts = get_word_frequencies_from_file(file_name)
            if isinstance(word_counts, str):  # If an error string was returned
                print(word_counts)
            else:
                for i, (word, count) in enumerate(word_counts):
                    print(f"{i + 1}. {word}: {count}")
                    if top_n and i + 1 >= top_n:  # Limit to Top-N words
                        break
        except Exception as e:
            print(f"Error processing file '{file_name}': {e}")
        print("\n")  # Blank line between files


# Example
file_names = ['Lorem Ipsum.txt', 'Kafka.txt', 'Werther.txt']
display_word_frequencies_per_file(file_names, top_n=10)  # Show only the top 10 words
