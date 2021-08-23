# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
	def removeNthFromEnd(self, head, n):
		slow = fast = head
		for _ in range(n):
			fast = fast.next
		if not fast:
			return slow.next

		while fast.next:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
		return head

head = [1,2,3,4,5]
n = 2
a = ListNode()
b = Solution()
print(b.removeNthFromEnd(head, n))