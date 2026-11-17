# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        new = dummy

        while curr1 and curr2:
            if curr1.val < curr2.val:
                new.next = curr1
                new = new.next

                next_node = curr1.next
                curr1 = next_node
            
            else:
                new.next = curr2
                new = new.next

                next_node = curr2.next
                curr2 = next_node
        
        if curr1:
            new.next = curr1
        
        if curr2:
            new.next = curr2

        return dummy.next