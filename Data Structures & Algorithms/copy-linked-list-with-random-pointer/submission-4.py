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
        old_new = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_new[curr] = copy
            curr = curr.next

        curr = head
        while curr:
          copy = old_new[curr]
          copy.next = old_new[curr.next]
          copy.random = old_new[curr.random]
          curr = curr.next     

        return old_new[head]   

