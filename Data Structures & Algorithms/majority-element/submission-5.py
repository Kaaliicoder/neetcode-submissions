class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        return nums[len(nums)//2]
        # size = len(nums)/2
        # count = 1
        # temp = nums[0]
        # result = 0
        # for i in range(1,len(nums)):
        #     if temp == nums[i]:
        #         count = count + 1
        #     elif temp != nums[i]:
        #         if count>size:
        #             result = temp
        #         temp = nums[i]
        #         count = 0
        
        # return result
