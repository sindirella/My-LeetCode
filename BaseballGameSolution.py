class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        arr = []
        for op in operations:
            if op == "+":
                arr.append(arr[-1] + arr[-2])
            elif op == "D":
                arr.append(2* arr[-1])
            elif op == "C":
                arr.pop()
            else:
                arr.append(int(op))
        return sum(arr)