# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        t1 = head.next
        t2 = head.next.next
        head.next = None

        while t1 != None:
            t1.next = head
            head = t1
            t1 = t2

            if t2 != None:
                t2 = t2.next

        return head

        