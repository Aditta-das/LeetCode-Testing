# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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

    def hasCycle(self, head):
        hare, tortoise = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False
