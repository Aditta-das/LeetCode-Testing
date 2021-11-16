# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

# class MyLinkedList(object):
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def print(self):
#         itr = self.head
#         if itr is None:
#             return
#         llstr = ''
#         while itr:
#             llstr += str(itr.val) + '--> ' if itr.next else str(itr.val)
#             itr = itr.next
#         print(llstr)
        
#     def get(self, index):
#         if index < 0 and index >= self.size:
#             return -1
#         current = self.head
#         for i in range(0, index):
#             current = current.next
#         return current.val


#     def addAtHead(self, val):
#         node = ListNode(val, self.head)
#         self.head = node
        

#     def addAtTail(self, val):
#         if self.head is None:
#             self.head = ListNode(val, None)
#             return 
#         itr = self.head 
#         while itr.next:
#             itr = itr.next
#         itr.next = ListNode(val, None)
        

#     def addAtIndex(self, index, val):
#         if index < self.size:
#             return 
            
#         if index == 0:
#             self.addAtHead(val)
#             return
        
#         self.size = 0
#         itr = self.head
#         while itr:
#             if self.size == index - 1:
#                 node = ListNode(val, itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             self.size += 1

#     def deleteAtIndex(self, index):
#         if index < 0 or index >= self.size:
#             return 

#         if index == 0:
#             self.head = self.head.next
#             return 

#         self.size = 0
#         itr = self.head
#         while itr:
#             if self.size == index - 1:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             self.size += 1
        


# # Your MyLinkedList object will be instantiated and called as such:
# a = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]

# obj = MyLinkedList()
# obj.head = ListNode("MyList")
# obj.head.next = ListNode("MyList2")

# # obj.print()

# # print(obj.head.val)
# # print(obj.head.next.val)

# param_1 = obj.get(1)
# print(f"para: {param_1}")

# # print(param_1)
# obj.addAtHead("NewList")
# # print(obj.head.val)
# # print(obj.head.next.val)
# obj.addAtTail("Tail")
# # print(obj.head.next.next.next.val)
# obj.addAtIndex(index=2,val="indexadd")
# # obj.deleteAtIndex(2)
# # print(obj.head.val)
# # print(obj.head.next.val)
# # print(obj.head.next.next.val)
# # print(obj.head.next.next.next.val)
# obj.print()









# # class ListNode:
# #     def __init__(self, val):
# #         self.val = val
# #         self.next = None

# # class MyLinkedList(object):
# #     def __init__(self):
# #         self.head = None
# #         self.size = 0

# #     def get(self, index: int) -> int:
# #         if index < 0 or index >= self.size:
# #             return -1

# #         current = self.head

# #         for _ in range(0, index):
# #             current = current.next

# #         return current.val
    
# #     def addAtHead(self, val: int) -> None:
# #         self.addAtIndex(0, val)

# #     def addAtTail(self, val: int) -> None:
# #         self.addAtIndex(self.size, val)

# #     def addAtIndex(self, index: int, val: int) -> None:
# #         if index > self.size:
# #             return

# #         current = self.head
# #         new_node = ListNode(val)

# #         if index <= 0:
# #             new_node.next = current
# #             self.head = new_node
# #         else:
# #             for _ in range(index - 1):
# #                 current = current.next
# #             new_node.next = current.next
# #             current.next = new_node

# #         self.size += 1

# #     def deleteAtIndex(self, index: int) -> None:
# #         if index < 0 or index >= self.size:
# #             return

# #         current = self.head

# #         if index == 0:
# #             self.head = self.head.next
# #         else:
# #             for _ in range(0, index - 1):
# #                 current = current.next
# #             current.next = current.next.next
# #         self.size -= 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = headB if not n1 else n1.next
            n2 = headA if not n2 else n2.next
        return n1



