class Solution:
    def maxScore(self, s: str) -> int:
        # 法1
        # sum = 0
        # print(list(range(1, len(s))))
        # for i in range(1, len(s)):
        #     sum1 = 0
        #     sum2 = 0
        #     print(s[:i])
        #     for str in s[:i]:
        #         if str == '0':
        #             sum1 = sum1 + 1
        #     print(s[i:])
        #     for str in s[i:]:
        #         if str == '1':
        #             sum2 = sum2 + 1
        #
        #     if sum < sum1 + sum2:
        #         sum = sum1 + sum2
        #
        # return sum

        # 法2
        # return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))

        # 法3
        ans = score =(s[0] == '0') + s[1:].count('1')
        for c in s[1:-1]:
            score += 1 if c == '0' else -1
            ans = max(ans, score)

        return ans

s = "011101"
s1 = "00111"
s2 = "1111"
print(Solution().maxScore(s))
print(Solution().maxScore(s1))
print(Solution().maxScore(s2))
