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

        else:
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

    def getMiddle(self):
        current = self.head
        count = 0
        middle = self.size // 2
        while current:
            if count == middle:
                return current

            current = current.next
            count += 1

    def contains(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True

            current = current.next

        return False

    def indexOf(self, data):
        current = self.head
        count = 0
        while current != None:
            if current.data == data:
                return count
            current = current.next
            count += 1

        return None

    def deleteByIndex(self, index):
        if index > 0 and index > self.size:
            return None

        current = self.head
        count = 0

        if index == 0:
            self.head = current.next
            self.head.prev = None

        else:
            while count < index:
                count += 1
                current = current.next

            current.prev.next = current.next

        self.size -= 1

    def deleteByData(self, data):
        current = self.head

        if current is not None:
            if current.data == data:
                self.head = current.next
                self.head.prev = None
                current = None
                return

        else:
            while current is not None:
                if current.data == data:
                    break
                current = current.next

            if current == None:
                return None

            current.prev.next = current.next

            current = None

        self.size -= 1

    def deleteAll(self):
        self.head = None
        self.size = 0

    def reverse(self):
        current = self.head
        while current is not None:
            prev = current.prev
            next = current.next
            current.prev = current.next
            current.next = prev
            current = next

        self.head = prev

    def removeDuplicates(self):
        current = second = self.head
        while current is not None:
            while second.next is not None:
                if second.next.data == current.data:
                    second.next = second.next.next
                    self.size -= 1
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(1)
    ll.addLast(3)
    ll.getAll()
