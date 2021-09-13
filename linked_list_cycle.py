# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hare, tortoise = head, head
        while hare != None and hare.next != None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False

head = [3,2,0,-4]
pos = 1
a = Solution()
print(a.hasCycle(head))