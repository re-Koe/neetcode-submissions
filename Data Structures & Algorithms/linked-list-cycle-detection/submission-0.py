# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        aset = set()
        
        curr = head
        while curr:
            if curr in aset:
                return True
            aset.add(curr)
            curr = curr.next
        
        return False