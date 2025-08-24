# n = int(input())
# nums = list(map(int, input().split()))
#
# print(n)
# print(nums)
#
# nums.sort()
# print(nums)
# result = []
# # def mid(nums, n):
# def mid(nums):
#     if len(nums) == 1:
#         index = 0
#         mid_x = nums[index]
#     elif len(nums) % 2 == 1:
#         #return nums[nums//2]
#         #result.append(nums[nums//2])
#         index = len(nums) // 2
#         mid_x = nums[index]
#     elif len(nums) % 2 == 0:
#         index = len(nums) // 2 - 1
#         if nums[index] > nums[index+1]:
#             index = index + 1
#         mid_x = nums[index]
#     nums.pop(index)
#     return nums, mid_x
#
# while len(nums) > 0:
#     nums, mid_x = mid(nums)
#     result.append(mid_x)
#
# for num in result:
#     print(num, end=" ")
# # print(result)
# # print(mid(nums, n))


# def mid(nums):
#     if len(nums) == 1:
#         index = 0
#         mid_x = nums[index]
#     elif len(nums) % 2 == 1:
#         index = len(nums) // 2
#         mid_x = nums[index]
#     elif len(nums) % 2 == 0:
#         index = len(nums) // 2 - 1
#         # if nums[index] > nums[index+1]:
#         #     index = index + 1
#         mid_x = nums[index]
#     nums.pop(index)
#     return nums, mid_x
#
# n = int(input())
# nums = list(map(int, input().split()))
#
# nums.sort()
# result = []
#
# while len(nums) > 0:
#     nums, mid_x = mid(nums)
#     print(mid_x, end=" ")
#     # result.append(mid_x)
#
# # for num in result:
# #     print(num, end=" ")

# # 暴力搜索 GPT 16/20 未通过
# def median_sequence(arr):
#     res = []
#     arr.sort()
#     while arr:
#         n = len(arr)
#         if n % 2 == 1:
#             mid = arr[n//2]
#         else:
#             mid = arr[n//2-1]
#         res.append(mid)
#         arr.remove(mid)
#     return res
#
# n = int(input())
# arr = list(map(int, input().split()))
# result = median_sequence(arr)
# for num in result:
#     print(num, end=' ')

import heapq

def median_sequence(arr):
    max_heap = []  # 大根堆（用负数存储）
    min_heap = []  # 小根堆
    res = []

    for num in arr:
        # 先往大根堆放
        heapq.heappush(max_heap, -num)
        # 平衡：保证大根堆最大 <= 小根堆最小
        if min_heap and -max_heap[0] > min_heap[0]:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)

        # 平衡大小
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    n = len(arr)
    for _ in range(n):
        if (len(max_heap) + len(min_heap)) % 2 == 1:
            mid = -max_heap[0]   # 奇数长度
        else:
            mid = min(-max_heap[0], min_heap[0])  # 偶数长度

        res.append(mid)

        # 删除中位数
        if mid == -max_heap[0]:
            heapq.heappop(max_heap)
        else:
            heapq.heappop(min_heap)

        # 重新平衡
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    return res

n = int(input())
arr = list(map(int, input().split()))
result = median_sequence(arr)
for num in result:
    print(num, end=' ')