class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            for x in range(1,len(nums)):
                if x != i:
                    if nums[i] + nums[x] == target:
                        result.append(i)
                        result.append(x)
                        return result
