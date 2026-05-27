class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
       self.cache = {}
       self.cap = capacity
       self.left, self.right = Node(0,0) , Node(0,0)
       self.left.next = self.right
       self.right.prev = self.left

    def remove(self, node):
        previous = node.prev
        nextNode = node.next
        previous.next = nextNode
        nextNode.prev = previous

    def insert(self, node):  
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] =  Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
       