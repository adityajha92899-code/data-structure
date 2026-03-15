# Node for Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete by value
    def delete_by_value(self, value):

        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    # Traverse
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")



        # Node for Doubly Linked List
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):

        new_node = DNode(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Insert after node
    def insert_after_node(self, prev_node, data):

        if prev_node is None:
            return

        new_node = DNode(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    # Delete at position
    def delete_at_position(self, position):

        temp = self.head

        for i in range(position):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Traverse
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")




        print("Singly Linked List")

sll = SinglyLinkedList()

sll.insert_at_beginning(10)
sll.insert_at_beginning(5)
sll.insert_at_end(20)

sll.traverse()

sll.delete_by_value(10)

print("After deletion:")
sll.traverse()


print("\nDoubly Linked List")

dll = DoublyLinkedList()

dll.insert_at_beginning(1)
dll.insert_at_beginning(2)

dll.traverse()

dll.insert_after_node(dll.head, 5)

print("After insert:")
dll.traverse()

dll.delete_at_position(1)

print("After delete:")
dll.traverse()