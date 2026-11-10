
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


linked_list = []
head = None
tail = None

print("===== LINKED LIST PROGRAM =====")

for i in range(5):
    letter = input("Enter a letter: ").upper()

    new_node = Node(letter)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

    linked_list.append(letter)

print("\nAdded:", " -> ".join(linked_list))

removed = []

while head is not None:
    removed.append(head.data)
    head = head.next

print("Removed:", " -> ".join(removed))
print("Linked List is empty.")
