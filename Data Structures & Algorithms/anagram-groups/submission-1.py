class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        
        result = []
        dict1 = {}
        for i in range(len(strs)):
            new_word = "".join(sorted(strs[i]))
            if new_word not in dict1.keys():
                dict1[new_word] = [strs[i]]
            else:
                dict1[new_word].append(strs[i])
        
        
        for word in dict1.values():
            result.append(word)

        return word
        