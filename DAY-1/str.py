# str data type

# Declaring and initializing string variables

text = "Sakshyam Paudel"
string_with_spaces = "  Python is friendly and Powerful Programming Language  "


# Calculating length of a string
print(f"\nLength: {len(text)}")

# Converting a string value to uppercase
print(f"\nUpper String: {text.upper()}")

# Converting a string value to lowercase
print(f"\nLower String: {text.lower()}")

# Counting the number of times a specific character appears in a string
print(f"\nCount the Letter 'a': {text.count('a')}")      # does not count 'A'

# Finding the position of a specific character in a string
print(f"\nPosition of letter 'S': {text.find('S')}")   


# Removing spaces from the beginning and the end of a string
print(f"\nBefore Removing Spaces: {string_with_spaces}")
print(f"\nAfter Removing Spaces: {string_with_spaces.strip()}")


# Splitting a string into a list
sentence = "SAKSHYAM PAUDEL"
print(f"\nOriginal sentence: {sentence}")
print(f"\nString method split: {sentence.split()}")




