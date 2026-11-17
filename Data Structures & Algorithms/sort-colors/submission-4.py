class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        var1 = var2 = var0 = 0
        count = 0
        for number in nums:
            if number==0:
                var0 = var0 + 1
            elif number==1:
                var1 = var1 + 1
            else:
                var2 = var2 + 1

        for index in range(len(nums)):
            if var0 != 0 and var1>=0 and var2>=0:
                nums[index] = 0
                var0 = var0 - 1
            elif var0 == 0 and var1!=0 and var2>=0:
                nums[index] = 1
                var1 = var1 -1
            elif var0 == 0 and var1==0 and var2!=0:
                nums[index] = 2
                var2 = var2 -1





        