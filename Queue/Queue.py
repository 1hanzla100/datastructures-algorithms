class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, data):
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
        return node

    def dequeue():
        current = self.head
        self.head = current.next
        self.size -= 1
        return current

    def peek():
        return self.head

    def isEmpty():
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
    qu = Queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)

    qu.getAll()
