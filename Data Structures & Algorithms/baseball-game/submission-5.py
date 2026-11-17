class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for index in range(len(operations)):
            op = operations[index]

            if op not in {"C", "D", "+"}:
                result.append(int(op))
            elif op == "+":
                result.append(result[-1] + result[-2])
            elif op == "C":
                result.pop()
            elif op == "D":
                result.append(2 * result[-1])

        return sum(result)
