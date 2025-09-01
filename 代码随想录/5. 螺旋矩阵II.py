# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         start_x, start_y = 0, 0
#         offset = 1
#         count = 1
#         nums = [[0]*n for _ in range(n)]
#         loop = n // 2
#         while loop:
#             for j in range(start_y, n-offset):
#                 nums[start_x][j] = count
#                 count += 1
#             for i in range(start_x, n-offset):
#                 # nums[i][n-offset-1] = count
#                 nums[i][n-offset] = count
#                 count += 1
#             for j in range(n-offset, start_y, -1):
#                 # nums[n-offset-1][j] = count
#                 nums[n-offset][j] = count
#                 count += 1
#             for i in range(n-offset, start_x, -1):
#                 # nums[i][n-offset-1] = count
#                 nums[i][start_y] = count
#                 count += 1
#             start_x += 1
#             start_y += 1
#             offset += 1
#             loop -= 1
#         if n % 2 == 1:
#             nums[n//2][n//2] = count
#         return nums

# ----------------------------------------------------------------------------------------------------------------------

# 代码随想录
# ----------------------------------------------------------------------------------------------------------------------
# （版本一）滑动窗口法
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0               # 起始点
        loop, mid = n // 2, n // 2          # 迭代次数、n为奇数时，矩阵的中心点
        count = 1                           # 计数

        for offset in range(1, loop + 1) :      # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset) :    # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums

# ----------------------------------------------------------------------------------------------------------------------

# 测试样例
# ----------------------------------------------------------------------------------------------------------------------
sol = Solution()
n = 3
print(sol.generateMatrix(n))
n = 1
print(sol.generateMatrix(n))
