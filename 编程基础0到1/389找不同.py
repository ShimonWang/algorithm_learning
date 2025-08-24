class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s = list(s)
        # t = list(t)
        # for str in s:
        #     # print(str)
        #     if str not in t:
        #         return str
        #     else:
        #         # print(t)
        #         t.remove(str)
        #     #     t.remove(item)
        # return ''.join(t)

        # # 法2：
        # dic = {}
        # for tt in t:
        #     if tt not in dic:
        #         dic[tt] = 1
        #     else:
        #         dic[tt] += 1
        # for ss in s:
        #     dic[ss] -= 1
        # for ch in dic:
        #     if dic[ch] == 1:
        #         return ch

        # 法3
        s, t = sorted(s) + [''], sorted(t)
        for c1,c2 in zip(s, t):
            if c1 != c2:
                return c2

        # 法4 求和法
        res = 0
        for i in t:
            res += ord(i)
        for j in s:
            res -= ord(j)
        return chr(res)

solv = Solution()
s = ""
t = "y"
print(solv.findTheDifference("abcd", "abcde"))
print(solv.findTheDifference(s, t))