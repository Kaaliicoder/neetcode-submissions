class Solution:
    def reverseString(self, s: List[str]) -> None:
        result = []
        count = -1
        for i in range(0, len(s)):
            result.append(s[count])
            count = count - 1
        s = result