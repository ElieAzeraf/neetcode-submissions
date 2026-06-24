# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        actual_node = head
        for i in range(1000):
            if actual_node.next == None:
                return False
            
            actual_node = actual_node.next
        
        return True
        