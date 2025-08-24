# import sys
#
# for line in sys.stdin:
#     try:
#         a = line.split()
#         print(f"type(line):{type(line)},{line}")
#         print(f"type(a):{type(a)}, {a}")
#         if len(a) >= 2:
#             print(int(a[0]) + int(a[1]))
#         else:
#             print("每行必须输入超过两个数字")
#     except ValueError:
#         print("输入无效，无法转换为整数")


# 牛客官方
# ----------------------------------------------------------------------------------------------------------------------
# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


#
# ----------------------------------------------------------------------------------------------------------------------
# import sys
# # data = sys.stdin.read().strip().split()
# # print(f"sys.stdin:{sys.stdin}")
# # print(f"sys.stdin.read():{sys.stdin.read()}")
# # print(f"sys.stdin.read().strip():{sys.stdin.read().strip()}")
# # print(f"sys.stdin.read().strip().split():{sys.stdin.read().strip().split()}")
#
# data = """1 2
# 3 4"""
# print(f"sys.stdin:{data}")
# print(f"sys.stdin.read():{data.read()}")
# print(f"sys.stdin.read().strip():{sys.stdin.read().strip()}")
# print(f"sys.stdin.read().strip().split():{sys.stdin.read().strip().split()}")


# 通用输入模版
# ----------------------------------------------------------------------------------------------------------------------
'''
test data 注意复制最后一行换行符
2
4 2
1 2 3 3
3 1
2 6 8

'''
import sys


def read_ints():
    """读取一行并转为int列表"""
    return list(map(int, sys.stdin.readline().strip().split()))


def main():
    T = int(sys.stdin.readline().strip())  # 测试组数
    for case in range(1, T + 1):
        n, m = read_ints()  # 每组开头两个数
        a = read_ints()  # 长度为 n 的数组

        # 调试打印（写题时可删）
        print(f"Case {case}: n={n}, m={m}, a={a}")

        # TODO: 在这里写每组数据的处理逻辑
        # result = solve(n, m, a)
        # print(result)


if __name__ == "__main__":
    main()