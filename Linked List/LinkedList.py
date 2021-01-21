class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # def __str__(self) -> str:
    #     return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert at First
    def insertFirst(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    
    # Insert at Last
    def insertLast(self, data):
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

    # Insert at Index
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

    # Get at index
    def getAtIndex(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                print(current.data)
            count += 1
            current = current.next
        
        return None 

    # Remove at index
    def removeAtIndex(self, index):
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

    # Clear List Data
    def clearList(self):
        self.head = None
        self.size = 0
    # Get List Data
    def getAll(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


ll = LinkedList()
ll.insertFirst(600)
ll.insertFirst(500)
ll.insertFirst(400)
ll.insertFirst(300)
ll.insertFirst(200)
ll.insertFirst(100)

ll.removeAtIndex(2)

ll.getAll()
print(ll.size)
