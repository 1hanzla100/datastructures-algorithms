class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def addLast(self, data):
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

    def insertAtIndex(self, data, index):
        if index > 0 and index > self.size:
            return None

        if index == 0:
            self.insertFirst(data)

        else:
            node = Node(data)
            previous = None
            current = self.head
            count = 0
            while count < index:
                previous = current
                count += 1
                current = current.next

            node.next = current
            previous.next = node

        self.size += 1

    def getByIndex(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                print(current.data)
            count += 1
            current = current.next

        return None

    def getAll(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    def getMiddle(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1

        middle = count // 2
        count = 0
        current = self.head
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

        previous = None
        current = self.head
        count = 0

        if index == 0:
            self.head = current.next

        else:
            while count < index:
                count += 1
                previous = current
                current = current.next

            previous.next = current.next

        self.size -= 1

    def deleteByData(self, data):
        current = self.head
        prev = None

        if current is not None:
            if current.data == data:
                self.head = current.next
                current = None
                return

        while current is not None:
            if current.data == data:
                break
            prev = current
            current = current.next

        if current == None:
            return None

        prev.next = current.next
        current = None

        self.size -= 1

    def deleteAll(self):
        self.head = None
        self.size = 0

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
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
                    second = second.next
            current = second = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.addLast(100)
    ll.addLast(200)
    ll.addLast(400)
    ll.addLast(500)
    ll.insertAtIndex(300, 2)
    
    ll.addLast(200)
    ll.addLast(400)
    ll.addLast(300)
    # ll.getByIndex(1)
    # print(ll.getMiddle())
    # print(ll.contains(500))
    # print(ll.indexOf(500))
    # ll.deleteAll()
    # ll.deleteByIndex(3)
    # ll.deleteByData(100)
    # ll.reverse()
    # ll.removeDuplicates()
    ll.getAll()
