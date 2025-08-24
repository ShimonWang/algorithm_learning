import time

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        start = time.time()
        # arr.sort()
        # diff = arr[1] - arr[0]
        # for i in range(2, len(arr)):
        #     if arr[i] - arr[i-1] != diff:
        #         return False
        # return True

        # 官方解题
        arr.sort()
        for i in range(1, len(arr) -1):
            if arr[i] * 2 != arr[i - 1] + arr[i + 1]:
                return False
        return True

        print()
solv = Solution()
arr1 = [3,5,1]
arr2 = [1,2,4]
print(solv.canMakeArithmeticProgression(arr1))
print(solv.canMakeArithmeticProgression(arr2))