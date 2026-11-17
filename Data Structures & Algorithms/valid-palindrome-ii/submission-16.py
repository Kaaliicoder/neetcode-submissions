class Solution:
    def validPalindrome(self, s: str) -> bool:
        test = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

        first = ""
        second = ""

        # new = len(s) - 1
        
        quit = 0
        skip = 0
        count = -1
        while quit != 1:

            if len(s)>2:
                for i in range(0,len(s)):
                    if skip != i:
                        if s[i].lower() in test:
                            first = first + s[i].lower()
                
                for i in range(0,len(s)):
                    if skip<len(s):
                        if s[skip] != s[count]: # Solved # the fucking problem is here in this condition of if statement
                            if s[count].lower() in test:
                                second = second + s[count].lower()
                        count = count - 1
            elif len(s) == 1:
                return True
            elif len(s) == 2:
                return True
            if first == second:
                return True
            
            skip = skip + 1
            first = ""
            second = ""
            count = -1
            if skip>len(s):
                quit = 1
            
        return False


            



