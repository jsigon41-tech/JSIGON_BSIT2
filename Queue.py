
from collections import deque

queue = deque()

print("===== QUEUE PROGRAM =====")

for i in range(5):
    letter = input("Enter a letter: ").upper()
    queue.append(letter)

print("\nAdded:", " ".join(queue))

removed = []

while len(queue) > 0:
    letter = queue.popleft()
    removed.append(letter)

print("Removed:", " ".join(removed))
print("Queue is empty.")