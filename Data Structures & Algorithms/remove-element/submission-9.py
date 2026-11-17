class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                count=count+1
        for ii in range(0,len(nums)):
            for i in range(0,len(nums)):
                if i+1<len(nums): 
                    if nums[i] == val:
                        temp = nums[i+1]
                        nums[i+1] = nums[i]
                        nums[i] = temp
        print(nums,count)
        return count