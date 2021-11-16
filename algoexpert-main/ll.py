class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def print(self):
        itr = self.head
        if itr is None:
            return 
        llstr = ''
        while itr:
            llstr += str(itr.val) + ' ---> ' if itr.next else str(itr.val)
            itr = itr.next
        print(llstr)
    
    def addAtIndex(self, index, val):
        if index > self.size:
            return
        
        current = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def addAtHead(self, val):
        self.addAtIndex(0, val)
    
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

a = LinkedList()
a.addAtHead("Hello")
a.addAtIndex(1, "I")
a.addAtIndex(2, "Am")
a.addAtIndex(3, "Nishad")
a.addAtTail("Tail")
a.print()
a.deleteAtIndex(2)
a.print()

