from element import Element




class demolinkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        NewElement = element(value)

        if self.head is None:
            self.head = NewElement
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = NewElement
        new_node.prev = current

    def ShowAll(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

