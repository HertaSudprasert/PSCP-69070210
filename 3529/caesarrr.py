"""al gorithm"""

raw = input()

thing = [
    "what",
    "when",
    "why",
    "which",
    "this",
    "there",
    "where",
    "the",
    "is",
    "am",
    "are",
    "you",
    "we",
    "they",
    "he",
    "she",
    "it"
]

best_str = ""
best_score = -1

for i in range(1, 27):
    each_str = ""

    for j in raw:
        if j.islower():
            each_str += chr((ord(j) - ord('a') + i) % 26 + ord('a'))
        elif j.isupper():
            each_str += chr((ord(j) - ord('A') + i) % 26 + ord('A'))
        else:
            each_str += j

    words = each_str.lower().split()
    score = sum(1 for word in thing if word in words)

    if score > best_score:
        best_score = score
        best_str = each_str

print(best_str)
