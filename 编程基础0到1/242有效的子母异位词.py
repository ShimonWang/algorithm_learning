from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s, t = sorted(s), sorted(t)
        # if s == t:
        #     return True
        # return False


        # 法2
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True
solv = Solution()

s = "anagram"
t = "nagaram"
# print(solv.isAnagram('hello', 'll'))
print(solv.isAnagram(s, t))