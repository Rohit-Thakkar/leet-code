class MyHashMap:
    def __init__(self):
        self.data = {}
    def put(self, key: int, val: int) -> None:
        self.data[key] = val
    def get(self, key: int) -> int:
        return self.data.get(key, -1)
    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key]
