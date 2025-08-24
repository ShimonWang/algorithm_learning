class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonzeros = []
        zeros_num = 0
        for num in nums:
            if num:
                nonzeros.append(num)
            else:
                zeros_num += 1
        return nonzeros + [0] * zeros_num

solv = Solution()
nums1 = [0,1,0,3,12]
nums2 = [0]
print(solv.moveZeroes(nums1))
print(solv.moveZeroes(nums2))