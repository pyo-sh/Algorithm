class MyHashSet:

    def __init__(self):
        self.hash = set()

    def add(self, key):
        self.hash.add(key)

    def remove(self, key):
        if self.contains(key):
            self.hash.discard(key)

    def contains(self, key):
        return key in self.hash


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)