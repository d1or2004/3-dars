class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):  # listni boshiga element qo'shish
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def insert(self, prev_node, new_data):  # Ixtiyoriy nuqtaga son qo'shish
        if prev_node is None:
            print("List bosh ")

        new_son = Node(new_data)
        new_son.next = prev_node.next
        prev_node.next = new_son

    def append(self, new_data):
        new_data = Node(new_data)
        if new_data is None:  # list bo'sh bo'lgande
            self.head = new_data

        last = self.head
        while last.next:
            last = last.next
        last.next = new_data


a = Node(1)
b = Node(2)
c = Node(0)
d = Node(4)
g = Node(6)
ll = LinkedList()
ll.head = a
a.next = b
b.next = c
c.next = d
d.next = g
ll.push(2)
ll.printList()
