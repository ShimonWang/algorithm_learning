class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # newword = ''
        # i = 0
        # while i <= min(len(word1), len(word2)) - 1:
        #     newword = newword + word1[i] + word2[i]
        #     i = i + 1
        #
        # newword = newword + word1[i:] + word2[i:]
        # return newword
        #
        newword = list()
        i = 0
        while i <= min(len(word1), len(word2)) - 1:
            newword.append(word1[i]+ word2[i])
            i = i + 1

        newword.append(word1[i:] + word2[i:])
        return "".join(newword)
# word1 = "abc"
# word2 = "pqr"

# word1 = "ab"
# word2 = "pqrs"

word1 = "abcd"
word2 = "pq"
print(word1.find(word1))

sol = Solution()
print(sol.mergeAlternately(word1, word2))