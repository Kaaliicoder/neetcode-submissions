class MyHashSet:

    def __init__(self):
        self.nums = []

    def add(self, key: int) -> None:
        if self.nums == []:
            self.nums.append(key)
        for number in self.nums:
            if number != key:
                self.nums.append(key)

    def remove(self, key: int) -> None:
        for number in self.nums:
            if number == key:
                self.nums.remove(key)

    def contains(self, key: int) -> bool:
        print()
        for number in self.nums:
            if number == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)