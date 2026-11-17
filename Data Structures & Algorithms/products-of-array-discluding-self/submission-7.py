class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [1] * len(nums)
        arr2 = [1] * len(nums)
        result = [1] * len(nums)
        prefix = 1
        suffix = 1
        n = len(nums)-1
        for i in range(len(nums)):
            arr1[i] = prefix
            prefix  *= nums[i]
        
            arr2[n-i] = suffix
            suffix *= nums[n-i]

            result[i] = arr1[i]*arr2[i]
        return result 