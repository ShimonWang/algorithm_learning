class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # 暴力求解，超出时间限制
        # count = 0
        # for i in range(low, high+1):
        #     if i % 2 == 1:
        #         count += 1
        # return count

        # # 法2
        # if low % 2 == 0:
        #     low += 1
        # if high % 2 == 0:
        #     high -= 1
        # return (high - low) // 2 + 1

        # 官方解题
        pre = lambda x: (x + 1) >> 1  # 位运算符 等价于 f(x) = (x + 1) // 2，表示从1到x的奇数个数
        return pre(high) - pre(low - 1)

solv = Solution()
low = 3
high = 7
print(solv.countOdds(low, high))

low = 8
high = 10
print(solv.countOdds(low, high))