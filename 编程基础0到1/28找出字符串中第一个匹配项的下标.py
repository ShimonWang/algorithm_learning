class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(len(haystack) - len(needle) + 1)
        for i in range(len(haystack) - len(needle) + 1):
            print(i)
            print(haystack[i:i+len(needle)])
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1

solv = Solution()
# print(solv.strStr('hello', 'll'))
print(solv.strStr('hello', 'le'))