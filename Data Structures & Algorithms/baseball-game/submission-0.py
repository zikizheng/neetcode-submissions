class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for operation in operations:
            if operation == '+':
                rec.append(rec[-2] + rec[-1])
            elif operation == 'C':
                rec.pop()
            elif operation == 'D':
                rec.append(2 * rec[-1])
            else:
                rec.append(int(operation))
        return sum(rec)