class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        x=0
        for i in nums:
            if i not in dicti.keys():
                dicti[i] = 0
            else:
                return True

        return False