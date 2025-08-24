class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        # count = 0
        # print(words[left:right+1])
        # for word in words[left:right+1]:
        #     if word[0].lower() in 'aeiou' and word[-1].lower() in 'aeiou':
        #         count = count + 1
        #
        # return count

        count = 0
        print(words[left:right+1])
        for word in words[left:right+1]:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                count = count + 1

        return count


words = ["are", "amy", "u"]
left = 0
right = 2
sol = Solution()
print(sol.vowelStrings(words, left, right))
