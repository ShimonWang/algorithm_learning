class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        for i, str in enumerate(strs):
            str_new = sorted(str)
        out = sorted(strs)
        return out
        pass


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))