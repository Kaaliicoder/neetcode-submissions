class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = ""
        test = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9]
        for i in s:
            if i in test:
                first = first + i.lower()
        
        second = ""
        count = -1
        for i in range(0, len(s)):
            if s[count] in test:
                second = second + s[count].lower()
            count = count - 1

        print(second)
        print(" \n")
        print(first)
        if second == first:
            return True
        return False
