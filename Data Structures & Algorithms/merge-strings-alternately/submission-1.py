class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        indexCount = 0
        for i in range(0, (len(word1)*2) - 1):
            if i % 2 == 0:
                a.append(word1[indexCount])
                indexCount += 1
            else:
                a.append(" ")
        print(a)
        
        indexCount = 0
        for i in range(0, len(a)):
            if a[i] == " ":
                a[i] = word2[indexCount]
                indexCount += 1
        
        for i in range(indexCount, len(word2)):
            a.append(word2[i])

        print(a)

        result= "".join(a)
        print(result)
        return result