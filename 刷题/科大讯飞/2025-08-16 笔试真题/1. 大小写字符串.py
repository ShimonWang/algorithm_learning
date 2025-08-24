# n, k = tuple(map(int, input().split()))
# s = str(input())
# # print(n, k)
# # print(s)
#
# u = 0
# for i in s:
#     if 'A' <= i <= 'Z':
#         u +=1
# l = n - u
#
# if k <= l:
#     number = u + k
# elif (k - l) % 2 == 1:
#     number = n - 1
# else:
#     number = n
#
# print(number)

# 参考代码
# ----------------------------------------------------------------------------------------------------------------------
import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        # return data
        return
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    U = sum(1 for c in s if 'A' <= c <= 'Z')  # 初始大写数量
    L = n - U  # 初始小写数量

    if k <= L:
      ans = U + k  # 直接翻 k 个小写
    else:
      r = k - L  # 剩余步数
      ans = n if r % 2 == 0 else n - 1  # 看奇偶决定是否损失 1

    print(ans)

if __name__ == "__main__":
 return_code = main()
