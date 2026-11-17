class MyHashMap:

    def __init__(self):
        self.nums = []

    def put(self, key: int, value: int) -> None:
        x = [key, value]
        found = 0 
        for number in self.nums:
            if key == number[0]:
                number[1] = value
                found = 1
        if found == 0:
            self.nums.append(x)

    def get(self, key: int) -> int:
        found = 0
        for number in self.nums:
            if key == number[0]:
                found = 1
                return number[1]
        if found == 0:
            return -1

    def remove(self, key: int) -> None:
        for number in self.nums:
            if key == number[0]:
                self.nums.remove(number)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)