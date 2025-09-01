class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat[0])
        # ans = 0
        if n % 2 == 1:
            ans = self.primary_diagonal_sum(mat) + self.secondary_diagonal_sum(mat) - mat[n//2][n//2]
        else:
            ans = self.primary_diagonal_sum(mat) + self.secondary_diagonal_sum(mat)
        return ans

    def primary_diagonal_sum(self, mat):
        sum = 0
        n = len(mat[0])
        for i in range(n):
            sum = sum + mat[i][i]
        return sum

    def secondary_diagonal_sum(self, mat):
        sum = 0
        n = len(mat[0])
        for i in range(n):
            sum = sum + mat[i][n-i-1]
        return sum


solv = Solution()
mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
print(solv.diagonalSum(mat))
mat = [[5]]
print(solv.diagonalSum(mat))
