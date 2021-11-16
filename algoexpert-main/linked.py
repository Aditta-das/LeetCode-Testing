class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            return 
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data)+ ' ---> ' if itr.next else str(itr.data)
            itr = itr.next
        print(listr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_at(self, idx, data):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid")
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at(self, idx):
        if idx > self.get_length() or idx < 0:
            raise Exception("Invalid")
        
        if idx == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



list1 = LinkedList()
list1.head = Node("Monday")
list1.head.next = Node("Tuesday")
list1.head.next.next = Node("Wednesday")
list1.head.next.next.next = Node("Thrusday")
list1.insert_at_beginning("Sunday")
list1.insert_at_end("Friday")
list1.print()
print(list1.get_length())
list1.insert_at(3, "Saturday")
list1.remove_at(4)
list1.print()
list1.insert_values([1, 2, 3, 4])
list1.print()