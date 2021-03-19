class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        current = None

        if self.head == None:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

        self.size += 1

    def pop(self):
        previous = None
        current = self.head

        while current.next:
            if current.next.next == None:
                current.next = None
            else:
                current = current.next
                
        if self.size == 1:
            self.head = None
            self.size -= 0

        self.size -= 1

    def peek(self):
        return self.head

    def isEmpty(self):
        if self.head is not None:
            return False
        else:
            return True

    def getAll(self):
        current = self.head
        while current:
            print(current)
            current = current.next


if __name__ == '__main__':
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.pop()
    stack.pop()
    stack.pop()

    stack.getAll()
