class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
         
        dict1 = {}
        for i in range(len(strs)):
            new_word = "".join(sorted(strs[i]))
            if new_word not in dict1.keys():
                dict1[new_word] = [strs[i]]
            else:
                dict1[new_word].append(strs[i])
        
        return dict1.values()
        

        