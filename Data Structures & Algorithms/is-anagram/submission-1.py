class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):
            return False
        
        for i,j in zip(s,t):
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] + 1

        
            if j not in dict2.keys():
                dict2[j] = 1
            else:
                dict2[j] = dict2[j] + 1
        
        if dict1 == dict2:
            return True
        
        return False

