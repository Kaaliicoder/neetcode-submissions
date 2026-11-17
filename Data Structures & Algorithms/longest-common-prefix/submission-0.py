class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stop = 1
        result = ""
        leng = len(min(strs))
        dict1 = {}
        count = 0;
        for word in strs:
            if word not in dict1.keys():
                dict1[word] = 0
        if len(dict1) == 1:
            return dict1.keys()
        
     