class Solution: # using Stack data structure
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i.lstrip("-").isdigit():
                record.append(int(i))
            elif i == '+':
                record.append(record[-1] + record[-2])
            elif i == 'D':
                record.append(record[-1] * 2)
            else:
                record.pop()

        return sum(record)