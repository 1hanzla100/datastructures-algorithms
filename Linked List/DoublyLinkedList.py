class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def addLast(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

        self.size += 1

    def insertAtIndex(self, data, index):
        if index > 0 and index > self.size:
            return None

        if index == 0:
            self.addFirst(data)

        node = Node(data)
        current = self.head
        previous = None
        count = 0
        while count < index:
            previous = current
            count += 1
            current = current.next

        node.next = current
        node.prev = previous
        previous.next = node

        if current is not None:
            current.prev = node

        self.size += 1

    def getByIndex(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next

        return None

    def getAll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # def getMiddle(self):
    #     current = self.head
    #     count = 0
    #     while current:
    #         current = current.next
    #         count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    ll.addLast(4)
    ll.insertAtIndex(5, 4)
    ll.insertAtIndex(6, 5)
    ll.insertAtIndex(7, 6)
    ll.
    print(ll.getByIndex(4).next.next.next)
