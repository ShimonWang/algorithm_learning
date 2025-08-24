# import sys
# T = int(input())
# print(T)
#
# for i in range(T):
#     for line in sys.stdin:
#         a = line.split()
#
# import


# 法2
# ----------------------------------------------------------------------------------------------------------------------
'''
test data 注意复制最后一行换行符
2
4 2
1 2 3 3
3 1
2 6 8

'''
# T = int(input())
# print(f"T:{T}")
# for i in range(T):
#     n, m = list(map(int, input().split()))
#     # map_obj = map(int, input().split())
#     a = list(map(int, input().split()))
#     print(f"第{i + 1}组数据:")
#     # print(f"map_obj:{map_obj}")
#     print(f"n,m:{n},{m}")
#     print(f"a:{a}")
#
#     for i in range(1, len(a)):
#         if a[i] - a[i-1] <= m:
#             ans = 1
#             break
#         ans = -1
#     print(ans)
#
# T = int(input())
# for i in range(T):
#     n, m = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#
#     for i in range(1, len(a)):
#         if a[i] - a[i-1] < m:
#             ans = 1
#             break
#         ans = -1
#     print(ans)


# 参考解题 https://mp.weixin.qq.com/s/jmAiFN_JF6kKYhiSCw45lA
# ----------------------------------------------------------------------------------------------------------------------
import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    T = next(it, 0)
    out = []
    for _ in range(T):
        n = next(it)
        m = next(it)
        a = [next(it) for _ in range(n)]
        # 只需检查是否存在相邻差小于 m
        ans = -1
        for i in range(n - 1):
            if a[i + 1] - a[i] < m:
                ans = 1
                break
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
