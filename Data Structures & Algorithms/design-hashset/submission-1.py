class MyHashSet:

    def __init__(self):
        self.nums = []

    def add(self, key: int) -> None:
        for number in self.nums:
            if number != key:
                self.nums.append(key)

    def remove(self, key: int) -> None:
        flag = 0
        for number in self.nums:
            if number == key:
                flag = 1
        if flag == 1:
            self.nums.remove(key)

    def contains(self, key: int) -> bool:
        for number in self.nums:
            if number == key:
                return true
        return false


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)