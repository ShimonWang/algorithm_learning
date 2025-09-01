"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

"""

# ----------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # i, result = 0, len(nums)
        # sum = 0
        # for j in range(result):
        #     sum += nums[j]
        #     while sum >= target:
        #         sub_l = j - i + 1
        #         result = min(result, sub_l)
        #         sum = sum - nums[i]
        #         i += 1
        # return result if sum >= target else -1

        l = len(nums)
        i = 0
        j = 0
        min_l = float('inf')
        sum = 0
        while j < l:
            sum += nums[j]
            while sum >= target:
                sub_l = j - i + 1
                min_l = min(min_l, sub_l)
                sum = sum - nums[i]
                i += 1
            j += 1
        return min_l if min_l != float('inf') else 0
# ----------------------------------------------------------------------------------------------------------------------

# 代码随想录
# ----------------------------------------------------------------------------------------------------------------------
# （版本一）滑动窗口法
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         l = len(nums)
#         left = 0
#         right = 0
#         min_len = float('inf')
#         cur_sum = 0  # 当前的累加值
#
#         while right < l:
#             cur_sum += nums[right]
#
#             while cur_sum >= s:  # 当前累加值大于目标值
#                 min_len = min(min_len, right - left + 1)
#                 cur_sum -= nums[left]
#                 left += 1
#
#             right += 1
#
#         return min_len if min_len != float('inf') else 0

# ----------------------------------------------------------------------------------------------------------------------

# 测试样例
# ----------------------------------------------------------------------------------------------------------------------
sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(sol.minSubArrayLen(target, nums))
target = 11
nums = [1,1,1,1,1,1,1,1]
print(sol.minSubArrayLen(target, nums))
