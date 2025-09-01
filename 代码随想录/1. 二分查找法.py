# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         left = 0
#         right = len(nums)
#         while left < right:
#             middle = (left + right) // 2
#             if nums[middle] < target:
#                  left = middle + 1
#             elif nums[middle] > target:
#                 right = middle
#             else:
#                 return middle
#         return -1
# ----------------------------------------------------------------------------------------------------------------------

# 代码随想录
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)  # 定义target在左闭右开的区间里，即：[left, right)

        while left < right:  # 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle  # target 在左区间，在[left, middle)中
            elif nums[middle] < target:
                left = middle + 1  # target 在右区间，在[middle + 1, right)中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值
# ----------------------------------------------------------------------------------------------------------------------

# 测试样例
# ----------------------------------------------------------------------------------------------------------------------
solv = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(solv.search(nums, target))
nums = [-1,0,3,5,9,12]
target = 2
print(solv.search(nums, target))
