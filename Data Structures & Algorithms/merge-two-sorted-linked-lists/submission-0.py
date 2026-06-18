# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        p1, p2 = list1, list2

        if list1.val <= list2.val:
            h = list1
            p1 = list1.next
        else:
            h = list2
            p2 = list2.next

        t = h

        while p1 != None and p2 != None:

            if p1.val <= p2.val:
                t.next = p1
                p1 = p1.next
            else:
                t.next = p2
                p2 = p2.next

            t = t.next

        if p1 == None:
            t.next = p2
        elif p2 == None:
            t.next = p1

        return h   

        