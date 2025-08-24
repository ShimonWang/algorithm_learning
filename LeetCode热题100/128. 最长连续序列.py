class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_sorted = sorted(set(nums))
        for i in range(len(nums_sorted)-1):
            if nums_sorted[i+1] - nums_sorted[i] > 1:
                return i+1
        return len(nums_sorted)


sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([1,0,1,2]))