class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = ""
        for i in s:
            if i != " ":
                first = first + i

        second = ""
        count = -1
        for i in range(0, len(s)):
            if s[count] != " ":
                second = second + s[count]
            count = count - 1

        if second == first:
            return True
        return False
