class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict1 = {}

        for number in nums:
            if number not in dict1.keys():
                dict1[number] = 1
            else:
                dict1[number] = dict1[number] + 1
        
        print(sorted(dict1)) 