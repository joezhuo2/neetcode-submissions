class MyHashMap:
    def __init__(self):
        self.bucket = []

    def put(self, key: int, value: int) -> None:
        for pair in self.bucket:
            if pair[0] == key:
                pair[1] = value
                return
        self.bucket.append([key, value])

    def get(self, key: int) -> int:
        for pair in self.bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        for i, pair in enumerate(self.bucket):
            if pair[0] == key:
                del self.bucket[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)