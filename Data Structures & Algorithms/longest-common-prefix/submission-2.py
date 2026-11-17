class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = strs[0]
        j = len(strs[0])

        for i in range(1,len(strs)):
            while j>0 and result[:j] != strs[i][:j]:
                j = j -1
            result = result[:j]
        
        return result
        
