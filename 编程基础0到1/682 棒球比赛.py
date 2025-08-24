class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # score = []
        # for i in range(len(operations)):
        #     if operations[i] == "+":
        #         # score.append(operations[i-1] + (operations[i-2]))
        #         score.append(score[-1] + score[-2])
        #     elif operations[i] == "D":
        #         # score += 2 * operations[i-1]
        #         # score.append(2 * operations[i-1])
        #         score.append(2 * score[-1])
        #     elif operations[i] == "C":
        #         # score[-1] = []
        #         del score[-1]
        #     else:
        #         # score.append(operations[i])
        #         score.append(int(operations[i]))
        # # return score
        # return sum(score)

        # 题解1
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)

solv = Solution()
ops = ["5","2","C","D","+"]
out = 30
print(solv.calPoints(ops))
assert solv.calPoints(ops) == out

ops = ["5","-2","4","C","D","9","+","+"]
out = 27
print(solv.calPoints(ops))
assert solv.calPoints(ops) == out

ops = ["1"]
out = 1
print(solv.calPoints(ops))
assert solv.calPoints(ops) == out

