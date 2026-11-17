class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        dict1 = {}
        for i in range(len(nums)):
            if target-nums[i] in dict1.keys():
                result.append(dict1[target-nums[i]])
                result.append(i)
                return result
            else:
                dict1[nums[i]] = i


            
        # for i in dict1.keys():
        #     if target-i in dict1.keys():
        #         result.append(dict1[i])
        #         result.append(dict1[target-i])
        #         print(result)