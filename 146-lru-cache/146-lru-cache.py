class LRUCache:

    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.d.move_to_end(key)
            return
        if self.capacity == 0:
            self.d.popitem(last=False)
        else:
            self.capacity-=1
        self.d[key] = value
        self.d.move_to_end(key)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)