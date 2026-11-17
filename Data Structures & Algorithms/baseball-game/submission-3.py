class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for index in range(len(operations)):
            if operations[index] not in {"C", "D", "+"}:                
                result.append(int(operations[index]))
                # print(result,operations[index])
            elif operations[index] == "+":
                result.append(operations[index-1]+operations[index-2])
            elif operations[index] == "C":
                result.remove(result[-1])
            elif operations[index] == "D":
                result.append(2*int(operations[index-1]))
        print(result)
        return sum(result)

