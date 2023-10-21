f = open("books/frankenstein.txt", "r")
words = f.read()
word_count = len(words.split())

print(f"Word Count: {word_count}")

letter_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for char in words:
    if char.lower() in letter_count:
        letter_count[char.lower()] += 1

print(letter_count)

print("Begin report of books/frankenstein.txt")
print(f"{word_count} words found in the document")

char_list = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
sortdict = dict(char_list)

for letter in sortdict:
    print(f"The '{letter}' character was found {sortdict[letter]} times.")
