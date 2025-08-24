class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # for i in range(1, len(arr)-1):
        #     if arr[i] > arr[i+1]:
        #         index = i
        #         break
        #
        # return index

        n = len(arr)
        left, right, ans = 0, n-1, 0
        while left < right:
            mid = (left + right)//2
            if arr[mid] > arr[mid+1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans



arr = [0,1,0]
arr1 = [0,2,1,0]
arr2 = [0,10,5,2]
print(Solution().peakIndexInMountainArray(arr))
print(Solution().peakIndexInMountainArray(arr1))
print(Solution().peakIndexInMountainArray(arr2))
left, right, ans = 1, 5 - 2, 0
pass