class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     product = 1
    #     for num in nums:
    #         product *= num
    #     return self.signFunc(product)
    # def signFunc(self, product):
    #     if product < 0:
    #         return -1
    #     elif product == 0:
    #         return 0
    #     else:
    #         return 1

    # 官方解题
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign


solv = Solution()
nums1 = [-1,-2,-3,-4,3,2,1]
nums2 = [1,5,0,2,-3]
nums3 = [-1,1,-1,1,-1]
print(solv.arraySign(nums1))
print(solv.arraySign(nums2))
print(solv.arraySign(nums3))