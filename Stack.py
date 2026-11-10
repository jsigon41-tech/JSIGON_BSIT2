
stack = []

print("===== STACK PROGRAM =====")

for i in range(5):
    letter = input("Enter a letter: ").upper()
    stack.append(letter)

print("\nAdded (Push):", " ".join(stack))

removed = []

while len(stack) > 0:
    letter = stack.pop()
    removed.append(letter)

print("Removed (Pop):", " ".join(removed))
print("Stack is empty.")