class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.right is not None:
                temp = temp.right
            temp.right = new_node
            new_node.left = temp

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.right

    def display_reverse(self):
        temp = self.head
        if not temp:
            return
        while temp.right is not None:
            temp = temp.right
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.left

dll = DoublyLinkedList()
while True:
    data = int(input())
    if data >= 0:
        dll.append(data)
    else:
        break

print("Forward: ", end="")
dll.display()
print("\nReverse: ", end="")
dll.display_reverse()
