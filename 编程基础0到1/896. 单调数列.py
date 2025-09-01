# class Solution(object):
#     def isMonotonic(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n = len(nums)
#
#         # if n <= 1:
#         #     return True
#         # else:
#         #     if nums[0] < nums[1]:
#         #         flag = -1
#         #     else:
#         #         flag = 1
#         #     for i in range(1, n):
#         #         if
#         if n <= 2:
#             return True
#         else:
#             for i in range(1, n-1):
#                 if nums[i-1] <= nums[i] <= nums[i+1]:
#                     # flag = 1
#                     continue
#                 else:
#                     # flag = 0
#                     return False
#             for i in range(1, n-1):
#                 if nums[i-1] >= nums[i] >= nums[i+1]:
#                     # flag = 1
#                     continue
#                 else:
#                     # flag = 0
#                     return False
#             return True


# 题解1 https://leetcode.cn/problems/monotonic-array/solutions/625294/liang-ci-bian-li-yu-yi-ci-bian-li-by-fux-qvw0/
# ----------------------------------------------------------------------------------------------------------------------
class Solution():
    def isMonotonic(self, A):
        return self.isIncreasing(A) or self.isDecreasing(A)

    def isIncreasing(self, A):
        N = len(A)
        for i in range(N-1):
            if A[i+1]-A[i] < 0:
                return False
        return True

    def isDecreasing(self, A):
        N = len(A)
        for i in range(N-1):
            if A[i+1]-A[i] > 0:
                return False
        return True


# 题解2
# 作者：负雪明烛
# 链接：https://leetcode.cn/problems/monotonic-array/solutions/625294/liang-ci-bian-li-yu-yi-ci-bian-li-by-fux-qvw0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# ----------------------------------------------------------------------------------------------------------------------
class Solution:
    def isMonotonic(self, A):
        N = len(A)
        inc, dec = True, True
        for i in range(1, N):
            if A[i] < A[i - 1]:
                inc = False
            if A[i] > A[i - 1]:
                dec = False
            if not inc and not dec:
                return False
        return True


solv = Solution()
nums = [1,2,2,3]
print(solv.isMonotonic(nums))
nums = [6,5,4,4]
print(solv.isMonotonic(nums))
nums = [1,3,2]
print(solv.isMonotonic(nums))
