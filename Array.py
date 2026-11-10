
letters = []

print("===== ARRAY PROGRAM =====")


for i in range(5):
    letter = input("Enter a letter: ").upper()
    letters.append(letter)

print("\nAdded:", " ".join(letters))

removed = []

while len(letters) > 0:
    letter = letters.pop(0)
    removed.append(letter)

print("Removed:", " ".join(removed))
print("Array is empty.")