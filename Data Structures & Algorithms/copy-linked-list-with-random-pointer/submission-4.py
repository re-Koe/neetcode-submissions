"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapy = {None:None} # {actual linked list : copy}

        curr = head
        while curr: # [pointer to values]
            copy = Node(curr.val)
            mapy[curr] = copy
            curr = curr.next

        curr2 = head

        while curr2:
            copy = mapy[curr2]
            copy.next = mapy[curr2.next]
            copy.random = mapy[curr2.random]
            curr2 = curr2.next
        return mapy[head]