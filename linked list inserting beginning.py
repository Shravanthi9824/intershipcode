class node:#insert at end
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
obj=LinkedList()
obj.insert_at_beginning(5)
obj.insert_at_beginning(8)
obj.insert_at_beginning(7)
obj.display()

