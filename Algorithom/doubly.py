class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val
    
    def print_forward(self):
        itr = self.head
        if itr is None:
            return ("Linked List Is Empty") 

        llstr = ''
        while itr:
            llstr += str(itr.val) + ' ---> ' if itr.next else str(itr.val)
            itr = itr.next
        print(llstr)  

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
        else:
            node = Node(val, self.head, None)
            self.head.prev = node
            self.head = node
        
    def addAtTail(self, val):
        if self.head is None:
            self.head = Node(val, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None, itr)
        

    def addAtIndex(self, index, val):
        if index > self.size or index < 0:
            return
        if index == 0:
            self.addAtHead(val) 
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            
            new_node = Node(val)
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index):
        if index < 0 or index > self.size:
            return 
        
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(5)
obj.addAtHead(6)
obj.addAtTail(val=7)
obj.addAtTail(val=12)
# obj.print_forward()
obj.get(index=0)
obj.print_forward()
obj.addAtIndex(index=3,val=10)
# obj.deleteAtIndex(index=0)
obj.print_forward()