class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result= []
        for number in nums:
            if number != val:
                result.append(int(number))
        return len(result)