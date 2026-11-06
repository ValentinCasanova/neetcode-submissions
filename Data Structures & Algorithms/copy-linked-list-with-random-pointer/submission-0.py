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
        list1_map = {}
        list2_list = []
        cur = head
        i = 0
        while cur:
            list1_map[cur] = i
            i += 1
            cur = cur.next

        sentinel = Node(5)
        new_head = sentinel
        cur = head
        while cur:
            new_head.next = Node(cur.val)
            new_head = new_head.next
            cur = cur.next
        
        cur = sentinel.next
        while cur:
            list2_list.append(cur)
            cur = cur.next
        
        cur = head
        new_head = sentinel.next
        while cur:
            if cur.random:
                new_head.random = list2_list[list1_map[cur.random]]
            cur = cur.next
            new_head = new_head.next

        return sentinel.next
            
        
