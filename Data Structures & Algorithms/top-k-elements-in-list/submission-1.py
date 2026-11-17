class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = {}
        for index in range(len(nums)):
            if nums[index] not in dict1.keys():
                dict1[nums[index]] = [index, 1]
            else:
                x = dict1[nums[index]][1] + 1
                dict1[nums[index]] = [index, x]

        values = list(dict1.values())
        print(values)
        # for index in range(len(values)):
        #     for index1 in range(1,len(values)):
                
        #         if values[index1][1] > values[index][1]:
        #             temp = values[index]
        #             values[index] = values[index1]
        #             values[index1] = temp
        #         elif values[index][1] > values[index1][1]:
        #             temp = values[index1]
        #             values[index1] = values[index]
        #             values[index] = temp
        for index in range(len(values)):
            for index1 in range(index + 1, len(values)):   # <-- start from index+1
                if values[index1][1] > values[index][1]:   # swap if index1 is bigger
                    temp = values[index]
                    values[index] = values[index1]
                    values[index1] = temp
        
        print(values)
        result = []
        for i in range(k):
            result.append(nums[values[i][0]])

        return result
        