# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         slow = 0
#         n = len(nums)
#         for fast in range(n):
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#         return slow
# ----------------------------------------------------------------------------------------------------------------------

# 代码随想录 暴力法（参考）
# ----------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        # for i in range(n):
        while i < n:
            if nums[i] == val:
                for j in range(i+1, n):
                    nums[j-1] = nums[j]
                n -= 1
                i -= 1
            i += 1
        return n
# ----------------------------------------------------------------------------------------------------------------------

# 测试样例
# ----------------------------------------------------------------------------------------------------------------------
sol = Solution()
nums = [3,2,2,3]
val = 3
print(sol.removeElement(nums, val))
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))
