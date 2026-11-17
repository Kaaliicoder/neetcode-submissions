#In this case there are three different situations:
    # 1 when length is equals to 1 or 2 return false
    # 2 when you need remove a letter to make it valid
    # 3 when you don't need to remove anything from the string


class Solution:
    def validPalindrome(self, s: str) -> bool:

        if len(s) == 1 or len(s) == 2:
            return True




        test = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

        first = ""
        second = ""

        # new = len(s) - 1
        
        quit = 0
        skip = 0
        count = -1

        for i in range(0,len(s)):
            if s[i].lower() in test:
                first = first + s[i].lower()

        for i in range(0, len(s)):
            if s[count].lower() in test:
                second = second + s[count].lower()
            count = count - 1

        if first == second:
            return True

        count = -1
        first = ""
        second = ""


        while quit != 1:

            if len(s)>2:
                for i in range(0,len(s)):
                    if skip != i:
                        if s[i].lower() in test:
                            first = first + s[i].lower()
                
                for i in range(0,len(s)):
                    if skip<len(s):
                        if s[skip] != s[count]: # still issue in this if statement # the fucking problem is here in this condition of if statement
                            if s[count].lower() in test:
                                second = second + s[count].lower()
                        count = count - 1
            
            if first == second:
                return True
            
            skip = skip + 1
            first = ""
            second = ""
            count = -1
            if skip>len(s):
                quit = 1
            
        return False


            



