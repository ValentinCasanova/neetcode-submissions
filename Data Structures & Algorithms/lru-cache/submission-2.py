class ListNode:
    def __init__(self, prev=None, next=None, val=0):
        self.prev = prev
        self.next = next
        self.val = val

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def pop(self):
        tail = self.tail.prev
        self.tail.prev = tail.prev
        self.tail.prev.next = self.tail
        tail.next = None
        tail.prev = None
        return tail.val
    
    def prepend(self, val):
        cur_head = self.head.next
        new_node = ListNode(next=self.head, val=val)
        if not cur_head:
            self.head.next = new_node
        else:
            cur_head.prev = new_node
            new_node.next = cur_head
            self.head.next = new_node
        new_node.prev = self.head
        return new_node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        if prev:
            prev.next = node.next
        if next:
            next.prev = node.prev
        node.next = None
        node.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.kv_map = {}
        self.key_node = {}
        self.linked_list = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.kv_map:
            self.linked_list.remove(self.key_node[key])
            self.key_node[key] = self.linked_list.prepend(key)
            return self.kv_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            self.linked_list.remove(self.key_node[key])
        elif len(self.kv_map) == self.capacity:
            node_val = self.linked_list.pop()
            self.kv_map.pop(node_val)
            

        self.key_node[key] = self.linked_list.prepend(key)
        self.kv_map[key] = value
        
