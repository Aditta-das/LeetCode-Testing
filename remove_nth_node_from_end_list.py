# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head
        
        while current:
            length += 1
            current = current.next
        nth = length-(n-1)
        prev = None
        i = 0
        while current:
            i+=1
            if i == nth and prev == None:
                return head.next
            elif i == nth:
                prev.next = current.next
                break
            prev = current
            current = current.next  
        return head


head = [1, 2, 3, 4, 5]
n = 2
a = Solution()
print(a.removeNthFromEnd(head, n))
