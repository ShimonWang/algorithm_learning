class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # nums_shuffle = [0]*2*n
        nums_shuffle = nums[:]
        print(id(nums_shuffle))
        print(id(nums))
        for i in range(n):
            nums_shuffle[2*i] = nums[i]
            nums_shuffle[2*i+1] = nums[i+n]

        return nums_shuffle
nums = [2,5,1,3,4,7]
n= 3
print(Solution().shuffle(nums, n))