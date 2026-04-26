# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        curr, curr2 = list1, list2
        dummy = node = ListNode()

        while curr and curr2:
            if curr.val < curr2.val:
                node.next = curr
                curr = curr.next
            else:
                node.next = curr2
                curr2 = curr2.next
            node = node.next
        
        if curr:
            node.next = curr
        if curr2:
            node.next = curr2
        return dummy.next
